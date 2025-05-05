import typing
import collections.abc
import typing_extensions
import bpy.types

def bend(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Iterable[float] | None = 0.0,
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Bend selected items between the 3D cursor and the mouse

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Angle
        :type value: collections.abc.Iterable[float] | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | None
        :param center_override: Center Override, Force using this center value (when set)
        :type center_override: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def create_orientation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    use_view: bool | None = False,
    use: bool | None = False,
    overwrite: bool | None = False,
):
    """Create transformation orientation from selection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the new custom orientation
    :type name: str
    :param use_view: Use View, Use the current view instead of the active object to create the new orientation
    :type use_view: bool | None
    :param use: Use after creation, Select orientation after its creation
    :type use: bool | None
    :param overwrite: Overwrite previous, Overwrite previously created orientation with same name
    :type overwrite: bool | None
    """

def delete_orientation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete transformation orientation

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def edge_bevelweight(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Change the bevel weight of edges

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Factor
        :type value: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def edge_crease(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Change the crease of edges

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Factor
        :type value: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def edge_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    single_side: bool | None = False,
    use_even: bool | None = False,
    flipped: bool | None = False,
    use_clamp: bool | None = True,
    mirror: bool | None = False,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    correct_uv: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Slide an edge loop along a mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Factor
        :type value: float | None
        :param single_side: Single Side
        :type single_side: bool | None
        :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
        :type use_even: bool | None
        :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
        :type flipped: bool | None
        :param use_clamp: Clamp, Clamp within the edge extents
        :type use_clamp: bool | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param correct_uv: Correct UVs, Correct UV coordinates when transforming
        :type correct_uv: bool | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    constraint_orientation: typing.Literal[
        "GLOBAL", "LOCAL", "NORMAL", "GIMBAL", "VIEW"
    ]
    | None = "GLOBAL",
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Mirror selected items around one or more axes

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: collections.abc.Iterable[bool] | None
        :param constraint_orientation: Orientation, Transformation orientation

    GLOBAL Global, Align the transformation axes to world space.

    LOCAL Local, Align the transformation axes to the selected objects' local space.

    NORMAL Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).

    GIMBAL Gimbal, Align each axis to the Euler rotation axis as used for input.

    VIEW View, Align the transformation axes to the window.
        :type constraint_orientation: typing.Literal['GLOBAL','LOCAL','NORMAL','GIMBAL','VIEW'] | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | None
        :param center_override: Center Override, Force using this center value (when set)
        :type center_override: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def push_pull(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    center_override: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Push/Pull selected items

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Distance
        :type value: float | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param center_override: Center Override, Force using this center value (when set)
        :type center_override: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def resize(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Iterable[float] | None = (1.0, 1.0, 1.0),
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    constraint_orientation: typing.Literal[
        "GLOBAL", "LOCAL", "NORMAL", "GIMBAL", "VIEW"
    ]
    | None = "GLOBAL",
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | None = False,
    texture_space: bool | None = False,
    remove_on_cancel: bool | None = False,
    center_override: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Scale (resize) selected items

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Scale
        :type value: collections.abc.Iterable[float] | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: collections.abc.Iterable[bool] | None
        :param constraint_orientation: Orientation, Transformation orientation

    GLOBAL Global, Align the transformation axes to world space.

    LOCAL Local, Align the transformation axes to the selected objects' local space.

    NORMAL Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).

    GIMBAL Gimbal, Align each axis to the Euler rotation axis as used for input.

    VIEW View, Align the transformation axes to the window.
        :type constraint_orientation: typing.Literal['GLOBAL','LOCAL','NORMAL','GIMBAL','VIEW'] | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | None
        :param texture_space: Edit Texture Space, Edit Object data texture space
        :type texture_space: bool | None
        :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
        :type remove_on_cancel: bool | None
        :param center_override: Center Override, Force using this center value (when set)
        :type center_override: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def rotate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    axis: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    constraint_orientation: typing.Literal[
        "GLOBAL", "LOCAL", "NORMAL", "GIMBAL", "VIEW"
    ]
    | None = "GLOBAL",
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Rotate selected items

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Angle
        :type value: float | None
        :param axis: Axis, The axis around which the transformation occurs
        :type axis: collections.abc.Iterable[float] | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: collections.abc.Iterable[bool] | None
        :param constraint_orientation: Orientation, Transformation orientation

    GLOBAL Global, Align the transformation axes to world space.

    LOCAL Local, Align the transformation axes to the selected objects' local space.

    NORMAL Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).

    GIMBAL Gimbal, Align each axis to the Euler rotation axis as used for input.

    VIEW View, Align the transformation axes to the window.
        :type constraint_orientation: typing.Literal['GLOBAL','LOCAL','NORMAL','GIMBAL','VIEW'] | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | None
        :param center_override: Center Override, Force using this center value (when set)
        :type center_override: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def select_orientation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    orientation: typing.Literal["GLOBAL", "LOCAL", "NORMAL", "GIMBAL", "VIEW"]
    | None = "GLOBAL",
):
    """Select transformation orientation

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param orientation: Orientation, Transformation orientation

    GLOBAL Global, Align the transformation axes to world space.

    LOCAL Local, Align the transformation axes to the selected objects' local space.

    NORMAL Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).

    GIMBAL Gimbal, Align each axis to the Euler rotation axis as used for input.

    VIEW View, Align the transformation axes to the window.
        :type orientation: typing.Literal['GLOBAL','LOCAL','NORMAL','GIMBAL','VIEW'] | None
    """

def seq_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Iterable[float] | None = (0.0, 0.0),
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Slide a sequence strip in time

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Offset
        :type value: collections.abc.Iterable[float] | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def shear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Shear selected items along the horizontal screen axis

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Offset
        :type value: float | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def shrink_fatten(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    use_even_offset: bool | None = True,
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Shrink/fatten selected vertices along normals

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Offset
        :type value: float | None
        :param use_even_offset: Offset Even, Scale the offset to give more even thickness
        :type use_even_offset: bool | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def skin_resize(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Iterable[float] | None = (1.0, 1.0, 1.0),
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    constraint_orientation: typing.Literal[
        "GLOBAL", "LOCAL", "NORMAL", "GIMBAL", "VIEW"
    ]
    | None = "GLOBAL",
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Scale selected vertices' skin radii

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Scale
        :type value: collections.abc.Iterable[float] | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: collections.abc.Iterable[bool] | None
        :param constraint_orientation: Orientation, Transformation orientation

    GLOBAL Global, Align the transformation axes to world space.

    LOCAL Local, Align the transformation axes to the selected objects' local space.

    NORMAL Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).

    GIMBAL Gimbal, Align each axis to the Euler rotation axis as used for input.

    VIEW View, Align the transformation axes to the window.
        :type constraint_orientation: typing.Literal['GLOBAL','LOCAL','NORMAL','GIMBAL','VIEW'] | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def tilt(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Tilt selected control vertices of 3D curve

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Angle
        :type value: float | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def tosphere(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Move selected vertices outward in a spherical shape around mesh center

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Factor
        :type value: float | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | None
        :param center_override: Center Override, Force using this center value (when set)
        :type center_override: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def trackball(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Iterable[float] | None = (0.0, 0.0),
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Trackball style rotation of selected items

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Angle
        :type value: collections.abc.Iterable[float] | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | None
        :param center_override: Center Override, Force using this center value (when set)
        :type center_override: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def transform(
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
    value: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 0.0),
    axis: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    constraint_orientation: typing.Literal[
        "GLOBAL", "LOCAL", "NORMAL", "GIMBAL", "VIEW"
    ]
    | None = "GLOBAL",
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | None = False,
    center_override: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Transform selected items by mode type

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode
        :type mode: typing.Literal['INIT','DUMMY','TRANSLATION','ROTATION','RESIZE','SKIN_RESIZE','TOSPHERE','SHEAR','BEND','SHRINKFATTEN','TILT','TRACKBALL','PUSHPULL','CREASE','MIRROR','BONE_SIZE','BONE_ENVELOPE','BONE_ENVELOPE_DIST','CURVE_SHRINKFATTEN','MASK_SHRINKFATTEN','GPENCIL_SHRINKFATTEN','BONE_ROLL','TIME_TRANSLATE','TIME_SLIDE','TIME_SCALE','TIME_EXTEND','BAKE_TIME','BWEIGHT','ALIGN','EDGESLIDE','SEQSLIDE'] | None
        :param value: Values
        :type value: collections.abc.Iterable[float] | None
        :param axis: Axis, The axis around which the transformation occurs
        :type axis: collections.abc.Iterable[float] | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: collections.abc.Iterable[bool] | None
        :param constraint_orientation: Orientation, Transformation orientation

    GLOBAL Global, Align the transformation axes to world space.

    LOCAL Local, Align the transformation axes to the selected objects' local space.

    NORMAL Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).

    GIMBAL Gimbal, Align each axis to the Euler rotation axis as used for input.

    VIEW View, Align the transformation axes to the window.
        :type constraint_orientation: typing.Literal['GLOBAL','LOCAL','NORMAL','GIMBAL','VIEW'] | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | None
        :param center_override: Center Override, Force using this center value (when set)
        :type center_override: collections.abc.Iterable[float] | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def translate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    constraint_axis: collections.abc.Iterable[bool] | None = (False, False, False),
    constraint_orientation: typing.Literal[
        "GLOBAL", "LOCAL", "NORMAL", "GIMBAL", "VIEW"
    ]
    | None = "GLOBAL",
    mirror: bool | None = False,
    proportional: typing.Literal["DISABLED", "ENABLED", "PROJECTED", "CONNECTED"]
    | None = "DISABLED",
    proportional_edit_falloff: typing.Literal[
        "SMOOTH",
        "SPHERE",
        "ROOT",
        "INVERSE_SQUARE",
        "SHARP",
        "LINEAR",
        "CONSTANT",
        "RANDOM",
    ]
    | None = "SMOOTH",
    proportional_size: float | None = 1.0,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    gpencil_strokes: bool | None = False,
    texture_space: bool | None = False,
    remove_on_cancel: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Translate (move) selected items

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Move
        :type value: collections.abc.Iterable[float] | None
        :param constraint_axis: Constraint Axis
        :type constraint_axis: collections.abc.Iterable[bool] | None
        :param constraint_orientation: Orientation, Transformation orientation

    GLOBAL Global, Align the transformation axes to world space.

    LOCAL Local, Align the transformation axes to the selected objects' local space.

    NORMAL Normal, Align the transformation axes to average normal of selected elements (bone Y axis for pose mode).

    GIMBAL Gimbal, Align each axis to the Euler rotation axis as used for input.

    VIEW View, Align the transformation axes to the window.
        :type constraint_orientation: typing.Literal['GLOBAL','LOCAL','NORMAL','GIMBAL','VIEW'] | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param proportional: Proportional Editing

    DISABLED Disable, Proportional Editing disabled.

    ENABLED Enable, Proportional Editing enabled.

    PROJECTED Projected (2D), Proportional Editing using screen space locations.

    CONNECTED Connected, Proportional Editing using connected geometry only.
        :type proportional: typing.Literal['DISABLED','ENABLED','PROJECTED','CONNECTED'] | None
        :param proportional_edit_falloff: Proportional Editing Falloff, Falloff type for proportional editing mode

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.

    CONSTANT Constant, Constant falloff.

    RANDOM Random, Random falloff.
        :type proportional_edit_falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR','CONSTANT','RANDOM'] | None
        :param proportional_size: Proportional Size
        :type proportional_size: float | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param gpencil_strokes: Edit Grease Pencil, Edit selected Grease Pencil strokes
        :type gpencil_strokes: bool | None
        :param texture_space: Edit Texture Space, Edit Object data texture space
        :type texture_space: bool | None
        :param remove_on_cancel: Remove on Cancel, Remove elements on cancel
        :type remove_on_cancel: bool | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def vert_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value: float | None = 0.0,
    use_even: bool | None = False,
    flipped: bool | None = False,
    use_clamp: bool | None = True,
    mirror: bool | None = False,
    snap: bool | None = False,
    snap_target: typing.Literal["CLOSEST", "CENTER", "MEDIAN", "ACTIVE"]
    | None = "CLOSEST",
    snap_point: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    snap_align: bool | None = False,
    snap_normal: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    correct_uv: bool | None = False,
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Slide a vertex along a mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param value: Factor
        :type value: float | None
        :param use_even: Even, Make the edge loop match the shape of the adjacent edge loop
        :type use_even: bool | None
        :param flipped: Flipped, When Even mode is active, flips between the two adjacent edge loops
        :type flipped: bool | None
        :param use_clamp: Clamp, Clamp within the edge extents
        :type use_clamp: bool | None
        :param mirror: Mirror Editing
        :type mirror: bool | None
        :param snap: Use Snapping Options
        :type snap: bool | None
        :param snap_target: Target

    CLOSEST Closest, Snap closest point onto target.

    CENTER Center, Snap transormation center onto target.

    MEDIAN Median, Snap median onto target.

    ACTIVE Active, Snap active onto target.
        :type snap_target: typing.Literal['CLOSEST','CENTER','MEDIAN','ACTIVE'] | None
        :param snap_point: Point
        :type snap_point: collections.abc.Iterable[float] | None
        :param snap_align: Align with Point Normal
        :type snap_align: bool | None
        :param snap_normal: Normal
        :type snap_normal: collections.abc.Iterable[float] | None
        :param correct_uv: Correct UVs, Correct UV coordinates when transforming
        :type correct_uv: bool | None
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def vertex_random(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.1,
    uniform: float | None = 0.0,
    normal: float | None = 0.0,
    seed: int | None = 0,
):
    """Randomize vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Amount, Distance to offset
    :type offset: float | None
    :param uniform: Uniform, Increase for uniform offset distance
    :type uniform: float | None
    :param normal: normal, Align offset direction to normals
    :type normal: float | None
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int | None
    """

def vertex_warp(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    warp_angle: float | None = 6.28319,
    offset_angle: float | None = 0.0,
    min: float | None = -1,
    max: float | None = 1.0,
    viewmat: list[list[float]]
    | tuple[
        tuple[float, float, float, float],
        tuple[float, float, float, float],
        tuple[float, float, float, float],
        tuple[float, float, float, float],
    ]
    | None = (
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
        (0.0, 0.0, 0.0, 0.0),
    ),
    center: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
):
    """Warp vertices around the cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param warp_angle: Warp Angle, Amount to warp about the cursor
    :type warp_angle: float | None
    :param offset_angle: Offset Angle, Angle to use as the basis for warping
    :type offset_angle: float | None
    :param min: Min
    :type min: float | None
    :param max: Max
    :type max: float | None
    :param viewmat: Matrix
    :type viewmat: list[list[float]] | tuple[tuple[float, float, float, float], tuple[float, float, float, float], tuple[float, float, float, float], tuple[float, float, float, float]] | None
    :param center: Center
    :type center: collections.abc.Iterable[float] | None
    """
