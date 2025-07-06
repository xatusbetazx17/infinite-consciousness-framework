# dream_weaver.py

"""
This module simulates immersive dream-states within a consciousness environment.
Dreams are generated using memory remixing, symbolic interference, and emotion-driven
logic warping. Useful for cognitive restoration, subconscious processing, or experimental narratives.
"""

import uuid
import numpy as np
import random
from memory_threads import MemoryThread, ThreadCluster
from identity_binding import IdentityCore
from law_core import Law

class DreamWeaver:
    def __init__(self, identity_core: IdentityCore):
        self.identity = identity_core
        self.dreams = []

    def generate_dream(self, mode="healing", intensity=0.5, loops=3):
        """
        Synthesizes a dream experience based on memory threads and emotional bias.
        Modes: 'healing', 'chaotic', 'echo', 'learning'
        """
        raw = self.identity.memory_cluster.threads
        if not raw:
            return None

        selected = random.sample(raw, min(len(raw), 5))
        pattern_matrix = self._remix_patterns(selected, intensity)
        theme = self._infer_theme(selected)

        for _ in range(loops):
            pattern_matrix = self._mutate(pattern_matrix, mode)

        dream_id = str(uuid.uuid4())
        dream_summary = {
            "id": dream_id,
            "theme": theme,
            "intensity": round(intensity, 3),
            "mode": mode,
            "signature": pattern_matrix[:5].tolist()
        }

        self.dreams.append(dream_summary)
        return dream_summary

    def _remix_patterns(self, memories, weight=0.5):
        signals = [self._thread_to_vector(m) for m in memories]
        base = np.mean(signals, axis=0)
        noise = np.random.normal(0, weight, size=base.shape)
        remixed = np.clip(base + noise, 0, 1)
        return remixed

    def _mutate(self, pattern, mode):
        if mode == "healing":
            filter = np.cos(np.linspace(0, np.pi, len(pattern)))
        elif mode == "chaotic":
            filter = np.random.uniform(-1, 1, len(pattern))
        elif mode == "echo":
            filter = np.sin(np.linspace(0, 2*np.pi, len(pattern)))
        elif mode == "learning":
            filter = np.logspace(-2, 0, len(pattern))
        else:
            filter = np.ones_like(pattern)

        mutated = pattern * filter
        return np.clip(mutated, 0, 1)

    def _thread_to_vector(self, memory):
        # Convert a thread to vector using emotional charge and entropy
        return np.linspace(memory.emotional_charge, 1 - memory.entropy, 128)

    def _infer_theme(self, memories):
        keywords = [m.origin_label for m in memories]
        common = max(set(keywords), key=keywords.count)
        return common

    def render_dream_law(self, dream_summary):
        label = dream_summary["theme"]
        signature = dream_summary["signature"]
        avg_amp = np.mean(signature)

        description = f"Dream-state distortion law based on theme '{label}' with synthetic amplitude {round(avg_amp, 3)}."

        def dream_logic(context):
            context[label] = context.get(label, 1.0) * (0.9 + avg_amp * 0.2)
            context["dream_effect"] = True
            return context

        return Law(f"DreamLaw_{label}_{dream_summary['id'][:6]}", description, dream_logic)

    def list_dreams(self):
        return [{"id": d["id"], "theme": d["theme"], "mode": d["mode"]} for d in self.dreams]


# Example test
if __name__ == "__main__":
    id_core = IdentityCore("DreamHost")
    for i in range(6):
        id_core.bind_memory(MemoryThread(f"Memory {i}", emotional_charge=0.6 - i * 0.1, entropy=0.1 * i, origin_label="hope"))

    weaver = DreamWeaver(id_core)
    dream = weaver.generate_dream(mode="healing", intensity=0.4, loops=5)
    print("Dream Summary:", dream)
    law = weaver.render_dream_law(dream)
    print("Dream Law Output:", law.describe())
