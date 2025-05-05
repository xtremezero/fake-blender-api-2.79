import typing
import collections.abc
import typing_extensions
import bpy.ops.transform
import bpy.types

def beautify_fill(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 3.14159,
):
    """Rearrange some faces to try to get less degenerated geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: float | None
    """

def bevel(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset_type: typing.Literal["OFFSET", "WIDTH", "DEPTH", "PERCENT"]
    | None = "OFFSET",
    offset: float | None = 0.0,
    segments: int | None = 1,
    profile: float | None = 0.5,
    vertex_only: bool | None = False,
    clamp_overlap: bool | None = False,
    loop_slide: bool | None = True,
    material: int | None = -1,
):
    """Edge Bevel

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param offset_type: Amount Type, What distance Amount measures

    OFFSET Offset, Amount is offset of new edges from original.

    WIDTH Width, Amount is width of new face.

    DEPTH Depth, Amount is perpendicular distance from original edge to bevel face.

    PERCENT Percent, Amount is percent of adjacent edge length.
        :type offset_type: typing.Literal['OFFSET','WIDTH','DEPTH','PERCENT'] | None
        :param offset: Amount
        :type offset: float | None
        :param segments: Segments, Segments for curved edge
        :type segments: int | None
        :param profile: Profile, Controls profile shape (0.5 = round)
        :type profile: float | None
        :param vertex_only: Vertex Only, Bevel only vertices
        :type vertex_only: bool | None
        :param clamp_overlap: Clamp Overlap, Do not allow beveled edges/vertices to overlap each other
        :type clamp_overlap: bool | None
        :param loop_slide: Loop Slide, Prefer slide along edge to even widths
        :type loop_slide: bool | None
        :param material: Material, Material for bevel faces (-1 means use adjacent faces)
        :type material: int | None
    """

def bisect(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    plane_co: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    plane_no: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    use_fill: bool | None = False,
    clear_inner: bool | None = False,
    clear_outer: bool | None = False,
    threshold: float | None = 0.0001,
    xstart: int | None = 0,
    xend: int | None = 0,
    ystart: int | None = 0,
    yend: int | None = 0,
    cursor: int | None = 1002,
):
    """Cut geometry along a plane (click-drag to define plane)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param plane_co: Plane Point, A point on the plane
    :type plane_co: collections.abc.Iterable[float] | None
    :param plane_no: Plane Normal, The direction the plane points
    :type plane_no: collections.abc.Iterable[float] | None
    :param use_fill: Fill, Fill in the cut
    :type use_fill: bool | None
    :param clear_inner: Clear Inner, Remove geometry behind the plane
    :type clear_inner: bool | None
    :param clear_outer: Clear Outer, Remove geometry in front of the plane
    :type clear_outer: bool | None
    :param threshold: Axis Threshold, Preserves the existing geometry along the cut plane
    :type threshold: float | None
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

def blend_from_shape(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    shape: str | None = "",
    blend: float | None = 1.0,
    add: bool | None = True,
):
    """Blend in shape from a shape key

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param shape: Shape, Shape key to use for blending
    :type shape: str | None
    :param blend: Blend, Blending factor
    :type blend: float | None
    :param add: Add, Add rather than blend between shapes
    :type add: bool | None
    """

def bridge_edge_loops(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SINGLE", "CLOSED", "PAIRS"] | None = "SINGLE",
    use_merge: bool | None = False,
    merge_factor: float | None = 0.5,
    twist_offset: int | None = 0,
    number_cuts: int | None = 0,
    interpolation: typing.Literal["LINEAR", "PATH", "SURFACE"] | None = "PATH",
    smoothness: float | None = 1.0,
    profile_shape_factor: float | None = 0.0,
    profile_shape: typing.Literal[
        "SMOOTH", "SPHERE", "ROOT", "INVERSE_SQUARE", "SHARP", "LINEAR"
    ]
    | None = "SMOOTH",
):
    """Make faces between two or more edge loops

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Connect Loops, Method of bridging multiple loops
        :type type: typing.Literal['SINGLE','CLOSED','PAIRS'] | None
        :param use_merge: Merge, Merge rather than creating faces
        :type use_merge: bool | None
        :param merge_factor: Merge Factor
        :type merge_factor: float | None
        :param twist_offset: Twist, Twist offset for closed loops
        :type twist_offset: int | None
        :param number_cuts: Number of Cuts
        :type number_cuts: int | None
        :param interpolation: Interpolation, Interpolation method
        :type interpolation: typing.Literal['LINEAR','PATH','SURFACE'] | None
        :param smoothness: Smoothness, Smoothness factor
        :type smoothness: float | None
        :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
        :type profile_shape_factor: float | None
        :param profile_shape: Profile Shape, Shape of the profile

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.
        :type profile_shape: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR'] | None
    """

def colors_reverse(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flip direction of vertex colors inside faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def colors_rotate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_ccw: bool | None = False,
):
    """Rotate vertex colors inside faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool | None
    """

def convex_hull(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delete_unused: bool | None = True,
    use_existing_faces: bool | None = True,
    make_holes: bool | None = False,
    join_triangles: bool | None = True,
    face_threshold: float | None = 0.698132,
    shape_threshold: float | None = 0.698132,
    uvs: bool | None = False,
    vcols: bool | None = False,
    seam: bool | None = False,
    sharp: bool | None = False,
    materials: bool | None = False,
):
    """Enclose selected vertices in a convex polyhedron

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param delete_unused: Delete Unused, Delete selected elements that are not used by the hull
    :type delete_unused: bool | None
    :param use_existing_faces: Use Existing Faces, Skip hull triangles that are covered by a pre-existing face
    :type use_existing_faces: bool | None
    :param make_holes: Make Holes, Delete selected faces that are used by the hull
    :type make_holes: bool | None
    :param join_triangles: Join Triangles, Merge adjacent triangles into quads
    :type join_triangles: bool | None
    :param face_threshold: Max Face Angle, Face angle limit
    :type face_threshold: float | None
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :type shape_threshold: float | None
    :param uvs: Compare UVs
    :type uvs: bool | None
    :param vcols: Compare VCols
    :type vcols: bool | None
    :param seam: Compare Seam
    :type seam: bool | None
    :param sharp: Compare Sharp
    :type sharp: bool | None
    :param materials: Compare Materials
    :type materials: bool | None
    """

def customdata_custom_splitnormals_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a custom split normals layer, if none exists yet

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def customdata_custom_splitnormals_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove the custom split normals layer, if it exists

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def customdata_mask_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear vertex sculpt masking data from the mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def customdata_skin_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a vertex skin layer

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def customdata_skin_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear vertex skin layer

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def decimate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 1.0,
    use_vertex_group: bool | None = False,
    vertex_group_factor: float | None = 1.0,
    invert_vertex_group: bool | None = False,
    use_symmetry: bool | None = False,
    symmetry_axis: typing.Literal["X", "Y", "Z"] | None = "Y",
):
    """Simplify geometry by collapsing edges

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param ratio: Ratio
    :type ratio: float | None
    :param use_vertex_group: Vertex Group, Use active vertex group as an influence
    :type use_vertex_group: bool | None
    :param vertex_group_factor: Weight, Vertex group strength
    :type vertex_group_factor: float | None
    :param invert_vertex_group: Invert, Invert vertex group influence
    :type invert_vertex_group: bool | None
    :param use_symmetry: Symmetry, Maintain symmetry on an axis
    :type use_symmetry: bool | None
    :param symmetry_axis: Axis, Axis of symmetry
    :type symmetry_axis: typing.Literal['X','Y','Z'] | None
    """

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["VERT", "EDGE", "FACE", "EDGE_FACE", "ONLY_FACE"]
    | None = "VERT",
):
    """Delete selected vertices, edges or faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Method used for deleting mesh data
    :type type: typing.Literal['VERT','EDGE','FACE','EDGE_FACE','ONLY_FACE'] | None
    """

def delete_edgeloop(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_split: bool | None = True,
):
    """Delete an edge loop by merging the faces on each side

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | None
    """

def delete_loose(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = True,
    use_edges: bool | None = True,
    use_faces: bool | None = False,
):
    """Delete loose vertices, edges or faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Vertices, Remove loose vertices
    :type use_verts: bool | None
    :param use_edges: Edges, Remove loose edges
    :type use_edges: bool | None
    :param use_faces: Faces, Remove loose faces
    :type use_faces: bool | None
    """

def dissolve_degenerate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.0001,
):
    """Dissolve zero area faces and zero length edges

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Merge Distance, Minimum distance between elements to merge
    :type threshold: float | None
    """

def dissolve_edges(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = True,
    use_face_split: bool | None = False,
):
    """Dissolve edges, merging faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Dissolve Verts, Dissolve remaining vertices
    :type use_verts: bool | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | None
    """

def dissolve_faces(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = False,
):
    """Dissolve faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Dissolve Verts, Dissolve remaining vertices
    :type use_verts: bool | None
    """

def dissolve_limited(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 0.0872665,
    use_dissolve_boundaries: bool | None = False,
    delimit: set[typing.Literal["NORMAL", "MATERIAL", "SEAM", "SHARP", "UV"]] | None = {
        "NORMAL"
    },
):
    """Dissolve selected edges and verts, limited by the angle of surrounding geometry

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param angle_limit: Max Angle, Angle limit
        :type angle_limit: float | None
        :param use_dissolve_boundaries: All Boundaries, Dissolve all vertices inbetween face boundaries
        :type use_dissolve_boundaries: bool | None
        :param delimit: Delimit, Delimit dissolve operation

    NORMAL Normal, Delimit by face directions.

    MATERIAL Material, Delimit by face material.

    SEAM Seam, Delimit by edge seams.

    SHARP Sharp, Delimit by sharp edges.

    UV UVs, Delimit by UV coordinates.
        :type delimit: set[typing.Literal['NORMAL','MATERIAL','SEAM','SHARP','UV']] | None
    """

def dissolve_mode(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_verts: bool | None = False,
    use_face_split: bool | None = False,
    use_boundary_tear: bool | None = False,
):
    """Dissolve geometry based on the selection mode

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_verts: Dissolve Verts, Dissolve remaining vertices
    :type use_verts: bool | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | None
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    :type use_boundary_tear: bool | None
    """

def dissolve_verts(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_split: bool | None = False,
    use_boundary_tear: bool | None = False,
):
    """Dissolve verts, merge edges and faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_split: Face Split, Split off face corners to maintain surrounding geometry
    :type use_face_split: bool | None
    :param use_boundary_tear: Tear Boundary, Split off face corners instead of merging faces
    :type use_boundary_tear: bool | None
    """

def drop_named_image(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "Image",
    filepath: str = "Path",
    relative_path: bool | None = True,
):
    """Assign Image to active UV Map, or create an UV Map

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param name: Name, Image name to assign
    :type name: str
    :param filepath: Filepath, Path to image file
    :type filepath: str
    :param relative_path: Relative Path, Select the file relative to the blend file
    :type relative_path: bool | None
    """

def dupli_extrude_cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    rotate_source: bool | None = True,
):
    """Duplicate and extrude selected vertices, edges or faces towards the mouse cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param rotate_source: Rotate Source, Rotate initial selection giving better shape
    :type rotate_source: bool | None
    """

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: int | None = 1,
):
    """Duplicate selected vertices, edges or faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: int | None
    """

def duplicate_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Duplicate mesh and move

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_duplicate: Duplicate, Duplicate selected vertices, edges or faces
    :type MESH_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def edge_collapse(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Collapse selected edges

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def edge_face_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add an edge or face to selected

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def edge_rotate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_ccw: bool | None = False,
):
    """Rotate selected edge or adjoining faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool | None
    """

def edge_split(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Split selected edges so that each neighbor face gets its own copy

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def edgering_select(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    ring: bool | None = True,
):
    """Select an edge ring

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    :param deselect: Deselect, Remove from the selection
    :type deselect: bool | None
    :param toggle: Toggle Select, Toggle the selection
    :type toggle: bool | None
    :param ring: Select Ring, Select ring
    :type ring: bool | None
    """

def edges_select_sharp(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    sharpness: float | None = 0.523599,
):
    """Select all sharp-enough edges

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param sharpness: Sharpness
    :type sharpness: float | None
    """

def extrude_edges_indiv(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_normal_flip: bool | None = False,
    mirror: bool | None = False,
):
    """Extrude individual edges only

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    """

def extrude_edges_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude edges and move result

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_edges_indiv: Extrude Only Edges, Extrude individual edges only
    :type MESH_OT_extrude_edges_indiv: extrude_edges_indiv | None
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def extrude_faces_indiv(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
):
    """Extrude individual faces only

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    """

def extrude_faces_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_faces_indiv: extrude_faces_indiv | None = None,
    TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None = None,
):
    """Extrude faces and move result

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_faces_indiv: Extrude Individual Faces, Extrude individual faces only
    :type MESH_OT_extrude_faces_indiv: extrude_faces_indiv | None
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    :type TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None
    """

def extrude_region(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_normal_flip: bool | None = False,
    mirror: bool | None = False,
):
    """Extrude region of faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    """

def extrude_region_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude region and move result

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: extrude_region | None
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def extrude_region_shrink_fatten(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_region: extrude_region | None = None,
    TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None = None,
):
    """Extrude along normals and move result

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_region: Extrude Region, Extrude region of faces
    :type MESH_OT_extrude_region: extrude_region | None
    :param TRANSFORM_OT_shrink_fatten: Shrink/Fatten, Shrink/fatten selected vertices along normals
    :type TRANSFORM_OT_shrink_fatten: bpy.ops.transform.shrink_fatten | None
    """

def extrude_repeat(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 2.0,
    steps: int | None = 10,
):
    """Extrude selected vertices, edges or faces repeatedly

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Offset
    :type offset: float | None
    :param steps: Steps
    :type steps: int | None
    """

def extrude_vertices_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_extrude_verts_indiv: extrude_verts_indiv | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extrude vertices and move result

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_extrude_verts_indiv: Extrude Only Vertices, Extrude individual vertices only
    :type MESH_OT_extrude_verts_indiv: extrude_verts_indiv | None
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def extrude_verts_indiv(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mirror: bool | None = False,
):
    """Extrude individual vertices only

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mirror: Mirror Editing
    :type mirror: bool | None
    """

def face_make_planar(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 1.0,
    repeat: int | None = 1,
):
    """Flatten selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor
    :type factor: float | None
    :param repeat: Iterations
    :type repeat: int | None
    """

def face_split_by_edges(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Weld loose edges into faces (splitting them into new faces)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def faces_mirror_uv(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal["POSITIVE", "NEGATIVE"] | None = "POSITIVE",
    precision: int | None = 3,
):
    """Copy mirror UV coordinates on the X axis based on a mirrored mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Axis Direction
    :type direction: typing.Literal['POSITIVE','NEGATIVE'] | None
    :param precision: Precision, Tolerance for finding vertex duplicates
    :type precision: int | None
    """

def faces_select_linked_flat(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    sharpness: float | None = 0.0174533,
):
    """Select linked faces by angle

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param sharpness: Sharpness
    :type sharpness: float | None
    """

def faces_shade_flat(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Display faces flat

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def faces_shade_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Display faces smooth (using vertex normals)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def fill(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_beauty: bool | None = True,
):
    """Fill a selected edge loop with faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_beauty: Beauty, Use best triangulation division
    :type use_beauty: bool | None
    """

def fill_grid(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    span: int | None = 1,
    offset: int | None = 0,
    use_interp_simple: bool | None = False,
):
    """Fill grid from two loops

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param span: Span, Number of grid columns
    :type span: int | None
    :param offset: Offset, Vertex that is the corner of the grid
    :type offset: int | None
    :param use_interp_simple: Simple Blending, Use simple interpolation of grid vertices
    :type use_interp_simple: bool | None
    """

def fill_holes(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    sides: int | None = 4,
):
    """Fill in holes (boundary edge loops)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param sides: Sides, Number of sides in hole required to fill (zero fills all holes)
    :type sides: int | None
    """

def flip_normals(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flip the direction of selected faces' normals (and of their vertices)

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
    """Hide (un)selected vertices, edges or faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected
    :type unselected: bool | None
    """

def inset(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_boundary: bool | None = True,
    use_even_offset: bool | None = True,
    use_relative_offset: bool | None = False,
    use_edge_rail: bool | None = False,
    thickness: float | None = 0.01,
    depth: float | None = 0.0,
    use_outset: bool | None = False,
    use_select_inset: bool | None = False,
    use_individual: bool | None = False,
    use_interpolate: bool | None = True,
):
    """Inset new faces into selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_boundary: Boundary, Inset face boundaries
    :type use_boundary: bool | None
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool | None
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: bool | None
    :param use_edge_rail: Edge Rail, Inset the region along existing edges
    :type use_edge_rail: bool | None
    :param thickness: Thickness
    :type thickness: float | None
    :param depth: Depth
    :type depth: float | None
    :param use_outset: Outset, Outset rather than inset
    :type use_outset: bool | None
    :param use_select_inset: Select Outer, Select the new inset faces
    :type use_select_inset: bool | None
    :param use_individual: Individual, Individual Face Inset
    :type use_individual: bool | None
    :param use_interpolate: Interpolate, Blend face data across the inset
    :type use_interpolate: bool | None
    """

def intersect(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["SELECT", "SELECT_UNSELECT"] | None = "SELECT_UNSELECT",
    separate_mode: typing.Literal["ALL", "CUT", "NONE"] | None = "CUT",
    threshold: float | None = 1e-06,
):
    """Cut an intersection into faces

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Source

    SELECT Self Intersect, Self intersect selected faces.

    SELECT_UNSELECT Selected/Unselected, Intersect selected with unselected faces.
        :type mode: typing.Literal['SELECT','SELECT_UNSELECT'] | None
        :param separate_mode: Separate Mode

    ALL All, Separate all geometry from intersections.

    CUT Cut, Cut into geometry keeping each side separate (Selected/Unselected only).

    NONE Merge, Merge all geometry from the intersection.
        :type separate_mode: typing.Literal['ALL','CUT','NONE'] | None
        :param threshold: Merge threshold
        :type threshold: float | None
    """

def intersect_boolean(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    operation: typing.Literal["INTERSECT", "UNION", "DIFFERENCE"] | None = "DIFFERENCE",
    use_swap: bool | None = False,
    threshold: float | None = 1e-06,
):
    """Cut solid geometry from selected to unselected

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param operation: Boolean
    :type operation: typing.Literal['INTERSECT','UNION','DIFFERENCE'] | None
    :param use_swap: Swap, Use with difference intersection to swap which side is kept
    :type use_swap: bool | None
    :param threshold: Merge threshold
    :type threshold: float | None
    """

def knife_project(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    cut_through: bool | None = False,
):
    """Use other objects outlines & boundaries to project knife cuts

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param cut_through: Cut through, Cut through all faces, not just visible ones
    :type cut_through: bool | None
    """

def knife_tool(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_occlude_geometry: bool | None = True,
    only_selected: bool | None = False,
    wait_for_input: bool | None = True,
):
    """Cut new topology

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_occlude_geometry: Occlude Geometry, Only cut the front most geometry
    :type use_occlude_geometry: bool | None
    :param only_selected: Only Selected, Only cut selected geometry
    :type only_selected: bool | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    """

def loop_multi_select(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ring: bool | None = False,
):
    """Select a loop of connected edges by connection type

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param ring: Ring
    :type ring: bool | None
    """

def loop_select(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    ring: bool | None = False,
):
    """Select a loop of connected edges

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend Select, Extend the selection
    :type extend: bool | None
    :param deselect: Deselect, Remove from the selection
    :type deselect: bool | None
    :param toggle: Toggle Select, Toggle the selection
    :type toggle: bool | None
    :param ring: Select Ring, Select ring
    :type ring: bool | None
    """

def loop_to_region(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select_bigger: bool | None = False,
):
    """Select region of faces inside of a selected loop of edges

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select_bigger: Select Bigger, Select bigger regions instead of smaller ones
    :type select_bigger: bool | None
    """

def loopcut(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 1,
    smoothness: float | None = 0.0,
    falloff: typing.Literal[
        "SMOOTH", "SPHERE", "ROOT", "INVERSE_SQUARE", "SHARP", "LINEAR"
    ]
    | None = "INVERSE_SQUARE",
    edge_index: int | None = -1,
    mesh_select_mode_init: collections.abc.Iterable[bool] | None = (
        False,
        False,
        False,
    ),
):
    """Add a new loop between existing loops

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param number_cuts: Number of Cuts
        :type number_cuts: int | None
        :param smoothness: Smoothness, Smoothness factor
        :type smoothness: float | None
        :param falloff: Falloff, Falloff type the feather

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.
        :type falloff: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR'] | None
        :param edge_index: Edge Index
        :type edge_index: int | None
        :type mesh_select_mode_init: collections.abc.Iterable[bool] | None
    """

def loopcut_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_loopcut: loopcut | None = None,
    TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None = None,
):
    """Cut mesh loop and slide it

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_loopcut: Loop Cut, Add a new loop between existing loops
    :type MESH_OT_loopcut: loopcut | None
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    :type TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None
    """

def mark_freestyle_edge(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
):
    """(Un)mark selected edges as Freestyle feature edges

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | None
    """

def mark_freestyle_face(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
):
    """(Un)mark selected faces for exclusion from Freestyle feature edge detection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | None
    """

def mark_seam(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
):
    """(Un)mark selected edges as a seam

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | None
    """

def mark_sharp(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    clear: bool | None = False,
    use_verts: bool | None = False,
):
    """(Un)mark selected edges as sharp

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param clear: Clear
    :type clear: bool | None
    :param use_verts: Vertices, Consider vertices instead of edges to select which edges to (un)tag as sharp
    :type use_verts: bool | None
    """

def merge(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["FIRST", "LAST", "CENTER", "CURSOR", "COLLAPSE"]
    | None = "CENTER",
    uvs: bool | None = False,
):
    """Merge selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type, Merge method to use
    :type type: typing.Literal['FIRST','LAST','CENTER','CURSOR','COLLAPSE'] | None
    :param uvs: UVs, Move UVs according to merge
    :type uvs: bool | None
    """

def navmesh_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove navmesh data from this mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def navmesh_face_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add a new index and assign it to selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def navmesh_face_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the index from the active face

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def navmesh_make(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create navigation mesh for selected objects

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def navmesh_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Assign a new index to every face

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def noise(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.1,
):
    """Use vertex coordinate as texture coordinate

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor
    :type factor: float | None
    """

def normals_make_consistent(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    inside: bool | None = False,
):
    """Make face and vertex normals point either outside or inside the mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param inside: Inside
    :type inside: bool | None
    """

def offset_edge_loops(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_cap_endpoint: bool | None = False,
):
    """Create offset edge loop from the current selection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_cap_endpoint: Cap Endpoint, Extend loop around end-points
    :type use_cap_endpoint: bool | None
    """

def offset_edge_loops_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_offset_edge_loops: offset_edge_loops | None = None,
    TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None = None,
):
    """Offset edge loop slide

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_offset_edge_loops: Offset Edge Loop, Create offset edge loop from the current selection
    :type MESH_OT_offset_edge_loops: offset_edge_loops | None
    :param TRANSFORM_OT_edge_slide: Edge Slide, Slide an edge loop along a mesh
    :type TRANSFORM_OT_edge_slide: bpy.ops.transform.edge_slide | None
    """

def poke(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    offset: float | None = 0.0,
    use_relative_offset: bool | None = False,
    center_mode: typing.Literal["MEDIAN_WEIGHTED", "MEDIAN", "BOUNDS"]
    | None = "MEDIAN_WEIGHTED",
):
    """Split a face into a fan

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param offset: Poke Offset, Poke Offset
        :type offset: float | None
        :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
        :type use_relative_offset: bool | None
        :param center_mode: Poke Center, Poke Face Center Calculation

    MEDIAN_WEIGHTED Weighted Median, Weighted median face center.

    MEDIAN Median, Median face center.

    BOUNDS Bounds, Face bounds center.
        :type center_mode: typing.Literal['MEDIAN_WEIGHTED','MEDIAN','BOUNDS'] | None
    """

def primitive_circle_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    vertices: int | None = 32,
    radius: float | None = 1.0,
    fill_type: typing.Literal["NOTHING", "NGON", "TRIFAN"] | None = "NOTHING",
    calc_uvs: bool | None = False,
    view_align: bool | None = False,
    enter_editmode: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
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
    ),
):
    """Construct a circle mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param vertices: Vertices
        :type vertices: int | None
        :param radius: Radius
        :type radius: float | None
        :param fill_type: Fill Type

    NOTHING Nothing, Don't fill at all.

    NGON Ngon, Use ngons.

    TRIFAN Triangle Fan, Use triangle fans.
        :type fill_type: typing.Literal['NOTHING','NGON','TRIFAN'] | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param view_align: Align to View, Align the new object to the view
        :type view_align: bool | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Iterable[float] | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Iterable[float] | None
        :param layers: Layer
        :type layers: collections.abc.Iterable[bool] | None
    """

def primitive_cone_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    vertices: int | None = 32,
    radius1: float | None = 1.0,
    radius2: float | None = 0.0,
    depth: float | None = 2.0,
    end_fill_type: typing.Literal["NOTHING", "NGON", "TRIFAN"] | None = "NGON",
    calc_uvs: bool | None = False,
    view_align: bool | None = False,
    enter_editmode: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
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
    ),
):
    """Construct a conic mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param vertices: Vertices
        :type vertices: int | None
        :param radius1: Radius 1
        :type radius1: float | None
        :param radius2: Radius 2
        :type radius2: float | None
        :param depth: Depth
        :type depth: float | None
        :param end_fill_type: Base Fill Type

    NOTHING Nothing, Don't fill at all.

    NGON Ngon, Use ngons.

    TRIFAN Triangle Fan, Use triangle fans.
        :type end_fill_type: typing.Literal['NOTHING','NGON','TRIFAN'] | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param view_align: Align to View, Align the new object to the view
        :type view_align: bool | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Iterable[float] | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Iterable[float] | None
        :param layers: Layer
        :type layers: collections.abc.Iterable[bool] | None
    """

def primitive_cube_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    calc_uvs: bool | None = False,
    view_align: bool | None = False,
    enter_editmode: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
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
    ),
):
    """Construct a cube mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: float | None
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | None
    :param location: Location, Location for the newly added object
    :type location: collections.abc.Iterable[float] | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: collections.abc.Iterable[float] | None
    :param layers: Layer
    :type layers: collections.abc.Iterable[bool] | None
    """

def primitive_cylinder_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    vertices: int | None = 32,
    radius: float | None = 1.0,
    depth: float | None = 2.0,
    end_fill_type: typing.Literal["NOTHING", "NGON", "TRIFAN"] | None = "NGON",
    calc_uvs: bool | None = False,
    view_align: bool | None = False,
    enter_editmode: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
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
    ),
):
    """Construct a cylinder mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param vertices: Vertices
        :type vertices: int | None
        :param radius: Radius
        :type radius: float | None
        :param depth: Depth
        :type depth: float | None
        :param end_fill_type: Cap Fill Type

    NOTHING Nothing, Don't fill at all.

    NGON Ngon, Use ngons.

    TRIFAN Triangle Fan, Use triangle fans.
        :type end_fill_type: typing.Literal['NOTHING','NGON','TRIFAN'] | None
        :param calc_uvs: Generate UVs, Generate a default UV map
        :type calc_uvs: bool | None
        :param view_align: Align to View, Align the new object to the view
        :type view_align: bool | None
        :param enter_editmode: Enter Editmode, Enter editmode when adding this object
        :type enter_editmode: bool | None
        :param location: Location, Location for the newly added object
        :type location: collections.abc.Iterable[float] | None
        :param rotation: Rotation, Rotation for the newly added object
        :type rotation: collections.abc.Iterable[float] | None
        :param layers: Layer
        :type layers: collections.abc.Iterable[bool] | None
    """

def primitive_grid_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    x_subdivisions: int | None = 10,
    y_subdivisions: int | None = 10,
    radius: float | None = 1.0,
    calc_uvs: bool | None = False,
    view_align: bool | None = False,
    enter_editmode: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
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
    ),
):
    """Construct a grid mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param x_subdivisions: X Subdivisions
    :type x_subdivisions: int | None
    :param y_subdivisions: Y Subdivisions
    :type y_subdivisions: int | None
    :param radius: Radius
    :type radius: float | None
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | None
    :param location: Location, Location for the newly added object
    :type location: collections.abc.Iterable[float] | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: collections.abc.Iterable[float] | None
    :param layers: Layer
    :type layers: collections.abc.Iterable[bool] | None
    """

def primitive_ico_sphere_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    subdivisions: int | None = 2,
    size: float | None = 1.0,
    calc_uvs: bool | None = False,
    view_align: bool | None = False,
    enter_editmode: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
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
    ),
):
    """Construct an Icosphere mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param subdivisions: Subdivisions
    :type subdivisions: int | None
    :param size: Size
    :type size: float | None
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | None
    :param location: Location, Location for the newly added object
    :type location: collections.abc.Iterable[float] | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: collections.abc.Iterable[float] | None
    :param layers: Layer
    :type layers: collections.abc.Iterable[bool] | None
    """

def primitive_monkey_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    calc_uvs: bool | None = False,
    view_align: bool | None = False,
    enter_editmode: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
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
    ),
):
    """Construct a Suzanne mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: float | None
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | None
    :param location: Location, Location for the newly added object
    :type location: collections.abc.Iterable[float] | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: collections.abc.Iterable[float] | None
    :param layers: Layer
    :type layers: collections.abc.Iterable[bool] | None
    """

def primitive_plane_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
    calc_uvs: bool | None = False,
    view_align: bool | None = False,
    enter_editmode: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
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
    ),
):
    """Construct a filled planar mesh with 4 vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: float | None
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | None
    :param location: Location, Location for the newly added object
    :type location: collections.abc.Iterable[float] | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: collections.abc.Iterable[float] | None
    :param layers: Layer
    :type layers: collections.abc.Iterable[bool] | None
    """

def primitive_torus_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    view_align: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
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
    ),
    major_segments: int | None = 48,
    minor_segments: int | None = 12,
    mode: typing.Literal["MAJOR_MINOR", "EXT_INT"] | None = "MAJOR_MINOR",
    major_radius: float | None = 1.0,
    minor_radius: float | None = 0.25,
    abso_major_rad: float | None = 1.25,
    abso_minor_rad: float | None = 0.75,
    generate_uvs: bool | None = False,
):
    """Add a torus mesh

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param view_align: Align to View
        :type view_align: bool | None
        :param location: Location
        :type location: collections.abc.Iterable[float] | None
        :param rotation: Rotation
        :type rotation: collections.abc.Iterable[float] | None
        :param layers: Layers
        :type layers: collections.abc.Iterable[bool] | None
        :param major_segments: Major Segments, Number of segments for the main ring of the torus
        :type major_segments: int | None
        :param minor_segments: Minor Segments, Number of segments for the minor ring of the torus
        :type minor_segments: int | None
        :param mode: Torus Dimensions

    MAJOR_MINOR Major/Minor, Use the major/minor radii for torus dimensions.

    EXT_INT Exterior/Interior, Use the exterior/interior radii for torus dimensions.
        :type mode: typing.Literal['MAJOR_MINOR','EXT_INT'] | None
        :param major_radius: Major Radius, Radius from the origin to the center of the cross sections
        :type major_radius: float | None
        :param minor_radius: Minor Radius, Radius of the torus' cross section
        :type minor_radius: float | None
        :param abso_major_rad: Exterior Radius, Total Exterior Radius of the torus
        :type abso_major_rad: float | None
        :param abso_minor_rad: Interior Radius, Total Interior Radius of the torus
        :type abso_minor_rad: float | None
        :param generate_uvs: Generate UVs, Generate a default UV map
        :type generate_uvs: bool | None
    """

def primitive_uv_sphere_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    segments: int | None = 32,
    ring_count: int | None = 16,
    size: float | None = 1.0,
    calc_uvs: bool | None = False,
    view_align: bool | None = False,
    enter_editmode: bool | None = False,
    location: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    rotation: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
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
    ),
):
    """Construct a UV sphere mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param segments: Segments
    :type segments: int | None
    :param ring_count: Rings
    :type ring_count: int | None
    :param size: Size
    :type size: float | None
    :param calc_uvs: Generate UVs, Generate a default UV map
    :type calc_uvs: bool | None
    :param view_align: Align to View, Align the new object to the view
    :type view_align: bool | None
    :param enter_editmode: Enter Editmode, Enter editmode when adding this object
    :type enter_editmode: bool | None
    :param location: Location, Location for the newly added object
    :type location: collections.abc.Iterable[float] | None
    :param rotation: Rotation, Rotation for the newly added object
    :type rotation: collections.abc.Iterable[float] | None
    :param layers: Layer
    :type layers: collections.abc.Iterable[bool] | None
    """

def quads_convert_to_tris(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    quad_method: typing.Literal[
        "BEAUTY", "FIXED", "FIXED_ALTERNATE", "SHORTEST_DIAGONAL"
    ]
    | None = "BEAUTY",
    ngon_method: typing.Literal["BEAUTY", "CLIP"] | None = "BEAUTY",
):
    """Triangulate selected faces

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param quad_method: Quad Method, Method for splitting the quads into triangles

    BEAUTY Beauty , Split the quads in nice triangles, slower method.

    FIXED Fixed, Split the quads on the first and third vertices.

    FIXED_ALTERNATE Fixed Alternate, Split the quads on the 2nd and 4th vertices.

    SHORTEST_DIAGONAL Shortest Diagonal, Split the quads based on the distance between the vertices.
        :type quad_method: typing.Literal['BEAUTY','FIXED','FIXED_ALTERNATE','SHORTEST_DIAGONAL'] | None
        :param ngon_method: Polygon Method, Method for splitting the polygons into triangles

    BEAUTY Beauty, Arrange the new triangles evenly (slow).

    CLIP Clip, Split the polygons with an ear clipping algorithm.
        :type ngon_method: typing.Literal['BEAUTY','CLIP'] | None
    """

def region_to_loop(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select boundary edges around the selected faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def remove_doubles(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    threshold: float | None = 0.0001,
    use_unselected: bool | None = False,
):
    """Remove duplicate vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Merge Distance, Minimum distance between elements to merge
    :type threshold: float | None
    :param use_unselected: Unselected, Merge selected to other unselected vertices
    :type use_unselected: bool | None
    """

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
):
    """Reveal all hidden vertices, edges and faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    """

def rip(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
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
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
    use_fill: bool | None = False,
):
    """Disconnect vertex or edges from connected geometry

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
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
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
        :param use_fill: Fill, Fill the ripped region
        :type use_fill: bool | None
    """

def rip_edge(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
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
    release_confirm: bool | None = False,
    use_accurate: bool | None = False,
):
    """Extend vertices along the edge closest to the cursor

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
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
        :param release_confirm: Confirm on Release, Always confirm operation when releasing button
        :type release_confirm: bool | None
        :param use_accurate: Accurate, Use accurate transformation
        :type use_accurate: bool | None
    """

def rip_edge_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_rip_edge: rip_edge | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Extend vertices and move the result

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_rip_edge: Extend Vertices, Extend vertices along the edge closest to the cursor
    :type MESH_OT_rip_edge: rip_edge | None
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def rip_move(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MESH_OT_rip: rip | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Rip polygons and move the result

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param MESH_OT_rip: Rip, Disconnect vertex or edges from connected geometry
    :type MESH_OT_rip: rip | None
    :param TRANSFORM_OT_translate: Translate, Translate (move) selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def screw(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    steps: int | None = 9,
    turns: int | None = 1,
    center: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    axis: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
):
    """Extrude selected vertices in screw-shaped rotation around the cursor in indicated viewport

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param steps: Steps, Steps
    :type steps: int | None
    :param turns: Turns, Turns
    :type turns: int | None
    :param center: Center, Center in global view space
    :type center: collections.abc.Iterable[float] | None
    :param axis: Axis, Axis in global view space
    :type axis: collections.abc.Iterable[float] | None
    """

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """(De)select all vertices, edges or faces

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

def select_axis(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["POSITIVE", "NEGATIVE", "ALIGNED"] | None = "POSITIVE",
    axis: typing.Literal["X_AXIS", "Y_AXIS", "Z_AXIS"] | None = "X_AXIS",
    threshold: float | None = 0.0001,
):
    """Select all data in the mesh on a single axis

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Axis Mode, Axis side to use when selecting
    :type mode: typing.Literal['POSITIVE','NEGATIVE','ALIGNED'] | None
    :param axis: Axis, Select the axis to compare each vertex on
    :type axis: typing.Literal['X_AXIS','Y_AXIS','Z_AXIS'] | None
    :param threshold: Threshold
    :type threshold: float | None
    """

def select_face_by_sides(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number: int | None = 4,
    type: typing.Literal["LESS", "EQUAL", "GREATER", "NOTEQUAL"] | None = "EQUAL",
    extend: bool | None = True,
):
    """Select vertices or faces by the number of polygon sides

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param number: Number of Vertices
    :type number: int | None
    :param type: Type, Type of comparison to make
    :type type: typing.Literal['LESS','EQUAL','GREATER','NOTEQUAL'] | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_interior_faces(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select faces where all edges have more than 2 face users

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_step: bool | None = True,
):
    """Deselect vertices, edges or faces at the boundary of each selection region

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Step, Connected faces (instead of edges)
    :type use_face_step: bool | None
    """

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    delimit: set[typing.Literal["NORMAL", "MATERIAL", "SEAM", "SHARP", "UV"]] | None = {
        "SEAM"
    },
):
    """Select all vertices connected to the current selection

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param delimit: Delimit, Delimit selected region

    NORMAL Normal, Delimit by face directions.

    MATERIAL Material, Delimit by face material.

    SEAM Seam, Delimit by edge seams.

    SHARP Sharp, Delimit by sharp edges.

    UV UVs, Delimit by UV coordinates.
        :type delimit: set[typing.Literal['NORMAL','MATERIAL','SEAM','SHARP','UV']] | None
    """

def select_linked_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deselect: bool | None = False,
    delimit: set[typing.Literal["NORMAL", "MATERIAL", "SEAM", "SHARP", "UV"]] | None = {
        "SEAM"
    },
    index: int | None = -1,
):
    """(De)select all vertices linked to the edge under the mouse cursor

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param deselect: Deselect
        :type deselect: bool | None
        :param delimit: Delimit, Delimit selected region

    NORMAL Normal, Delimit by face directions.

    MATERIAL Material, Delimit by face material.

    SEAM Seam, Delimit by edge seams.

    SHARP Sharp, Delimit by sharp edges.

    UV UVs, Delimit by UV coordinates.
        :type delimit: set[typing.Literal['NORMAL','MATERIAL','SEAM','SHARP','UV']] | None
        :type index: int | None
    """

def select_loose(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
):
    """Select loose geometry based on the selection mode

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: set[typing.Literal["X", "Y", "Z"]] | None = {"X"},
    extend: bool | None = False,
):
    """Select mesh items at mirrored locations

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param axis: Axis
    :type axis: set[typing.Literal['X','Y','Z']] | None
    :param extend: Extend, Extend the existing selection
    :type extend: bool | None
    """

def select_mode(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_extend: bool | None = False,
    use_expand: bool | None = False,
    type: typing.Literal["VERT", "EDGE", "FACE"] | None = "VERT",
    action: typing.Literal["DISABLE", "ENABLE", "TOGGLE"] | None = "TOGGLE",
):
    """Change selection mode

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param use_extend: Extend
        :type use_extend: bool | None
        :param use_expand: Expand
        :type use_expand: bool | None
        :param type: Type
        :type type: typing.Literal['VERT','EDGE','FACE'] | None
        :param action: Action, Selection action to execute

    DISABLE Disable, Disable selected markers.

    ENABLE Enable, Enable selected markers.

    TOGGLE Toggle, Toggle disabled flag for selected markers.
        :type action: typing.Literal['DISABLE','ENABLE','TOGGLE'] | None
    """

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_step: bool | None = True,
):
    """Select more vertices, edges or faces connected to initial selection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Step, Connected faces (instead of edges)
    :type use_face_step: bool | None
    """

def select_next_item(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select the next element (using selection order)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_non_manifold(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = True,
    use_wire: bool | None = True,
    use_boundary: bool | None = True,
    use_multi_face: bool | None = True,
    use_non_contiguous: bool | None = True,
    use_verts: bool | None = True,
):
    """Select all non-manifold vertices or edges

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    :param use_wire: Wire, Wire edges
    :type use_wire: bool | None
    :param use_boundary: Boundaries, Boundary edges
    :type use_boundary: bool | None
    :param use_multi_face: Multiple Faces, Edges shared by 3+ faces
    :type use_multi_face: bool | None
    :param use_non_contiguous: Non Contiguous, Edges between faces pointing in alternate directions
    :type use_non_contiguous: bool | None
    :param use_verts: Vertices, Vertices connecting multiple face regions
    :type use_verts: bool | None
    """

def select_nth(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    nth: int | None = 2,
    skip: int | None = 1,
    offset: int | None = 0,
):
    """Deselect every Nth element starting from the active vertex, edge or face

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param nth: Nth Element, Skip every Nth element
    :type nth: int | None
    :param skip: Skip, Number of elements to skip at once
    :type skip: int | None
    :param offset: Offset, Offset from the starting point
    :type offset: int | None
    """

def select_prev_item(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select the previous element (using selection order)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_random(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    percent: float | None = 50.0,
    seed: int | None = 0,
    action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
):
    """Randomly select vertices

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param percent: Percent, Percentage of objects to select randomly
        :type percent: float | None
        :param seed: Random Seed, Seed for the random number generator
        :type seed: int | None
        :param action: Action, Selection action to execute

    SELECT Select, Select all elements.

    DESELECT Deselect, Deselect all elements.
        :type action: typing.Literal['SELECT','DESELECT'] | None
    """

def select_similar(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "NORMAL",
        "FACE",
        "VGROUP",
        "EDGE",
        "LENGTH",
        "DIR",
        "FACE",
        "FACE_ANGLE",
        "CREASE",
        "BEVEL",
        "SEAM",
        "SHARP",
        "FREESTYLE_EDGE",
        "MATERIAL",
        "IMAGE",
        "AREA",
        "SIDES",
        "PERIMETER",
        "NORMAL",
        "COPLANAR",
        "SMOOTH",
        "FREESTYLE_FACE",
    ]
    | None = "NORMAL",
    compare: typing.Literal["EQUAL", "GREATER", "LESS"] | None = "EQUAL",
    threshold: float | None = 0.0,
):
    """Select similar vertices, edges or faces by property types

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['NORMAL','FACE','VGROUP','EDGE','LENGTH','DIR','FACE','FACE_ANGLE','CREASE','BEVEL','SEAM','SHARP','FREESTYLE_EDGE','MATERIAL','IMAGE','AREA','SIDES','PERIMETER','NORMAL','COPLANAR','SMOOTH','FREESTYLE_FACE'] | None
    :param compare: Compare
    :type compare: typing.Literal['EQUAL','GREATER','LESS'] | None
    :param threshold: Threshold
    :type threshold: float | None
    """

def select_similar_region(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select similar face regions to the current selection

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_ungrouped(
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

def separate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SELECTED", "MATERIAL", "LOOSE"] | None = "SELECTED",
):
    """Separate selected geometry into a new mesh

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: typing.Literal['SELECTED','MATERIAL','LOOSE'] | None
    """

def set_normals_from_faces(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set the custom vertex normals from the selected faces ones

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def shape_propagate_to_all(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply selected vertex locations to all other shape keys

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def shortest_path_pick(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_step: bool | None = False,
    use_topology_distance: bool | None = False,
    use_fill: bool | None = False,
    nth: int | None = 1,
    skip: int | None = 1,
    offset: int | None = 0,
    index: int | None = -1,
):
    """Select shortest path between two selections

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool | None
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool | None
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool | None
    :param nth: Nth Element, Skip every Nth element
    :type nth: int | None
    :param skip: Skip, Number of elements to skip at once
    :type skip: int | None
    :param offset: Offset, Offset from the starting point
    :type offset: int | None
    :type index: int | None
    """

def shortest_path_select(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_face_step: bool | None = False,
    use_topology_distance: bool | None = False,
    use_fill: bool | None = False,
    nth: int | None = 1,
    skip: int | None = 1,
    offset: int | None = 0,
):
    """Selected shortest path between two vertices/edges/faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_face_step: Face Stepping, Traverse connected faces (includes diagonals and edge-rings)
    :type use_face_step: bool | None
    :param use_topology_distance: Topology Distance, Find the minimum number of steps, ignoring spatial distance
    :type use_topology_distance: bool | None
    :param use_fill: Fill Region, Select all paths between the source/destination elements
    :type use_fill: bool | None
    :param nth: Nth Element, Skip every Nth element
    :type nth: int | None
    :param skip: Skip, Number of elements to skip at once
    :type skip: int | None
    :param offset: Offset, Offset from the starting point
    :type offset: int | None
    """

def solidify(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    thickness: float | None = 0.01,
):
    """Create a solid skin by extruding, compensating for sharp angles

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param thickness: Thickness
    :type thickness: float | None
    """

def sort_elements(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "VIEW_ZAXIS",
        "VIEW_XAXIS",
        "CURSOR_DISTANCE",
        "MATERIAL",
        "SELECTED",
        "RANDOMIZE",
        "REVERSE",
    ]
    | None = "VIEW_ZAXIS",
    elements: set[typing.Literal["VERT", "EDGE", "FACE"]] | None = {"VERT"},
    reverse: bool | None = False,
    seed: int | None = 0,
):
    """The order of selected vertices/edges/faces is modified, based on a given method

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type, Type of re-ordering operation to apply

    VIEW_ZAXIS View Z Axis, Sort selected elements from farthest to nearest one in current view.

    VIEW_XAXIS View X Axis, Sort selected elements from left to right one in current view.

    CURSOR_DISTANCE Cursor Distance, Sort selected elements from nearest to farthest from 3D cursor.

    MATERIAL Material, Sort selected elements from smallest to greatest material index (faces only!).

    SELECTED Selected, Move all selected elements in first places, preserving their relative order (WARNING: this will affect unselected elements' indices as well!).

    RANDOMIZE Randomize, Randomize order of selected elements.

    REVERSE Reverse, Reverse current order of selected elements.
        :type type: typing.Literal['VIEW_ZAXIS','VIEW_XAXIS','CURSOR_DISTANCE','MATERIAL','SELECTED','RANDOMIZE','REVERSE'] | None
        :param elements: Elements, Which elements to affect (vertices, edges and/or faces)
        :type elements: set[typing.Literal['VERT','EDGE','FACE']] | None
        :param reverse: Reverse, Reverse the sorting effect
        :type reverse: bool | None
        :param seed: Seed, Seed for random-based operations
        :type seed: int | None
    """

def spin(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    steps: int | None = 9,
    dupli: bool | None = False,
    angle: float | None = 1.5708,
    use_auto_merge: bool | None = True,
    use_normal_flip: bool | None = False,
    center: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    axis: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
):
    """Extrude selected vertices in a circle around the cursor in indicated viewport

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param steps: Steps, Steps
    :type steps: int | None
    :param dupli: Dupli, Make Duplicates
    :type dupli: bool | None
    :param angle: Angle, Rotation for each step
    :type angle: float | None
    :param use_auto_merge: Auto Merge, Merge first/last when the angle is a full revolution
    :type use_auto_merge: bool | None
    :param use_normal_flip: Flip Normals
    :type use_normal_flip: bool | None
    :param center: Center, Center in global view space
    :type center: collections.abc.Iterable[float] | None
    :param axis: Axis, Axis in global view space
    :type axis: collections.abc.Iterable[float] | None
    """

def split(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Split off selected geometry from connected unselected geometry

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def subdivide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 1,
    smoothness: float | None = 0.0,
    quadtri: bool | None = False,
    quadcorner: typing.Literal["INNERVERT", "PATH", "STRAIGHT_CUT", "FAN"]
    | None = "STRAIGHT_CUT",
    fractal: float | None = 0.0,
    fractal_along_normal: float | None = 0.0,
    seed: int | None = 0,
):
    """Subdivide selected edges

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param number_cuts: Number of Cuts
    :type number_cuts: int | None
    :param smoothness: Smoothness, Smoothness factor
    :type smoothness: float | None
    :param quadtri: Quad/Tri Mode, Tries to prevent ngons
    :type quadtri: bool | None
    :param quadcorner: Quad Corner Type, How to subdivide quad corners (anything other than Straight Cut will prevent ngons)
    :type quadcorner: typing.Literal['INNERVERT','PATH','STRAIGHT_CUT','FAN'] | None
    :param fractal: Fractal, Fractal randomness factor
    :type fractal: float | None
    :param fractal_along_normal: Along Normal, Apply fractal displacement along normal only
    :type fractal_along_normal: float | None
    :param seed: Random Seed, Seed for the random number generator
    :type seed: int | None
    """

def subdivide_edgering(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    number_cuts: int | None = 10,
    interpolation: typing.Literal["LINEAR", "PATH", "SURFACE"] | None = "PATH",
    smoothness: float | None = 1.0,
    profile_shape_factor: float | None = 0.0,
    profile_shape: typing.Literal[
        "SMOOTH", "SPHERE", "ROOT", "INVERSE_SQUARE", "SHARP", "LINEAR"
    ]
    | None = "SMOOTH",
):
    """Undocumented

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param number_cuts: Number of Cuts
        :type number_cuts: int | None
        :param interpolation: Interpolation, Interpolation method
        :type interpolation: typing.Literal['LINEAR','PATH','SURFACE'] | None
        :param smoothness: Smoothness, Smoothness factor
        :type smoothness: float | None
        :param profile_shape_factor: Profile Factor, How much intermediary new edges are shrunk/expanded
        :type profile_shape_factor: float | None
        :param profile_shape: Profile Shape, Shape of the profile

    SMOOTH Smooth, Smooth falloff.

    SPHERE Sphere, Spherical falloff.

    ROOT Root, Root falloff.

    INVERSE_SQUARE Inverse Square, Inverse Square falloff.

    SHARP Sharp, Sharp falloff.

    LINEAR Linear, Linear falloff.
        :type profile_shape: typing.Literal['SMOOTH','SPHERE','ROOT','INVERSE_SQUARE','SHARP','LINEAR'] | None
    """

def symmetrize(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal[
        "NEGATIVE_X",
        "POSITIVE_X",
        "NEGATIVE_Y",
        "POSITIVE_Y",
        "NEGATIVE_Z",
        "POSITIVE_Z",
    ]
    | None = "NEGATIVE_X",
    threshold: float | None = 0.0001,
):
    """Enforce symmetry (both form and topological) across an axis

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Which sides to copy from and to
    :type direction: typing.Literal['NEGATIVE_X','POSITIVE_X','NEGATIVE_Y','POSITIVE_Y','NEGATIVE_Z','POSITIVE_Z'] | None
    :param threshold: Threshold, Limit for snap middle vertices to the axis center
    :type threshold: float | None
    """

def symmetry_snap(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    direction: typing.Literal[
        "NEGATIVE_X",
        "POSITIVE_X",
        "NEGATIVE_Y",
        "POSITIVE_Y",
        "NEGATIVE_Z",
        "POSITIVE_Z",
    ]
    | None = "NEGATIVE_X",
    threshold: float | None = 0.05,
    factor: float | None = 0.5,
    use_center: bool | None = True,
):
    """Snap vertex pairs to their mirrored locations

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param direction: Direction, Which sides to copy from and to
    :type direction: typing.Literal['NEGATIVE_X','POSITIVE_X','NEGATIVE_Y','POSITIVE_Y','NEGATIVE_Z','POSITIVE_Z'] | None
    :param threshold: Threshold, Distance within which matching vertices are searched
    :type threshold: float | None
    :param factor: Factor, Mix factor of the locations of the vertices
    :type factor: float | None
    :param use_center: Center, Snap middle vertices to the axis center
    :type use_center: bool | None
    """

def tris_convert_to_quads(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    face_threshold: float | None = 0.698132,
    shape_threshold: float | None = 0.698132,
    uvs: bool | None = False,
    vcols: bool | None = False,
    seam: bool | None = False,
    sharp: bool | None = False,
    materials: bool | None = False,
):
    """Join triangles into quads

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param face_threshold: Max Face Angle, Face angle limit
    :type face_threshold: float | None
    :param shape_threshold: Max Shape Angle, Shape angle limit
    :type shape_threshold: float | None
    :param uvs: Compare UVs
    :type uvs: bool | None
    :param vcols: Compare VCols
    :type vcols: bool | None
    :param seam: Compare Seam
    :type seam: bool | None
    :param sharp: Compare Sharp
    :type sharp: bool | None
    :param materials: Compare Materials
    :type materials: bool | None
    """

def unsubdivide(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    iterations: int | None = 2,
):
    """UnSubdivide selected edges & faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param iterations: Iterations, Number of times to unsubdivide
    :type iterations: int | None
    """

def uv_texture_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add UV Map

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def uv_texture_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove UV Map

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def uvs_reverse(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Flip direction of UV coordinates inside faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def uvs_rotate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_ccw: bool | None = False,
):
    """Rotate UV coordinates inside faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_ccw: Counter Clockwise
    :type use_ccw: bool | None
    """

def vert_connect(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Connect selected vertices of faces, splitting the face

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vert_connect_concave(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Make all faces convex

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vert_connect_nonplanar(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    angle_limit: float | None = 0.0872665,
):
    """Split non-planar faces that exceed the angle threshold

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param angle_limit: Max Angle, Angle limit
    :type angle_limit: float | None
    """

def vert_connect_path(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Connect vertices by their selection order, creating edges, splitting faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertex_color_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add vertex color layer

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertex_color_remove(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove vertex color layer

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def vertices_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    factor: float | None = 0.5,
    repeat: int | None = 1,
    xaxis: bool | None = True,
    yaxis: bool | None = True,
    zaxis: bool | None = True,
):
    """Flatten angles of selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Smoothing, Smoothing factor
    :type factor: float | None
    :param repeat: Repeat, Number of times to smooth the mesh
    :type repeat: int | None
    :param xaxis: X-Axis, Smooth along the X axis
    :type xaxis: bool | None
    :param yaxis: Y-Axis, Smooth along the Y axis
    :type yaxis: bool | None
    :param zaxis: Z-Axis, Smooth along the Z axis
    :type zaxis: bool | None
    """

def vertices_smooth_laplacian(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    repeat: int | None = 1,
    lambda_factor: float | None = 5e-05,
    lambda_border: float | None = 5e-05,
    use_x: bool | None = True,
    use_y: bool | None = True,
    use_z: bool | None = True,
    preserve_volume: bool | None = True,
):
    """Laplacian smooth of selected vertices

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param repeat: Number of iterations to smooth the mesh
    :type repeat: int | None
    :param lambda_factor: Lambda factor
    :type lambda_factor: float | None
    :param lambda_border: Lambda factor in border
    :type lambda_border: float | None
    :param use_x: Smooth X Axis, Smooth object along X axis
    :type use_x: bool | None
    :param use_y: Smooth Y Axis, Smooth object along Y axis
    :type use_y: bool | None
    :param use_z: Smooth Z Axis, Smooth object along Z axis
    :type use_z: bool | None
    :param preserve_volume: Preserve Volume, Apply volume preservation after smooth
    :type preserve_volume: bool | None
    """

def wireframe(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    use_boundary: bool | None = True,
    use_even_offset: bool | None = True,
    use_relative_offset: bool | None = False,
    use_replace: bool | None = True,
    thickness: float | None = 0.01,
    offset: float | None = 0.01,
    use_crease: bool | None = False,
    crease_weight: float | None = 0.01,
):
    """Create a solid wire-frame from faces

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param use_boundary: Boundary, Inset face boundaries
    :type use_boundary: bool | None
    :param use_even_offset: Offset Even, Scale the offset to give more even thickness
    :type use_even_offset: bool | None
    :param use_relative_offset: Offset Relative, Scale the offset by surrounding geometry
    :type use_relative_offset: bool | None
    :param use_replace: Replace, Remove original faces
    :type use_replace: bool | None
    :param thickness: Thickness
    :type thickness: float | None
    :param offset: Offset
    :type offset: float | None
    :param use_crease: Crease, Crease hub edges for improved subsurf
    :type use_crease: bool | None
    :param crease_weight: Crease weight
    :type crease_weight: float | None
    """
