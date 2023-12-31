# Process2.py
import sys
import uuid  # <-- Import the uuid module here

from modules.CRDTJson import CRDTJson
import json

def main():
    process2_uuid = str(uuid.uuid4())  # <-- Generate a UUID for the process
    process2_json = CRDTJson()
    process2_json.set("World", process2_uuid)

    with open('output-files/process2.json', 'w') as file:
        json.dump(process2_json.data, file)

    process2_json.save_metadata('output-files/process2_metadata.json')

    with open('output-files/process2.done', 'w') as file:
        file.write('Done')

if __name__ == "__main__":
    main()
