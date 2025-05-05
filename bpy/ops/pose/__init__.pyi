import typing
import collections.abc
import typing_extensions
import bpy.types

def armature_apply(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply the current pose as the new rest pose

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def autoside_names(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: typing.Literal["XAXIS", "YAXIS", "ZAXIS"] | None = "XAXIS",
):
    """Automatically renames the selected bones according to which side of the target axis they fall on

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param axis: Axis, Axis tag names with

    XAXIS X-Axis, Left/Right.

    YAXIS Y-Axis, Front/Back.

    ZAXIS Z-Axis, Top/Bottom.
        :type axis: typing.Literal['XAXIS','YAXIS','ZAXIS'] | None
    """

def bone_layers(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    layers: collections.abc.Iterable[bool] | None = (
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ),
):
    """Change the layers that the selected bones belong to

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param layers: Layer, Armature layers that bone belongs to
    :type layers: collections.abc.Iterable[bool] | None
    """

def breakdown(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    percentage: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
):
    """Create a suitable breakdown pose on the current frame

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param percentage: Percentage, Weighting factor for which keyframe is favored more
        :type percentage: float | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: int | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: int | None
        :param channels: Channels, Set of properties that are affected

    ALL All Properties, All properties, including transforms, bendy bone shape, and custom properties.

    LOC Location, Location only.

    ROT Rotation, Rotation only.

    SIZE Scale, Scale only.

    BBONE Bendy Bone, Bendy Bone shape properties.

    CUSTOM Custom Properties, Custom properties.
        :type channels: typing.Literal['ALL','LOC','ROT','SIZE','BBONE','CUSTOM'] | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE Free, All axes are affected.

    X X, Only X-axis transforms are affected.

    Y Y, Only Y-axis transforms are affected.

    Z Z, Only Z-axis transforms are affected.
        :type axis_lock: typing.Literal['FREE','X','Y','Z'] | None
    """

def constraint_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "CAMERA_SOLVER",
        "FOLLOW_TRACK",
        "OBJECT_SOLVER",
        "COPY_LOCATION",
        "COPY_ROTATION",
        "COPY_SCALE",
        "COPY_TRANSFORMS",
        "LIMIT_DISTANCE",
        "LIMIT_LOCATION",
        "LIMIT_ROTATION",
        "LIMIT_SCALE",
        "MAINTAIN_VOLUME",
        "TRANSFORM",
        "TRANSFORM_CACHE",
        "CLAMP_TO",
        "DAMPED_TRACK",
        "IK",
        "LOCKED_TRACK",
        "SPLINE_IK",
        "STRETCH_TO",
        "TRACK_TO",
        "ACTION",
        "CHILD_OF",
        "FLOOR",
        "FOLLOW_PATH",
        "PIVOT",
        "RIGID_BODY_JOINT",
        "SHRINKWRAP",
    ]
    | None = "",
):
    """Add a constraint to the active bone

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CAMERA_SOLVER Camera Solver.

    FOLLOW_TRACK Follow Track.

    OBJECT_SOLVER Object Solver.

    COPY_LOCATION Copy Location, Copy the location of a target (with an optional offset), so that they move together.

    COPY_ROTATION Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together.

    COPY_SCALE Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.

    COPY_TRANSFORMS Copy Transforms, Copy all the transformations of a target, so that they move together.

    LIMIT_DISTANCE Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).

    LIMIT_LOCATION Limit Location, Restrict movement along each axis within given ranges.

    LIMIT_ROTATION Limit Rotation, Restrict rotation along each axis within given ranges.

    LIMIT_SCALE Limit Scale, Restrict scaling along each axis with given ranges.

    MAINTAIN_VOLUME Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes.

    TRANSFORM Transformation, Use one transform property from target to control another (or same) property on owner.

    TRANSFORM_CACHE Transform Cache, Look up the transformation matrix from an external file.

    CLAMP_TO Clamp To, Restrict movements to lie along a curve by remapping location along curve's longest axis.

    DAMPED_TRACK Damped Track, Point towards a target by performing the smallest rotation necessary.

    IK Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only).

    LOCKED_TRACK Locked Track, Rotate around the specified ('locked') axis to point towards a target.

    SPLINE_IK Spline IK, Align chain of bones along a curve (Bones only).

    STRETCH_TO Stretch To, Stretch along Y-Axis to point towards a target.

    TRACK_TO Track To, Legacy tracking constraint prone to twisting artifacts.

    ACTION Action, Use transform property of target to look up pose for owner from an Action.

    CHILD_OF Child Of, Make target the 'detachable' parent of owner.

    FLOOR Floor, Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner can not cross.

    FOLLOW_PATH Follow Path, Use to animate an object/bone following a path.

    PIVOT Pivot, Change pivot point for transforms (buggy).

    RIGID_BODY_JOINT Rigid Body Joint, Use to define a Rigid Body Constraint (for Game Engine use only).

    SHRINKWRAP Shrinkwrap, Restrict movements to surface of target mesh.
        :type type: typing.Literal['CAMERA_SOLVER','FOLLOW_TRACK','OBJECT_SOLVER','COPY_LOCATION','COPY_ROTATION','COPY_SCALE','COPY_TRANSFORMS','LIMIT_DISTANCE','LIMIT_LOCATION','LIMIT_ROTATION','LIMIT_SCALE','MAINTAIN_VOLUME','TRANSFORM','TRANSFORM_CACHE','CLAMP_TO','DAMPED_TRACK','IK','LOCKED_TRACK','SPLINE_IK','STRETCH_TO','TRACK_TO','ACTION','CHILD_OF','FLOOR','FOLLOW_PATH','PIVOT','RIGID_BODY_JOINT','SHRINKWRAP'] | None
    """

def constraint_add_with_targets(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "CAMERA_SOLVER",
        "FOLLOW_TRACK",
        "OBJECT_SOLVER",
        "COPY_LOCATION",
        "COPY_ROTATION",
        "COPY_SCALE",
        "COPY_TRANSFORMS",
        "LIMIT_DISTANCE",
        "LIMIT_LOCATION",
        "LIMIT_ROTATION",
        "LIMIT_SCALE",
        "MAINTAIN_VOLUME",
        "TRANSFORM",
        "TRANSFORM_CACHE",
        "CLAMP_TO",
        "DAMPED_TRACK",
        "IK",
        "LOCKED_TRACK",
        "SPLINE_IK",
        "STRETCH_TO",
        "TRACK_TO",
        "ACTION",
        "CHILD_OF",
        "FLOOR",
        "FOLLOW_PATH",
        "PIVOT",
        "RIGID_BODY_JOINT",
        "SHRINKWRAP",
    ]
    | None = "",
):
    """Add a constraint to the active bone, with target (where applicable) set to the selected Objects/Bones

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CAMERA_SOLVER Camera Solver.

    FOLLOW_TRACK Follow Track.

    OBJECT_SOLVER Object Solver.

    COPY_LOCATION Copy Location, Copy the location of a target (with an optional offset), so that they move together.

    COPY_ROTATION Copy Rotation, Copy the rotation of a target (with an optional offset), so that they rotate together.

    COPY_SCALE Copy Scale, Copy the scale factors of a target (with an optional offset), so that they are scaled by the same amount.

    COPY_TRANSFORMS Copy Transforms, Copy all the transformations of a target, so that they move together.

    LIMIT_DISTANCE Limit Distance, Restrict movements to within a certain distance of a target (at the time of constraint evaluation only).

    LIMIT_LOCATION Limit Location, Restrict movement along each axis within given ranges.

    LIMIT_ROTATION Limit Rotation, Restrict rotation along each axis within given ranges.

    LIMIT_SCALE Limit Scale, Restrict scaling along each axis with given ranges.

    MAINTAIN_VOLUME Maintain Volume, Compensate for scaling one axis by applying suitable scaling to the other two axes.

    TRANSFORM Transformation, Use one transform property from target to control another (or same) property on owner.

    TRANSFORM_CACHE Transform Cache, Look up the transformation matrix from an external file.

    CLAMP_TO Clamp To, Restrict movements to lie along a curve by remapping location along curve's longest axis.

    DAMPED_TRACK Damped Track, Point towards a target by performing the smallest rotation necessary.

    IK Inverse Kinematics, Control a chain of bones by specifying the endpoint target (Bones only).

    LOCKED_TRACK Locked Track, Rotate around the specified ('locked') axis to point towards a target.

    SPLINE_IK Spline IK, Align chain of bones along a curve (Bones only).

    STRETCH_TO Stretch To, Stretch along Y-Axis to point towards a target.

    TRACK_TO Track To, Legacy tracking constraint prone to twisting artifacts.

    ACTION Action, Use transform property of target to look up pose for owner from an Action.

    CHILD_OF Child Of, Make target the 'detachable' parent of owner.

    FLOOR Floor, Use position (and optionally rotation) of target to define a 'wall' or 'floor' that the owner can not cross.

    FOLLOW_PATH Follow Path, Use to animate an object/bone following a path.

    PIVOT Pivot, Change pivot point for transforms (buggy).

    RIGID_BODY_JOINT Rigid Body Joint, Use to define a Rigid Body Constraint (for Game Engine use only).

    SHRINKWRAP Shrinkwrap, Restrict movements to surface of target mesh.
        :type type: typing.Literal['CAMERA_SOLVER','FOLLOW_TRACK','OBJECT_SOLVER','COPY_LOCATION','COPY_ROTATION','COPY_SCALE','COPY_TRANSFORMS','LIMIT_DISTANCE','LIMIT_LOCATION','LIMIT_ROTATION','LIMIT_SCALE','MAINTAIN_VOLUME','TRANSFORM','TRANSFORM_CACHE','CLAMP_TO','DAMPED_TRACK','IK','LOCKED_TRACK','SPLINE_IK','STRETCH_TO','TRACK_TO','ACTION','CHILD_OF','FLOOR','FOLLOW_PATH','PIVOT','RIGID_BODY_JOINT','SHRINKWRAP'] | None
    """

def constraints_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear all the constraints for the selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def constraints_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy constraints to other selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def copy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copies the current pose of the selected bones to copy/paste buffer

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def flip_names(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    do_strip_numbers: bool | None = False,
):
    """Flips (and corrects) the axis suffixes of the names of selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param do_strip_numbers: Strip Numbers, Try to remove right-most dot-number from flipped names (WARNING: may result in incoherent naming in some cases)
    :type do_strip_numbers: bool | None
    """

def group_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a new bone group

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def group_assign(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: int | None = 0,
):
    """Add selected bones to the chosen bone group

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Bone Group Index
    :type type: int | None
    """

def group_deselect(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect bones of active Bone Group

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def group_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Change position of active Bone Group in list of Bone Groups

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the active Bone Group towards
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def group_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the active bone group

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def group_select(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select bones in active Bone Group

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def group_sort(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Sort Bone Groups by their names in ascending order

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def group_unassign(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove selected bones from all bone groups

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Tag selected bones to not be visible in Pose Mode

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected
    :type unselected: bool | None
    """

def ik_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    with_targets: bool | None = True,
):
    """Add IK Constraint to the active Bone

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param with_targets: With Targets, Assign IK Constraint with targets derived from the select bones/objects
    :type with_targets: bool | None
    """

def ik_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove all IK Constraints from selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def loc_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset locations of selected bones to their default values

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def paste(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    flipped: bool | None = False,
    selected_mask: bool | None = False,
):
    """Paste the stored pose on to the current pose

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param flipped: Flipped on X-Axis, Paste the stored pose flipped on to current pose
    :type flipped: bool | None
    :param selected_mask: On Selected Only, Only paste the stored pose on to selected bones in the current pose
    :type selected_mask: bool | None
    """

def paths_calculate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    start_frame: int | None = 1,
    end_frame: int | None = 250,
    bake_location: typing.Literal["HEADS", "TAILS"] | None = "TAILS",
):
    """Calculate paths for the selected bones

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param start_frame: Start, First frame to calculate bone paths on
        :type start_frame: int | None
        :param end_frame: End, Last frame to calculate bone paths on
        :type end_frame: int | None
        :param bake_location: Bake Location, Which point on the bones is used when calculating paths

    HEADS Heads, Calculate bone paths from heads.

    TAILS Tails, Calculate bone paths from tails.
        :type bake_location: typing.Literal['HEADS','TAILS'] | None
    """

def paths_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_selected: bool | None = False,
):
    """Clear path caches for all bones, hold Shift key for selected bones only

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_selected: Only Selected, Only clear paths from selected bones
    :type only_selected: bool | None
    """

def paths_update(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Recalculate paths for bones that already have them

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def propagate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal[
        "WHILE_HELD",
        "NEXT_KEY",
        "LAST_KEY",
        "BEFORE_FRAME",
        "BEFORE_END",
        "SELECTED_KEYS",
        "SELECTED_MARKERS",
    ]
    | None = "WHILE_HELD",
    end_frame: float | None = 250.0,
):
    """Copy selected aspects of the current pose to subsequent poses already keyframed

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Terminate Mode, Method used to determine when to stop propagating pose to keyframes

    WHILE_HELD While Held, Propagate pose to all keyframes after current frame that don't change (Default behavior).

    NEXT_KEY To Next Keyframe, Propagate pose to first keyframe following the current frame only.

    LAST_KEY To Last Keyframe, Propagate pose to the last keyframe only (i.e. making action cyclic).

    BEFORE_FRAME Before Frame, Propagate pose to all keyframes between current frame and 'Frame' property.

    BEFORE_END Before Last Keyframe, Propagate pose to all keyframes from current frame until no more are found.

    SELECTED_KEYS On Selected Keyframes, Propagate pose to all selected keyframes.

    SELECTED_MARKERS On Selected Markers, Propagate pose to all keyframes occurring on frames with Scene Markers after the current frame.
        :type mode: typing.Literal['WHILE_HELD','NEXT_KEY','LAST_KEY','BEFORE_FRAME','BEFORE_END','SELECTED_KEYS','SELECTED_MARKERS'] | None
        :param end_frame: End Frame, Frame to stop propagating frames to (for 'Before Frame' mode)
        :type end_frame: float | None
    """

def push(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    percentage: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
):
    """Exaggerate the current pose

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param percentage: Percentage, Weighting factor for which keyframe is favored more
        :type percentage: float | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: int | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: int | None
        :param channels: Channels, Set of properties that are affected

    ALL All Properties, All properties, including transforms, bendy bone shape, and custom properties.

    LOC Location, Location only.

    ROT Rotation, Rotation only.

    SIZE Scale, Scale only.

    BBONE Bendy Bone, Bendy Bone shape properties.

    CUSTOM Custom Properties, Custom properties.
        :type channels: typing.Literal['ALL','LOC','ROT','SIZE','BBONE','CUSTOM'] | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE Free, All axes are affected.

    X X, Only X-axis transforms are affected.

    Y Y, Only Y-axis transforms are affected.

    Z Z, Only Z-axis transforms are affected.
        :type axis_lock: typing.Literal['FREE','X','Y','Z'] | None
    """

def quaternions_flip(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flip quaternion values to achieve desired rotations, while maintaining the same orientations

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def relax(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    percentage: float | None = 0.5,
    prev_frame: int | None = 0,
    next_frame: int | None = 0,
    channels: typing.Literal["ALL", "LOC", "ROT", "SIZE", "BBONE", "CUSTOM"]
    | None = "ALL",
    axis_lock: typing.Literal["FREE", "X", "Y", "Z"] | None = "FREE",
):
    """Make the current pose more similar to its surrounding ones

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param percentage: Percentage, Weighting factor for which keyframe is favored more
        :type percentage: float | None
        :param prev_frame: Previous Keyframe, Frame number of keyframe immediately before the current frame
        :type prev_frame: int | None
        :param next_frame: Next Keyframe, Frame number of keyframe immediately after the current frame
        :type next_frame: int | None
        :param channels: Channels, Set of properties that are affected

    ALL All Properties, All properties, including transforms, bendy bone shape, and custom properties.

    LOC Location, Location only.

    ROT Rotation, Rotation only.

    SIZE Scale, Scale only.

    BBONE Bendy Bone, Bendy Bone shape properties.

    CUSTOM Custom Properties, Custom properties.
        :type channels: typing.Literal['ALL','LOC','ROT','SIZE','BBONE','CUSTOM'] | None
        :param axis_lock: Axis Lock, Transform axis to restrict effects to

    FREE Free, All axes are affected.

    X X, Only X-axis transforms are affected.

    Y Y, Only Y-axis transforms are affected.

    Z Z, Only Z-axis transforms are affected.
        :type axis_lock: typing.Literal['FREE','X','Y','Z'] | None
    """

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
):
    """Reveal all bones hidden in Pose Mode

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    """

def rot_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset rotations of selected bones to their default values

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def rotation_mode_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "QUATERNION", "XYZ", "XZY", "YXZ", "YZX", "ZXY", "ZYX", "AXIS_ANGLE"
    ]
    | None = "QUATERNION",
):
    """Set the rotation representation used by selected bones

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Rotation Mode

    QUATERNION Quaternion (WXYZ), No Gimbal Lock (default).

    XYZ XYZ Euler, XYZ Rotation Order (prone to Gimbal Lock).

    XZY XZY Euler, XZY Rotation Order (prone to Gimbal Lock).

    YXZ YXZ Euler, YXZ Rotation Order (prone to Gimbal Lock).

    YZX YZX Euler, YZX Rotation Order (prone to Gimbal Lock).

    ZXY ZXY Euler, ZXY Rotation Order (prone to Gimbal Lock).

    ZYX ZYX Euler, ZYX Rotation Order (prone to Gimbal Lock).

    AXIS_ANGLE Axis Angle, Axis Angle (W+XYZ), defines a rotation around some axis defined by 3D-Vector.
        :type type: typing.Literal['QUATERNION','XYZ','XZY','YXZ','YZX','ZXY','ZYX','AXIS_ANGLE'] | None
    """

def scale_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset scaling of selected bones to their default values

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Toggle selection status of all bones

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE Toggle, Toggle selection for all elements.

    SELECT Select, Select all elements.

    DESELECT Deselect, Deselect all elements.

    INVERT Invert, Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
    """

def select_constraint_target(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select bones used as targets for the currently selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_grouped(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    type: typing.Literal["LAYER", "GROUP", "KEYINGSET"] | None = "LAYER",
):
    """Select all visible bones grouped by similar properties

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param extend: Extend, Extend selection instead of deselecting everything first
        :type extend: bool | None
        :param type: Type

    LAYER Layer, Shared layers.

    GROUP Group, Shared group.

    KEYINGSET Keying Set, All bones affected by active Keying Set.
        :type type: typing.Literal['LAYER','GROUP','KEYINGSET'] | None
    """

def select_hierarchy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["PARENT", "CHILD"] | None = "PARENT",
    extend: bool | None = False,
):
    """Select immediate parent/children of selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction
    :type direction: typing.Literal['PARENT','CHILD'] | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
):
    """Select bones related to selected ones by parent/child relationships

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    """

def select_mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_active: bool | None = False,
    extend: bool | None = False,
):
    """Mirror the bone selection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Active Only, Only operate on the active bone
    :type only_active: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_parent(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select bones that are parents of the currently selected bones

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def transforms_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset location, rotation, and scaling of selected bones to their default values

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def user_transforms_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    only_selected: bool | None = True,
):
    """Reset pose on selected bones to keyframed state

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_selected: Only Selected, Only visible/selected bones
    :type only_selected: bool | None
    """

def visual_transform_apply(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply final constrained position of pose bones to their transform

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """
