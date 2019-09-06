from os import listdir
from os.path import isfile, join
import pandas as pd

from datetime import datetime
import warnings
warnings.filterwarnings("ignore")
startTime = datetime.now()


mypath = r'followers\\'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
frames = []
for i in onlyfiles:
    df = pd.read_csv(r'followers\\'+str(i))
    frames.append(df)
combined = pd.concat(frames)
print("total files:",len(onlyfiles))
y = len(onlyfiles)
x = (datetime.now() - startTime)
print("time took:",x)
print(str(round(y/x.seconds)),"per second")
remaining = str(round(((4667-y)/10)*2)/60)+ " hours"
print(remaining)
