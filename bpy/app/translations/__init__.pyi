"""
This object contains some data/methods regarding internationalization in Blender, and allows every py script
to feature translations for its own UI messages.


--------------------

[WARNING]
Most of this object should only be useful if you actually manipulate i18n stuff from Python.
If you are a regular add-on, you should only bother about contexts member,
and the register/unregister functions! The pgettext family of functions
should only be used in rare, specific cases (like e.g. complex "composited" UI strings...).

To add translations to your python script, you must define a dictionary formatted like that:
{locale: {msg_key: msg_translation, ...}, ...}



where:

* locale is either a lang iso code (e.g. fr

), a lang+country code (e.g. pt_BR

),
a lang+variant code (e.g. sr@latin

), or a full code (e.g. uz_UZ@cyrilic

).
* msg_key is a tuple (context, org message) - use, as much as possible, the predefined contexts.
* msg_translation is the translated message in given language!

Then, call bpy.app.translations.register(__name__, your_dict)

 in your register()

 function, and
bpy.app.translations.unregister(__name__)

 in your unregister()

 one.

The Manage UI translations

 add-on has several functions to help you collect strings to translate, and
generate the needed python code (the translation dictionary), as well as optional intermediary po files
if you want some... See
How to Translate Blender and
Using i18n in Blender Code
for more info.


--------------------

```../examples/bpy.app.translations.py```

"""

import typing
import collections.abc
import typing_extensions

def locale_explode(locale):
    """Return all components and their combinations  of the given ISO locale string.For non-complete locales, missing elements will be None.

    :param locale: The ISO locale string to explode.
    :return: A tuple (language, country, variant, language_country, language@variant).
    """

def pgettext(msgid: str | None, msgctxt: None | str | None):
    """Try to translate the given msgid (with optional msgctxt).

    :param msgid: The string to translate.
    :type msgid: str | None
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: None | str | None
    :return: The translated string (or msgid if no translation was found).
    """

def pgettext_data(msgid: str | None, msgctxt: None | str | None):
    """Try to translate the given msgid (with optional msgctxt), if new data name's translation is enabled.

    :param msgid: The string to translate.
    :type msgid: str | None
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: None | str | None
    :return: The translated string (or msgid if no translation was found).
    """

def pgettext_iface(msgid: str | None, msgctxt: None | str | None):
    """Try to translate the given msgid (with optional msgctxt), if labels' translation is enabled.

    :param msgid: The string to translate.
    :type msgid: str | None
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: None | str | None
    :return: The translated string (or msgid if no translation was found).
    """

def pgettext_tip(msgid: str | None, msgctxt: None | str | None):
    """Try to translate the given msgid (with optional msgctxt), if tooltips' translation is enabled.

    :param msgid: The string to translate.
    :type msgid: str | None
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: None | str | None
    :return: The translated string (or msgid if no translation was found).
    """

def register(module_name: str | None, translations_dict: dict | None):
    """Registers an addon's UI translations.

        :param module_name: The name identifying the addon.
        :type module_name: str | None
        :param translations_dict: A dictionary built like that:
    {locale: {msg_key: msg_translation, ...}, ...}
        :type translations_dict: dict | None
    """

def unregister(module_name: str | None):
    """Unregisters an addon's UI translations.

    :param module_name: The name identifying the addon.
    :type module_name: str | None
    """

contexts: typing.Any
""" constant value bpy.app.translations.contexts(default_real=None, default='*', operator_default='Operator', ui_events_keymaps='UI_Events_KeyMaps', plural='Plural', id_action='Action', id_armature='Armature', id_brush='Brush', id_camera='Camera', id_cachefile='CacheFile', id_curve='Curve', id_fs_linestyle='FreestyleLineStyle', id_gpencil='GPencil', id_group='Group', id_id='ID', id_image='Image', id_shapekey='Key', id_lamp='Lamp', id_library='Library', id_lattice='Lattice', id_mask='Mask', id_material='Material', ...)
"""

contexts_C_to_py: typing.Any
""" A readonly dict mapping contexts' C-identifiers to their py-identifiers.
"""

locale: typing.Any
""" The actual locale currently in use (will always return a void string when Blender is built without internationalization support).
"""

locales: typing.Any
""" All locales currently known by Blender (i.e. available as translations).
"""
