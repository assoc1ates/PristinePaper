# Process2.py
from CRDTJson import CRDTJson
import json

def main():
    process2_json = CRDTJson()
    process2_json.set("World", "Process2_UUID")

    with open('process2.json', 'w') as file:
        json.dump(process2_json.data, file)

if __name__ == "__main__":
    main()
