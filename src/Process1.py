# Process1.py
import sys
import uuid  # <-- Import the uuid module here

from modules.CRDTJson import CRDTJson
import json

def main():
    process1_uuid = str(uuid.uuid4())  # <-- Generate a UUID for the process
    process1_json = CRDTJson()
    process1_json.set("Hello", process1_uuid)

    with open('process1.json', 'w') as file:
        json.dump(process1_json.data, file)

    process1_json.save_metadata('process1_metadata.json')

    with open('process1.done', 'w') as file:
        file.write('Done')

if __name__ == "__main__":
    main()
