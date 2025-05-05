import typing
import collections.abc
import typing_extensions
import bpy.types

def action_pushdown(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    channel_index: int | None = -1,
):
    """Push action down onto the top of the NLA stack as a new strip

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param channel_index: Channel Index, Index of NLA action channel to perform pushdown operation on
    :type channel_index: int | None
    """

def action_sync_length(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    active: bool | None = True,
):
    """Synchronize the length of the referenced Action with the length used in the strip

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param active: Active Strip Only, Only sync the active length for the active strip
    :type active: bool | None
    """

def action_unlink(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    force_delete: bool | None = False,
):
    """Unlink this action from the active action slot (and/or exit Tweak Mode)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this datablock's NLA stack
    :type force_delete: bool | None
    """

def actionclip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: str | None = "",
):
    """Add an Action-Clip strip (i.e. an NLA Strip referencing an Action) to the active track

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param action: Action
    :type action: str | None
    """

def apply_scale(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply scaling of selected strips to their referenced Actions

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def bake(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame_start: int | None = 1,
    frame_end: int | None = 250,
    step: int | None = 1,
    only_selected: bool | None = True,
    visual_keying: bool | None = False,
    clear_constraints: bool | None = False,
    clear_parents: bool | None = False,
    use_current_action: bool | None = False,
    bake_types: set[typing.Literal["POSE", "OBJECT"]] | None = {"POSE"},
):
    """Bake all selected objects loc/scale/rotation animation to an action

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param frame_start: Start Frame, Start frame for baking
        :type frame_start: int | None
        :param frame_end: End Frame, End frame for baking
        :type frame_end: int | None
        :param step: Frame Step, Frame Step
        :type step: int | None
        :param only_selected: Only Selected Bones, Only key selected bones (Pose baking only)
        :type only_selected: bool | None
        :param visual_keying: Visual Keying, Keyframe from the final transformations (with constraints applied)
        :type visual_keying: bool | None
        :param clear_constraints: Clear Constraints, Remove all constraints from keyed object/bones, and do 'visual' keying
        :type clear_constraints: bool | None
        :param clear_parents: Clear Parents, Bake animation onto the object then clear parents (objects only)
        :type clear_parents: bool | None
        :param use_current_action: Overwrite Current Action, Bake animation into current action, instead of creating a new one (useful for baking only part of bones in an armature)
        :type use_current_action: bool | None
        :param bake_types: Bake Data, Which data's transformations to bake

    POSE Pose, Bake bones transformations.

    OBJECT Object, Bake object transformations.
        :type bake_types: set[typing.Literal['POSE','OBJECT']] | None
    """

def channels_click(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
):
    """Handle clicks to select NLA channels

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend Select
    :type extend: bool | None
    """

def clear_scale(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset scaling of selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def click_select(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
):
    """Handle clicks to select NLA Strips

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend Select
    :type extend: bool | None
    """

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    linked: bool | None = False,
    mode: typing.Literal[
        "INIT",
        "DUMMY",
        "TRANSLATION",
        "ROTATION",
        "RESIZE",
        "SKIN_RESIZE",
        "TOSPHERE",
        "SHEAR",
        "BEND",
        "SHRINKFATTEN",
        "TILT",
        "TRACKBALL",
        "PUSHPULL",
        "CREASE",
        "MIRROR",
        "BONE_SIZE",
        "BONE_ENVELOPE",
        "BONE_ENVELOPE_DIST",
        "CURVE_SHRINKFATTEN",
        "MASK_SHRINKFATTEN",
        "GPENCIL_SHRINKFATTEN",
        "BONE_ROLL",
        "TIME_TRANSLATE",
        "TIME_SLIDE",
        "TIME_SCALE",
        "TIME_EXTEND",
        "BAKE_TIME",
        "BWEIGHT",
        "ALIGN",
        "EDGESLIDE",
        "SEQSLIDE",
    ]
    | None = "TRANSLATION",
):
    """Duplicate selected NLA-Strips, adding the new strips in new tracks above the originals

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param linked: Linked, When duplicating strips, assign new copies of the actions they use
    :type linked: bool | None
    :param mode: Mode
    :type mode: typing.Literal['INIT','DUMMY','TRANSLATION','ROTATION','RESIZE','SKIN_RESIZE','TOSPHERE','SHEAR','BEND','SHRINKFATTEN','TILT','TRACKBALL','PUSHPULL','CREASE','MIRROR','BONE_SIZE','BONE_ENVELOPE','BONE_ENVELOPE_DIST','CURVE_SHRINKFATTEN','MASK_SHRINKFATTEN','GPENCIL_SHRINKFATTEN','BONE_ROLL','TIME_TRANSLATE','TIME_SLIDE','TIME_SCALE','TIME_EXTEND','BAKE_TIME','BWEIGHT','ALIGN','EDGESLIDE','SEQSLIDE'] | None
    """

def fmodifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "NULL",
        "GENERATOR",
        "FNGENERATOR",
        "ENVELOPE",
        "CYCLES",
        "NOISE",
        "LIMITS",
        "STEPPED",
    ]
    | None = "NULL",
    only_active: bool | None = True,
):
    """Add F-Modifier to the active/selected NLA-Strips

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    NULL Invalid.

    GENERATOR Generator, Generate a curve using a factorized or expanded polynomial.

    FNGENERATOR Built-In Function, Generate a curve using standard math functions such as sin and cos.

    ENVELOPE Envelope, Reshape F-Curve values - e.g. change amplitude of movements.

    CYCLES Cycles, Cyclic extend/repeat keyframe sequence.

    NOISE Noise, Add pseudo-random noise on top of F-Curves.

    LIMITS Limits, Restrict maximum and minimum values of F-Curve.

    STEPPED Stepped Interpolation, Snap values to nearest grid-step - e.g. for a stop-motion look.
        :type type: typing.Literal['NULL','GENERATOR','FNGENERATOR','ENVELOPE','CYCLES','NOISE','LIMITS','STEPPED'] | None
        :param only_active: Only Active, Only add a F-Modifier of the specified type to the active strip
        :type only_active: bool | None
    """

def fmodifier_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the F-Modifier(s) of the active NLA-Strip

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def fmodifier_paste(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_active: bool | None = True,
    replace: bool | None = False,
):
    """Add copied F-Modifiers to the selected NLA-Strips

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Only Active, Only paste F-Modifiers on active strip
    :type only_active: bool | None
    :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
    :type replace: bool | None
    """

def make_single_user(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Ensure that each action is only used once in the set of strips selected

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def meta_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add new meta-strips incorporating the selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def meta_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Separate out the strips held by the selected meta-strips

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def move_down(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Move selected strips down a track if there's room

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def move_up(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Move selected strips up a track if there's room

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def mute_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Mute or un-mute selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def previewrange_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Automatically set Preview Range based on range of keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def properties(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the properties region visibility

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_all_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    invert: bool | None = False,
):
    """Select or deselect all NLA-Strips

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param invert: Invert
    :type invert: bool | None
    """

def select_border(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    deselect: bool | None = False,
    extend: bool | None = True,
    axis_range: bool | None = False,
):
    """Use box selection to grab NLA-Strips

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    :param axis_range: Axis Range
    :type axis_range: bool | None
    """

def select_leftright(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["CHECK", "LEFT", "RIGHT"] | None = "CHECK",
    extend: bool | None = False,
):
    """Select strips to the left or the right of the current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['CHECK','LEFT','RIGHT'] | None
    :param extend: Extend Select
    :type extend: bool | None
    """

def selected_objects_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make selected objects appear in NLA Editor by adding Animation Data

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CFRA", "NEAREST_FRAME", "NEAREST_SECOND", "NEAREST_MARKER"]
    | None = "CFRA",
):
    """Move start of strips to specified time

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['CFRA','NEAREST_FRAME','NEAREST_SECOND','NEAREST_MARKER'] | None
    """

def soundclip_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a strip for controlling when speaker plays its sound clip

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def split(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Split selected strips at their midpoints

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def swap(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Swap order of selected strips within tracks

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def tracks_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    above_selected: bool | None = False,
):
    """Add NLA-Tracks above/after the selected tracks

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param above_selected: Above Selected, Add a new NLA Track above every existing selected one
    :type above_selected: bool | None
    """

def tracks_delete(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete selected NLA-Tracks and the strips they contain

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def transition_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a transition strip between two adjacent selected strips

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def tweakmode_enter(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    isolate_action: bool | None = False,
):
    """Enter tweaking mode for the action referenced by the active strip to edit its keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param isolate_action: Isolate Action, Enable 'solo' on the NLA Track containing the active strip, to edit it without seeing the effects of the NLA stack
    :type isolate_action: bool | None
    """

def tweakmode_exit(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    isolate_action: bool | None = False,
):
    """Exit tweaking mode for the action referenced by the active strip

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param isolate_action: Isolate Action, Disable 'solo' on any of the NLA Tracks after exiting tweak mode to get things back to normal
    :type isolate_action: bool | None
    """

def view_all(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset viewable area to show full strips range

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_frame(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset viewable area to show range around current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset viewable area to show selected strips range

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """
