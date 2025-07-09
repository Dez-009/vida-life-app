import sys
import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from database import get_db
from models.user import Base

# Use SQLite in-memory database for testing with proper connection settings
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool  # This ensures a single connection for in-memory DB
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="session")
def test_app():
    # Set up
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db
    yield app
    # Tear down
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def test_client(test_app):
    return TestClient(test_app)

@pytest.fixture(autouse=True)
def setup_test_db():
    # Setup - will be run before each test
    Base.metadata.create_all(bind=engine)
    yield
    # Teardown - will be run after each test
    Base.metadata.drop_all(bind=engine)
