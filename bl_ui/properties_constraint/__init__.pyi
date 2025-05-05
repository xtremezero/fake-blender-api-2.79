import typing
import collections.abc
import typing_extensions
import bpy.types

class BONE_PT_constraints(ConstraintButtonsPanel, bpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class ConstraintButtonsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def ACTION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def CAMERA_SOLVER(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def CHILD_OF(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def CLAMP_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def COPY_LOCATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def COPY_ROTATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def COPY_SCALE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def COPY_TRANSFORMS(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def DAMPED_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def FLOOR(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def FOLLOW_PATH(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def FOLLOW_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def IK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def IK_COPY_POSE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def IK_DISTANCE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def LIMIT_DISTANCE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def LIMIT_LOCATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def LIMIT_ROTATION(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def LIMIT_SCALE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def LOCKED_TRACK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def MAINTAIN_VOLUME(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def OBJECT_SOLVER(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def PIVOT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def RIGID_BODY_JOINT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def SCRIPT(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def SHRINKWRAP(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def SPLINE_IK(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def STRETCH_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def TRACK_TO(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def TRANSFORM(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def TRANSFORM_CACHE(self, context, layout, con):
        """

        :param context:
        :param layout:
        :param con:
        """

    def draw_constraint(self, context, con):
        """

        :param context:
        :param con:
        """

    @staticmethod
    def ik_template(layout, con):
        """

        :param layout:
        :param con:
        """

    @staticmethod
    def space_template(layout, con, target=True, owner=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        """

    @staticmethod
    def target_template(layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
        """

class OBJECT_PT_constraints(ConstraintButtonsPanel, bpy.types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any

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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """
