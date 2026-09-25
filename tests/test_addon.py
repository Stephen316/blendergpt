import importlib.util
from pathlib import Path
from types import SimpleNamespace

import bpy


addon_path = Path(__file__).resolve().parents[1] / "blendergpt_addon.py"
spec = importlib.util.spec_from_file_location("blendergpt_addon", addon_path)
addon = importlib.util.module_from_spec(spec)
spec.loader.exec_module(addon)

addon.register()
try:
    scene = bpy.context.scene
    original_objects = set(scene.objects)
    assert scene.blendergpt.prompt == ""
    assert addon.BLENDERGPT_OT_RunPrompt.bl_label == "Check Prompt"
    assert "CHECKMARK" in bpy.types.UILayout.bl_rna.functions["operator"].parameters["icon"].enum_items

    class PanelLayout:
        def label(self, **kwargs):
            assert "no scene changes" in kwargs["text"]

        def prop(self, props, name):
            assert props == scene.blendergpt and name == "prompt"

        def operator(self, name, **kwargs):
            assert name == "blendergpt.run_prompt"

    addon.BLENDERGPT_PT_MainPanel.draw(SimpleNamespace(layout=PanelLayout()), bpy.context)
    assert bpy.ops.blendergpt.run_prompt() == {"CANCELLED"}

    scene.blendergpt.prompt = "  \t  "
    assert bpy.ops.blendergpt.run_prompt() == {"CANCELLED"}

    scene.blendergpt.prompt = "Create a simple cube scene"
    assert bpy.ops.blendergpt.run_prompt() == {"FINISHED"}
    assert set(scene.objects) == original_objects
finally:
    addon.unregister()

assert not hasattr(bpy.types.Scene, "blendergpt")
print("BlenderGPT prompt flow passed")
