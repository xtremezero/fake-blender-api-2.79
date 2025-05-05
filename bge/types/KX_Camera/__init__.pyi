import typing
import collections.abc
import typing_extensions
import bge.types.KX_GameObject
import mathutils

class KX_Camera(bge.types.KX_GameObject.KX_GameObject):
    """A Camera object."""

    INSIDE: typing.Any
    """ See `sphereInsideFrustum` and `boxInsideFrustum`"""

    INTERSECT: typing.Any
    """ See `sphereInsideFrustum` and `boxInsideFrustum`"""

    OUTSIDE: typing.Any
    """ See `sphereInsideFrustum` and `boxInsideFrustum`"""

    lens: float
    """ The camera's lens value.

    :type: float
    """

    lodDistanceFactor: float
    """ The factor to multiply distance to camera to adjust levels of detail.
A float < 1.0f will make the distance to camera used to compute
levels of detail decrease.

    :type: float
    """

    fov: float
    """ The camera's field of view value.

    :type: float
    """

    ortho_scale: float
    """ The camera's view scale when in orthographic mode.

    :type: float
    """

    near: float
    """ The camera's near clip distance.

    :type: float
    """

    far: float
    """ The camera's far clip distance.

    :type: float
    """

    shift_x: float
    """ The camera's horizontal shift.

    :type: float
    """

    shift_y: float
    """ The camera's vertical shift.

    :type: float
    """

    perspective: bool
    """ True if this camera has a perspective transform, False for an orthographic projection.

    :type: bool
    """

    frustum_culling: bool
    """ True if this camera is frustum culling.

    :type: bool
    """

    activityCulling: bool
    """ True if this camera is used to compute object distance for object activity culling.

    :type: bool
    """

    projection_matrix: typing.Any
    """ This camera's 4x4 projection matrix."""

    projectionMatrixLeft: typing.Any
    """ This camera's 4x4 left eye projection matrix."""

    projectionMatrixRight: typing.Any
    """ This camera's 4x4 right eye projection matrix."""

    modelview_matrix: typing.Any
    """ This camera's 4x4 model view matrix. (read-only)."""

    camera_to_world: typing.Any
    """ This camera's camera to world transform. (read-only)."""

    world_to_camera: typing.Any
    """ This camera's world to camera transform. (read-only)."""

    useViewport: bool
    """ True when the camera is used as a viewport, set True to enable a viewport for this camera.

    :type: bool
    """

    def sphereInsideFrustum(self, centre, radius: float) -> int:
        """Tests the given sphere against the view frustum.

        :param centre: The centre of the sphere (in world coordinates.)
        :param radius: the radius of the sphere
        :type radius: float
        :return: `~bge.types.KX_Camera.INSIDE`, `~bge.types.KX_Camera.OUTSIDE` or `~bge.types.KX_Camera.INTERSECT`
        :rtype: int
        """

    def boxInsideFrustum(self, box):
        """Tests the given box against the view frustum.

        :param box: Eight (8) corner points of the box (in world coordinates.)
        :return: `~bge.types.KX_Camera.INSIDE`, `~bge.types.KX_Camera.OUTSIDE` or `~bge.types.KX_Camera.INTERSECT`
        """

    def pointInsideFrustum(
        self, point: collections.abc.Sequence[float] | mathutils.Vector
    ) -> bool:
        """Tests the given point against the view frustum.

        :param point: The point to test (in world coordinates.)
        :type point: collections.abc.Sequence[float] | mathutils.Vector
        :return: True if the given point is inside this camera's viewing frustum.
        :rtype: bool
        """

    def getCameraToWorld(self):
        """Returns the camera-to-world transform.

        :return: the camera-to-world transform matrix.
        """

    def getWorldToCamera(self):
        """Returns the world-to-camera transform.This returns the inverse matrix of getCameraToWorld().

        :return: the world-to-camera transform matrix.
        """

    def setOnTop(self):
        """Set this cameras viewport ontop of all other viewport."""

    def setViewport(self, left: int, bottom: int, right: int, top: int):
        """Sets the region of this viewport on the screen in pixels.Use `bge.render.getWindowHeight` and `bge.render.getWindowWidth` to calculate values relative to the entire display.

        :param left: left pixel coordinate of this viewport
        :type left: int
        :param bottom: bottom pixel coordinate of this viewport
        :type bottom: int
        :param right: right pixel coordinate of this viewport
        :type right: int
        :param top: top pixel coordinate of this viewport
        :type top: int
        """

    def getScreenPosition(
        self,
        object: bge.types.KX_GameObject.KX_GameObject
        | collections.abc.Sequence[float]
        | mathutils.Vector,
    ):
        """Gets the position of an object projected on screen space.

        :param object: object name or list [x, y, z]
        :type object: bge.types.KX_GameObject.KX_GameObject | collections.abc.Sequence[float] | mathutils.Vector
        :return: the object's position in screen coordinates.
        """

    def getScreenVect(
        self, x: float, y: float
    ) -> collections.abc.Sequence[float] | mathutils.Vector:
        """Gets the vector from the camera position in the screen coordinate direction.

        :param x: X Axis
        :type x: float
        :param y: Y Axis
        :type y: float
        :return: The vector from screen coordinate.
        :rtype: collections.abc.Sequence[float] | mathutils.Vector
        """

    def getScreenRay(
        self, x: float, y: float, dist: float = inf, property: str | None = None
    ) -> bge.types.KX_GameObject.KX_GameObject:
        """Look towards a screen coordinate (x, y) and find first object hit within dist that matches prop.
        The ray is similar to KX_GameObject->rayCastTo.

                :param x: X Axis
                :type x: float
                :param y: Y Axis
                :type y: float
                :param dist: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
                :type dist: float
                :param property: property name that object must have; can be omitted => detect any object
                :type property: str | None
                :return: the first object hit or None if no object or object does not match prop
                :rtype: bge.types.KX_GameObject.KX_GameObject
        """
