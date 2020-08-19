from fastapi import FastAPI, APIRouter, Request
from starlette.responses import RedirectResponse, JSONResponse
from app.db import db
# controller
from app.controllers import (
    admin_controller,
    sample_controller
)

API_VERSION = 'v1'

app = FastAPI()

@app.middleware('http')
async def check_login(request: Request, call_next):
    """Cookieからsessionidを取得し、django_sessionテーブルに存在すればログイン済み→素通り
        そうでなければ/admin/loginにリダイレクト
    """
    # ブラウザからアクセスされた時
    if 'Mozilla' in request.headers['user-agent']:
        if 'sessionid' not in request.cookies:
            return RedirectResponse('/admin/login/')

        session_id = request.cookies['sessionid']
        if db.table('django_session').where('session_key', session_id).count() == 0:
            return RedirectResponse('/admin/login/')
    # APIからアクセスされた時
    else:
        if 'sessionid' not in request.cookies:
            response = JSONResponse({})
            response.status_code = 403
            return response

        session_id = request.cookies['sessionid']
        if db.table('django_session').where('session_key', session_id).count() == 0:
            response = JSONResponse({})
            response.status_code = 403
            return response

    response = await call_next(request)
    return response


api_router = APIRouter()
# ここにコントローラーとURLのプレフィックスの組み合わせを追加する
# API
api_router.include_router(sample_controller.router)

api_prefix_router = APIRouter()
api_prefix_router.include_router(api_router, prefix=f'/api/{API_VERSION}')

# MPA
router = APIRouter()
router.include_router(admin_controller.router)

app.include_router(api_prefix_router)
app.include_router(router)
