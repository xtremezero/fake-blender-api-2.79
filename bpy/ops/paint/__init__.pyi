import typing
import collections.abc
import typing_extensions
import bpy.types

def add_simple_uvs(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add cube map uvs on mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def add_texture_paint_slot(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "DIFFUSE_COLOR",
        "DIFFUSE_INTENSITY",
        "ALPHA",
        "TRANSLUCENCY",
        "SPECULAR_COLOR",
        "SPECULAR_INTENSITY",
        "SPECULAR_HARDNESS",
        "AMBIENT",
        "EMIT",
        "MIRROR_COLOR",
        "RAYMIRROR",
        "NORMAL",
        "WARP",
        "DISPLACE",
    ]
    | None = "DIFFUSE_COLOR",
    name: str = "Untitled",
    width: int | None = 1024,
    height: int | None = 1024,
    color: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0, 1.0),
    alpha: bool | None = True,
    generated_type: typing.Literal["BLANK", "UV_GRID", "COLOR_GRID"] | None = "BLANK",
    float: bool | None = False,
):
    """Add a texture paint slot

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Merge method to use
        :type type: typing.Literal['DIFFUSE_COLOR','DIFFUSE_INTENSITY','ALPHA','TRANSLUCENCY','SPECULAR_COLOR','SPECULAR_INTENSITY','SPECULAR_HARDNESS','AMBIENT','EMIT','MIRROR_COLOR','RAYMIRROR','NORMAL','WARP','DISPLACE'] | None
        :param name: Name, Image data-block name
        :type name: str
        :param width: Width, Image width
        :type width: int | None
        :param height: Height, Image height
        :type height: int | None
        :param color: Color, Default fill color
        :type color: collections.abc.Iterable[float] | None
        :param alpha: Alpha, Create an image with an alpha channel
        :type alpha: bool | None
        :param generated_type: Generated Type, Fill the image with a grid for UV map testing

    BLANK Blank, Generate a blank image.

    UV_GRID UV Grid, Generated grid to test UV mappings.

    COLOR_GRID Color Grid, Generated improved UV grid to test UV mappings.
        :type generated_type: typing.Literal['BLANK','UV_GRID','COLOR_GRID'] | None
        :param float: 32 bit Float, Create image with 32 bit floating point bit depth
        :type float: bool | None
    """

def brush_colors_flip(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle foreground and background brush colors

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def brush_select(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    paint_mode: typing.Literal[
        "ACTIVE", "SCULPT", "VERTEX_PAINT", "WEIGHT_PAINT", "TEXTURE_PAINT"
    ]
    | None = "ACTIVE",
    sculpt_tool: typing.Literal[
        "BLOB",
        "CLAY",
        "CLAY_STRIPS",
        "CREASE",
        "DRAW",
        "FILL",
        "FLATTEN",
        "GRAB",
        "INFLATE",
        "LAYER",
        "MASK",
        "NUDGE",
        "PINCH",
        "ROTATE",
        "SCRAPE",
        "SIMPLIFY",
        "SMOOTH",
        "SNAKE_HOOK",
        "THUMB",
    ]
    | None = "BLOB",
    vertex_paint_tool: typing.Literal[
        "MIX",
        "ADD",
        "SUB",
        "MUL",
        "BLUR",
        "LIGHTEN",
        "DARKEN",
        "AVERAGE",
        "SMEAR",
        "COLORDODGE",
        "DIFFERENCE",
        "SCREEN",
        "HARDLIGHT",
        "OVERLAY",
        "SOFTLIGHT",
        "EXCLUSION",
        "LUMINOCITY",
        "SATURATION",
        "HUE",
        "ERASE_ALPHA",
        "ADD_ALPHA",
    ]
    | None = "MIX",
    weight_paint_tool: typing.Literal[
        "MIX",
        "ADD",
        "SUB",
        "MUL",
        "BLUR",
        "LIGHTEN",
        "DARKEN",
        "AVERAGE",
        "SMEAR",
        "COLORDODGE",
        "DIFFERENCE",
        "SCREEN",
        "HARDLIGHT",
        "OVERLAY",
        "SOFTLIGHT",
        "EXCLUSION",
        "LUMINOCITY",
        "SATURATION",
        "HUE",
        "ERASE_ALPHA",
        "ADD_ALPHA",
    ]
    | None = "MIX",
    texture_paint_tool: typing.Literal[
        "DRAW", "SOFTEN", "SMEAR", "CLONE", "FILL", "MASK"
    ]
    | None = "DRAW",
    toggle: bool | None = False,
    create_missing: bool | None = False,
):
    """Select a paint mode's brush by tool type

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param paint_mode: Paint Mode

    ACTIVE Current, Set brush for active paint mode.

    SCULPT Sculpt.

    VERTEX_PAINT Vertex Paint.

    WEIGHT_PAINT Weight Paint.

    TEXTURE_PAINT Texture Paint.
        :type paint_mode: typing.Literal['ACTIVE','SCULPT','VERTEX_PAINT','WEIGHT_PAINT','TEXTURE_PAINT'] | None
        :param sculpt_tool: Sculpt Tool
        :type sculpt_tool: typing.Literal['BLOB','CLAY','CLAY_STRIPS','CREASE','DRAW','FILL','FLATTEN','GRAB','INFLATE','LAYER','MASK','NUDGE','PINCH','ROTATE','SCRAPE','SIMPLIFY','SMOOTH','SNAKE_HOOK','THUMB'] | None
        :param vertex_paint_tool: Vertex Paint Tool

    MIX Mix, Use mix blending mode while painting.

    ADD Add, Use add blending mode while painting.

    SUB Subtract, Use subtract blending mode while painting.

    MUL Multiply, Use multiply blending mode while painting.

    BLUR Blur, Blur the color with surrounding values.

    LIGHTEN Lighten, Use lighten blending mode while painting.

    DARKEN Darken, Use darken blending mode while painting.

    AVERAGE Average, Use average blending mode while painting.

    SMEAR Smear, Use smear blending mode while painting.

    COLORDODGE Color Dodge, Use color dodge blending mode while painting.

    DIFFERENCE Difference, Use difference blending mode while painting.

    SCREEN Screen, Use screen blending mode while painting.

    HARDLIGHT Hardlight, Use hardlight blending mode while painting.

    OVERLAY Overlay, Use overlay blending mode while painting.

    SOFTLIGHT Softlight, Use softlight blending mode while painting.

    EXCLUSION Exclusion, Use exclusion blending mode while painting.

    LUMINOCITY Luminocity, Use luminocity blending mode while painting.

    SATURATION Saturation, Use saturation blending mode while painting.

    HUE Hue, Use hue blending mode while painting.

    ERASE_ALPHA Erase Alpha, Erase alpha while painting.

    ADD_ALPHA Add Alpha, Add alpha while painting.
        :type vertex_paint_tool: typing.Literal['MIX','ADD','SUB','MUL','BLUR','LIGHTEN','DARKEN','AVERAGE','SMEAR','COLORDODGE','DIFFERENCE','SCREEN','HARDLIGHT','OVERLAY','SOFTLIGHT','EXCLUSION','LUMINOCITY','SATURATION','HUE','ERASE_ALPHA','ADD_ALPHA'] | None
        :param weight_paint_tool: Weight Paint Tool

    MIX Mix, Use mix blending mode while painting.

    ADD Add, Use add blending mode while painting.

    SUB Subtract, Use subtract blending mode while painting.

    MUL Multiply, Use multiply blending mode while painting.

    BLUR Blur, Blur the color with surrounding values.

    LIGHTEN Lighten, Use lighten blending mode while painting.

    DARKEN Darken, Use darken blending mode while painting.

    AVERAGE Average, Use average blending mode while painting.

    SMEAR Smear, Use smear blending mode while painting.

    COLORDODGE Color Dodge, Use color dodge blending mode while painting.

    DIFFERENCE Difference, Use difference blending mode while painting.

    SCREEN Screen, Use screen blending mode while painting.

    HARDLIGHT Hardlight, Use hardlight blending mode while painting.

    OVERLAY Overlay, Use overlay blending mode while painting.

    SOFTLIGHT Softlight, Use softlight blending mode while painting.

    EXCLUSION Exclusion, Use exclusion blending mode while painting.

    LUMINOCITY Luminocity, Use luminocity blending mode while painting.

    SATURATION Saturation, Use saturation blending mode while painting.

    HUE Hue, Use hue blending mode while painting.

    ERASE_ALPHA Erase Alpha, Erase alpha while painting.

    ADD_ALPHA Add Alpha, Add alpha while painting.
        :type weight_paint_tool: typing.Literal['MIX','ADD','SUB','MUL','BLUR','LIGHTEN','DARKEN','AVERAGE','SMEAR','COLORDODGE','DIFFERENCE','SCREEN','HARDLIGHT','OVERLAY','SOFTLIGHT','EXCLUSION','LUMINOCITY','SATURATION','HUE','ERASE_ALPHA','ADD_ALPHA'] | None
        :param texture_paint_tool: Texture Paint Tool
        :type texture_paint_tool: typing.Literal['DRAW','SOFTEN','SMEAR','CLONE','FILL','MASK'] | None
        :param toggle: Toggle, Toggle between two brushes rather than cycling
        :type toggle: bool | None
        :param create_missing: Create Missing, If the requested brush type does not exist, create a new brush
        :type create_missing: bool | None
    """

def delete_texture_paint_slot(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete selected texture paint slot

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def face_select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Change selection for all faces

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

def face_select_hide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Hide selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected objects
    :type unselected: bool | None
    """

def face_select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select linked faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def face_select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
):
    """Select linked faces under the cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deselect: Deselect, Deselect rather than select items
    :type deselect: bool | None
    """

def face_select_reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
):
    """Reveal hidden faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    """

def grab_clone(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delta: collections.abc.Iterable[float] | None = (0.0, 0.0),
):
    """Move the clone source image

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param delta: Delta, Delta offset of clone image in 0.0..1.0 coordinates
    :type delta: collections.abc.Iterable[float] | None
    """

def hide_show(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["HIDE", "SHOW"] | None = "HIDE",
    area: typing.Literal["OUTSIDE", "INSIDE", "ALL", "MASKED"] | None = "INSIDE",
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
):
    """Hide/show some vertices

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Whether to hide or show vertices

    HIDE Hide, Hide vertices.

    SHOW Show, Show vertices.
        :type action: typing.Literal['HIDE','SHOW'] | None
        :param area: Area, Which vertices to hide or show

    OUTSIDE Outside, Hide or show vertices outside the selection.

    INSIDE Inside, Hide or show vertices inside the selection.

    ALL All, Hide or show all vertices.

    MASKED Masked, Hide or show vertices that are masked (minimum mask value of 0.5).
        :type area: typing.Literal['OUTSIDE','INSIDE','ALL','MASKED'] | None
        :param xmin: X Min
        :type xmin: int | None
        :param xmax: X Max
        :type xmax: int | None
        :param ymin: Y Min
        :type ymin: int | None
        :param ymax: Y Max
        :type ymax: int | None
    """

def image_from_view(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
):
    """Make an image from the current 3D view for re-projection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Name of the file
    :type filepath: str
    """

def image_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH"] | None = "NORMAL",
):
    """Paint a stroke into the image

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL Normal, Apply brush normally.

    INVERT Invert, Invert action of brush for duration of stroke.

    SMOOTH Smooth, Switch brush to smooth mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH'] | None
    """

def mask_flood_fill(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
    value: float | None = 0.0,
):
    """Fill the whole mask with a given value, or invert its values

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode

    VALUE Value, Set mask to the level specified by the 'value' property.

    VALUE_INVERSE Value Inverted, Set mask to the level specified by the inverted 'value' property.

    INVERT Invert, Invert the mask.
        :type mode: typing.Literal['VALUE','VALUE_INVERSE','INVERT'] | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: float | None
    """

def mask_lasso_gesture(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    mode: typing.Literal["VALUE", "VALUE_INVERSE", "INVERT"] | None = "VALUE",
    value: float | None = 1.0,
):
    """Add mask within the lasso as you move the brush

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param mode: Mode

    VALUE Value, Set mask to the level specified by the 'value' property.

    VALUE_INVERSE Value Inverted, Set mask to the level specified by the inverted 'value' property.

    INVERT Invert, Invert the mask.
        :type mode: typing.Literal['VALUE','VALUE_INVERSE','INVERT'] | None
        :param value: Value, Mask level to use when mode is 'Value'; zero means no masking and one is fully masked
        :type value: float | None
    """

def project_image(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    image: str | None = "",
):
    """Project an edited render from the active camera back onto the object

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param image: Image
    :type image: str | None
    """

def sample_color(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Iterable[int] | None = (0, 0),
    merged: bool | None = False,
    palette: bool | None = False,
):
    """Use the mouse to sample a color in the image

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location
    :type location: collections.abc.Iterable[int] | None
    :param merged: Sample Merged, Sample the output display color
    :type merged: bool | None
    :param palette: Add to Palette
    :type palette: bool | None
    """

def texture_paint_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle texture paint mode in 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vert_select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Change selection for all vertices

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

def vert_select_ungrouped(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
):
    """Select vertices without a group

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def vertex_color_brightness_contrast(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    brightness: float | None = 0.0,
    contrast: float | None = 0.0,
):
    """Adjust vertex color brightness/contrast

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param brightness: Brightness
    :type brightness: float | None
    :param contrast: Contrast
    :type contrast: float | None
    """

def vertex_color_dirt(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    blur_strength: float | None = 1.0,
    blur_iterations: int | None = 1,
    clean_angle: float | None = 3.14159,
    dirt_angle: float | None = 0.0,
    dirt_only: bool | None = False,
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param blur_strength: Blur Strength, Blur strength per iteration
    :type blur_strength: float | None
    :param blur_iterations: Blur Iterations, Number of times to blur the colors (higher blurs more)
    :type blur_iterations: int | None
    :param clean_angle: Highlight Angle, Less than 90 limits the angle used in the tonal range
    :type clean_angle: float | None
    :param dirt_angle: Dirt Angle, Less than 90 limits the angle used in the tonal range
    :type dirt_angle: float | None
    :param dirt_only: Dirt Only, Don't calculate cleans for convex areas
    :type dirt_only: bool | None
    """

def vertex_color_from_weight(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Convert active weight into gray scale vertex colors

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertex_color_hsv(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    h: float | None = 0.5,
    s: float | None = 1.0,
    v: float | None = 1.0,
):
    """Adjust vertex color HSV values

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param h: Hue
    :type h: float | None
    :param s: Saturation
    :type s: float | None
    :param v: Value
    :type v: float | None
    """

def vertex_color_invert(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Invert RGB values

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertex_color_levels(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.0,
    gain: float | None = 1.0,
):
    """Adjust levels of vertex colors

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset, Value to add to colors
    :type offset: float | None
    :param gain: Gain, Value to multiply colors by
    :type gain: float | None
    """

def vertex_color_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Fill the active vertex color layer with the current paint color

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertex_color_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Smooth colors across vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertex_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH"] | None = "NORMAL",
):
    """Paint a stroke in the active vertex color layer

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL Normal, Apply brush normally.

    INVERT Invert, Invert action of brush for duration of stroke.

    SMOOTH Smooth, Switch brush to smooth mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH'] | None
    """

def vertex_paint_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the vertex paint mode in 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weight_from_bones(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["AUTOMATIC", "ENVELOPES"] | None = "AUTOMATIC",
):
    """Set the weights of the groups matching the attached armature's selected bones, using the distance between the vertices and the bones

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Method to use for assigning weights

    AUTOMATIC Automatic, Automatic weights from bones.

    ENVELOPES From Envelopes, Weights from envelopes with user defined radius.
        :type type: typing.Literal['AUTOMATIC','ENVELOPES'] | None
    """

def weight_gradient(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["LINEAR", "RADIAL"] | None = "LINEAR",
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    cursor: int | None = 1002,
):
    """Draw a line to apply a weight gradient to selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['LINEAR','RADIAL'] | None
    :param xstart: X Start
    :type xstart: int | None
    :param xend: X End
    :type xend: int | None
    :param ystart: Y Start
    :type ystart: int | None
    :param yend: Y End
    :type yend: int | None
    :param cursor: Cursor, Mouse cursor style to use during the modal operator
    :type cursor: int | None
    """

def weight_paint(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement]
    | None = None,
    mode: typing.Literal["NORMAL", "INVERT", "SMOOTH"] | None = "NORMAL",
):
    """Paint a stroke in the current vertex group's weights

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param stroke: Stroke
        :type stroke: bpy.types.bpy_prop_collection[bpy.types.OperatorStrokeElement] | None
        :param mode: Stroke Mode, Action taken when a paint stroke is made

    NORMAL Normal, Apply brush normally.

    INVERT Invert, Invert action of brush for duration of stroke.

    SMOOTH Smooth, Switch brush to smooth mode for duration of stroke.
        :type mode: typing.Literal['NORMAL','INVERT','SMOOTH'] | None
    """

def weight_paint_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle weight paint mode in 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weight_sample(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Use the mouse to sample a weight in the 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def weight_sample_group(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    group: str | None = "DEFAULT",
):
    """Select one of the vertex groups available under current mouse position

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param group: Keying Set, The Keying Set to use
    :type group: str | None
    """

def weight_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Fill the active vertex group with the current paint weight

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """
