from datetime import datetime
from typing import (
    Any,
    Dict,
)


def object_deserializer(obj: Dict[str, Any]) -> Dict[str, Any]: ...


def object_serializer(obj: datetime) -> str: ...
