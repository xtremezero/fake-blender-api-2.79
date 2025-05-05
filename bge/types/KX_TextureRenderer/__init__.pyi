import typing
import collections.abc
import typing_extensions
import bge.types.EXP_Value
import bge.types.KX_GameObject

class KX_TextureRenderer(bge.types.EXP_Value.EXP_Value):
    """Python API for object doing a render stored in a texture."""

    autoUpdate: bool
    """ Choose to update automatically each frame the texture renderer or not.

    :type: bool
    """

    viewpointObject: bge.types.KX_GameObject.KX_GameObject
    """ The object where the texture renderer will render the scene.

    :type: bge.types.KX_GameObject.KX_GameObject
    """

    enabled: bool
    """ Enable the texture renderer to render the scene.

    :type: bool
    """

    ignoreLayers: typing.Any
    """ The layers to ignore when rendering."""

    clipStart: float
    """ The projection view matrix near plane, used for culling.

    :type: float
    """

    clipEnd: float
    """ The projection view matrix far plane, used for culling.

    :type: float
    """

    lodDistanceFactor: float
    """ The factor to multiply distance to camera to adjust levels of detail.
A float < 1.0f will make the distance to camera used to compute
levels of detail decrease.

    :type: float
    """

    def update(self):
        """Request to update this texture renderer during the rendering stage. This function is effective only when `autoUpdate` is disabled."""
