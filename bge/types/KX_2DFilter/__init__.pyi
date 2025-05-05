import typing
import collections.abc
import typing_extensions
import bge.types.BL_Shader

class KX_2DFilter(bge.types.BL_Shader.BL_Shader):
    """2D filter shader object. Can be alterated with `BL_Shader`'s functions."""

    mipmap: bool
    """ Request mipmap generation of the render bgl_RenderedTexture texture. Accessing mipmapping level is similar to:

    :type: bool
    """

    offScreen: typing.Any
    """ The custom off screen the filter render to (read-only)."""

    def setTexture(self, index: int, bindCode: int, samplerName: str = ""):
        """Set specified texture bind code `bindCode` in specified slot `index`. Any call to `setTexture`
        should be followed by a call to `BL_Shader.setSampler` with the same `index` if `sampleName` is not specified.

                :param index: The texture slot.
                :type index: int
                :param bindCode: The texture bind code/Id.
                :type bindCode: int
                :param samplerName: The shader sampler name set to `index` if `samplerName` is passed in the function. (optional)
                :type samplerName: str
        """

    def setCubeMap(self, index: int, bindCode: int, samplerName: str = ""):
        """Set specified cube map texture bind code `bindCode` in specified slot `index`. Any call to `setCubeMap`
        should be followed by a call to `BL_Shader.setSampler` with the same `index` if `sampleName` is not specified.

                :param index: The texture slot.
                :type index: int
                :param bindCode: The cube map texture bind code/Id.
                :type bindCode: int
                :param samplerName: The shader sampler name set to `index` if `samplerName` is passed in the function. (optional)
                :type samplerName: str
        """

    def addOffScreen(
        self,
        slots: int,
        depth: bool = False,
        width: int = -1,
        height: int = -1,
        hdr=bge.render.HDR_NONE,
        mipmap: bool = False,
    ):
        """Register a custom off screen to render the filter to.

        :param slots: The number of color texture attached to the off screen, between 0 and 8 excluded.
        :type slots: int
        :param depth: True of the off screen use a depth texture (optional).
        :type depth: bool
        :param width: The off screen width, -1 if it can be resized dynamically when the viewport dimensions changed (optional).
        :type width: int
        :param height: The off screen height, -1 if it can be resized dynamically when the viewport dimensions changed (optional).
        :type height: int
        :param hdr: The image quality HDR of the color textures (optional).
        :param mipmap: True if the color texture generate mipmap at the end of the filter rendering (optional).
        :type mipmap: bool
        """

    def removeOffScreen(self):
        """Unregister the custom off screen the filter render to."""
