# CRDT JSON Merging System Documentation

## Overview

This system is designed to allow concurrent processes to produce individual JSON files that will eventually be merged into a single, conflict-free JSON file. It uses a CRDT (Conflict-Free Replicated Data Type) approach, where each process has its own instance of a `CRDTJson` class.

## Components

1. **CRDTJson Class**
    - The `CRDTJson` class is a custom data structure that manages JSON data, timestamps for conflict resolution, and unique identifiers (UUIDs).
    - Methods:
        - `set(replaced_text, process_uuid)` to add or update an entry.
        - `get(replaced_text)` to retrieve the value associated with a given key.
        - `merge(other)` to merge another `CRDTJson` object into the current one.
        - `save_metadata(filename)` to save the timestamps and UUIDs to a file.
        - `load_metadata(filename)` to load the timestamps and UUIDs from a file.

2. **Individual Process Scripts (e.g., `Process1.py`, `Process2.py`, `Process3.py`)**
    - These scripts represent different processes that are running concurrently.
    - Each script:
        - Instantiates a `CRDTJson` object.
        - Uses the `set` method to add some data.
        - Saves this data to a JSON file.
        - Saves metadata (timestamps and UUIDs) to another JSON file.
        - Writes a `.done` file indicating that it has finished its task.

3. **MergeScript (`MergeScript.py`)**
    - This script is responsible for merging the JSON files produced by the individual process scripts.
    - The `MergeScript`:
        - Waits for the `.done` files from each process, indicating they have finished writing their JSON files.
        - Loads the existing `merged.json` file if it exists, along with its metadata.
        - Merges the data from each process using the `merge` method of `CRDTJson`.
        - Saves the merged data back to `merged.json`.
        - Saves the merged metadata to `merged_metadata.json`.
        - Deletes the individual JSON files and `.done` files from the processes after merging.

## Workflow

1. **Start Individual Processes**
    - Run the individual process scripts (e.g., `Process1.py`, `Process2.py`, `Process3.py`) concurrently.
    - Each process will create its own JSON file and a corresponding `.done` file when it finishes.

2. **Wait for Processes to Complete**
    - `MergeScript.py` waits until it detects the `.done` files from all the individual processes.

3. **Merge Data**
    - `MergeScript.py` loads the JSON data and metadata files from each process.
    - It then merges this data into a single `CRDTJson` object, resolving conflicts based on timestamps.

4. **Save Merged Data**
    - `MergeScript.py` saves the merged data to `merged.json` and the merged metadata to `merged_metadata.json`.

5. **Cleanup**
    - `MergeScript.py` deletes the individual process JSON files and `.done` files after the merging is complete.

## Notes

- **Conflict Resolution**: In case of conflicts (i.e., different processes setting a value for the same key), the system uses timestamps to resolve the conflict. The value with the latest timestamp wins.
- **UUIDs**: The system also maintains a set of UUIDs to uniquely identify each operation, ensuring idempotency.