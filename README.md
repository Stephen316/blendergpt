# BlenderGPT

BlenderGPT is a starter Blender add-on project. The goal is to let you type an instruction and turn it into Blender actions.

## What is included

- `blendergpt_addon.py` - the Blender add-on file.
- `requirements.txt` - Python package list for future OpenAI/API work.
- `.gitignore` - keeps temporary files out of GitHub.
- `README.md` - this guide.

## How to try it in Blender

1. Open Blender.
2. Go to `Edit > Preferences > Add-ons`.
3. Click `Install...`.
4. Choose `blendergpt_addon.py` from this folder.
5. Enable the add-on.
6. Open the 3D View sidebar with `N` and find the `BlenderGPT` tab.

## Current status

This first version lets you enter and check a prompt in the BlenderGPT sidebar. The prompt starts empty; the Check Prompt button asks you to enter one if it is blank, or confirms receipt otherwise. **No scene changes or AI commands are run yet.** This is a starting point for adding real AI commands next.

## Test in Blender

With Blender 4.0 or later installed, run `blender -b --python-exit-code 1 --python tests/test_addon.py` to check registration and the prompt flow.
