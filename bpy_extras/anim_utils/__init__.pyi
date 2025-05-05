import typing
import collections.abc
import typing_extensions
import bpy.types

def bake_action(
    obj: bpy.types.Object, *, action: bpy.types.Action | None, frames, **kwargs
) -> bpy.types.Action:
    """

        :param obj: Object to bake.
        :type obj: bpy.types.Object
        :param action: An action to bake the data into, or None for a new action
    to be created.
        :type action: bpy.types.Action | None
        :param frames: Frames to bake.
        :return: an action or None
        :rtype: bpy.types.Action
    """

def bake_action_iter(
    obj: bpy.types.Object,
    *,
    action: bpy.types.Action | None,
    only_selected: bool = False,
    do_pose: bool = True,
    do_object: bool = True,
    do_visual_keying: bool = True,
    do_constraint_clear: bool = False,
    do_parents_clear: bool = False,
    do_clean: bool = False,
) -> bpy.types.Action:
    """An coroutine that bakes action for a single object.

        :param obj: Object to bake.
        :type obj: bpy.types.Object
        :param action: An action to bake the data into, or None for a new action
    to be created.
        :type action: bpy.types.Action | None
        :param only_selected: Only bake selected bones.
        :type only_selected: bool
        :param do_pose: Bake pose channels.
        :type do_pose: bool
        :param do_object: Bake objects.
        :type do_object: bool
        :param do_visual_keying: Use the final transformations for baking ('visual keying')
        :type do_visual_keying: bool
        :param do_constraint_clear: Remove constraints after baking.
        :type do_constraint_clear: bool
        :param do_parents_clear: Unparent after baking objects.
        :type do_parents_clear: bool
        :param do_clean: Remove redundant keyframes after baking.
        :type do_clean: bool
        :return: an action or None
        :rtype: bpy.types.Action
    """

def bake_action_objects(
    object_action_pairs, *, frames, **kwargs
) -> list[bpy.types.Action]:
    """A version of `bake_action_objects_iter` that takes frames and returns the output.

    :param frames: Frames to bake.
    :return: A sequence of Action or None types (aligned with object_action_pairs)
    :rtype: list[bpy.types.Action]
    """

def bake_action_objects_iter(object_action_pairs, **kwargs):
    """An coroutine that bakes actions for multiple objects.

        :param object_action_pairs: Sequence of object action tuples,
    action is the destination for the baked data. When None a new action will be created.
    """
