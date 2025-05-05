import typing
import collections.abc
import typing_extensions
import bge.types.BL_Shader
import bge.types.EXP_PyObjectPlus
import mathutils

class KX_BlenderMaterial(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """This is the interface to materials in the game engine.Materials define the render state to be applied to mesh objects.The example below shows a simple GLSL shader setup allowing to dynamically mix two texture channels
    in a material. All materials of the object executing this script should have two textures using
    separate UV maps in the two first texture channels.The code works for both Multitexture and GLSL rendering modes.
    """

    shader: bge.types.BL_Shader.BL_Shader
    """ The material's shader.

    :type: bge.types.BL_Shader.BL_Shader
    """

    blending: tuple[int, int]
    """ Ints used for pixel blending, (src, dst), matching the setBlending method.

    :type: tuple[int, int]
    """

    alpha: typing.Any
    """ The material's alpha transparency."""

    hardness: typing.Any
    """ How hard (sharp) the material's specular reflection is."""

    emit: typing.Any
    """ Amount of light to emit."""

    ambient: typing.Any
    """ Amount of ambient light on the material."""

    specularAlpha: typing.Any
    """ Alpha transparency for specular areas."""

    specularIntensity: typing.Any
    """ How intense (bright) the material's specular reflection is."""

    diffuseIntensity: typing.Any
    """ The material's amount of diffuse reflection."""

    specularColor: mathutils.Color
    """ The material's specular color.

    :type: mathutils.Color
    """

    diffuseColor: mathutils.Color
    """ The material's diffuse color.

    :type: mathutils.Color
    """

    textures: typing.Any
    """ List of all material's textures."""

    def getShader(self) -> bge.types.BL_Shader.BL_Shader:
        """Returns the material's shader.

        :return: the material's shader
        :rtype: bge.types.BL_Shader.BL_Shader
        """

    def getTextureBindcode(self, textureslot: int) -> int:
        """Returns the material's texture OpenGL bind code/id/number/name.use :py:meth:`bge.types.BL_Texture.bindCode`

        :param textureslot: Specifies the texture slot number
        :type textureslot: int
        :return: the material's texture OpenGL bind code/id/number/name
        :rtype: int
        """

    def setBlending(self, src: int, dest: int):
        """Set the pixel color arithmetic functions.

                :param src: Specifies how the red, green, blue, and alpha source blending factors are computed, one of...

        `~bgl.GL_ZERO`

        `~bgl.GL_ONE`

        `~bgl.GL_SRC_COLOR`

        `~bgl.GL_ONE_MINUS_SRC_COLOR`

        `~bgl.GL_DST_COLOR`

        `~bgl.GL_ONE_MINUS_DST_COLOR`

        `~bgl.GL_SRC_ALPHA`

        `~bgl.GL_ONE_MINUS_SRC_ALPHA`

        `~bgl.GL_DST_ALPHA`

        `~bgl.GL_ONE_MINUS_DST_ALPHA`

        `~bgl.GL_SRC_ALPHA_SATURATE`
                :type src: int
                :param dest: Specifies how the red, green, blue, and alpha destination blending factors are computed, one of...

        `~bgl.GL_ZERO`

        `~bgl.GL_ONE`

        `~bgl.GL_SRC_COLOR`

        `~bgl.GL_ONE_MINUS_SRC_COLOR`

        `~bgl.GL_DST_COLOR`

        `~bgl.GL_ONE_MINUS_DST_COLOR`

        `~bgl.GL_SRC_ALPHA`

        `~bgl.GL_ONE_MINUS_SRC_ALPHA`

        `~bgl.GL_DST_ALPHA`

        `~bgl.GL_ONE_MINUS_DST_ALPHA`

        `~bgl.GL_SRC_ALPHA_SATURATE`
                :type dest: int
        """
