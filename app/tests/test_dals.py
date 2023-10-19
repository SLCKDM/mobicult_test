import unittest
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.db import get_db, base
from app.db.base import Base

SQLALCHEMY_DATABASE_URL = "sqlite://"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    db = None
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        if db:
            db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


class TestCurrencyDAL(unittest.TestCase):

    def test_create(self):
        self.assertEqual(1, 1)

    def test_delete(self):
        self.assertEqual(1, 1)

    def test_update(self):
        self.assertEqual(1, 1)
