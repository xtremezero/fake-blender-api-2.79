"""

--------------------

This module contains the classes that appear as instances in the Game Engine. A
script must interact with these classes if it is to affect the behaviour of
objects in a game.

The following example would move an object (i.e. an instance of
KX_GameObject) one unit up.

```
# bge.types.SCA_PythonController
cont = bge.logic.getCurrentController()

# bge.types.KX_GameObject
obj = cont.owner
obj.worldPosition.z += 1
```

To run the code, it could be placed in a Blender text block and executed with
a SCA_PythonController logic brick.


--------------------

bge.types.*

:glob:

"""

import typing
import collections.abc
import typing_extensions
from . import BL_ActionActuator as BL_ActionActuator
from . import BL_ArmatureActuator as BL_ArmatureActuator
from . import BL_ArmatureBone as BL_ArmatureBone
from . import BL_ArmatureChannel as BL_ArmatureChannel
from . import BL_ArmatureConstraint as BL_ArmatureConstraint
from . import BL_ArmatureObject as BL_ArmatureObject
from . import BL_Shader as BL_Shader
from . import BL_Texture as BL_Texture
from . import EXP_ListValue as EXP_ListValue
from . import EXP_PropValue as EXP_PropValue
from . import EXP_PyObjectPlus as EXP_PyObjectPlus
from . import EXP_Value as EXP_Value
from . import KX_2DFilter as KX_2DFilter
from . import KX_2DFilterManager as KX_2DFilterManager
from . import KX_2DFilterOffScreen as KX_2DFilterOffScreen
from . import KX_ArmatureSensor as KX_ArmatureSensor
from . import KX_BatchGroup as KX_BatchGroup
from . import KX_BlenderMaterial as KX_BlenderMaterial
from . import KX_BoundingBox as KX_BoundingBox
from . import KX_Camera as KX_Camera
from . import KX_CameraActuator as KX_CameraActuator
from . import KX_CharacterWrapper as KX_CharacterWrapper
from . import KX_CollisionContactPoint as KX_CollisionContactPoint
from . import KX_CollisionSensor as KX_CollisionSensor
from . import KX_ConstraintActuator as KX_ConstraintActuator
from . import KX_ConstraintWrapper as KX_ConstraintWrapper
from . import KX_CubeMap as KX_CubeMap
from . import KX_FontObject as KX_FontObject
from . import KX_GameActuator as KX_GameActuator
from . import KX_GameObject as KX_GameObject
from . import KX_LibLoadStatus as KX_LibLoadStatus
from . import KX_LightObject as KX_LightObject
from . import KX_LodLevel as KX_LodLevel
from . import KX_LodManager as KX_LodManager
from . import KX_Mesh as KX_Mesh
from . import KX_MouseActuator as KX_MouseActuator
from . import KX_MouseFocusSensor as KX_MouseFocusSensor
from . import KX_NavMeshObject as KX_NavMeshObject
from . import KX_NearSensor as KX_NearSensor
from . import KX_NetworkMessageActuator as KX_NetworkMessageActuator
from . import KX_NetworkMessageSensor as KX_NetworkMessageSensor
from . import KX_ObjectActuator as KX_ObjectActuator
from . import KX_ParentActuator as KX_ParentActuator
from . import KX_PlanarMap as KX_PlanarMap
from . import KX_PolyProxy as KX_PolyProxy
from . import KX_PythonComponent as KX_PythonComponent
from . import KX_RadarSensor as KX_RadarSensor
from . import KX_RaySensor as KX_RaySensor
from . import KX_SCA_AddObjectActuator as KX_SCA_AddObjectActuator
from . import KX_SCA_DynamicActuator as KX_SCA_DynamicActuator
from . import KX_SCA_EndObjectActuator as KX_SCA_EndObjectActuator
from . import KX_SCA_ReplaceMeshActuator as KX_SCA_ReplaceMeshActuator
from . import KX_Scene as KX_Scene
from . import KX_SceneActuator as KX_SceneActuator
from . import KX_SoundActuator as KX_SoundActuator
from . import KX_StateActuator as KX_StateActuator
from . import KX_SteeringActuator as KX_SteeringActuator
from . import KX_TextureRenderer as KX_TextureRenderer
from . import KX_TrackToActuator as KX_TrackToActuator
from . import KX_VehicleWrapper as KX_VehicleWrapper
from . import KX_VertexProxy as KX_VertexProxy
from . import KX_VisibilityActuator as KX_VisibilityActuator
from . import KX_WorldInfo as KX_WorldInfo
from . import SCA_2DFilterActuator as SCA_2DFilterActuator
from . import SCA_ANDController as SCA_ANDController
from . import SCA_ActuatorSensor as SCA_ActuatorSensor
from . import SCA_AlwaysSensor as SCA_AlwaysSensor
from . import SCA_DelaySensor as SCA_DelaySensor
from . import SCA_IActuator as SCA_IActuator
from . import SCA_IController as SCA_IController
from . import SCA_ILogicBrick as SCA_ILogicBrick
from . import SCA_IObject as SCA_IObject
from . import SCA_ISensor as SCA_ISensor
from . import SCA_InputEvent as SCA_InputEvent
from . import SCA_JoystickSensor as SCA_JoystickSensor
from . import SCA_KeyboardSensor as SCA_KeyboardSensor
from . import SCA_MouseSensor as SCA_MouseSensor
from . import SCA_NANDController as SCA_NANDController
from . import SCA_NORController as SCA_NORController
from . import SCA_ORController as SCA_ORController
from . import SCA_PropertyActuator as SCA_PropertyActuator
from . import SCA_PropertySensor as SCA_PropertySensor
from . import SCA_PythonController as SCA_PythonController
from . import SCA_PythonJoystick as SCA_PythonJoystick
from . import SCA_PythonKeyboard as SCA_PythonKeyboard
from . import SCA_PythonMouse as SCA_PythonMouse
from . import SCA_RandomActuator as SCA_RandomActuator
from . import SCA_RandomSensor as SCA_RandomSensor
from . import SCA_VibrationActuator as SCA_VibrationActuator
from . import SCA_XNORController as SCA_XNORController
from . import SCA_XORController as SCA_XORController
