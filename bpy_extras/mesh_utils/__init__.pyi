import typing
import collections.abc
import typing_extensions
import bpy.types

def edge_face_count(mesh) -> list:
    """

    :return: list face users for each item in mesh.edges.
    :rtype: list
    """

def edge_face_count_dict(mesh) -> dict:
    """

        :return: dict of edge keys with their value set to the number of
    faces using each edge.
        :rtype: dict
    """

def edge_loops_from_edges(mesh, edges=None):
    """Edge loops defined by edgesTakes me.edges or a list of edges and returns the edge loopsreturn a list of vertex indices.
    [ [1, 6, 7, 2], ...]closed loops have matching start and end values.

    """

def edge_loops_from_tessfaces(
    mesh: bpy.types.Mesh,
    tessfaces: bpy.types.MeshTessFace | collections.abc.Sequence | None = None,
    seams=(),
) -> list:
    """Edge loops defined by facesTakes me.tessfaces or a list of faces and returns the edge loops
    These edge loops are the edges that sit between quads, so they don't touch
    1 quad, note: not connected will make 2 edge loops,
    both only containing 2 edges.return a list of edge key lists
    [[(0, 1), (4, 8), (3, 8)], ...]

        :param mesh: the mesh used to get edge loops from.
        :type mesh: bpy.types.Mesh
        :param tessfaces: optional face list to only use some of the meshes faces.
        :type tessfaces: bpy.types.MeshTessFace | collections.abc.Sequence | None
        :return: return a list of edge vertex index lists.
        :rtype: list
    """

def face_random_points(
    num_points, tessfaces: bpy.types.MeshTessFace | collections.abc.Sequence
) -> list:
    """Generates a list of random points over mesh tessfaces.

    :param num_points: the number of random points to generate on each face.
    :param tessfaces: list of the faces to generate points on.
    :type tessfaces: bpy.types.MeshTessFace | collections.abc.Sequence
    :return: list of random points over all faces.
    :rtype: list
    """

def mesh_linked_tessfaces(mesh: bpy.types.Mesh) -> list:
    """Splits the mesh into connected faces, use this for separating cubes from
    other mesh elements within 1 mesh datablock.

        :param mesh: the mesh used to group with.
        :type mesh: bpy.types.Mesh
        :return: lists of lists containing faces.
        :rtype: list
    """

def mesh_linked_uv_islands(mesh: bpy.types.Mesh) -> list:
    """Splits the mesh into connected polygons, use this for separating cubes from
    other mesh elements within 1 mesh datablock.

        :param mesh: the mesh used to group with.
        :type mesh: bpy.types.Mesh
        :return: lists of lists containing polygon indices
        :rtype: list
    """

def ngon_tessellate(
    from_data: bpy.types.Mesh | list, indices: list, fix_loops: bool = True
):
    """Takes a polyline of indices (fgon) and returns a list of face
    index lists. Designed to be used for importers that need indices for an
    fgon to create from existing verts.

        :param from_data: either a mesh, or a list/tuple of vectors.
        :type from_data: bpy.types.Mesh | list
        :param indices: a list of indices to use this list
    is the ordered closed polyline
    to fill, and can be a subset of the data given.
        :type indices: list
        :param fix_loops: If this is enabled polylines
    that use loops to make multiple
    polylines are delt with correctly.
        :type fix_loops: bool
    """
