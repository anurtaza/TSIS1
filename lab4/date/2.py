import datetime

today_date = datetime.date.today()

yesterday_date = today_date - datetime.timedelta(days=1)

tomorrow_date = today_date + datetime.timedelta(days=1)

print("yesterday: ", yesterday_date)
print("today: ", today_date)
print("tomorrow: ", tomorrow_date)