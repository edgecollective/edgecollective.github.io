import argparse
parser = argparse.ArgumentParser()
parser.add_argument("mypath", help="filepath")
args = parser.parse_args()
#print(args.mypath)

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(args.mypath) if isfile(join(args.mypath, f))]

firstimage=onlyfiles[0]

print("---")
print("pageTitle: "+args.mypath)
print("layout: layout.njk")
print("date: 2020-08-04")
print("updated: 2020-08-04")
print("tags: notes")
print("image: img/"+args.mypath+"/"+firstimage)
print("blurb: Recent work.")
print("---\n")

for g in onlyfiles:
    name = g.split(".")[0]
    filepath = "/img/"+args.mypath+"/"+g
    #out = "| ![" + name + "](/img/"+args.mypath+"/"+g+") |\n|:--:|\n|  |\n\n"
    #out = "| ![" + name + "]("+filepath+") |\n|:--:|\n|  |\n\n"
    out = "|[ ![" + name + "]("+filepath+")]("+filepath+")|\n|:--:|\n|  |\n\n"
    print(out)

