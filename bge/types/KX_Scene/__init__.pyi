import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus
import bge.types.KX_2DFilterManager
import bge.types.KX_Camera
import bge.types.KX_GameObject
import bge.types.KX_WorldInfo

class KX_Scene(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """An active scene that gives access to objects, cameras, lights and scene attributes.The activity culling stuff is supposed to disable logic bricks when their owner gets too far
    from the active camera.  It was taken from some code lurking at the back of KX_Scene - who knows
    what it does!@bug: All attributes are read only at the moment.
    """

    name: str
    """ The scene's name, (read-only).

    :type: str
    """

    objects: typing.Any
    """ A list of objects in the scene, (read-only)."""

    objectsInactive: typing.Any
    """ A list of objects on background layers (used for the addObject actuator), (read-only)."""

    lights: typing.Any
    """ A list of lights in the scene, (read-only)."""

    cameras: typing.Any
    """ A list of cameras in the scene, (read-only)."""

    texts: typing.Any
    """ A list of texts in the scene, (read-only)."""

    active_camera: bge.types.KX_Camera.KX_Camera
    """ The current active camera.

    :type: bge.types.KX_Camera.KX_Camera
    """

    overrideCullingCamera: bge.types.KX_Camera.KX_Camera | None
    """ The override camera used for scene culling, if set to None the culling is proceeded with the camera used to render.

    :type: bge.types.KX_Camera.KX_Camera | None
    """

    world: bge.types.KX_WorldInfo.KX_WorldInfo
    """ The current active world, (read-only).

    :type: bge.types.KX_WorldInfo.KX_WorldInfo
    """

    filterManager: bge.types.KX_2DFilterManager.KX_2DFilterManager
    """ The scene's 2D filter manager, (read-only).

    :type: bge.types.KX_2DFilterManager.KX_2DFilterManager
    """

    suspended: bool
    """ True if the scene is suspended, (read-only).

    :type: bool
    """

    activityCulling: bool
    """ True if the scene allow object activity culling.

    :type: bool
    """

    dbvt_culling: bool
    """ True when Dynamic Bounding box Volume Tree is set (read-only).

    :type: bool
    """

    pre_draw: list
    """ A list of callables to be run before the render step. The callbacks can take as argument the rendered camera.

    :type: list
    """

    post_draw: list
    """ A list of callables to be run after the render step.

    :type: list
    """

    pre_draw_setup: list
    """ A list of callables to be run before the drawing setup (i.e., before the model view and projection matrices are computed).
The callbacks can take as argument the rendered camera, the camera could be temporary in case of stereo rendering.

    :type: list
    """

    onRemove: list
    """ A list of callables to run when the scene is destroyed.

    :type: list
    """

    gravity: typing.Any
    """ The scene gravity using the world x, y and z axis."""

    def addObject(
        self,
        object: bge.types.KX_GameObject.KX_GameObject | str,
        reference: bge.types.KX_GameObject.KX_GameObject | str | None = "",
        time: float = 0.0,
    ) -> bge.types.KX_GameObject.KX_GameObject:
        """Adds an object to the scene like the Add Object Actuator would.

        :param object: The (name of the) object to add.
        :type object: bge.types.KX_GameObject.KX_GameObject | str
        :param reference: The (name of the) object which position, orientation, and scale to copy (optional), if the object to add is a light and there is not reference the light's layer will be the same that the active layer in the blender scene.
        :type reference: bge.types.KX_GameObject.KX_GameObject | str | None
        :param time: The lifetime of the added object, in frames (assumes one frame is 1/50 second). A time of 0.0 means the object will last forever (optional).
        :type time: float
        :return: The newly added object.
        :rtype: bge.types.KX_GameObject.KX_GameObject
        """

    def end(self):
        """Removes the scene from the game."""

    def restart(self):
        """Restarts the scene."""

    def replace(self, scene: str) -> bool:
        """Replaces this scene with another one.

        :param scene: The name of the scene to replace this scene with.
        :type scene: str
        :return: True if the scene exists and was scheduled for addition, False otherwise.
        :rtype: bool
        """

    def suspend(self):
        """Suspends this scene."""

    def resume(self):
        """Resume this scene."""

    def get(self, key, default=None):
        """Return the value matching key, or the default value if its not found.
        :return: The key value or a default.

                :param key:
                :param default:
        """

    def drawObstacleSimulation(self):
        """Draw debug visualization of obstacle simulation."""
