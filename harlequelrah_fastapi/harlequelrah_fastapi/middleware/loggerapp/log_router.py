from typing import List
from fastapi import APIRouter, Depends

from harlequelrah_fastapi.router.route_config import RouteConfig
from harlequelrah_fastapi.router.router_namespace import DefaultRoutesName
from harlequelrah_fastapi.router.router_provider import CustomRouterProvider
from .log_crud import logCrud
from my_project.settings.database import authentication
from .log_schema import LoggerMiddlewarePydanticModel as LMPD

router_provider = CustomRouterProvider(
    prefix="/logs",
    tags=["logs"],
    PydanticModel=LMPD,
    crud=logCrud,
)
app_logger = router_provider.get_protected_router(
    [DefaultRoutesName.UPDATE, DefaultRoutesName.DELETE, DefaultRoutesName.CREATE]
)
