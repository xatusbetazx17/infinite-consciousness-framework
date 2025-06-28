# memory_threads.py

"""
This module manages the structure and evolution of memory threads in simulated consciousness.
Each thread represents a coherent cluster of experiences, emotions, and logical relationships.
"""

import uuid
import time
import hashlib

class MemoryThread:
    def __init__(self, content, emotional_charge=0.0, entropy=0.0, origin_label="neutral"):
        self.id = str(uuid.uuid4())
        self.timestamp = time.time()
        self.content = content  # A string or symbolic data structure
        self.entropy = entropy  # Represents internal chaos or decay risk
        self.emotional_charge = emotional_charge  # -1.0 (negative) to +1.0 (positive)
        self.origin_label = origin_label
        self.fingerprint = self.generate_fingerprint()

    def generate_fingerprint(self):
        return hashlib.sha256(self.content.encode('utf-8')).hexdigest()

    def decay(self, rate=0.001):
        self.entropy += rate
        self.emotional_charge *= (1 - rate)

    def reinforce(self, emotion_boost=0.01):
        self.entropy *= 0.95
        self.emotional_charge += emotion_boost
        if self.emotional_charge > 1.0:
            self.emotional_charge = 1.0

    def summarize(self):
        return {
            "id": self.id,
            "entropy": round(self.entropy, 3),
            "emotion": round(self.emotional_charge, 3),
            "origin": self.origin_label,
            "hash": self.fingerprint[:10],
        }

# Thread cluster example for multi-thread simulation
class ThreadCluster:
    def __init__(self):
        self.threads = []

    def add_thread(self, thread):
        self.threads.append(thread)

    def decay_all(self):
        for t in self.threads:
            t.decay()

    def reinforce_all(self, positive=True):
        for t in self.threads:
            t.reinforce(0.01 if positive else -0.01)

    def get_summary(self):
        return [t.summarize() for t in self.threads]
