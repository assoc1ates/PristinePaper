import time
import uuid
import json
import threading

class CRDTJson:
    def __init__(self):
        self.data = {}
        self.timestamps = {}
        self.uuids = set()
        self.lock = threading.Lock()

    def set(self, replaced_text, process_uuid):
        timestamp = time.time()

        with self.lock:
            # Check if the replaced_text is already in the data
            if replaced_text in self.data:
                # If it is, we simply return and do not update it
                return
            if (replaced_text in self.timestamps and self.timestamps[replaced_text] > timestamp) or (process_uuid in self.uuids):
                return

            self.data[replaced_text] = process_uuid
            self.timestamps[replaced_text] = timestamp
            self.uuids.add(process_uuid)

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
