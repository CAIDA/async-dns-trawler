from enum import Enum
from typing import List, Union

from dt.typing.custom_types.primitive import Primitive

ValueLiteral = Union[Primitive, List[Primitive], Enum]
