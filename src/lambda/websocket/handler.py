from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

# HTML for the WebSocket client
html = """
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <textarea id="chat" cols="30" rows="10" readonly></textarea><br>
        <input id="message" type="text" placeholder="Type a message...">
        <button onclick="sendMessage()">Send</button>

        <script>
            const ws = new WebSocket("ws://localhost:8000/ws");
            const chat = document.getElementById("chat");

            ws.onmessage = function(event) {
                const message = JSON.parse(event.data);
                chat.value += message.user + ": " + message.content + "\\n";
            };

            function sendMessage() {
                const input = document.getElementById("message");
                const message = { user: "User", content: input.value };
                ws.send(JSON.stringify(message));
                input.value = "";
            }
        </script>
    </body>
</html>
"""

@app.get("/")
async def get():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(data)