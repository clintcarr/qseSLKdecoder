import requests
import json
import base64

# Put your SLK here
SLK = ""
headers = {'authorization': 'Bearer {}'.format(SLK)}
r = requests.get("https://license.qlikcloud.com/v1/definitions/portable/info", headers=headers)
jl = json.loads(r.text)

license = (jl["license"])
sld = (jl["sld"])

sldObj = json.loads(base64.b64decode(sld))
sldFin = sldObj["signedDef"]["definition"]

definition = json.loads(base64.b64decode(sldFin))

print (json.dumps(definition,indent=4))