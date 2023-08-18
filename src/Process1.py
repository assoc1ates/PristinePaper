# Process1.py`
import sys
import uuid
from modules.CRDTJson import CRDTJson
from modules.LlamaReplicateAPI import LlamaReplicateAPI  # <-- Import the LlamaReplicateAPI module here
import json

def main():
    process1_uuid = str(uuid.uuid4())
    process1_json = CRDTJson()
    process1_json.set("Hello", process1_uuid)

    with open('output-files/process1.json', 'w') as file:
        json.dump(process1_json.data, file)

    process1_json.save_metadata('output-files/process1_metadata.json')

    # Use LlamaReplicateAPI here
    llama_api = LlamaReplicateAPI()
    for item in llama_api.run_model("Hello, how are you?", temperature=0.75):
        print(item)

    with open('output-files/process1.done', 'w') as file:
        file.write('Done')

if __name__ == "__main__":
    main()
