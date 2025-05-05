import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IObject

class KX_VertexProxy(bge.types.SCA_IObject.SCA_IObject):
    """A vertex holds position, UV, color and normal information.Note:
    The physics simulation is NOT currently updated - physics will not respond
    to changes in the vertex position.
    """

    XYZ: typing.Any
    """ The position of the vertex."""

    UV: typing.Any
    """ The texture coordinates of the vertex."""

    uvs: typing.Any
    """ The texture coordinates list of the vertex."""

    normal: typing.Any
    """ The normal of the vertex."""

    color: typing.Any
    """ The color of the vertex.Black = [0.0, 0.0, 0.0, 1.0], White = [1.0, 1.0, 1.0, 1.0]"""

    colors: typing.Any
    """ The color list of the vertex."""

    x: float
    """ The x coordinate of the vertex.

    :type: float
    """

    y: float
    """ The y coordinate of the vertex.

    :type: float
    """

    z: float
    """ The z coordinate of the vertex.

    :type: float
    """

    u: float
    """ The u texture coordinate of the vertex.

    :type: float
    """

    v: float
    """ The v texture coordinate of the vertex.

    :type: float
    """

    u2: float
    """ The second u texture coordinate of the vertex.

    :type: float
    """

    v2: float
    """ The second v texture coordinate of the vertex.

    :type: float
    """

    r: float
    """ The red component of the vertex color. 0.0 <= r <= 1.0.

    :type: float
    """

    g: float
    """ The green component of the vertex color. 0.0 <= g <= 1.0.

    :type: float
    """

    b: float
    """ The blue component of the vertex color. 0.0 <= b <= 1.0.

    :type: float
    """

    a: float
    """ The alpha component of the vertex color. 0.0 <= a <= 1.0.

    :type: float
    """

    def getXYZ(self):
        """Gets the position of this vertex.

        :return: this vertexes position in local coordinates.
        """

    def setXYZ(self, pos):
        """Sets the position of this vertex.

        :param pos: the new position for this vertex in local coordinates.
        """

    def getUV(self):
        """Gets the UV (texture) coordinates of this vertex.

        :return: this vertexes UV (texture) coordinates.
        """

    def setUV(self, uv):
        """Sets the UV (texture) coordinates of this vertex.

        :param uv:
        """

    def getUV2(self):
        """Gets the 2nd UV (texture) coordinates of this vertex.

        :return: this vertexes UV (texture) coordinates.
        """

    def setUV2(self, uv, unit):
        """Sets the 2nd UV (texture) coordinates of this vertex.

        :param uv:
        :param unit: optional argument, FLAT==1, SECOND_UV==2, defaults to SECOND_UVinteger
        """

    def getRGBA(self) -> int:
        """Gets the color of this vertex.The color is represented as four bytes packed into an integer value.  The color is
        packed as RGBA.Since Python offers no way to get each byte without shifting, you must use the struct module to
        access color in an machine independent way.Because of this, it is suggested you use the r, g, b and a attributes or the color attribute instead.

                :return: packed color. 4 byte integer with one byte per color channel in RGBA format.
                :rtype: int
        """

    def setRGBA(self, col: int):
        """Sets the color of this vertex.See getRGBA() for the format of col, and its relevant problems.  Use the r, g, b and a attributes
        or the color attribute instead.setRGBA() also accepts a four component list as argument col.  The list represents the color as [r, g, b, a]
        with black = [0.0, 0.0, 0.0, 1.0] and white = [1.0, 1.0, 1.0, 1.0]

                :param col: the new color of this vertex in packed RGBA format.
                :type col: int
        """

    def getNormal(self):
        """Gets the normal vector of this vertex.

        :return: normalized normal vector.
        """

    def setNormal(self, normal):
        """Sets the normal vector of this vertex.

        :param normal: the new normal of this vertex.
        """
