import os
import sys

# Add the parent directory (containing entities) to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from entities.user import User, db  # Import db from the User model
from main import app  # Import the app instance directly
import unittest


class TestUserMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Push an app context and create all tables
        cls.app_context = app.app_context()
        cls.app_context.push()
        db.create_all()

        # Insert fake users into the database
        cls.fake_user1 = User(username="user1", password="password1", name="User 1")
        cls.fake_user2 = User(username="user2", password="password2", name="User 2")
        db.session.add(cls.fake_user1)
        db.session.add(cls.fake_user2)
        db.session.commit()

    @classmethod
    def tearDownClass(cls):
        # Remove the session and drop all tables
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_user_init(self):
        user = User(username="user1", password="password1", name="User 1")
        assert user.username == "user1"
        assert user.password == "password1"
        assert user.name == "User 1"

    def test_user_repr(self):
        user = User(username="user1", password="password1", name="User 1")
        assert repr(user) == "<User user1>"

    def test_user_name(self):
        user = User(username="user1", password="password1", name="User 1")
        assert user.name == "User 1"
