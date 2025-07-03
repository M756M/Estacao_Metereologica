from enum import Enum as enum_t;

class tbl(enum_t):
    READINGS_T1 = "create table if not exists readings_s1(date text, cod integer, temperatura real, umidade_rel real, pressao real)";
    READINGS_T2 = "create table if not exists readings_s2(date text, cod integer, temperatura real, velocidade_vento real, direcao_vento text)";
    READINGS_T3 = "create table if not exists readings_s3(date text, cod integer, precipitacao real)";

def create_tbl(tbl: tbl):
    if(tbl not in tbl): raise ValueError("Invalid table schema");

    from sqlite3 import connect;
    from .config import db_path;

    with connect(db_path("readings")) as db: db.execute(tbl.value);
    return;

def tbl_info(table: tbl):
    if(table == tbl.READINGS_T1):
        return {
            "columns": {
                "date": "text",
                "cod": "integer",
                "temperatura": "real",
                "umidade_rel": "real",
                "pressao": "real"
            }
        };
    if(table == tbl.READINGS_T2):
        return {
            "columns": {
                "date": "text",
                "cod": "integer",
                "temperatura": "real",
                "velocidade_vento": "real",
                "direcao_vento": "real"
            }
        };
    if(table == tbl.READINGS_T3):
        return {
            "columns": {
                "date": "text",
                "cod": "integer",
                "precipitacao": "real"
            }
        };
    return {};