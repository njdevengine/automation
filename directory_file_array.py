from os import listdir
from os.path import isfile, join
mypath = r'directory\to_read\\'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
