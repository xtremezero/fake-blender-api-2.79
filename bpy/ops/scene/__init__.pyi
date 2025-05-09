import typing
import collections.abc
import typing_extensions
import bpy.types

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete active scene

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_add_edge_marks_to_keying_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_add_face_marks_to_keying_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_alpha_modifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "ALONG_STROKE",
        "CREASE_ANGLE",
        "CURVATURE_3D",
        "DISTANCE_FROM_CAMERA",
        "DISTANCE_FROM_OBJECT",
        "MATERIAL",
        "NOISE",
        "TANGENT",
    ]
    | None = "ALONG_STROKE",
):
    """Add an alpha transparency modifier to the line style associated with the active lineset

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['ALONG_STROKE','CREASE_ANGLE','CURVATURE_3D','DISTANCE_FROM_CAMERA','DISTANCE_FROM_OBJECT','MATERIAL','NOISE','TANGENT'] | None
    """

def freestyle_color_modifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "ALONG_STROKE",
        "CREASE_ANGLE",
        "CURVATURE_3D",
        "DISTANCE_FROM_CAMERA",
        "DISTANCE_FROM_OBJECT",
        "MATERIAL",
        "NOISE",
        "TANGENT",
    ]
    | None = "ALONG_STROKE",
):
    """Add a line color modifier to the line style associated with the active lineset

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['ALONG_STROKE','CREASE_ANGLE','CURVATURE_3D','DISTANCE_FROM_CAMERA','DISTANCE_FROM_OBJECT','MATERIAL','NOISE','TANGENT'] | None
    """

def freestyle_fill_range_by_selection(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["COLOR", "ALPHA", "THICKNESS"] | None = "COLOR",
    name: str = "",
):
    """Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Type of the modifier to work on

    COLOR Color, Color modifier type.

    ALPHA Alpha, Alpha modifier type.

    THICKNESS Thickness, Thickness modifier type.
        :type type: typing.Literal['COLOR','ALPHA','THICKNESS'] | None
        :param name: Name, Name of the modifier to work on
        :type name: str
    """

def freestyle_geometry_modifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "2D_OFFSET",
        "2D_TRANSFORM",
        "BACKBONE_STRETCHER",
        "BEZIER_CURVE",
        "BLUEPRINT",
        "GUIDING_LINES",
        "PERLIN_NOISE_1D",
        "PERLIN_NOISE_2D",
        "POLYGONIZATION",
        "SAMPLING",
        "SIMPLIFICATION",
        "SINUS_DISPLACEMENT",
        "SPATIAL_NOISE",
        "TIP_REMOVER",
    ]
    | None = "2D_OFFSET",
):
    """Add a stroke geometry modifier to the line style associated with the active lineset

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['2D_OFFSET','2D_TRANSFORM','BACKBONE_STRETCHER','BEZIER_CURVE','BLUEPRINT','GUIDING_LINES','PERLIN_NOISE_1D','PERLIN_NOISE_2D','POLYGONIZATION','SAMPLING','SIMPLIFICATION','SINUS_DISPLACEMENT','SPATIAL_NOISE','TIP_REMOVER'] | None
    """

def freestyle_lineset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a line set into the list of line sets

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_lineset_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the active line set to a buffer

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_lineset_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Change the position of the active line set within the list of line sets

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the active line set towards
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def freestyle_lineset_paste(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Paste the buffer content to the active line set

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_lineset_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the active line set from the list of line sets

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_linestyle_new(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a new line style, reusable by multiple line sets

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_modifier_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Duplicate the modifier within the list of modifiers

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_modifier_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Move the modifier within the list of modifiers

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the chosen modifier towards
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def freestyle_modifier_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the modifier from the list of modifiers

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_module_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a style module into the list of modules

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_module_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["UP", "DOWN"] | None = "UP",
):
    """Change the position of the style module within in the list of style modules

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Direction to move the chosen style module towards
    :type direction: typing.Literal['UP','DOWN'] | None
    """

def freestyle_module_open(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    make_internal: bool | None = True,
):
    """Open a style module file

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: filepath
    :type filepath: str
    :param make_internal: Make internal, Make module file internal after loading
    :type make_internal: bool | None
    """

def freestyle_module_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the style module from the stack

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_stroke_material_create(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create Freestyle stroke material for testing

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def freestyle_thickness_modifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "ALONG_STROKE",
        "CALLIGRAPHY",
        "CREASE_ANGLE",
        "CURVATURE_3D",
        "DISTANCE_FROM_CAMERA",
        "DISTANCE_FROM_OBJECT",
        "MATERIAL",
        "NOISE",
        "TANGENT",
    ]
    | None = "ALONG_STROKE",
):
    """Add a line thickness modifier to the line style associated with the active lineset

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['ALONG_STROKE','CALLIGRAPHY','CREASE_ANGLE','CURVATURE_3D','DISTANCE_FROM_CAMERA','DISTANCE_FROM_OBJECT','MATERIAL','NOISE','TANGENT'] | None
    """

def new(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "NEW", "EMPTY", "LINK_OBJECTS", "LINK_OBJECT_DATA", "FULL_COPY"
    ]
    | None = "NEW",
):
    """Add new scene by type

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    NEW New, Add new scene.

    EMPTY Copy Settings, Make a copy without any objects.

    LINK_OBJECTS Link Objects, Link to the objects from the current scene.

    LINK_OBJECT_DATA Link Object Data, Copy objects linked to data from the current scene.

    FULL_COPY Full Copy, Make a full copy of the current scene.
        :type type: typing.Literal['NEW','EMPTY','LINK_OBJECTS','LINK_OBJECT_DATA','FULL_COPY'] | None
    """

def render_attachment_new(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create a render attachment

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def render_attachment_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the selected render attachment

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def render_layer_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a render layer

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def render_layer_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the selected render layer

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def render_view_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a render view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def render_view_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the selected render view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def units_length_preset_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "",
    remove_active: bool | None = False,
):
    """Add or remove length units preset

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Name of the preset, used to make the path name
    :type name: str
    :param remove_active: remove_active
    :type remove_active: bool | None
    """
