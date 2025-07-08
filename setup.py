from setuptools import setup, find_packages

setup(
    name="vida-life-app",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "sqlalchemy",
        "python-jose[cryptography]",
        "passlib[bcrypt]",
        "pydantic[email]",
        "python-multipart",
    ],
)
