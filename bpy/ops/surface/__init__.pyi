import typing
import collections.abc
import typing_extensions
import bpy.types

def primitive_nurbs_surface_circle_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
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
    """Construct a Nurbs surface Circle

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: float | None
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

def primitive_nurbs_surface_curve_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
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
    """Construct a Nurbs surface Curve

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: float | None
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

def primitive_nurbs_surface_cylinder_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
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
    """Construct a Nurbs surface Cylinder

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: float | None
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

def primitive_nurbs_surface_sphere_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
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
    """Construct a Nurbs surface Sphere

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: float | None
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

def primitive_nurbs_surface_surface_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
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
    """Construct a Nurbs surface Patch

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: float | None
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

def primitive_nurbs_surface_torus_add(
    override_context: bpy.types.Context | dict[str, typing.Any] = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    radius: float | None = 1.0,
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
    """Construct a Nurbs surface Torus

    :type override_context: bpy.types.Context | dict[str, typing.Any]
    :type execution_context: int | str | None
    :type undo: bool | None
    :param radius: Radius
    :type radius: float | None
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
