# Process2.py
from CRDTJson import CRDTJson
import json

process2_json = CRDTJson()
process2_json.set("World", "Process2_UUID")

with open('process2.json', 'w') as file:
    json.dump(process2_json.data, file)
