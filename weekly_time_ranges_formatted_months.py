ranges = []
end = last_thurs
start = last_friday
for i in range(1,53):
    end = (end - timedelta(weeks=1))
    start = (start - timedelta(weeks=1))
    array = []
    array.append(start.strftime("%Y-%m-%d"))
    array.append(end.strftime("%Y-%m-%d"))
    ranges.append(array)

#run only once
months_dict = {'01':'JAN','02':'FEB','03':'MAR','04':'APR','05':'MAY',
               '06':'JUN','07':'JUL','08':'AUG','09':'SEP','10':'OCT',
               '11':'NOV','12':'DEC'}
new_ranges = ranges
for i in range(len(ranges)):
    for x in range(len(ranges[i])):
        ranges[i][x] = months_dict[ranges[i][x].split("-")[1]]+"-"+ranges[i][x].split("-")[2]
