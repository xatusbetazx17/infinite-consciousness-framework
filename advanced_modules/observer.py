# observer.py

"""
This module defines passive observers within the simulation. Observers can watch
identity evolution, law applications, or environmental changes without influencing them.
They are useful for logging, monitoring, debugging, or consciousness research scenarios.
"""

import uuid
import time

class Observer:
    def __init__(self, label="AnonymousObserver"):
        self.id = str(uuid.uuid4())
        self.label = label
        self.logs = []

    def watch_event(self, event_type, data):
        timestamp = time.time()
        entry = {
            "timestamp": timestamp,
            "event_type": event_type,
            "data": data
        }
        self.logs.append(entry)
        return entry

    def get_recent_logs(self, limit=5):
        return self.logs[-limit:]

    def summarize(self):
        return {
            "id": self.id,
            "label": self.label,
            "observed_events": len(self.logs)
        }

# Test block
if __name__ == "__main__":
    observer = Observer("MetaLogger")
    observer.watch_event("identity_created", {"id": "X17", "type": "Oracle"})
    observer.watch_event("law_applied", {"law": "Entropy Control"})
    observer.watch_event("memory_injected", {"threads": 3})

    print("Summary:", observer.summarize())
    print("Recent Logs:", observer.get_recent_logs())
