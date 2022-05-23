#!/usr/bin/env python3
"""Authentication relevant methods module"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """Return hashed and salted password

    Args:
        password: password string

    Returns:
        hashed and salted byte string password
    """
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self) -> None:
        self._db = DB()
        return None

    def register_user(self, email, password) -> User:
        """Register a new user to the database

        Args:
            email: email of new user
            password: password of new user

        Returns:
            a `User` instance

        Raises:
            ValueError: when user already exists
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            return self._db.add_user(
                email, str(_hash_password(password))
            )
    pass