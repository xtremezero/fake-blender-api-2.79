import typing
import collections.abc
import typing_extensions
import bpy.types

def autodesk_3ds(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Z",
    filter_glob: str = "*.3ds",
    use_selection: bool | None = False,
):
    """Export to 3DS file format (.3ds)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param filepath: File Path, Filepath used for exporting the file
    :type filepath: str
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: bool | None
    :param axis_forward: Forward
    :type axis_forward: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
    :param axis_up: Up
    :type axis_up: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
    :param filter_glob: filter_glob
    :type filter_glob: str
    :param use_selection: Selection Only, Export selected objects only
    :type use_selection: bool | None
    """

def fbx(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "-Z",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    filter_glob: str = "*.fbx",
    ui_tab: typing.Literal["MAIN", "GEOMETRY", "ARMATURE", "ANIMATION"] | None = "MAIN",
    use_selection: bool | None = False,
    global_scale: float | None = 1.0,
    apply_unit_scale: bool | None = True,
    apply_scale_options: typing.Literal[
        "FBX_SCALE_NONE", "FBX_SCALE_UNITS", "FBX_SCALE_CUSTOM", "FBX_SCALE_ALL"
    ]
    | None = "FBX_SCALE_NONE",
    bake_space_transform: bool | None = False,
    object_types: set[
        typing.Literal["EMPTY", "CAMERA", "LAMP", "ARMATURE", "MESH", "OTHER"]
    ]
    | None = {"ARMATURE", "CAMERA", "EMPTY", "LAMP", "MESH", "OTHER"},
    use_mesh_modifiers: bool | None = True,
    use_mesh_modifiers_render: bool | None = True,
    mesh_smooth_type: typing.Literal["OFF", "FACE", "EDGE"] | None = "OFF",
    use_mesh_edges: bool | None = False,
    use_tspace: bool | None = False,
    use_custom_props: bool | None = False,
    add_leaf_bones: bool | None = True,
    primary_bone_axis: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    secondary_bone_axis: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "X",
    use_armature_deform_only: bool | None = False,
    armature_nodetype: typing.Literal["NULL", "ROOT", "LIMBNODE"] | None = "NULL",
    bake_anim: bool | None = True,
    bake_anim_use_all_bones: bool | None = True,
    bake_anim_use_nla_strips: bool | None = True,
    bake_anim_use_all_actions: bool | None = True,
    bake_anim_force_startend_keying: bool | None = True,
    bake_anim_step: float | None = 1.0,
    bake_anim_simplify_factor: float | None = 1.0,
    path_mode: typing.Literal["AUTO", "ABSOLUTE", "RELATIVE", "MATCH", "STRIP", "COPY"]
    | None = "AUTO",
    embed_textures: bool | None = False,
    batch_mode: typing.Literal["OFF", "SCENE", "GROUP"] | None = "OFF",
    use_batch_own_dir: bool | None = True,
    use_metadata: bool | None = True,
):
    """Write a FBX file

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for exporting the file
        :type filepath: str
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param axis_forward: Forward
        :type axis_forward: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param axis_up: Up
        :type axis_up: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param filter_glob: filter_glob
        :type filter_glob: str
        :param ui_tab: ui_tab, Export options categories

    MAIN Main, Main basic settings.

    GEOMETRY Geometries, Geometry-related settings.

    ARMATURE Armatures, Armature-related settings.

    ANIMATION Animation, Animation-related settings.
        :type ui_tab: typing.Literal['MAIN','GEOMETRY','ARMATURE','ANIMATION'] | None
        :param use_selection: Selected Objects, Export selected objects on visible layers
        :type use_selection: bool | None
        :param global_scale: Scale, Scale all data (Some importers do not support scaled armatures!)
        :type global_scale: float | None
        :param apply_unit_scale: Apply Unit, Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)
        :type apply_unit_scale: bool | None
        :param apply_scale_options: Apply Scalings, How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way)

    FBX_SCALE_NONE All Local, Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0.

    FBX_SCALE_UNITS FBX Units Scale, Apply custom scaling to each object transformation, and units scaling to FBX scale.

    FBX_SCALE_CUSTOM FBX Custom Scale, Apply custom scaling to FBX scale, and units scaling to each object transformation.

    FBX_SCALE_ALL FBX All, Apply custom scaling and units scaling to FBX scale.
        :type apply_scale_options: typing.Literal['FBX_SCALE_NONE','FBX_SCALE_UNITS','FBX_SCALE_CUSTOM','FBX_SCALE_ALL'] | None
        :param bake_space_transform: !EXPERIMENTAL! Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender's space (WARNING! experimental option, use at own risks, known broken with armatures/animations)
        :type bake_space_transform: bool | None
        :param object_types: Object Types, Which kind of object to export

    EMPTY Empty.

    CAMERA Camera.

    LAMP Lamp.

    ARMATURE Armature, WARNING: not supported in dupli/group instances.

    MESH Mesh.

    OTHER Other, Other geometry types, like curve, metaball, etc. (converted to meshes).
        :type object_types: set[typing.Literal['EMPTY','CAMERA','LAMP','ARMATURE','MESH','OTHER']] | None
        :param use_mesh_modifiers: Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys
        :type use_mesh_modifiers: bool | None
        :param use_mesh_modifiers_render: Use Modifiers Render Setting, Use render settings when applying modifiers to mesh objects
        :type use_mesh_modifiers_render: bool | None
        :param mesh_smooth_type: Smoothing, Export smoothing information (prefer 'Normals Only' option if your target importer understand split normals)

    OFF Normals Only, Export only normals instead of writing edge or face smoothing data.

    FACE Face, Write face smoothing.

    EDGE Edge, Write edge smoothing.
        :type mesh_smooth_type: typing.Literal['OFF','FACE','EDGE'] | None
        :param use_mesh_edges: Loose Edges, Export loose edges (as two-vertices polygons)
        :type use_mesh_edges: bool | None
        :param use_tspace: Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)
        :type use_tspace: bool | None
        :param use_custom_props: Custom Properties, Export custom properties
        :type use_custom_props: bool | None
        :param add_leaf_bones: Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)
        :type add_leaf_bones: bool | None
        :param primary_bone_axis: Primary Bone Axis
        :type primary_bone_axis: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param secondary_bone_axis: Secondary Bone Axis
        :type secondary_bone_axis: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param use_armature_deform_only: Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children)
        :type use_armature_deform_only: bool | None
        :param armature_nodetype: Armature FBXNode Type, FBX type of node (object) used to represent Blender's armatures (use Null one unless you experience issues with other app, other choices may no import back perfectly in Blender...)

    NULL Null, 'Null' FBX node, similar to Blender's Empty (default).

    ROOT Root, 'Root' FBX node, supposed to be the root of chains of bones....

    LIMBNODE LimbNode, 'LimbNode' FBX node, a regular joint between two bones....
        :type armature_nodetype: typing.Literal['NULL','ROOT','LIMBNODE'] | None
        :param bake_anim: Baked Animation, Export baked keyframe animation
        :type bake_anim: bool | None
        :param bake_anim_use_all_bones: Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)
        :type bake_anim_use_all_bones: bool | None
        :param bake_anim_use_nla_strips: NLA Strips, Export each non-muted NLA strip as a separated FBX's AnimStack, if any, instead of global scene animation
        :type bake_anim_use_nla_strips: bool | None
        :param bake_anim_use_all_actions: All Actions, Export each action as a separated FBX's AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)
        :type bake_anim_use_all_actions: bool | None
        :param bake_anim_force_startend_keying: Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels
        :type bake_anim_force_startend_keying: bool | None
        :param bake_anim_step: Sampling Rate, How often to evaluate animated values (in frames)
        :type bake_anim_step: float | None
        :param bake_anim_simplify_factor: Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified)
        :type bake_anim_simplify_factor: float | None
        :param path_mode: Path Mode, Method used to reference paths

    AUTO Auto, Use Relative paths with subdirectories only.

    ABSOLUTE Absolute, Always write absolute paths.

    RELATIVE Relative, Always write relative paths (where possible).

    MATCH Match, Match Absolute/Relative setting with input path.

    STRIP Strip Path, Filename only.

    COPY Copy, Copy the file to the destination path (or subdirectory).
        :type path_mode: typing.Literal['AUTO','ABSOLUTE','RELATIVE','MATCH','STRIP','COPY'] | None
        :param embed_textures: Embed Textures, Embed textures in FBX binary file (only for "Copy" path mode!)
        :type embed_textures: bool | None
        :param batch_mode: Batch Mode

    OFF Off, Active scene to file.

    SCENE Scene, Each scene as a file.

    GROUP Group, Each group as a file.
        :type batch_mode: typing.Literal['OFF','SCENE','GROUP'] | None
        :param use_batch_own_dir: Batch Own Dir, Create a dir for each exported file
        :type use_batch_own_dir: bool | None
        :param use_metadata: Use Metadata
        :type use_metadata: bool | None
    """

def obj(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "-Z",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    filter_glob: str = "*.obj;*.mtl",
    use_selection: bool | None = False,
    use_animation: bool | None = False,
    use_mesh_modifiers: bool | None = True,
    use_mesh_modifiers_render: bool | None = False,
    use_edges: bool | None = True,
    use_smooth_groups: bool | None = False,
    use_smooth_groups_bitflags: bool | None = False,
    use_normals: bool | None = True,
    use_uvs: bool | None = True,
    use_materials: bool | None = True,
    use_triangles: bool | None = False,
    use_nurbs: bool | None = False,
    use_vertex_groups: bool | None = False,
    use_blen_objects: bool | None = True,
    group_by_object: bool | None = False,
    group_by_material: bool | None = False,
    keep_vertex_order: bool | None = False,
    global_scale: float | None = 1.0,
    path_mode: typing.Literal["AUTO", "ABSOLUTE", "RELATIVE", "MATCH", "STRIP", "COPY"]
    | None = "AUTO",
):
    """Save a Wavefront OBJ File

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for exporting the file
        :type filepath: str
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param axis_forward: Forward
        :type axis_forward: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param axis_up: Up
        :type axis_up: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param filter_glob: filter_glob
        :type filter_glob: str
        :param use_selection: Selection Only, Export selected objects only
        :type use_selection: bool | None
        :param use_animation: Animation, Write out an OBJ for each frame
        :type use_animation: bool | None
        :param use_mesh_modifiers: Apply Modifiers, Apply modifiers
        :type use_mesh_modifiers: bool | None
        :param use_mesh_modifiers_render: Use Modifiers Render Settings, Use render settings when applying modifiers to mesh objects
        :type use_mesh_modifiers_render: bool | None
        :param use_edges: Include Edges
        :type use_edges: bool | None
        :param use_smooth_groups: Smooth Groups, Write sharp edges as smooth groups
        :type use_smooth_groups: bool | None
        :param use_smooth_groups_bitflags: Bitflag Smooth Groups, Same as 'Smooth Groups', but generate smooth groups IDs as bitflags (produces at most 32 different smooth groups, usually much less)
        :type use_smooth_groups_bitflags: bool | None
        :param use_normals: Write Normals, Export one normal per vertex and per face, to represent flat faces and sharp edges
        :type use_normals: bool | None
        :param use_uvs: Include UVs, Write out the active UV coordinates
        :type use_uvs: bool | None
        :param use_materials: Write Materials, Write out the MTL file
        :type use_materials: bool | None
        :param use_triangles: Triangulate Faces, Convert all faces to triangles
        :type use_triangles: bool | None
        :param use_nurbs: Write Nurbs, Write nurbs curves as OBJ nurbs rather than converting to geometry
        :type use_nurbs: bool | None
        :param use_vertex_groups: Polygroups
        :type use_vertex_groups: bool | None
        :param use_blen_objects: Objects as OBJ Objects
        :type use_blen_objects: bool | None
        :param group_by_object: Objects as OBJ Groups
        :type group_by_object: bool | None
        :param group_by_material: Material Groups
        :type group_by_material: bool | None
        :param keep_vertex_order: Keep Vertex Order
        :type keep_vertex_order: bool | None
        :param global_scale: Scale
        :type global_scale: float | None
        :param path_mode: Path Mode, Method used to reference paths

    AUTO Auto, Use Relative paths with subdirectories only.

    ABSOLUTE Absolute, Always write absolute paths.

    RELATIVE Relative, Always write relative paths (where possible).

    MATCH Match, Match Absolute/Relative setting with input path.

    STRIP Strip Path, Filename only.

    COPY Copy, Copy the file to the destination path (or subdirectory).
        :type path_mode: typing.Literal['AUTO','ABSOLUTE','RELATIVE','MATCH','STRIP','COPY'] | None
    """

def x3d(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    filepath: str = "",
    check_existing: bool | None = True,
    axis_forward: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Z",
    axis_up: typing.Literal["X", "Y", "Z", "-X", "-Y", "-Z"] | None = "Y",
    filter_glob: str = "*.x3d",
    use_selection: bool | None = False,
    use_mesh_modifiers: bool | None = True,
    use_triangulate: bool | None = False,
    use_normals: bool | None = False,
    use_compress: bool | None = False,
    use_hierarchy: bool | None = True,
    name_decorations: bool | None = True,
    use_h3d: bool | None = False,
    global_scale: float | None = 1.0,
    path_mode: typing.Literal["AUTO", "ABSOLUTE", "RELATIVE", "MATCH", "STRIP", "COPY"]
    | None = "AUTO",
):
    """Export selection to Extensible 3D file (.x3d)

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Filepath used for exporting the file
        :type filepath: str
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param axis_forward: Forward
        :type axis_forward: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param axis_up: Up
        :type axis_up: typing.Literal['X','Y','Z','-X','-Y','-Z'] | None
        :param filter_glob: filter_glob
        :type filter_glob: str
        :param use_selection: Selection Only, Export selected objects only
        :type use_selection: bool | None
        :param use_mesh_modifiers: Apply Modifiers, Use transformed mesh data from each object
        :type use_mesh_modifiers: bool | None
        :param use_triangulate: Triangulate, Write quads into 'IndexedTriangleSet'
        :type use_triangulate: bool | None
        :param use_normals: Normals, Write normals with geometry
        :type use_normals: bool | None
        :param use_compress: Compress, Compress the exported file
        :type use_compress: bool | None
        :param use_hierarchy: Hierarchy, Export parent child relationships
        :type use_hierarchy: bool | None
        :param name_decorations: Name decorations, Add prefixes to the names of exported nodes to indicate their type
        :type name_decorations: bool | None
        :param use_h3d: H3D Extensions, Export shaders for H3D
        :type use_h3d: bool | None
        :param global_scale: Scale
        :type global_scale: float | None
        :param path_mode: Path Mode, Method used to reference paths

    AUTO Auto, Use Relative paths with subdirectories only.

    ABSOLUTE Absolute, Always write absolute paths.

    RELATIVE Relative, Always write relative paths (where possible).

    MATCH Match, Match Absolute/Relative setting with input path.

    STRIP Strip Path, Filename only.

    COPY Copy, Copy the file to the destination path (or subdirectory).
        :type path_mode: typing.Literal['AUTO','ABSOLUTE','RELATIVE','MATCH','STRIP','COPY'] | None
    """
