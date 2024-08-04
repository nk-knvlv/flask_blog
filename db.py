from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]


class Base(DeclarativeBase):
    pass


class DB:
    def __init__(self, db_uri):
        self.db = SQLAlchemy(model_class=Base)

        pass

    def check_credentials(self, username, password) -> bool:
        url = f"SELECT CASE WHEN password = {password} THEN 1 ELSE 2 END FROM users WHERE user = {username};"
        result = True
        return result

    def query(sql, self):
        result = 'result string'
        return result

    def fake_close_connection(sql, self):
        result = 'result string'
        return result
