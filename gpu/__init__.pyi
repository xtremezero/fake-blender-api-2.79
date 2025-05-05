"""
This module provides access to materials GLSL shaders.

Submodules:

gpu.offscreen.rst

:maxdepth: 1


--------------------

Module to provide functions concerning the GPU implementation in Blender, in particular
the GLSL shaders that blender generates automatically to render materials in the 3D view
and in the game engine.

[WARNING]
The API provided by this module is subject to change.
The data exposed by the API are are closely related to Blender's internal GLSL code
and may change if the GLSL code is modified (e.g. new uniform type).


--------------------


--------------------

Type of GLSL data.
For shader uniforms, the data type determines which glUniform

 function
variant to use to send the uniform value to the GPU.
For vertex attributes, the data type determines which glVertexAttrib

 function
variant to use to send the vertex attribute to the GPU.

See export_shader


--------------------

Constants that specify the type of uniform used in a GLSL shader.
The uniform type determines the data type, origin and method
of calculation used by Blender to compute the uniform value.

The calculation of some of the uniforms is based on matrices available in the scene:

[QUOTE]
mat4_cam_to_world


    Model matrix of the camera. OpenGL 4x4 matrix that converts
    camera local coordinates to world coordinates. In blender this is obtained from the
    'matrix_world' attribute of the camera object.Some uniform will need the *mat4_world_to_cam*
    matrix computed as the inverse of this matrix.

mat4_object_to_world


    Model matrix of the object that is being rendered. OpenGL 4x4 matric that converts
    object local coordinates to world coordinates. In blender this is obtained from the
    'matrix_world' attribute of the object.Some uniform will need the *mat4_world_to_object* matrix, computed as the inverse of this matrix.

mat4_lamp_to_world


    Model matrix of the lamp lighting the object. OpenGL 4x4 matrix that converts lamp
    local coordinates to world coordinates. In blender this is obtained from the
    'matrix_world' attribute of the lamp object.Some uniform will need the *mat4_world_to_lamp* matrix
    computed as the inverse of this matrix.


[NOTE]
Any uniforms used for view projections or transformations (object, lamp matrices for eg),
can only be set once per frame.


--------------------

[NOTE]
* Object transformations and color must be set before drawing the object.
* There is at most one uniform of these types per shader.



--------------------

[NOTE]
There is one uniform of that type per lamp lighting the material.


--------------------


--------------------


--------------------


--------------------


--------------------

Type of the vertex attribute used in the GLSL shader. Determines the mesh custom data
layer that contains the vertex attribute.


--------------------


--------------------

1. Calculation of the mat4_lamp_to_perspective

 matrix for a spot lamp.
The following pseudo code shows how the mat4_lamp_to_perspective

 matrix is computed
in blender for uniforms of gpu.GPU_DYNAMIC_LAMP_DYNPERSMAT type:
```
# Get the lamp datablock with:
lamp = bpy.data.objects[uniform["lamp"]].data

# Compute the projection matrix:
#  You will need these lamp attributes:
#  lamp.clipsta : near clip plane in world unit
#  lamp.clipend : far clip plane in world unit
#  lamp.spotsize : angle in degree of the spot light

# The size of the projection plane is computed with the usual formula:
wsize = lamp.clista * tan(lamp.spotsize/2)

# And the projection matrix:
mat4_lamp_to_perspective = glFrustum(-wsize, wsize, -wsize, wsize, lamp.clista, lamp.clipend)
```

2. Creation of the shadow map for a spot lamp.
The shadow map is the depth buffer of a render performed by placing the camera at the
spot light position. The size of the shadow map is given by the attribute lamp.bufsize

:
shadow map size in pixel, same size in both dimensions.

"""

import typing
import collections.abc
import typing_extensions
import bpy.types

from . import offscreen as offscreen

def export_shader(scene: bpy.types.Scene, material: bpy.types.Material):
    """Extracts the GLSL shader producing the visual effect of material in scene for the purpose of
    reusing the shader in an external engine.This function is meant to be used in material exporter
    so that the GLSL shader can be exported entirely.The return value is a dictionary containing the
    shader source code and all associated data.The dictionary contains the following elements:Example:

        :param scene: the scene in which the material in rendered.
        :type scene: bpy.types.Scene
        :param material: the material that you want to export the GLSL shader
        :type material: bpy.types.Material
        :return: the shader source code and all associated data in a dictionary
    """

CD_MCOL: typing.Any
""" Vertex attribute is color layer. Data type is vector 4 unsigned byte (RGBA).There can be more than one attribute of that type, they are differenciated by name.
In blender you can retrieve the attribute data with:
"""

CD_MTFACE: typing.Any
""" Vertex attribute is a UV Map. Data type is vector of 2 float.There can be more than one attribute of that type, they are differenciated by name.
In blender, you can retrieve the attribute data with:
"""

CD_ORCO: typing.Any
""" Vertex attribute is original coordinates. Data type is vector 3 float.There can be only 1 attribute of that type per shader.
In blender you can retrieve the attribute data with:
"""

CD_TANGENT: typing.Any
""" Vertex attribute is the tangent vector. Data type is vector 4 float.There can be only 1 attribute of that type per shader.
There is currently no way to retrieve this attribute data via the RNA API but a standalone
C function to compute the tangent layer from the other layers can be obtained from
blender.org.
"""

GPU_DATA_16F: typing.Any
""" matrix 4x4 in column-major order
"""

GPU_DATA_1F: typing.Any
""" one float
"""

GPU_DATA_1I: typing.Any
""" one integer
"""

GPU_DATA_2F: typing.Any
""" two floats
"""

GPU_DATA_3F: typing.Any
""" three floats
"""

GPU_DATA_4F: typing.Any
""" four floats
"""

GPU_DATA_4UB: typing.Any
""" four unsigned byte
"""

GPU_DATA_9F: typing.Any
""" matrix 3x3 in column-major order
"""

GPU_DYNAMIC_AMBIENT_COLOR: typing.Any
""" See `bpy.types.World.ambient_color`.
"""

GPU_DYNAMIC_HORIZON_COLOR: typing.Any
""" See `bpy.types.World.horizon_color`.
"""

GPU_DYNAMIC_LAMP_ATT1: float
""" See
`bpy.types.PointLamp.linear_attenuation`,
`bpy.types.SpotLamp.linear_attenuation`.
"""

GPU_DYNAMIC_LAMP_ATT2: float
""" See
`bpy.types.PointLamp.quadratic_attenuation`,
`bpy.types.SpotLamp.quadratic_attenuation`.
"""

GPU_DYNAMIC_LAMP_DISTANCE: float
""" See `bpy.types.Lamp.distance`.
"""

GPU_DYNAMIC_LAMP_DYNCO: typing.Any
""" Represents the position of the light in camera space.
"""

GPU_DYNAMIC_LAMP_DYNCOL: typing.Any
""" See `bpy.types.Lamp.color`.
"""

GPU_DYNAMIC_LAMP_DYNENERGY: float
""" See `bpy.types.Lamp.energy`.
"""

GPU_DYNAMIC_LAMP_DYNIMAT: typing.Any
""" Matrix that converts vector in camera space to lamp space.
"""

GPU_DYNAMIC_LAMP_DYNPERSMAT: typing.Any
""" Matrix that converts a vector in camera space to shadow buffer depth space.mat4_perspective_to_depth is a fixed matrix defined as follow:
"""

GPU_DYNAMIC_LAMP_DYNVEC: typing.Any
""" Represents the direction of light in camera space.
"""

GPU_DYNAMIC_LAMP_SPOTBLEND: float
""" See `bpy.types.SpotLamp.spot_blend`.
"""

GPU_DYNAMIC_LAMP_SPOTSCALE: typing.Any
""" Represents the SpotLamp local scale.
"""

GPU_DYNAMIC_LAMP_SPOTSIZE: float
""" See `bpy.types.SpotLamp.spot_size`.
"""

GPU_DYNAMIC_MAT_ALPHA: float
""" See `bpy.types.Material.alpha`.
"""

GPU_DYNAMIC_MAT_AMB: float
""" See `bpy.types.Material.ambient`.
"""

GPU_DYNAMIC_MAT_DIFFRGB: typing.Any
""" See `bpy.types.Material.diffuse_color`.
"""

GPU_DYNAMIC_MAT_EMIT: float
""" See `bpy.types.Material.emit`.
"""

GPU_DYNAMIC_MAT_HARD: float
""" See `bpy.types.Material.specular_hardness`.
"""

GPU_DYNAMIC_MAT_REF: float
""" See `bpy.types.Material.diffuse_intensity`.
"""

GPU_DYNAMIC_MAT_SPEC: float
""" See `bpy.types.Material.specular_intensity`.
"""

GPU_DYNAMIC_MAT_SPECRGB: typing.Any
""" See `bpy.types.Material.specular_color`.
"""

GPU_DYNAMIC_MIST_COLOR: typing.Any

GPU_DYNAMIC_MIST_DISTANCE: float
""" See `bpy.types.WorldMistSettings.intensity`.
"""

GPU_DYNAMIC_MIST_ENABLE: typing.Any
""" See `bpy.types.WorldMistSettings.use_mist`.
"""

GPU_DYNAMIC_MIST_INTENSITY: float

GPU_DYNAMIC_MIST_START: float
""" See `bpy.types.WorldMistSettings.start`.See `bpy.types.WorldMistSettings.depth`.
"""

GPU_DYNAMIC_MIST_TYPE: typing.Any
""" See `bpy.types.WorldMistSettings.falloff`.
"""

GPU_DYNAMIC_OBJECT_AUTOBUMPSCALE: float
""" Multiplier for bump-map scaling.
"""

GPU_DYNAMIC_OBJECT_COLOR: typing.Any
""" An RGB color + alpha defined at object level.
Each values between 0.0 and 1.0.See `bpy.types.Object.color`.
"""

GPU_DYNAMIC_OBJECT_IMAT: typing.Any
""" The uniform is a 4x4 GL matrix that converts world coodinates
to object coordinates (see mat4_world_to_object).
"""

GPU_DYNAMIC_OBJECT_MAT: typing.Any
""" A matrix that converts object coordinates to world coordinates (see mat4_object_to_world).
"""

GPU_DYNAMIC_OBJECT_VIEWIMAT: typing.Any
""" The uniform is a 4x4 GL matrix that converts coordinates
in camera space to world coordinates (see mat4_cam_to_world).
"""

GPU_DYNAMIC_OBJECT_VIEWMAT: typing.Any
""" A matrix that converts world coordinates to camera coordinates (see mat4_world_to_cam).
"""

GPU_DYNAMIC_SAMPLER_2DBUFFER: int
""" Represents an internal texture used for certain effect
(color band, etc).
"""

GPU_DYNAMIC_SAMPLER_2DIMAGE: int
""" Represents a texture loaded from an image file.
"""

GPU_DYNAMIC_SAMPLER_2DSHADOW: int
""" Represents a texture loaded from a shadow buffer file.
"""
