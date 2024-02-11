import datetime

current = datetime.date.today()

new = current - datetime.timedelta(days=5)

print(current)
print(new)