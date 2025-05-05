import typing
import collections.abc
import typing_extensions
import bge.types.KX_BlenderMaterial
import bge.types.SCA_IObject

class KX_PolyProxy(bge.types.SCA_IObject.SCA_IObject):
    """A polygon holds the index of the vertex forming the poylgon.Note:
    The polygon attributes are read-only, you need to retrieve the vertex proxy if you want
    to change the vertex settings.
    """

    material_name: str
    """ The name of polygon material, empty if no material.

    :type: str
    """

    material: bge.types.KX_BlenderMaterial.KX_BlenderMaterial
    """ The material of the polygon.

    :type: bge.types.KX_BlenderMaterial.KX_BlenderMaterial
    """

    texture_name: str
    """ The texture name of the polygon.

    :type: str
    """

    material_id: int
    """ The material index of the polygon, use this to retrieve vertex proxy from mesh proxy.

    :type: int
    """

    v1: int
    """ vertex index of the first vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

    :type: int
    """

    v2: int
    """ vertex index of the second vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

    :type: int
    """

    v3: int
    """ vertex index of the third vertex of the polygon, use this to retrieve vertex proxy from mesh proxy.

    :type: int
    """

    v4: int
    """ polygons are triangles.

    :type: int
    """

    visible: int
    """ visible state of the polygon: 1=visible, 0=invisible.

    :type: int
    """

    collide: int
    """ collide state of the polygon: 1=receives collision, 0=collision free.

    :type: int
    """

    vertices: typing.Any
    """ Returns the list of vertices of this polygon."""

    def getMaterialName(self) -> str:
        """Returns the polygon material name with MA prefix

        :return: material name
        :rtype: str
        """

    def getMaterial(self) -> bge.types.KX_BlenderMaterial.KX_BlenderMaterial:
        """

        :return: The polygon material
        :rtype: bge.types.KX_BlenderMaterial.KX_BlenderMaterial
        """

    def getTextureName(self) -> str:
        """

        :return: The texture name
        :rtype: str
        """

    def getMaterialIndex(self) -> int:
        """Returns the material bucket index of the polygon.
        This index and the ones returned by getVertexIndex() are needed to retrieve the vertex proxy from `MeshProxy`.

                :return: the material index in the mesh
                :rtype: int
        """

    def getNumVertex(self) -> int:
        """Returns the number of vertex of the polygon.

        :return: number of vertex.
        :rtype: int
        """

    def isVisible(self) -> bool:
        """Returns whether the polygon is visible or not

        :return: 0=invisible, 1=visible
        :rtype: bool
        """

    def isCollider(self) -> int:
        """Returns whether the polygon is receives collision or not

        :return: 0=collision free, 1=receives collision
        :rtype: int
        """

    def getVertexIndex(self, vertex) -> int:
        """Returns the mesh vertex index of a polygon vertex
        This index and the one returned by getMaterialIndex() are needed to retrieve the vertex proxy from `MeshProxy`.

                :param vertex: index of the vertex in the polygon: 0->2integer
                :return: mesh vertex index
                :rtype: int
        """

    def getMesh(self):
        """Returns a mesh proxy

        :return: mesh proxy
        """
