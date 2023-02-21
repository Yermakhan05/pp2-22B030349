import datetime

current_date = datetime.date.today() 
five_days_ago = current_date - datetime.timedelta(days=5)


print("Five days ago:", five_days_ago)
