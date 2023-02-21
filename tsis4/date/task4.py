import datetime

date_1 = input("Format 'dd.MM.YYYY HH:MM:SS': ")
date_2 = input("Format 'dd.MM.YYYY HH:MM:SS': ")

date1 = datetime.datetime.strptime(date_1, '%d.%m.%Y %H:%M:%S')
date2 = datetime.datetime.strptime(date_2, '%d.%m.%Y %H:%M:%S')

sec = int((date2 - date1).total_seconds())

print(sec)