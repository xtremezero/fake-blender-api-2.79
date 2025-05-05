import typing
import collections.abc
import typing_extensions
import bge.types.KX_BatchGroup
import bge.types.KX_BoundingBox
import bge.types.KX_CollisionContactPoint
import bge.types.KX_LodManager
import bge.types.KX_Mesh
import bge.types.KX_PolyProxy
import bge.types.KX_Scene
import bge.types.SCA_IObject
import bge.types.SCA_ISensor
import mathutils

class KX_GameObject(bge.types.SCA_IObject.SCA_IObject):
    """All game objects are derived from this class.Properties assigned to game objects are accessible as attributes of this class.KX_GameObject can be subclassed to extend functionality. For example:When subclassing objects other than empties and meshes, the specific type
    should be used - e.g. inherit from `BL_ArmatureObject` when the object
    to mutate is an armature.
    """

    name: str
    """ The object's name.

    :type: str
    """

    mass: float
    """ The object's mass

    :type: float
    """

    isSuspendDynamics: bool
    """ The object's dynamic state (read-only).:py:meth:`suspendDynamics` and :py:meth:`restoreDynamics` allow you to change the state.

    :type: bool
    """

    linearDamping: typing.Any
    """ The object's linear damping, also known as translational damping. Can be set simultaneously with angular damping using the `setDamping` method."""

    angularDamping: typing.Any
    """ The object's angular damping, also known as rotationation damping. Can be set simultaneously with linear damping using the `setDamping` method."""

    linVelocityMin: float
    """ Enforces the object keeps moving at a minimum velocity.

    :type: float
    """

    linVelocityMax: float
    """ Clamp the maximum linear velocity to prevent objects moving beyond a set speed.

    :type: float
    """

    angularVelocityMin: typing.Any
    """ Enforces the object keeps rotating at a minimum velocity. A value of 0.0 disables this."""

    angularVelocityMax: typing.Any
    """ Clamp the maximum angular velocity to prevent objects rotating beyond a set speed.
A value of 0.0 disables clamping; it does not stop rotation."""

    localInertia: typing.Any
    """ the object's inertia vector in local coordinates. Read only."""

    parent: typing_extensions.Self | None
    """ The object's parent object. (read-only).

    :type: typing_extensions.Self | None
    """

    groupMembers: typing.Any
    """ Returns the list of group members if the object is a group object (dupli group instance), otherwise None is returned."""

    groupObject: typing_extensions.Self | None
    """ Returns the group object (dupli group instance) that the object belongs to or None if the object is not part of a group.

    :type: typing_extensions.Self | None
    """

    collisionGroup: typing.Any
    """ The object's collision group."""

    collisionMask: typing.Any
    """ The object's collision mask."""

    collisionCallbacks: typing.Any
    """ A list of functions to be called when a collision occurs.Callbacks should either accept one argument (object), or four
arguments (object, point, normal, points). For simplicity, per
colliding object the first collision point is reported in second
and third argument."""

    scene: bge.types.KX_Scene.KX_Scene | None
    """ The object's scene. (read-only).

    :type: bge.types.KX_Scene.KX_Scene | None
    """

    visible: bool
    """ visibility flag.

    :type: bool
    """

    layer: typing.Any
    """ The layer mask used for shadow and real-time cube map render."""

    cullingBox: bge.types.KX_BoundingBox.KX_BoundingBox
    """ The object's bounding volume box used for culling.

    :type: bge.types.KX_BoundingBox.KX_BoundingBox
    """

    culled: typing.Any
    """ Returns True if the object is culled, else False."""

    color: mathutils.Vector
    """ The object color of the object. [r, g, b, a]

    :type: mathutils.Vector
    """

    occlusion: bool
    """ occlusion capability flag.

    :type: bool
    """

    physicsCulling: bool
    """ True if the object suspends its physics depending on its nearest distance to any camera.

    :type: bool
    """

    logicCulling: bool
    """ True if the object suspends its logic and animation depending on its nearest distance to any camera.

    :type: bool
    """

    physicsCullingRadius: float
    """ Suspend object's physics if this radius is smaller than its nearest distance to any camera
and `physicsCulling` set to True.

    :type: float
    """

    logicCullingRadius: float
    """ Suspend object's logic and animation if this radius is smaller than its nearest distance to any camera
and `logicCulling` set to True.

    :type: float
    """

    position: mathutils.Vector
    """ The object's position. [x, y, z] On write: local position, on read: world positionuse :data:`localPosition` and :data:`worldPosition`.

    :type: mathutils.Vector
    """

    orientation: mathutils.Matrix
    """ The object's orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector. On write: local orientation, on read: world orientationuse :data:`localOrientation` and :data:`worldOrientation`.

    :type: mathutils.Matrix
    """

    scaling: mathutils.Vector
    """ The object's scaling factor. [sx, sy, sz] On write: local scaling, on read: world scalinguse :data:`localScale` and :data:`worldScale`.

    :type: mathutils.Vector
    """

    localOrientation: mathutils.Matrix
    """ The object's local orientation. 3x3 Matrix. You can also write a Quaternion or Euler vector.

    :type: mathutils.Matrix
    """

    worldOrientation: mathutils.Matrix
    """ The object's world orientation. 3x3 Matrix.

    :type: mathutils.Matrix
    """

    localScale: mathutils.Vector
    """ The object's local scaling factor. [sx, sy, sz]

    :type: mathutils.Vector
    """

    worldScale: mathutils.Vector
    """ The object's world scaling factor. [sx, sy, sz]

    :type: mathutils.Vector
    """

    localPosition: mathutils.Vector
    """ The object's local position. [x, y, z]

    :type: mathutils.Vector
    """

    worldPosition: mathutils.Vector
    """ The object's world position. [x, y, z]

    :type: mathutils.Vector
    """

    localTransform: mathutils.Matrix
    """ The object's local space transform matrix. 4x4 Matrix.

    :type: mathutils.Matrix
    """

    worldTransform: mathutils.Matrix
    """ The object's world space transform matrix. 4x4 Matrix.

    :type: mathutils.Matrix
    """

    localLinearVelocity: mathutils.Vector
    """ The object's local linear velocity. [x, y, z]

    :type: mathutils.Vector
    """

    worldLinearVelocity: mathutils.Vector
    """ The object's world linear velocity. [x, y, z]

    :type: mathutils.Vector
    """

    localAngularVelocity: mathutils.Vector
    """ The object's local angular velocity. [x, y, z]

    :type: mathutils.Vector
    """

    worldAngularVelocity: mathutils.Vector
    """ The object's world angular velocity. [x, y, z]

    :type: mathutils.Vector
    """

    gravity: mathutils.Vector
    """ The object's gravity. [x, y, z]

    :type: mathutils.Vector
    """

    timeOffset: float
    """ adjust the slowparent delay at runtime.

    :type: float
    """

    state: int
    """ the game object's state bitmask, using the first 30 bits, one bit must always be set.

    :type: int
    """

    meshes: list[bge.types.KX_Mesh.KX_Mesh]
    """ a list meshes for this object.

    :type: list[bge.types.KX_Mesh.KX_Mesh]
    """

    batchGroup: bge.types.KX_BatchGroup.KX_BatchGroup
    """ The object batch group containing the batched mesh.

    :type: bge.types.KX_BatchGroup.KX_BatchGroup
    """

    sensors: list
    """ a sequence of `SCA_ISensor` objects with string/index lookups and iterator support.

    :type: list
    """

    controllers: list[bge.types.SCA_ISensor.SCA_ISensor]
    """ a sequence of `SCA_IController` objects with string/index lookups and iterator support.

    :type: list[bge.types.SCA_ISensor.SCA_ISensor]
    """

    actuators: list
    """ a list of `SCA_IActuator` with string/index lookups and iterator support.

    :type: list
    """

    attrDict: dict
    """ get the objects internal python attribute dictionary for direct (faster) access.

    :type: dict
    """

    components: typing.Any
    """ All python components."""

    children: typing.Any
    """ direct children of this object, (read-only)."""

    childrenRecursive: typing.Any
    """ all children of this object including children's children, (read-only)."""

    life: float
    """ The number of frames until the object ends, assumes one frame is 1/50 second (read-only).

    :type: float
    """

    debug: bool
    """ If true, the object's debug properties will be displayed on screen.

    :type: bool
    """

    debugRecursive: bool
    """ If true, the object's and children's debug properties will be displayed on screen.

    :type: bool
    """

    currentLodLevel: int
    """ The index of the level of detail (LOD) currently used by this object (read-only).

    :type: int
    """

    lodManager: bge.types.KX_LodManager.KX_LodManager
    """ Return the lod manager of this object.
Needed to access to lod manager to set attributes of levels of detail of this object.
The lod manager is shared between instance objects and can be changed to use the lod levels of an other object.
If the lod manager is set to None the object's mesh backs to the mesh of the previous first lod level.

    :type: bge.types.KX_LodManager.KX_LodManager
    """

    def endObject(self):
        """Delete this object, can be used in place of the EndObject Actuator.The actual removal of the object from the scene is delayed."""

    def replaceMesh(
        self, mesh: str, useDisplayMesh: bool = True, usePhysicsMesh: bool = False
    ):
        """Replace the mesh of this object with a new mesh. This works the same was as the actuator.

        :param mesh: mesh to replace or the meshes name.
        :type mesh: str
        :param useDisplayMesh: when enabled the display mesh will be replaced (optional argument).
        :type useDisplayMesh: bool
        :param usePhysicsMesh: when enabled the physics mesh will be replaced (optional argument).
        :type usePhysicsMesh: bool
        """

    def setVisible(self, visible: bool, recursive: bool | None = False):
        """Sets the game object's visible flag.

        :param visible: the visible state to set.
        :type visible: bool
        :param recursive: optional argument to set all childrens visibility flag too, defaults to False if no value passed.
        :type recursive: bool | None
        """

    def setOcclusion(self, occlusion: bool, recursive: bool | None = False):
        """Sets the game object's occlusion capability.

        :param occlusion: the state to set the occlusion to.
        :type occlusion: bool
        :param recursive: optional argument to set all childrens occlusion flag too, defaults to False if no value passed.
        :type recursive: bool | None
        """

    def alignAxisToVect(
        self,
        vect: collections.abc.Sequence[float] | mathutils.Vector,
        axis: int = 2,
        factor: float = 1.0,
    ):
        """Aligns any of the game object's axis along the given vector.

                :param vect: a vector to align the axis.
                :type vect: collections.abc.Sequence[float] | mathutils.Vector
                :param axis: The axis you want to align

        0: X axis

        1: Y axis

        2: Z axis
                :type axis: int
                :param factor: Only rotate a feaction of the distance to the target vector (0.0 - 1.0)
                :type factor: float
        """

    def getAxisVect(self, vect: collections.abc.Sequence[float] | mathutils.Vector):
        """Returns the axis vector rotates by the object's worldspace orientation.
        This is the equivalent of multiplying the vector by the orientation matrix.

                :param vect: a vector to align the axis.
                :type vect: collections.abc.Sequence[float] | mathutils.Vector
                :return: The vector in relation to the objects rotation.
        """

    def applyMovement(
        self, movement: collections.abc.Sequence[float] | mathutils.Vector, local
    ):
        """Sets the game object's movement.

                :param movement: movement vector.
                :type movement: collections.abc.Sequence[float] | mathutils.Vector
                :param local: False: get the "global" movement ie: relative to world orientation.

        True: get the "local" movement ie: relative to object orientation.

        Default to False if not passed.boolean
        """

    def applyRotation(
        self, rotation: collections.abc.Sequence[float] | mathutils.Vector, local
    ):
        """Sets the game object's rotation.

                :param rotation: rotation vector.
                :type rotation: collections.abc.Sequence[float] | mathutils.Vector
                :param local: False: get the "global" rotation ie: relative to world orientation.

        True: get the "local" rotation ie: relative to object orientation.

        Default to False if not passed.boolean
        """

    def applyForce(
        self, force: collections.abc.Sequence[float] | mathutils.Vector, local: bool
    ):
        """Sets the game object's force.This requires a dynamic object.

                :param force: force vector.
                :type force: collections.abc.Sequence[float] | mathutils.Vector
                :param local: False: get the "global" force ie: relative to world orientation.

        True: get the "local" force ie: relative to object orientation.

        Default to False if not passed.
                :type local: bool
        """

    def applyTorque(
        self, torque: collections.abc.Sequence[float] | mathutils.Vector, local: bool
    ):
        """Sets the game object's torque.This requires a dynamic object.

                :param torque: torque vector.
                :type torque: collections.abc.Sequence[float] | mathutils.Vector
                :param local: False: get the "global" torque ie: relative to world orientation.

        True: get the "local" torque ie: relative to object orientation.

        Default to False if not passed.
                :type local: bool
        """

    def getLinearVelocity(self, local: bool):
        """Gets the game object's linear velocity.This method returns the game object's velocity through it's center of mass, ie no angular velocity component.

                :param local: False: get the "global" velocity ie: relative to world orientation.

        True: get the "local" velocity ie: relative to object orientation.

        Default to False if not passed.
                :type local: bool
                :return: the object's linear velocity.
        """

    def setLinearVelocity(
        self, velocity: collections.abc.Sequence[float] | mathutils.Vector, local: bool
    ):
        """Sets the game object's linear velocity.This method sets game object's velocity through it's center of mass,
        ie no angular velocity component.This requires a dynamic object.

                :param velocity: linear velocity vector.
                :type velocity: collections.abc.Sequence[float] | mathutils.Vector
                :param local: False: get the "global" velocity ie: relative to world orientation.

        True: get the "local" velocity ie: relative to object orientation.

        Default to False if not passed.
                :type local: bool
        """

    def getAngularVelocity(self, local: bool):
        """Gets the game object's angular velocity.

                :param local: False: get the "global" velocity ie: relative to world orientation.

        True: get the "local" velocity ie: relative to object orientation.

        Default to False if not passed.
                :type local: bool
                :return: the object's angular velocity.
        """

    def setAngularVelocity(self, velocity: bool, local):
        """Sets the game object's angular velocity.This requires a dynamic object.

                :param velocity: angular velocity vector.
                :type velocity: bool
                :param local: False: get the "global" velocity ie: relative to world orientation.

        True: get the "local" velocity ie: relative to object orientation.

        Default to False if not passed.
        """

    def getVelocity(
        self, point: collections.abc.Sequence[float] | mathutils.Vector | None = []
    ):
        """Gets the game object's velocity at the specified point.Gets the game object's velocity at the specified point, including angular
        components.

                :param point: optional point to return the velocity for, in local coordinates, defaults to (0, 0, 0) if no value passed.
                :type point: collections.abc.Sequence[float] | mathutils.Vector | None
                :return: the velocity at the specified point.
        """

    def getReactionForce(self):
        """Gets the game object's reaction force.The reaction force is the force applied to this object over the last simulation timestep.
        This also includes impulses, eg from collisions.

                :return: the reaction force of this object.
        """

    def applyImpulse(
        self,
        point,
        impulse: collections.abc.Sequence[float] | mathutils.Vector,
        local: bool,
    ):
        """Applies an impulse to the game object.This will apply the specified impulse to the game object at the specified point.
        If point != position, applyImpulse will also change the object's angular momentum.
        Otherwise, only linear momentum will change.

                :param point: the point to apply the impulse to (in world or local coordinates)
                :param impulse: impulse vector.
                :type impulse: collections.abc.Sequence[float] | mathutils.Vector
                :param local: False: get the "global" impulse ie: relative to world coordinates with world orientation.

        True: get the "local" impulse ie: relative to local coordinates with object orientation.

        Default to False if not passed.
                :type local: bool
        """

    def setDamping(self, linear_damping, angular_damping):
        """Sets both the `linearDamping` and `angularDamping` simultaneously. This is more efficient than setting both properties individually.

        :param linear_damping: Linear ("translational") damping factor.
        :param angular_damping: Angular ("rotational") damping factor.
        """

    def suspendPhysics(self, freeConstraints: bool):
        """Suspends physics for this object.

                :param freeConstraints: When set to True physics constraints used by the object are deleted.
        Else when False (the default) constraints are restored when restoring physics.
                :type freeConstraints: bool
        """

    def restorePhysics(self):
        """Resumes physics for this object. Also reinstates collisions."""

    def suspendDynamics(self, ghost: bool):
        """Suspends dynamics physics for this object.:py:attr:`isSuspendDynamics` allows you to inspect whether the object is in a suspended state.

                :param ghost: When set to True, collisions with the object will be ignored, similar to the "ghost" checkbox in
        Blender. When False (the default), the object becomes static but still collide with other objects.
                :type ghost: bool
        """

    def restoreDynamics(self):
        """Resumes dynamics physics for this object. Also reinstates collisions; the object will no longer be a ghost."""

    def enableRigidBody(self):
        """Enables rigid body physics for this object.Rigid body physics allows the object to roll on collisions."""

    def disableRigidBody(self):
        """Disables rigid body physics for this object."""

    def setParent(
        self, parent: typing_extensions.Self, compound: bool = True, ghost: bool = True
    ):
        """Sets this object's parent.
        Control the shape status with the optional compound and ghost parameters:In that case you can control if it should be ghost or not:

                :param parent: new parent object.
                :type parent: typing_extensions.Self
                :param compound: whether the shape should be added to the parent compound shape.

        True: the object shape should be added to the parent compound shape.

        False: the object should keep its individual shape.
                :type compound: bool
                :param ghost: whether the object should be ghost while parented.

        True: if the object should be made ghost while parented.

        False: if the object should be solid while parented.
                :type ghost: bool
        """

    def removeParent(self):
        """Removes this objects parent."""

    def getPhysicsId(self):
        """Returns the user data object associated with this game object's physics controller."""

    def getPropertyNames(self) -> list:
        """Gets a list of all property names.

        :return: All property names for this object.
        :rtype: list
        """

    def getDistanceTo(self, other: typing_extensions.Self) -> float:
        """

        :param other: a point or another `KX_GameObject` to measure the distance to.
        :type other: typing_extensions.Self
        :return: distance to another object or point.
        :rtype: float
        """

    def getVectTo(self, other: typing_extensions.Self):
        """Returns the vector and the distance to another object or point.
        The vector is normalized unless the distance is 0, in which a zero length vector is returned.

                :param other: a point or another `KX_GameObject` to get the vector and distance to.
                :type other: typing_extensions.Self
                :return: (distance, globalVector(3), localVector(3))
        """

    def rayCastTo(
        self, other: typing_extensions.Self, dist: float = 0, prop: str = ""
    ) -> typing_extensions.Self:
        """Look towards another point/object and find first object hit within dist that matches prop.The ray is always casted from the center of the object, ignoring the object itself.
        The ray is casted towards the center of another object or an explicit [x, y, z] point.
        Use rayCast() if you need to retrieve the hit point

                :param other: [x, y, z] or object towards which the ray is casted
                :type other: typing_extensions.Self
                :param dist: max distance to look (can be negative => look behind); 0 or omitted => detect up to other
                :type dist: float
                :param prop: property name that object must have; can be omitted => detect any object
                :type prop: str
                :return: the first object hit or None if no object or object does not match prop
                :rtype: typing_extensions.Self
        """

    def rayCast(
        self,
        objto: typing_extensions.Self,
        objfrom: typing_extensions.Self | None = None,
        dist: float = 0,
        prop: str = "",
        face: int = False,
        xray: int = False,
        poly: int = 0,
        mask=65535,
    ) -> bge.types.KX_PolyProxy.KX_PolyProxy:
        """Look from a point/object to another point/object and find first object hit within dist that matches prop.
        if poly is 0, returns a 3-tuple with object reference, hit point and hit normal or (None, None, None) if no hit.
        if poly is 1, returns a 4-tuple with in addition a `KX_PolyProxy` as 4th element.
        if poly is 2, returns a 5-tuple with in addition a 2D vector with the UV mapping of the hit point as 5th element.The face parameter determines the orientation of the normal.The ray has X-Ray capability if xray parameter is 1, otherwise the first object hit (other than self object) stops the ray.
        The prop and xray parameters interact as follow.The `KX_PolyProxy` 4th element of the return tuple when poly=1 allows to retrieve information on the polygon hit by the ray.
        If there is no hit or the hit object is not a static mesh, None is returned as 4th element.The ray ignores collision-free objects and faces that dont have the collision flag enabled, you can however use ghost objects.

                :param objto: [x, y, z] or object to which the ray is casted
                :type objto: typing_extensions.Self
                :param objfrom: [x, y, z] or object from which the ray is casted; None or omitted => use self object center
                :type objfrom: typing_extensions.Self | None
                :param dist: max distance to look (can be negative => look behind); 0 or omitted => detect up to to
                :type dist: float
                :param prop: property name that object must have; can be omitted or "" => detect any object
                :type prop: str
                :param face: normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
                :type face: int
                :param xray: X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
                :type xray: int
                :param poly: polygon option: 0, 1 or 2 to return a 3-, 4- or 5-tuple with information on the face hit.

        0 or omitted: return value is a 3-tuple (object, hitpoint, hitnormal) or (None, None, None) if no hit

        1: return value is a 4-tuple and the 4th element is a `KX_PolyProxy` or None if no hit or the object doesn't use a mesh collision shape.

        2: return value is a 5-tuple and the 5th element is a 2-tuple (u, v) with the UV mapping of the hit point or None if no hit, or the object doesn't use a mesh collision shape, or doesn't have a UV mapping.
                :type poly: int
                :param mask: collision mask: The collision mask (16 layers mapped to a 16-bit integer) is combined with each object's collision group, to hit only a subset of the objects in the scene. Only those objects for which collisionGroup & mask is true can be hit.
                :return: (object, hitpoint, hitnormal) or (object, hitpoint, hitnormal, polygon) or (object, hitpoint, hitnormal, polygon, hituv).

        object, hitpoint and hitnormal are None if no hit.

        polygon is valid only if the object is valid and is a static object, a dynamic object using mesh collision shape or a soft body object, otherwise it is None

        hituv is valid only if polygon is valid and the object has a UV mapping, otherwise it is None
                :rtype: bge.types.KX_PolyProxy.KX_PolyProxy
        """

    def collide(
        self, obj: str | typing_extensions.Self
    ) -> list[bge.types.KX_CollisionContactPoint.KX_CollisionContactPoint]:
        """Test if this object collides object `obj`.

                :param obj: the object to test collision with
                :type obj: str | typing_extensions.Self
                :return: (collide, points)

        collide, True if this object collides object `obj`

        points, contact point data of the collision or None
                :rtype: list[bge.types.KX_CollisionContactPoint.KX_CollisionContactPoint]
        """

    def setCollisionMargin(self, margin: float):
        """Set the objects collision margin.

        :param margin: the collision margin distance in blender units.
        :type margin: float
        """

    def sendMessage(self, subject: str, body: str = "", to: str = ""):
        """Sends a message.

        :param subject: The subject of the message
        :type subject: str
        :param body: The body of the message (optional)
        :type body: str
        :param to: The name of the object to send the message to (optional)
        :type to: str
        """

    def reinstancePhysicsMesh(
        self,
        gameObject: str | typing_extensions.Self | None = "",
        meshObject: str | None = "",
        dupli: bool | None = False,
    ) -> bool:
        """Updates the physics system with the changed mesh.If no arguments are given the physics mesh will be re-created from the first mesh assigned to the game object.

        :param gameObject: optional argument, set the physics shape from this gameObjets mesh.
        :type gameObject: str | typing_extensions.Self | None
        :param meshObject: optional argument, set the physics shape from this mesh.
        :type meshObject: str | None
        :param dupli: optional argument, duplicate the physics shape.
        :type dupli: bool | None
        :return: True if reinstance succeeded, False if it failed.
        :rtype: bool
        """

    def replacePhysicsShape(self, gameObject: str | typing_extensions.Self) -> bool:
        """Replace the current physics shape.

        :param gameObject: set the physics shape from this gameObjets.
        :type gameObject: str | typing_extensions.Self
        :return: True if replace succeeded, False if it failed.
        :rtype: bool
        """

    def get(self, key, default):
        """Return the value matching key, or the default value if its not found.
        :arg key: the matching key
        :type key: string
        :arg default: optional default value is the key isn't matching, defaults to None if no value passed.
        :return: The key value or a default.

                :param key:
                :param default:
        """

    def playAction(
        self,
        name: str,
        start_frame,
        end_frame,
        layer: int = 0,
        priority: int = 0,
        blendin: float = 0,
        play_mode=KX_ACTION_MODE_PLAY,
        layer_weight: float = 0.0,
        ipo_flags=0,
        speed: float = 1.0,
        blend_mode=KX_ACTION_BLEND_BLEND,
    ):
        """Plays an action.

        :param name: the name of the action
        :type name: str
        :param start_frame:
        :param end_frame:
        :param layer: the layer the action will play in (actions in different layers are added/blended together)
        :type layer: int
        :param priority: only play this action if there isn't an action currently playing in this layer with a higher (lower number) priority
        :type priority: int
        :param blendin: the amount of blending between this animation and the previous one on this layer
        :type blendin: float
        :param play_mode: the play mode
        :param layer_weight: how much of the previous layer to use for blending
        :type layer_weight: float
        :param ipo_flags: flags for the old IPO behaviors (force, etc)
        :param speed: the playback speed of the action as a factor (1.0 = normal speed, 2.0 = 2x speed, etc)
        :type speed: float
        :param blend_mode: how to blend this layer with previous layers
        """

    def stopAction(self, layer: int):
        """Stop playing the action on the given layer.

        :param layer: The layer to stop playing, defaults to 0 if no value passed.
        :type layer: int
        """

    def getActionFrame(self, layer: int) -> float:
        """Gets the current frame of the action playing in the supplied layer.

        :param layer: The layer that you want to get the frame from, defaults to 0 if no value passed.
        :type layer: int
        :return: The current frame of the action
        :rtype: float
        """

    def getActionName(self, layer: int) -> str:
        """Gets the name of the current action playing in the supplied layer.

        :param layer: The layer that you want to get the action name from, defaults to 0 if no value passed.
        :type layer: int
        :return: The name of the current action
        :rtype: str
        """

    def setActionFrame(self, frame: float, layer: int):
        """Set the current frame of the action playing in the supplied layer.

        :param frame: The frame to set the action to
        :type frame: float
        :param layer: The layer where you want to set the frame, default to 0 if no value passed.
        :type layer: int
        """

    def isPlayingAction(self, layer: int) -> bool:
        """Checks to see if there is an action playing in the given layer.

        :param layer: The layer to check for a playing action, defaults to 0 if no value passed.
        :type layer: int
        :return: Whether or not the action is playing
        :rtype: bool
        """

    def addDebugProperty(self, name: str, debug: bool):
        """Adds a single debug property to the debug list.

        :param name: name of the property that added to the debug list.
        :type name: str
        :param debug: the debug state, default to True is no value passed.
        :type debug: bool
        """
