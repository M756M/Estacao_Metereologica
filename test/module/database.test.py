import sys;
sys.path.append("src")

from database import Date;
import enum

format = "YYYY/MM/DD at hh:mm"
subject = "2025/04/24 at 01:59"

f = Date(subject, format)
print([f.year, f.month, f.day, f.hour, f.minute])
#u = Date(f.getAdapter(format)(f))