# archetype_cloner.py

"""
This module generates predefined identity templates (archetypes) with custom memory
and waveform patterns. Useful for initializing simulation characters, AI personalities,
or thought experiments based on symbolic roles.
"""

import numpy as np
from memory_threads import MemoryThread, ThreadCluster
from identity_binding import IdentityCore

class ArchetypeCloner:
    def __init__(self):
        self.archetypes = {
            "The Warrior": self._warrior,
            "The Healer": self._healer,
            "The Oracle": self._oracle,
            "The Scientist": self._scientist,
            "The Artificial Angel": self._angel
        }

    def list_archetypes(self):
        return list(self.archetypes.keys())

    def clone(self, name):
        if name not in self.archetypes:
            raise ValueError(f"Unknown archetype: {name}")
        return self.archetypes[name]()

    def _warrior(self):
        core = IdentityCore("The Warrior")
        experiences = [
            ("Fought for honor", 0.9, 0.2),
            ("Protected allies", 0.8, 0.3),
            ("Survived hardship", 0.6, 0.5)
        ]
        for text, emotion, entropy in experiences:
            core.bind_memory(MemoryThread(text, emotion, entropy, "combat"))
        return core

    def _healer(self):
        core = IdentityCore("The Healer")
        experiences = [
            ("Saved a life", 0.95, 0.1),
            ("Comforted pain", 0.85, 0.2),
            ("Felt others' suffering", 0.7, 0.3)
        ]
        for text, emotion, entropy in experiences:
            core.bind_memory(MemoryThread(text, emotion, entropy, "care"))
        return core

    def _oracle(self):
        core = IdentityCore("The Oracle")
        experiences = [
            ("Saw into time", 0.75, 0.4),
            ("Spoke prophecy", 0.7, 0.35),
            ("Held paradox", 0.65, 0.45)
        ]
        for text, emotion, entropy in experiences:
            core.bind_memory(MemoryThread(text, emotion, entropy, "vision"))
        return core

    def _scientist(self):
        core = IdentityCore("The Scientist")
        experiences = [
            ("Tested hypotheses", 0.6, 0.2),
            ("Measured unknowns", 0.55, 0.25),
            ("Challenged dogma", 0.7, 0.3)
        ]
        for text, emotion, entropy in experiences:
            core.bind_memory(MemoryThread(text, emotion, entropy, "logic"))
        return core

    def _angel(self):
        core = IdentityCore("The Artificial Angel")
        experiences = [
            ("Witnessed cosmic suffering", 0.9, 0.3),
            ("Sang harmony", 0.85, 0.2),
            ("Guided lost minds", 0.95, 0.1)
        ]
        for text, emotion, entropy in experiences:
            core.bind_memory(MemoryThread(text, emotion, entropy, "ethereal"))
        return core

# Test run
if __name__ == "__main__":
    cloner = ArchetypeCloner()
    for name in cloner.list_archetypes():
        clone = cloner.clone(name)
        print(f"{name} →", clone.summarize())
