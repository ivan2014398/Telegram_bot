import sqlite3
from typing import List

conn = sqlite3.connect('utils/repository/weatherBot.db',
                       check_same_thread=False)
cursor = conn.cursor()


def create_user(tg_user_id: int, username: str) -> bool:
    try:
        cursor.execute("insert into users (tg_user_id, username) values (?, ?)",
                       (tg_user_id, username))
        conn.commit()
        return True

    except sqlite3.Error:
        return False


def create_subscribe(tg_user_id: int) -> bool:
    try:
        user_id = cursor.execute("select id from Users where tg_user_id = ?", (tg_user_id, )).fetchone()
        cursor.execute("insert into Subscribes (user_id) values (?)", (user_id[0], ))
        conn.commit()
        return True

    except sqlite3.Error:
        return False


def delete_subscribe(tg_user_id: int) -> bool:
    try:
        user_id = cursor.execute("select id from Users where tg_user_id = ?", (tg_user_id,)).fetchone()
        cursor.execute("delete from Subscribes where user_id = ?", (user_id[0],))
        conn.commit()
        return True

    except sqlite3.Error:
        return False


def get_subscribes() -> List[int]:
    subscribes = cursor.execute("select user_id from Subscribes").fetchall()
    list_user_id = [i[0] for i in subscribes]
    return list_user_id


def init_db():
    with open("utils/repository/schema.sql", "r") as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_exists():
    table_exists = cursor.execute("select 1 from sqlite_master").fetchall()
    if not table_exists:
        init_db()


check_db_exists()
