from typing import List, Optional, Sequence, Tuple

# our default integer and floating point types
from numpy import float64, int64

try:
    from numpy.typing import ArrayLike, NDArray
except BaseException:
    NDArray = Sequence
    ArrayLike = Sequence


__all__ = ["NDArray", "ArrayLike", "Optional", "List", "Tuple", "float64", "int64"]
