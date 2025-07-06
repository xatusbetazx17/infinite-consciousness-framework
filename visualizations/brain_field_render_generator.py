# brain_field_render_generator.py

"""
Animated metaphysical brain render generator for Blender.
Now fully integrated with beyond-human NewMath logic and cognitive control.
Simulates an ultra-advanced brain with real-time logic resolution, synaptic restructuring,
and multidimensional learning and emotional overlays.
"""

import bpy
import math
import random

# ─── NewMath class ────────────────────────────────────────────────────────────
class NewMath:
    def __init__(self):
        self.infinity = float('inf')

    def add(self, a, b):
        return self.infinity if self.infinity in (a, b) else a + b

    def subtract(self, a, b):
        if a == b == self.infinity: return "Undefined"
        return a if b == self.infinity else a - b

    def multiply(self, a, b):
        return 0 if 0 in (a, b) else self.infinity if self.infinity in (a, b) else a * b

    def divide(self, a, b):
        return "Undefined" if b == 0 and a == 0 else self.infinity if b == 0 else a / b

    def exponentiate(self, a, b):
        if a == self.infinity and b == 0: return 1
        if b == self.infinity: return self.infinity if a > 1 else 0
        return a ** b

nm = NewMath()

# ─── Blender Environment Reset ────────────────────────────────────────────────

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for block in bpy.data.meshes:
        bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        bpy.data.materials.remove(block)
    for block in bpy.data.curves:
        bpy.data.curves.remove(block)

# ─── Neuron Types ─────────────────────────────────────────────────────────────

neuron_types = {
    "Pyramidal": (1, 0.2, 0.2, 1),
    "Interneuron": (0.2, 0.8, 0.2, 1),
    "MirrorNeuron": (0.2, 0.6, 1, 1),
    "DreamWeaver": (0.8, 0.5, 1, 1),
    "Hyperintuition": (1.0, 1.0, 0.2, 1),
    "TemporalAnchor": (0.2, 1.0, 0.8, 1),
    "MetaCognition": (1.0, 0.4, 0.0, 1),
    "InfinityNode": (1, 1, 1, 1)
}

neuron_objects = []

# ─── Create Neuron ─────────────────────────────────────────────────────────────

def create_neuron(name, location, color):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=5, radius=0.1, location=location)
    neuron = bpy.context.active_object
    neuron.name = name
    mat = bpy.data.materials.new(name=f"{name}_Material")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    emission = nodes.new("ShaderNodeEmission")
    emission.inputs[0].default_value = color
    emission.inputs[1].default_value = 2.5 + random.random() * 2
    output = nodes.get("Material Output")
    links.new(emission.outputs[0], output.inputs[0])
    neuron.data.materials.append(mat)
    return neuron

# ─── Animate Neuron Logic Pulse ────────────────────────────────────────────────

def add_pulse_animation(obj, start=1, duration=40):
    obj.scale = (1, 1, 1)
    obj.keyframe_insert(data_path="scale", frame=start)
    try:
        scale_peak = nm.exponentiate(1.2, 2)
    except Exception:
        scale_peak = 1.44
    obj.scale = (scale_peak, scale_peak, scale_peak)
    obj.keyframe_insert(data_path="scale", frame=start + duration//2)
    obj.scale = (1, 1, 1)
    obj.keyframe_insert(data_path="scale", frame=start + duration)

# ─── Generate Neurons with Thought Burst Animations ────────────────────────────

def generate_reactive_neurons():
    for i in range(256):
        label = random.choice(list(neuron_types.keys()))
        loc = (random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5))
        n = create_neuron(label, loc, neuron_types[label])
        neuron_objects.append(n)
        if i % 25 == 0:
            add_pulse_animation(n, start=10 + i // 4, duration=30)

# ─── Synaptic Connections (Fixed Emission Node) ────────────────────────────────

def create_dynamic_synapses(count=120):
    for _ in range(count):
        bpy.ops.curve.primitive_nurbs_path_add(location=(
            random.uniform(-2, 2),
            random.uniform(-2, 2),
            random.uniform(-2, 2)))
        path = bpy.context.active_object
        path.scale = (random.uniform(0.1, 0.3),) * 3

        mat = bpy.data.materials.new(name="SynapseMat")
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links

        # Clear existing nodes and create emission-driven synaptic visual
        for node in nodes:
            nodes.remove(node)

        emission = nodes.new(type="ShaderNodeEmission")
        emission.inputs[0].default_value = (0.9, 0.3, 1, 1)
        emission.inputs[1].default_value = 5.0

        output = nodes.new(type="ShaderNodeOutputMaterial")
        links.new(emission.outputs[0], output.inputs[0])

        path.data.materials.append(mat)

# ─── Label Utility ─────────────────────────────────────────────────────────────

def create_label(text, location):
    bpy.ops.object.text_add(location=location)
    label = bpy.context.active_object
    label.data.body = text
    label.data.size = 0.3
    label.rotation_euler = (math.radians(90), 0, 0)
    return label

# ─── Build Simulation ──────────────────────────────────────────────────────────

def build_animated_brain_field():
    clear_scene()
    generate_reactive_neurons()
    create_dynamic_synapses()
    create_label("⚛ Ultra-Thought Web", (2, 0, 1))
    create_label("📊 Predictive Decision Core", (2, 0, 0.4))
    create_label("🎭 Emotional Phase Loop", (2, 0, -0.2))
    create_label("🧠 Meta-Structural Intelligence", (2, 0, -0.8))
    create_label("∞ Conscious Engine Active", (2, 0, -1.2))
    create_label("🧮 NewMath Logic Matrix", (2, 0, -1.6))

# ─── Run in Blender ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    build_animated_brain_field()
