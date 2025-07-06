# bci_interface.py

"""
This module provides a bridge between EEG/BCI hardware and the identity framework.
It reads raw brainwave data and converts it into cognitive waveform vectors
for real-time integration with simulated consciousness states.
"""

import numpy as np

class BCIInterface:
    def __init__(self, channels=8, normalization=True):
        self.channels = channels
        self.normalization = normalization
        self.latest_signal = np.zeros(channels)

    def ingest_raw_signal(self, raw_data):
        """
        Accepts raw EEG-like input. Expects a list or array of floats.
        """
        if len(raw_data) != self.channels:
            raise ValueError(f"Expected {self.channels} channels, got {len(raw_data)}")
        signal = np.array(raw_data, dtype=float)
        if self.normalization:
            signal = self._normalize(signal)
        self.latest_signal = signal
        return signal

    def _normalize(self, signal):
        min_val, max_val = np.min(signal), np.max(signal)
        if max_val - min_val == 0:
            return np.zeros_like(signal)
        return (signal - min_val) / (max_val - min_val)

    def to_identity_waveform(self, target_size=128):
        """
        Expands EEG data into full-size waveform for injection.
        """
        return np.interp(
            np.linspace(0, self.channels - 1, target_size),
            np.arange(self.channels),
            self.latest_signal
        )

# Example simulation integration
if __name__ == "__main__":
    bci = BCIInterface(channels=8)
    brain_data = [0.3, 0.45, 0.29, 0.5, 0.4, 0.6, 0.35, 0.2]
    normalized = bci.ingest_raw_signal(brain_data)
    waveform = bci.to_identity_waveform()

    print("Normalized BCI Signal:", normalized)
    print("Generated Waveform (sample):", waveform[:5])
