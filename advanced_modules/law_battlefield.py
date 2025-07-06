# law_battlefield.py

"""
This module simulates clashes between competing logic systems or law sets.
Useful for testing contradictions, system resilience, and adaptive dominance
of programmable physics in cognitive and universal simulations.
"""

from law_core import Law
import numpy as np
import random

class LawArena:
    def __init__(self):
        self.set_a = []
        self.set_b = []
        self.battle_log = []

    def load_sets(self, laws_a, laws_b):
        self.set_a = laws_a
        self.set_b = laws_b

    def simulate(self, base_context=None, iterations=5):
        if base_context is None:
            base_context = {
                "entropy": 0.5,
                "stability": 1.0,
                "mutation": 1.0,
                "gravity": 1.0,
                "cohesion": 1.0,
                "dream_effect": False,
                "time_flow": 1
            }

        context_a = base_context.copy()
        context_b = base_context.copy()

        for i in range(iterations):
            for law in self.set_a:
                context_a = law.apply(context_a)
            for law in self.set_b:
                context_b = law.apply(context_b)

            score_a = self._score_context(context_a)
            score_b = self._score_context(context_b)
            winner = "Set A" if score_a > score_b else ("Set B" if score_b > score_a else "Draw")

            self.battle_log.append({
                "round": i + 1,
                "score_a": round(score_a, 3),
                "score_b": round(score_b, 3),
                "winner": winner,
                "context_diff": self._compare_contexts(context_a, context_b)
            })

        return self.battle_log

    def _score_context(self, context):
        score = context.get("stability", 1.0) + context.get("cohesion", 1.0)
        score -= context.get("entropy", 0.0)
        if context.get("dream_effect"):
            score *= 1.1
        return score

    def _compare_contexts(self, a, b):
        diff = {}
        for key in set(a.keys()).union(b.keys()):
            diff[key] = round(a.get(key, 0) - b.get(key, 0), 3)
        return diff

# Test block
if __name__ == "__main__":
    def stabilize(ctx):
        ctx["stability"] *= 1.01
        return ctx

    def destabilize(ctx):
        ctx["entropy"] += 0.05
        return ctx

    law1 = Law("Stabilizer", "Increases system stability.", stabilize)
    law2 = Law("Destabilizer", "Increases system entropy.", destabilize)

    arena = LawArena()
    arena.load_sets([law1], [law2])
    result = arena.simulate(iterations=3)

    for r in result:
        print(f"Round {r['round']}: {r['winner']} (A: {r['score_a']} vs B: {r['score_b']})")
