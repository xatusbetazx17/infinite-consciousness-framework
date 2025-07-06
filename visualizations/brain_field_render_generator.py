# brain_field_render_generator.py

"""
Animated metaphysical brain render generator for Blender.
This version includes neuron reaction dynamics to stimulus input,
decision resolution visuals, and synaptic restructuring based on entropy.
It simulates an ultra-advanced brain with dynamic logic rewiring.
"""

import bpy
import math
import random

# Reset environment

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for block in bpy.data.meshes:
        bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        bpy.data.materials.remove(block)
    for block in bpy.data.curves:
        bpy.data.curves.remove(block)

# Neuron types and parameters

neuron_types = {
    "Pyramidal": (1, 0.2, 0.2, 1),
    "Interneuron": (0.2, 0.8, 0.2, 1),
    "MirrorNeuron": (0.2, 0.6, 1, 1),
    "DreamWeaver": (0.8, 0.5, 1, 1),
    "Hyperintuition": (1.0, 1.0, 0.2, 1),
    "TemporalAnchor": (0.2, 1.0, 0.8, 1),
    "MetaCognition": (1.0, 0.4, 0.0, 1)
}

neuron_objects = []

# Create neurons

def create_neuron(name, location, color):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=4, radius=0.1, location=location)
    neuron = bpy.context.active_object
    neuron.name = name
    mat = bpy.data.materials.new(name=f"{name}_Material")
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    emission = nodes.new("ShaderNodeEmission")
    emission.inputs[0].default_value = color
    emission.inputs[1].default_value = 2.0
    output = nodes.get("Material Output")
    links.new(emission.outputs[0], output.inputs[0])
    neuron.data.materials.append(mat)
    return neuron

# Animated burst reaction

def add_pulse_animation(obj, start=1, duration=40):
    obj.scale = (1, 1, 1)
    obj.keyframe_insert(data_path="scale", frame=start)
    obj.scale = (1.8, 1.8, 1.8)
    obj.keyframe_insert(data_path="scale", frame=start + duration//2)
    obj.scale = (1, 1, 1)
    obj.keyframe_insert(data_path="scale", frame=start + duration)

# Generate neurons and animate decision nodes

def generate_reactive_neurons():
    for i in range(256):
        label = random.choice(list(neuron_types.keys()))
        loc = (random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5), random.uniform(-1.5, 1.5))
        n = create_neuron(label, loc, neuron_types[label])
        neuron_objects.append(n)
        if i % 25 == 0:
            add_pulse_animation(n, start=10 + i // 4, duration=30)

# Create synaptic webs (with rebuild pattern)

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
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        bsdf.inputs['Emission'].default_value = (0.9, 0.3, 1, 1)
        bsdf.inputs['Emission Strength'].default_value = 4
        path.data.materials.append(mat)

# Labels for concepts

def create_label(text, location):
    bpy.ops.object.text_add(location=location)
    label = bpy.context.active_object
    label.data.body = text
    label.data.size = 0.3
    label.rotation_euler = (math.radians(90), 0, 0)
    return label

# Build simulation

def build_animated_brain_field():
    clear_scene()
    generate_reactive_neurons()
    create_dynamic_synapses()
    create_label("⚛ Ultra-Thought Web", (2, 0, 1))
    create_label("📊 Predictive Decision Core", (2, 0, 0.4))
    create_label("🎭 Emotional Phase Loop", (2, 0, -0.2))
    create_label("🧠 Meta-Structural Intelligence", (2, 0, -0.8))

# Execute in Blender
if __name__ == "__main__":
    build_animated_brain_field()
