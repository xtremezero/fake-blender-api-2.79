import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PropValue

class EXP_ListValue(bge.types.EXP_PropValue.EXP_PropValue):
    """This is a list like object used in the game engine internally that behaves similar to a python list in most ways.As well as the normal index lookup (val= clist[i]), EXP_ListValue supports string lookups (val= scene.objects["Cube"])Other operations such as len(clist), list(clist), clist[0:10] are also supported."""

    def append(self, val):
        """Add an item to the list (like pythons append)

        :param val:
        """

    def count(self, val) -> int:
        """Count the number of instances of a value in the list.

        :param val:
        :return: number of instances
        :rtype: int
        """

    def index(self, val) -> int:
        """Return the index of a value in the list.

        :param val:
        :return: The index of the value in the list.
        :rtype: int
        """

    def reverse(self):
        """Reverse the order of the list."""

    def get(self, key, default=None):
        """Return the value matching key, or the default value if its not found.

        :param key:
        :param default:
        :return: The key value or a default.
        """

    def filter(self, name, prop):
        """Return a list of items with name matching name regex and with a property matching prop regex.
        If name is empty every items are checked, if prop is empty no property check is proceeded.

                :param name:
                :param prop:
                :return: The list of matching items.
        """

    def from_id(self, id):
        """This is a funtion especially for the game engine to return a value with a spesific id.Since object names are not always unique, the id of an object can be used to get an object from the EXP_ValueList.Example:Where myObID is an int or long from the id function.This has the advantage that you can store the id in places you could not store a gameObject.

        :param id:
        """
