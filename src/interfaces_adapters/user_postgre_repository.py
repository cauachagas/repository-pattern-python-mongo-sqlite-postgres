from uuid import UUID

import psycopg

from domain.user import User
from domain.user_repository import UserRepository


class UserPostgreRepository(UserRepository):
    def __init__(self, uri: str):
        self.__uri = uri
        self.__create_table()

    def __create_table(self):
        with psycopg.connect(self.__uri) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id UUID,
                    name TEXT,
                    email TEXT,
                    CONSTRAINT users_pk PRIMARY KEY (id)
                )
            """)

    def add_user(self, user: User):
        with psycopg.connect(self.__uri) as conn:
            conn.execute(
                "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)",
                (user.id, user.name, user.email),
            )

    def get_user(self, id: UUID) -> User | None:
        with psycopg.connect(self.__uri) as conn:
            row = conn.execute(
                "SELECT id, name, email FROM users WHERE id = %s", (id,)
            ).fetchone()
            if isinstance(row, tuple):
                return User(*row)
            return None

    def delete_user(self, id: UUID):
        with psycopg.connect(self.__uri) as conn:
            conn.execute("DELETE FROM users WHERE id = %s", (id,))
