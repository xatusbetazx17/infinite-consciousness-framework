# cortex_engine.py

"""
This module simulates the functional digital cortex of a conscious identity.
It processes inputs, stores short-term and long-term signal branches, and 
coordinates logic resolution and memory integration.
"""

import numpy as np
from memory_threads import MemoryThread

class CortexEngine:
    def __init__(self, input_size=64, memory_limit=100):
        self.input_size = input_size
        self.signal_register = np.zeros(input_size)
        self.memory_buffer = []
        self.memory_limit = memory_limit
        self.logic_overdrive = False  # toggled during abstract processing

    def receive_input(self, signal):
        """
        Receives new data input (real or simulated sensory feed).
        """
        if len(signal) != self.input_size:
            raise ValueError("Signal input does not match cortex dimensions.")
        self.signal_register = np.array(signal)

    def integrate_memory(self, thread: MemoryThread):
        """
        Stores meaningful experience patterns in cortex memory.
        """
        self.memory_buffer.append(thread)
        if len(self.memory_buffer) > self.memory_limit:
            self.memory_buffer.pop(0)  # discard oldest memory

    def logic_pulse(self):
        """
        Simulates logical thought burst or pattern solving cycle.
        """
        self.logic_overdrive = True
        pattern = np.sin(self.signal_register * np.pi)
        resolved = np.clip(pattern * np.random.rand(self.input_size), 0, 1)
        self.logic_overdrive = False
        return resolved

    def memory_index(self):
        """
        Returns a compact list of memory summaries.
        """
        return [m.summarize() for m in self.memory_buffer]

# Example use
if __name__ == "__main__":
    cortex = CortexEngine()
    sample_signal = np.random.rand(64)
    cortex.receive_input(sample_signal)
    output = cortex.logic_pulse()
    print("Logic Pulse Result:", output[:5])
