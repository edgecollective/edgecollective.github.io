import argparse
parser = argparse.ArgumentParser()
parser.add_argument("mypath", help="filepath")
args = parser.parse_args()
print(args.mypath)

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(args.mypath) if isfile(join(args.mypath, f))]
for g in onlyfiles:
    name = g.split(".")[0]
    out = "| ![" + name + "](/img/"+args.mypath+"/"+g+") |\n|:--:|\n|"+name+"|"
    print(out)

