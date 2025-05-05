import typing
import collections.abc
import typing_extensions
import bpy.types

def childof_clear_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
):
    """Clear inverse correction for ChildOf constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: typing.Literal['OBJECT','BONE'] | None
    """

def childof_set_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
):
    """Set inverse correction for ChildOf constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: typing.Literal['OBJECT','BONE'] | None
    """

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove constraint from constraint stack

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def followpath_path_animate(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
    frame_start: int | None = 1,
    length: int | None = 100,
):
    """Add default animation for path used by constraint if it isn't animated already

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: typing.Literal['OBJECT','BONE'] | None
        :param frame_start: Start Frame, First frame of path animation
        :type frame_start: int | None
        :param length: Length, Number of frames that path animation should take
        :type length: int | None
    """

def limitdistance_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
):
    """Reset limiting distance for Limit Distance Constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: typing.Literal['OBJECT','BONE'] | None
    """

def move_down(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
):
    """Move constraint down in constraint stack

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: typing.Literal['OBJECT','BONE'] | None
    """

def move_up(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
):
    """Move constraint up in constraint stack

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: typing.Literal['OBJECT','BONE'] | None
    """

def objectsolver_clear_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
):
    """Clear inverse correction for ObjectSolver constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: typing.Literal['OBJECT','BONE'] | None
    """

def objectsolver_set_inverse(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
):
    """Set inverse correction for ObjectSolver constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: typing.Literal['OBJECT','BONE'] | None
    """

def stretchto_reset(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    constraint: str = "",
    owner: typing.Literal["OBJECT", "BONE"] | None = "OBJECT",
):
    """Reset original length of bone for Stretch To Constraint

        :type override_context: bpy.types.Context | dict[str, typing.Any]
        :type execution_context: int | str | None
        :type undo: bool | None
        :param constraint: Constraint, Name of the constraint to edit
        :type constraint: str
        :param owner: Owner, The owner of this constraint

    OBJECT Object, Edit a constraint on the active object.

    BONE Bone, Edit a constraint on the active bone.
        :type owner: typing.Literal['OBJECT','BONE'] | None
    """
