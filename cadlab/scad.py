"""OpenSCAD interface"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_scad.ipynb.

# %% auto 0
__all__ = ['colorscheme', 'colorschemes', 'export_to', 'to_img', 'foo']

# %% ../nbs/01_scad.ipynb 2
#import solid2
from solid2.core.object_base.object_base_impl import RenderMixin
from solid2 import *
import subprocess

from PIL import Image
import io
from fastcore.all import *

import matplotlib.pyplot as plt

# %% ../nbs/01_scad.ipynb 3
colorscheme = "Tomorrow Night" #"Cornfield"
colorschemes = [
    "Cornfield", "Metallic", "Sunset", "Starnight",
    "BeforeDawn", "Nature", "DeepOcean", "Solarized",
    "Tomorrow", "Tomorrow Night", "Monotone"
]

# %% ../nbs/01_scad.ipynb 4
def export_to(model, export_format, w=300, h=150, colorscheme=None):
    colorscheme = colorscheme or globals()['colorscheme']
    
    result = subprocess.run(
        ['openscad', '--colorscheme', colorscheme, '--imgsize', f'{w},{h}', '--export-format', export_format, '-o', '-', '-'],
        input=bytes(str(model), 'utf-8'),
        capture_output=True
    )
    return result.stdout

# %% ../nbs/01_scad.ipynb 5
def to_img(model, w=300, h=150, colorscheme=None):
    "Convert model to image"

    data = export_to(model, "png", w=w, h=h, colorscheme=colorscheme)

    return Image.open(io.BytesIO(data))

# %% ../nbs/01_scad.ipynb 15
def foo(): pass
