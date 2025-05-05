import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject

class KX_NavMeshObject(bge.types.KX_GameObject.KX_GameObject):
    """Python interface for using and controlling navigation meshes."""

    def findPath(self, start, goal):
        """Finds the path from start to goal points.

        :param start: the start point3D Vector3D Vector
        :param goal: the goal point
        :return: a path as a list of points
        """

    def raycast(self, start, goal) -> float:
        """Raycast from start to goal points.

        :param start: the start point3D Vector3D Vector
        :param goal: the goal point
        :return: the hit factor
        :rtype: float
        """

    def draw(self, mode):
        """Draws a debug mesh for the navigation mesh.

        :param mode: the drawing mode (one of `these constants <navmesh-draw-mode>`)integer
        :return: None
        """

    def rebuild(self):
        """Rebuild the navigation mesh.

        :return: None
        """
