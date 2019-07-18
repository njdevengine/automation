from os import listdir
from os.path import isfile, join
mypath = r'C:\path\folder\\'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#"Name Search" is a common string that can be found in files you want
my_stuff = []
for i in onlyfiles:
    if "Name Search" in i:
        if "~$" not in i:
            my_stuff.append(i)
            
#GET NEWEST FILE           
p_path = []
for i in my_stuff:
    path = r'C:\path\folder\\'+i
    p_path.append(path)
latest_file = max(p_path, key=os.path.getctime)

xlsx = pd.ExcelFile(latest_file)
df = pd.read_excel(xlsx, 'sheet1')
