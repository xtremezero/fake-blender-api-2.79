"""
This module provides access to the audaspace audio library.


--------------------

This script shows how to use the classes: Device, Factory and
Handle.

```../examples/aud.py```

device()

Returns the application's Device.

return: The application's Device.
rtype: Device

"""

import typing
import collections.abc
import typing_extensions

class Device:
    """Device objects represent an audio output backend like OpenAL or SDL, but might also represent a file output or RAM buffer output.lock()Locks the device so that it's guaranteed, that no samples are read from the streams until `unlock` is called.
    This is useful if you want to do start/stop/pause/resume some sounds at the same time.play(factory, keep=False)Plays a factory.stopAll()Stops all playing and paused sounds.unlock()Unlocks the device after a lock call, see `lock` for details.
    """

    channels: typing.Any
    """ The channel count of the device."""

    distance_model: typing.Any
    """ The distance model of the device.`OpenAL documentation <https://www.openal.org/documentation>`__"""

    doppler_factor: typing.Any
    """ The doppler factor of the device.
This factor is a scaling factor for the velocity vectors in doppler calculation. So a value bigger than 1 will exaggerate the effect as it raises the velocity."""

    format: typing.Any
    """ The native sample format of the device."""

    listener_location: typing.Any
    """ The listeners's location in 3D space, a 3D tuple of floats."""

    listener_orientation: typing.Any
    """ The listener's orientation in 3D space as quaternion, a 4 float tuple."""

    listener_velocity: typing.Any
    """ The listener's velocity in 3D space, a 3D tuple of floats."""

    rate: typing.Any
    """ The sampling rate of the device in Hz."""

    speed_of_sound: typing.Any
    """ The speed of sound of the device.
The speed of sound in air is typically 343.3 m/s."""

    volume: typing.Any
    """ The overall volume of the device."""

class Factory:
    """Factory objects are immutable and represent a sound that can be played simultaneously multiple times. They are called factories because they create reader objects internally that are used for playback.file(filename)Creates a factory object of a sound file.sine(frequency, rate=48000)Creates a sine factory which plays a sine wave.buffer()Buffers a factory into RAM.
    This saves CPU usage needed for decoding and file access if the underlying factory reads from a file on the harddisk, but it consumes a lot of memory.delay(time)Delays by playing adding silence in front of the other factory's data.fadein(start, length)Fades a factory in by raising the volume linearly in the given time interval.fadeout(start, length)Fades a factory in by lowering the volume linearly in the given time interval.filter(b, a = (1))Filters a factory with the supplied IIR filter coefficients.
    Without the second parameter you'll get a FIR filter.
    If the first value of the a sequence is 0 it will be set to 1 automatically.
    If the first value of the a sequence is neither 0 nor 1, all filter coefficients will be scaled by this value so that it is 1 in the end, you don't have to scale yourself.highpass(frequency, Q=0.5)Creates a second order highpass filter based on the transfer function H(s) = s^2 / (s^2 + s/Q + 1)join(factory)Plays two factories in sequence.limit(start, end)Limits a factory within a specific start and end time.loop(count)Loops a factory.lowpass(frequency, Q=0.5)Creates a second order lowpass filter based on the transfer function H(s) = 1 / (s^2 + s/Q + 1)mix(factory)Mixes two factories.pingpong()Plays a factory forward and then backward.
    This is like joining a factory with its reverse.pitch(factor)Changes the pitch of a factory with a specific factor.reverse()Plays a factory reversed.square(threshold = 0)Makes a square wave out of an audio wave by setting all samples with a amplitude >= threshold to 1, all <= -threshold to -1 and all between to 0.volume(volume)Changes the volume of a factory.
    """

class Handle:
    """Handle objects are playback handles that can be used to control playback of a sound. If a sound is played back multiple times then there are as many handles.pause()Pauses playback.resume()Resumes playback.stop()Stops playback."""

    attenuation: typing.Any
    """ This factor is used for distance based attenuation of the source.:attr:`Device.distance_model`"""

    cone_angle_inner: typing.Any
    """ The opening angle of the inner cone of the source. If the cone values of a source are set there are two (audible) cones with the apex at the `location` of the source and with infinite height, heading in the direction of the source's `orientation`.
In the inner cone the volume is normal. Outside the outer cone the volume will be `cone_volume_outer` and in the area between the volume will be interpolated linearly."""

    cone_angle_outer: typing.Any
    """ The opening angle of the outer cone of the source.:attr:`cone_angle_inner`"""

    cone_volume_outer: typing.Any
    """ The volume outside the outer cone of the source.:attr:`cone_angle_inner`"""

    distance_maximum: typing.Any
    """ The maximum distance of the source.
If the listener is further away the source volume will be 0.:attr:`Device.distance_model`"""

    distance_reference: typing.Any
    """ The reference distance of the source.
At this distance the volume will be exactly `volume`.:attr:`Device.distance_model`"""

    keep: typing.Any
    """ Whether the sound should be kept paused in the device when its end is reached.
This can be used to seek the sound to some position and start playback again."""

    location: typing.Any
    """ The source's location in 3D space, a 3D tuple of floats."""

    loop_count: typing.Any
    """ The (remaining) loop count of the sound. A negative value indicates infinity."""

    orientation: typing.Any
    """ The source's orientation in 3D space as quaternion, a 4 float tuple."""

    pitch: typing.Any
    """ The pitch of the sound."""

    position: typing.Any
    """ The playback position of the sound in seconds."""

    relative: typing.Any
    """ Whether the source's location, velocity and orientation is relative or absolute to the listener."""

    status: typing.Any
    """ Whether the sound is playing, paused or stopped (=invalid)."""

    velocity: typing.Any
    """ The source's velocity in 3D space, a 3D tuple of floats."""

    volume: typing.Any
    """ The volume of the sound."""

    volume_maximum: typing.Any
    """ The maximum volume of the source.:attr:`Device.distance_model`"""

    volume_minimum: typing.Any
    """ The minimum volume of the source.:attr:`Device.distance_model`"""

class error: ...

AUD_DEVICE_JACK: typing.Any
""" constant value 3
"""

AUD_DEVICE_NULL: typing.Any
""" constant value 0
"""

AUD_DEVICE_OPENAL: typing.Any
""" constant value 1
"""

AUD_DEVICE_SDL: typing.Any
""" constant value 2
"""

AUD_DISTANCE_MODEL_EXPONENT: typing.Any
""" constant value 5
"""

AUD_DISTANCE_MODEL_EXPONENT_CLAMPED: typing.Any
""" constant value 6
"""

AUD_DISTANCE_MODEL_INVALID: typing.Any
""" constant value 0
"""

AUD_DISTANCE_MODEL_INVERSE: typing.Any
""" constant value 1
"""

AUD_DISTANCE_MODEL_INVERSE_CLAMPED: typing.Any
""" constant value 2
"""

AUD_DISTANCE_MODEL_LINEAR: typing.Any
""" constant value 3
"""

AUD_DISTANCE_MODEL_LINEAR_CLAMPED: typing.Any
""" constant value 4
"""

AUD_FORMAT_FLOAT32: typing.Any
""" constant value 36
"""

AUD_FORMAT_FLOAT64: typing.Any
""" constant value 40
"""

AUD_FORMAT_INVALID: typing.Any
""" constant value 0
"""

AUD_FORMAT_S16: typing.Any
""" constant value 18
"""

AUD_FORMAT_S24: typing.Any
""" constant value 19
"""

AUD_FORMAT_S32: typing.Any
""" constant value 20
"""

AUD_FORMAT_U8: typing.Any
""" constant value 1
"""

AUD_STATUS_INVALID: typing.Any
""" constant value 0
"""

AUD_STATUS_PAUSED: typing.Any
""" constant value 2
"""

AUD_STATUS_PLAYING: typing.Any
""" constant value 1
"""

AUD_STATUS_STOPPED: typing.Any
""" constant value 3
"""
