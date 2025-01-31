# Library API

## Description

REST API for book manipulation in library.

## Functional

- Adding new books(POST)
- Getting books (with filters genre/author/avalibily) (GET)
- Updating info about book(PUT)
- Deleting book(DELETE)

## Used techs

- **Python** (FastAPI, SQLAlchemy)
- **SQLite** (DB)
- **Uvicorn** (server)

## Installation

Ensure you have [Poetry](https://python-poetry.org/docs/) installed.
e.g:

```sh
pip install poetry
```

Clone the repository and install dependencies:

```sh
git clone <repository-url>
cd <project-directory>
poetry install
```

## Usage

Activate the virtual environment and run the project:

```sh
poetry shell
uvicorn main:app
```

Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
