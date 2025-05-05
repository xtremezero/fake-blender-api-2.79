import typing
import collections.abc
import typing_extensions
import bpy.ops.transform
import bpy.types

def clean(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.001,
    channels: bool | None = False,
):
    """Simplify F-Curves by removing closely spaced keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Threshold
    :type threshold: float | None
    :param channels: Channels
    :type channels: bool | None
    """

def clickselect(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    column: bool | None = False,
    channel: bool | None = False,
):
    """Select keyframes by clicking on them

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only
    :type extend: bool | None
    :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse
    :type column: bool | None
    :param channel: Only Channel, Select all the keyframes in the channel under the mouse
    :type channel: bool | None
    """

def copy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy selected keyframes to the copy/paste buffer

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove all selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make a copy of all selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def duplicate_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ACTION_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_transform: bpy.ops.transform.transform | None = None,
):
    """Make a copy of all selected keyframes and move them

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param ACTION_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
    :type ACTION_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_transform: Transform, Transform selected items by mode type
    :type TRANSFORM_OT_transform: bpy.ops.transform.transform | None
    """

def extrapolation_type(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CONSTANT", "LINEAR", "MAKE_CYCLIC", "CLEAR_CYCLIC"]
    | None = "CONSTANT",
):
    """Set extrapolation mode for selected F-Curves

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CONSTANT Constant Extrapolation, Values on endpoint keyframes are held.

    LINEAR Linear Extrapolation, Straight-line slope of end segments are extended past the endpoint keyframes.

    MAKE_CYCLIC Make Cyclic (F-Modifier), Add Cycles F-Modifier if one doesn't exist already.

    CLEAR_CYCLIC Clear Cyclic (F-Modifier), Remove Cycles F-Modifier if not needed anymore.
        :type type: typing.Literal['CONSTANT','LINEAR','MAKE_CYCLIC','CLEAR_CYCLIC'] | None
    """

def frame_jump(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set the current frame to the average frame value of selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def handle_type(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["FREE", "VECTOR", "ALIGNED", "AUTO", "AUTO_CLAMPED"]
    | None = "FREE",
):
    """Set type of handle for selected keyframes

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    FREE Free.

    VECTOR Vector.

    ALIGNED Aligned.

    AUTO Automatic.

    AUTO_CLAMPED Auto Clamped, Auto handles clamped to not overshoot.
        :type type: typing.Literal['FREE','VECTOR','ALIGNED','AUTO','AUTO_CLAMPED'] | None
    """

def interpolation_type(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "CONSTANT",
        "LINEAR",
        "BEZIER",
        "SINE",
        "QUAD",
        "CUBIC",
        "QUART",
        "QUINT",
        "EXPO",
        "CIRC",
        "BACK",
        "BOUNCE",
        "ELASTIC",
    ]
    | None = "CONSTANT",
):
    """Set interpolation mode for the F-Curve segments starting from the selected keyframes

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CONSTANT Constant, No interpolation, value of A gets held until B is encountered.

    LINEAR Linear, Straight-line interpolation between A and B (i.e. no ease in/out).

    BEZIER Bezier, Smooth interpolation between A and B, with some control over curve shape.

    SINE Sinusoidal, Sinusoidal easing (weakest, almost linear but with a slight curvature).

    QUAD Quadratic, Quadratic easing.

    CUBIC Cubic, Cubic easing.

    QUART Quartic, Quartic easing.

    QUINT Quintic, Quintic easing.

    EXPO Exponential, Exponential easing (dramatic).

    CIRC Circular, Circular easing (strongest and most dynamic).

    BACK Back, Cubic easing with overshoot and settle.

    BOUNCE Bounce, Exponentially decaying parabolic bounce, like when objects collide.

    ELASTIC Elastic, Exponentially decaying sine wave, like an elastic band.
        :type type: typing.Literal['CONSTANT','LINEAR','BEZIER','SINE','QUAD','CUBIC','QUART','QUINT','EXPO','CIRC','BACK','BOUNCE','ELASTIC'] | None
    """

def keyframe_insert(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["ALL", "SEL", "GROUP"] | None = "ALL",
):
    """Insert keyframes for the specified channels

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['ALL','SEL','GROUP'] | None
    """

def keyframe_type(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["KEYFRAME", "BREAKDOWN", "MOVING_HOLD", "EXTREME", "JITTER"]
    | None = "KEYFRAME",
):
    """Set type of keyframe for the selected keyframes

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    KEYFRAME Keyframe, Normal keyframe - e.g. for key poses.

    BREAKDOWN Breakdown, A breakdown pose - e.g. for transitions between key poses.

    MOVING_HOLD Moving Hold, A keyframe that is part of a moving hold.

    EXTREME Extreme, An 'extreme' pose, or some other purpose as needed.

    JITTER Jitter, A filler or baked keyframe for keying on ones, or some other purpose as needed.
        :type type: typing.Literal['KEYFRAME','BREAKDOWN','MOVING_HOLD','EXTREME','JITTER'] | None
    """

def layer_next(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Switch to editing action in animation layer above the current action in the NLA Stack

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def layer_prev(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Switch to editing action in animation layer below the current action in the NLA Stack

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def markers_make_local(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Move selected scene markers to the active Action as local 'pose' markers

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CFRA", "XAXIS", "MARKER"] | None = "CFRA",
):
    """Flip selected keyframes over the selected mirror line

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CFRA By Times over Current frame, Flip times of selected keyframes using the current frame as the mirror line.

    XAXIS By Values over Value=0, Flip values of selected keyframes (i.e. negative values become positive, and vice versa).

    MARKER By Times over First Selected Marker, Flip times of selected keyframes using the first selected marker as the reference point.
        :type type: typing.Literal['CFRA','XAXIS','MARKER'] | None
    """

def new(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create new action

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
    offset: typing.Literal["START", "END", "RELATIVE", "NONE"] | None = "START",
    merge: typing.Literal["MIX", "OVER_ALL", "OVER_RANGE", "OVER_RANGE_ALL"]
    | None = "MIX",
    flipped: bool | None = False,
):
    """Paste keyframes from copy/paste buffer for the selected channels, starting on the current frame

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param offset: Offset, Paste time offset of keys

    START Frame Start, Paste keys starting at current frame.

    END Frame End, Paste keys ending at current frame.

    RELATIVE Frame Relative, Paste keys relative to the current frame when copying.

    NONE No Offset, Paste keys from original time.
        :type offset: typing.Literal['START','END','RELATIVE','NONE'] | None
        :param merge: Type, Method of merging pasted keys and existing

    MIX Mix, Overlay existing with new keys.

    OVER_ALL Overwrite All, Replace all keys.

    OVER_RANGE Overwrite Range, Overwrite keys in pasted range.

    OVER_RANGE_ALL Overwrite Entire Range, Overwrite keys in pasted range, using the range of all copied keys.
        :type merge: typing.Literal['MIX','OVER_ALL','OVER_RANGE','OVER_RANGE_ALL'] | None
        :param flipped: Flipped, Paste keyframes from mirrored bones if they exist
        :type flipped: bool | None
    """

def previewrange_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set Preview Range based on extents of selected Keyframes

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

def push_down(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Push action down on to the NLA stack as a new strip

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def sample(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add keyframes on every frame between the selected keyframes

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
    """Toggle selection of all keyframes

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
    """Select all keyframes within the specified region

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

def select_circle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x: int | None = 0,
    y: int | None = 0,
    radius: int | None = 25,
    deselect: bool | None = False,
):
    """Select keyframe points using circle selection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param x: X
    :type x: int | None
    :param y: Y
    :type y: int | None
    :param radius: Radius
    :type radius: int | None
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool | None
    """

def select_column(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["KEYS", "CFRA", "MARKERS_COLUMN", "MARKERS_BETWEEN"]
    | None = "KEYS",
):
    """Select all keyframes on the specified frame(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['KEYS','CFRA','MARKERS_COLUMN','MARKERS_BETWEEN'] | None
    """

def select_lasso(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    deselect: bool | None = False,
    extend: bool | None = True,
):
    """Select keyframe points using lasso selection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param path: Path
    :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
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
    """Select keyframes to the left or the right of the current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['CHECK','LEFT','RIGHT'] | None
    :param extend: Extend Select
    :type extend: bool | None
    """

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect keyframes on ends of selection islands

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select keyframes occurring in the same F-Curves as selected ones

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select keyframes beside already selected ones

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
    """Snap selected keyframes to the times specified

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CFRA Current frame, Snap selected keyframes to the current frame.

    NEAREST_FRAME Nearest Frame, Snap selected keyframes to the nearest (whole) frame (use to fix accidental sub-frame offsets).

    NEAREST_SECOND Nearest Second, Snap selected keyframes to the nearest second.

    NEAREST_MARKER Nearest Marker, Snap selected keyframes to the nearest marker.
        :type type: typing.Literal['CFRA','NEAREST_FRAME','NEAREST_SECOND','NEAREST_MARKER'] | None
    """

def stash(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    create_new: bool | None = True,
):
    """Store this action in the NLA stack as a non-contributing strip for later use

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param create_new: Create New Action, Create a new action once the existing one has been safely stored
    :type create_new: bool | None
    """

def stash_and_create(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Store this action in the NLA stack as a non-contributing strip for later use, and create a new action

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def unlink(
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
    :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-block's NLA stack
    :type force_delete: bool | None
    """

def view_all(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset viewable area to show full keyframe range

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
    """Reset viewable area to show selected keyframes range

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """
