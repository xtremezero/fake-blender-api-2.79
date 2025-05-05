import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject

class KX_LightObject(bge.types.KX_GameObject.KX_GameObject):
    """A Light object."""

    SPOT: typing.Any
    """ A spot light source. See attribute `type`"""

    SUN: typing.Any
    """ A point light source with no attenuation. See attribute `type`"""

    NORMAL: typing.Any
    """ A point light source. See attribute `type`"""

    HEMI: typing.Any
    """ A hemi light source. See attribute `type`"""

    type: typing.Any
    """ The type of light - must be SPOT, SUN or NORMAL"""

    energy: float
    """ The brightness of this light.

    :type: float
    """

    shadowClipStart: typing.Any
    """ The shadowmap clip start, below which objects will not generate shadows."""

    shadowClipEnd: typing.Any
    """ The shadowmap clip end, beyond which objects will not generate shadows."""

    shadowFrustumSize: typing.Any
    """ Size of the frustum used for creating the shadowmap."""

    shadowBindId: typing.Any
    """ The OpenGL shadow texture bind number/id."""

    shadowMapType: typing.Any
    """ The shadow shadow map type (0 -> Simple; 1 -> Variance)"""

    shadowBias: typing.Any
    """ The shadow buffer sampling bias."""

    shadowBleedBias: typing.Any
    """ The bias for reducing light-bleed on variance shadow maps."""

    useShadow: typing.Any
    """ Returns True if the light has Shadow option activated, else returns False."""

    shadowColor: typing.Any
    """ The color of this light shadows. Black = (0.0, 0.0, 0.0), White = (1.0, 1.0, 1.0)."""

    shadowMatrix: typing.Any
    """ Matrix that converts a vector in camera space to shadow buffer depth space.mat4_perspective_to_depth is a fixed matrix defined as follow:"""

    distance: float
    """ The maximum distance this light can illuminate. (SPOT and NORMAL lights only).

    :type: float
    """

    color: typing.Any
    """ The color of this light. Black = [0.0, 0.0, 0.0], White = [1.0, 1.0, 1.0]."""

    lin_attenuation: float
    """ The linear component of this light's attenuation. (SPOT and NORMAL lights only).

    :type: float
    """

    quad_attenuation: float
    """ The quadratic component of this light's attenuation (SPOT and NORMAL lights only).

    :type: float
    """

    spotsize: typing.Any
    """ The cone angle of the spot light, in degrees (SPOT lights only)."""

    spotblend: float
    """ Specifies the intensity distribution of the spot light (SPOT lights only).

    :type: float
    """

    staticShadow: typing.Any
    """ Enables static shadows. By default (staticShadow=False) the shadow cast by the lamp is recalculated every frame. When this is not needed, set staticShadow=True. In that case, call `updateShadow` to request a shadow update."""

    def updateShadow(self):
        """Set the shadow to be updated next frame if the lamp uses a static shadow, see `staticShadow`."""
