"""
This module contains callback lists


--------------------

This script shows the most simple example of adding a handler.

```../examples/bpy.app.handlers.py```


--------------------

By default handlers are freed when loading new files, in some cases you may
want the handler stay running across multiple files (when the handler is
part of an add-on for example).

For this the bpy.app.handlers.persistent decorator needs to be used.

```../examples/bpy.app.handlers.1.py```

"""

import typing
import collections.abc
import typing_extensions
import bpy.types

frame_change_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on frame change for playback and rendering (after)
"""

frame_change_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on frame change for playback and rendering (before)
"""

game_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on ending the game engine
"""

game_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on starting the game engine
"""

load_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading a new blend file (after)
"""

load_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading a new blend file (before)
"""

persistent: typing.Any
""" Function decorator for callback functions not to be removed when loading new files
"""

redo_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading a redo step (after)
"""

redo_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading a redo step (before)
"""

render_cancel: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on canceling a render job
"""

render_complete: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on completion of render job
"""

render_init: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on initialization of a render job
"""

render_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on render (after)
"""

render_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on render (before)
"""

render_stats: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on printing render statistics
"""

render_write: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on writing a render frame (directly after the frame is written)
"""

save_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on saving a blend file (after)
"""

save_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on saving a blend file (before)
"""

scene_update_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on every scene data update. Does not imply that anything changed in the scene, just that the dependency graph was reevaluated, and the scene was possibly updated by Blender's animation system.
"""

scene_update_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on every scene data update. Does not imply that anything changed in the scene, just that the dependency graph is about to be reevaluated, and the scene is about to be updated by Blender's animation system.
"""

undo_post: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading an undo step (after)
"""

undo_pre: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on loading an undo step (before)
"""

version_update: list[collections.abc.Callable[[bpy.types.Scene], None]]
""" on ending the versioning code
"""
