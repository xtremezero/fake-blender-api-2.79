import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus
import bge.types.KX_GameObject

class KX_VehicleWrapper(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """KX_VehicleWrapperTODO - description"""

    rayMask: typing.Any
    """ Set ray cast mask."""

    def addWheel(
        self,
        wheel: bge.types.KX_GameObject.KX_GameObject,
        attachPos,
        downDir,
        axleDir,
        suspensionRestLength: float,
        wheelRadius: float,
        hasSteering: bool,
    ):
        """Add a wheel to the vehicle

        :param wheel: The object to use as a wheel.
        :type wheel: bge.types.KX_GameObject.KX_GameObject
        :param attachPos: The position to attach the wheel, relative to the chassis object center.
        :param downDir: The direction vector pointing down to where the vehicle should collide with the floor.
        :param axleDir: The axis the wheel rotates around, relative to the chassis.
        :param suspensionRestLength: The length of the suspension when no forces are being applied.
        :type suspensionRestLength: float
        :param wheelRadius: The radius of the wheel (half the diameter).
        :type wheelRadius: float
        :param hasSteering: True if the wheel should turn with steering, typically used in front wheels.
        :type hasSteering: bool
        """

    def applyBraking(self, force: float, wheelIndex: int):
        """Apply a braking force to the specified wheel

        :param force: the brake force
        :type force: float
        :param wheelIndex: index of the wheel where the force needs to be applied
        :type wheelIndex: int
        """

    def applyEngineForce(self, force: float, wheelIndex: int):
        """Apply an engine force to the specified wheel

        :param force: the engine force
        :type force: float
        :param wheelIndex: index of the wheel where the force needs to be applied
        :type wheelIndex: int
        """

    def getConstraintId(self) -> int:
        """Get the constraint ID

        :return: the constraint id
        :rtype: int
        """

    def getConstraintType(self) -> int:
        """Returns the constraint type.

        :return: constraint type
        :rtype: int
        """

    def getNumWheels(self) -> int:
        """Returns the number of wheels.

        :return: the number of wheels for this vehicle
        :rtype: int
        """

    def getWheelOrientationQuaternion(self, wheelIndex: int):
        """Returns the wheel orientation as a quaternion.

        :param wheelIndex: the wheel index
        :type wheelIndex: int
        :return: TODO Description
        """

    def getWheelPosition(self, wheelIndex: int) -> list:
        """Returns the position of the specified wheel

        :param wheelIndex: the wheel index
        :type wheelIndex: int
        :return: position vector
        :rtype: list
        """

    def getWheelRotation(self, wheelIndex: int) -> float:
        """Returns the rotation of the specified wheel

        :param wheelIndex: the wheel index
        :type wheelIndex: int
        :return: the wheel rotation
        :rtype: float
        """

    def setRollInfluence(self, rollInfluece: float, wheelIndex: int):
        """Set the specified wheel's roll influence.
        The higher the roll influence the more the vehicle will tend to roll over in corners.

                :param rollInfluece: the wheel roll influence
                :type rollInfluece: float
                :param wheelIndex: the wheel index
                :type wheelIndex: int
        """

    def setSteeringValue(self, steering: float, wheelIndex: int):
        """Set the specified wheel's steering

        :param steering: the wheel steering
        :type steering: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """

    def setSuspensionCompression(self, compression: float, wheelIndex: int):
        """Set the specified wheel's compression

        :param compression: the wheel compression
        :type compression: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """

    def setSuspensionDamping(self, damping: float, wheelIndex: int):
        """Set the specified wheel's damping

        :param damping: the wheel damping
        :type damping: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """

    def setSuspensionStiffness(self, stiffness: float, wheelIndex: int):
        """Set the specified wheel's stiffness

        :param stiffness: the wheel stiffness
        :type stiffness: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """

    def setTyreFriction(self, friction: float, wheelIndex: int):
        """Set the specified wheel's tyre friction

        :param friction: the tyre friction
        :type friction: float
        :param wheelIndex: the wheel index
        :type wheelIndex: int
        """
