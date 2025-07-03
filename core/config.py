ROOT = "D:/data/IFSUL/proj_py";
DB_ROOT = ROOT + "/db";

def db_path(filename: str) -> str:
    import re;

    while re.match(r"^(/|\\)", filename): filename = filename.replace("/", count=1);

    return DB_ROOT + "/" + filename;