# Monkopoly Web

Web version of the Monkopoly board game — React frontend + Python (FastAPI) backend.

## Local Development

You need Python 3.10+ and Node.js 18+.

### Backend (Terminal 1)

```bash
cd web/backend
pip install -r requirements.txt
uvicorn main:app --reload
```

The API runs at `http://localhost:8000`.

### Frontend (Terminal 2)

```bash
cd web/frontend
npm install
npm run dev
```

Open `http://localhost:5173` in your browser. Vite proxies WebSocket and API
requests to the backend automatically.

## Docker

Build and run everything in a single container:

```bash
# From the repo root
docker build -t monkopoly -f web/Dockerfile .
docker run -p 8000:8000 monkopoly
```

Open `http://localhost:8000`.

## EC2 Deployment

1. Install Docker on your EC2 instance:
   ```bash
   sudo yum install -y docker
   sudo service docker start
   sudo usermod -aG docker ec2-user
   ```

2. Clone the repo and build:
   ```bash
   git clone <your-repo-url>
   cd Monkopoly-Single-Player
   docker build -t monkopoly -f web/Dockerfile .
   docker run -d -p 80:8000 monkopoly
   ```

3. Access the game at `http://<your-ec2-public-ip>`.

## Architecture

- **Backend** (`web/backend/`): FastAPI app with WebSocket endpoint. All game
  logic runs server-side — board state, dice, rent, AI turns.
- **Frontend** (`web/frontend/`): React + TypeScript + Vite. Renders the board,
  handles player interactions, communicates via WebSocket.
- **Images** (`Images/`): Shared game assets (board, dice, player tokens,
  property cards).

## How It Works

1. Browser connects via WebSocket to `/ws/game`
2. Server creates a new game (1 human + 3 AI players)
3. Human sends actions: roll, buy, pass, manage, trade, end_turn
4. Server processes actions, runs AI turns automatically, sends state updates
5. Frontend renders the updated board state
