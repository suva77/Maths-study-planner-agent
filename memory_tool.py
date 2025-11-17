# memory_tool.py

import json
import os

class MemoryTool:
    def __init__(self, file_path="study_history.json"):
        self.path = file_path
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

    def read_history(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def save_history(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)
