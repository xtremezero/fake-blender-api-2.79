"""
BVH tree structures for proximity searches and ray casts on geometry.

"""

import typing
import collections.abc
import typing_extensions
import bmesh.types
import bpy.types
import mathutils

class BVHTree:
    @classmethod
    def FromBMesh(cls, bmesh: bmesh.types.BMesh, epsilon: float = 0.0):
        """BVH tree based on `BMesh` data.

        :param bmesh: BMesh data.
        :type bmesh: bmesh.types.BMesh
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :type epsilon: float
        """

    @classmethod
    def FromObject(
        cls,
        object: bpy.types.Object,
        scene: bpy.types.Scene,
        deform: bool = True,
        render: bool = False,
        cage: bool = False,
        epsilon: float = 0.0,
    ):
        """BVH tree based on `Object` data.

        :param object: Object data.
        :type object: bpy.types.Object
        :param scene: Scene data to use for evaluating the mesh.
        :type scene: bpy.types.Scene
        :param deform: Use mesh with deformations.
        :type deform: bool
        :param render: Use render settings.
        :type render: bool
        :param cage: Use render settings.
        :type cage: bool
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :type epsilon: float
        """

    @classmethod
    def FromPolygons(
        cls, vertices, polygons, all_triangles: bool = False, epsilon: float = 0.0
    ):
        """BVH tree constructed geometry passed in as arguments.

        :param vertices: float triplets each representing (x, y, z)
        :param polygons: Sequence of polyugons, each containing indices to the vertices argument.
        :param all_triangles: Use when all polygons are triangles for more efficient conversion.
        :type all_triangles: bool
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :type epsilon: float
        """

    def find_nearest(self, origin, distance: float = 1.84467e19) -> tuple:
        """Find the nearest element (typically face index) to a point.

                :param origin:
                :param distance: Maximum distance threshold.
                :type distance: float
                :return: Returns a tuple
        (`Vector` location, `Vector` normal, int index, float distance),
        Values will all be None if no hit is found.
                :rtype: tuple
        """

    def find_nearest_range(self, origin, distance: float = 1.84467e19) -> list:
        """Find the nearest elements (typically face index) to a point in the distance range.

                :param origin:
                :param distance: Maximum distance threshold.
                :type distance: float
                :return: Returns a list of tuples
        (`Vector` location, `Vector` normal, int index, float distance),
                :rtype: list
        """

    def overlap(self, other_tree: typing_extensions.Self) -> list:
        """Find overlapping indices between 2 trees.

        :param other_tree: Other tree to perform overlap test on.
        :type other_tree: typing_extensions.Self
        :return: Returns a list of unique index pairs,      the first index referencing this tree, the second referencing the other_tree.
        :rtype: list
        """

    def ray_cast(
        self,
        origin,
        direction: collections.abc.Sequence[float] | mathutils.Vector,
        distance: float = sys.float_info.max,
    ) -> tuple:
        """Cast a ray onto the mesh.

                :param origin:
                :param direction: Direction of the ray in object space.
                :type direction: collections.abc.Sequence[float] | mathutils.Vector
                :param distance: Maximum distance threshold.
                :type distance: float
                :return: Returns a tuple
        (`Vector` location, `Vector` normal, int index, float distance),
        Values will all be None if no hit is found.
                :rtype: tuple
        """

    def __init__(self, size):
        """

        :param size:
        """
