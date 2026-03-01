# Build from the repo root: docker build -t monkopoly -f web/Dockerfile .

# Stage 1: Build the React frontend
FROM node:20-alpine AS frontend-build
WORKDIR /app/frontend
COPY web/frontend/package.json web/frontend/package-lock.json* ./
RUN npm install
COPY web/frontend/ ./
RUN npm run build

# Stage 2: Python runtime with backend + built frontend
FROM python:3.12-slim
WORKDIR /app

COPY web/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY web/backend/ ./
COPY --from=frontend-build /app/frontend/dist ./frontend/dist/
COPY Images/ ./Images/

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
