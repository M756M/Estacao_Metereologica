import sqlite3;

from . import config;

def get(query: str):
    if(query.find(";") >= 0): raise ValueError("Cannot execute the query. Must not contain a semicolon");

    with sqlite3.connect(config.db_path("readings")) as db:
        return db.execute(query).fetchall();

def insert(query: str):
    if(query.find(";") >= 0): raise ValueError("Cannot execute the query. Must not contain a semicolon");

    with sqlite3.connect(config.db_path("readings")) as db:
        return db.execute(query).fetchall();
    return;

def delete(query: str):
    if(query.find(";") >= 0): raise ValueError("Cannot execute the query. Must not contain a semicolon");

    with sqlite3.connect(config.db_path("readings")) as db:
        return db.execute(query).fetchall();
    return;

def update(query: str):
    if(query.find(";") >= 0): raise ValueError("Cannot execute the query. Must not contain a semicolon");

    with sqlite3.connect(config.db_path("readings")) as db:
        return db.execute(query).fetchall();
    return;