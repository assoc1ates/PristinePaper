# CRDTJson.py
import time
import uuid

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
            self.set(key, other.data[key])
            if key in other.timestamps:
                if key not in self.timestamps or other.timestamps[key] > self.timestamps[key]:
                    self.timestamps[key] = other.timestamps[key]
