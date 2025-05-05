"""
This module has a similar scope to os.path, containing utility
functions for dealing with paths in Blender.

"""

import typing
import collections.abc
import typing_extensions
import bpy.types

def abspath(
    path, start: bytes | str | None = None, library: bpy.types.Library | None = None
):
    """Returns the absolute path relative to the current blend file
    using the "//" prefix.

        :param start: Relative to this path,
    when not set the current filename is used.
        :type start: bytes | str | None
        :param library: The library this path is from. This is only included for
    convenience, when the library is not None its path replaces start.
        :type library: bpy.types.Library | None
    """

def basename(path):
    """Equivalent to os.path.basename, but skips a "//" prefix.Use for Windows compatibility."""

def clean_name(name, replace="_"):
    """Returns a name with characters replaced that
    may cause problems under various circumstances,
    such as writing to a file.
    All characters besides A-Z/a-z, 0-9 are replaced with "_"
    or the replace argument if defined.

    """

def display_name(name):
    """Creates a display string from name to be used menus and the user interface.
    Capitalize the first letter in all lowercase names,
    mixed case names are kept as is. Intended for use with
    filenames and module names.

    """

def display_name_from_filepath(name):
    """Returns the path stripped of directory and extension,
    ensured to be utf8 compatible.

    """

def display_name_to_filepath(name):
    """Performs the reverse of display_name using literal versions of characters
    which aren't supported in a filepath.

    """

def ensure_ext(filepath, ext: str, case_sensitive: bool = False):
    """Return the path with the extension added if it is not already set.

        :param ext: The extension to check for, can be a compound extension. Should
    start with a dot, such as '.blend' or '.tar.gz'.
        :type ext: str
        :param case_sensitive: Check for matching case when comparing extensions.
        :type case_sensitive: bool
    """

def is_subdir(path: bytes | str, directory):
    """Returns true if path in a subdirectory of directory.
    Both paths must be absolute.

        :param path: An absolute path.
        :type path: bytes | str
    """

def module_names(path: str, recursive: bool = False) -> list:
    """Return a list of modules which can be imported from path.

    :param path: a directory to scan.
    :type path: str
    :param recursive: Also return submodule names for packages.
    :type recursive: bool
    :return: a list of string pairs (module_name, module_file).
    :rtype: list
    """

def native_pathsep(path):
    """Replace the path separator with the systems native os.sep."""

def reduce_dirs(dirs: collections.abc.Sequence) -> list:
    """Given a sequence of directories, remove duplicates and
    any directories nested in one of the other paths.
    (Useful for recursive path searching).

        :param dirs: Sequence of directory paths.
        :type dirs: collections.abc.Sequence
        :return: A unique list of paths.
        :rtype: list
    """

def relpath(path: bytes | str, start: bytes | str | None = None):
    """Returns the path relative to the current blend file using the "//" prefix.

        :param path: An absolute path.
        :type path: bytes | str
        :param start: Relative to this path,
    when not set the current filename is used.
        :type start: bytes | str | None
    """

def resolve_ncase(path):
    """Resolve a case insensitive path on a case sensitive system,
    returning a string with the path if found else return the original path.

    """
