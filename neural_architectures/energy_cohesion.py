# energy_cohesion.py

"""
This module evaluates the energetic stability and cohesion of an identity system,
specifically focusing on the bonding strength between memory threads and the integrity
of the overall cognitive field.
"""

import numpy as np
from memory_threads import MemoryThread, ThreadCluster

class CohesionAnalyzer:
    def __init__(self, cluster: ThreadCluster):
        self.cluster = cluster

    def calculate_entropy_distribution(self):
        return [t.entropy for t in self.cluster.threads]

    def calculate_emotional_spectrum(self):
        return [t.emotional_charge for t in self.cluster.threads]

    def compute_cohesion_index(self):
        """
        Measures how stable the memory cluster is. Range: 0 (unstable) to 1 (highly stable).
        """
        if not self.cluster.threads:
            return 1.0  # empty cluster is trivially stable

        entropies = self.calculate_entropy_distribution()
        emotions = self.calculate_emotional_spectrum()

        entropy_factor = 1.0 - np.mean(entropies)
        emotion_balance = 1.0 - abs(np.mean(emotions))  # closer to 0 = more volatile

        cohesion = (entropy_factor + emotion_balance) / 2
        return round(np.clip(cohesion, 0.0, 1.0), 3)

    def report(self):
        return {
            "entropy": round(np.mean(self.calculate_entropy_distribution()), 3),
            "emotion_avg": round(np.mean(self.calculate_emotional_spectrum()), 3),
            "cohesion_index": self.compute_cohesion_index(),
            "thread_count": len(self.cluster.threads)
        }

# Example usage
if __name__ == "__main__":
    cluster = ThreadCluster()
    for i in range(10):
        thread = MemoryThread(content=f"Experience {i}", emotional_charge=np.random.uniform(-1, 1), entropy=np.random.rand())
        cluster.add_thread(thread)

    analyzer = CohesionAnalyzer(cluster)
    print("Cohesion Report:", analyzer.report())
