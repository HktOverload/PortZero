# PortZero by HktOverload

import typing
from utils import *

Export(...) @ globals()

class ExtEvent(typing.NamedTuple):
    name: str
    data: dict[str, typing.Any]
