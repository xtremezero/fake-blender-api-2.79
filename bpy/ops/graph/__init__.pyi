import typing
import collections.abc
import typing_extensions
import bpy.ops.transform
import bpy.types

def bake(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Bake selected F-Curves to a set of sampled points defining a similar curve

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

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

def click_insert(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: float | None = 1.0,
    value: float | None = 1.0,
    extend: bool | None = False,
):
    """Insert new keyframe at the cursor position for the active F-Curve

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame Number, Frame to insert keyframe on
    :type frame: float | None
    :param value: Value, Value for keyframe on
    :type value: float | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    """

def clickselect(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    column: bool | None = False,
    curves: bool | None = False,
):
    """Select keyframes by clicking on them

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only
    :type extend: bool | None
    :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse
    :type column: bool | None
    :param curves: Only Curves, Select all the keyframes in the curve
    :type curves: bool | None
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

def cursor_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frame: float | None = 0.0,
    value: float | None = 0.0,
):
    """Interactively set the current frame and value cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame
    :type frame: float | None
    :param value: Value
    :type value: float | None
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

def driver_delete_invalid(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete all visible drivers considered invalid

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def driver_variables_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the driver variables of the active F-Curve

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def driver_variables_paste(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    replace: bool | None = False,
):
    """Add copied driver variables to the active driver

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param replace: Replace Existing, Replace existing driver variables, instead of just appending to the end of the existing list
    :type replace: bool | None
    """

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
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
    """Make a copy of all selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['INIT','DUMMY','TRANSLATION','ROTATION','RESIZE','SKIN_RESIZE','TOSPHERE','SHEAR','BEND','SHRINKFATTEN','TILT','TRACKBALL','PUSHPULL','CREASE','MIRROR','BONE_SIZE','BONE_ENVELOPE','BONE_ENVELOPE_DIST','CURVE_SHRINKFATTEN','MASK_SHRINKFATTEN','GPENCIL_SHRINKFATTEN','BONE_ROLL','TIME_TRANSLATE','TIME_SLIDE','TIME_SCALE','TIME_EXTEND','BAKE_TIME','BWEIGHT','ALIGN','EDGESLIDE','SEQSLIDE'] | None
    """

def duplicate_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    GRAPH_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_transform: bpy.ops.transform.transform | None = None,
):
    """Make a copy of all selected keyframes and move them

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param GRAPH_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
    :type GRAPH_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_transform: Transform, Transform selected items by mode type
    :type TRANSFORM_OT_transform: bpy.ops.transform.transform | None
    """

def easing_type(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["AUTO", "EASE_IN", "EASE_OUT", "EASE_IN_OUT"] | None = "AUTO",
):
    """Set easing type for the F-Curve segments starting from the selected keyframes

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    AUTO Automatic Easing, Easing type is chosen automatically based on what the type of interpolation used (e.g. 'Ease In' for transitional types, and 'Ease Out' for dynamic effects).

    EASE_IN Ease In, Only on the end closest to the next keyframe.

    EASE_OUT Ease Out, Only on the end closest to the first keyframe.

    EASE_IN_OUT Ease In and Out, Segment between both keyframes.
        :type type: typing.Literal['AUTO','EASE_IN','EASE_OUT','EASE_IN_OUT'] | None
    """

def euler_filter(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Fix large jumps and flips in the selected Euler Rotation F-Curves arising from rotation values being clipped when baking physics

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
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
    """Add F-Modifier to the active/selected F-Curves

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
        :param only_active: Only Active, Only add F-Modifier to active F-Curve
        :type only_active: bool | None
    """

def fmodifier_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the F-Modifier(s) of the active F-Curve

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
    """Add copied F-Modifiers to the selected F-Curves

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Only Active, Only paste F-Modifiers on active F-Curve
    :type only_active: bool | None
    :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
    :type replace: bool | None
    """

def frame_jump(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Place the cursor on the midpoint of selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def ghost_curves_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear F-Curve snapshots (Ghosts) for active Graph Editor

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def ghost_curves_create(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create snapshot (Ghosts) of selected F-Curves as background aid for active Graph Editor

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

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Hide selected curves from Graph Editor view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected curves
    :type unselected: bool | None
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
    type: typing.Literal["ALL", "SEL", "CURSOR_ACTIVE", "CURSOR_SEL"] | None = "ALL",
):
    """Insert keyframes for the specified channels

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    ALL All Channels, Insert a keyframe on all visible and editable F-Curves using each curve's current value.

    SEL Only Selected Channels, Insert a keyframe on selected F-Curves using each curve's current value.

    CURSOR_ACTIVE Active Channels At Cursor, Insert a keyframe for the active F-Curve at the cursor point.

    CURSOR_SEL Selected Channels At Cursor, Insert a keyframe for selected F-Curves at the cursor point.
        :type type: typing.Literal['ALL','SEL','CURSOR_ACTIVE','CURSOR_SEL'] | None
    """

def mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["CFRA", "VALUE", "YAXIS", "XAXIS", "MARKER"] | None = "CFRA",
):
    """Flip selected keyframes over the selected mirror line

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CFRA By Times over Current Frame, Flip times of selected keyframes using the current frame as the mirror line.

    VALUE By Values over Cursor Value, Flip values of selected keyframes using the cursor value (Y/Horizontal component) as the mirror line.

    YAXIS By Times over Time=0, Flip times of selected keyframes, effectively reversing the order they appear in.

    XAXIS By Values over Value=0, Flip values of selected keyframes (i.e. negative values become positive, and vice versa).

    MARKER By Times over First Selected Marker, Flip times of selected keyframes using the first selected marker as the reference point.
        :type type: typing.Literal['CFRA','VALUE','YAXIS','XAXIS','MARKER'] | None
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

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
):
    """Make previously hidden curves visible again in Graph Editor view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
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
    include_handles: bool | None = False,
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
    :param include_handles: Include Handles, Are handles tested individually against the selection criteria
    :type include_handles: bool | None
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

def smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply weighted moving means to make selected F-Curves less bumpy

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
    type: typing.Literal[
        "CFRA",
        "VALUE",
        "NEAREST_FRAME",
        "NEAREST_SECOND",
        "NEAREST_MARKER",
        "HORIZONTAL",
    ]
    | None = "CFRA",
):
    """Snap selected keyframes to the chosen times/values

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CFRA Current Frame, Snap selected keyframes to the current frame.

    VALUE Cursor Value, Set values of selected keyframes to the cursor value (Y/Horizontal component).

    NEAREST_FRAME Nearest Frame, Snap selected keyframes to the nearest (whole) frame (use to fix accidental sub-frame offsets).

    NEAREST_SECOND Nearest Second, Snap selected keyframes to the nearest second.

    NEAREST_MARKER Nearest Marker, Snap selected keyframes to the nearest marker.

    HORIZONTAL Flatten Handles, Flatten handles for a smoother transition.
        :type type: typing.Literal['CFRA','VALUE','NEAREST_FRAME','NEAREST_SECOND','NEAREST_MARKER','HORIZONTAL'] | None
    """

def sound_bake(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = True,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = True,
    filter_text: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal["DEFAULT", "LIST_SHORT", "LIST_LONG", "THUMBNAIL"]
    | None = "DEFAULT",
    sort_method: typing.Literal[
        "FILE_SORT_ALPHA", "FILE_SORT_EXTENSION", "FILE_SORT_TIME", "FILE_SORT_SIZE"
    ]
    | None = "FILE_SORT_ALPHA",
    low: float | None = 0.0,
    high: float | None = 100000.0,
    attack: float | None = 0.005,
    release: float | None = 0.2,
    threshold: float | None = 0.0,
    use_accumulate: bool | None = False,
    use_additive: bool | None = False,
    use_square: bool | None = False,
    sthreshold: float | None = 0.1,
):
    """Bakes a sound wave to selected F-Curves

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT Default, Automatically determine display type for files.

    LIST_SHORT Short List, Display files as short list.

    LIST_LONG Long List, Display files as a detailed list.

    THUMBNAIL Thumbnails, Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_SHORT','LIST_LONG','THUMBNAIL'] | None
        :param sort_method: File sorting mode

    FILE_SORT_ALPHA Sort alphabetically, Sort the file list alphabetically.

    FILE_SORT_EXTENSION Sort by extension, Sort the file list by extension/type.

    FILE_SORT_TIME Sort by time, Sort files by modification time.

    FILE_SORT_SIZE Sort by size, Sort files by size.
        :type sort_method: typing.Literal['FILE_SORT_ALPHA','FILE_SORT_EXTENSION','FILE_SORT_TIME','FILE_SORT_SIZE'] | None
        :param low: Lowest frequency, Cutoff frequency of a high-pass filter that is applied to the audio data
        :type low: float | None
        :param high: Highest frequency, Cutoff frequency of a low-pass filter that is applied to the audio data
        :type high: float | None
        :param attack: Attack time, Value for the hull curve calculation that tells how fast the hull curve can rise (the lower the value the steeper it can rise)
        :type attack: float | None
        :param release: Release time, Value for the hull curve calculation that tells how fast the hull curve can fall (the lower the value the steeper it can fall)
        :type release: float | None
        :param threshold: Threshold, Minimum amplitude value needed to influence the hull curve
        :type threshold: float | None
        :param use_accumulate: Accumulate, Only the positive differences of the hull curve amplitudes are summarized to produce the output
        :type use_accumulate: bool | None
        :param use_additive: Additive, The amplitudes of the hull curve are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated)
        :type use_additive: bool | None
        :param use_square: Square, The output is a square curve (negative values always result in -1, and positive ones in 1)
        :type use_square: bool | None
        :param sthreshold: Square Threshold, Square only: all values with an absolute amplitude lower than that result in 0
        :type sthreshold: float | None
    """

def view_all(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    include_handles: bool | None = True,
):
    """Reset viewable area to show full keyframe range

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool | None
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
    /,
    *,
    include_handles: bool | None = True,
):
    """Reset viewable area to show selected keyframe range

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool | None
    """
