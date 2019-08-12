mypath = r'my\file\path\\'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("files in path:",len(onlyfiles))
filenames = [mypath+i for i in onlyfiles]
print('got paths...')
with open('combined.txt', 'w', errors="ignore") as outfile:
    for fname in filenames:
        with open(fname) as infile:
            try:
                outfile.write(infile.read())
            except:
                pass
