#include <sqlite3.h>

#ifndef NULL
#define NULL (void*)0
#endif

int main(){
    sqlite3* db;

    sqlite3_open("db/readings", &db);

    char err[32];
    sqlite3_exec(db, "create table if not exists readings (text date, int cods)", NULL, NULL, (char**)&err);
    
    sqlite3_close(db);
    return 0;
};