import typing
import collections.abc
import typing_extensions
import bpy.types

class SmartProject(bpy.types.Operator):
    """This script projection unwraps the selected faces of a mesh (it operates on all selected mesh objects, and can be used to unwrap selected faces, or all faces)"""

    angle_limit: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    island_margin: typing.Any
    order: typing.Any
    stretch_to_bounds: typing.Any
    use_aspect: typing.Any
    user_area_weight: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def execute(self, context):
        """

        :param context:
        """

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class thickface: ...

def VectoQuat(vec): ...
def boundsIsland(faces): ...
def getUvIslands(faceGroups, me): ...
def island2Edge(island): ...
def islandIntersectUvIsland(source, target, SourceOffset): ...
def main(
    context,
    island_margin,
    projection_limit,
    user_area_weight,
    use_aspect,
    stretch_to_bounds,
): ...
def main_consts(): ...
def mergeUvIslands(islandList): ...
def optiRotateUvIsland(faces): ...
def packIslands(islandList): ...
def pointInIsland(pt, island): ...
def pointInTri2D(v, v1, v2, v3): ...
def rotate_uvs(uv_points, angle): ...
