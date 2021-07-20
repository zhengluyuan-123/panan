
from fastapi import APIRouter


class FastAPIRouter(APIRouter):
    def route(self, rule, **options):
        self.redirect_slashes = options.get("strict_slashes", True)
        return self.api_route(path=rule, methods=options.get('methods'))