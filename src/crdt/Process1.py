# Process1.py
from CRDTJson import CRDTJson
import json

def main():
    process1_json = CRDTJson()
    process1_json.set("Hello", "Process1_UUID")

    with open('process1.json', 'w') as file:
        json.dump(process1_json.data, file)

if __name__ == "__main__":
    main()

