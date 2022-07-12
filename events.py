# PortZero by HktOverload

import typing as t
from utils import *

Export(...) @ globals()

class Event(t.NamedTuple):
    name: str
    eventType: t.Literal
    data: dict[str, typing.Any]
