# law_core.py

"""
Defines the base structure for programmable laws in the Infinite Consciousness Framework.
Each law is treated as an object with a unique identity and an activation function that
transforms simulation context or identity state.
"""

class Law:
    def __init__(self, name, description, activation_func):
        """
        Args:
            name (str): Unique name of the law
            description (str): Short summary of the rule or transformation
            activation_func (function): A function that takes in context and returns transformed context
        """
        self.name = name
        self.description = description
        self.activation_func = activation_func

    def apply(self, context):
        """
        Apply the law's logic to a given simulation context.
        Args:
            context (dict): The simulation state or logic environment
        Returns:
            dict: Modified context
        """
        return self.activation_func(context)

    def describe(self):
        """
        Returns a readable dictionary description of the law.
        """
        return {
            "name": self.name,
            "description": self.description,
            "activation_signature": str(self.activation_func.__name__)
        }

# Example default law (for testing)
def identity_preservation_law(context):
    if "identity_waveform" in context:
        context["stability"] = context.get("stability", 1.0) * 0.99  # mild decay
    return context

if __name__ == "__main__":
    test_law = Law("Identity Preservation", "Maintains identity coherence over time.", identity_preservation_law)
    ctx = {"identity_waveform": [0.8, 0.9, 0.95], "stability": 1.0}
    new_ctx = test_law.apply(ctx)
    print("Original:", ctx)
    print("Transformed:", new_ctx)
    print("Law Info:", test_law.describe())
