from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import app.settings as conf
from app.api.views import bp

app = FastAPI()
app.mount(
    conf.STATIC_URL, StaticFiles(directory=conf.STATIC_DIR), name="static"
)
templates = Jinja2Templates(directory=conf.TEMPLATE_DIR)

app.include_router(bp)

@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    ''' returns home page '''
    return templates.TemplateResponse("index.html", {"request": request})
