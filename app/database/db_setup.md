# Campus Management System

Learning project built with **FastAPI** and **SQLModel**.

## What We Implemented

### SQLModel Setup

Created a SQLite database engine.

```python
from sqlmodel import create_engine

DATABASE_URL = "sqlite:///campus.db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)
```

* `sqlite:///campus.db` creates a SQLite database file named `campus.db`.
* `echo=True` prints all SQL statements to the console, which is useful for learning and debugging.

---

### Student Model

```python
from typing import Optional

from sqlmodel import Field, SQLModel


class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    age: int
    course: str
```

The `Student` model represents the `student` table in the database.

---

### Session Dependency

```python
from collections.abc import Generator

from sqlmodel import Session

from app.database.engine import engine


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
```

This dependency:

* Creates a database session.
* Provides the session to FastAPI endpoints.
* Automatically closes the session after the request is completed.

---

### Database Initialization

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel

from app.database.engine import engine

# Register all models
import app.models


@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)
```

`SQLModel.metadata.create_all(engine)` creates all registered tables if they do not already exist.

The models must be imported before calling `create_all()` so they are registered with `SQLModel.metadata`.

---

## Why `@asynccontextmanager`?

FastAPI recommends using the **Lifespan API** for application startup and shutdown.

```python
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    SQLModel.metadata.create_all(engine)

    yield

    # Shutdown
```

Everything **before** `yield` runs once when the application starts.

Everything **after** `yield` runs once when the application shuts down.

In our application:

* **Startup:** Create database tables.
* **Shutdown:** Nothing yet.

Later we'll use the shutdown section to clean up resources such as:

* Database connections
* Redis clients
* Background workers
* External service connections

The older `@app.on_event("startup")` approach still works, but the Lifespan API is the modern, recommended pattern for new FastAPI applications.

---

## Current Project Structure

```text
app/
├── main.py
├── database/
│   ├── engine.py
│   └── session.py
├── models/
│   └── student.py
└── routers/
```
