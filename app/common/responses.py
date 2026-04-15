"""Common response helpers."""

def success_response[T](data: T) -> dict[str, bool | T]:
    return {"success": True, "data": data}
