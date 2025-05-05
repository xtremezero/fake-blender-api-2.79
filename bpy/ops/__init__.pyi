import typing
import collections.abc
import typing_extensions
from . import action as action
from . import anim as anim
from . import armature as armature
from . import boid as boid
from . import brush as brush
from . import buttons as buttons
from . import cachefile as cachefile
from . import camera as camera
from . import clip as clip
from . import cloth as cloth
from . import console as console
from . import constraint as constraint
from . import curve as curve
from . import cycles as cycles
from . import dpaint as dpaint
from . import ed as ed
from . import export_anim as export_anim
from . import export_mesh as export_mesh
from . import export_scene as export_scene
from . import file as file
from . import fluid as fluid
from . import font as font
from . import gpencil as gpencil
from . import graph as graph
from . import group as group
from . import image as image
from . import import_anim as import_anim
from . import import_curve as import_curve
from . import import_mesh as import_mesh
from . import import_scene as import_scene
from . import info as info
from . import lamp as lamp
from . import lattice as lattice
from . import logic as logic
from . import marker as marker
from . import mask as mask
from . import material as material
from . import mball as mball
from . import mesh as mesh
from . import nla as nla
from . import node as node
from . import object as object
from . import outliner as outliner
from . import paint as paint
from . import paintcurve as paintcurve
from . import palette as palette
from . import particle as particle
from . import pose as pose
from . import poselib as poselib
from . import ptcache as ptcache
from . import render as render
from . import rigidbody as rigidbody
from . import safe_areas as safe_areas
from . import scene as scene
from . import screen as screen
from . import script as script
from . import sculpt as sculpt
from . import sequencer as sequencer
from . import sketch as sketch
from . import sound as sound
from . import surface as surface
from . import text as text
from . import texture as texture
from . import time as time
from . import transform as transform
from . import ui as ui
from . import uv as uv
from . import view2d as view2d
from . import view3d as view3d
from . import wm as wm
from . import world as world

class BPyOps:
    """Fake module like class."""

class BPyOpsSubMod:
    """Utility class to fake submodules.eg. bpy.ops.object"""

class BPyOpsSubModOp:
    def get_rna_type(self):
        """Internal function for introspection"""

    def idname(self): ...
    def idname_py(self): ...
    def poll(self, *args):
        """

        :param args:
        """
