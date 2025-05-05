import typing
import collections.abc
import typing_extensions
import bge.types.EXP_Value
import bge.types.KX_CubeMap
import bge.types.KX_PlanarMap
import mathutils

class BL_Texture(bge.types.EXP_Value.EXP_Value):
    """A texture object that contains attributes of a material texture."""

    diffuseIntensity: float
    """ Amount texture affects diffuse reflectivity.

    :type: float
    """

    diffuseFactor: float
    """ Amount texture affects diffuse color.

    :type: float
    """

    alpha: float
    """ Amount texture affects alpha.

    :type: float
    """

    specularIntensity: float
    """ Amount texture affects specular reflectivity.

    :type: float
    """

    specularFactor: float
    """ Amount texture affects specular color.

    :type: float
    """

    hardness: float
    """ Amount texture affects hardness.

    :type: float
    """

    emit: float
    """ Amount texture affects emission.

    :type: float
    """

    mirror: float
    """ Amount texture affects mirror color.

    :type: float
    """

    normal: float
    """ Amount texture affects normal values.

    :type: float
    """

    parallaxBump: float
    """ Height of parallax occlusion mapping.

    :type: float
    """

    parallaxStep: float
    """ Number of steps to achieve parallax effect.

    :type: float
    """

    lodBias: float
    """ Amount bias on mipmapping.

    :type: float
    """

    bindCode: int
    """ Texture bind code/Id/number.

    :type: int
    """

    renderer: bge.types.KX_CubeMap.KX_CubeMap | bge.types.KX_PlanarMap.KX_PlanarMap | None
    """ Texture renderer of this texture.

    :type: bge.types.KX_CubeMap.KX_CubeMap | bge.types.KX_PlanarMap.KX_PlanarMap | None
    """

    ior: typing.Any
    """ Index Of Refraction used to compute refraction."""

    refractionRatio: typing.Any
    """ Amount refraction mixed with reflection."""

    uvOffset: mathutils.Vector
    """ Offset applied to texture UV coordinates (mainly translation on U and V axis).

    :type: mathutils.Vector
    """

    uvSize: mathutils.Vector
    """ Scale applied to texture UV coordinates.

    :type: mathutils.Vector
    """

    uvRotation: typing.Any
    """ Rotation applied to texture UV coordinates."""
