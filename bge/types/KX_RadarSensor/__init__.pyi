import typing
import collections.abc
import typing_extensions
import bge.types.KX_NearSensor
import mathutils

class KX_RadarSensor(bge.types.KX_NearSensor.KX_NearSensor):
    """Radar sensor is a near sensor with a conical sensor object."""

    coneOrigin: mathutils.Vector
    """ The origin of the cone with which to test. The origin is in the middle of the cone. (read-only).

    :type: mathutils.Vector
    """

    coneTarget: mathutils.Vector
    """ The center of the bottom face of the cone with which to test. (read-only).

    :type: mathutils.Vector
    """

    distance: float
    """ The height of the cone with which to test.

    :type: float
    """

    angle: float
    """ The angle of the cone (in degrees) with which to test.

    :type: float
    """

    axis: typing.Any
    """ The axis on which the radar cone is cast.KX_RADAR_AXIS_POS_X, KX_RADAR_AXIS_POS_Y, KX_RADAR_AXIS_POS_Z,
KX_RADAR_AXIS_NEG_X, KX_RADAR_AXIS_NEG_Y, KX_RADAR_AXIS_NEG_Z"""
