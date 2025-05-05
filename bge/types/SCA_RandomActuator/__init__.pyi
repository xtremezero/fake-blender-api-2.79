import typing
import collections.abc
import typing_extensions
import bge.types.SCA_IActuator

class SCA_RandomActuator(bge.types.SCA_IActuator.SCA_IActuator):
    """Random Actuator"""

    seed: int
    """ Seed of the random number generator.Equal seeds produce equal series. If the seed is 0, the generator will produce the same value on every call.

    :type: int
    """

    para1: float
    """ the first parameter of the active distribution.Refer to the documentation of the generator types for the meaning of this value.

    :type: float
    """

    para2: float
    """ the second parameter of the active distribution.Refer to the documentation of the generator types for the meaning of this value.

    :type: float
    """

    distribution: int
    """ Distribution type. (read-only). Can be one of `these constants <logic-random-distributions>`

    :type: int
    """

    propName: str
    """ the name of the property to set with the random value.If the generator and property types do not match, the assignment is ignored.

    :type: str
    """

    def setBoolConst(self, value: bool):
        """Sets this generator to produce a constant boolean value.

        :param value: The value to return.
        :type value: bool
        """

    def setBoolUniform(self):
        """Sets this generator to produce a uniform boolean distribution.The generator will generate True or False with 50% chance."""

    def setBoolBernouilli(self, value: float):
        """Sets this generator to produce a Bernouilli distribution.

                :param value: Specifies the proportion of False values to produce.

        0.0: Always generate True

        1.0: Always generate False
                :type value: float
        """

    def setIntConst(self, value: int):
        """Sets this generator to always produce the given value.

        :param value: the value this generator produces.
        :type value: int
        """

    def setIntUniform(self, lower_bound: int, upper_bound: int):
        """Sets this generator to produce a random value between the given lower and
        upper bounds (inclusive).

                :param lower_bound:
                :type lower_bound: int
                :param upper_bound:
                :type upper_bound: int
        """

    def setIntPoisson(self, value: float):
        """Generate a Poisson-distributed number.This performs a series of Bernouilli tests with parameter value.
        It returns the number of tries needed to achieve succes.

                :param value:
                :type value: float
        """

    def setFloatConst(self, value: float):
        """Always generate the given value.

        :param value:
        :type value: float
        """

    def setFloatUniform(self, lower_bound: float, upper_bound: float):
        """Generates a random float between lower_bound and upper_bound with a
        uniform distribution.

                :param lower_bound:
                :type lower_bound: float
                :param upper_bound:
                :type upper_bound: float
        """

    def setFloatNormal(self, mean: float, standard_deviation: float):
        """Generates a random float from the given normal distribution.

        :param mean: The mean (average) value of the generated numbers
        :type mean: float
        :param standard_deviation: The standard deviation of the generated numbers.
        :type standard_deviation: float
        """

    def setFloatNegativeExponential(self, half_life: float):
        """Generate negative-exponentially distributed numbers.The half-life 'time' is characterized by half_life.

        :param half_life:
        :type half_life: float
        """
