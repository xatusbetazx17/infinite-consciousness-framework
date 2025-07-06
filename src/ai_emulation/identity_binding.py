# identity_binding.py

"""
This module defines the structure and binding mechanisms for maintaining identity persistence
across simulated environments, physical systems, or memory-based reconstructions.
It links memory threads to a coherent self while managing cognitive resonance and stability.
"""

import uuid
import numpy as np
from memory_threads import MemoryThread, ThreadCluster

class IdentityCore:
    def __init__(self, label="UnnamedEntity"):
        self.id = str(uuid.uuid4())
        self.label = label
        self.memory_cluster = ThreadCluster()
        self.identity_waveform = self.initialize_waveform()
        self.stability_score = 1.0  # 0.0 = fragmented, 1.0 = stable

    def initialize_waveform(self, size=128):
        # Randomized signal representing identity presence and cohesion
        return np.random.rand(size)

    def bind_memory(self, memory: MemoryThread):
        self.memory_cluster.add_thread(memory)
        self.update_stability()
        self.update_waveform(memory)

    def update_waveform(self, memory):
        # Influence waveform by emotional charge and entropy
        delta = np.random.normal(loc=memory.emotional_charge, scale=memory.entropy, size=self.identity_waveform.shape)
        self.identity_waveform = np.clip(self.identity_waveform + delta * 0.01, 0, 1)

    def update_stability(self):
        entropies = [t.entropy for t in self.memory_cluster.threads]
        avg_entropy = np.mean(entropies) if entropies else 0.0
        self.stability_score = max(0.0, 1.0 - avg_entropy)

    def resonate_with(self, other):
        dot = np.dot(self.identity_waveform, other.identity_waveform)
        norm = np.linalg.norm(self.identity_waveform) * np.linalg.norm(other.identity_waveform)
        return dot / norm if norm != 0 else 0.0

    def summarize(self):
        return {
            "id": self.id,
            "label": self.label,
            "memories": len(self.memory_cluster.threads),
            "stability": round(self.stability_score, 3),
            "waveform_sample": self.identity_waveform[:5].tolist(),
        }
