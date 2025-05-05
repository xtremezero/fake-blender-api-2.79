import typing
import collections.abc
import typing_extensions
import bge.types.EXP_PyObjectPlus
import bge.types.KX_2DFilter

class KX_2DFilterManager(bge.types.EXP_PyObjectPlus.EXP_PyObjectPlus):
    """2D filter manager used to add, remove and find filters in a scene."""

    def addFilter(
        self, index: int, type: int, fragmentProgram: str | None = ""
    ) -> bge.types.KX_2DFilter.KX_2DFilter:
        """Add a filter to the pass index `index`, type `type` and fragment program if custom filter.

                :param index: The filter pass index.
                :type index: int
                :param type: The filter type, one of:

        `bge.logic.RAS_2DFILTER_BLUR`

        `bge.logic.RAS_2DFILTER_DILATION`

        `bge.logic.RAS_2DFILTER_EROSION`

        `bge.logic.RAS_2DFILTER_SHARPEN`

        `bge.logic.RAS_2DFILTER_LAPLACIAN`

        `bge.logic.RAS_2DFILTER_PREWITT`

        `bge.logic.RAS_2DFILTER_SOBEL`

        `bge.logic.RAS_2DFILTER_GRAYSCALE`

        `bge.logic.RAS_2DFILTER_SEPIA`

        `bge.logic.RAS_2DFILTER_CUSTOMFILTER`
                :type type: int
                :param fragmentProgram: The filter shader fragment program.
        Used only if `type` is `bge.logic.RAS_2DFILTER_CUSTOMFILTER`, if empty or not specified the filter is created without shader, waiting call to `BL_Shader.setSourceList`. (optional)
                :type fragmentProgram: str | None
                :return: The 2D Filter.
                :rtype: bge.types.KX_2DFilter.KX_2DFilter
        """

    def removeFilter(self, index: int):
        """Remove filter to the pass index `index`.

        :param index: The filter pass index.
        :type index: int
        """

    def getFilter(self, index: int) -> bge.types.KX_2DFilter.KX_2DFilter:
        """Return filter to the pass index `index`.

        :param index: The filter pass index.
        :type index: int
        :return: The filter in the specified pass index or None.
        :rtype: bge.types.KX_2DFilter.KX_2DFilter
        """
