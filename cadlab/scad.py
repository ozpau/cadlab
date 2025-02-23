"""OpenSCAD interface"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/api/01_scad.ipynb.

# %% auto 0
__all__ = ['colorscheme', 'colorschemes', 'export_to', 'to_img', 'export_to_stl']

# %% ../nbs/api/01_scad.ipynb 2
#import solid2
from solid2.core.object_base.object_base_impl import RenderMixin
from solid2 import *
import subprocess

from PIL import Image
import io
from fastcore.all import *

import matplotlib.pyplot as plt
import numpy
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# %% ../nbs/api/01_scad.ipynb 4
colorscheme = "Tomorrow Night" #"Cornfield"
colorschemes = [
    "Cornfield", "Metallic", "Sunset", "Starnight",
    "BeforeDawn", "Nature", "DeepOcean", "Solarized",
    "Tomorrow", "Tomorrow Night", "Monotone"
]

# %% ../nbs/api/01_scad.ipynb 5
def export_to(model, export_format, w=600, h=300, colorscheme=None):
    colorscheme = colorscheme or globals()['colorscheme']
    
    result = subprocess.run(
        ['openscad', '--colorscheme', colorscheme, '--imgsize', f'{w},{h}',
         '--export-format', export_format,
        # '--preview', 'throwntogether',
         '--view', 'axes,crosshairs,scales',
         #'--view', 'scales',
         '--projection', 'ortho',
         '-o', '-', '-'],
        input=bytes(str(model), 'utf-8'),
        capture_output=True,
        check=True
    )
    return result.stdout

# %% ../nbs/api/01_scad.ipynb 6
def to_img(model, w=600, h=300, colorscheme=None):
    "Convert model to image"

    # If we render at slightly higher resolution, the result looks smoother
    s = 1.75
    data = export_to(model, "png", w=int(s*w), h=int(s*h), colorscheme=colorscheme)

    return Image.open(io.BytesIO(data)).resize((w,h), resample=Image.LANCZOS)

# %% ../nbs/api/01_scad.ipynb 8
@patch
def _repr_png_(self: RenderMixin):
    return to_img(self)._repr_png_()

del RenderMixin._ipython_display_

# %% ../nbs/api/01_scad.ipynb 13
def export_to_stl(model):
    stl = export_to(d, 'stl')
    stl = mesh.Mesh.from_file("", fh=io.BytesIO(stl))
    return stl
