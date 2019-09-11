# FRIDAY - THURSDAY LAST 5 WEEKS
from datetime import date

today = date.today()
offset = (today.weekday() - 3) % 7
last_thurs = today - timedelta(days=offset)
last_friday = last_thurs - datetime.timedelta(days=-1,weeks=1)

ranges = []
end = last_thurs
start = last_friday
for i in range(1,6):
    end = (end - timedelta(weeks=1))
    start = (start - timedelta(weeks=1))
    array = []
    array.append(start.strftime("%Y-%m-%d"))
    array.append(end.strftime("%Y-%m-%d"))
    ranges.append(array)
