import typing
import collections.abc
import typing_extensions
import bge.types.SCA_ILogicBrick

class SCA_ISensor(bge.types.SCA_ILogicBrick.SCA_ILogicBrick):
    """Base class for all sensor logic bricks."""

    usePosPulseMode: bool
    """ Flag to turn positive pulse mode on and off.

    :type: bool
    """

    useNegPulseMode: bool
    """ Flag to turn negative pulse mode on and off.

    :type: bool
    """

    frequency: int
    """ The frequency for pulse mode sensors. (Deprecated: use SCA_ISensor.skippedTicks)

    :type: int
    """

    skippedTicks: int
    """ Number of logic ticks skipped between 2 active pulses

    :type: int
    """

    level: bool
    """ level Option whether to detect level or edge transition when entering a state.
It makes a difference only in case of logic state transition (state actuator).
A level detector will immediately generate a pulse, negative or positive
depending on the sensor condition, as soon as the state is activated.
A edge detector will wait for a state change before generating a pulse.
note: mutually exclusive with `tap`, enabling will disable `tap`.

    :type: bool
    """

    tap: bool
    """ When enabled only sensors that are just activated will send a positive event,
after this they will be detected as negative by the controllers.
This will make a key thats held act as if its only tapped for an instant.
note: mutually exclusive with `level`, enabling will disable `level`.

    :type: bool
    """

    invert: bool
    """ Flag to set if this sensor activates on positive or negative events.

    :type: bool
    """

    triggered: bool
    """ True if this sensor brick is in a positive state. (read-only).

    :type: bool
    """

    positive: bool
    """ True if this sensor brick is in a positive state. (read-only).

    :type: bool
    """

    pos_ticks: int
    """ The number of ticks since the last positive pulse (read-only).

    :type: int
    """

    neg_ticks: int
    """ The number of ticks since the last negative pulse (read-only).

    :type: int
    """

    status: int
    """ The status of the sensor (read-only): can be one of `these constants<sensor-status>`.

    :type: int
    """

    def reset(self):
        """Reset sensor internal state, effect depends on the type of sensor and settings.The sensor is put in its initial state as if it was just activated."""
