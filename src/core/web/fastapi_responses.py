import orjson
from typing import Any
from starlette.responses import JSONResponse


class KYZDefaultResponseJson(JSONResponse):

    media_type = "application/json"

    def __init__(self,
                 content: Any = None,
                 status_code: int = 200,
                 headers: dict = None,
                 media_type: str = None,
                 background=None)-> None:
        super().__init__(
            content=content,
            status_code=status_code,
            headers=headers,
            media_type=media_type,
            background=background,
        )

    def render(self, content: Any) -> bytes:
        return orjson.dumps(content)