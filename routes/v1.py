from fastapi import APIRouter
from ._v1 import post_router

router = APIRouter()

router.include_router(post_router, prefix="/post", tags=["post"])
