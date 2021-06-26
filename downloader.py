import os
import requests
from zipfile import ZipFile
account = "supermerill"
repository = "SuperSlicer"
assetIndex = 3
url = requests.get("https://api.github.com/repos/"+account+"/"+repository+"/releases/latest").json()
filename = str(url["assets"][assetIndex]["name"])
print("downloading: "+filename)
r = requests.get(str(url["assets"][assetIndex]["browser_download_url"]), allow_redirects=True)
open(filename, 'wb').write(r.content)
with ZipFile(filename, 'r') as zipObj:
   zipObj.extractall()
os.remove(filename)