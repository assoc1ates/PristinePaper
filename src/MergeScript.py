# MergeScript.py
from CRDTJson import CRDTJson
import json

def load_json_to_crdt(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    crdt_json = CRDTJson()
    crdt_json.data = data
    return crdt_json

# Load the saved JSON data from each process into CRDTJson instances
process1_json = load_json_to_crdt('process1.json')
process2_json = load_json_to_crdt('process2.json')
process3_json = load_json_to_crdt('process3.json')

# Create a new CRDTJson instance to merge into
merged_json = CRDTJson()

# Merge the separate CRDTJson instances into the merged_json instance
merged_json.merge(process1_json)
merged_json.merge(process2_json)
merged_json.merge(process3_json)

# Print the final, merged JSON object
print(merged_json.data)

# Optionally, save the merged data back to a new JSON file
with open('merged.json', 'w') as file:
    json.dump(merged_json.data, file)
