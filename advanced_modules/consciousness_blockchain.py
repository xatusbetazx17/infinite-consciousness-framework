# consciousness_blockchain.py

"""
This module implements a lightweight blockchain ledger to record consciousness events,
law updates, memory shard movements, and identity forks.
It ensures persistence, traceability, and tamper-resistance for all critical
simulation transactions.
"""

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, event_type, payload):
        self.index = index
        self.timestamp = time.time()
        self.event_type = event_type  # e.g., 'law_update', 'memory_shard', 'identity_fork'
        self.payload = payload  # dictionary or event snapshot
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()

    def compute_hash(self):
        data = f"{self.index}{self.timestamp}{self.event_type}{self.payload}{self.previous_hash}"
        return hashlib.sha256(data.encode()).hexdigest()

    def summarize(self):
        return {
            "index": self.index,
            "type": self.event_type,
            "timestamp": self.timestamp,
            "hash": self.hash[:12],
            "prev": self.previous_hash[:12]
        }

class ConsciousnessLedger:
    def __init__(self):
        self.chain = []
        self.genesis_block()

    def genesis_block(self):
        genesis = Block(0, "0" * 64, "genesis", {"note": "Consciousness ledger initiated."})
        self.chain.append(genesis)

    def add_event(self, event_type, payload):
        previous = self.chain[-1]
        block = Block(len(self.chain), previous.hash, event_type, payload)
        self.chain.append(block)
        return block

    def verify_chain(self):
        for i in range(1, len(self.chain)):
            prev = self.chain[i - 1]
            curr = self.chain[i]
            if curr.previous_hash != prev.hash:
                return False
        return True

    def summarize_chain(self):
        return [b.summarize() for b in self.chain]

# Test block
if __name__ == "__main__":
    ledger = ConsciousnessLedger()
    ledger.add_event("law_update", {"law_name": "Entropy Lock", "version": "1.2"})
    ledger.add_event("memory_shard", {"shard_id": "abc123", "origin": "Oracle"})
    ledger.add_event("identity_fork", {"base_id": "X17", "new_id": "X17.1"})

    print("Ledger Verified:", ledger.verify_chain())
    print("Chain Summary:")
    for entry in ledger.summarize_chain():
        print(entry)
