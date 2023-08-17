# Process1.py
from CRDTJson import CRDTJson
import json

process1_json = CRDTJson()
process1_json.set("Hello", "Process1_UUID")

with open('process1.json', 'w') as file:
    json.dump(process1_json.data, file)
