import WebSocket from 'ws';

class WebSocketService {
    constructor(url) {
        this.url = url;
        this.socket = null;
    }

    connect() {
        this.socket = new WebSocket(this.url);

        this.socket.onopen = () => {
            console.log('WebSocket connection established');
        };

        this.socket.onmessage = (event) => {
            this.handleMessage(event.data);
        };

        this.socket.onclose = () => {
            console.log('WebSocket connection closed');
        };

        this.socket.onerror = (error) => {
            console.error('WebSocket error:', error);
        };
    }

    handleMessage(data) {
        // Handle incoming messages
        console.log('Received message:', data);
    }

    sendMessage(message) {
        if (this.socket && this.socket.readyState === WebSocket.OPEN) {
            this.socket.send(message);
            console.log('Sent message:', message);
        } else {
            console.error('WebSocket is not open. Cannot send message.');
        }
    }

    disconnect() {
        if (this.socket) {
            this.socket.close();
        }
    }
}

export default WebSocketService;