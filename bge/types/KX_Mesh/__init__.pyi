import typing
import collections.abc
import typing_extensions
import bge.types.EXP_Value
import bge.types.KX_BlenderMaterial
import bge.types.KX_PolyProxy
import bge.types.KX_VertexProxy
import mathutils
import mathutils.bvhtree

class KX_Mesh(bge.types.EXP_Value.EXP_Value):
    """A mesh object.You can only change the vertex properties of a mesh object, not the mesh topology.To use mesh objects effectively, you should know a bit about how the game engine handles them.The correct method of iterating over every `KX_VertexProxy` in a game object"""

    materials: typing.Any
    numPolygons: int
    """ 

    :type: int
    """

    numMaterials: int
    """ 

    :type: int
    """

    polygons: typing.Any
    """ Returns the list of polygons of this mesh."""

    def getMaterialName(self, matid: int) -> str:
        """Gets the name of the specified material.

        :param matid: the specified material.
        :type matid: int
        :return: the attached material name.
        :rtype: str
        """

    def getTextureName(self, matid: int) -> str:
        """Gets the name of the specified material's texture.

        :param matid: the specified material
        :type matid: int
        :return: the attached material's texture name.
        :rtype: str
        """

    def getVertexArrayLength(self, matid: int) -> int:
        """Gets the length of the vertex array associated with the specified material.There is one vertex array for each material.

        :param matid: the specified material
        :type matid: int
        :return: the number of verticies in the vertex array.
        :rtype: int
        """

    def getVertex(
        self, matid: int, index: int
    ) -> bge.types.KX_VertexProxy.KX_VertexProxy:
        """Gets the specified vertex from the mesh object.

        :param matid: the specified material
        :type matid: int
        :param index: the index into the vertex array.
        :type index: int
        :return: a vertex object.
        :rtype: bge.types.KX_VertexProxy.KX_VertexProxy
        """

    def getPolygon(self, index: int) -> bge.types.KX_PolyProxy.KX_PolyProxy:
        """Gets the specified polygon from the mesh.

        :param index: polygon number
        :type index: int
        :return: a polygon object.
        :rtype: bge.types.KX_PolyProxy.KX_PolyProxy
        """

    def transform(self, matid: int, matrix):
        """Transforms the vertices of a mesh.

        :param matid: material index, -1 transforms all.
        :type matid: int
        :param matrix: transformation matrix.
        """

    def transformUV(
        self, matid: int, matrix, uv_index: int = -1, uv_index_from: int = -1
    ):
        """Transforms the vertices UV's of a mesh.

        :param matid: material index, -1 transforms all.
        :type matid: int
        :param matrix: transformation matrix.
        :param uv_index: optional uv index, -1 for all, otherwise 0 or 1.
        :type uv_index: int
        :param uv_index_from: optional uv index to copy from, -1 to transform the current uv.
        :type uv_index_from: int
        """

    def replaceMaterial(
        self, matid: int, material: bge.types.KX_BlenderMaterial.KX_BlenderMaterial
    ):
        """Replace the material in slot `matid` by the material `material`.

        :param matid: The material index.
        :type matid: int
        :param material: The material replacement.
        :type material: bge.types.KX_BlenderMaterial.KX_BlenderMaterial
        """

    def copy(self):
        """Return a duplicated mesh.

        :return: a duplicated mesh of the current used.
        """

    def constructBvh(
        self,
        transform: collections.abc.Sequence[collections.abc.Sequence[float]]
        | mathutils.Matrix = mathutils.Matrix.Identity(4),
        epsilon: float = 0,
    ) -> mathutils.bvhtree.BVHTree:
        """Return a BVH tree based on mesh geometry. Indices of tree elements match polygons indices.

        :param transform: The transform 4x4 matrix applied to vertices.
        :type transform: collections.abc.Sequence[collections.abc.Sequence[float]] | mathutils.Matrix
        :param epsilon: The tree distance epsilon.
        :type epsilon: float
        :return: A BVH tree based on mesh geometry.
        :rtype: mathutils.bvhtree.BVHTree
        """
