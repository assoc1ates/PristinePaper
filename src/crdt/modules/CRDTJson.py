import time
import uuid
import json

class CRDTJson:
    def __init__(self):
        self.data = {}
        self.timestamps = {}
        self.uuids = set()

    def set(self, replaced_text, process_uuid):
        timestamp = time.time()
        text_uuid = str(uuid.uuid4())

        if replaced_text in self.timestamps and self.timestamps[replaced_text] > timestamp:
            return

        if text_uuid in self.uuids:
            return

        self.data[replaced_text] = text_uuid
        self.timestamps[replaced_text] = timestamp
        self.uuids.add(text_uuid)

    def get(self, replaced_text):
        return self.data.get(replaced_text)

    def merge(self, other):
        for key in other.data:
            self.set(key, other.get(key))
            if key in other.timestamps:
                if key not in self.timestamps or other.timestamps[key] > self.timestamps[key]:
                    self.timestamps[key] = other.timestamps[key]

    def save_metadata(self, filename):
        with open(filename, 'w') as file:
            json.dump({'timestamps': self.timestamps, 'uuids': list(self.uuids)}, file)

    def load_metadata(self, filename):
        with open(filename, 'r') as file:
            metadata = json.load(file)
            self.timestamps = metadata['timestamps']
            self.uuids = set(metadata['uuids'])
