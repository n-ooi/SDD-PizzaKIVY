import sys
import datetime

date = str(datetime.datetime.now())[0:10]
print(date)
print(sys.getsizeof(date))