import typing
import collections.abc
import typing_extensions
import bge.types.KX_TextureRenderer
import mathutils

class KX_PlanarMap(bge.types.KX_TextureRenderer.KX_TextureRenderer):
    """Python API for realtime planar map textures."""

    normal: mathutils.Vector
    """ Plane normal used to compute the reflection or refraction orientation of the render camera.

    :type: mathutils.Vector
    """
