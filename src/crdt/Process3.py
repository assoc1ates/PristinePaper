# Process3.py
from CRDTJson import CRDTJson
import json

def main():
    process3_json = CRDTJson()
    process3_json.set("Hello", "Process3_UUID")

    with open('process3.json', 'w') as file:
        json.dump(process3_json.data, file)

if __name__ == "__main__":
    main()
