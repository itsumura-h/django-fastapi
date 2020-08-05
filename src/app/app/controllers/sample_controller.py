from fastapi import APIRouter
from pydantic import BaseModel
from typing import (
  Dict
)

router = APIRouter()

@router.get("/index")
def index()->Dict[str, str]:
  return {"Hello": "World"}
