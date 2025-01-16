import requests
from pprint import pprint
import json

res = requests.get(
    "https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_North_American_Roads/FeatureServer/0/query?where=1%3D1&outFields=ID,LENGTH,LINKID,COUNTRY,JURISNAME,ROADNUM,ROADNAME,SPEEDLIM,Shape__Length,CLASS&outSR=4326&f=json")
# pprint(res.text)

print(res.status_code)
open("NTAD.json", "w").write(json.dumps(res.text, indent=6))


print("Completed")
