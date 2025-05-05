import typing
import collections.abc
import typing_extensions
import bpy.types

class DATA_PT_modifiers(ModifierButtonsPanel, bpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

    def ARMATURE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def ARRAY(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def BEVEL(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def BOOLEAN(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def BUILD(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def CAST(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def CLOTH(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def COLLISION(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def CORRECTIVE_SMOOTH(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def CURVE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def DATA_TRANSFER(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def DECIMATE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def DISPLACE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def DYNAMIC_PAINT(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def EDGE_SPLIT(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def EXPLODE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def FLUID_SIMULATION(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def HOOK(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def LAPLACIANDEFORM(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def LAPLACIANSMOOTH(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def LATTICE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def MASK(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def MESH_CACHE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def MESH_DEFORM(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def MESH_SEQUENCE_CACHE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def MIRROR(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def MULTIRES(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def NORMAL_EDIT(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def OCEAN(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def PARTICLE_INSTANCE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def PARTICLE_SYSTEM(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def REMESH(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SCREW(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SHRINKWRAP(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SIMPLE_DEFORM(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SKIN(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SMOKE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SMOOTH(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SOFT_BODY(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SOLIDIFY(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SUBSURF(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SURFACE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def SURFACE_DEFORM(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def TRIANGULATE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def UV_PROJECT(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def UV_WARP(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def VERTEX_WEIGHT_EDIT(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def VERTEX_WEIGHT_MIX(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def VERTEX_WEIGHT_PROXIMITY(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def WARP(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def WAVE(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

    def WIREFRAME(self, layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

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

    def draw(self, context):
        """

        :param context:
        """

    @staticmethod
    def vertex_weight_mask(layout, ob, md):
        """

        :param layout:
        :param ob:
        :param md:
        """

class ModifierButtonsPanel:
    bl_context: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any
