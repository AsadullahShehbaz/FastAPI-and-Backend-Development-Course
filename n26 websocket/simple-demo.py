from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
<head>
    <title>FastAPI WebSocket Demo</title>
</head>
<body>

    <h1>FastAPI WebSocket Demo</h1>

    <input
        type="text"
        id="messageInput"
        placeholder="Enter your message"
    />

    <button onclick="sendMessage()">
        Send
    </button>

    <ul id="messages"></ul>

    <script>
        const socket = new WebSocket(
            "ws://127.0.0.1:8000/ws"
        );

        socket.onopen = () => {
            console.log("Connected to server");
        };

        socket.onmessage = (event) => {
            const messages = document.getElementById(
                "messages"
            );

            const item = document.createElement("li");

            item.textContent = event.data;

            messages.appendChild(item);
        };

        socket.onclose = () => {
            console.log("Connection closed");
        };

        socket.onerror = (error) => {
            console.error("WebSocket error:", error);
        };

        function sendMessage() {
            const input = document.getElementById(
                "messageInput"
            );

            socket.send(input.value);

            input.value = "";
        }
    </script>

</body>
</html>
"""

@app.get("/")
def root():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    while True:
        data = await websocket.receive_text()

        await websocket.send_text(
            f"Message received: {data}"
        )
