from fastapi import Request, APIRouter, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse

from not_db.player_info import PlayerData

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, 'PlayerData': PlayerData})


@router.get("/what_you_need")
async def what_you_need(request: Request):
    return templates.TemplateResponse()


@router.get("/bips")
async def home(index: str = Header(default="1")):
    dex = int(index) % 12
    return FileResponse(f'./static/bips/{dex}.mp3', media_type='Audio')
