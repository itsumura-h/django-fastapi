from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Dict

templates = Jinja2Templates(directory="resources")

router = APIRouter()

@router.get('/')
async def index(request:Request):
    return templates.TemplateResponse("admin/index.html", {"request": request})
