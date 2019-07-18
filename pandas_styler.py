#similar to conditional formatting in excel
def colorize(val):
    color = 'green' if val == "1st" else "yellow" if val == "2nd" else "orange" if val == "3rd" else "red" if val == "4th" else "white"
    return 'background-color: %s' % color
    
for i in range(len(dataframes)):
    dataframes[i] = dataframes[i].style.applymap(colorize)
