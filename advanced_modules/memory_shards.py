# memory_shards.py

"""
This module allows the extraction, storage, recombination, and injection
of memory fragments ("shards") into identity structures. These shards
are transferable containers of memory threads useful for duplication,
healing, or knowledge sharing.
"""

import uuid
from memory_threads import MemoryThread, ThreadCluster

class MemoryShard:
    def __init__(self, source_id, label="UnnamedShard"):
        self.id = str(uuid.uuid4())
        self.label = label
        self.source_id = source_id
        self.threads = []

    def add_thread(self, memory_thread: MemoryThread):
        self.threads.append(memory_thread)

    def summarize(self):
        return {
            "id": self.id,
            "label": self.label,
            "source": self.source_id,
            "count": len(self.threads),
            "entropy_avg": round(sum(t.entropy for t in self.threads) / len(self.threads), 3) if self.threads else 0,
            "emotional_charge_avg": round(sum(t.emotional_charge for t in self.threads) / len(self.threads), 3) if self.threads else 0
        }

    def inject_to_cluster(self, cluster: ThreadCluster):
        for t in self.threads:
            cluster.add_thread(t)

# Utility function to create a shard from a cluster subset

def extract_shard(cluster: ThreadCluster, filter_func=lambda t: True, label="FilteredShard"):
    shard = MemoryShard(source_id="cluster", label=label)
    for t in cluster.threads:
        if filter_func(t):
            shard.add_thread(t)
    return shard

# Test block
if __name__ == "__main__":
    from memory_threads import MemoryThread

    cluster = ThreadCluster()
    for i in range(5):
        cluster.add_thread(MemoryThread(f"Exp {i}", emotional_charge=0.6 - i * 0.1, entropy=0.1 + i * 0.05))

    shard = extract_shard(cluster, filter_func=lambda t: t.emotional_charge > 0.3, label="PositiveMemory")
    print("Shard Summary:", shard.summarize())
