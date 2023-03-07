from fastapi import Request, APIRouter, WebSocket, Header
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.responses import FileResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "sound": ["", 'https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3']})

@router.get("/bips")
async def home(request: Request, index: str = Header(default="8")):
    dex = int(index) % 12
    return FileResponse(f'./static/bips/{dex}.mp3', media_type='Audio')
