from CRDTJson import CRDTJson
import json

def main():
    process1_json = CRDTJson()
    process1_json.set("Hello", "Process1_UUID")

    with open('process1.json', 'w') as file:
        json.dump(process1_json.data, file)

    process1_json.save_metadata('process1_metadata.json')

    with open('process1.done', 'w') as file:
        file.write('Done')

if __name__ == "__main__":
    main()
