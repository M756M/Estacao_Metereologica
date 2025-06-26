#include <stdlib.h>

const char* db_root_path = "~/proj/db";

void db_path(char* filename){
    int db_root_path_len = 0;
    int filename_len = 0;

    while(db_root_path[db_root_path_len] != '\0') db_root_path_len++;
    while(db_root_path[filename_len] != '\0') filename_len++;

    char* new_db_root_path[db_root_path_len + filename_len];



    return;
};