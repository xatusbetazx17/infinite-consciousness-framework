# mind_render_gui.py

"""
This module provides a real-time GUI-based simulation visualizer for
conscious waveform evolution, emotion overlays, dream transitions,
and law-based contextual changes. This renderer is designed to go
beyond standard human-centric UI paradigms and display the
inner landscape of programmable consciousness.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from consciousness_environment import ConsciousnessEnvironment

class MindRenderGUI:
    def __init__(self, environment: ConsciousnessEnvironment):
        self.env = environment
        self.fig, self.ax = plt.subplots(3, 1, figsize=(10, 8))
        self.identity_waveform = np.copy(self.env.identity.identity_waveform)
        self.context_trace = []
        self.entropy_trace = []
        self.stability_trace = []
        self.emotion_trace = []

    def update_frame(self, frame):
        context = self.env.simulate_tick()

        # Update traces
        self.identity_waveform = self.env.identity.identity_waveform
        self.entropy_trace.append(context["entropy"])
        self.stability_trace.append(context["stability"])
        self.emotion_trace.append(context["emotion"])

        if len(self.entropy_trace) > 100:
            self.entropy_trace.pop(0)
            self.stability_trace.pop(0)
            self.emotion_trace.pop(0)

        # Clear axes
        for ax in self.ax:
            ax.clear()

        # Waveform Rendering
        self.ax[0].plot(self.identity_waveform, label="Cognitive Waveform", color="blue")
        self.ax[0].set_ylim(0, 1)
        self.ax[0].set_title("🧠 Consciousness Identity Waveform")
        self.ax[0].legend()

        # Stability & Entropy Plot
        self.ax[1].plot(self.entropy_trace, label="Entropy", color="red")
        self.ax[1].plot(self.stability_trace, label="Stability", color="green")
        self.ax[1].set_ylim(0, 1.2)
        self.ax[1].set_title("⚖️ Entropy vs Stability")
        self.ax[1].legend()

        # Emotion Spectrum Plot
        self.ax[2].plot(self.emotion_trace, label="Average Emotion Signal", color="purple")
        self.ax[2].set_ylim(0, 1.0)
        self.ax[2].set_title("💓 Emotional Activity Field")
        self.ax[2].legend()

        plt.tight_layout()

    def run(self):
        ani = animation.FuncAnimation(self.fig, self.update_frame, interval=1000)
        plt.show()

# Run the GUI simulation
if __name__ == "__main__":
    env = ConsciousnessEnvironment("RenderedMind")
    env.imprint_memory("Woke within rendered state", emotional_charge=0.6, entropy=0.2)
    env.inject_emotion("wonder", intensity=0.85, volatility=0.03)
    env.evolve_logic()
    renderer = MindRenderGUI(env)
    renderer.run()
