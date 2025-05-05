import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus

class BL_Shader(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """BL_Shader is a class used to compile and use custom shaders scripts. It supports vertex, fragment and geometry shader scripts.
    The shader is compiled with a generated header for the three shaders scripts.
    This header set the #version directive, so the user must not define his own #version.
    """

    enabled: bool
    """ Set shader enabled to use.

    :type: bool
    """

    objectCallbacks: typing.Any
    """ The list of python callbacks executed when the shader is used to render an object.
All the functions can expect as argument the object currently rendered."""

    bindCallbacks: typing.Any
    """ The list of python callbacks executed when the shader is begin used to render."""

    def setUniformfv(self, name: str, fList: list[float]):
        """Set a uniform with a list of float values

        :param name: the uniform name
        :type name: str
        :param fList: a list (2, 3 or 4 elements) of float values
        :type fList: list[float]
        """

    def delSource(self):
        """Clear the shader. Use this method before the source is changed with `setSource`."""

    def getFragmentProg(self) -> str:
        """Returns the fragment program.

        :return: The fragment program.
        :rtype: str
        """

    def getVertexProg(self) -> str:
        """Get the vertex program.

        :return: The vertex program.
        :rtype: str
        """

    def isValid(self) -> bool:
        """Check if the shader is valid.

        :return: True if the shader is valid
        :rtype: bool
        """

    def setAttrib(self, enum: int):
        """Set attribute location. (The parameter is ignored a.t.m. and the value of "tangent" is always used.)

        :param enum: attribute location value
        :type enum: int
        """

    def setSampler(self, name: str, index: int):
        """Set uniform texture sample index.

        :param name: Uniform name
        :type name: str
        :param index: Texture sample index.
        :type index: int
        """

    def setSource(self, vertexProgram: str, fragmentProgram: str, apply: bool):
        """Set the vertex and fragment programs

        :param vertexProgram: Vertex program
        :type vertexProgram: str
        :param fragmentProgram: Fragment program
        :type fragmentProgram: str
        :param apply: Enable the shader.
        :type apply: bool
        """

    def setSourceList(self, sources: dict, apply: bool):
        """Set the vertex, fragment and geometry shader programs.

                :param sources: Dictionary of all programs. The keys `vertex`, `fragment` and `geometry` represent shader programs of the same name.
        `geometry` is an optional program.
        This dictionary can be similar to:

        sources = {
            "vertex" : vertexProgram,
            "fragment" : fragmentProgram,
            "geometry" : geometryProgram
        }
                :type sources: dict
                :param apply: Enable the shader.
                :type apply: bool
        """

    def setUniform1f(self, name: str, fx: float):
        """Set a uniform with 1 float value.

        :param name: the uniform name
        :type name: str
        :param fx: Uniform value
        :type fx: float
        """

    def setUniform1i(self, name: str, ix: int):
        """Set a uniform with an integer value.

        :param name: the uniform name
        :type name: str
        :param ix: the uniform value
        :type ix: int
        """

    def setUniform2f(self, name: str, fx: float, fy: float):
        """Set a uniform with 2 float values

        :param name: the uniform name
        :type name: str
        :param fx: first float value
        :type fx: float
        :param fy: second float value
        :type fy: float
        """

    def setUniform2i(self, name: str, ix: int, iy: int):
        """Set a uniform with 2 integer values

        :param name: the uniform name
        :type name: str
        :param ix: first integer value
        :type ix: int
        :param iy: second integer value
        :type iy: int
        """

    def setUniform3f(self, name: str, fx: float, fy: float, fz: float):
        """Set a uniform with 3 float values.

        :param name: the uniform name
        :type name: str
        :param fx: first float value
        :type fx: float
        :param fy: second float value
        :type fy: float
        :param fz: third float value
        :type fz: float
        """

    def setUniform3i(self, name: str, ix: int, iy: int, iz: int):
        """Set a uniform with 3 integer values

        :param name: the uniform name
        :type name: str
        :param ix: first integer value
        :type ix: int
        :param iy: second integer value
        :type iy: int
        :param iz: third integer value
        :type iz: int
        """

    def setUniform4f(self, name: str, fx: float, fy: float, fz: float, fw: float):
        """Set a uniform with 4 float values.

        :param name: the uniform name
        :type name: str
        :param fx: first float value
        :type fx: float
        :param fy: second float value
        :type fy: float
        :param fz: third float value
        :type fz: float
        :param fw: fourth float value
        :type fw: float
        """

    def setUniform4i(self, name: str, ix: int, iy: int, iz: int, iw: int):
        """Set a uniform with 4 integer values

        :param name: the uniform name
        :type name: str
        :param ix: first integer value
        :type ix: int
        :param iy: second integer value
        :type iy: int
        :param iz: third integer value
        :type iz: int
        :param iw: fourth integer value
        :type iw: int
        """

    def setUniformDef(self, name: str, type: int):
        """Define a new uniform

        :param name: the uniform name
        :type name: str
        :param type: uniform type, one of `these constants <shader-defined-uniform>`
        :type type: int
        """

    def setUniformMatrix3(self, name: str, mat, transpose: bool):
        """Set a uniform with a 3x3 matrix value

        :param name: the uniform name
        :type name: str
        :param mat: A 3x3 matrix [[f, f, f], [f, f, f], [f, f, f]]
        :param transpose: set to True to transpose the matrix
        :type transpose: bool
        """

    def setUniformMatrix4(self, name: str, mat, transpose: bool):
        """Set a uniform with a 4x4 matrix value

        :param name: the uniform name
        :type name: str
        :param mat: A 4x4 matrix [[f, f, f, f], [f, f, f, f], [f, f, f, f], [f, f, f, f]]
        :param transpose: set to True to transpose the matrix
        :type transpose: bool
        """

    def setUniformiv(self, name: str, iList: list[int]):
        """Set a uniform with a list of integer values

        :param name: the uniform name
        :type name: str
        :param iList: a list (2, 3 or 4 elements) of integer values
        :type iList: list[int]
        """

    def setUniformEyef(self, name: str):
        """Set a uniform with a float value that reflects the eye being render in stereo mode:
        0.0 for the left eye, 0.5 for the right eye. In non stereo mode, the value of the uniform
        is fixed to 0.0. The typical use of this uniform is in stereo mode to sample stereo textures
        containing the left and right eye images in a top-bottom order.

                :param name: the uniform name
                :type name: str
        """

    def validate(self):
        """Validate the shader object."""
