from fastapi import (
    FastAPI,
    WebSocket,
    WebSocketDisconnect
)
from fastapi.responses import HTMLResponse

app = FastAPI()


class ConnectionManager:

    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()

        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, message: str):

        for connection in self.active_connections.copy():

            try:
                await connection.send_text(message)

            except Exception:
                self.disconnect(connection)


manager = ConnectionManager()


@app.websocket("/ws/{username}")
async def websocket_endpoint(
    websocket: WebSocket,
    username: str
):

    await manager.connect(websocket)

    await manager.broadcast(
        f"{username} joined the chat!"
    )

    try:

        while True:

            message = await websocket.receive_text()

            await manager.broadcast(
                f"{username}: {message}"
            )

    except WebSocketDisconnect:

        manager.disconnect(websocket)

        await manager.broadcast(
            f"{username} left the chat!"
        )


html = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>FastAPI Multi-user WebSocket Demo</title>
    <style>
        body {
            max-width: 720px;
            margin: 40px auto;
            padding: 0 16px;
            font-family: system-ui, sans-serif;
        }
        #messages {
            height: 320px;
            overflow-y: auto;
            padding: 12px 32px;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        form, .connection-controls {
            display: flex;
            gap: 8px;
            margin: 12px 0;
        }
        input {
            flex: 1;
            min-width: 0;
            padding: 8px;
        }
        button {
            padding: 8px 12px;
        }
        #status {
            color: #555;
        }
    </style>
</head>
<body>

    <h1>Multi-user WebSocket Chat</h1>
    <p>Open this page in multiple tabs or browsers and connect with a different name in each.</p>

    <div class="connection-controls">
        <input
            type="text"
            id="usernameInput"
            placeholder="Choose a username"
            maxlength="50"
            autocomplete="nickname"
        />
        <button id="connectButton" type="button">Connect</button>
        <button id="disconnectButton" type="button" disabled>Disconnect</button>
    </div>
    <p id="status" role="status">Not connected</p>

    <ul id="messages" aria-live="polite"></ul>
    <form id="messageForm">
        <input
            type="text"
            id="messageInput"
            placeholder="Enter your message"
            autocomplete="off"
            disabled
        />
        <button id="sendButton" type="submit" disabled>Send</button>
    </form>

    <script>
        const usernameInput = document.getElementById("usernameInput");
        const connectButton = document.getElementById("connectButton");
        const disconnectButton = document.getElementById("disconnectButton");
        const messageInput = document.getElementById("messageInput");
        const sendButton = document.getElementById("sendButton");
        const messageForm = document.getElementById("messageForm");
        const messages = document.getElementById("messages");
        const status = document.getElementById("status");
        let socket = null;

        function setConnected(connected) {
            usernameInput.disabled = connected;
            connectButton.disabled = connected;
            disconnectButton.disabled = !connected;
            messageInput.disabled = !connected;
            sendButton.disabled = !connected;
            status.textContent = connected ? "Connected" : "Not connected";
        }

        connectButton.addEventListener("click", () => {
            const username = usernameInput.value.trim();
            if (!username) {
                status.textContent = "Enter a username to connect.";
                usernameInput.focus();
                return;
            }

            const protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
            socket = new WebSocket(
                `${protocol}//${window.location.host}/ws/${encodeURIComponent(username)}`
            );
            status.textContent = "Connecting...";
            connectButton.disabled = true;

            socket.addEventListener("open", () => {
                setConnected(true);
                messageInput.focus();
            });

            socket.addEventListener("message", (event) => {
                const item = document.createElement("li");
                item.textContent = event.data;
                messages.appendChild(item);
                messages.scrollTop = messages.scrollHeight;
            });

            socket.addEventListener("close", () => {
                setConnected(false);
                socket = null;
            });

            socket.addEventListener("error", () => {
                status.textContent = "Connection error. Check that the server is running.";
            });
        });

        disconnectButton.addEventListener("click", () => {
            if (socket) {
                socket.close();
            }
        });

        messageForm.addEventListener("submit", (event) => {
            event.preventDefault();
            const message = messageInput.value.trim();
            if (socket && socket.readyState === WebSocket.OPEN && message) {
                socket.send(message);
                messageInput.value = "";
                messageInput.focus();
            }
        });
    </script>

</body>
</html>
"""

@app.get("/")
def root():
    return HTMLResponse(html)

