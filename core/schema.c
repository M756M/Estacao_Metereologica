#ifndef SCHEMA_PROP_C
#define SCHEMA_PROP_C

#include <sqlite3.h>
#include <config>

int create_readings_table(){
    sqlite3* db;
    char* db_name = "readings";

    sqlite3_open(db_path("readings"), &db);
};

#endif