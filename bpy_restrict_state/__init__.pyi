import typing
import collections.abc
import typing_extensions

class RestrictBlend:
    context: typing.Any
    data: typing.Any

class _RestrictContext:
    user_preferences: typing.Any
    window_manager: typing.Any

class _RestrictData: ...
