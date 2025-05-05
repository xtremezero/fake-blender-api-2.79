"""
This module contains utility functions specific to blender but
not associated with blenders internal data.

bpy.utils.previews.rst

bpy.utils.units.rst

:maxdepth: 1

"""

import typing
import collections.abc
import typing_extensions
from . import previews as previews
from . import units as units

def app_template_paths(subdir: str | None = None):
    """Returns valid application template paths.

    :param subdir: Optional subdir.
    :type subdir: str | None
    :return: app template paths.
    """

def blend_paths(
    absolute: bool = False, packed: bool = False, local: bool = False
) -> list[str]:
    """Returns a list of paths to external files referenced by the loaded .blend file.

    :param absolute: When true the paths returned are made absolute.
    :type absolute: bool
    :param packed: When true skip file paths for packed data.
    :type packed: bool
    :param local: When true skip linked library paths.
    :type local: bool
    :return: path list.
    :rtype: list[str]
    """

def escape_identifier(string: str) -> str:
    """Simple string escaping function used for animation paths.

    :param string: text
    :type string: str
    :return: The escaped string.
    :rtype: str
    """

def keyconfig_set(filepath, report=None): ...
def load_scripts(reload_scripts: bool = False, refresh_scripts: bool = False):
    """Load scripts and run each modules register function.

        :param reload_scripts: Causes all scripts to have their unregister method
    called before loading.
        :type reload_scripts: bool
        :param refresh_scripts: only load scripts which are not already loaded
    as modules.
        :type refresh_scripts: bool
    """

def make_rna_paths(struct_name: str, prop_name: str, enum_name: str):
    """Create RNA "paths" from given names.

        :param struct_name: Name of a RNA struct (like e.g. "Scene").
        :type struct_name: str
        :param prop_name: Name of a RNA struct's property.
        :type prop_name: str
        :param enum_name: Name of a RNA enum identifier.
        :type enum_name: str
        :return: A triple of three "RNA paths"
    (most_complete_path, "struct.prop", "struct.prop:'enum'").
    If no enum_name is given, the third element will always be void.
    """

def manual_map(): ...
def modules_from_path(path: str, loaded_modules: set) -> list:
    """Load all modules in a path and return them as a list.

        :param path: this path is scanned for scripts and packages.
        :type path: str
        :param loaded_modules: already loaded module names, files matching these
    names will be ignored.
        :type loaded_modules: set
        :return: all loaded modules.
        :rtype: list
    """

def preset_find(name, preset_path, display_name=False, ext=".py"): ...
def preset_paths(subdir: str) -> list:
    """Returns a list of paths for a specific preset.

    :param subdir: preset subdirectory (must not be an absolute path).
    :type subdir: str
    :return: script paths.
    :rtype: list
    """

def refresh_script_paths():
    """Run this after creating new script paths to update sys.path"""

def register_class(cls):
    """Register a subclass of a blender type in (`bpy.types.Panel`,
    `bpy.types.UIList`, `bpy.types.Menu`, `bpy.types.Header`,
    `bpy.types.Operator`, `bpy.types.KeyingSetInfo`,
    `bpy.types.RenderEngine`).If the class has a register class method it will be called
    before registration.

    """

def register_classes_factory(classes):
    """Utility function to create register and unregister functions
    which simply registers and unregisters a sequence of classes.

    """

def register_manual_map(manual_hook): ...
def register_module(module, verbose=False): ...
def register_submodule_factory(module_name: str, submodule_names: list[str]):
    """Utility function to create register and unregister functions
    which simply load submodules,
    calling their register & unregister functions.

        :param module_name: The module name, typically __name__.
        :type module_name: str
        :param submodule_names: List of submodule names to load and unload.
        :type submodule_names: list[str]
        :return: register and unregister functions.
    """

def resource_path(
    type: str, major: int = bpy.app.version[0], minor: str = bpy.app.version[1]
) -> str:
    """Return the base path for storing system files.

    :param type: string in ['USER', 'LOCAL', 'SYSTEM'].
    :type type: str
    :param major: major version, defaults to current.
    :type major: int
    :param minor: minor version, defaults to current.
    :type minor: str
    :return: the resource path (not necessarily existing).
    :rtype: str
    """

def script_path_pref():
    """returns the user preference or None"""

def script_path_user():
    """returns the env var and falls back to home dir or None"""

def script_paths(
    subdir: str | None = None,
    user_pref: bool = True,
    check_all: bool = False,
    use_user=True,
) -> list:
    """Returns a list of valid script paths.

        :param subdir: Optional subdir.
        :type subdir: str | None
        :param user_pref: Include the user preference script path.
        :type user_pref: bool
        :param check_all: Include local, user and system paths rather just the paths
    blender uses.
        :type check_all: bool
        :return: script paths.
        :rtype: list
    """

def smpte_from_frame(frame: int, fps=None, fps_base=None) -> str:
    """Returns an SMPTE formatted string from the frame:
    HH:MM:SS:FF.If fps and fps_base are not given the current scene is used.

        :param frame: frame number.
        :type frame: int
        :return: the frame string.
        :rtype: str
    """

def smpte_from_seconds(time: float, fps=None) -> str:
    """Returns an SMPTE formatted string from the time:
    HH:MM:SS:FF.If the fps is not given the current scene is used.

        :param time: time in seconds.
        :type time: float
        :return: the frame string.
        :rtype: str
    """

def time_from_frame(frame: int, fps=None, fps_base=None):
    """Returns the time from a frame number .If fps and fps_base are not given the current scene is used.

    :param frame: number.
    :type frame: int
    :return: the time in seconds.
    """

def time_to_frame(time, fps=None, fps_base=None) -> float:
    """Returns a float frame number from a time given in seconds or
    as a datetime.timedelta object.If fps and fps_base are not given the current scene is used.

        :param time: time in seconds.
        :return: the frame.
        :rtype: float
    """

def unregister_class(cls):
    """Unload the python class from blender.If the class has an unregister class method it will be called
    before unregistering.

    """

def unregister_manual_map(manual_hook): ...
def unregister_module(module, verbose=False): ...
def user_resource(resource_type, path="", create: bool = False) -> str:
    """Return a user resource path (normally from the users home directory).

        :param create: Treat the path as a directory and create
    it if its not existing.
        :type create: bool
        :return: a path.
        :rtype: str
    """
