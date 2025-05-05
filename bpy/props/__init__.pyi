"""
This module defines properties to extend Blender's internal data. The result of these functions is used to assign properties to classes registered with Blender and can't be used directly.

[NOTE]
All parameters to these functions must be passed as keywords.


--------------------

Custom properties can be added to any subclass of an ID,
Bone and PoseBone.

These properties can be animated, accessed by the user interface and python
like Blender's existing properties.

```../examples/bpy.props.py```


--------------------

A common use of custom properties is for python based Operator
classes. Test this code by running it in the text editor, or by clicking the
button in the 3D Viewport's Tools panel. The latter will show the properties
in the Redo panel and allow you to change them.

```../examples/bpy.props.1.py```


--------------------

PropertyGroups can be used for collecting custom settings into one value
to avoid many individual settings mixed in together.

```../examples/bpy.props.2.py```


--------------------

Custom properties can be added to any subclass of an ID,
Bone and PoseBone.

```../examples/bpy.props.3.py```


--------------------

It can be useful to perform an action when a property is changed and can be
used to update other properties or synchronize with external data.

All properties define update functions except for CollectionProperty.

```../examples/bpy.props.4.py```


--------------------

Getter/setter functions can be used for boolean, int, float, string and enum properties.
If these callbacks are defined the property will not be stored in the ID properties
automatically. Instead, the get and set functions will be called when the property
is respectively read or written from the API.

```../examples/bpy.props.5.py```

[NOTE]
Typically this function doesn't need to be accessed directly.
Instead use del cls.attr



"""

import typing
import collections.abc
import typing_extensions
import bpy.types

def BoolProperty(
    *,
    name: str | None = "",
    description: str | None = "",
    default=False,
    options: set | None = {"ANIMATABLE"},
    tags: set | None = {},
    subtype: str | None = "NONE",
    update: typing.Any | None = None,
    get: typing.Any | None = None,
    set: typing.Any | None = None,
):
    """Returns a new boolean property definition.

        :param name: Name used in the user interface.
        :type name: str | None
        :param description: Text used for the tooltip and api documentation.
        :type description: str | None
        :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
        :type options: set | None
        :param tags: Enumerator of tags that are defined by parent class.
        :type tags: set | None
        :param subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
        :type subtype: str | None
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :type update: typing.Any | None
        :param get: Function to be called when this value is 'read',
    This function must take 1 value (self) and return the value of the property.
        :type get: typing.Any | None
        :param set: Function to be called when this value is 'written',
    This function must take 2 values (self, value) and return None.
        :type set: typing.Any | None
    """

def BoolVectorProperty(
    *,
    name: str | None = "",
    description: str | None = "",
    default: collections.abc.Sequence | None = (False, False, False),
    options: set | None = {"ANIMATABLE"},
    tags: set | None = {},
    subtype: str | None = "NONE",
    size: int | None = 3,
    update: typing.Any | None = None,
    get: typing.Any | None = None,
    set: typing.Any | None = None,
):
    """Returns a new vector boolean property definition.

        :param name: Name used in the user interface.
        :type name: str | None
        :param description: Text used for the tooltip and api documentation.
        :type description: str | None
        :param default: sequence of booleans the length of size.
        :type default: collections.abc.Sequence | None
        :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
        :type options: set | None
        :param tags: Enumerator of tags that are defined by parent class.
        :type tags: set | None
        :param subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'LAYER_MEMBER', 'NONE'].
        :type subtype: str | None
        :param size: Vector dimensions in [1, 32].
        :type size: int | None
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :type update: typing.Any | None
        :param get: Function to be called when this value is 'read',
    This function must take 1 value (self) and return the value of the property.
        :type get: typing.Any | None
        :param set: Function to be called when this value is 'written',
    This function must take 2 values (self, value) and return None.
        :type set: typing.Any | None
    """

def CollectionProperty(
    *,
    type=None,
    name: str | None = "",
    description: str | None = "",
    options: set | None = {"ANIMATABLE"},
    tags: set | None = {},
):
    """Returns a new collection property definition.

    :param type: A subclass of `bpy.types.PropertyGroup` or `bpy.types.ID`.
    :param name: Name used in the user interface.
    :type name: str | None
    :param description: Text used for the tooltip and api documentation.
    :type description: str | None
    :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
    :type options: set | None
    :param tags: Enumerator of tags that are defined by parent class.
    :type tags: set | None
    """

def EnumProperty(
    *,
    items: collections.abc.Iterable[
        tuple[str, str, str]
        | tuple[str, str, str, int]
        | tuple[str, str, str, str, int]
        | None
    ]
    | collections.abc.Callable[
        [typing.Any, bpy.types.Context | None],
        collections.abc.Iterable[
            tuple[str, str, str]
            | tuple[str, str, str, int]
            | tuple[str, str, str, str, int]
            | None
        ],
    ],
    name: str | None = "",
    description: str | None = "",
    default: set | str | None = None,
    options: set | None = {"ANIMATABLE"},
    tags: set | None = {},
    update: typing.Any | None = None,
    get: typing.Any | None = None,
    set: typing.Any | None = None,
):
    """Returns a new enumerator property definition.

        :param items: sequence of enum items formatted:
    [(identifier, name, description, icon, number), ...].

    The first three elements of the tuples are mandatory.

    identifier

    The identifier is used for Python access.

    name

    Name for the interace.

    description

    Used for documentation and tooltips.

    icon

    An icon string identifier or integer icon value
    (e.g. returned by `bpy.types.UILayout.icon`)

    number

    Unique value used as the identifier for this item (stored in file data).
    Use when the identifier may need to change. If the ENUM_FLAG option is used,
    the values are bitmasks and should be powers of two.

    When an item only contains 4 items they define (identifier, name, description, number).

    For dynamic values a callback can be passed which returns a list in
    the same format as the static list.
    This function must take 2 arguments (self, context), context may be None.

    There is a known bug with using a callback,
    Python must keep a reference to the strings returned or Blender will misbehave
    or even crash.
        :type items: collections.abc.Iterable[tuple[str, str, str] | tuple[str, str, str, int] | tuple[str, str, str, str, int] | None] | collections.abc.Callable[[typing.Any, bpy.types.Context | None], collections.abc.Iterable[tuple[str, str, str] | tuple[str, str, str, int] | tuple[str, str, str, str, int] | None]]
        :param name: Name used in the user interface.
        :type name: str | None
        :param description: Text used for the tooltip and api documentation.
        :type description: str | None
        :param default: The default value for this enum, a string from the identifiers used in items.
    If the ENUM_FLAG option is used this must be a set of such string identifiers instead.
    WARNING: It shall not be specified (or specified to its default None value) for dynamic enums
    (i.e. if a callback function is given as items parameter).
        :type default: set | str | None
        :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'ENUM_FLAG', 'LIBRARY_EDITABLE'].
        :type options: set | None
        :param tags: Enumerator of tags that are defined by parent class.
        :type tags: set | None
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :type update: typing.Any | None
        :param get: Function to be called when this value is 'read',
    This function must take 1 value (self) and return the value of the property.
        :type get: typing.Any | None
        :param set: Function to be called when this value is 'written',
    This function must take 2 values (self, value) and return None.
        :type set: typing.Any | None
    """

def FloatProperty(
    *,
    name: str | None = "",
    description: str | None = "",
    default=0.0,
    min: float | None = sys.float_info.min,
    max: float | None = sys.float_info.max,
    soft_min: float | None = sys.float_info.min,
    soft_max: float | None = sys.float_info.max,
    step: int | None = 3,
    precision: int | None = 2,
    options: set | None = {"ANIMATABLE"},
    tags: set | None = {},
    subtype: str | None = "NONE",
    unit: str | None = "NONE",
    update: typing.Any | None = None,
    get: typing.Any | None = None,
    set: typing.Any | None = None,
):
    """Returns a new float property definition.

        :param name: Name used in the user interface.
        :type name: str | None
        :param description: Text used for the tooltip and api documentation.
        :type description: str | None
        :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
        :type min: float | None
        :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
        :type max: float | None
        :param soft_min: Soft minimum (>= min), user won't be able to drag the widget below this value in the UI.
        :type soft_min: float | None
        :param soft_max: Soft maximum (<= max), user won't be able to drag the widget above this value in the UI.
        :type soft_max: float | None
        :param step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
        :type step: int | None
        :param precision: Maximum number of decimal digits to display, in [0, 6].
        :type precision: int | None
        :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
        :type options: set | None
        :param tags: Enumerator of tags that are defined by parent class.
        :type tags: set | None
        :param subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
        :type subtype: str | None
        :param unit: Enumerator in ['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'VELOCITY', 'ACCELERATION', 'MASS', 'CAMERA'].
        :type unit: str | None
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :type update: typing.Any | None
        :param get: Function to be called when this value is 'read',
    This function must take 1 value (self) and return the value of the property.
        :type get: typing.Any | None
        :param set: Function to be called when this value is 'written',
    This function must take 2 values (self, value) and return None.
        :type set: typing.Any | None
    """

def FloatVectorProperty(
    *,
    name: str | None = "",
    description: str | None = "",
    default: collections.abc.Sequence | None = (0.0, 0.0, 0.0),
    min: float | None = sys.float_info.min,
    max: float | None = sys.float_info.max,
    soft_min: float | None = sys.float_info.min,
    soft_max: float | None = sys.float_info.max,
    step: int | None = 3,
    precision: int | None = 2,
    options: set | None = {"ANIMATABLE"},
    tags: set | None = {},
    subtype: str | None = "NONE",
    unit: str | None = "NONE",
    size: int | None = 3,
    update: typing.Any | None = None,
    get: typing.Any | None = None,
    set: typing.Any | None = None,
):
    """Returns a new vector float property definition.

        :param name: Name used in the user interface.
        :type name: str | None
        :param description: Text used for the tooltip and api documentation.
        :type description: str | None
        :param default: sequence of floats the length of size.
        :type default: collections.abc.Sequence | None
        :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
        :type min: float | None
        :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
        :type max: float | None
        :param soft_min: Soft minimum (>= min), user won't be able to drag the widget below this value in the UI.
        :type soft_min: float | None
        :param soft_max: Soft maximum (<= max), user won't be able to drag the widget above this value in the UI.
        :type soft_max: float | None
        :param step: Step of increment/decrement in UI, in [1, 100], defaults to 3 (WARNING: actual value is /100).
        :type step: int | None
        :param precision: Maximum number of decimal digits to display, in [0, 6].
        :type precision: int | None
        :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
        :type options: set | None
        :param tags: Enumerator of tags that are defined by parent class.
        :type tags: set | None
        :param subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'LAYER_MEMBER', 'NONE'].
        :type subtype: str | None
        :param unit: Enumerator in ['NONE', 'LENGTH', 'AREA', 'VOLUME', 'ROTATION', 'TIME', 'VELOCITY', 'ACCELERATION', 'MASS', 'CAMERA'].
        :type unit: str | None
        :param size: Vector dimensions in [1, 32].
        :type size: int | None
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :type update: typing.Any | None
        :param get: Function to be called when this value is 'read',
    This function must take 1 value (self) and return the value of the property.
        :type get: typing.Any | None
        :param set: Function to be called when this value is 'written',
    This function must take 2 values (self, value) and return None.
        :type set: typing.Any | None
    """

def IntProperty(
    *,
    name: str | None = "",
    description: str | None = "",
    default=0,
    min: int | None = None,
    max: int | None = None,
    soft_min: int | None = None,
    soft_max: int | None = None,
    step: int | None = 1,
    options: set | None = {"ANIMATABLE"},
    tags: set | None = {},
    subtype: str | None = "NONE",
    update: typing.Any | None = None,
    get: typing.Any | None = None,
    set: typing.Any | None = None,
):
    """Returns a new int property definition.

        :param name: Name used in the user interface.
        :type name: str | None
        :param description: Text used for the tooltip and api documentation.
        :type description: str | None
        :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
        :type min: int | None
        :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
        :type max: int | None
        :param soft_min: Soft minimum (>= min), user won't be able to drag the widget below this value in the UI.
        :type soft_min: int | None
        :param soft_max: Soft maximum (<= max), user won't be able to drag the widget above this value in the UI.
        :type soft_max: int | None
        :param step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
        :type step: int | None
        :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
        :type options: set | None
        :param tags: Enumerator of tags that are defined by parent class.
        :type tags: set | None
        :param subtype: Enumerator in ['PIXEL', 'UNSIGNED', 'PERCENTAGE', 'FACTOR', 'ANGLE', 'TIME', 'DISTANCE', 'NONE'].
        :type subtype: str | None
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :type update: typing.Any | None
        :param get: Function to be called when this value is 'read',
    This function must take 1 value (self) and return the value of the property.
        :type get: typing.Any | None
        :param set: Function to be called when this value is 'written',
    This function must take 2 values (self, value) and return None.
        :type set: typing.Any | None
    """

def IntVectorProperty(
    *,
    name: str | None = "",
    description: str | None = "",
    default: collections.abc.Sequence | None = (0, 0, 0),
    min: int | None = None,
    max: int | None = None,
    soft_min: int | None = None,
    soft_max: int | None = None,
    step: int | None = 1,
    options: set | None = {"ANIMATABLE"},
    tags: set | None = {},
    subtype: str | None = "NONE",
    size: int | None = 3,
    update: typing.Any | None = None,
    get: typing.Any | None = None,
    set: typing.Any | None = None,
):
    """Returns a new vector int property definition.

        :param name: Name used in the user interface.
        :type name: str | None
        :param description: Text used for the tooltip and api documentation.
        :type description: str | None
        :param default: sequence of ints the length of size.
        :type default: collections.abc.Sequence | None
        :param min: Hard minimum, trying to assign a value below will silently assign this minimum instead.
        :type min: int | None
        :param max: Hard maximum, trying to assign a value above will silently assign this maximum instead.
        :type max: int | None
        :param soft_min: Soft minimum (>= min), user won't be able to drag the widget below this value in the UI.
        :type soft_min: int | None
        :param soft_max: Soft maximum (<= max), user won't be able to drag the widget above this value in the UI.
        :type soft_max: int | None
        :param step: Step of increment/decrement in UI, in [1, 100], defaults to 1 (WARNING: unused currently!).
        :type step: int | None
        :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
        :type options: set | None
        :param tags: Enumerator of tags that are defined by parent class.
        :type tags: set | None
        :param subtype: Enumerator in ['COLOR', 'TRANSLATION', 'DIRECTION', 'VELOCITY', 'ACCELERATION', 'MATRIX', 'EULER', 'QUATERNION', 'AXISANGLE', 'XYZ', 'COLOR_GAMMA', 'LAYER', 'LAYER_MEMBER', 'NONE'].
        :type subtype: str | None
        :param size: Vector dimensions in [1, 32].
        :type size: int | None
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :type update: typing.Any | None
        :param get: Function to be called when this value is 'read',
    This function must take 1 value (self) and return the value of the property.
        :type get: typing.Any | None
        :param set: Function to be called when this value is 'written',
    This function must take 2 values (self, value) and return None.
        :type set: typing.Any | None
    """

def PointerProperty(
    *,
    type=None,
    name: str | None = "",
    description: str | None = "",
    options: set | None = {"ANIMATABLE"},
    tags: set | None = {},
    poll: typing.Any | None = None,
    update: typing.Any | None = None,
):
    """Returns a new pointer property definition.

        :param type: A subclass of `bpy.types.PropertyGroup` or `bpy.types.ID`.
        :param name: Name used in the user interface.
        :type name: str | None
        :param description: Text used for the tooltip and api documentation.
        :type description: str | None
        :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
        :type options: set | None
        :param tags: Enumerator of tags that are defined by parent class.
        :type tags: set | None
        :param poll: function to be called to determine whether an item is valid for this property.
    The function must take 2 values (self, object) and return Bool.
        :type poll: typing.Any | None
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :type update: typing.Any | None
    """

def RemoveProperty(*, cls: typing.Any | None, attr: str | None):
    """Removes a dynamically defined property.

    :param cls: The class containing the property (must be a positional argument).
    :type cls: typing.Any | None
    :param attr: Property name (must be passed as a keyword).
    :type attr: str | None
    """

def StringProperty(
    *,
    name: str | None = "",
    description: str | None = "",
    default: str | None = "",
    maxlen: int | None = 0,
    options: set | None = {"ANIMATABLE"},
    tags: set | None = {},
    subtype: str | None = "NONE",
    update: typing.Any | None = None,
    get: typing.Any | None = None,
    set: typing.Any | None = None,
):
    """Returns a new string property definition.

        :param name: Name used in the user interface.
        :type name: str | None
        :param description: Text used for the tooltip and api documentation.
        :type description: str | None
        :param default: initializer string.
        :type default: str | None
        :param maxlen: maximum length of the string.
        :type maxlen: int | None
        :param options: Enumerator in ['HIDDEN', 'SKIP_SAVE', 'ANIMATABLE', 'LIBRARY_EDITABLE', 'PROPORTIONAL','TEXTEDIT_UPDATE'].
        :type options: set | None
        :param tags: Enumerator of tags that are defined by parent class.
        :type tags: set | None
        :param subtype: Enumerator in ['FILE_PATH', 'DIR_PATH', 'FILE_NAME', 'BYTE_STRING', 'PASSWORD', 'NONE'].
        :type subtype: str | None
        :param update: Function to be called when this value is modified,
    This function must take 2 values (self, context) and return None.
    Warning there are no safety checks to avoid infinite recursion.
        :type update: typing.Any | None
        :param get: Function to be called when this value is 'read',
    This function must take 1 value (self) and return the value of the property.
        :type get: typing.Any | None
        :param set: Function to be called when this value is 'written',
    This function must take 2 values (self, value) and return None.
        :type set: typing.Any | None
    """
