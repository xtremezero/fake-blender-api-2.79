"""
This module provides access to math operations.

[NOTE]
Classes, methods and attributes that accept vectors also accept other numeric sequences,
such as tuples, lists.

Submodules:

mathutils.geometry.rst
mathutils.bvhtree.rst
mathutils.kdtree.rst
mathutils.interpolate.rst
mathutils.noise.rst

:maxdepth: 1

The mathutils module provides the following classes:

* Color,
* Euler,
* Matrix,
* Quaternion,
* Vector,

```../examples/mathutils.py```

"""

import typing
import collections.abc
import typing_extensions
from . import bvhtree as bvhtree
from . import geometry as geometry
from . import interpolate as interpolate
from . import kdtree as kdtree
from . import noise as noise

class Color:
    """This object gives access to Colors in Blender."""

    b: float
    """ Blue color channel.

    :type: float
    """

    g: float
    """ Green color channel.

    :type: float
    """

    h: float
    """ HSV Hue component in [0, 1].

    :type: float
    """

    hsv: Vector | collections.abc.Sequence[float]
    """ HSV Values in [0, 1].

    :type: Vector | collections.abc.Sequence[float]
    """

    is_frozen: bool
    """ True when this object has been frozen (read-only).

    :type: bool
    """

    is_wrapped: bool
    """ True when this object wraps external data (read-only).

    :type: bool
    """

    owner: typing.Any
    """ The item this is wrapping or None  (read-only)."""

    r: float
    """ Red color channel.

    :type: float
    """

    s: float
    """ HSV Saturation component in [0, 1].

    :type: float
    """

    v: float
    """ HSV Value component in [0, 1].

    :type: float
    """

    def copy(self) -> typing_extensions.Self:
        """Returns a copy of this color.

        :return: A copy of the color.
        :rtype: typing_extensions.Self
        """

    def freeze(self) -> typing_extensions.Self:
        """Make this object immutable.After this the object can be hashed, used in dictionaries & sets.

        :return: An instance of this object.
        :rtype: typing_extensions.Self
        """

    def __init__(self, rgb: collections.abc.Sequence[float] = (0.0, 0.0, 0.0)):
        """

        :param rgb:
        :type rgb: collections.abc.Sequence[float]
        """

    def __get__(self, instance, owner) -> typing_extensions.Self:
        """

        :param instance:
        :param owner:
        :return:
        :rtype: typing_extensions.Self
        """

    def __set__(
        self, instance, value: collections.abc.Sequence[float] | typing_extensions.Self
    ):
        """

        :param instance:
        :param value:
        :type value: collections.abc.Sequence[float] | typing_extensions.Self
        """

    def __add__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __sub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __mul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    def __truediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    def __radd__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __rsub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __rmul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    def __rtruediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    def __iadd__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __isub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __imul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    def __itruediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    @typing.overload
    def __getitem__(self, key: int) -> float:
        """

        :param key:
        :type key: int
        :return:
        :rtype: float
        """

    @typing.overload
    def __getitem__(self, key: slice) -> tuple[float, ...]:
        """

        :param key:
        :type key: slice
        :return:
        :rtype: tuple[float, ...]
        """

    @typing.overload
    def __setitem__(self, key: int, value: float):
        """

        :param key:
        :type key: int
        :param value:
        :type value: float
        """

    @typing.overload
    def __setitem__(self, key: slice, value: collections.abc.Iterable[float] | Color):
        """

        :param key:
        :type key: slice
        :param value:
        :type value: collections.abc.Iterable[float] | Color
        """

class Euler:
    """This object gives access to Eulers in Blender.`Euler angles <https://en.wikipedia.org/wiki/Euler_angles>`__ on Wikipedia."""

    is_frozen: bool
    """ True when this object has been frozen (read-only).

    :type: bool
    """

    is_wrapped: bool
    """ True when this object wraps external data (read-only).

    :type: bool
    """

    order: typing.Any
    """ Euler rotation order."""

    owner: typing.Any
    """ The item this is wrapping or None  (read-only)."""

    x: float
    """ Euler axis angle in radians.

    :type: float
    """

    y: float
    """ Euler axis angle in radians.

    :type: float
    """

    z: float
    """ Euler axis angle in radians.

    :type: float
    """

    def copy(self) -> typing_extensions.Self:
        """Returns a copy of this euler.

        :return: A copy of the euler.
        :rtype: typing_extensions.Self
        """

    def freeze(self) -> typing_extensions.Self:
        """Make this object immutable.After this the object can be hashed, used in dictionaries & sets.

        :return: An instance of this object.
        :rtype: typing_extensions.Self
        """

    def make_compatible(self, other):
        """Make this euler compatible with another,
        so interpolating between them works as intended.

                :param other:
        """

    def rotate(
        self,
        other: Matrix
        | Quaternion
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | collections.abc.Sequence[float]
        | typing_extensions.Self,
    ):
        """Rotates the euler by another mathutils value.

        :param other: rotation component of mathutils value
        :type other: Matrix | Quaternion | collections.abc.Sequence[collections.abc.Sequence[float]] | collections.abc.Sequence[float] | typing_extensions.Self
        """

    def rotate_axis(self, axis: str, angle: float):
        """Rotates the euler a certain amount and returning a unique euler rotation
        (no 720 degree pitches).

                :param axis: single character in ['X, 'Y', 'Z'].
                :type axis: str
                :param angle: angle in radians.
                :type angle: float
        """

    def to_matrix(self) -> Matrix:
        """Return a matrix representation of the euler.

        :return: A 3x3 rotation matrix representation of the euler.
        :rtype: Matrix
        """

    def to_quaternion(self) -> Quaternion:
        """Return a quaternion representation of the euler.

        :return: Quaternion representation of the euler.
        :rtype: Quaternion
        """

    def zero(self):
        """Set all values to zero."""

    def __init__(
        self,
        angles: collections.abc.Sequence[float] = (0.0, 0.0, 0.0),
        order: str = "XYZ",
    ):
        """

        :param angles:
        :type angles: collections.abc.Sequence[float]
        :param order:
        :type order: str
        """

    def __get__(self, instance, owner) -> typing_extensions.Self:
        """

        :param instance:
        :param owner:
        :return:
        :rtype: typing_extensions.Self
        """

    def __set__(
        self, instance, value: collections.abc.Sequence[float] | typing_extensions.Self
    ):
        """

        :param instance:
        :param value:
        :type value: collections.abc.Sequence[float] | typing_extensions.Self
        """

    @typing.overload
    def __getitem__(self, key: int) -> float:
        """

        :param key:
        :type key: int
        :return:
        :rtype: float
        """

    @typing.overload
    def __getitem__(self, key: slice) -> tuple[float, ...]:
        """

        :param key:
        :type key: slice
        :return:
        :rtype: tuple[float, ...]
        """

    @typing.overload
    def __setitem__(self, key: int, value: float):
        """

        :param key:
        :type key: int
        :param value:
        :type value: float
        """

    @typing.overload
    def __setitem__(self, key: slice, value: collections.abc.Iterable[float] | Euler):
        """

        :param key:
        :type key: slice
        :param value:
        :type value: collections.abc.Iterable[float] | Euler
        """

class Matrix:
    """This object gives access to Matrices in Blender, supporting square and rectangular
    matrices from 2x2 up to 4x4.
    """

    col: typing.Any
    """ Access the matrix by columns, 3x3 and 4x4 only, (read-only)."""

    is_frozen: bool
    """ True when this object has been frozen (read-only).

    :type: bool
    """

    is_negative: bool
    """ True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only).

    :type: bool
    """

    is_orthogonal: bool
    """ True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only).

    :type: bool
    """

    is_orthogonal_axis_vectors: bool
    """ True if this matrix has got orthogonal axis vectors, 3x3 and 4x4 only, (read-only).

    :type: bool
    """

    is_wrapped: bool
    """ True when this object wraps external data (read-only).

    :type: bool
    """

    median_scale: float
    """ The average scale applied to each axis (read-only).

    :type: float
    """

    owner: typing.Any
    """ The item this is wrapping or None  (read-only)."""

    row: typing.Any
    """ Access the matrix by rows (default), (read-only)."""

    translation: Vector
    """ The translation component of the matrix.

    :type: Vector
    """

    @classmethod
    def Identity(cls, size: int) -> typing_extensions.Self:
        """Create an identity matrix.

        :param size: The size of the identity matrix to construct [2, 4].
        :type size: int
        :return: A new identity matrix.
        :rtype: typing_extensions.Self
        """

    @classmethod
    def OrthoProjection(
        cls, axis: Vector | collections.abc.Sequence[float] | str, size: int
    ) -> typing_extensions.Self:
        """Create a matrix to represent an orthographic projection.

                :param axis: Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'],
        where a single axis is for a 2D matrix.
        Or a vector for an arbitrary axis
                :type axis: Vector | collections.abc.Sequence[float] | str
                :param size: The size of the projection matrix to construct [2, 4].
                :type size: int
                :return: A new projection matrix.
                :rtype: typing_extensions.Self
        """

    @classmethod
    def Rotation(
        cls,
        angle: float,
        size: int,
        axis: Vector | collections.abc.Sequence[float] | str | None = "",
    ) -> typing_extensions.Self:
        """Create a matrix representing a rotation.

                :param angle: The angle of rotation desired, in radians.
                :type angle: float
                :param size: The size of the rotation matrix to construct [2, 4].
                :type size: int
                :param axis: a string in ['X', 'Y', 'Z'] or a 3D Vector Object
        (optional when size is 2).
                :type axis: Vector | collections.abc.Sequence[float] | str | None
                :return: A new rotation matrix.
                :rtype: typing_extensions.Self
        """

    @classmethod
    def Scale(
        cls,
        factor: float,
        size: int,
        axis: Vector | collections.abc.Sequence[float] | None = [],
    ) -> typing_extensions.Self:
        """Create a matrix representing a scaling.

        :param factor: The factor of scaling to apply.
        :type factor: float
        :param size: The size of the scale matrix to construct [2, 4].
        :type size: int
        :param axis: Direction to influence scale. (optional).
        :type axis: Vector | collections.abc.Sequence[float] | None
        :return: A new scale matrix.
        :rtype: typing_extensions.Self
        """

    @classmethod
    def Shear(cls, plane: str, size: int, factor: float) -> typing_extensions.Self:
        """Create a matrix to represent an shear transformation.

                :param plane: Can be any of the following: ['X', 'Y', 'XY', 'XZ', 'YZ'],
        where a single axis is for a 2D matrix only.
                :type plane: str
                :param size: The size of the shear matrix to construct [2, 4].
                :type size: int
                :param factor: The factor of shear to apply. For a 3 or 4 size matrix
        pass a pair of floats corresponding with the plane axis.
                :type factor: float
                :return: A new shear matrix.
                :rtype: typing_extensions.Self
        """

    @classmethod
    def Translation(
        cls, vector: Vector | collections.abc.Sequence[float]
    ) -> typing_extensions.Self:
        """Create a matrix representing a translation.

        :param vector: The translation vector.
        :type vector: Vector | collections.abc.Sequence[float]
        :return: An identity matrix with a translation.
        :rtype: typing_extensions.Self
        """

    def adjugate(self):
        """Set the matrix to its adjugate.`Adjugate matrix <https://en.wikipedia.org/wiki/Adjugate_matrix>` on Wikipedia."""

    def adjugated(self) -> typing_extensions.Self:
        """Return an adjugated copy of the matrix.

        :return: the adjugated matrix.
        :rtype: typing_extensions.Self
        """

    def copy(self) -> typing_extensions.Self:
        """Returns a copy of this matrix.

        :return: an instance of itself
        :rtype: typing_extensions.Self
        """

    def decompose(self) -> tuple[Vector, Quaternion, Vector]:
        """Return the translation, rotation, and scale components of this matrix.

        :return: tuple of translation, rotation, and scale
        :rtype: tuple[Vector, Quaternion, Vector]
        """

    def determinant(self) -> float:
        """Return the determinant of a matrix.`Determinant <https://en.wikipedia.org/wiki/Determinant>` on Wikipedia.

        :return: Return the determinant of a matrix.
        :rtype: float
        """

    def freeze(self) -> typing_extensions.Self:
        """Make this object immutable.After this the object can be hashed, used in dictionaries & sets.

        :return: An instance of this object.
        :rtype: typing_extensions.Self
        """

    def identity(self):
        """Set the matrix to the identity matrix.`Identity matrix <https://en.wikipedia.org/wiki/Identity_matrix>` on Wikipedia."""

    def invert(
        self,
        fallback: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self
        | None = None,
    ):
        """Set the matrix to its inverse.`Inverse matrix <https://en.wikipedia.org/wiki/Inverse_matrix>` on Wikipedia.

                :param fallback: Set the matrix to this value when the inverse cannot be calculated
        (instead of raising a `ValueError` exception).
                :type fallback: collections.abc.Sequence[collections.abc.Sequence[float]] | typing_extensions.Self | None
        """

    def invert_safe(self):
        """Set the matrix to its inverse, will never error.
        If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
        If tweaked matrix is still degenerated, set to the identity matrix instead.`Inverse Matrix <https://en.wikipedia.org/wiki/Inverse_matrix>` on Wikipedia.

        """

    def inverted(self, fallback: typing.Any | None = None) -> typing_extensions.Self:
        """Return an inverted copy of the matrix.

                :param fallback: return this when the inverse can't be calculated
        (instead of raising a `ValueError`).
                :type fallback: typing.Any | None
                :return: the inverted matrix or fallback when given.
                :rtype: typing_extensions.Self
        """

    def inverted_safe(self) -> typing_extensions.Self:
        """Return an inverted copy of the matrix, will never error.
        If degenerated (e.g. zero scale on an axis), add some epsilon to its diagonal, to get an invertible one.
        If tweaked matrix is still degenerated, return the identity matrix instead.

                :return: the inverted matrix.
                :rtype: typing_extensions.Self
        """

    def lerp(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
        factor: float,
    ) -> typing_extensions.Self:
        """Returns the interpolation of two matrices. Uses polar decomposition, see   "Matrix Animation and Polar Decomposition", Shoemake and Duff, 1992.

        :param other: value to interpolate with.
        :type other: collections.abc.Sequence[collections.abc.Sequence[float]] | typing_extensions.Self
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :return: The interpolated matrix.
        :rtype: typing_extensions.Self
        """

    def normalize(self):
        """Normalize each of the matrix columns."""

    def normalized(self) -> typing_extensions.Self:
        """Return a column normalized matrix

        :return: a column normalized matrix
        :rtype: typing_extensions.Self
        """

    def resize_4x4(self):
        """Resize the matrix to 4x4."""

    def rotate(
        self,
        other: Euler
        | Quaternion
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | collections.abc.Sequence[float]
        | typing_extensions.Self,
    ):
        """Rotates the matrix by another mathutils value.

        :param other: rotation component of mathutils value
        :type other: Euler | Quaternion | collections.abc.Sequence[collections.abc.Sequence[float]] | collections.abc.Sequence[float] | typing_extensions.Self
        """

    def to_3x3(self) -> typing_extensions.Self:
        """Return a 3x3 copy of this matrix.

        :return: a new matrix.
        :rtype: typing_extensions.Self
        """

    def to_4x4(self) -> typing_extensions.Self:
        """Return a 4x4 copy of this matrix.

        :return: a new matrix.
        :rtype: typing_extensions.Self
        """

    def to_euler(
        self,
        order: str | None = "",
        euler_compat: Euler | collections.abc.Sequence[float] | None = [],
    ) -> Euler:
        """Return an Euler representation of the rotation matrix
        (3x3 or 4x4 matrix only).

                :param order: Optional rotation order argument in
        ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
                :type order: str | None
                :param euler_compat: Optional euler argument the new euler will be made
        compatible with (no axis flipping between them).
        Useful for converting a series of matrices to animation curves.
                :type euler_compat: Euler | collections.abc.Sequence[float] | None
                :return: Euler representation of the matrix.
                :rtype: Euler
        """

    def to_quaternion(self) -> Quaternion:
        """Return a quaternion representation of the rotation matrix.

        :return: Quaternion representation of the rotation matrix.
        :rtype: Quaternion
        """

    def to_scale(self) -> Vector:
        """Return the scale part of a 3x3 or 4x4 matrix.

        :return: Return the scale of a matrix.
        :rtype: Vector
        """

    def to_translation(self) -> Vector:
        """Return the translation part of a 4 row matrix.

        :return: Return the translation of a matrix.
        :rtype: Vector
        """

    def transpose(self):
        """Set the matrix to its transpose.`Transpose <https://en.wikipedia.org/wiki/Transpose>` on Wikipedia."""

    def transposed(self) -> typing_extensions.Self:
        """Return a new, transposed matrix.

        :return: a transposed matrix
        :rtype: typing_extensions.Self
        """

    def zero(self) -> typing_extensions.Self:
        """Set all the matrix values to zero.

        :return:
        :rtype: typing_extensions.Self
        """

    def __init__(
        self,
        rows: collections.abc.Sequence[collections.abc.Sequence[float]] = (
            (1.0, 0.0, 0.0, 0.0),
            (0.0, 1.0, 0.0, 0.0),
            (0.0, 0.0, 1.0, 0.0),
            (0.0, 0.0, 0.0, 1.0),
        ),
    ):
        """

        :param rows:
        :type rows: collections.abc.Sequence[collections.abc.Sequence[float]]
        """

    def __get__(self, instance, owner) -> typing_extensions.Self:
        """

        :param instance:
        :param owner:
        :return:
        :rtype: typing_extensions.Self
        """

    def __set__(
        self,
        instance,
        value: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ):
        """

        :param instance:
        :param value:
        :type value: collections.abc.Sequence[collections.abc.Sequence[float]] | typing_extensions.Self
        """

    @typing.overload
    def __getitem__(self, key: int) -> Vector:
        """

        :param key:
        :type key: int
        :return:
        :rtype: Vector
        """

    @typing.overload
    def __getitem__(self, key: slice) -> tuple[Vector, ...]:
        """

        :param key:
        :type key: slice
        :return:
        :rtype: tuple[Vector, ...]
        """

    @typing.overload
    def __setitem__(self, key: int, value: Vector | collections.abc.Iterable[float]):
        """

        :param key:
        :type key: int
        :param value:
        :type value: Vector | collections.abc.Iterable[float]
        """

    @typing.overload
    def __setitem__(
        self,
        key: slice,
        value: collections.abc.Iterable[Vector | collections.abc.Iterable[float]]
        | Matrix,
    ):
        """

        :param key:
        :type key: slice
        :param value:
        :type value: collections.abc.Iterable[Vector | collections.abc.Iterable[float]] | Matrix
        """

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """

    def __add__(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[collections.abc.Sequence[float]] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __sub__(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[collections.abc.Sequence[float]] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __mul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    @typing.overload
    def __matmul__(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[collections.abc.Sequence[float]] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    @typing.overload
    def __matmul__(self, other: Vector | collections.abc.Sequence[float]) -> Vector:
        """

        :param other:
        :type other: Vector | collections.abc.Sequence[float]
        :return:
        :rtype: Vector
        """

    def __radd__(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[collections.abc.Sequence[float]] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __rsub__(
        self,
        other: collections.abc.Sequence[collections.abc.Sequence[float]]
        | typing_extensions.Self,
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[collections.abc.Sequence[float]] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __rmul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    def __imul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

class Quaternion:
    """This object gives access to Quaternions in Blender.The constructor takes arguments in various forms:"""

    angle: float
    """ Angle of the quaternion.

    :type: float
    """

    axis: Vector
    """ Quaternion axis as a vector.

    :type: Vector
    """

    is_frozen: bool
    """ True when this object has been frozen (read-only).

    :type: bool
    """

    is_wrapped: bool
    """ True when this object wraps external data (read-only).

    :type: bool
    """

    magnitude: float
    """ Size of the quaternion (read-only).

    :type: float
    """

    owner: typing.Any
    """ The item this is wrapping or None  (read-only)."""

    w: float
    """ Quaternion axis value.

    :type: float
    """

    x: float
    """ Quaternion axis value.

    :type: float
    """

    y: float
    """ Quaternion axis value.

    :type: float
    """

    z: float
    """ Quaternion axis value.

    :type: float
    """

    def conjugate(self):
        """Set the quaternion to its conjugate (negate x, y, z)."""

    def conjugated(self) -> typing_extensions.Self:
        """Return a new conjugated quaternion.

        :return: a new quaternion.
        :rtype: typing_extensions.Self
        """

    def copy(self) -> typing_extensions.Self:
        """Returns a copy of this quaternion.

        :return: A copy of the quaternion.
        :rtype: typing_extensions.Self
        """

    def cross(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """Return the cross product of this quaternion and another.

        :param other: The other quaternion to perform the cross product with.
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return: The cross product.
        :rtype: typing_extensions.Self
        """

    def dot(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """Return the dot product of this quaternion and another.

        :param other: The other quaternion to perform the dot product with.
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return: The dot product.
        :rtype: typing_extensions.Self
        """

    def freeze(self) -> typing_extensions.Self:
        """Make this object immutable.After this the object can be hashed, used in dictionaries & sets.

        :return: An instance of this object.
        :rtype: typing_extensions.Self
        """

    def identity(self) -> typing_extensions.Self:
        """Set the quaternion to an identity quaternion.

        :return:
        :rtype: typing_extensions.Self
        """

    def invert(self):
        """Set the quaternion to its inverse."""

    def inverted(self) -> typing_extensions.Self:
        """Return a new, inverted quaternion.

        :return: the inverted value.
        :rtype: typing_extensions.Self
        """

    def negate(self) -> typing_extensions.Self:
        """Set the quaternion to its negative.

        :return:
        :rtype: typing_extensions.Self
        """

    def normalize(self):
        """Normalize the quaternion."""

    def normalized(self) -> typing_extensions.Self:
        """Return a new normalized quaternion.

        :return: a normalized copy.
        :rtype: typing_extensions.Self
        """

    def rotate(
        self,
        other: Euler
        | Matrix
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | collections.abc.Sequence[float]
        | typing_extensions.Self,
    ):
        """Rotates the quaternion by another mathutils value.

        :param other: rotation component of mathutils value
        :type other: Euler | Matrix | collections.abc.Sequence[collections.abc.Sequence[float]] | collections.abc.Sequence[float] | typing_extensions.Self
        """

    def rotation_difference(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """Returns a quaternion representing the rotational difference.

        :param other: second quaternion.
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return: the rotational difference between the two quat rotations.
        :rtype: typing_extensions.Self
        """

    def slerp(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        factor: float,
    ) -> typing_extensions.Self:
        """Returns the interpolation of two quaternions.

        :param other: value to interpolate with.
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :return: The interpolated rotation.
        :rtype: typing_extensions.Self
        """

    def to_axis_angle(self) -> tuple[Vector, float]:
        """Return the axis, angle representation of the quaternion.

        :return: axis, angle.
        :rtype: tuple[Vector, float]
        """

    def to_euler(
        self,
        order: str | None = "",
        euler_compat: Euler | collections.abc.Sequence[float] | None = [],
    ) -> Euler:
        """Return Euler representation of the quaternion.

                :param order: Optional rotation order argument in
        ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX'].
                :type order: str | None
                :param euler_compat: Optional euler argument the new euler will be made
        compatible with (no axis flipping between them).
        Useful for converting a series of matrices to animation curves.
                :type euler_compat: Euler | collections.abc.Sequence[float] | None
                :return: Euler representation of the quaternion.
                :rtype: Euler
        """

    def to_exponential_map(self):
        """Return the exponential map representation of the quaternion.This representation consist of the rotation axis multiplied by the rotation angle.   Such a representation is useful for interpolation between multiple orientations.To convert back to a quaternion, pass it to the `Quaternion` constructor.

        :return: exponential map.
        """

    def to_matrix(self) -> Matrix:
        """Return a matrix representation of the quaternion.

        :return: A 3x3 rotation matrix representation of the quaternion.
        :rtype: Matrix
        """

    def __init__(
        self,
        seq: Vector | collections.abc.Sequence[float] = (1.0, 0.0, 0.0, 0.0),
        angle: float = 0.0,
    ):
        """

        :param seq:
        :type seq: Vector | collections.abc.Sequence[float]
        :param angle:
        :type angle: float
        """

    def __get__(self, instance, owner) -> typing_extensions.Self:
        """

        :param instance:
        :param owner:
        :return:
        :rtype: typing_extensions.Self
        """

    def __set__(
        self, instance, value: collections.abc.Sequence[float] | typing_extensions.Self
    ):
        """

        :param instance:
        :param value:
        :type value: collections.abc.Sequence[float] | typing_extensions.Self
        """

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """

    @typing.overload
    def __getitem__(self, key: int) -> float:
        """

        :param key:
        :type key: int
        :return:
        :rtype: float
        """

    @typing.overload
    def __getitem__(self, key: slice) -> tuple[float, ...]:
        """

        :param key:
        :type key: slice
        :return:
        :rtype: tuple[float, ...]
        """

    @typing.overload
    def __setitem__(self, key: int, value: float):
        """

        :param key:
        :type key: int
        :param value:
        :type value: float
        """

    @typing.overload
    def __setitem__(
        self, key: slice, value: collections.abc.Iterable[float] | Quaternion
    ):
        """

        :param key:
        :type key: slice
        :param value:
        :type value: collections.abc.Iterable[float] | Quaternion
        """

    def __add__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __sub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __mul__(
        self, other: collections.abc.Sequence[float] | float | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | float | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    @typing.overload
    def __matmul__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    @typing.overload
    def __matmul__(self, other: Vector | collections.abc.Sequence[float]) -> Vector:
        """

        :param other:
        :type other: Vector | collections.abc.Sequence[float]
        :return:
        :rtype: Vector
        """

    def __radd__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __rsub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __rmul__(
        self, other: collections.abc.Sequence[float] | float | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | float | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __imul__(
        self, other: collections.abc.Sequence[float] | float | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | float | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

class Vector:
    """This object gives access to Vectors in Blender."""

    is_frozen: bool
    """ True when this object has been frozen (read-only).

    :type: bool
    """

    is_wrapped: bool
    """ True when this object wraps external data (read-only).

    :type: bool
    """

    length: float
    """ Vector Length.

    :type: float
    """

    length_squared: float
    """ Vector length squared (v.dot(v)).

    :type: float
    """

    magnitude: float
    """ Vector Length.

    :type: float
    """

    owner: typing.Any
    """ The item this is wrapping or None  (read-only)."""

    w: float
    """ Vector W axis (4D Vectors only).

    :type: float
    """

    ww: typing.Any
    """ Undocumented"""

    www: typing.Any
    """ Undocumented"""

    wwww: typing.Any
    """ Undocumented"""

    wwwx: typing.Any
    """ Undocumented"""

    wwwy: typing.Any
    """ Undocumented"""

    wwwz: typing.Any
    """ Undocumented"""

    wwx: typing.Any
    """ Undocumented"""

    wwxw: typing.Any
    """ Undocumented"""

    wwxx: typing.Any
    """ Undocumented"""

    wwxy: typing.Any
    """ Undocumented"""

    wwxz: typing.Any
    """ Undocumented"""

    wwy: typing.Any
    """ Undocumented"""

    wwyw: typing.Any
    """ Undocumented"""

    wwyx: typing.Any
    """ Undocumented"""

    wwyy: typing.Any
    """ Undocumented"""

    wwyz: typing.Any
    """ Undocumented"""

    wwz: typing.Any
    """ Undocumented"""

    wwzw: typing.Any
    """ Undocumented"""

    wwzx: typing.Any
    """ Undocumented"""

    wwzy: typing.Any
    """ Undocumented"""

    wwzz: typing.Any
    """ Undocumented"""

    wx: typing.Any
    """ Undocumented"""

    wxw: typing.Any
    """ Undocumented"""

    wxww: typing.Any
    """ Undocumented"""

    wxwx: typing.Any
    """ Undocumented"""

    wxwy: typing.Any
    """ Undocumented"""

    wxwz: typing.Any
    """ Undocumented"""

    wxx: typing.Any
    """ Undocumented"""

    wxxw: typing.Any
    """ Undocumented"""

    wxxx: typing.Any
    """ Undocumented"""

    wxxy: typing.Any
    """ Undocumented"""

    wxxz: typing.Any
    """ Undocumented"""

    wxy: typing.Any
    """ Undocumented"""

    wxyw: typing.Any
    """ Undocumented"""

    wxyx: typing.Any
    """ Undocumented"""

    wxyy: typing.Any
    """ Undocumented"""

    wxyz: typing.Any
    """ Undocumented"""

    wxz: typing.Any
    """ Undocumented"""

    wxzw: typing.Any
    """ Undocumented"""

    wxzx: typing.Any
    """ Undocumented"""

    wxzy: typing.Any
    """ Undocumented"""

    wxzz: typing.Any
    """ Undocumented"""

    wy: typing.Any
    """ Undocumented"""

    wyw: typing.Any
    """ Undocumented"""

    wyww: typing.Any
    """ Undocumented"""

    wywx: typing.Any
    """ Undocumented"""

    wywy: typing.Any
    """ Undocumented"""

    wywz: typing.Any
    """ Undocumented"""

    wyx: typing.Any
    """ Undocumented"""

    wyxw: typing.Any
    """ Undocumented"""

    wyxx: typing.Any
    """ Undocumented"""

    wyxy: typing.Any
    """ Undocumented"""

    wyxz: typing.Any
    """ Undocumented"""

    wyy: typing.Any
    """ Undocumented"""

    wyyw: typing.Any
    """ Undocumented"""

    wyyx: typing.Any
    """ Undocumented"""

    wyyy: typing.Any
    """ Undocumented"""

    wyyz: typing.Any
    """ Undocumented"""

    wyz: typing.Any
    """ Undocumented"""

    wyzw: typing.Any
    """ Undocumented"""

    wyzx: typing.Any
    """ Undocumented"""

    wyzy: typing.Any
    """ Undocumented"""

    wyzz: typing.Any
    """ Undocumented"""

    wz: typing.Any
    """ Undocumented"""

    wzw: typing.Any
    """ Undocumented"""

    wzww: typing.Any
    """ Undocumented"""

    wzwx: typing.Any
    """ Undocumented"""

    wzwy: typing.Any
    """ Undocumented"""

    wzwz: typing.Any
    """ Undocumented"""

    wzx: typing.Any
    """ Undocumented"""

    wzxw: typing.Any
    """ Undocumented"""

    wzxx: typing.Any
    """ Undocumented"""

    wzxy: typing.Any
    """ Undocumented"""

    wzxz: typing.Any
    """ Undocumented"""

    wzy: typing.Any
    """ Undocumented"""

    wzyw: typing.Any
    """ Undocumented"""

    wzyx: typing.Any
    """ Undocumented"""

    wzyy: typing.Any
    """ Undocumented"""

    wzyz: typing.Any
    """ Undocumented"""

    wzz: typing.Any
    """ Undocumented"""

    wzzw: typing.Any
    """ Undocumented"""

    wzzx: typing.Any
    """ Undocumented"""

    wzzy: typing.Any
    """ Undocumented"""

    wzzz: typing.Any
    """ Undocumented"""

    x: float
    """ Vector X axis.

    :type: float
    """

    xw: typing.Any
    """ Undocumented"""

    xww: typing.Any
    """ Undocumented"""

    xwww: typing.Any
    """ Undocumented"""

    xwwx: typing.Any
    """ Undocumented"""

    xwwy: typing.Any
    """ Undocumented"""

    xwwz: typing.Any
    """ Undocumented"""

    xwx: typing.Any
    """ Undocumented"""

    xwxw: typing.Any
    """ Undocumented"""

    xwxx: typing.Any
    """ Undocumented"""

    xwxy: typing.Any
    """ Undocumented"""

    xwxz: typing.Any
    """ Undocumented"""

    xwy: typing.Any
    """ Undocumented"""

    xwyw: typing.Any
    """ Undocumented"""

    xwyx: typing.Any
    """ Undocumented"""

    xwyy: typing.Any
    """ Undocumented"""

    xwyz: typing.Any
    """ Undocumented"""

    xwz: typing.Any
    """ Undocumented"""

    xwzw: typing.Any
    """ Undocumented"""

    xwzx: typing.Any
    """ Undocumented"""

    xwzy: typing.Any
    """ Undocumented"""

    xwzz: typing.Any
    """ Undocumented"""

    xx: typing.Any
    """ Undocumented"""

    xxw: typing.Any
    """ Undocumented"""

    xxww: typing.Any
    """ Undocumented"""

    xxwx: typing.Any
    """ Undocumented"""

    xxwy: typing.Any
    """ Undocumented"""

    xxwz: typing.Any
    """ Undocumented"""

    xxx: typing.Any
    """ Undocumented"""

    xxxw: typing.Any
    """ Undocumented"""

    xxxx: typing.Any
    """ Undocumented"""

    xxxy: typing.Any
    """ Undocumented"""

    xxxz: typing.Any
    """ Undocumented"""

    xxy: typing.Any
    """ Undocumented"""

    xxyw: typing.Any
    """ Undocumented"""

    xxyx: typing.Any
    """ Undocumented"""

    xxyy: typing.Any
    """ Undocumented"""

    xxyz: typing.Any
    """ Undocumented"""

    xxz: typing.Any
    """ Undocumented"""

    xxzw: typing.Any
    """ Undocumented"""

    xxzx: typing.Any
    """ Undocumented"""

    xxzy: typing.Any
    """ Undocumented"""

    xxzz: typing.Any
    """ Undocumented"""

    xy: typing.Any
    """ Undocumented"""

    xyw: typing.Any
    """ Undocumented"""

    xyww: typing.Any
    """ Undocumented"""

    xywx: typing.Any
    """ Undocumented"""

    xywy: typing.Any
    """ Undocumented"""

    xywz: typing.Any
    """ Undocumented"""

    xyx: typing.Any
    """ Undocumented"""

    xyxw: typing.Any
    """ Undocumented"""

    xyxx: typing.Any
    """ Undocumented"""

    xyxy: typing.Any
    """ Undocumented"""

    xyxz: typing.Any
    """ Undocumented"""

    xyy: typing.Any
    """ Undocumented"""

    xyyw: typing.Any
    """ Undocumented"""

    xyyx: typing.Any
    """ Undocumented"""

    xyyy: typing.Any
    """ Undocumented"""

    xyyz: typing.Any
    """ Undocumented"""

    xyz: typing.Any
    """ Undocumented"""

    xyzw: typing.Any
    """ Undocumented"""

    xyzx: typing.Any
    """ Undocumented"""

    xyzy: typing.Any
    """ Undocumented"""

    xyzz: typing.Any
    """ Undocumented"""

    xz: typing.Any
    """ Undocumented"""

    xzw: typing.Any
    """ Undocumented"""

    xzww: typing.Any
    """ Undocumented"""

    xzwx: typing.Any
    """ Undocumented"""

    xzwy: typing.Any
    """ Undocumented"""

    xzwz: typing.Any
    """ Undocumented"""

    xzx: typing.Any
    """ Undocumented"""

    xzxw: typing.Any
    """ Undocumented"""

    xzxx: typing.Any
    """ Undocumented"""

    xzxy: typing.Any
    """ Undocumented"""

    xzxz: typing.Any
    """ Undocumented"""

    xzy: typing.Any
    """ Undocumented"""

    xzyw: typing.Any
    """ Undocumented"""

    xzyx: typing.Any
    """ Undocumented"""

    xzyy: typing.Any
    """ Undocumented"""

    xzyz: typing.Any
    """ Undocumented"""

    xzz: typing.Any
    """ Undocumented"""

    xzzw: typing.Any
    """ Undocumented"""

    xzzx: typing.Any
    """ Undocumented"""

    xzzy: typing.Any
    """ Undocumented"""

    xzzz: typing.Any
    """ Undocumented"""

    y: float
    """ Vector Y axis.

    :type: float
    """

    yw: typing.Any
    """ Undocumented"""

    yww: typing.Any
    """ Undocumented"""

    ywww: typing.Any
    """ Undocumented"""

    ywwx: typing.Any
    """ Undocumented"""

    ywwy: typing.Any
    """ Undocumented"""

    ywwz: typing.Any
    """ Undocumented"""

    ywx: typing.Any
    """ Undocumented"""

    ywxw: typing.Any
    """ Undocumented"""

    ywxx: typing.Any
    """ Undocumented"""

    ywxy: typing.Any
    """ Undocumented"""

    ywxz: typing.Any
    """ Undocumented"""

    ywy: typing.Any
    """ Undocumented"""

    ywyw: typing.Any
    """ Undocumented"""

    ywyx: typing.Any
    """ Undocumented"""

    ywyy: typing.Any
    """ Undocumented"""

    ywyz: typing.Any
    """ Undocumented"""

    ywz: typing.Any
    """ Undocumented"""

    ywzw: typing.Any
    """ Undocumented"""

    ywzx: typing.Any
    """ Undocumented"""

    ywzy: typing.Any
    """ Undocumented"""

    ywzz: typing.Any
    """ Undocumented"""

    yx: typing.Any
    """ Undocumented"""

    yxw: typing.Any
    """ Undocumented"""

    yxww: typing.Any
    """ Undocumented"""

    yxwx: typing.Any
    """ Undocumented"""

    yxwy: typing.Any
    """ Undocumented"""

    yxwz: typing.Any
    """ Undocumented"""

    yxx: typing.Any
    """ Undocumented"""

    yxxw: typing.Any
    """ Undocumented"""

    yxxx: typing.Any
    """ Undocumented"""

    yxxy: typing.Any
    """ Undocumented"""

    yxxz: typing.Any
    """ Undocumented"""

    yxy: typing.Any
    """ Undocumented"""

    yxyw: typing.Any
    """ Undocumented"""

    yxyx: typing.Any
    """ Undocumented"""

    yxyy: typing.Any
    """ Undocumented"""

    yxyz: typing.Any
    """ Undocumented"""

    yxz: typing.Any
    """ Undocumented"""

    yxzw: typing.Any
    """ Undocumented"""

    yxzx: typing.Any
    """ Undocumented"""

    yxzy: typing.Any
    """ Undocumented"""

    yxzz: typing.Any
    """ Undocumented"""

    yy: typing.Any
    """ Undocumented"""

    yyw: typing.Any
    """ Undocumented"""

    yyww: typing.Any
    """ Undocumented"""

    yywx: typing.Any
    """ Undocumented"""

    yywy: typing.Any
    """ Undocumented"""

    yywz: typing.Any
    """ Undocumented"""

    yyx: typing.Any
    """ Undocumented"""

    yyxw: typing.Any
    """ Undocumented"""

    yyxx: typing.Any
    """ Undocumented"""

    yyxy: typing.Any
    """ Undocumented"""

    yyxz: typing.Any
    """ Undocumented"""

    yyy: typing.Any
    """ Undocumented"""

    yyyw: typing.Any
    """ Undocumented"""

    yyyx: typing.Any
    """ Undocumented"""

    yyyy: typing.Any
    """ Undocumented"""

    yyyz: typing.Any
    """ Undocumented"""

    yyz: typing.Any
    """ Undocumented"""

    yyzw: typing.Any
    """ Undocumented"""

    yyzx: typing.Any
    """ Undocumented"""

    yyzy: typing.Any
    """ Undocumented"""

    yyzz: typing.Any
    """ Undocumented"""

    yz: typing.Any
    """ Undocumented"""

    yzw: typing.Any
    """ Undocumented"""

    yzww: typing.Any
    """ Undocumented"""

    yzwx: typing.Any
    """ Undocumented"""

    yzwy: typing.Any
    """ Undocumented"""

    yzwz: typing.Any
    """ Undocumented"""

    yzx: typing.Any
    """ Undocumented"""

    yzxw: typing.Any
    """ Undocumented"""

    yzxx: typing.Any
    """ Undocumented"""

    yzxy: typing.Any
    """ Undocumented"""

    yzxz: typing.Any
    """ Undocumented"""

    yzy: typing.Any
    """ Undocumented"""

    yzyw: typing.Any
    """ Undocumented"""

    yzyx: typing.Any
    """ Undocumented"""

    yzyy: typing.Any
    """ Undocumented"""

    yzyz: typing.Any
    """ Undocumented"""

    yzz: typing.Any
    """ Undocumented"""

    yzzw: typing.Any
    """ Undocumented"""

    yzzx: typing.Any
    """ Undocumented"""

    yzzy: typing.Any
    """ Undocumented"""

    yzzz: typing.Any
    """ Undocumented"""

    z: float
    """ Vector Z axis (3D Vectors only).

    :type: float
    """

    zw: typing.Any
    """ Undocumented"""

    zww: typing.Any
    """ Undocumented"""

    zwww: typing.Any
    """ Undocumented"""

    zwwx: typing.Any
    """ Undocumented"""

    zwwy: typing.Any
    """ Undocumented"""

    zwwz: typing.Any
    """ Undocumented"""

    zwx: typing.Any
    """ Undocumented"""

    zwxw: typing.Any
    """ Undocumented"""

    zwxx: typing.Any
    """ Undocumented"""

    zwxy: typing.Any
    """ Undocumented"""

    zwxz: typing.Any
    """ Undocumented"""

    zwy: typing.Any
    """ Undocumented"""

    zwyw: typing.Any
    """ Undocumented"""

    zwyx: typing.Any
    """ Undocumented"""

    zwyy: typing.Any
    """ Undocumented"""

    zwyz: typing.Any
    """ Undocumented"""

    zwz: typing.Any
    """ Undocumented"""

    zwzw: typing.Any
    """ Undocumented"""

    zwzx: typing.Any
    """ Undocumented"""

    zwzy: typing.Any
    """ Undocumented"""

    zwzz: typing.Any
    """ Undocumented"""

    zx: typing.Any
    """ Undocumented"""

    zxw: typing.Any
    """ Undocumented"""

    zxww: typing.Any
    """ Undocumented"""

    zxwx: typing.Any
    """ Undocumented"""

    zxwy: typing.Any
    """ Undocumented"""

    zxwz: typing.Any
    """ Undocumented"""

    zxx: typing.Any
    """ Undocumented"""

    zxxw: typing.Any
    """ Undocumented"""

    zxxx: typing.Any
    """ Undocumented"""

    zxxy: typing.Any
    """ Undocumented"""

    zxxz: typing.Any
    """ Undocumented"""

    zxy: typing.Any
    """ Undocumented"""

    zxyw: typing.Any
    """ Undocumented"""

    zxyx: typing.Any
    """ Undocumented"""

    zxyy: typing.Any
    """ Undocumented"""

    zxyz: typing.Any
    """ Undocumented"""

    zxz: typing.Any
    """ Undocumented"""

    zxzw: typing.Any
    """ Undocumented"""

    zxzx: typing.Any
    """ Undocumented"""

    zxzy: typing.Any
    """ Undocumented"""

    zxzz: typing.Any
    """ Undocumented"""

    zy: typing.Any
    """ Undocumented"""

    zyw: typing.Any
    """ Undocumented"""

    zyww: typing.Any
    """ Undocumented"""

    zywx: typing.Any
    """ Undocumented"""

    zywy: typing.Any
    """ Undocumented"""

    zywz: typing.Any
    """ Undocumented"""

    zyx: typing.Any
    """ Undocumented"""

    zyxw: typing.Any
    """ Undocumented"""

    zyxx: typing.Any
    """ Undocumented"""

    zyxy: typing.Any
    """ Undocumented"""

    zyxz: typing.Any
    """ Undocumented"""

    zyy: typing.Any
    """ Undocumented"""

    zyyw: typing.Any
    """ Undocumented"""

    zyyx: typing.Any
    """ Undocumented"""

    zyyy: typing.Any
    """ Undocumented"""

    zyyz: typing.Any
    """ Undocumented"""

    zyz: typing.Any
    """ Undocumented"""

    zyzw: typing.Any
    """ Undocumented"""

    zyzx: typing.Any
    """ Undocumented"""

    zyzy: typing.Any
    """ Undocumented"""

    zyzz: typing.Any
    """ Undocumented"""

    zz: typing.Any
    """ Undocumented"""

    zzw: typing.Any
    """ Undocumented"""

    zzww: typing.Any
    """ Undocumented"""

    zzwx: typing.Any
    """ Undocumented"""

    zzwy: typing.Any
    """ Undocumented"""

    zzwz: typing.Any
    """ Undocumented"""

    zzx: typing.Any
    """ Undocumented"""

    zzxw: typing.Any
    """ Undocumented"""

    zzxx: typing.Any
    """ Undocumented"""

    zzxy: typing.Any
    """ Undocumented"""

    zzxz: typing.Any
    """ Undocumented"""

    zzy: typing.Any
    """ Undocumented"""

    zzyw: typing.Any
    """ Undocumented"""

    zzyx: typing.Any
    """ Undocumented"""

    zzyy: typing.Any
    """ Undocumented"""

    zzyz: typing.Any
    """ Undocumented"""

    zzz: typing.Any
    """ Undocumented"""

    zzzw: typing.Any
    """ Undocumented"""

    zzzx: typing.Any
    """ Undocumented"""

    zzzy: typing.Any
    """ Undocumented"""

    zzzz: typing.Any
    """ Undocumented"""

    @classmethod
    def Fill(cls, size: int, fill: float = 0.0):
        """Create a vector of length size with all values set to fill.

        :param size: The length of the vector to be created.
        :type size: int
        :param fill: The value used to fill the vector.
        :type fill: float
        """

    @classmethod
    def Linspace(cls, start: int, stop: int, size: int):
        """Create a vector of the specified size which is filled with linearly spaced values between start and stop values.

        :param start: The start of the range used to fill the vector.
        :type start: int
        :param stop: The end of the range used to fill the vector.
        :type stop: int
        :param size: The size of the vector to be created.
        :type size: int
        """

    @classmethod
    def Range(cls, start: int = 0, stop: int = -1, step: int = 1):
        """Create a filled with a range of values.

        :param start: The start of the range used to fill the vector.
        :type start: int
        :param stop: The end of the range used to fill the vector.
        :type stop: int
        :param step: The step between successive values in the vector.
        :type step: int
        """

    @classmethod
    def Repeat(cls, vector, size: int):
        """Create a vector by repeating the values in vector until the required size is reached.

        :param vector:
        :param size: The size of the vector to be created.
        :type size: int
        """

    def angle(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        fallback: typing.Any | None = None,
    ) -> float:
        """Return the angle between two vectors.

                :param other: another vector to compare the angle with
                :type other: collections.abc.Sequence[float] | typing_extensions.Self
                :param fallback: return this when the angle can't be calculated (zero length vector),
        (instead of raising a `ValueError`).
                :type fallback: typing.Any | None
                :return: angle in radians or fallback when given
                :rtype: float
        """

    def angle_signed(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        fallback: typing.Any,
    ) -> float:
        """Return the signed angle between two 2D vectors (clockwise is positive).

                :param other: another vector to compare the angle with
                :type other: collections.abc.Sequence[float] | typing_extensions.Self
                :param fallback: return this when the angle can't be calculated (zero length vector),
        (instead of raising a `ValueError`).
                :type fallback: typing.Any
                :return: angle in radians or fallback when given
                :rtype: float
        """

    def copy(self) -> typing_extensions.Self:
        """Returns a copy of this vector.

        :return: A copy of the vector.
        :rtype: typing_extensions.Self
        """

    def cross(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """Return the cross product of this vector and another.

        :param other: The other vector to perform the cross product with.
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return: The cross product.
        :rtype: typing_extensions.Self
        """

    def dot(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """Return the dot product of this vector and another.

        :param other: The other vector to perform the dot product with.
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return: The dot product.
        :rtype: typing_extensions.Self
        """

    def freeze(self) -> typing_extensions.Self:
        """Make this object immutable.After this the object can be hashed, used in dictionaries & sets.

        :return: An instance of this object.
        :rtype: typing_extensions.Self
        """

    def lerp(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        factor: float,
    ) -> typing_extensions.Self:
        """Returns the interpolation of two vectors.

        :param other: value to interpolate with.
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :param factor: The interpolation value in [0.0, 1.0].
        :type factor: float
        :return: The interpolated vector.
        :rtype: typing_extensions.Self
        """

    def negate(self):
        """Set all values to their negative."""

    def normalize(self):
        """Normalize the vector, making the length of the vector always 1.0."""

    def normalized(self) -> typing_extensions.Self:
        """Return a new, normalized vector.

        :return: a normalized copy of the vector
        :rtype: typing_extensions.Self
        """

    def orthogonal(self) -> typing_extensions.Self:
        """Return a perpendicular vector.

        :return: a new vector 90 degrees from this vector.
        :rtype: typing_extensions.Self
        """

    def project(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """Return the projection of this vector onto the other.

        :param other: second vector.
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return: the parallel projection vector
        :rtype: typing_extensions.Self
        """

    def reflect(
        self, mirror: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """Return the reflection vector from the mirror argument.

        :param mirror: This vector could be a normal from the reflecting surface.
        :type mirror: collections.abc.Sequence[float] | typing_extensions.Self
        :return: The reflected vector matching the size of this vector.
        :rtype: typing_extensions.Self
        """

    def resize(self, size=3):
        """Resize the vector to have size number of elements.

        :param size:
        """

    def resize_2d(self):
        """Resize the vector to 2D  (x, y)."""

    def resize_3d(self):
        """Resize the vector to 3D  (x, y, z)."""

    def resize_4d(self):
        """Resize the vector to 4D (x, y, z, w)."""

    def resized(self, size=3) -> typing_extensions.Self:
        """Return a resized copy of the vector with size number of elements.

        :param size:
        :return: a new vector
        :rtype: typing_extensions.Self
        """

    def rotate(
        self,
        other: Euler
        | Matrix
        | Quaternion
        | collections.abc.Sequence[collections.abc.Sequence[float]]
        | collections.abc.Sequence[float],
    ):
        """Rotate the vector by a rotation value.

        :param other: rotation component of mathutils value
        :type other: Euler | Matrix | Quaternion | collections.abc.Sequence[collections.abc.Sequence[float]] | collections.abc.Sequence[float]
        """

    def rotation_difference(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> Quaternion:
        """Returns a quaternion representing the rotational difference between this
        vector and another.

                :param other: second vector.
                :type other: collections.abc.Sequence[float] | typing_extensions.Self
                :return: the rotational difference between the two vectors.
                :rtype: Quaternion
        """

    def slerp(
        self,
        other: collections.abc.Sequence[float] | typing_extensions.Self,
        factor: float,
        fallback: typing.Any | None = None,
    ) -> typing_extensions.Self:
        """Returns the interpolation of two non-zero vectors (spherical coordinates).

                :param other: value to interpolate with.
                :type other: collections.abc.Sequence[float] | typing_extensions.Self
                :param factor: The interpolation value typically in [0.0, 1.0].
                :type factor: float
                :param fallback: return this when the vector can't be calculated (zero length vector or direct opposites),
        (instead of raising a `ValueError`).
                :type fallback: typing.Any | None
                :return: The interpolated vector.
                :rtype: typing_extensions.Self
        """

    def to_2d(self) -> typing_extensions.Self:
        """Return a 2d copy of the vector.

        :return: a new vector
        :rtype: typing_extensions.Self
        """

    def to_3d(self) -> typing_extensions.Self:
        """Return a 3d copy of the vector.

        :return: a new vector
        :rtype: typing_extensions.Self
        """

    def to_4d(self) -> typing_extensions.Self:
        """Return a 4d copy of the vector.

        :return: a new vector
        :rtype: typing_extensions.Self
        """

    def to_track_quat(self, track: str, up: str) -> Quaternion:
        """Return a quaternion rotation from the vector and the track and up axis.

        :param track: Track axis in ['X', 'Y', 'Z', '-X', '-Y', '-Z'].
        :type track: str
        :param up: Up axis in ['X', 'Y', 'Z'].
        :type up: str
        :return: rotation from the vector and the track and up axis.
        :rtype: Quaternion
        """

    def to_tuple(self, precision: int = -1) -> tuple:
        """Return this vector as a tuple with.

        :param precision: The number to round the value to in [-1, 21].
        :type precision: int
        :return: the values of the vector rounded by precision
        :rtype: tuple
        """

    def zero(self):
        """Set all values to zero."""

    def __init__(self, seq: collections.abc.Sequence[float] = (0.0, 0.0, 0.0)):
        """

        :param seq:
        :type seq: collections.abc.Sequence[float]
        """

    def __get__(self, instance, owner) -> typing_extensions.Self:
        """

        :param instance:
        :param owner:
        :return:
        :rtype: typing_extensions.Self
        """

    def __set__(
        self, instance, value: collections.abc.Sequence[float] | typing_extensions.Self
    ):
        """

        :param instance:
        :param value:
        :type value: collections.abc.Sequence[float] | typing_extensions.Self
        """

    def __len__(self) -> int:
        """

        :return:
        :rtype: int
        """

    @typing.overload
    def __getitem__(self, key: int) -> float:
        """

        :param key:
        :type key: int
        :return:
        :rtype: float
        """

    @typing.overload
    def __getitem__(self, key: slice) -> tuple[float, ...]:
        """

        :param key:
        :type key: slice
        :return:
        :rtype: tuple[float, ...]
        """

    @typing.overload
    def __setitem__(self, key: int, value: float):
        """

        :param key:
        :type key: int
        :param value:
        :type value: float
        """

    @typing.overload
    def __setitem__(self, key: slice, value: collections.abc.Iterable[float] | Vector):
        """

        :param key:
        :type key: slice
        :param value:
        :type value: collections.abc.Iterable[float] | Vector
        """

    def __neg__(self) -> typing_extensions.Self:
        """

        :return:
        :rtype: typing_extensions.Self
        """

    def __add__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __sub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    @typing.overload
    def __mul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    @typing.overload
    def __mul__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __truediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    @typing.overload
    def __matmul__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> float:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: float
        """

    @typing.overload
    def __matmul__(
        self, other: Matrix | collections.abc.Sequence[collections.abc.Sequence[float]]
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: Matrix | collections.abc.Sequence[collections.abc.Sequence[float]]
        :return:
        :rtype: typing_extensions.Self
        """

    def __radd__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __rsub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __rmul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    def __rtruediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    def __iadd__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __isub__(
        self, other: collections.abc.Sequence[float] | typing_extensions.Self
    ) -> typing_extensions.Self:
        """

        :param other:
        :type other: collections.abc.Sequence[float] | typing_extensions.Self
        :return:
        :rtype: typing_extensions.Self
        """

    def __imul__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """

    def __itruediv__(self, other: float) -> typing_extensions.Self:
        """

        :param other:
        :type other: float
        :return:
        :rtype: typing_extensions.Self
        """
