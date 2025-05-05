import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus
import mathutils

class KX_WorldInfo(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """A world object."""

    KX_MIST_QUADRATIC: typing.Any
    """ Type of quadratic attenuation used to fade mist."""

    KX_MIST_LINEAR: typing.Any
    """ Type of linear attenuation used to fade mist."""

    KX_MIST_INV_QUADRATIC: typing.Any
    """ Type of inverse quadratic attenuation used to fade mist."""

    mistEnable: bool
    """ Return the state of the mist.

    :type: bool
    """

    mistStart: float
    """ The mist start point.

    :type: float
    """

    mistDistance: float
    """ The mist distance fom the start point to reach 100% mist.

    :type: float
    """

    mistIntensity: float
    """ The mist intensity.

    :type: float
    """

    mistType: typing.Any
    """ The type of mist - must be KX_MIST_QUADRATIC, KX_MIST_LINEAR or KX_MIST_INV_QUADRATIC"""

    mistColor: mathutils.Color
    """ The color of the mist. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].
Mist and background color sould always set to the same color.

    :type: mathutils.Color
    """

    horizonColor: mathutils.Vector
    """ The horizon color. Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0].
Mist and horizon color should always be set to the same color.

    :type: mathutils.Vector
    """

    zenithColor: mathutils.Vector
    """ The zenith color. Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0].

    :type: mathutils.Vector
    """

    ambientColor: mathutils.Color
    """ The color of the ambient light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0].

    :type: mathutils.Color
    """

    exposure: typing.Any
    """ Amount of exponential color correction for light."""

    range: typing.Any
    """ The color range that will be mapped to 0 - 1."""

    envLightEnergy: typing.Any
    """ The environment light energy."""

    envLightEnabled: typing.Any
    """ Returns True if Environment Lighting is enabled. Else returns False"""

    envLightColor: typing.Any
    """ White:       returns 0
SkyColor:    returns 1
SkyTexture:  returns 2"""
