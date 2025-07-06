# physics_loader.py

"""
This module loads physics rule definitions from YAML (or JSON) and converts them
into active Law objects that can be registered in the logic engine.
Useful for defining alternate universes, modifying logic sets, or importing
custom physics on demand.
"""

import yaml
from law_core import Law

class PhysicsLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.law_list = []

    def load(self):
        with open(self.filepath, 'r') as file:
            raw = yaml.safe_load(file)
        self.law_list = self._parse(raw)
        return self.law_list

    def _parse(self, data):
        law_objects = []
        for name, props in data.items():
            desc = props.get("description", "No description provided.")
            rule = props.get("rule")
            params = props.get("params", {})

            def make_func(rule, params):
                def logic(context):
                    # Dynamically insert values based on rule logic
                    if rule == "harmonic_pull":
                        context["gravity"] = context.get("gravity", 1.0) * params.get("strength", 1.0)
                    if rule == "invert_time_if_stable":
                        if context.get("entropy", 1.0) < 0.5:
                            context["time_flow"] *= -1
                    return context
                return logic

            logic_func = make_func(rule, params)
            law_objects.append(Law(name, desc, logic_func))
        return law_objects


# Example YAML File (for reference):
"""
gravity:
  description: Applies harmonic gravity scaling
  rule: harmonic_pull
  params:
    strength: 2.5

entropy_gate:
  description: Inverts time flow if entropy is low
  rule: invert_time_if_stable
"""

# Test block
if __name__ == "__main__":
    loader = PhysicsLoader("example_physics.yaml")
    laws = loader.load()
    for law in laws:
        print("Loaded Law:", law.describe())
