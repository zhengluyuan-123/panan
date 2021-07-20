
from typing import Any, Dict, List, Sequence, Type, Union
from flask import Blueprint

class FlaskAPIRouter(Blueprint):
    """
    summary:摘要
    """

    def get(self,
            path: str,
            *,
            response_model: Type[Any] = None,
            status_code: int = 200,
            tags: List[str] = None,
            dependencies: Sequence = None,
            summary:str = None,
            description: str = None,
            response_description: str = 'Successful Response',
            responses: Dict[Union[int,str], Dict[str, Any]] = None,
            deprecated: bool = None,
            operation_id: str = None,
            response_model_include = None,
            response_model_exclude= set(),
            response_model_by_alias: bool = True,
            response_model_skip_defaults: bool = None,
            response_model_exclude_unset: bool = False,
            response_model_exclude_defaults: bool = False,
            response_model_exclude_none: bool = True,
            response_class = None,
            name: str =None,
            callbacks: List[object] = None
            ):
        return self.route(path,methods=['GET'])

    def post(self,
            path: str,
            *,
            response_model: Type[Any] = None,
            status_code: int = 200,
            tags: List[str] = None,
            dependencies: Sequence = None,
            summary: str = None,
            description: str = None,
            response_description: str = 'Successful Response',
            responses: Dict[Union[int, str], Dict[str, Any]] = None,
            deprecated: bool = None,
            operation_id: str = None,
            response_model_include=None,
            response_model_exclude=set(),
            response_model_by_alias: bool = True,
            response_model_skip_defaults: bool = None,
            response_model_exclude_unset: bool = False,
            response_model_exclude_defaults: bool = False,
            response_model_exclude_none: bool = True,
            response_class=None,
            name: str = None,
            callbacks: List[object] = None
            ):
        return self.route(path, methods=['POST'])