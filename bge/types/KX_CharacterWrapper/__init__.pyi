import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus
import mathutils

class KX_CharacterWrapper(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """A wrapper to expose character physics options."""

    onGround: bool
    """ Whether or not the character is on the ground. (read-only)

    :type: bool
    """

    gravity: float
    """ The gravity value used for the character.

    :type: float
    """

    fallSpeed: float
    """ The character falling speed.

    :type: float
    """

    maxJumps: int
    """ The maximum number of jumps a character can perform before having to touch the ground. By default this is set to 1. 2 allows for a double jump, etc.

    :type: int
    """

    jumpCount: int
    """ The current jump count. This can be used to have different logic for a single jump versus a double jump. For example, a different animation for the second jump.

    :type: int
    """

    jumpSpeed: float
    """ The character jumping speed.

    :type: float
    """

    maxSlope: float
    """ The maximum slope which the character can climb.

    :type: float
    """

    walkDirection: typing.Any
    """ The speed and direction the character is traveling in using world coordinates. This should be used instead of applyMovement() to properly move the character."""

    def jump(self):
        """The character jumps based on it's jump speed."""

    def setVelocity(
        self,
        velocity: collections.abc.Sequence[float] | mathutils.Vector,
        time: float,
        local: bool = False,
    ):
        """Sets the character's linear velocity for a given period.This method sets character's velocity through it's center of mass during a period.

                :param velocity: Linear velocity vector.
                :type velocity: collections.abc.Sequence[float] | mathutils.Vector
                :param time: Period while applying linear velocity.
                :type time: float
                :param local: False: you get the "global" velocity ie: relative to world orientation.

        True: you get the "local" velocity ie: relative to object orientation.
                :type local: bool
        """

    def reset(self):
        """Resets the character velocity and walk direction."""
