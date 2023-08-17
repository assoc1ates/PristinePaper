# MergeScript.py
from CRDTJson import CRDTJson
import json
import time
import os

def load_json_to_crdt(filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    crdt_json = CRDTJson()
    crdt_json.data = data
    return crdt_json

def wait_for_files(filenames, interval=5):
    while True:
        if all(os.path.exists(f) for f in filenames):
            break
        print("Waiting for files...")
        time.sleep(interval)

def delete_files(filenames):
    for filename in filenames:
        try:
            os.remove(filename)
            print(f"Deleted file: {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found")

def main():
    filenames = ['process1.json', 'process2.json', 'process3.json']

    wait_for_files(filenames)

    merged_json = CRDTJson()

    # Load existing data from merged.json if it exists
    if os.path.exists('merged.json'):
        merged_json = load_json_to_crdt('merged.json')

    process1_json = load_json_to_crdt('process1.json')
    process2_json = load_json_to_crdt('process2.json')
    process3_json = load_json_to_crdt('process3.json')

    merged_json.merge(process1_json)
    merged_json.merge(process2_json)
    merged_json.merge(process3_json)

    print(merged_json.data)

    with open('merged.json', 'w') as file:
        json.dump(merged_json.data, file)

    # Delete the process json files after merging
    delete_files(filenames)

if __name__ == "__main__":
    main()
