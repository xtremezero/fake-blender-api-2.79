"""
Module to access application values that remain unchanged during runtime.

"""

import typing
import collections.abc
import typing_extensions

has_joystick: bool
""" True if the BGE has been built with joystick support.
"""

has_physics: bool
""" True if the BGE has been built with physics support.
"""

has_texture_ffmpeg: bool
""" True if the BGE has been built with FFmpeg support,
enabling use of `~bge.texture.ImageFFmpeg` and `~bge.texture.VideoFFmpeg`.
"""

upbge_version: typing.Any
""" The UPBGE version as a tuple of 3 ints, eg. (0, 0, 3).
"""

upbge_version_string: str
""" The UPBGE version formatted as a string, eg. "0.0 (sub 3)".
"""

version: typing.Any
""" The Blender/BGE version as a tuple of 3 ints, eg. (2, 75, 1).
"""

version_char: str
""" The Blender/BGE version character (for minor releases).
"""

version_string: str
""" The Blender/BGE version formatted as a string, eg. "2.75 (sub 1)".
"""
