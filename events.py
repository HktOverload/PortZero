# PortZero by HktOverload

import typing as t
from utils import *

Export(...) @ globals()

class Event(t.NamedTuple):
    name: str
    eventCls: t.Literal['wld', 'ext', 'scn']
    data: dict[str, t.Any]
