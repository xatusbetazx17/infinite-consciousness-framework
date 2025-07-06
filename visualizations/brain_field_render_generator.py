# brain_field_render_generator.py

"""
This script builds a complex neural-visual Blender scene when run inside Blender’s Python environment.
It creates a neocortex mesh, animated neuron pathways, volumetric emotion rings, and
predictive cognitive fields to visually simulate a beyond-human brain.
"""

import bpy
import math
import random

# Clean slate
def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for block in bpy.data.meshes:
        bpy.data.meshes.remove(block)
    for block in bpy.data.materials:
        bpy.data.materials.remove(block)

# Neocortex mesh

def create_neocortex():
    bpy.ops.mesh.primitive_uv_sphere_add(segments=128, ring_count=64, radius=1.0, location=(0, 0, 0))
    cortex = bpy.context.active_object
    cortex.name = "Neocortex"
    bpy.ops.object.modifier_add(type='SUBSURF')
    cortex.modifiers['Subdivision'].levels = 4
    cortex.modifiers['Subdivision'].render_levels = 6
    bpy.ops.object.shade_smooth()
    return cortex

# Emotion waveform torus

def create_emotion_rings():
    rings = []
    for i in range(3):
        bpy.ops.mesh.primitive_torus_add(location=(0, 0, 0.2 * (i - 1)))
        torus = bpy.context.active_object
        torus.scale = (1.4 + 0.2 * i, 1.4 + 0.2 * i, 0.05)
        torus.name = f"EmotionRing_{i}"
        mat = bpy.data.materials.new(name=f"EmotionMat_{i}")
        mat.use_nodes = True
        emission = mat.node_tree.nodes.new("ShaderNodeEmission")
        output = mat.node_tree.nodes["Material Output"]
        mat.node_tree.links.new(emission.outputs[0], output.inputs[0])
        emission.inputs[0].default_value = (1 - i * 0.3, 0.2 + i * 0.3, 0.9, 1)
        emission.inputs[1].default_value = 3 + i
        torus.data.materials.append(mat)
        rings.append(torus)
    return rings

# Particle halo (quantum cortex field)

def create_quantum_halo():
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=4, radius=2.5, location=(0, 0, 0))
    halo = bpy.context.active_object
    halo.name = "QuantumHalo"
    bpy.ops.object.particle_system_add()
    psys = halo.particle_systems[0]
    psys.name = "NeuronParticles"
    halo.modifiers["ParticleSystem"].show_render = False
    settings = psys.settings
    settings.count = 2048
    settings.lifetime = 1000
    settings.frame_start = 1
    settings.frame_end = 250
    settings.emit_from = 'VOLUME'
    settings.physics_type = 'BOIDS'
    return halo

# Label field HUD

def create_label(text, location):
    bpy.ops.object.text_add(location=location)
    label = bpy.context.active_object
    label.data.body = text
    label.data.size = 0.3
    label.name = f"Label_{text}"
    label.rotation_euler = (math.radians(90), 0, 0)
    return label

# Assemble the full brain field render

def build_brain_field():
    clear_scene()
    cortex = create_neocortex()
    create_emotion_rings()
    create_quantum_halo()
    create_label("Entropy", (2.5, -1, 0))
    create_label("Stability", (2.5, -1, -0.5))
    create_label("Dream Field", (2.5, -1, 0.5))

# Execute in Blender
if __name__ == "__main__":
    build_brain_field()
