import sys

from modules.CRDTJson import CRDTJson
import json
import time
import os

def load_json_to_crdt(filename, metadata_filename):
    with open(filename, 'r') as file:
        data = json.load(file)

    crdt_json = CRDTJson()
    crdt_json.data = data
    crdt_json.load_metadata(metadata_filename)

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
    filenames = ['output-files/process1.json', 'output-files/process2.json', 'output-files/process3.json']
    done_filenames = ['output-files/process1.done', 'output-files/process2.done', 'output-files/process3.done']
    metadata_filenames = ['output-files/process1_metadata.json', 'output-files/process2_metadata.json', 'output-files/process3_metadata.json']

    wait_for_files(done_filenames)

    merged_json = CRDTJson()

    if os.path.exists('output-files/merged.json'):
        merged_json = load_json_to_crdt('output-files/merged.json', 'output-files/merged_metadata.json')

    process1_json = load_json_to_crdt('output-files/process1.json', 'output-files/process1_metadata.json')
    process2_json = load_json_to_crdt('output-files/process2.json', 'output-files/process2_metadata.json')
    process3_json = load_json_to_crdt('output-files/process3.json', 'output-files/process3_metadata.json')

    merged_json.merge(process1_json)
    merged_json.merge(process2_json)
    merged_json.merge(process3_json)

    print(merged_json.data)

    with open('output-files/merged.json', 'w') as file:
        json.dump(merged_json.data, file)

    merged_json.save_metadata('output-files/merged_metadata.json')

    delete_files(filenames)
    delete_files(done_filenames)
    delete_files(metadata_filenames)

if __name__ == "__main__":
    main()
