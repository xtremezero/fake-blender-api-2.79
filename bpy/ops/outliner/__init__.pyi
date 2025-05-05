import typing
import collections.abc
import typing_extensions
import bpy.types

def action_set(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: str | None = "",
):
    """Change the active action used

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param action: Action
    :type action: str | None
    """

def animdata_operation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "CLEAR_ANIMDATA", "SET_ACT", "CLEAR_ACT", "REFRESH_DRIVERS", "CLEAR_DRIVERS"
    ]
    | None = "CLEAR_ANIMDATA",
):
    """Undocumented

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Animation Operation

    CLEAR_ANIMDATA Clear Animation Data, Remove this animation data container.

    SET_ACT Set Action.

    CLEAR_ACT Unlink Action.

    REFRESH_DRIVERS Refresh Drivers.

    CLEAR_DRIVERS Clear Drivers.
        :type type: typing.Literal['CLEAR_ANIMDATA','SET_ACT','CLEAR_ACT','REFRESH_DRIVERS','CLEAR_DRIVERS'] | None
    """

def constraint_operation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["ENABLE", "DISABLE", "DELETE"] | None = "ENABLE",
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Constraint Operation
    :type type: typing.Literal['ENABLE','DISABLE','DELETE'] | None
    """

def data_operation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["SELECT", "DESELECT", "HIDE", "UNHIDE", "SELECT_LINKED"]
    | None = "SELECT",
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Data Operation
    :type type: typing.Literal['SELECT','DESELECT','HIDE','UNHIDE','SELECT_LINKED'] | None
    """

def drivers_add_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add drivers to selected items

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def drivers_delete_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete drivers assigned to selected items

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def expanded_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Expand/Collapse all items

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def group_link(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    object: str = "Object",
):
    """Link Object to Group in Outliner

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param object: Object, Target Object
    :type object: str
    """

def group_operation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "UNLINK",
        "LOCAL",
        "LINK",
        "DELETE",
        "REMAP",
        "INSTANCE",
        "TOGVIS",
        "TOGSEL",
        "TOGREN",
        "RENAME",
    ]
    | None = "UNLINK",
):
    """Undocumented

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Group Operation

    UNLINK Unlink Group.

    LOCAL Make Local Group.

    LINK Link Group Objects to Scene.

    DELETE Delete Group.

    REMAP Remap Users, Make all users of selected data-blocks to use instead current (clicked) one.

    INSTANCE Instance Groups in Scene.

    TOGVIS Toggle Visible Group.

    TOGSEL Toggle Selectable.

    TOGREN Toggle Renderable.

    RENAME Rename.
        :type type: typing.Literal['UNLINK','LOCAL','LINK','DELETE','REMAP','INSTANCE','TOGVIS','TOGSEL','TOGREN','RENAME'] | None
    """

def id_delete(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete the ID under cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def id_operation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "UNLINK",
        "LOCAL",
        "SINGLE",
        "DELETE",
        "REMAP",
        "ADD_FAKE",
        "CLEAR_FAKE",
        "RENAME",
        "SELECT_LINKED",
    ]
    | None = "UNLINK",
):
    """Undocumented

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: ID data Operation

    UNLINK Unlink.

    LOCAL Make Local.

    SINGLE Make Single User.

    DELETE Delete, WARNING: no undo.

    REMAP Remap Users, Make all users of selected data-blocks to use instead current (clicked) one.

    ADD_FAKE Add Fake User, Ensure data-block gets saved even if it isn't in use (e.g. for motion and material libraries).

    CLEAR_FAKE Clear Fake User.

    RENAME Rename.

    SELECT_LINKED Select Linked.
        :type type: typing.Literal['UNLINK','LOCAL','SINGLE','DELETE','REMAP','ADD_FAKE','CLEAR_FAKE','RENAME','SELECT_LINKED'] | None
    """

def id_remap(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    id_type: typing.Literal[
        "ACTION",
        "ARMATURE",
        "BRUSH",
        "CAMERA",
        "CACHEFILE",
        "CURVE",
        "FONT",
        "GREASEPENCIL",
        "GROUP",
        "IMAGE",
        "KEY",
        "LAMP",
        "LIBRARY",
        "LINESTYLE",
        "LATTICE",
        "MASK",
        "MATERIAL",
        "META",
        "MESH",
        "MOVIECLIP",
        "NODETREE",
        "OBJECT",
        "PAINTCURVE",
        "PALETTE",
        "PARTICLE",
        "SCENE",
        "SCREEN",
        "SOUND",
        "SPEAKER",
        "TEXT",
        "TEXTURE",
        "WINDOWMANAGER",
        "WORLD",
    ]
    | None = "OBJECT",
    old_id: str | None = "",
    new_id: str | None = "",
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param id_type: ID Type
    :type id_type: typing.Literal['ACTION','ARMATURE','BRUSH','CAMERA','CACHEFILE','CURVE','FONT','GREASEPENCIL','GROUP','IMAGE','KEY','LAMP','LIBRARY','LINESTYLE','LATTICE','MASK','MATERIAL','META','MESH','MOVIECLIP','NODETREE','OBJECT','PAINTCURVE','PALETTE','PARTICLE','SCENE','SCREEN','SOUND','SPEAKER','TEXT','TEXTURE','WINDOWMANAGER','WORLD'] | None
    :param old_id: Old ID, Old ID to replace
    :type old_id: str | None
    :param new_id: New ID, New ID to remap all selected IDs' users to
    :type new_id: str | None
    """

def item_activate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = True,
    recursive: bool | None = False,
):
    """Handle mouse clicks to activate/select items

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection for activation
    :type extend: bool | None
    :param recursive: Recursive, Select Objects and their children
    :type recursive: bool | None
    """

def item_openclose(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    all: bool | None = True,
):
    """Toggle whether item under cursor is enabled or closed

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param all: All, Close or open all items
    :type all: bool | None
    """

def item_rename(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Rename item under cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyingset_add_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add selected items (blue-gray rows) to active Keying Set

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def keyingset_remove_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove selected items (blue-gray rows) from active Keying Set

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def lib_operation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["RENAME", "DELETE", "RELOCATE", "RELOAD"] | None = "RENAME",
):
    """Undocumented

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Library Operation

    RENAME Rename.

    DELETE Delete, Delete this library and all its item from Blender - WARNING: no undo.

    RELOCATE Relocate, Select a new path for this library, and reload all its data.

    RELOAD Reload, Reload all data from this library.
        :type type: typing.Literal['RENAME','DELETE','RELOCATE','RELOAD'] | None
    """

def lib_relocate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Relocate the library under cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def material_drop(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    object: str = "Object",
    material: str = "Material",
):
    """Drag material to object in Outliner

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param object: Object, Target Object
    :type object: str
    :param material: Material, Target Material
    :type material: str
    """

def modifier_operation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["TOGVIS", "TOGREN", "DELETE"] | None = "TOGVIS",
):
    """Undocumented

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Modifier Operation
    :type type: typing.Literal['TOGVIS','TOGREN','DELETE'] | None
    """

def object_operation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal[
        "SELECT",
        "DESELECT",
        "SELECT_HIERARCHY",
        "DELETE",
        "DELETE_HIERARCHY",
        "REMAP",
        "TOGVIS",
        "TOGSEL",
        "TOGREN",
        "RENAME",
    ]
    | None = "SELECT",
):
    """Undocumented

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Object Operation

    SELECT Select.

    DESELECT Deselect.

    SELECT_HIERARCHY Select Hierarchy.

    DELETE Delete.

    DELETE_HIERARCHY Delete Hierarchy.

    REMAP Remap Users, Make all users of selected data-blocks to use instead a new chosen one.

    TOGVIS Toggle Visible.

    TOGSEL Toggle Selectable.

    TOGREN Toggle Renderable.

    RENAME Rename.
        :type type: typing.Literal['SELECT','DESELECT','SELECT_HIERARCHY','DELETE','DELETE_HIERARCHY','REMAP','TOGVIS','TOGSEL','TOGREN','RENAME'] | None
    """

def operation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Context menu for item operations

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def orphans_purge(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear all orphaned data-blocks without any users from the file (cannot be undone, saves to current .blend file)

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def parent_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    dragged_obj: str = "Object",
    type: typing.Literal["CLEAR", "CLEAR_KEEP_TRANSFORM", "CLEAR_INVERSE"]
    | None = "CLEAR",
):
    """Drag to clear parent in Outliner

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param dragged_obj: Child, Child Object
        :type dragged_obj: str
        :param type: Type

    CLEAR Clear Parent, Completely clear the parenting relationship, including involved modifiers if any.

    CLEAR_KEEP_TRANSFORM Clear and Keep Transformation, As 'Clear Parent', but keep the current visual transformations of the object.

    CLEAR_INVERSE Clear Parent Inverse, Reset the transform corrections applied to the parenting relationship, does not remove parenting itself.
        :type type: typing.Literal['CLEAR','CLEAR_KEEP_TRANSFORM','CLEAR_INVERSE'] | None
    """

def parent_drop(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    child: str = "Object",
    parent: str = "Object",
    type: typing.Literal[
        "OBJECT",
        "ARMATURE",
        "ARMATURE_NAME",
        "ARMATURE_AUTO",
        "ARMATURE_ENVELOPE",
        "BONE",
        "BONE_RELATIVE",
        "CURVE",
        "FOLLOW",
        "PATH_CONST",
        "LATTICE",
        "VERTEX",
        "VERTEX_TRI",
    ]
    | None = "OBJECT",
):
    """Drag to parent in Outliner

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param child: Child, Child Object
    :type child: str
    :param parent: Parent, Parent Object
    :type parent: str
    :param type: Type
    :type type: typing.Literal['OBJECT','ARMATURE','ARMATURE_NAME','ARMATURE_AUTO','ARMATURE_ENVELOPE','BONE','BONE_RELATIVE','CURVE','FOLLOW','PATH_CONST','LATTICE','VERTEX','VERTEX_TRI'] | None
    """

def renderability_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the renderability of selected items

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def scene_drop(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    object: str = "Object",
    scene: str = "Scene",
):
    """Drag object to scene in Outliner

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param object: Object, Target Object
    :type object: str
    :param scene: Scene, Target Scene
    :type scene: str
    """

def scene_operation(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["DELETE"] | None = "DELETE",
):
    """Context menu for scene operations

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Scene Operation
    :type type: typing.Literal['DELETE'] | None
    """

def scroll_page(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    up: bool | None = False,
):
    """Scroll page up or down

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param up: Up, Scroll up one page
    :type up: bool | None
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
):
    """Use box selection to select tree elements

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
    """

def selectability_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the selectability

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def selected_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the Outliner selection of items

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def show_active(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Open up the tree and adjust the view so that the active Object is shown centered

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def show_hierarchy(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Open all object entries and close all others

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def show_one_level(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    open: bool | None = True,
):
    """Expand/collapse all entries by one level

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param open: Open, Expand all entries one level deep
    :type open: bool | None
    """

def visibility_toggle(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Toggle the visibility of selected items

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """
