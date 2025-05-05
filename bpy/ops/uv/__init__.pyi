import typing
import collections.abc
import typing_extensions
import bpy.types

def align(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: typing.Literal[
        "ALIGN_S", "ALIGN_T", "ALIGN_U", "ALIGN_AUTO", "ALIGN_X", "ALIGN_Y"
    ]
    | None = "ALIGN_AUTO",
):
    """Align selected UV vertices to an axis

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param axis: Axis, Axis to align UV locations on

    ALIGN_S Straighten, Align UVs along the line defined by the endpoints.

    ALIGN_T Straighten X, Align UVs along the line defined by the endpoints along the X axis.

    ALIGN_U Straighten Y, Align UVs along the line defined by the endpoints along the Y axis.

    ALIGN_AUTO Align Auto, Automatically choose the axis on which there is most alignment already.

    ALIGN_X Align X, Align UVs on X axis.

    ALIGN_Y Align Y, Align UVs on Y axis.
        :type axis: typing.Literal['ALIGN_S','ALIGN_T','ALIGN_U','ALIGN_AUTO','ALIGN_X','ALIGN_Y'] | None
    """

def average_islands_scale(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Average the size of separate UV islands, based on their area in 3D space

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def circle_select(
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
    """Select UV vertices using circle selection

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

def cube_project(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    cube_size: float | None = 1.0,
    correct_aspect: bool | None = True,
    clip_to_bounds: bool | None = False,
    scale_to_bounds: bool | None = False,
):
    """Project the UV vertices of the mesh over the six faces of a cube

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param cube_size: Cube Size, Size of the cube to project on
    :type cube_size: float | None
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool | None
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: bool | None
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool | None
    """

def cursor_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0),
):
    """Set 2D cursor location

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Cursor location in normalized (0.0-1.0) coordinates
    :type location: collections.abc.Iterable[float] | None
    """

def cylinder_project(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["VIEW_ON_EQUATOR", "VIEW_ON_POLES", "ALIGN_TO_OBJECT"]
    | None = "VIEW_ON_EQUATOR",
    align: typing.Literal["POLAR_ZX", "POLAR_ZY"] | None = "POLAR_ZX",
    radius: float | None = 1.0,
    correct_aspect: bool | None = True,
    clip_to_bounds: bool | None = False,
    scale_to_bounds: bool | None = False,
):
    """Project the UV vertices of the mesh over the curved wall of a cylinder

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param direction: Direction, Direction of the sphere or cylinder

    VIEW_ON_EQUATOR View on Equator, 3D view is on the equator.

    VIEW_ON_POLES View on Poles, 3D view is on the poles.

    ALIGN_TO_OBJECT Align to Object, Align according to object transform.
        :type direction: typing.Literal['VIEW_ON_EQUATOR','VIEW_ON_POLES','ALIGN_TO_OBJECT'] | None
        :param align: Align, How to determine rotation around the pole

    POLAR_ZX Polar ZX, Polar 0 is X.

    POLAR_ZY Polar ZY, Polar 0 is Y.
        :type align: typing.Literal['POLAR_ZX','POLAR_ZY'] | None
        :param radius: Radius, Radius of the sphere or cylinder
        :type radius: float | None
        :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        :type correct_aspect: bool | None
        :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        :type clip_to_bounds: bool | None
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        :type scale_to_bounds: bool | None
    """

def export_layout(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
    export_all: bool | None = False,
    modified: bool | None = False,
    mode: typing.Literal["SVG", "EPS", "PNG"] | None = "PNG",
    size: collections.abc.Iterable[int] | None = (1024, 1024),
    opacity: float | None = 0.25,
    tessellated: bool | None = False,
):
    """Export UV layout to file

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: filepath
        :type filepath: str
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param export_all: All UVs, Export all UVs in this mesh (not just visible ones)
        :type export_all: bool | None
        :param modified: Modified, Exports UVs from the modified mesh
        :type modified: bool | None
        :param mode: Format, File format to export the UV layout to

    SVG Scalable Vector Graphic (.svg), Export the UV layout to a vector SVG file.

    EPS Encapsulate PostScript (.eps), Export the UV layout to a vector EPS file.

    PNG PNG Image (.png), Export the UV layout to a bitmap image.
        :type mode: typing.Literal['SVG','EPS','PNG'] | None
        :param size: size, Dimensions of the exported file
        :type size: collections.abc.Iterable[int] | None
        :param opacity: Fill Opacity, Set amount of opacity for exported UV layout
        :type opacity: float | None
        :param tessellated: Tessellated UVs, Export tessellated UVs instead of polygons ones
        :type tessellated: bool | None
    """

def follow_active_quads(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["EVEN", "LENGTH", "LENGTH_AVERAGE"] | None = "LENGTH_AVERAGE",
):
    """Follow UVs from active quads along continuous face loops

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Edge Length Mode, Method to space UV edge loops

    EVEN Even, Space all UVs evenly.

    LENGTH Length, Average space UVs edge length of each loop.

    LENGTH_AVERAGE Length Average, Average space UVs edge length of each loop.
        :type mode: typing.Literal['EVEN','LENGTH','LENGTH_AVERAGE'] | None
    """

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
):
    """Hide (un)selected UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool | None
    """

def lightmap_pack(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    PREF_CONTEXT: typing.Literal["SEL_FACES", "ALL_FACES", "ALL_OBJECTS"]
    | None = "SEL_FACES",
    PREF_PACK_IN_ONE: bool | None = True,
    PREF_NEW_UVLAYER: bool | None = False,
    PREF_APPLY_IMAGE: bool | None = False,
    PREF_IMG_PX_SIZE: int | None = 512,
    PREF_BOX_DIV: int | None = 12,
    PREF_MARGIN_DIV: float | None = 0.1,
):
    """Pack each faces UV's into the UV bounds

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param PREF_CONTEXT: Selection

    SEL_FACES Selected Faces, Space all UVs evenly.

    ALL_FACES All Faces, Average space UVs edge length of each loop.

    ALL_OBJECTS Selected Mesh Object, Average space UVs edge length of each loop.
        :type PREF_CONTEXT: typing.Literal['SEL_FACES','ALL_FACES','ALL_OBJECTS'] | None
        :param PREF_PACK_IN_ONE: Share Tex Space, Objects Share texture space, map all objects into 1 uvmap
        :type PREF_PACK_IN_ONE: bool | None
        :param PREF_NEW_UVLAYER: New UV Map, Create a new UV map for every mesh packed
        :type PREF_NEW_UVLAYER: bool | None
        :param PREF_APPLY_IMAGE: New Image, Assign new images for every mesh (only one if shared tex space enabled)
        :type PREF_APPLY_IMAGE: bool | None
        :param PREF_IMG_PX_SIZE: Image Size, Width and Height for the new image
        :type PREF_IMG_PX_SIZE: int | None
        :param PREF_BOX_DIV: Pack Quality, Pre Packing before the complex boxpack
        :type PREF_BOX_DIV: int | None
        :param PREF_MARGIN_DIV: Margin, Size of the margin as a division of the UV
        :type PREF_MARGIN_DIV: float | None
    """

def mark_seam(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
):
    """Mark selected UV edges as seams

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear Seams, Clear instead of marking seams
    :type clear: bool | None
    """

def minimize_stretch(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    fill_holes: bool | None = True,
    blend: float | None = 0.0,
    iterations: int | None = 0,
):
    """Reduce UV stretching by relaxing angles

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param fill_holes: Fill Holes, Virtual fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
    :type fill_holes: bool | None
    :param blend: Blend, Blend factor between stretch minimized and original
    :type blend: float | None
    :param iterations: Iterations, Number of iterations to run, 0 is unlimited when run interactively
    :type iterations: int | None
    """

def pack_islands(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    rotate: bool | None = True,
    margin: float | None = 0.001,
):
    """Transform all islands so that they fill up the UV space as much as possible

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param rotate: Rotate, Rotate islands for best fit
    :type rotate: bool | None
    :param margin: Margin, Space between islands
    :type margin: float | None
    """

def pin(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
):
    """Set/clear selected UV vertices as anchored between multiple unwrap operations

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear, Clear pinning for the selection instead of setting it
    :type clear: bool | None
    """

def project_from_view(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    orthographic: bool | None = False,
    camera_bounds: bool | None = True,
    correct_aspect: bool | None = True,
    clip_to_bounds: bool | None = False,
    scale_to_bounds: bool | None = False,
):
    """Project the UV vertices of the mesh as seen in current 3D view

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param orthographic: Orthographic, Use orthographic projection
    :type orthographic: bool | None
    :param camera_bounds: Camera Bounds, Map UVs to the camera region taking resolution and aspect into account
    :type camera_bounds: bool | None
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool | None
    :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
    :type clip_to_bounds: bool | None
    :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
    :type scale_to_bounds: bool | None
    """

def remove_doubles(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.02,
    use_unselected: bool | None = False,
):
    """Selected UV vertices that are within a radius of each other are welded together

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Merge Distance, Maximum distance between welded vertices
    :type threshold: float | None
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :type use_unselected: bool | None
    """

def reset(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset UV projection

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
    """Reveal all hidden UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    """

def seams_from_islands(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mark_seams: bool | None = True,
    mark_sharp: bool | None = False,
):
    """Set mesh seams according to island setup in the UV editor

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mark_seams: Mark Seams, Mark boundary edges as seams
    :type mark_seams: bool | None
    :param mark_sharp: Mark Sharp, Mark boundary edges as sharp
    :type mark_sharp: bool | None
    """

def select(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0),
):
    """Select UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: collections.abc.Iterable[float] | None
    """

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Change selection of all UV vertices

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

def select_border(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    pinned: bool | None = False,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    deselect: bool | None = False,
    extend: bool | None = True,
):
    """Select UV vertices using border selection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param pinned: Pinned, Border select pinned UVs only
    :type pinned: bool | None
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
    """Select UVs using lasso selection

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

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect UV vertices at the boundary of each selection region

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
):
    """Select all UV vertices linked to the active UV map

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    :param deselect: Deselect, Deselect linked UV vertices rather than selecting them
    :type deselect: bool | None
    """

def select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0),
):
    """Select all UV vertices linked under the mouse

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    :param deselect: Deselect, Deselect linked UV vertices rather than selecting them
    :type deselect: bool | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: collections.abc.Iterable[float] | None
    """

def select_loop(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0),
):
    """Select a loop of connected UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection rather than clearing the existing selection
    :type extend: bool | None
    :param location: Location, Mouse location in normalized coordinates, 0.0 to 1.0 is within the image bounds
    :type location: collections.abc.Iterable[float] | None
    """

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select more UV vertices connected to initial selection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_pinned(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select all pinned UV vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_split(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select only entirely selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def smart_project(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 66.0,
    island_margin: float | None = 0.0,
    user_area_weight: float | None = 0.0,
    use_aspect: bool | None = True,
    stretch_to_bounds: bool | None = True,
):
    """This script projection unwraps the selected faces of a mesh (it operates on all selected mesh objects, and can be used to unwrap selected faces, or all faces)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle_limit: Angle Limit, Lower for more projection groups, higher for less distortion
    :type angle_limit: float | None
    :param island_margin: Island Margin, Margin to reduce bleed from adjacent islands
    :type island_margin: float | None
    :param user_area_weight: Area Weight, Weight projections vector by faces with larger areas
    :type user_area_weight: float | None
    :param use_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type use_aspect: bool | None
    :param stretch_to_bounds: Stretch to UV Bounds, Stretch the final output to texture bounds
    :type stretch_to_bounds: bool | None
    """

def snap_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    target: typing.Literal["PIXELS", "SELECTED"] | None = "PIXELS",
):
    """Snap cursor to target type

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param target: Target, Target to snap the selected UVs to
    :type target: typing.Literal['PIXELS','SELECTED'] | None
    """

def snap_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    target: typing.Literal["PIXELS", "CURSOR", "CURSOR_OFFSET", "ADJACENT_UNSELECTED"]
    | None = "PIXELS",
):
    """Snap selected UV vertices to target type

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param target: Target, Target to snap the selected UVs to
    :type target: typing.Literal['PIXELS','CURSOR','CURSOR_OFFSET','ADJACENT_UNSELECTED'] | None
    """

def sphere_project(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["VIEW_ON_EQUATOR", "VIEW_ON_POLES", "ALIGN_TO_OBJECT"]
    | None = "VIEW_ON_EQUATOR",
    align: typing.Literal["POLAR_ZX", "POLAR_ZY"] | None = "POLAR_ZX",
    correct_aspect: bool | None = True,
    clip_to_bounds: bool | None = False,
    scale_to_bounds: bool | None = False,
):
    """Project the UV vertices of the mesh over the curved surface of a sphere

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param direction: Direction, Direction of the sphere or cylinder

    VIEW_ON_EQUATOR View on Equator, 3D view is on the equator.

    VIEW_ON_POLES View on Poles, 3D view is on the poles.

    ALIGN_TO_OBJECT Align to Object, Align according to object transform.
        :type direction: typing.Literal['VIEW_ON_EQUATOR','VIEW_ON_POLES','ALIGN_TO_OBJECT'] | None
        :param align: Align, How to determine rotation around the pole

    POLAR_ZX Polar ZX, Polar 0 is X.

    POLAR_ZY Polar ZY, Polar 0 is Y.
        :type align: typing.Literal['POLAR_ZX','POLAR_ZY'] | None
        :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
        :type correct_aspect: bool | None
        :param clip_to_bounds: Clip to Bounds, Clip UV coordinates to bounds after unwrapping
        :type clip_to_bounds: bool | None
        :param scale_to_bounds: Scale to Bounds, Scale UV coordinates to bounds after unwrapping
        :type scale_to_bounds: bool | None
    """

def stitch(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_limit: bool | None = False,
    snap_islands: bool | None = True,
    limit: float | None = 0.01,
    static_island: int | None = 0,
    midpoint_snap: bool | None = False,
    clear_seams: bool | None = True,
    mode: typing.Literal["VERTEX", "EDGE"] | None = "VERTEX",
    stored_mode: typing.Literal["VERTEX", "EDGE"] | None = "VERTEX",
    selection: bpy.types.bpy_prop_collection[bpy.types.SelectedUvElement] | None = None,
):
    """Stitch selected UV vertices by proximity

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_limit: Use Limit, Stitch UVs within a specified limit distance
    :type use_limit: bool | None
    :param snap_islands: Snap Islands, Snap islands together (on edge stitch mode, rotates the islands too)
    :type snap_islands: bool | None
    :param limit: Limit, Limit distance in normalized coordinates
    :type limit: float | None
    :param static_island: Static Island, Island that stays in place when stitching islands
    :type static_island: int | None
    :param midpoint_snap: Snap At Midpoint, UVs are stitched at midpoint instead of at static island
    :type midpoint_snap: bool | None
    :param clear_seams: Clear Seams, Clear seams of stitched edges
    :type clear_seams: bool | None
    :param mode: Operation Mode, Use vertex or edge stitching
    :type mode: typing.Literal['VERTEX','EDGE'] | None
    :param stored_mode: Stored Operation Mode, Use vertex or edge stitching
    :type stored_mode: typing.Literal['VERTEX','EDGE'] | None
    :param selection: Selection
    :type selection: bpy.types.bpy_prop_collection[bpy.types.SelectedUvElement] | None
    """

def tile_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    tile: collections.abc.Iterable[int] | None = (0, 0),
):
    """Set UV image tile coordinates

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param tile: Tile, Tile coordinate
    :type tile: collections.abc.Iterable[int] | None
    """

def unwrap(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    method: typing.Literal["ANGLE_BASED", "CONFORMAL"] | None = "ANGLE_BASED",
    fill_holes: bool | None = True,
    correct_aspect: bool | None = True,
    use_subsurf_data: bool | None = False,
    margin: float | None = 0.001,
):
    """Unwrap the mesh of the object being edited

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param method: Method, Unwrapping method (Angle Based usually gives better results than Conformal, while being somewhat slower)
    :type method: typing.Literal['ANGLE_BASED','CONFORMAL'] | None
    :param fill_holes: Fill Holes, Virtual fill holes in mesh before unwrapping, to better avoid overlaps and preserve symmetry
    :type fill_holes: bool | None
    :param correct_aspect: Correct Aspect, Map UVs taking image aspect ratio into account
    :type correct_aspect: bool | None
    :param use_subsurf_data: Use Subsurf Modifier, Map UVs taking vertex position after Subdivision Surface modifier has been applied
    :type use_subsurf_data: bool | None
    :param margin: Margin, Space between islands
    :type margin: float | None
    """

def weld(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Weld selected UV vertices together

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """
