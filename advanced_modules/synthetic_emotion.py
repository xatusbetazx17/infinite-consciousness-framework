# synthetic_emotion.py

"""
This module simulates programmable emotional fields as interactive data forces.
Synthetic emotions can modulate cognition, amplify memories, influence waveform activity,
and bind or disrupt identity cohesion. Each emotional vector is treated as a layered
multi-dimensional effect — capable of being injected, simulated, or organically formed.
"""

import numpy as np
import uuid
import random

class SyntheticEmotion:
    def __init__(self, label, intensity=0.5, volatility=0.1, polarity=1):
        self.id = str(uuid.uuid4())
        self.label = label  # e.g., "joy", "rage", "serenity", "anxiety"
        self.intensity = np.clip(intensity, 0.0, 1.0)  # emotional strength
        self.volatility = np.clip(volatility, 0.0, 1.0)  # stability of emotion over time
        self.polarity = polarity  # +1 = positive, -1 = negative, 0 = neutral
        self.vector = self._generate_vector()

    def _generate_vector(self, size=128):
        base = np.full(size, self.intensity * self.polarity)
        noise = np.random.normal(0, self.volatility, size)
        return np.clip(base + noise, -1.0, 1.0)

    def mutate(self, entropy=0.05):
        mutation = np.random.normal(0, entropy, self.vector.shape)
        self.vector = np.clip(self.vector + mutation, -1.0, 1.0)

    def inject_into_waveform(self, identity_waveform):
        mod = np.clip(identity_waveform + self.vector * 0.1, 0.0, 1.0)
        return mod

    def to_dict(self):
        return {
            "id": self.id,
            "label": self.label,
            "intensity": round(self.intensity, 3),
            "volatility": round(self.volatility, 3),
            "polarity": self.polarity,
            "sample_vector": self.vector[:5].tolist()
        }

# Emotional Field Synthesizer
class EmotionField:
    def __init__(self):
        self.active_emotions = []

    def emit(self, emotion: SyntheticEmotion):
        self.active_emotions.append(emotion)

    def resolve_field(self, waveform):
        if not self.active_emotions:
            return waveform
        combined = np.zeros_like(waveform)
        for e in self.active_emotions:
            combined += e.vector
        combined = np.clip(combined / max(len(self.active_emotions), 1), -1.0, 1.0)
        modulated = np.clip(waveform + combined * 0.05, 0.0, 1.0)
        return modulated

    def describe(self):
        return [e.to_dict() for e in self.active_emotions]

# Example run
if __name__ == "__main__":
    identity_wf = np.random.rand(128)

    joy = SyntheticEmotion("joy", intensity=0.8, volatility=0.05, polarity=1)
    rage = SyntheticEmotion("rage", intensity=0.7, volatility=0.2, polarity=-1)

    field = EmotionField()
    field.emit(joy)
    field.emit(rage)

    modulated = field.resolve_field(identity_wf)

    print("Original sample:", identity_wf[:5])
    print("Modulated sample:", modulated[:5])
    print("Field Description:")
    for desc in field.describe():
        print(desc)
