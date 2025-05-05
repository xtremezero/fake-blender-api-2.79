import typing
import collections.abc
import typing_extensions
import bge.types.EXP_Value
import bge.types.KX_GameObject

class KX_PythonComponent(bge.types.EXP_Value.EXP_Value):
    """Python component can be compared to python logic bricks with parameters.
    The python component is a script loaded in the UI, this script defined a component class by inheriting from `KX_PythonComponent`.
    This class must contain a dictionary of properties: `args` and two default functions: `start` and `update`.The script must have .py extension.The component properties are loaded from the `args` attribute from the UI at loading time.
    When the game start the function `start` is called with as arguments a dictionary of the properties' name and value.
    The `update` function is called every frames during the logic stage before running logics bricks,
    the goal of this function is to handle and process everything.The following component example moves and rotates the object when pressing the keys W, A, S and D.Since the components are loaded for the first time outside the bge, then `bge` is a fake module that contains only the class
    `KX_PythonComponent` to avoid importing all the bge modules.
    This behavior is safer but creates some issues at loading when the user want to use functions or attributes from the bge modules other
    than the `KX_PythonComponent` class. The way is to not call these functions at loading outside the bge. To detect it, the bge
    module contains the attribute `__component__` when it's imported outside the bge.The following component example add a "Cube" object at initialization and move it along x for each update. It shows that the user can
    use functions from scene and load the component outside the bge by setting global attributes in a condition at the beginning of the
    script.The property types supported are float, integer, boolean, string, set (for enumeration) and Vector 2D, 3D and 4D. The following example
    show all of these property types.
    """

    object: bge.types.KX_GameObject.KX_GameObject
    """ The object owner of the component.

    :type: bge.types.KX_GameObject.KX_GameObject
    """

    args: dict
    """ Dictionary of the component properties, the keys are string and the value can be: float, integer, Vector(2D/3D/4D), set, string.

    :type: dict
    """

    def start(self, args: dict):
        """Initialize the component.

        :param args: The dictionary of the properties' name and value.
        :type args: dict
        """

    def update(self):
        """Process the logic of the component."""
