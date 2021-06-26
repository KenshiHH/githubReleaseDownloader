import os
import requests
from tqdm import tqdm
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


response = requests.get(str(url["assets"][val]["browser_download_url"]), stream=True)
total_size_in_bytes= int(response.headers.get('content-length', 0))
block_size = 1024 #1 Kibibyte
progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
with open(filename, 'wb') as file:
    for data in response.iter_content(block_size):
        progress_bar.update(len(data))
        file.write(data)
progress_bar.close()
if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
    print("ERROR, something went wrong")

print("\n trying to extract file...")    
with ZipFile(filename, 'r') as zipObj:
   zipObj.extractall()
os.remove(filename)