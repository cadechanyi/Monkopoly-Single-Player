"""
FastAPI application — serves WebSocket game endpoint and static files.
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api.websocket import game_websocket  # noqa: E402

app = FastAPI(title="Monkopoly")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.websocket("/ws/game")(game_websocket)

# Serve game images
images_dir = Path(__file__).resolve().parent.parent.parent / "Images"
if images_dir.exists():
    app.mount("/images", StaticFiles(directory=str(images_dir)), name="images")

# In production, serve the frontend build.
# Support both the monorepo layout (web/frontend/dist) and the Docker image layout (/app/frontend/dist).
backend_root = Path(__file__).resolve().parent
frontend_candidates = [
    backend_root.parent / "frontend" / "dist",  # repo layout: web/frontend/dist
    backend_root / "frontend" / "dist",        # Docker layout: /app/frontend/dist
]
for frontend_dist in frontend_candidates:
    if frontend_dist.exists():
        app.mount("/", StaticFiles(directory=str(frontend_dist), html=True), name="frontend")
        break


@app.get("/api/health")
async def health():
    return {"status": "ok"}
