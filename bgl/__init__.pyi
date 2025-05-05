"""
This module wraps OpenGL constants and functions, making them available from
within Blender Python.

The complete list can be retrieved from the module itself, by listing its
contents: dir(bgl).  A simple search on the web can point to more
than enough material to teach OpenGL programming, from books to many
collections of tutorials.

Here is a comprehensive list of books (non free).
The arcsynthesis tutorials
is one of the best resources to learn modern OpenGL and
g-truc
offers a set of extensive examples, including advanced features.

[NOTE]
You can use the Image type to load and set textures.
See Image.gl_load and Image.gl_load,
for example.

"""

import typing
import collections.abc
import typing_extensions

class Buffer:
    """The Buffer object is simply a block of memory that is delineated and initialized by the
    user. Many OpenGL functions return data to a C-style pointer, however, because this
    is not possible in python the Buffer object can be used to this end. Wherever pointer
    notation is used in the OpenGL functions the Buffer object can be used in it's bgl
    wrapper. In some instances the Buffer object will need to be initialized with the template
    parameter, while in other instances the user will want to create just a blank buffer
    which will be zeroed by default.
    """

    dimensions: typing.Any
    """ The number of dimensions of the Buffer."""

    def to_list(self):
        """The contents of the Buffer as a python list."""

    def __init__(self, type: int, dimensions, template=None):
        """This will create a new Buffer object for use with other bgl OpenGL commands.
        Only the type of argument to store in the buffer and the dimensions of the buffer
        are necessary. Buffers are zeroed by default unless a template is supplied, in
        which case the buffer is initialized to the template.

                :param type: The format to store data in. The type should be one of
        GL_BYTE, GL_SHORT, GL_INT, or GL_FLOAT.
                :type type: int
                :param dimensions: If the dimensions are specified as an int a linear array will
        be created for the buffer. If a sequence is passed for the dimensions, the buffer
        becomes n-Dimensional, where n is equal to the number of parameters passed in the
        sequence. Example: [256,2] is a two- dimensional buffer while [256,256,4] creates
        a three- dimensional buffer. You can think of each additional dimension as a sub-item
        of the dimension to the left. i.e. [10,2] is a 10 element array each with 2 sub-items.
        [(0,0), (0,1), (1,0), (1,1), (2,0), ...] etc.
                :param template: A sequence of matching dimensions which will be used to initialize
        the Buffer. If a template is not passed in all fields will be initialized to 0.
                :return: The newly created buffer as a PyObject.
        """

def glAccum(op: set[str], value: float):
    """Operate on the accumulation buffer.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glAccum.xml>`__

    :param op: The accumulation buffer operation.
    :type op: set[str]
    :param value: a value used in the accumulation buffer operation.
    :type value: float
    """

def glActiveTexture(texture: int):
    """Select active texture unit.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glActiveTexture.xml>`__

    :param texture: Constant in GL_TEXTURE0 0 - 8
    :type texture: int
    """

def glAlphaFunc(func: set[str], ref: float):
    """Specify the alpha test function.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glAlphaFunc.xml>`__

        :param func: Specifies the alpha comparison function.
        :type func: set[str]
        :param ref: The reference value that incoming alpha values are compared to.
    Clamped between 0 and 1.
        :type ref: float
    """

def glAreTexturesResident(n: int, textures: Buffer, residences: Buffer):
    """Determine if textures are loaded in texture memory`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glAreTexturesResident.xml>`__

        :param n: Specifies the number of textures to be queried.
        :type n: int
        :param textures: Specifies an array containing the names of the textures to be queried
        :type textures: Buffer
        :param residences: An array in which the texture residence status in returned.
    The residence status of a texture named by an element of textures is
    returned in the corresponding element of residences.
        :type residences: Buffer
    """

def glAttachShader(program: int, shader: int):
    """Attaches a shader object to a program object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glAttachShader.xml>`__

    :param program: Specifies the program object to which a shader object will be attached.
    :type program: int
    :param shader: Specifies the shader object that is to be attached.
    :type shader: int
    """

def glBegin(mode: set[str]):
    """Delimit the vertices of a primitive or a group of like primitives`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glBegin.xml>`__

        :param mode: Specifies the primitive that will be create from vertices between
    glBegin and glEnd.
        :type mode: set[str]
    """

def glBindTexture(target: set[str], texture: int):
    """Bind a named texture to a texturing target`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glBindTexture.xml>`__

    :param target: Specifies the target to which the texture is bound.
    :type target: set[str]
    :param texture: Specifies the name of a texture.
    :type texture: int
    """

def glBitmap(
    width: int, height, xorig: float, yorig, xmove: float, ymove, bitmap: Buffer
):
    """Draw a bitmap`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glBitmap.xml>`__

        :param width: Specify the pixel width and height of the bitmap image.
        :type width: int
        :param xorig: Specify the location of the origin in the bitmap image. The origin is measured
    from the lower left corner of the bitmap, with right and up being the positive axes.
        :type xorig: float
        :param xmove: Specify the x and y offsets to be added to the current raster position after
    the bitmap is drawn.
        :type xmove: float
        :param bitmap: Specifies the address of the bitmap image.
        :type bitmap: Buffer
    """

def glBlendFunc(sfactor: set[str], dfactor: set[str]):
    """Specify pixel arithmetic`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glBlendFunc.xml>`__

        :param sfactor: Specifies how the red, green, blue, and alpha source blending factors are
    computed.
        :type sfactor: set[str]
        :param dfactor: Specifies how the red, green, blue, and alpha destination
    blending factors are computed.
        :type dfactor: set[str]
    """

def glCallList(list: int):
    """Execute a display list`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glCallList.xml>`__

    :param list: Specifies the integer name of the display list to be executed.
    :type list: int
    """

def glCallLists(n: int, type: set[str], lists: Buffer):
    """Execute a list of display lists`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glCallLists.xml>`__

        :param n: Specifies the number of display lists to be executed.
        :type n: int
        :param type: Specifies the type of values in lists.
        :type type: set[str]
        :param lists: Specifies the address of an array of name offsets in the display list.
    The pointer type is void because the offsets can be bytes, shorts, ints, or floats,
    depending on the value of type.
        :type lists: Buffer
    """

def glClear(mask):
    """Clear buffers to preset values`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glClear.xml>`__

    :param mask: Bitwise OR of masks that indicate the buffers to be cleared.
    """

def glClearAccum(red: float, green, blue, alpha):
    """Specify clear values for the accumulation buffer`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glClearAccum.xml>`__

        :param red: Specify the red, green, blue, and alpha values used when the
    accumulation buffer is cleared. The initial values are all 0.
        :type red: float
    """

def glClearColor(red: float, green, blue, alpha):
    """Specify clear values for the color buffers`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glClearColor.xml>`__

        :param red: Specify the red, green, blue, and alpha values used when the
    color buffers are cleared. The initial values are all 0.
        :type red: float
    """

def glClearDepth(depth: int):
    """Specify the clear value for the depth buffer`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glClearDepth.xml>`__

        :param depth: Specifies the depth value used when the depth buffer is cleared.
    The initial value is 1.
        :type depth: int
    """

def glClearIndex(c: float):
    """Specify the clear value for the color index buffers`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glClearIndex.xml>`__

        :param c: Specifies the index used when the color index buffers are cleared.
    The initial value is 0.
        :type c: float
    """

def glClearStencil(s: int):
    """Specify the clear value for the stencil buffer`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glClearStencil.xml>`__

    :param s: Specifies the index used when the stencil buffer is cleared. The initial value is 0.
    :type s: int
    """

def glClipPlane(plane: set[str], equation: Buffer):
    """Specify a plane against which all geometry is clipped`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glClipPlane.xml>`__

        :param plane: Specifies which clipping plane is being positioned.
        :type plane: set[str]
        :param equation: Specifies the address of an array of four double- precision
    floating-point values. These values are interpreted as a plane equation.
        :type equation: Buffer
    """

def glColor(red: typing.Any, green, blue, alpha):
    """B{glColor3b, glColor3d, glColor3f, glColor3i, glColor3s, glColor3ub, glColor3ui, glColor3us,
    glColor4b, glColor4d, glColor4f, glColor4i, glColor4s, glColor4ub, glColor4ui, glColor4us,
    glColor3bv, glColor3dv, glColor3fv, glColor3iv, glColor3sv, glColor3ubv, glColor3uiv,
    glColor3usv, glColor4bv, glColor4dv, glColor4fv, glColor4iv, glColor4sv, glColor4ubv,
    glColor4uiv, glColor4usv}Set a new color.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glColor.xml>`__

        :param red: Specify new red, green, and blue values for the current color.
        :type red: typing.Any
        :param alpha: Specifies a new alpha value for the current color. Included only in the
    four-argument glColor4 commands. (With '4' colors only)
    """

def glColorMask(red: int, green, blue, alpha):
    """Enable and disable writing of frame buffer color components`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glColorMask.xml>`__

        :param red: Specify whether red, green, blue, and alpha can or cannot be
    written into the frame buffer. The initial values are all GL_TRUE, indicating that the
    color components can be written.
        :type red: int
    """

def glColorMaterial(face: set[str], mode: set[str]):
    """Cause a material color to track the current color`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glColorMaterial.xml>`__

        :param face: Specifies whether front, back, or both front and back material parameters should
    track the current color.
        :type face: set[str]
        :param mode: Specifies which of several material parameters track the current color.
        :type mode: set[str]
    """

def glCompileShader(shader: int):
    """Compiles a shader object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glCompileShader.xml>`__

    :param shader: Specifies the shader object to be compiled.
    :type shader: int
    """

def glCopyPixels(x: int, y, width: int, height: int, type: set[str]):
    """Copy pixels in the frame buffer`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glCopyPixels.xml>`__def glCopyTexImage2D(target, level, internalformat, x, y, width, height, border):Copy pixels into a 2D texture image`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glCopyTexImage2D.xml>`__

        :param x: Specify the window coordinates of the lower left corner of the rectangular
    region of pixels to be copied.Specify the window coordinates of the first pixel that is copied
    from the frame buffer. This location is the lower left corner of a rectangular
    block of pixels.
        :type x: int
        :param width: Specify the dimensions of the rectangular region of pixels to be copied.
    Both must be non-negative.Specifies the width of the texture image. Must be 2n+2(border) for
    some integer n. All implementations support texture images that are at least 64
    texels wide.
        :type width: int
        :param height: Specifies the height of the texture image. Must be 2m+2(border) for
    some integer m. All implementations support texture images that are at least 64
    texels high.
        :type height: int
        :param type: Specifies whether color values, depth values, or stencil values are to be copied.
        :type type: set[str]
    """

def glCreateProgram() -> int:
    """Creates a program object`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glCreateProgram.xml>`__

    :return: The new program or zero if an error occurs.
    :rtype: int
    """

def glCreateShader(shaderType: GL_GEOMETRY_SHADER | typing.Any) -> int:
    """Creates a shader object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glCreateShader.xml>`__

    :type shaderType: GL_GEOMETRY_SHADER | typing.Any
    :return: 0 if an error occurs.
    :rtype: int
    """

def glCullFace(mode: set[str]):
    """Specify whether front- or back-facing facets can be culled`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glCullFace.xml>`__

    :param mode: Specifies whether front- or back-facing facets are candidates for culling.
    :type mode: set[str]
    """

def glDeleteLists(list: int, range: int):
    """Delete a contiguous group of display lists`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glDeleteLists.xml>`__

    :param list: Specifies the integer name of the first display list to delete
    :type list: int
    :param range: Specifies the number of display lists to delete
    :type range: int
    """

def glDeleteProgram(program: int):
    """Deletes a program object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glDeleteProgram.xml>`__

    :param program: Specifies the program object to be deleted.
    :type program: int
    """

def glDeleteShader(shader: int):
    """Deletes a shader object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glDeleteShader.xml>`__

    :param shader: Specifies the shader object to be deleted.
    :type shader: int
    """

def glDeleteTextures(n: int, textures: Buffer):
    """Delete named textures`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glDeleteTextures.xml>`__

    :param n: Specifies the number of textures to be deleted
    :type n: int
    :param textures: Specifies an array of textures to be deleted
    :type textures: Buffer
    """

def glDepthFunc(func: set[str]):
    """Specify the value used for depth buffer comparisons`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glDepthFunc.xml>`__

    :param func: Specifies the depth comparison function.
    :type func: set[str]
    """

def glDepthMask(flag: int):
    """Enable or disable writing into the depth buffer`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glDepthMask.xml>`__

        :param flag: Specifies whether the depth buffer is enabled for writing. If flag is GL_FALSE,
    depth buffer writing is disabled. Otherwise, it is enabled. Initially, depth buffer
    writing is enabled.
        :type flag: int
    """

def glDepthRange(zNear: int, zFar: int):
    """Specify mapping of depth values from normalized device coordinates to window coordinates`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glDepthRange.xml>`__

        :param zNear: Specifies the mapping of the near clipping plane to window coordinates.
    The initial value is 0.
        :type zNear: int
        :param zFar: Specifies the mapping of the far clipping plane to window coordinates.
    The initial value is 1.
        :type zFar: int
    """

def glDetachShader(program: int, shader: int):
    """Detaches a shader object from a program object to which it is attached.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glDetachShader.xml>`__

    :param program: Specifies the program object from which to detach the shader object.
    :type program: int
    :param shader: pecifies the program object from which to detach the shader object.
    :type shader: int
    """

def glDisable(cap: set[str]):
    """Disable server-side GL capabilities`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glEnable.xml>`__

    :param cap: Specifies a symbolic constant indicating a GL capability.
    :type cap: set[str]
    """

def glDrawBuffer(mode: set[str]):
    """Specify which color buffers are to be drawn into`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glDrawBuffer.xml>`__

    :param mode: Specifies up to four color buffers to be drawn into.
    :type mode: set[str]
    """

def glDrawPixels(width: int, height, format: set[str], type: set[str], pixels: Buffer):
    """Write a block of pixels to the frame buffer`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glDrawPixels.xml>`__

        :param width: Specify the dimensions of the pixel rectangle to be
    written into the frame buffer.
        :type width: int
        :param format: Specifies the format of the pixel data.
        :type format: set[str]
        :param type: Specifies the data type for pixels.
        :type type: set[str]
        :param pixels: Specifies a pointer to the pixel data.
        :type pixels: Buffer
    """

def glEdgeFlag(flag):
    """B{glEdgeFlag, glEdgeFlagv}Flag edges as either boundary or non-boundary`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glEdgeFlag.xml>`__

    :param flag: Specifies the current edge flag value.The initial value is GL_TRUE.
    """

def glEnable(cap: set[str]):
    """Enable server-side GL capabilities`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glEnable.xml>`__

    :param cap: Specifies a symbolic constant indicating a GL capability.
    :type cap: set[str]
    """

def glEnd():
    """Delimit the vertices of a primitive or group of like primitives`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glBegin.xml>`__"""

def glEndList():
    """Create or replace a display list`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glNewList.xml>`__"""

def glEvalCoord(u: typing.Any, v: typing.Any):
    """B{glEvalCoord1d, glEvalCoord1f, glEvalCoord2d, glEvalCoord2f, glEvalCoord1dv, glEvalCoord1fv,
    glEvalCoord2dv, glEvalCoord2fv}Evaluate enabled one- and two-dimensional maps`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glEvalCoord.xml>`__

        :param u: Specifies a value that is the domain coordinate u to the basis function defined
    in a previous glMap1 or glMap2 command. If the function prototype ends in 'v' then
    u specifies a pointer to an array containing either one or two domain coordinates. The first
    coordinate is u. The second coordinate is v, which is present only in glEvalCoord2 versions.
        :type u: typing.Any
        :param v: Specifies a value that is the domain coordinate v to the basis function defined
    in a previous glMap2 command. This argument is not present in a glEvalCoord1 command.
        :type v: typing.Any
    """

def glEvalMesh(mode: set[str], i1: int, i2):
    """B{glEvalMesh1 or glEvalMesh2}Compute a one- or two-dimensional grid of points or lines`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glEvalMesh.xml>`__

        :param mode: In glEvalMesh1, specifies whether to compute a one-dimensional
    mesh of points or lines.
        :type mode: set[str]
        :param i1: Specify the first and last integer values for the grid domain variable i.
        :type i1: int
    """

def glEvalPoint(i: int, j):
    """B{glEvalPoint1 and glEvalPoint2}Generate and evaluate a single point in a mesh`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glEvalPoint.xml>`__

    :param i: Specifies the integer value for grid domain variable i.
    :type i: int
    :param j: Specifies the integer value for grid domain variable j (glEvalPoint2 only).
    """

def glFeedbackBuffer(size: int, type: set[str], buffer: Buffer):
    """Controls feedback mode`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glFeedbackBuffer.xml>`__

        :param size: Specifies the maximum number of values that can be written into buffer.
        :type size: int
        :param type: Specifies a symbolic constant that describes the information that
    will be returned for each vertex.
        :type type: set[str]
        :param buffer: Returns the feedback data.
        :type buffer: Buffer
    """

def glFinish():
    """Block until all GL execution is complete`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glFinish.xml>`__"""

def glFlush():
    """Force Execution of GL commands in finite time`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glFlush.xml>`__"""

def glFog(pname: set[str], param: typing.Any):
    """B{glFogf, glFogi, glFogfv, glFogiv}Specify fog parameters`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glFog.xml>`__

        :param pname: Specifies a single-valued fog parameter. If the function prototype
    ends in 'v' specifies a fog parameter.
        :type pname: set[str]
        :param param: Specifies the value or values to be assigned to pname. GL_FOG_COLOR
    requires an array of four values. All other parameters accept an array containing
    only a single value.
        :type param: typing.Any
    """

def glFrontFace(mode: set[str]):
    """Define front- and back-facing polygons`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glFrontFace.xml>`__

    :param mode: Specifies the orientation of front-facing polygons.
    :type mode: set[str]
    """

def glFrustum(left: float, right, bottom, top: float, zNear: float, zFar):
    """Multiply the current matrix by a perspective matrix`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glFrustum.xml>`__

        :param left: Specify the coordinates for the left and right vertical
    clipping planes.
        :type left: float
        :param top: Specify the coordinates for the bottom and top horizontal
    clipping planes.
        :type top: float
        :param zNear: Specify the distances to the near and far depth clipping planes.
    Both distances must be positive.
        :type zNear: float
    """

def glGenLists(range: int):
    """Generate a contiguous set of empty display lists`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGenLists.xml>`__

    :param range: Specifies the number of contiguous empty display lists to be generated.
    :type range: int
    """

def glGenTextures(n: int, textures: Buffer):
    """Generate texture names`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGenTextures.xml>`__

    :param n: Specifies the number of textures name to be generated.
    :type n: int
    :param textures: Specifies an array in which the generated textures names are stored.
    :type textures: Buffer
    """

def glGet(pname: set[str], param: typing.Any):
    """B{glGetBooleanv, glGetfloatv, glGetFloatv, glGetIntegerv}Return the value or values of a selected parameter`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGet.xml>`__

    :param pname: Specifies the parameter value to be returned.
    :type pname: set[str]
    :param param: Returns the value or values of the specified parameter.
    :type param: typing.Any
    """

def glGetAttachedShaders(program: int, maxCount: int, count: Buffer, shaders: Buffer):
    """Returns the handles of the shader objects attached to a program object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetAttachedShaders.xml>`__

    :param program: Specifies the program object to be queried.
    :type program: int
    :param maxCount: Specifies the size of the array for storing the returned object names.
    :type maxCount: int
    :param count: Returns the number of names actually returned in objects.
    :type count: Buffer
    :param shaders: Specifies an array that is used to return the names of attached shader objects.
    :type shaders: Buffer
    """

def glGetClipPlane(plane: set[str], equation: Buffer):
    """Return the coefficients of the specified clipping plane`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetClipPlane.xml>`__

        :param plane: Specifies a clipping plane. The number of clipping planes depends on the
    implementation, but at least six clipping planes are supported. They are identified by
    symbolic names of the form GL_CLIP_PLANEi where 0 < i < GL_MAX_CLIP_PLANES.
        :type plane: set[str]
        :param equation: Returns four float (double)-precision values that are the coefficients of the
    plane equation of plane in eye coordinates. The initial value is (0, 0, 0, 0).
        :type equation: Buffer
    """

def glGetError():
    """Return error information`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetError.xml>`__"""

def glGetLight(light: set[str], pname: set[str], params: Buffer):
    """B{glGetLightfv and glGetLightiv}Return light source parameter values`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetLight.xml>`__

        :param light: Specifies a light source. The number of possible lights depends on the
    implementation, but at least eight lights are supported. They are identified by symbolic
    names of the form GL_LIGHTi where 0 < i < GL_MAX_LIGHTS.
        :type light: set[str]
        :param pname: Specifies a light source parameter for light.
        :type pname: set[str]
        :param params: Returns the requested data.
        :type params: Buffer
    """

def glGetMap(target: set[str], query: set[str], v: Buffer):
    """B{glGetMapdv, glGetMapfv, glGetMapiv}Return evaluator parameters`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetMap.xml>`_

    :param target: Specifies the symbolic name of a map.
    :type target: set[str]
    :param query: Specifies which parameter to return.
    :type query: set[str]
    :param v: Returns the requested data.
    :type v: Buffer
    """

def glGetMaterial(face: set[str], pname: set[str], params: Buffer):
    """B{glGetMaterialfv, glGetMaterialiv}Return material parameters`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetMaterial.xml>`__

        :param face: Specifies which of the two materials is being queried.
    representing the front and back materials, respectively.
        :type face: set[str]
        :param pname: Specifies the material parameter to return.
        :type pname: set[str]
        :param params: Returns the requested data.
        :type params: Buffer
    """

def glGetPixelMap(map: set[str], values: Buffer):
    """B{glGetPixelMapfv, glGetPixelMapuiv, glGetPixelMapusv}Return the specified pixel map`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetPixelMap.xml>`__

    :param map: Specifies the name of the pixel map to return.
    :type map: set[str]
    :param values: Returns the pixel map contents.
    :type values: Buffer
    """

def glGetPolygonStipple(mask: Buffer):
    """Return the polygon stipple pattern`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetPolygonStipple.xml>`__

    :param mask: Returns the stipple pattern. The initial value is all 1's.
    :type mask: Buffer
    """

def glGetProgramInfoLog(program: int, maxLength: int, length: Buffer, infoLog: Buffer):
    """Returns the information log for a program object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetProgramInfoLog.xml>`__

    :param program: Specifies the program object whose information log is to be queried.
    :type program: int
    :param maxLength: Specifies the size of the character buffer for storing the returned information log.
    :type maxLength: int
    :param length: Returns the length of the string returned in infoLog (excluding the null terminator).
    :type length: Buffer
    :param infoLog: Specifies an array of characters that is used to return the information log.
    :type infoLog: Buffer
    """

def glGetProgramiv(program: int, pname: int, params: Buffer):
    """Returns a parameter from a program object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetProgram.xml>`__

    :param program: Specifies the program object to be queried.
    :type program: int
    :param pname: Specifies the object parameter.
    :type pname: int
    :param params: Returns the requested object parameter.
    :type params: Buffer
    """

def glGetShaderInfoLog(program, maxLength: int, length: Buffer, infoLog: Buffer):
    """Returns the information log for a shader object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetShaderInfoLog.xml>`__

    :param maxLength: Specifies the size of the character buffer for storing the returned information log.
    :type maxLength: int
    :param length: Returns the length of the string returned in infoLog (excluding the null terminator).
    :type length: Buffer
    :param infoLog: Specifies an array of characters that is used to return the information log.
    :type infoLog: Buffer
    """

def glGetShaderSource(shader: int, bufSize: int, length: Buffer, source: Buffer):
    """Returns the source code string from a shader object`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetShaderSource.xml>`__

    :param shader: Specifies the shader object to be queried.
    :type shader: int
    :param bufSize: Specifies the size of the character buffer for storing the returned source code string.
    :type bufSize: int
    :param length: Returns the length of the string returned in source (excluding the null terminator).
    :type length: Buffer
    :param source: Specifies an array of characters that is used to return the source code string.
    :type source: Buffer
    """

def glGetString(name: set[str]):
    """Return a string describing the current GL connection`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetString.xml>`__

    :param name: Specifies a symbolic constant.
    :type name: set[str]
    """

def glGetTexEnv(target: set[str], pname: set[str], params: Buffer):
    """B{glGetTexEnvfv, glGetTexEnviv}Return texture environment parameters`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetTexEnv.xml>`__

    :param target: Specifies a texture environment. Must be GL_TEXTURE_ENV.
    :type target: set[str]
    :param pname: Specifies the symbolic name of a texture environment parameter.
    :type pname: set[str]
    :param params: Returns the requested data.
    :type params: Buffer
    """

def glGetTexGen(coord: set[str], pname: set[str], params: Buffer):
    """B{glGetTexGendv, glGetTexGenfv, glGetTexGeniv}Return texture coordinate generation parameters`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetTexGen.xml>`__

    :param coord: Specifies a texture coordinate.
    :type coord: set[str]
    :param pname: Specifies the symbolic name of the value(s) to be returned.
    :type pname: set[str]
    :param params: Returns the requested data.
    :type params: Buffer
    """

def glGetTexImage(
    target: set[str], level: int, format: set[str], type: set[str], pixels: Buffer
):
    """Return a texture image`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetTexImage.xml>`__

        :param target: Specifies which texture is to be obtained.
        :type target: set[str]
        :param level: Specifies the level-of-detail number of the desired image.
    Level 0 is the base image level. Level n is the nth mipmap reduction image.
        :type level: int
        :param format: Specifies a pixel format for the returned data.
        :type format: set[str]
        :param type: Specifies a pixel type for the returned data.
        :type type: set[str]
        :param pixels: Returns the texture image. Should be a pointer to an array of the
    type specified by type
        :type pixels: Buffer
    """

def glGetTexLevelParameter(
    target: set[str], level: int, pname: set[str], params: Buffer
):
    """B{glGetTexLevelParameterfv, glGetTexLevelParameteriv}return texture parameter values for a specific level of detail`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetTexLevelParameter.xml>`__

        :param target: Specifies the symbolic name of the target texture.
        :type target: set[str]
        :param level: Specifies the level-of-detail number of the desired image.
    Level 0 is the base image level. Level n is the nth mipmap reduction image.
        :type level: int
        :param pname: Specifies the symbolic name of a texture parameter.
        :type pname: set[str]
        :param params: Returns the requested data.
        :type params: Buffer
    """

def glGetTexParameter(target: set[str], pname: set[str], params: Buffer):
    """B{glGetTexParameterfv, glGetTexParameteriv}Return texture parameter values`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glGetTexParameter.xml>`__

    :param target: Specifies the symbolic name of the target texture.
    :type target: set[str]
    :param pname: Specifies the symbolic name the target texture.
    :type pname: set[str]
    :param params: Returns the texture parameters.
    :type params: Buffer
    """

def glHint(target: set[str], mode: set[str]):
    """Specify implementation-specific hints`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glHint.xml>`__

        :param target: Specifies a symbolic constant indicating the behavior to be
    controlled.
        :type target: set[str]
        :param mode: Specifies a symbolic constant indicating the desired behavior.
        :type mode: set[str]
    """

def glIndex(c: Buffer):
    """B{glIndexd, glIndexf, glIndexi, glIndexs,  glIndexdv, glIndexfv, glIndexiv, glIndexsv}Set the current color index`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glIndex.xml>`__

        :param c: Specifies a pointer to a one element array that contains the new value for
    the current color index.
        :type c: Buffer
    """

def glIndexMask(mask: int):
    """Control the writing of individual bits in the color index buffers`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glIndexMask.xml>`__

        :param mask: Specifies a bit mask to enable and disable the writing of individual bits
    in the color index buffers.
    Initially, the mask is all 1's.
        :type mask: int
    """

def glInitNames():
    """Initialize the name stack`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glInitNames.xml>`__"""

def glIsEnabled(cap: set[str]):
    """Test whether a capability is enabled`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glIsEnabled.xml>`__

    :param cap: Specifies a constant representing a GL capability.
    :type cap: set[str]
    """

def glIsList(list: int):
    """Determine if a name corresponds to a display-list`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glIsList.xml>`__

    :param list: Specifies a potential display-list name.
    :type list: int
    """

def glIsProgram(program: int):
    """Determines if a name corresponds to a program object`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glIsProgram.xml>`__

    :param program: Specifies a potential program object.
    :type program: int
    """

def glIsShader(shader: int):
    """Determines if a name corresponds to a shader object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glIsShader.xml>`__

    :param shader: Specifies a potential shader object.
    :type shader: int
    """

def glIsTexture(texture: int):
    """Determine if a name corresponds to a texture`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glIsTexture.xml>`__

    :param texture: Specifies a value that may be the name of a texture.
    :type texture: int
    """

def glLight(light: set[str], pname: set[str], param: typing.Any):
    """B{glLightf,glLighti, glLightfv, glLightiv}Set the light source parameters`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glLight.xml>`__

        :param light: Specifies a light. The number of lights depends on the implementation,
    but at least eight lights are supported. They are identified by symbolic names of the
    form GL_LIGHTi where 0 < i < GL_MAX_LIGHTS.
        :type light: set[str]
        :param pname: Specifies a single-valued light source parameter for light.
        :type pname: set[str]
        :param param: Specifies the value that parameter pname of light source light will be set to.
    If function prototype ends in 'v' specifies a pointer to the value or values that
    parameter pname of light source light will be set to.
        :type param: typing.Any
    """

def glLightModel(pname: set[str], param: typing.Any):
    """B{glLightModelf, glLightModeli, glLightModelfv, glLightModeliv}Set the lighting model parameters`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glLightModel.xml>`__

        :param pname: Specifies a single-value light model parameter.
        :type pname: set[str]
        :param param: Specifies the value that param will be set to. If function prototype ends in 'v'
    specifies a pointer to the value or values that param will be set to.
        :type param: typing.Any
    """

def glLineStipple(factor: int, pattern):
    """Specify the line stipple pattern`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glLineStipple.xml>`__

        :param factor: Specifies a multiplier for each bit in the line stipple pattern.
    If factor is 3, for example, each bit in the pattern is used three times before
    the next bit in the pattern is used. factor is clamped to the range [1, 256] and
    defaults to 1.
        :type factor: int
        :param pattern: Specifies a 16-bit integer whose bit pattern determines which fragments
    of a line will be drawn when the line is rasterized. Bit zero is used first; the default
    pattern is all 1's.
    """

def glLineWidth(width: float):
    """Specify the width of rasterized lines.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glLineWidth.xml>`__

    :param width: Specifies the width of rasterized lines. The initial value is 1.
    :type width: float
    """

def glLinkProgram(program: int):
    """Links a program object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glLinkProgram.xml>`__

    :param program: Specifies the handle of the program object to be linked.
    :type program: int
    """

def glListBase(base: int):
    """Set the display-list base for glCallLists`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glListBase.xml>`__

        :param base: Specifies an integer offset that will be added to glCallLists
    offsets to generate display-list names. The initial value is 0.
        :type base: int
    """

def glLoadIdentity():
    """Replace the current matrix with the identity matrix`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glLoadIdentity.xml>`__"""

def glLoadMatrix(m: Buffer):
    """B{glLoadMatrixd, glLoadMatixf}Replace the current matrix with the specified matrix`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glLoadMatrix.xml>`__

        :param m: Specifies a pointer to 16 consecutive values, which are used as the elements
    of a 4x4 column-major matrix.
        :type m: Buffer
    """

def glLoadName(name: int):
    """Load a name onto the name stack.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glLoadName.xml>`__

    :param name: Specifies a name that will replace the top value on the name stack.
    :type name: int
    """

def glLogicOp(opcode: set[str]):
    """Specify a logical pixel operation for color index rendering`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glLogicOp.xml>`__

    :param opcode: Specifies a symbolic constant that selects a logical operation.
    :type opcode: set[str]
    """

def glMap1(
    target: set[str], u1: typing.Any, u2, stride: int, order: int, points: Buffer
):
    """B{glMap1d, glMap1f}Define a one-dimensional evaluator`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glMap1.xml>`__

        :param target: Specifies the kind of values that are generated by the evaluator.
        :type target: set[str]
        :param u1: Specify a linear mapping of u, as presented to glEvalCoord1, to ^, t
    he variable that is evaluated by the equations specified by this command.
        :type u1: typing.Any
        :param stride: Specifies the number of floats or float (double)s between the beginning
    of one control point and the beginning of the next one in the data structure
    referenced in points. This allows control points to be embedded in arbitrary data
    structures. The only constraint is that the values for a particular control point must
    occupy contiguous memory locations.
        :type stride: int
        :param order: Specifies the number of control points. Must be positive.
        :type order: int
        :param points: Specifies a pointer to the array of control points.
        :type points: Buffer
    """

def glMap2(
    target: set[str],
    u1: typing.Any,
    u2,
    ustride: int,
    uorder: int,
    v1: typing.Any,
    v2,
    vstride: int,
    vorder: int,
    points: Buffer,
):
    """B{glMap2d, glMap2f}Define a two-dimensional evaluator`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glMap2.xml>`__

        :param target: Specifies the kind of values that are generated by the evaluator.
        :type target: set[str]
        :param u1: Specify a linear mapping of u, as presented to glEvalCoord2, to ^, t
    he variable that is evaluated by the equations specified by this command. Initially
    u1 is 0 and u2 is 1.
        :type u1: typing.Any
        :param ustride: Specifies the number of floats or float (double)s between the beginning
    of control point R and the beginning of control point R ij, where i and j are the u
    and v control point indices, respectively. This allows control points to be embedded
    in arbitrary data structures. The only constraint is that the values for a particular
    control point must occupy contiguous memory locations. The initial value of ustride is 0.
        :type ustride: int
        :param uorder: Specifies the dimension of the control point array in the u axis.
    Must be positive. The initial value is 1.
        :type uorder: int
        :param v1: Specify a linear mapping of v, as presented to glEvalCoord2,
    to ^, one of the two variables that are evaluated by the equations
    specified by this command. Initially, v1 is 0 and v2 is 1.
        :type v1: typing.Any
        :param vstride: Specifies the number of floats or float (double)s between the
    beginning of control point R and the beginning of control point R ij,
    where i and j are the u and v control point(indices, respectively.
    This allows control points to be embedded in arbitrary data structures.
    The only constraint is that the values for a particular control point must
    occupy contiguous memory locations. The initial value of vstride is 0.
        :type vstride: int
        :param vorder: Specifies the dimension of the control point array in the v axis.
    Must be positive. The initial value is 1.
        :type vorder: int
        :param points: Specifies a pointer to the array of control points.
        :type points: Buffer
    """

def glMapGrid(un: int, u1: typing.Any, u2, vn: int, v1: typing.Any, v2):
    """B{glMapGrid1d, glMapGrid1f, glMapGrid2d, glMapGrid2f}Define a one- or two-dimensional mesh`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glMapGrid.xml>`__

        :param un: Specifies the number of partitions in the grid range interval
    [u1, u2]. Must be positive.
        :type un: int
        :param u1: Specify the mappings for integer grid domain values i=0 and i=un.
        :type u1: typing.Any
        :param vn: Specifies the number of partitions in the grid range interval
    [v1, v2] (glMapGrid2 only).
        :type vn: int
        :param v1: Specify the mappings for integer grid domain values j=0 and j=vn
    (glMapGrid2 only).
        :type v1: typing.Any
    """

def glMaterial(face: set[str], pname: set[str], params: int):
    """Specify material parameters for the lighting model.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glMaterial.xml>`__

        :param face: Specifies which face or faces are being updated. Must be one of:
        :type face: set[str]
        :param pname: Specifies the single-valued material parameter of the face
    or faces that is being updated. Must be GL_SHININESS.
        :type pname: set[str]
        :param params: Specifies the value that parameter GL_SHININESS will be set to.
    If function prototype ends in 'v' specifies a pointer to the value or values that
    pname will be set to.
        :type params: int
    """

def glMatrixMode(mode: set[str]):
    """Specify which matrix is the current matrix.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glMatrixMode.xml>`__

    :param mode: Specifies which matrix stack is the target for subsequent matrix operations.
    :type mode: set[str]
    """

def glMultMatrix(m: Buffer):
    """B{glMultMatrixd, glMultMatrixf}Multiply the current matrix with the specified matrix`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glMultMatrix.xml>`__

        :param m: Points to 16 consecutive values that are used as the elements of a 4x4 column
    major matrix.
        :type m: Buffer
    """

def glNewList(list: int, mode: set[str]):
    """Create or replace a display list`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glNewList.xml>`__

    :param list: Specifies the display list name
    :type list: int
    :param mode: Specifies the compilation mode.
    :type mode: set[str]
    """

def glNormal3(nx: typing.Any, ny, nz, v: Buffer):
    """B{Normal3b, Normal3bv, Normal3d, Normal3dv, Normal3f, Normal3fv, Normal3i, Normal3iv,
    Normal3s, Normal3sv}Set the current normal vector`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glNormal.xml>`__

        :param nx: Specify the x, y, and z coordinates of the new current normal.
    The initial value of the current normal is the unit vector, (0, 0, 1).
        :type nx: typing.Any
        :param v: Specifies a pointer to an array of three elements: the x, y, and z coordinates
    of the new current normal.
        :type v: Buffer
    """

def glOrtho(left: float, right, bottom: float, top, zNear: float, zFar):
    """Multiply the current matrix with an orthographic matrix`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glOrtho.xml>`__

        :param left: Specify the coordinates for the left and
    right vertical clipping planes.
        :type left: float
        :param bottom: Specify the coordinates for the bottom and top
    horizontal clipping planes.
        :type bottom: float
        :param zNear: Specify the distances to the nearer and farther
    depth clipping planes. These values are negative if the plane is to be behind the viewer.
        :type zNear: float
    """

def glPassThrough(token: float):
    """Place a marker in the feedback buffer`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPassThrough.xml>`__

        :param token: Specifies a marker value to be placed in the feedback
    buffer following a GL_PASS_THROUGH_TOKEN.
        :type token: float
    """

def glPixelMap(map: set[str], mapsize: int, values: Buffer):
    """B{glPixelMapfv, glPixelMapuiv, glPixelMapusv}Set up pixel transfer maps`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPixelMap.xml>`__

    :param map: Specifies a symbolic map name.
    :type map: set[str]
    :param mapsize: Specifies the size of the map being defined.
    :type mapsize: int
    :param values: Specifies an array of mapsize values.
    :type values: Buffer
    """

def glPixelStore(pname: set[str], param: typing.Any):
    """B{glPixelStoref, glPixelStorei}Set pixel storage modes`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPixelStore.xml>`__

        :param pname: Specifies the symbolic name of the parameter to be set.
    Six values affect the packing of pixel data into memory.
    Six more affect the unpacking of pixel data from memory.
        :type pname: set[str]
        :param param: Specifies the value that pname is set to.
        :type param: typing.Any
    """

def glPixelTransfer(pname: set[str], param: typing.Any):
    """B{glPixelTransferf, glPixelTransferi}Set pixel transfer modes`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPixelTransfer.xml>`__

    :param pname: Specifies the symbolic name of the pixel transfer parameter to be set.
    :type pname: set[str]
    :param param: Specifies the value that pname is set to.
    :type param: typing.Any
    """

def glPixelZoom(xfactor: float, yfactor):
    """Specify the pixel zoom factors`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPixelZoom.xml>`__

    :param xfactor: Specify the x and y zoom factors for pixel write operations.
    :type xfactor: float
    """

def glPointSize(size: float):
    """Specify the diameter of rasterized points`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPointSize.xml>`__

    :param size: Specifies the diameter of rasterized points. The initial value is 1.
    :type size: float
    """

def glPolygonMode(face: set[str], mode: set[str]):
    """Select a polygon rasterization mode`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPolygonMode.xml>`__

        :param face: Specifies the polygons that mode applies to.
    Must be GL_FRONT for front-facing polygons, GL_BACK for back- facing
    polygons, or GL_FRONT_AND_BACK for front- and back-facing polygons.
        :type face: set[str]
        :param mode: Specifies how polygons will be rasterized.
    The initial value is GL_FILL for both front- and back- facing polygons.
        :type mode: set[str]
    """

def glPolygonOffset(factor: float, units: float):
    """Set the scale and units used to calculate depth values`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPolygonOffset.xml>`__

        :param factor: Specifies a scale factor that is used to create a variable depth
    offset for each polygon. The initial value is 0.
        :type factor: float
        :param units: Is multiplied by an implementation-specific value to create a
    constant depth offset. The initial value is 0.
        :type units: float
    """

def glPolygonStipple(mask: Buffer):
    """Set the polygon stippling pattern`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPolygonStipple.xml>`__

        :param mask: Specifies a pointer to a 32x32 stipple pattern that will be unpacked
    from memory in the same way that glDrawPixels unpacks pixels.
        :type mask: Buffer
    """

def glPopAttrib():
    """Pop the server attribute stack`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPopAttrib.xml>`__"""

def glPopClientAttrib():
    """Pop the client attribute stack`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPopClientAttrib.xml>`__"""

def glPopMatrix():
    """Pop the current matrix stack`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPopMatrix.xml>`__"""

def glPopName():
    """Pop the name stack`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPopName.xml>`__"""

def glPrioritizeTextures(n: int, textures: Buffer, priorities: Buffer):
    """Set texture residence priority`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPrioritizeTextures.xml>`__

        :param n: Specifies the number of textures to be prioritized.
        :type n: int
        :param textures: Specifies an array containing the names of the textures to be prioritized.
        :type textures: Buffer
        :param priorities: Specifies an array containing the texture priorities.
    A priority given in an element of priorities applies to the texture named
    by the corresponding element of textures.
        :type priorities: Buffer
    """

def glPushAttrib(mask):
    """Push the server attribute stack`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPushAttrib.xml>`__

    :param mask: Specifies a mask that indicates which attributes to save.
    """

def glPushClientAttrib(mask):
    """Push the client attribute stack`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPushClientAttrib.xml>`__

    :param mask: Specifies a mask that indicates which attributes to save.
    """

def glPushMatrix():
    """Push the current matrix stack`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPushMatrix.xml>`__"""

def glPushName(name: int):
    """Push the name stack`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glPushName.xml>`__

    :param name: Specifies a name that will be pushed onto the name stack.
    :type name: int
    """

def glRasterPos(x: typing.Any, y, z, w):
    """B{glRasterPos2d, glRasterPos2f, glRasterPos2i, glRasterPos2s, glRasterPos3d,
    glRasterPos3f, glRasterPos3i, glRasterPos3s, glRasterPos4d, glRasterPos4f,
    glRasterPos4i, glRasterPos4s, glRasterPos2dv, glRasterPos2fv, glRasterPos2iv,
    glRasterPos2sv, glRasterPos3dv, glRasterPos3fv, glRasterPos3iv, glRasterPos3sv,
    glRasterPos4dv, glRasterPos4fv, glRasterPos4iv, glRasterPos4sv}Specify the raster position for pixel operations`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glRasterPos.xml>`__

        :param x: Specify the x,y,z, and w object coordinates (if present) for the
    raster position.  If function prototype ends in 'v' specifies a pointer to an array of two,
    three, or four elements, specifying x, y, z, and w coordinates, respectively.
        :type x: typing.Any
    """

def glReadBuffer(mode: set[str]):
    """Select a color buffer source for pixels.`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glReadBuffer.xml>`__

    :param mode: Specifies a color buffer.
    :type mode: set[str]
    """

def glReadPixels(
    x: int, y, width: int, height, format: set[str], type: set[str], pixels: Buffer
):
    """Read a block of pixels from the frame buffer`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glReadPixels.xml>`__

        :param x: Specify the window coordinates of the first pixel that is read
    from the frame buffer. This location is the lower left corner of a rectangular
    block of pixels.
        :type x: int
        :param width: Specify the dimensions of the pixel rectangle. width and
    height of one correspond to a single pixel.
        :type width: int
        :param format: Specifies the format of the pixel data.
        :type format: set[str]
        :param type: Specifies the data type of the pixel data.
        :type type: set[str]
        :param pixels: Returns the pixel data.
        :type pixels: Buffer
    """

def glRect(x1: typing.Any, y1, x2: typing.Any, y2, v1: typing.Any, v2):
    """B{glRectd, glRectf, glRecti, glRects, glRectdv, glRectfv, glRectiv, glRectsv}Draw a rectangle`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glRect.xml>`__

        :param x1: Specify one vertex of a rectangle
        :type x1: typing.Any
        :param x2: Specify the opposite vertex of the rectangle
        :type x2: typing.Any
        :param v1: Specifies a pointer to one vertex of a rectangle and the pointer
    to the opposite vertex of the rectangle
        :type v1: typing.Any
    """

def glRenderMode(mode: set[str]):
    """Set rasterization mode`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glRenderMode.xml>`__

    :param mode: Specifies the rasterization mode.
    :type mode: set[str]
    """

def glRotate(angle: typing.Any, x: typing.Any, y, z):
    """B{glRotated, glRotatef}Multiply the current matrix by a rotation matrix`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glRotate.xml>`__

    :param angle: Specifies the angle of rotation in degrees.
    :type angle: typing.Any
    :param x: Specify the x, y, and z coordinates of a vector respectively.
    :type x: typing.Any
    """

def glScale(x: typing.Any, y, z):
    """B{glScaled, glScalef}Multiply the current matrix by a general scaling matrix`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glScale.xml>`__

    :param x: Specify scale factors along the x, y, and z axes, respectively.
    :type x: typing.Any
    """

def glScissor(x: int, y, width: int, height):
    """Define the scissor box`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glScissor.xml>`__

        :param x: Specify the lower left corner of the scissor box. Initially (0, 0).
        :type x: int
        :param width: Specify the width and height of the scissor box. When a
    GL context is first attached to a window, width and height are set to the
    dimensions of that window.
        :type width: int
    """

def glSelectBuffer(size: int, buffer: Buffer):
    """Establish a buffer for selection mode values`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glSelectBuffer.xml>`__

    :param size: Specifies the size of buffer
    :type size: int
    :param buffer: Returns the selection data
    :type buffer: Buffer
    """

def glShadeModel(mode: set[str]):
    """Select flat or smooth shading`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glShadeModel.xml>`__

    :param mode: Specifies a symbolic value representing a shading technique.
    :type mode: set[str]
    """

def glShaderSource(shader: int, shader_string: str):
    """Replaces the source code in a shader object.`OpenGL Docs <https://www.opengl.org/sdk/docs/man/html/glShaderSource.xhtml>`__

    :param shader: Specifies the handle of the shader object whose source code is to be replaced.
    :type shader: int
    :param shader_string: The shader string.
    :type shader_string: str
    """

def glStencilFunc(func: set[str], ref: int, mask: int):
    """Set function and reference value for stencil testing`OpenGL Docs <https://www.opengl.org/sdk/docs/man/docbook4/xhtml/glStencilFunc.xml>`__

        :param func: Specifies the test function.
        :type func: set[str]
        :param ref: Specifies the reference value for the stencil test. ref is clamped
    to the range [0,2n-1], where n is the number of bitplanes in the stencil
    buffer. The initial value is 0.
        :type ref: int
        :param mask: Specifies a mask that is ANDed with both the reference value and
    the stored stencil value when the test is done. The initial value is all 1's.
        :type mask: int
    """

def glStencilMask(mask: int):
    """Control the writing of individual bits in the stencil planes`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glStencilMask.xml>`__

        :param mask: Specifies a bit mask to enable and disable writing of individual bits
    in the stencil planes. Initially, the mask is all 1's.
        :type mask: int
    """

def glStencilOp(fail: set[str], zfail: set[str], zpass: set[str]):
    """Set stencil test actions`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glStencilOp.xml>`__

        :param fail: Specifies the action to take when the stencil test fails.
    The initial value is GL_KEEP.
        :type fail: set[str]
        :param zfail: Specifies the stencil action when the stencil test passes, but the
    depth test fails. zfail accepts the same symbolic constants as fail.
    The initial value is GL_KEEP.
        :type zfail: set[str]
        :param zpass: Specifies the stencil action when both the stencil test and the
    depth test pass, or when the stencil test passes and either there is no
    depth buffer or depth testing is not enabled. zpass accepts the same
    symbolic constants
    as fail. The initial value is GL_KEEP.
        :type zpass: set[str]
    """

def glTexCoord(s: typing.Any, t, r, q, v: Buffer):
    """B{glTexCoord1d, glTexCoord1f, glTexCoord1i, glTexCoord1s, glTexCoord2d, glTexCoord2f,
    glTexCoord2i, glTexCoord2s, glTexCoord3d, glTexCoord3f, glTexCoord3i, glTexCoord3s,
    glTexCoord4d, glTexCoord4f, glTexCoord4i, glTexCoord4s, glTexCoord1dv, glTexCoord1fv,
    glTexCoord1iv, glTexCoord1sv, glTexCoord2dv, glTexCoord2fv, glTexCoord2iv,
    glTexCoord2sv, glTexCoord3dv, glTexCoord3fv, glTexCoord3iv, glTexCoord3sv,
    glTexCoord4dv, glTexCoord4fv, glTexCoord4iv, glTexCoord4sv}Set the current texture coordinates`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glTexCoord.xml>`__

        :param s: Specify s, t, r, and q texture coordinates. Not all parameters are
    present in all forms of the command.
        :type s: typing.Any
        :param v: Specifies a pointer to an array of one, two, three, or four elements,
    which in turn specify the s, t, r, and q texture coordinates.
        :type v: Buffer
    """

def glTexEnv(target: set[str], pname: set[str], param: typing.Any):
    """B{glTextEnvf, glTextEnvi, glTextEnvfv, glTextEnviv}Set texture environment parameters`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glTexEnv.xml>`__

        :param target: Specifies a texture environment. Must be GL_TEXTURE_ENV.
        :type target: set[str]
        :param pname: Specifies the symbolic name of a single-valued texture environment
    parameter. Must be GL_TEXTURE_ENV_MODE.
        :type pname: set[str]
        :param param: Specifies a single symbolic constant. If function prototype ends in 'v'
    specifies a pointer to a parameter array that contains either a single
    symbolic constant or an RGBA color
        :type param: typing.Any
    """

def glTexGen(coord: set[str], pname: set[str], param: typing.Any):
    """B{glTexGend, glTexGenf, glTexGeni, glTexGendv, glTexGenfv, glTexGeniv}Control the generation of texture coordinates`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glTexGen.xml>`__

        :param coord: Specifies a texture coordinate.
        :type coord: set[str]
        :param pname: Specifies the symbolic name of the texture- coordinate generation function.
        :type pname: set[str]
        :param param: Specifies a single-valued texture generation parameter.
    If function prototype ends in 'v' specifies a pointer to an array of texture
    generation parameters. If pname is GL_TEXTURE_GEN_MODE, then the array must
    contain a single symbolic constant. Otherwise, params holds the coefficients
    for the texture-coordinate generation function specified by pname.
        :type param: typing.Any
    """

def glTexImage1D(
    target: set[str],
    level: int,
    internalformat: int,
    width: int,
    border: int,
    format: set[str],
    type: set[str],
    pixels: Buffer,
):
    """Specify a one-dimensional texture image`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glTexImage1D.xml>`__

        :param target: Specifies the target texture.
        :type target: set[str]
        :param level: Specifies the level-of-detail number. Level 0 is the base image level.
    Level n is the nth mipmap reduction image.
        :type level: int
        :param internalformat: Specifies the number of color components in the texture.
        :type internalformat: int
        :param width: Specifies the width of the texture image. Must be 2n+2(border)
    for some integer n. All implementations support texture images that are
    at least 64 texels wide. The height of the 1D texture image is 1.
        :type width: int
        :param border: Specifies the width of the border. Must be either 0 or 1.
        :type border: int
        :param format: Specifies the format of the pixel data.
        :type format: set[str]
        :param type: Specifies the data type of the pixel data.
        :type type: set[str]
        :param pixels: Specifies a pointer to the image data in memory.
        :type pixels: Buffer
    """

def glTexImage2D(
    target: set[str],
    level: int,
    internalformat: int,
    width: int,
    height: int,
    border: int,
    format: set[str],
    type: set[str],
    pixels: Buffer,
):
    """Specify a two-dimensional texture image`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glTexImage2D.xml>`__

        :param target: Specifies the target texture.
        :type target: set[str]
        :param level: Specifies the level-of-detail number. Level 0 is the base image level.
    Level n is the nth mipmap reduction image.
        :type level: int
        :param internalformat: Specifies the number of color components in the texture.
        :type internalformat: int
        :param width: Specifies the width of the texture image. Must be 2n+2(border)
    for some integer n. All implementations support texture images that are at
    least 64 texels wide.
        :type width: int
        :param height: Specifies the height of the texture image. Must be 2m+2(border) for
    some integer m. All implementations support texture images that are at
    least 64 texels high.
        :type height: int
        :param border: Specifies the width of the border. Must be either 0 or 1.
        :type border: int
        :param format: Specifies the format of the pixel data.
        :type format: set[str]
        :param type: Specifies the data type of the pixel data.
        :type type: set[str]
        :param pixels: Specifies a pointer to the image data in memory.
        :type pixels: Buffer
    """

def glTexParameter(target: set[str], pname: set[str], param: typing.Any):
    """B{glTexParameterf, glTexParameteri, glTexParameterfv, glTexParameteriv}Set texture parameters`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glTexParameter.xml>`__

        :param target: Specifies the target texture.
        :type target: set[str]
        :param pname: Specifies the symbolic name of a single-valued texture parameter.
        :type pname: set[str]
        :param param: Specifies the value of pname. If function prototype ends in 'v' specifies
    a pointer to an array where the value or values of pname are stored.
        :type param: typing.Any
    """

def glTranslate(x: typing.Any, y, z):
    """B{glTranslatef, glTranslated}Multiply the current matrix by a translation matrix`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glTranslate.xml>`__

    :param x: Specify the x, y, and z coordinates of a translation vector.
    :type x: typing.Any
    """

def glUseProgram(program: int):
    """Installs a program object as part of current rendering state`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glUseProgram.xml>`__

    :param program: Specifies the handle of the program object whose executables are to be used as part of current rendering state.
    :type program: int
    """

def glValidateProgram(program: int):
    """Validates a program object`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glValidateProgram.xml>`__

    :param program: Specifies the handle of the program object to be validated.
    :type program: int
    """

def glVertex(x: typing.Any, y, z, w, v: Buffer):
    """B{glVertex2d, glVertex2f, glVertex2i, glVertex2s, glVertex3d, glVertex3f, glVertex3i,
    glVertex3s, glVertex4d, glVertex4f, glVertex4i, glVertex4s, glVertex2dv, glVertex2fv,
    glVertex2iv, glVertex2sv, glVertex3dv, glVertex3fv, glVertex3iv, glVertex3sv, glVertex4dv,
    glVertex4fv, glVertex4iv, glVertex4sv}Specify a vertex`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glVertex.xml>`__

        :param x: Specify x, y, z, and w coordinates of a vertex. Not all parameters
    are present in all forms of the command.
        :type x: typing.Any
        :param v: Specifies a pointer to an array of two, three, or four elements. The
    elements of a two-element array are x and y; of a three-element array,
    x, y, and z; and of a four-element array, x, y, z, and w.
        :type v: Buffer
    """

def glViewport(x: int, y, width: int, height):
    """Set the viewport`OpenGL Docs <https://www.opengl.org/sdk/docs/man2/xhtml/glViewport.xml>`__

        :param x: Specify the lower left corner of the viewport rectangle,
    in pixels. The initial value is (0,0).
        :type x: int
        :param width: Specify the width and height of the viewport. When a GL
    context is first attached to a window, width and height are set to the
    dimensions of that window.
        :type width: int
    """

def gluLookAt(
    eyex: float, eyey, eyez, centerx: float, centery, centerz, upx: float, upy, upz
):
    """Define a viewing transformation.https://www.opengl.org/sdk/docs/man2/xhtml/gluLookAt.xml

    :param eyex: Specifies the position of the eye point.
    :type eyex: float
    :param centerx: Specifies the position of the reference point.
    :type centerx: float
    :param upx: Specifies the direction of the up vector.
    :type upx: float
    """

def gluOrtho2D(left: float, right, bottom: float, top):
    """Define a 2-D orthographic projection matrix.https://www.opengl.org/sdk/docs/man2/xhtml/gluOrtho2D.xml

    :param left: Specify the coordinates for the left and right vertical clipping planes.
    :type left: float
    :param bottom: Specify the coordinates for the bottom and top horizontal clipping planes.
    :type bottom: float
    """

def gluPerspective(fovY: float, aspect: float, zNear: float, zFar: float):
    """Set up a perspective projection matrix.https://www.opengl.org/sdk/docs/man2/xhtml/gluPerspective.xml

        :param fovY: Specifies the field of view angle, in degrees, in the y direction.
        :type fovY: float
        :param aspect: Specifies the aspect ratio that determines the field of view in the x direction.
    The aspect ratio is the ratio of x (width) to y (height).
        :type aspect: float
        :param zNear: Specifies the distance from the viewer to the near clipping plane (always positive).
        :type zNear: float
        :param zFar: Specifies the distance from the viewer to the far clipping plane (always positive).
        :type zFar: float
    """

def gluPickMatrix(x: float, y, width: float, height, viewport: Buffer):
    """Define a picking region.https://www.opengl.org/sdk/docs/man2/xhtml/gluPickMatrix.xml

    :param x: Specify the center of a picking region in window coordinates.
    :type x: float
    :param width: Specify the width and height, respectively, of the picking region in window coordinates.
    :type width: float
    :param viewport: Specifies the current viewport.
    :type viewport: Buffer
    """

def gluProject(
    objx: float,
    objy,
    objz,
    modelMatrix: Buffer,
    projMatrix: Buffer,
    viewport: Buffer,
    winx: Buffer,
    winy,
    winz,
):
    """Map object coordinates to window coordinates.https://www.opengl.org/sdk/docs/man2/xhtml/gluProject.xml

    :param objx: Specify the object coordinates.
    :type objx: float
    :param modelMatrix: Specifies the current modelview matrix (as from a glGetDoublev call).
    :type modelMatrix: Buffer
    :param projMatrix: Specifies the current projection matrix (as from a glGetDoublev call).
    :type projMatrix: Buffer
    :param viewport: Specifies the current viewport (as from a glGetIntegerv call).
    :type viewport: Buffer
    :param winx: Return the computed window coordinates.
    :type winx: Buffer
    """

def gluUnProject(
    winx: float,
    winy,
    winz,
    modelMatrix: Buffer,
    projMatrix: Buffer,
    viewport: Buffer,
    objx: Buffer,
    objy,
    objz,
):
    """Map object coordinates to window coordinates.https://www.opengl.org/sdk/docs/man2/xhtml/gluUnProject.xml

    :param winx: Specify the window coordinates to be mapped.
    :type winx: float
    :param modelMatrix: Specifies the current modelview matrix (as from a glGetDoublev call).
    :type modelMatrix: Buffer
    :param projMatrix: Specifies the current projection matrix (as from a glGetDoublev call).
    :type projMatrix: Buffer
    :param viewport: Specifies the current viewport (as from a glGetIntegerv call).
    :type viewport: Buffer
    :param objx: Return the computed object coordinates.
    :type objx: Buffer
    """

GL_2D: float

GL_2_BYTES: float

GL_3D: float

GL_3D_COLOR: float

GL_3D_COLOR_TEXTURE: float

GL_3_BYTES: float

GL_4D_COLOR_TEXTURE: float

GL_4_BYTES: float

GL_ACCUM: float

GL_ACCUM_ALPHA_BITS: float

GL_ACCUM_BLUE_BITS: float

GL_ACCUM_BUFFER_BIT: float

GL_ACCUM_CLEAR_VALUE: float

GL_ACCUM_GREEN_BITS: float

GL_ACCUM_RED_BITS: float

GL_ACTIVE_ATTRIBUTES: float

GL_ACTIVE_ATTRIBUTE_MAX_LENGTH: float

GL_ACTIVE_TEXTURE: float

GL_ACTIVE_UNIFORMS: float

GL_ACTIVE_UNIFORM_BLOCKS: float

GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH: float

GL_ACTIVE_UNIFORM_MAX_LENGTH: float

GL_ADD: float

GL_ADD_SIGNED: float

GL_ALIASED_LINE_WIDTH_RANGE: float

GL_ALIASED_POINT_SIZE_RANGE: float

GL_ALL_ATTRIB_BITS: float

GL_ALPHA: float

GL_ALPHA12: float

GL_ALPHA16: float

GL_ALPHA4: float

GL_ALPHA8: float

GL_ALPHA_BIAS: float

GL_ALPHA_BITS: float

GL_ALPHA_INTEGER: float

GL_ALPHA_SCALE: float

GL_ALPHA_TEST: float

GL_ALPHA_TEST_FUNC: float

GL_ALPHA_TEST_REF: float

GL_ALREADY_SIGNALED: float

GL_ALWAYS: float

GL_AMBIENT: float

GL_AMBIENT_AND_DIFFUSE: float

GL_AND: float

GL_AND_INVERTED: float

GL_AND_REVERSE: float

GL_ANY_SAMPLES_PASSED: float

GL_ARRAY_BUFFER: float

GL_ARRAY_BUFFER_BINDING: float

GL_ATTACHED_SHADERS: float

GL_ATTRIB_STACK_DEPTH: float

GL_AUTO_NORMAL: float

GL_AUX0: float

GL_AUX1: float

GL_AUX2: float

GL_AUX3: float

GL_AUX_BUFFERS: float

GL_BACK: float

GL_BACK_LEFT: float

GL_BACK_RIGHT: float

GL_BGR: float

GL_BGRA: float

GL_BGRA_INTEGER: float

GL_BGR_INTEGER: float

GL_BITMAP: float

GL_BITMAP_TOKEN: float

GL_BLEND: float

GL_BLEND_DST: float

GL_BLEND_DST_ALPHA: float

GL_BLEND_DST_RGB: float

GL_BLEND_EQUATION_ALPHA: float

GL_BLEND_EQUATION_RGB: float

GL_BLEND_SRC: float

GL_BLEND_SRC_ALPHA: float

GL_BLEND_SRC_RGB: float

GL_BLUE: float

GL_BLUE_BIAS: float

GL_BLUE_BITS: float

GL_BLUE_INTEGER: float

GL_BLUE_SCALE: float

GL_BOOL: float

GL_BOOL_VEC2: float

GL_BOOL_VEC3: float

GL_BOOL_VEC4: float

GL_BUFFER_ACCESS: float

GL_BUFFER_ACCESS_FLAGS: float

GL_BUFFER_MAPPED: float

GL_BUFFER_MAP_LENGTH: float

GL_BUFFER_MAP_OFFSET: float

GL_BUFFER_MAP_POINTER: float

GL_BUFFER_SIZE: float

GL_BUFFER_USAGE: float

GL_BYTE: float

GL_C3F_V3F: float

GL_C4F_N3F_V3F: float

GL_C4UB_V2F: float

GL_C4UB_V3F: float

GL_CCW: float

GL_CLAMP: float

GL_CLAMP_FRAGMENT_COLOR: float

GL_CLAMP_READ_COLOR: float

GL_CLAMP_TO_BORDER: float

GL_CLAMP_TO_EDGE: float

GL_CLAMP_VERTEX_COLOR: float

GL_CLEAR: float

GL_CLIENT_ACTIVE_TEXTURE: float

GL_CLIENT_ALL_ATTRIB_BITS: float

GL_CLIENT_ATTRIB_STACK_DEPTH: float

GL_CLIENT_PIXEL_STORE_BIT: float

GL_CLIENT_VERTEX_ARRAY_BIT: float

GL_CLIP_DISTANCE0: float

GL_CLIP_DISTANCE1: float

GL_CLIP_DISTANCE2: float

GL_CLIP_DISTANCE3: float

GL_CLIP_DISTANCE4: float

GL_CLIP_DISTANCE5: float

GL_CLIP_DISTANCE6: float

GL_CLIP_DISTANCE7: float

GL_CLIP_PLANE0: float

GL_CLIP_PLANE1: float

GL_CLIP_PLANE2: float

GL_CLIP_PLANE3: float

GL_CLIP_PLANE4: float

GL_CLIP_PLANE5: float

GL_COEFF: float

GL_COLOR: float

GL_COLOR_ARRAY: float

GL_COLOR_ARRAY_BUFFER_BINDING: float

GL_COLOR_ARRAY_POINTER: float

GL_COLOR_ARRAY_SIZE: float

GL_COLOR_ARRAY_STRIDE: float

GL_COLOR_ARRAY_TYPE: float

GL_COLOR_ATTACHMENT0: float

GL_COLOR_ATTACHMENT1: float

GL_COLOR_ATTACHMENT10: float

GL_COLOR_ATTACHMENT11: float

GL_COLOR_ATTACHMENT12: float

GL_COLOR_ATTACHMENT13: float

GL_COLOR_ATTACHMENT14: float

GL_COLOR_ATTACHMENT15: float

GL_COLOR_ATTACHMENT16: float

GL_COLOR_ATTACHMENT17: float

GL_COLOR_ATTACHMENT18: float

GL_COLOR_ATTACHMENT19: float

GL_COLOR_ATTACHMENT2: float

GL_COLOR_ATTACHMENT20: float

GL_COLOR_ATTACHMENT21: float

GL_COLOR_ATTACHMENT22: float

GL_COLOR_ATTACHMENT23: float

GL_COLOR_ATTACHMENT24: float

GL_COLOR_ATTACHMENT25: float

GL_COLOR_ATTACHMENT26: float

GL_COLOR_ATTACHMENT27: float

GL_COLOR_ATTACHMENT28: float

GL_COLOR_ATTACHMENT29: float

GL_COLOR_ATTACHMENT3: float

GL_COLOR_ATTACHMENT30: float

GL_COLOR_ATTACHMENT31: float

GL_COLOR_ATTACHMENT4: float

GL_COLOR_ATTACHMENT5: float

GL_COLOR_ATTACHMENT6: float

GL_COLOR_ATTACHMENT7: float

GL_COLOR_ATTACHMENT8: float

GL_COLOR_ATTACHMENT9: float

GL_COLOR_BUFFER_BIT: float

GL_COLOR_CLEAR_VALUE: float

GL_COLOR_INDEX: float

GL_COLOR_INDEXES: float

GL_COLOR_LOGIC_OP: float

GL_COLOR_MATERIAL: float

GL_COLOR_MATERIAL_FACE: float

GL_COLOR_MATERIAL_PARAMETER: float

GL_COLOR_SUM: float

GL_COLOR_WRITEMASK: float

GL_COMBINE: float

GL_COMBINE_ALPHA: float

GL_COMBINE_RGB: float

GL_COMPARE_REF_TO_TEXTURE: float

GL_COMPARE_R_TO_TEXTURE: float

GL_COMPILE: float

GL_COMPILE_AND_EXECUTE: float

GL_COMPILE_STATUS: float

GL_COMPRESSED_ALPHA: float

GL_COMPRESSED_INTENSITY: float

GL_COMPRESSED_LUMINANCE: float

GL_COMPRESSED_LUMINANCE_ALPHA: float

GL_COMPRESSED_RED: float

GL_COMPRESSED_RED_RGTC1: float

GL_COMPRESSED_RG: float

GL_COMPRESSED_RGB: float

GL_COMPRESSED_RGBA: float

GL_COMPRESSED_RG_RGTC2: float

GL_COMPRESSED_SIGNED_RED_RGTC1: float

GL_COMPRESSED_SIGNED_RG_RGTC2: float

GL_COMPRESSED_SLUMINANCE: float

GL_COMPRESSED_SLUMINANCE_ALPHA: float

GL_COMPRESSED_SRGB: float

GL_COMPRESSED_SRGB_ALPHA: float

GL_COMPRESSED_TEXTURE_FORMATS: float

GL_CONDITION_SATISFIED: float

GL_CONSTANT: float

GL_CONSTANT_ALPHA: float

GL_CONSTANT_ATTENUATION: float

GL_CONSTANT_COLOR: float

GL_CONTEXT_COMPATIBILITY_PROFILE_BIT: float

GL_CONTEXT_CORE_PROFILE_BIT: float

GL_CONTEXT_FLAGS: float

GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT: float

GL_CONTEXT_PROFILE_MASK: float

GL_COORD_REPLACE: float

GL_COPY: float

GL_COPY_INVERTED: float

GL_COPY_PIXEL_TOKEN: float

GL_COPY_READ_BUFFER: float

GL_COPY_WRITE_BUFFER: float

GL_CULL_FACE: float

GL_CULL_FACE_MODE: float

GL_CURRENT_BIT: float

GL_CURRENT_COLOR: float

GL_CURRENT_FOG_COORD: float

GL_CURRENT_FOG_COORDINATE: float

GL_CURRENT_INDEX: float

GL_CURRENT_NORMAL: float

GL_CURRENT_PROGRAM: float

GL_CURRENT_QUERY: float

GL_CURRENT_RASTER_COLOR: float

GL_CURRENT_RASTER_DISTANCE: float

GL_CURRENT_RASTER_INDEX: float

GL_CURRENT_RASTER_POSITION: float

GL_CURRENT_RASTER_POSITION_VALID: float

GL_CURRENT_RASTER_SECONDARY_COLOR: float

GL_CURRENT_RASTER_TEXTURE_COORDS: float

GL_CURRENT_SECONDARY_COLOR: float

GL_CURRENT_TEXTURE_COORDS: float

GL_CURRENT_VERTEX_ATTRIB: float

GL_CW: float

GL_DECAL: float

GL_DECR: float

GL_DECR_WRAP: float

GL_DELETE_STATUS: float

GL_DEPTH: float

GL_DEPTH24_STENCIL8: float

GL_DEPTH32F_STENCIL8: float

GL_DEPTH_ATTACHMENT: float

GL_DEPTH_BIAS: float

GL_DEPTH_BITS: float

GL_DEPTH_BUFFER_BIT: float

GL_DEPTH_CLAMP: float

GL_DEPTH_CLEAR_VALUE: float

GL_DEPTH_COMPONENT: float

GL_DEPTH_COMPONENT16: float

GL_DEPTH_COMPONENT24: float

GL_DEPTH_COMPONENT32: float

GL_DEPTH_COMPONENT32F: float

GL_DEPTH_FUNC: float

GL_DEPTH_RANGE: float

GL_DEPTH_SCALE: float

GL_DEPTH_STENCIL: float

GL_DEPTH_STENCIL_ATTACHMENT: float

GL_DEPTH_TEST: float

GL_DEPTH_TEXTURE_MODE: float

GL_DEPTH_WRITEMASK: float

GL_DIFFUSE: float

GL_DITHER: float

GL_DOMAIN: float

GL_DONT_CARE: float

GL_DOT3_RGB: float

GL_DOT3_RGBA: float

GL_DOUBLE: float

GL_DOUBLEBUFFER: float

GL_DRAW_BUFFER: float

GL_DRAW_BUFFER0: float

GL_DRAW_BUFFER1: float

GL_DRAW_BUFFER10: float

GL_DRAW_BUFFER11: float

GL_DRAW_BUFFER12: float

GL_DRAW_BUFFER13: float

GL_DRAW_BUFFER14: float

GL_DRAW_BUFFER15: float

GL_DRAW_BUFFER2: float

GL_DRAW_BUFFER3: float

GL_DRAW_BUFFER4: float

GL_DRAW_BUFFER5: float

GL_DRAW_BUFFER6: float

GL_DRAW_BUFFER7: float

GL_DRAW_BUFFER8: float

GL_DRAW_BUFFER9: float

GL_DRAW_FRAMEBUFFER: float

GL_DRAW_FRAMEBUFFER_BINDING: float

GL_DRAW_PIXEL_TOKEN: float

GL_DST_ALPHA: float

GL_DST_COLOR: float

GL_DYNAMIC_COPY: float

GL_DYNAMIC_DRAW: float

GL_DYNAMIC_READ: float

GL_EDGE_FLAG: float

GL_EDGE_FLAG_ARRAY: float

GL_EDGE_FLAG_ARRAY_BUFFER_BINDING: float

GL_EDGE_FLAG_ARRAY_POINTER: float

GL_EDGE_FLAG_ARRAY_STRIDE: float

GL_ELEMENT_ARRAY_BUFFER: float

GL_ELEMENT_ARRAY_BUFFER_BINDING: float

GL_EMISSION: float

GL_ENABLE_BIT: float

GL_EQUAL: float

GL_EQUIV: float

GL_EVAL_BIT: float

GL_EXP: float

GL_EXP2: float

GL_EXTENSIONS: float

GL_EYE_LINEAR: float

GL_EYE_PLANE: float

GL_FALSE: float

GL_FASTEST: float

GL_FEEDBACK: float

GL_FEEDBACK_BUFFER_POINTER: float

GL_FEEDBACK_BUFFER_SIZE: float

GL_FEEDBACK_BUFFER_TYPE: float

GL_FILL: float

GL_FIRST_VERTEX_CONVENTION: float

GL_FIXED_ONLY: float

GL_FLAT: float

GL_FLOAT: float

GL_FLOAT_32_UNSIGNED_INT_24_8_REV: float

GL_FLOAT_MAT2: float

GL_FLOAT_MAT2x3: float

GL_FLOAT_MAT2x4: float

GL_FLOAT_MAT3: float

GL_FLOAT_MAT3x2: float

GL_FLOAT_MAT3x4: float

GL_FLOAT_MAT4: float

GL_FLOAT_MAT4x2: float

GL_FLOAT_MAT4x3: float

GL_FLOAT_VEC2: float

GL_FLOAT_VEC3: float

GL_FLOAT_VEC4: float

GL_FOG: float

GL_FOG_BIT: float

GL_FOG_COLOR: float

GL_FOG_COORD: float

GL_FOG_COORDINATE: float

GL_FOG_COORDINATE_ARRAY: float

GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING: float

GL_FOG_COORDINATE_ARRAY_POINTER: float

GL_FOG_COORDINATE_ARRAY_STRIDE: float

GL_FOG_COORDINATE_ARRAY_TYPE: float

GL_FOG_COORDINATE_SOURCE: float

GL_FOG_COORD_ARRAY: float

GL_FOG_COORD_ARRAY_BUFFER_BINDING: float

GL_FOG_COORD_ARRAY_POINTER: float

GL_FOG_COORD_ARRAY_STRIDE: float

GL_FOG_COORD_ARRAY_TYPE: float

GL_FOG_COORD_SRC: float

GL_FOG_DENSITY: float

GL_FOG_END: float

GL_FOG_HINT: float

GL_FOG_INDEX: float

GL_FOG_MODE: float

GL_FOG_START: float

GL_FRAGMENT_DEPTH: float

GL_FRAGMENT_SHADER: float

GL_FRAGMENT_SHADER_DERIVATIVE_HINT: float

GL_FRAMEBUFFER: float

GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING: float

GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE: float

GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_LAYERED: float

GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: float

GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: float

GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE: float

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: float

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: float

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: float

GL_FRAMEBUFFER_BINDING: float

GL_FRAMEBUFFER_COMPLETE: float

GL_FRAMEBUFFER_DEFAULT: float

GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: float

GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER: float

GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS: float

GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: float

GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE: float

GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER: float

GL_FRAMEBUFFER_SRGB: float

GL_FRAMEBUFFER_UNDEFINED: float

GL_FRAMEBUFFER_UNSUPPORTED: float

GL_FRONT: float

GL_FRONT_AND_BACK: float

GL_FRONT_FACE: float

GL_FRONT_LEFT: float

GL_FRONT_RIGHT: float

GL_FUNC_ADD: float

GL_FUNC_REVERSE_SUBTRACT: float

GL_FUNC_SUBTRACT: float

GL_GENERATE_MIPMAP: float

GL_GENERATE_MIPMAP_HINT: float

GL_GEOMETRY_INPUT_TYPE: float

GL_GEOMETRY_OUTPUT_TYPE: float

GL_GEOMETRY_SHADER: float

GL_GEOMETRY_VERTICES_OUT: float

GL_GEQUAL: float

GL_GREATER: float

GL_GREEN: float

GL_GREEN_BIAS: float

GL_GREEN_BITS: float

GL_GREEN_INTEGER: float

GL_GREEN_SCALE: float

GL_HALF_FLOAT: float

GL_HINT_BIT: float

GL_INCR: float

GL_INCR_WRAP: float

GL_INDEX: float

GL_INDEX_ARRAY: float

GL_INDEX_ARRAY_BUFFER_BINDING: float

GL_INDEX_ARRAY_POINTER: float

GL_INDEX_ARRAY_STRIDE: float

GL_INDEX_ARRAY_TYPE: float

GL_INDEX_BITS: float

GL_INDEX_CLEAR_VALUE: float

GL_INDEX_LOGIC_OP: float

GL_INDEX_MODE: float

GL_INDEX_OFFSET: float

GL_INDEX_SHIFT: float

GL_INDEX_WRITEMASK: float

GL_INFO_LOG_LENGTH: float

GL_INT: float

GL_INTENSITY: float

GL_INTENSITY12: float

GL_INTENSITY16: float

GL_INTENSITY4: float

GL_INTENSITY8: float

GL_INTERLEAVED_ATTRIBS: float

GL_INTERPOLATE: float

GL_INT_2_10_10_10_REV: float

GL_INT_SAMPLER_1D: float

GL_INT_SAMPLER_1D_ARRAY: float

GL_INT_SAMPLER_2D: float

GL_INT_SAMPLER_2D_ARRAY: float

GL_INT_SAMPLER_2D_MULTISAMPLE: float

GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: float

GL_INT_SAMPLER_2D_RECT: float

GL_INT_SAMPLER_3D: float

GL_INT_SAMPLER_BUFFER: float

GL_INT_SAMPLER_CUBE: float

GL_INT_VEC2: float

GL_INT_VEC3: float

GL_INT_VEC4: float

GL_INVALID_ENUM: float

GL_INVALID_FRAMEBUFFER_OPERATION: float

GL_INVALID_INDEX: float

GL_INVALID_OPERATION: float

GL_INVALID_VALUE: float

GL_INVERT: float

GL_KEEP: float

GL_LAST_VERTEX_CONVENTION: float

GL_LEFT: float

GL_LEQUAL: float

GL_LESS: float

GL_LIGHT0: float

GL_LIGHT1: float

GL_LIGHT2: float

GL_LIGHT3: float

GL_LIGHT4: float

GL_LIGHT5: float

GL_LIGHT6: float

GL_LIGHT7: float

GL_LIGHTING: float

GL_LIGHTING_BIT: float

GL_LIGHT_MODEL_AMBIENT: float

GL_LIGHT_MODEL_COLOR_CONTROL: float

GL_LIGHT_MODEL_LOCAL_VIEWER: float

GL_LIGHT_MODEL_TWO_SIDE: float

GL_LINE: float

GL_LINEAR: float

GL_LINEAR_ATTENUATION: float

GL_LINEAR_MIPMAP_LINEAR: float

GL_LINEAR_MIPMAP_NEAREST: float

GL_LINES: float

GL_LINES_ADJACENCY: float

GL_LINE_BIT: float

GL_LINE_LOOP: float

GL_LINE_RESET_TOKEN: float

GL_LINE_SMOOTH: float

GL_LINE_SMOOTH_HINT: float

GL_LINE_STIPPLE: float

GL_LINE_STIPPLE_PATTERN: float

GL_LINE_STIPPLE_REPEAT: float

GL_LINE_STRIP: float

GL_LINE_STRIP_ADJACENCY: float

GL_LINE_TOKEN: float

GL_LINE_WIDTH: float

GL_LINE_WIDTH_GRANULARITY: float

GL_LINE_WIDTH_RANGE: float

GL_LINK_STATUS: float

GL_LIST_BASE: float

GL_LIST_BIT: float

GL_LIST_INDEX: float

GL_LIST_MODE: float

GL_LOAD: float

GL_LOGIC_OP: float

GL_LOGIC_OP_MODE: float

GL_LOWER_LEFT: float

GL_LUMINANCE: float

GL_LUMINANCE12: float

GL_LUMINANCE12_ALPHA12: float

GL_LUMINANCE12_ALPHA4: float

GL_LUMINANCE16: float

GL_LUMINANCE16_ALPHA16: float

GL_LUMINANCE4: float

GL_LUMINANCE4_ALPHA4: float

GL_LUMINANCE6_ALPHA2: float

GL_LUMINANCE8: float

GL_LUMINANCE8_ALPHA8: float

GL_LUMINANCE_ALPHA: float

GL_MAJOR_VERSION: float

GL_MAP1_COLOR_4: float

GL_MAP1_GRID_DOMAIN: float

GL_MAP1_GRID_SEGMENTS: float

GL_MAP1_INDEX: float

GL_MAP1_NORMAL: float

GL_MAP1_TEXTURE_COORD_1: float

GL_MAP1_TEXTURE_COORD_2: float

GL_MAP1_TEXTURE_COORD_3: float

GL_MAP1_TEXTURE_COORD_4: float

GL_MAP1_VERTEX_3: float

GL_MAP1_VERTEX_4: float

GL_MAP2_COLOR_4: float

GL_MAP2_GRID_DOMAIN: float

GL_MAP2_GRID_SEGMENTS: float

GL_MAP2_INDEX: float

GL_MAP2_NORMAL: float

GL_MAP2_TEXTURE_COORD_1: float

GL_MAP2_TEXTURE_COORD_2: float

GL_MAP2_TEXTURE_COORD_3: float

GL_MAP2_TEXTURE_COORD_4: float

GL_MAP2_VERTEX_3: float

GL_MAP2_VERTEX_4: float

GL_MAP_COLOR: float

GL_MAP_FLUSH_EXPLICIT_BIT: float

GL_MAP_INVALIDATE_BUFFER_BIT: float

GL_MAP_INVALIDATE_RANGE_BIT: float

GL_MAP_READ_BIT: float

GL_MAP_STENCIL: float

GL_MAP_UNSYNCHRONIZED_BIT: float

GL_MAP_WRITE_BIT: float

GL_MATRIX_MODE: float

GL_MAX: float

GL_MAX_3D_TEXTURE_SIZE: float

GL_MAX_ARRAY_TEXTURE_LAYERS: float

GL_MAX_ATTRIB_STACK_DEPTH: float

GL_MAX_CLIENT_ATTRIB_STACK_DEPTH: float

GL_MAX_CLIP_DISTANCES: float

GL_MAX_CLIP_PLANES: float

GL_MAX_COLOR_ATTACHMENTS: float

GL_MAX_COLOR_TEXTURE_SAMPLES: float

GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS: float

GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS: float

GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS: float

GL_MAX_COMBINED_UNIFORM_BLOCKS: float

GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS: float

GL_MAX_CUBE_MAP_TEXTURE_SIZE: float

GL_MAX_DEPTH_TEXTURE_SAMPLES: float

GL_MAX_DRAW_BUFFERS: float

GL_MAX_DUAL_SOURCE_DRAW_BUFFERS: float

GL_MAX_ELEMENTS_INDICES: float

GL_MAX_ELEMENTS_VERTICES: float

GL_MAX_EVAL_ORDER: float

GL_MAX_FRAGMENT_INPUT_COMPONENTS: float

GL_MAX_FRAGMENT_UNIFORM_BLOCKS: float

GL_MAX_FRAGMENT_UNIFORM_COMPONENTS: float

GL_MAX_GEOMETRY_INPUT_COMPONENTS: float

GL_MAX_GEOMETRY_OUTPUT_COMPONENTS: float

GL_MAX_GEOMETRY_OUTPUT_VERTICES: float

GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS: float

GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS: float

GL_MAX_GEOMETRY_UNIFORM_BLOCKS: float

GL_MAX_GEOMETRY_UNIFORM_COMPONENTS: float

GL_MAX_INTEGER_SAMPLES: float

GL_MAX_LIGHTS: float

GL_MAX_LIST_NESTING: float

GL_MAX_MODELVIEW_STACK_DEPTH: float

GL_MAX_NAME_STACK_DEPTH: float

GL_MAX_PIXEL_MAP_TABLE: float

GL_MAX_PROGRAM_TEXEL_OFFSET: float

GL_MAX_PROJECTION_STACK_DEPTH: float

GL_MAX_RECTANGLE_TEXTURE_SIZE: float

GL_MAX_RENDERBUFFER_SIZE: float

GL_MAX_SAMPLES: float

GL_MAX_SAMPLE_MASK_WORDS: float

GL_MAX_SERVER_WAIT_TIMEOUT: float

GL_MAX_TEXTURE_BUFFER_SIZE: float

GL_MAX_TEXTURE_COORDS: float

GL_MAX_TEXTURE_IMAGE_UNITS: float

GL_MAX_TEXTURE_LOD_BIAS: float

GL_MAX_TEXTURE_SIZE: float

GL_MAX_TEXTURE_STACK_DEPTH: float

GL_MAX_TEXTURE_UNITS: float

GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS: float

GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS: float

GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS: float

GL_MAX_UNIFORM_BLOCK_SIZE: float

GL_MAX_UNIFORM_BUFFER_BINDINGS: float

GL_MAX_VARYING_COMPONENTS: float

GL_MAX_VARYING_FLOATS: float

GL_MAX_VERTEX_ATTRIBS: float

GL_MAX_VERTEX_OUTPUT_COMPONENTS: float

GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS: float

GL_MAX_VERTEX_UNIFORM_BLOCKS: float

GL_MAX_VERTEX_UNIFORM_COMPONENTS: float

GL_MAX_VIEWPORT_DIMS: float

GL_MIN: float

GL_MINOR_VERSION: float

GL_MIN_PROGRAM_TEXEL_OFFSET: float

GL_MIRRORED_REPEAT: float

GL_MODELVIEW: float

GL_MODELVIEW_MATRIX: float

GL_MODELVIEW_STACK_DEPTH: float

GL_MODULATE: float

GL_MULT: float

GL_MULTISAMPLE: float

GL_MULTISAMPLE_BIT: float

GL_N3F_V3F: float

GL_NAME_STACK_DEPTH: float

GL_NAND: float

GL_NEAREST: float

GL_NEAREST_MIPMAP_LINEAR: float

GL_NEAREST_MIPMAP_NEAREST: float

GL_NEVER: float

GL_NICEST: float

GL_NONE: float

GL_NOOP: float

GL_NOR: float

GL_NORMALIZE: float

GL_NORMAL_ARRAY: float

GL_NORMAL_ARRAY_BUFFER_BINDING: float

GL_NORMAL_ARRAY_POINTER: float

GL_NORMAL_ARRAY_STRIDE: float

GL_NORMAL_ARRAY_TYPE: float

GL_NORMAL_MAP: float

GL_NOTEQUAL: float

GL_NO_ERROR: float

GL_NUM_COMPRESSED_TEXTURE_FORMATS: float

GL_NUM_EXTENSIONS: float

GL_OBJECT_LINEAR: float

GL_OBJECT_PLANE: float

GL_OBJECT_TYPE: float

GL_ONE: float

GL_ONE_MINUS_CONSTANT_ALPHA: float

GL_ONE_MINUS_CONSTANT_COLOR: float

GL_ONE_MINUS_DST_ALPHA: float

GL_ONE_MINUS_DST_COLOR: float

GL_ONE_MINUS_SRC1_ALPHA: float

GL_ONE_MINUS_SRC1_COLOR: float

GL_ONE_MINUS_SRC_ALPHA: float

GL_ONE_MINUS_SRC_COLOR: float

GL_OPERAND0_ALPHA: float

GL_OPERAND0_RGB: float

GL_OPERAND1_ALPHA: float

GL_OPERAND1_RGB: float

GL_OPERAND2_ALPHA: float

GL_OPERAND2_RGB: float

GL_OR: float

GL_ORDER: float

GL_OR_INVERTED: float

GL_OR_REVERSE: float

GL_OUT_OF_MEMORY: float

GL_PACK_ALIGNMENT: float

GL_PACK_IMAGE_HEIGHT: float

GL_PACK_LSB_FIRST: float

GL_PACK_ROW_LENGTH: float

GL_PACK_SKIP_IMAGES: float

GL_PACK_SKIP_PIXELS: float

GL_PACK_SKIP_ROWS: float

GL_PACK_SWAP_BYTES: float

GL_PASS_THROUGH_TOKEN: float

GL_PERSPECTIVE_CORRECTION_HINT: float

GL_PIXEL_MAP_A_TO_A: float

GL_PIXEL_MAP_A_TO_A_SIZE: float

GL_PIXEL_MAP_B_TO_B: float

GL_PIXEL_MAP_B_TO_B_SIZE: float

GL_PIXEL_MAP_G_TO_G: float

GL_PIXEL_MAP_G_TO_G_SIZE: float

GL_PIXEL_MAP_I_TO_A: float

GL_PIXEL_MAP_I_TO_A_SIZE: float

GL_PIXEL_MAP_I_TO_B: float

GL_PIXEL_MAP_I_TO_B_SIZE: float

GL_PIXEL_MAP_I_TO_G: float

GL_PIXEL_MAP_I_TO_G_SIZE: float

GL_PIXEL_MAP_I_TO_I: float

GL_PIXEL_MAP_I_TO_I_SIZE: float

GL_PIXEL_MAP_I_TO_R: float

GL_PIXEL_MAP_I_TO_R_SIZE: float

GL_PIXEL_MAP_R_TO_R: float

GL_PIXEL_MAP_R_TO_R_SIZE: float

GL_PIXEL_MAP_S_TO_S: float

GL_PIXEL_MAP_S_TO_S_SIZE: float

GL_PIXEL_MODE_BIT: float

GL_PIXEL_PACK_BUFFER: float

GL_PIXEL_PACK_BUFFER_BINDING: float

GL_PIXEL_UNPACK_BUFFER: float

GL_PIXEL_UNPACK_BUFFER_BINDING: float

GL_POINT: float

GL_POINTS: float

GL_POINT_BIT: float

GL_POINT_DISTANCE_ATTENUATION: float

GL_POINT_FADE_THRESHOLD_SIZE: float

GL_POINT_SIZE: float

GL_POINT_SIZE_GRANULARITY: float

GL_POINT_SIZE_MAX: float

GL_POINT_SIZE_MIN: float

GL_POINT_SIZE_RANGE: float

GL_POINT_SMOOTH: float

GL_POINT_SMOOTH_HINT: float

GL_POINT_SPRITE: float

GL_POINT_SPRITE_COORD_ORIGIN: float

GL_POINT_TOKEN: float

GL_POLYGON: float

GL_POLYGON_BIT: float

GL_POLYGON_MODE: float

GL_POLYGON_OFFSET_FACTOR: float

GL_POLYGON_OFFSET_FILL: float

GL_POLYGON_OFFSET_LINE: float

GL_POLYGON_OFFSET_POINT: float

GL_POLYGON_OFFSET_UNITS: float

GL_POLYGON_SMOOTH: float

GL_POLYGON_SMOOTH_HINT: float

GL_POLYGON_STIPPLE: float

GL_POLYGON_STIPPLE_BIT: float

GL_POLYGON_TOKEN: float

GL_POSITION: float

GL_PREVIOUS: float

GL_PRIMARY_COLOR: float

GL_PRIMITIVES_GENERATED: float

GL_PRIMITIVE_RESTART: float

GL_PRIMITIVE_RESTART_INDEX: float

GL_PROGRAM_POINT_SIZE: float

GL_PROJECTION: float

GL_PROJECTION_MATRIX: float

GL_PROJECTION_STACK_DEPTH: float

GL_PROVOKING_VERTEX: float

GL_PROXY_TEXTURE_1D: float

GL_PROXY_TEXTURE_1D_ARRAY: float

GL_PROXY_TEXTURE_2D: float

GL_PROXY_TEXTURE_2D_ARRAY: float

GL_PROXY_TEXTURE_2D_MULTISAMPLE: float

GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY: float

GL_PROXY_TEXTURE_3D: float

GL_PROXY_TEXTURE_CUBE_MAP: float

GL_PROXY_TEXTURE_RECTANGLE: float

GL_Q: float

GL_QUADRATIC_ATTENUATION: float

GL_QUADS: float

GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION: float

GL_QUAD_STRIP: float

GL_QUERY_BY_REGION_NO_WAIT: float

GL_QUERY_BY_REGION_WAIT: float

GL_QUERY_COUNTER_BITS: float

GL_QUERY_NO_WAIT: float

GL_QUERY_RESULT: float

GL_QUERY_RESULT_AVAILABLE: float

GL_QUERY_WAIT: float

GL_R: float

GL_R11F_G11F_B10F: float

GL_R16: float

GL_R16F: float

GL_R16I: float

GL_R16UI: float

GL_R16_SNORM: float

GL_R32F: float

GL_R32I: float

GL_R32UI: float

GL_R3_G3_B2: float

GL_R8: float

GL_R8I: float

GL_R8UI: float

GL_R8_SNORM: float

GL_RASTERIZER_DISCARD: float

GL_READ_BUFFER: float

GL_READ_FRAMEBUFFER: float

GL_READ_FRAMEBUFFER_BINDING: float

GL_READ_ONLY: float

GL_READ_WRITE: float

GL_RED: float

GL_RED_BIAS: float

GL_RED_BITS: float

GL_RED_INTEGER: float

GL_RED_SCALE: float

GL_REFLECTION_MAP: float

GL_RENDER: float

GL_RENDERBUFFER: float

GL_RENDERBUFFER_ALPHA_SIZE: float

GL_RENDERBUFFER_BINDING: float

GL_RENDERBUFFER_BLUE_SIZE: float

GL_RENDERBUFFER_DEPTH_SIZE: float

GL_RENDERBUFFER_GREEN_SIZE: float

GL_RENDERBUFFER_HEIGHT: float

GL_RENDERBUFFER_INTERNAL_FORMAT: float

GL_RENDERBUFFER_RED_SIZE: float

GL_RENDERBUFFER_SAMPLES: float

GL_RENDERBUFFER_STENCIL_SIZE: float

GL_RENDERBUFFER_WIDTH: float

GL_RENDERER: float

GL_RENDER_MODE: float

GL_REPEAT: float

GL_REPLACE: float

GL_RESCALE_NORMAL: float

GL_RETURN: float

GL_RG: float

GL_RG16: float

GL_RG16F: float

GL_RG16I: float

GL_RG16UI: float

GL_RG16_SNORM: float

GL_RG32F: float

GL_RG32I: float

GL_RG32UI: float

GL_RG8: float

GL_RG8I: float

GL_RG8UI: float

GL_RG8_SNORM: float

GL_RGB: float

GL_RGB10: float

GL_RGB10_A2: float

GL_RGB10_A2UI: float

GL_RGB12: float

GL_RGB16: float

GL_RGB16F: float

GL_RGB16I: float

GL_RGB16UI: float

GL_RGB16_SNORM: float

GL_RGB32F: float

GL_RGB32I: float

GL_RGB32UI: float

GL_RGB4: float

GL_RGB5: float

GL_RGB5_A1: float

GL_RGB8: float

GL_RGB8I: float

GL_RGB8UI: float

GL_RGB8_SNORM: float

GL_RGB9_E5: float

GL_RGBA: float

GL_RGBA12: float

GL_RGBA16: float

GL_RGBA16F: float

GL_RGBA16I: float

GL_RGBA16UI: float

GL_RGBA16_SNORM: float

GL_RGBA2: float

GL_RGBA32F: float

GL_RGBA32I: float

GL_RGBA32UI: float

GL_RGBA4: float

GL_RGBA8: float

GL_RGBA8I: float

GL_RGBA8UI: float

GL_RGBA8_SNORM: float

GL_RGBA_INTEGER: float

GL_RGBA_MODE: float

GL_RGB_INTEGER: float

GL_RGB_SCALE: float

GL_RG_INTEGER: float

GL_RIGHT: float

GL_S: float

GL_SAMPLER_1D: float

GL_SAMPLER_1D_ARRAY: float

GL_SAMPLER_1D_ARRAY_SHADOW: float

GL_SAMPLER_1D_SHADOW: float

GL_SAMPLER_2D: float

GL_SAMPLER_2D_ARRAY: float

GL_SAMPLER_2D_ARRAY_SHADOW: float

GL_SAMPLER_2D_MULTISAMPLE: float

GL_SAMPLER_2D_MULTISAMPLE_ARRAY: float

GL_SAMPLER_2D_RECT: float

GL_SAMPLER_2D_RECT_SHADOW: float

GL_SAMPLER_2D_SHADOW: float

GL_SAMPLER_3D: float

GL_SAMPLER_BINDING: float

GL_SAMPLER_BUFFER: float

GL_SAMPLER_CUBE: float

GL_SAMPLER_CUBE_SHADOW: float

GL_SAMPLES: float

GL_SAMPLES_PASSED: float

GL_SAMPLE_ALPHA_TO_COVERAGE: float

GL_SAMPLE_ALPHA_TO_ONE: float

GL_SAMPLE_BUFFERS: float

GL_SAMPLE_COVERAGE: float

GL_SAMPLE_COVERAGE_INVERT: float

GL_SAMPLE_COVERAGE_VALUE: float

GL_SAMPLE_MASK: float

GL_SAMPLE_MASK_VALUE: float

GL_SAMPLE_POSITION: float

GL_SCISSOR_BIT: float

GL_SCISSOR_BOX: float

GL_SCISSOR_TEST: float

GL_SECONDARY_COLOR_ARRAY: float

GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING: float

GL_SECONDARY_COLOR_ARRAY_POINTER: float

GL_SECONDARY_COLOR_ARRAY_SIZE: float

GL_SECONDARY_COLOR_ARRAY_STRIDE: float

GL_SECONDARY_COLOR_ARRAY_TYPE: float

GL_SELECT: float

GL_SELECTION_BUFFER_POINTER: float

GL_SELECTION_BUFFER_SIZE: float

GL_SEPARATE_ATTRIBS: float

GL_SEPARATE_SPECULAR_COLOR: float

GL_SET: float

GL_SHADER_SOURCE_LENGTH: float

GL_SHADER_TYPE: float

GL_SHADE_MODEL: float

GL_SHADING_LANGUAGE_VERSION: float

GL_SHININESS: float

GL_SHORT: float

GL_SIGNALED: float

GL_SIGNED_NORMALIZED: float

GL_SINGLE_COLOR: float

GL_SLUMINANCE: float

GL_SLUMINANCE8: float

GL_SLUMINANCE8_ALPHA8: float

GL_SLUMINANCE_ALPHA: float

GL_SMOOTH: float

GL_SMOOTH_LINE_WIDTH_GRANULARITY: float

GL_SMOOTH_LINE_WIDTH_RANGE: float

GL_SMOOTH_POINT_SIZE_GRANULARITY: float

GL_SMOOTH_POINT_SIZE_RANGE: float

GL_SOURCE0_ALPHA: float

GL_SOURCE0_RGB: float

GL_SOURCE1_ALPHA: float

GL_SOURCE1_RGB: float

GL_SOURCE2_ALPHA: float

GL_SOURCE2_RGB: float

GL_SPECULAR: float

GL_SPHERE_MAP: float

GL_SPOT_CUTOFF: float

GL_SPOT_DIRECTION: float

GL_SPOT_EXPONENT: float

GL_SRC0_ALPHA: float

GL_SRC0_RGB: float

GL_SRC1_ALPHA: float

GL_SRC1_COLOR: float

GL_SRC1_RGB: float

GL_SRC2_ALPHA: float

GL_SRC2_RGB: float

GL_SRC_ALPHA: float

GL_SRC_ALPHA_SATURATE: float

GL_SRC_COLOR: float

GL_SRGB: float

GL_SRGB8: float

GL_SRGB8_ALPHA8: float

GL_SRGB_ALPHA: float

GL_STACK_OVERFLOW: float

GL_STACK_UNDERFLOW: float

GL_STATIC_COPY: float

GL_STATIC_DRAW: float

GL_STATIC_READ: float

GL_STENCIL: float

GL_STENCIL_ATTACHMENT: float

GL_STENCIL_BACK_FAIL: float

GL_STENCIL_BACK_FUNC: float

GL_STENCIL_BACK_PASS_DEPTH_FAIL: float

GL_STENCIL_BACK_PASS_DEPTH_PASS: float

GL_STENCIL_BACK_REF: float

GL_STENCIL_BACK_VALUE_MASK: float

GL_STENCIL_BACK_WRITEMASK: float

GL_STENCIL_BITS: float

GL_STENCIL_BUFFER_BIT: float

GL_STENCIL_CLEAR_VALUE: float

GL_STENCIL_FAIL: float

GL_STENCIL_FUNC: float

GL_STENCIL_INDEX: float

GL_STENCIL_INDEX1: float

GL_STENCIL_INDEX16: float

GL_STENCIL_INDEX4: float

GL_STENCIL_INDEX8: float

GL_STENCIL_PASS_DEPTH_FAIL: float

GL_STENCIL_PASS_DEPTH_PASS: float

GL_STENCIL_REF: float

GL_STENCIL_TEST: float

GL_STENCIL_VALUE_MASK: float

GL_STENCIL_WRITEMASK: float

GL_STEREO: float

GL_STREAM_COPY: float

GL_STREAM_DRAW: float

GL_STREAM_READ: float

GL_SUBPIXEL_BITS: float

GL_SUBTRACT: float

GL_SYNC_CONDITION: float

GL_SYNC_FENCE: float

GL_SYNC_FLAGS: float

GL_SYNC_FLUSH_COMMANDS_BIT: float

GL_SYNC_GPU_COMMANDS_COMPLETE: float

GL_SYNC_STATUS: float

GL_T: float

GL_T2F_C3F_V3F: float

GL_T2F_C4F_N3F_V3F: float

GL_T2F_C4UB_V3F: float

GL_T2F_N3F_V3F: float

GL_T2F_V3F: float

GL_T4F_C4F_N3F_V4F: float

GL_T4F_V4F: float

GL_TEXTURE: float

GL_TEXTURE0: float

GL_TEXTURE1: float

GL_TEXTURE10: float

GL_TEXTURE11: float

GL_TEXTURE12: float

GL_TEXTURE13: float

GL_TEXTURE14: float

GL_TEXTURE15: float

GL_TEXTURE16: float

GL_TEXTURE17: float

GL_TEXTURE18: float

GL_TEXTURE19: float

GL_TEXTURE2: float

GL_TEXTURE20: float

GL_TEXTURE21: float

GL_TEXTURE22: float

GL_TEXTURE23: float

GL_TEXTURE24: float

GL_TEXTURE25: float

GL_TEXTURE26: float

GL_TEXTURE27: float

GL_TEXTURE28: float

GL_TEXTURE29: float

GL_TEXTURE3: float

GL_TEXTURE30: float

GL_TEXTURE31: float

GL_TEXTURE4: float

GL_TEXTURE5: float

GL_TEXTURE6: float

GL_TEXTURE7: float

GL_TEXTURE8: float

GL_TEXTURE9: float

GL_TEXTURE_1D: float

GL_TEXTURE_1D_ARRAY: float

GL_TEXTURE_2D: float

GL_TEXTURE_2D_ARRAY: float

GL_TEXTURE_2D_MULTISAMPLE: float

GL_TEXTURE_2D_MULTISAMPLE_ARRAY: float

GL_TEXTURE_3D: float

GL_TEXTURE_ALPHA_SIZE: float

GL_TEXTURE_ALPHA_TYPE: float

GL_TEXTURE_BASE_LEVEL: float

GL_TEXTURE_BINDING_1D: float

GL_TEXTURE_BINDING_1D_ARRAY: float

GL_TEXTURE_BINDING_2D: float

GL_TEXTURE_BINDING_2D_ARRAY: float

GL_TEXTURE_BINDING_2D_MULTISAMPLE: float

GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY: float

GL_TEXTURE_BINDING_3D: float

GL_TEXTURE_BINDING_BUFFER: float

GL_TEXTURE_BINDING_CUBE_MAP: float

GL_TEXTURE_BINDING_RECTANGLE: float

GL_TEXTURE_BIT: float

GL_TEXTURE_BLUE_SIZE: float

GL_TEXTURE_BLUE_TYPE: float

GL_TEXTURE_BORDER: float

GL_TEXTURE_BORDER_COLOR: float

GL_TEXTURE_BUFFER: float

GL_TEXTURE_BUFFER_DATA_STORE_BINDING: float

GL_TEXTURE_COMPARE_FUNC: float

GL_TEXTURE_COMPARE_MODE: float

GL_TEXTURE_COMPONENTS: float

GL_TEXTURE_COMPRESSED: float

GL_TEXTURE_COMPRESSED_IMAGE_SIZE: float

GL_TEXTURE_COMPRESSION_HINT: float

GL_TEXTURE_COORD_ARRAY: float

GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING: float

GL_TEXTURE_COORD_ARRAY_POINTER: float

GL_TEXTURE_COORD_ARRAY_SIZE: float

GL_TEXTURE_COORD_ARRAY_STRIDE: float

GL_TEXTURE_COORD_ARRAY_TYPE: float

GL_TEXTURE_CUBE_MAP: float

GL_TEXTURE_CUBE_MAP_NEGATIVE_X: float

GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: float

GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: float

GL_TEXTURE_CUBE_MAP_POSITIVE_X: float

GL_TEXTURE_CUBE_MAP_POSITIVE_Y: float

GL_TEXTURE_CUBE_MAP_POSITIVE_Z: float

GL_TEXTURE_CUBE_MAP_SEAMLESS: float

GL_TEXTURE_DEPTH: float

GL_TEXTURE_DEPTH_SIZE: float

GL_TEXTURE_DEPTH_TYPE: float

GL_TEXTURE_ENV: float

GL_TEXTURE_ENV_COLOR: float

GL_TEXTURE_ENV_MODE: float

GL_TEXTURE_FILTER_CONTROL: float

GL_TEXTURE_FIXED_SAMPLE_LOCATIONS: float

GL_TEXTURE_GEN_MODE: float

GL_TEXTURE_GEN_Q: float

GL_TEXTURE_GEN_R: float

GL_TEXTURE_GEN_S: float

GL_TEXTURE_GEN_T: float

GL_TEXTURE_GREEN_SIZE: float

GL_TEXTURE_GREEN_TYPE: float

GL_TEXTURE_HEIGHT: float

GL_TEXTURE_INTENSITY_SIZE: float

GL_TEXTURE_INTENSITY_TYPE: float

GL_TEXTURE_INTERNAL_FORMAT: float

GL_TEXTURE_LOD_BIAS: float

GL_TEXTURE_LUMINANCE_SIZE: float

GL_TEXTURE_LUMINANCE_TYPE: float

GL_TEXTURE_MAG_FILTER: float

GL_TEXTURE_MATRIX: float

GL_TEXTURE_MAX_LEVEL: float

GL_TEXTURE_MAX_LOD: float

GL_TEXTURE_MIN_FILTER: float

GL_TEXTURE_MIN_LOD: float

GL_TEXTURE_PRIORITY: float

GL_TEXTURE_RECTANGLE: float

GL_TEXTURE_RED_SIZE: float

GL_TEXTURE_RED_TYPE: float

GL_TEXTURE_RESIDENT: float

GL_TEXTURE_SAMPLES: float

GL_TEXTURE_SHARED_SIZE: float

GL_TEXTURE_STACK_DEPTH: float

GL_TEXTURE_STENCIL_SIZE: float

GL_TEXTURE_SWIZZLE_A: float

GL_TEXTURE_SWIZZLE_B: float

GL_TEXTURE_SWIZZLE_G: float

GL_TEXTURE_SWIZZLE_R: float

GL_TEXTURE_SWIZZLE_RGBA: float

GL_TEXTURE_WIDTH: float

GL_TEXTURE_WRAP_R: float

GL_TEXTURE_WRAP_S: float

GL_TEXTURE_WRAP_T: float

GL_TIMEOUT_EXPIRED: float

GL_TIMEOUT_IGNORED: float

GL_TIMESTAMP: float

GL_TIME_ELAPSED: float

GL_TRANSFORM_BIT: float

GL_TRANSFORM_FEEDBACK_BUFFER: float

GL_TRANSFORM_FEEDBACK_BUFFER_BINDING: float

GL_TRANSFORM_FEEDBACK_BUFFER_MODE: float

GL_TRANSFORM_FEEDBACK_BUFFER_SIZE: float

GL_TRANSFORM_FEEDBACK_BUFFER_START: float

GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN: float

GL_TRANSFORM_FEEDBACK_VARYINGS: float

GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH: float

GL_TRANSPOSE_COLOR_MATRIX: float

GL_TRANSPOSE_MODELVIEW_MATRIX: float

GL_TRANSPOSE_PROJECTION_MATRIX: float

GL_TRANSPOSE_TEXTURE_MATRIX: float

GL_TRIANGLES: float

GL_TRIANGLES_ADJACENCY: float

GL_TRIANGLE_FAN: float

GL_TRIANGLE_STRIP: float

GL_TRIANGLE_STRIP_ADJACENCY: float

GL_TRUE: float

GL_UNIFORM_ARRAY_STRIDE: float

GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS: float

GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES: float

GL_UNIFORM_BLOCK_BINDING: float

GL_UNIFORM_BLOCK_DATA_SIZE: float

GL_UNIFORM_BLOCK_INDEX: float

GL_UNIFORM_BLOCK_NAME_LENGTH: float

GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER: float

GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER: float

GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER: float

GL_UNIFORM_BUFFER: float

GL_UNIFORM_BUFFER_BINDING: float

GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT: float

GL_UNIFORM_BUFFER_SIZE: float

GL_UNIFORM_BUFFER_START: float

GL_UNIFORM_IS_ROW_MAJOR: float

GL_UNIFORM_MATRIX_STRIDE: float

GL_UNIFORM_NAME_LENGTH: float

GL_UNIFORM_OFFSET: float

GL_UNIFORM_SIZE: float

GL_UNIFORM_TYPE: float

GL_UNPACK_ALIGNMENT: float

GL_UNPACK_IMAGE_HEIGHT: float

GL_UNPACK_LSB_FIRST: float

GL_UNPACK_ROW_LENGTH: float

GL_UNPACK_SKIP_IMAGES: float

GL_UNPACK_SKIP_PIXELS: float

GL_UNPACK_SKIP_ROWS: float

GL_UNPACK_SWAP_BYTES: float

GL_UNSIGNALED: float

GL_UNSIGNED_BYTE: float

GL_UNSIGNED_BYTE_2_3_3_REV: float

GL_UNSIGNED_BYTE_3_3_2: float

GL_UNSIGNED_INT: float

GL_UNSIGNED_INT_10F_11F_11F_REV: float

GL_UNSIGNED_INT_10_10_10_2: float

GL_UNSIGNED_INT_24_8: float

GL_UNSIGNED_INT_2_10_10_10_REV: float

GL_UNSIGNED_INT_5_9_9_9_REV: float

GL_UNSIGNED_INT_8_8_8_8: float

GL_UNSIGNED_INT_8_8_8_8_REV: float

GL_UNSIGNED_INT_SAMPLER_1D: float

GL_UNSIGNED_INT_SAMPLER_1D_ARRAY: float

GL_UNSIGNED_INT_SAMPLER_2D: float

GL_UNSIGNED_INT_SAMPLER_2D_ARRAY: float

GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE: float

GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: float

GL_UNSIGNED_INT_SAMPLER_2D_RECT: float

GL_UNSIGNED_INT_SAMPLER_3D: float

GL_UNSIGNED_INT_SAMPLER_BUFFER: float

GL_UNSIGNED_INT_SAMPLER_CUBE: float

GL_UNSIGNED_INT_VEC2: float

GL_UNSIGNED_INT_VEC3: float

GL_UNSIGNED_INT_VEC4: float

GL_UNSIGNED_NORMALIZED: float

GL_UNSIGNED_SHORT: float

GL_UNSIGNED_SHORT_1_5_5_5_REV: float

GL_UNSIGNED_SHORT_4_4_4_4: float

GL_UNSIGNED_SHORT_4_4_4_4_REV: float

GL_UNSIGNED_SHORT_5_5_5_1: float

GL_UNSIGNED_SHORT_5_6_5: float

GL_UNSIGNED_SHORT_5_6_5_REV: float

GL_UPPER_LEFT: float

GL_V2F: float

GL_V3F: float

GL_VALIDATE_STATUS: float

GL_VENDOR: float

GL_VERSION: float

GL_VERTEX_ARRAY: float

GL_VERTEX_ARRAY_BINDING: float

GL_VERTEX_ARRAY_BUFFER_BINDING: float

GL_VERTEX_ARRAY_POINTER: float

GL_VERTEX_ARRAY_SIZE: float

GL_VERTEX_ARRAY_STRIDE: float

GL_VERTEX_ARRAY_TYPE: float

GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: float

GL_VERTEX_ATTRIB_ARRAY_DIVISOR: float

GL_VERTEX_ATTRIB_ARRAY_ENABLED: float

GL_VERTEX_ATTRIB_ARRAY_INTEGER: float

GL_VERTEX_ATTRIB_ARRAY_NORMALIZED: float

GL_VERTEX_ATTRIB_ARRAY_POINTER: float

GL_VERTEX_ATTRIB_ARRAY_SIZE: float

GL_VERTEX_ATTRIB_ARRAY_STRIDE: float

GL_VERTEX_ATTRIB_ARRAY_TYPE: float

GL_VERTEX_PROGRAM_POINT_SIZE: float

GL_VERTEX_PROGRAM_TWO_SIDE: float

GL_VERTEX_SHADER: float

GL_VIEWPORT: float

GL_VIEWPORT_BIT: float

GL_WAIT_FAILED: float

GL_WEIGHT_ARRAY_BUFFER_BINDING: float

GL_WRITE_ONLY: float

GL_XOR: float

GL_ZERO: float

GL_ZOOM_X: float

GL_ZOOM_Y: float
