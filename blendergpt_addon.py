bl_info = {
    "name": "BlenderGPT",
    "author": "Stephen",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > BlenderGPT",
    "description": "A starter panel for sending instructions to BlenderGPT.",
    "category": "3D View",
}

import bpy


class BLENDERGPT_Properties(bpy.types.PropertyGroup):
    prompt: bpy.props.StringProperty(
        name="Prompt",
        description="Tell BlenderGPT what you want to create or change",
        default="Create a simple cube scene",
    )


class BLENDERGPT_OT_RunPrompt(bpy.types.Operator):
    bl_idname = "blendergpt.run_prompt"
    bl_label = "Run Prompt"
    bl_description = "Run the current BlenderGPT prompt"

    def execute(self, context):
        prompt = context.scene.blendergpt.prompt
        self.report({"INFO"}, f"BlenderGPT prompt received: {prompt}")
        return {"FINISHED"}


class BLENDERGPT_PT_MainPanel(bpy.types.Panel):
    bl_label = "BlenderGPT"
    bl_idname = "BLENDERGPT_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BlenderGPT"

    def draw(self, context):
        layout = self.layout
        props = context.scene.blendergpt

        layout.prop(props, "prompt")
        layout.operator("blendergpt.run_prompt", icon="PLAY")


classes = (
    BLENDERGPT_Properties,
    BLENDERGPT_OT_RunPrompt,
    BLENDERGPT_PT_MainPanel,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.blendergpt = bpy.props.PointerProperty(type=BLENDERGPT_Properties)


def unregister():
    del bpy.types.Scene.blendergpt
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
