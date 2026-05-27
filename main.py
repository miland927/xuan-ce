from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from algorithms import calc_bazi, cast_gua, get_daily_gua


app = FastAPI(title="玄策")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return FileResponse("yijing-merged.html")


@app.get("/health")
def health():
    return {"status": "ok", "app": "玄策"}


@app.post("/bazi")
def bazi(data: dict):
    return calc_bazi(data["year"], data["month"], data["day"], data["hour"])


@app.post("/gua")
def gua(data: dict | None = None):
    data = data or {}
    return cast_gua(data.get("method", "random"))


@app.get("/daily")
def daily():
    return get_daily_gua()


# Start with:
# uvicorn main:app --reload --port 8000
