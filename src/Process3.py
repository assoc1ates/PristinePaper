# Process3.py
import sys
import uuid  # <-- Import the uuid module here

from modules.CRDTJson import CRDTJson
import json

def main():
    process3_uuid = str(uuid.uuid4())  # <-- Generate a UUID for the process
    process3_json = CRDTJson()
    process3_json.set("Hello", process3_uuid)

    with open('output-files/process3.json', 'w') as file:
        json.dump(process3_json.data, file)

    process3_json.save_metadata('output-files/process3_metadata.json')

    with open('output-files/process3.done', 'w') as file:
        file.write('Done')

if __name__ == "__main__":
    main()
