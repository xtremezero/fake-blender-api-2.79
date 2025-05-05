import typing
import collections.abc
import typing_extensions
import bpy.types

class BUILTIN_KSI_Available(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the already existing F-Curves"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
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

    def poll(self, ksi, context):
        """

        :param ksi:
        :param context:
        """

class BUILTIN_KSI_BendyBones(bpy.types.KeyingSetInfo):
    """Insert a keyframe for each of the BBone shape properties"""

    bl_label: typing.Any
    bl_rna: typing.Any
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

class BUILTIN_KSI_DeltaLocation(bpy.types.KeyingSetInfo):
    """Insert keyframes for additional location offset"""

    bl_label: typing.Any
    bl_rna: typing.Any
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

    def generate(self, ksi, context, ks, data):
        """

        :param ksi:
        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_DeltaRotation(bpy.types.KeyingSetInfo):
    """Insert keyframes for additional rotation offset"""

    bl_label: typing.Any
    bl_rna: typing.Any
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

    def generate(self, ksi, context, ks, data):
        """

        :param ksi:
        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_DeltaScale(bpy.types.KeyingSetInfo):
    """Insert keyframes for additional scaling factor"""

    bl_label: typing.Any
    bl_rna: typing.Any
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

    def generate(self, ksi, context, ks, data):
        """

        :param ksi:
        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_LocRot(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the location and rotation channels"""

    bl_label: typing.Any
    bl_rna: typing.Any
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

    def generate(self, context, ks, data):
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_LocRotScale(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the location, rotation, and scale channels"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
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

    def generate(self, context, ks, data):
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_LocScale(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the location and scale channels"""

    bl_label: typing.Any
    bl_rna: typing.Any
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

    def generate(self, context, ks, data):
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_Location(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the location channels"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
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

class BUILTIN_KSI_RotScale(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the rotation and scale channels"""

    bl_label: typing.Any
    bl_rna: typing.Any
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

    def generate(self, context, ks, data):
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_Rotation(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the rotation channels"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
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

class BUILTIN_KSI_Scaling(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the scale channels"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
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

class BUILTIN_KSI_VisualLoc(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the location channels, taking into account effects of constraints"""

    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
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

class BUILTIN_KSI_VisualLocRot(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the location and rotation channels, taking into account effects of constraints"""

    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
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

    def generate(self, context, ks, data):
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_VisualLocRotScale(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the location, rotation and scaling channels, taking into account effects"""

    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
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

    def generate(self, context, ks, data):
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_VisualLocScale(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the location and scaling channels, taking into account effects of constraints"""

    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
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

    def generate(self, context, ks, data):
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_VisualRot(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the rotation channels, taking into account effects of constraints"""

    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
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

class BUILTIN_KSI_VisualRotScale(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the rotation and scaling channels, taking into account effects of constraints"""

    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
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

    def generate(self, context, ks, data):
        """

        :param context:
        :param ks:
        :param data:
        """

class BUILTIN_KSI_VisualScaling(bpy.types.KeyingSetInfo):
    """Insert a keyframe on each of the scale channels, taking into account effects of constraints"""

    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
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

class BUILTIN_KSI_WholeCharacter(bpy.types.KeyingSetInfo):
    """Insert a keyframe for all properties that are likely to get animated in a character rig"""

    badBonePrefixes: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def addProp(self, ksi, ks, bone, prop, index=-1, use_groups=True):
        """

        :param ksi:
        :param ks:
        :param bone:
        :param prop:
        :param index:
        :param use_groups:
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

    def doBBone(self, ksi, context, ks, pchan):
        """

        :param ksi:
        :param context:
        :param ks:
        :param pchan:
        """

    def doCustomProps(self, ksi, ks, bone):
        """

        :param ksi:
        :param ks:
        :param bone:
        """

    def doLoc(self, ksi, ks, bone):
        """

        :param ksi:
        :param ks:
        :param bone:
        """

    def doRot3d(self, ksi, ks, bone):
        """

        :param ksi:
        :param ks:
        :param bone:
        """

    def doRot4d(self, ksi, ks, bone):
        """

        :param ksi:
        :param ks:
        :param bone:
        """

    def doScale(self, ksi, ks, bone):
        """

        :param ksi:
        :param ks:
        :param bone:
        """

    def generate(self, ksi, context, ks, bone):
        """

        :param ksi:
        :param context:
        :param ks:
        :param bone:
        """

    def iterator(self, ksi, context, ks):
        """

        :param ksi:
        :param context:
        :param ks:
        """

    def poll(self, ksi, context):
        """

        :param ksi:
        :param context:
        """

class BUILTIN_KSI_WholeCharacterSelected(bpy.types.KeyingSetInfo):
    """Insert a keyframe for all properties that are likely to get animated in a character rig"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_rna: typing.Any
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

    def iterator(self, ksi, context, ks):
        """

        :param ksi:
        :param context:
        :param ks:
        """

def register(): ...
def unregister(): ...
