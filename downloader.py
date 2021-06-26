import os
import requests
from zipfile import ZipFile
account = "supermerill"
repository = "SuperSlicer"
bValidInt = False
url = requests.get("https://api.github.com/repos/"+account+"/"+repository+"/releases/latest").json()
maxRange = len(url["assets"])

def printReleases():
   assetIndex = 0
   print("\n\n\n")

   for i in url["assets"]: 
      print ("     "+str(assetIndex)+": "+str(i["name"]))
      assetIndex = assetIndex + 1
   return

printReleases()

while not bValidInt:
   try:
      val = int(input("\n \n Select Release: "))
      if val not in range(0,maxRange):
         print("\n\n ERROR: selection out of range")
         printReleases()
      else:
         bValidInt = True
   except ValueError:
      print("\n\n ERROR: That's not an int!")
      printReleases()

filename = str(url["assets"][val]["name"])
print("\n downloading: "+filename+"\n please wait....")
r = requests.get(str(url["assets"][val]["browser_download_url"]), allow_redirects=True)

open(filename, 'wb').write(r.content)
with ZipFile(filename, 'r') as zipObj:
   zipObj.extractall()
os.remove(filename)

