import sqlite3
import streamlit as st
from pathlib import Path

_DB_PATH = str(Path(__file__).parent.parent.parent / "data.db")


def _get_connection():
    # BUG FIX: Do NOT cache the connection with @st.cache_resource
    # Cached connections go stale across reruns and swallow write errors silently.
    # Always open a fresh connection; SQLite is lightweight enough for this.
    conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")   # allows concurrent reads during writes
    conn.execute("PRAGMA foreign_keys=ON")    # BUG FIX: enforce FK so bad user_id fails loudly
    return conn


def init_db() -> None:
    conn = _get_connection()

    with conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                username   TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS exercises (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id       INTEGER NOT NULL REFERENCES users(id),
                exercise_name TEXT    NOT NULL,
                reps          INTEGER NOT NULL DEFAULT 0,
                sets          INTEGER NOT NULL DEFAULT 0,
                time          REAL    NOT NULL DEFAULT 0,
                created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def get_user(username):
    conn = _get_connection()
    return conn.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    ).fetchone()


def create_user(username: str) -> sqlite3.Row:
    conn = _get_connection()
    with conn:
        conn.execute(
            "INSERT INTO users (username) VALUES (?)",
            (username,)
        )
    return get_user(username)


def get_or_create_user(username):
    user = get_user(username)
    if user is None:
        user = create_user(username)
    return user


def add_exercise(user_id, exercise_name, reps, sets, time):
    # BUG FIX: Guard against invalid user_id before hitting DB
    if not user_id or user_id == 0:
        st.warning("⚠️ Cannot save workout: user_id is not set in session state.")
        return

    conn = _get_connection()

    try:
        with conn:
            existing = conn.execute(
                """
                SELECT * FROM exercises
                WHERE user_id = ?
                AND exercise_name = ?
                AND DATE(created_at) = DATE('now')
                """,
                (user_id, exercise_name)
            ).fetchone()

            if existing:
                conn.execute(
                    """
                    UPDATE exercises
                    SET reps = reps + ?,
                        sets = sets + ?,
                        time = time + ?
                    WHERE id = ?
                    """,
                    (reps, sets, time, existing["id"])
                )
            else:
                # BUG FIX: Column order in INSERT matched to VALUES order (reps before sets)
                conn.execute(
                    """
                    INSERT INTO exercises (
                        user_id,
                        exercise_name,
                        reps,
                        sets,
                        time
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (user_id, exercise_name, reps, sets, time)
                )
    except Exception as e:
        st.warning(f"⚠️ Failed to save exercise to DB: {e}")


def get_users_exercises(user_id):
    if not user_id or user_id == 0:
        return []
    conn = _get_connection()
    return conn.execute(
        "SELECT * FROM exercises WHERE user_id = ? ORDER BY created_at DESC",
        (user_id,)
    ).fetchall()