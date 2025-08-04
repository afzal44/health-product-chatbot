import React, { useState } from 'react';
import ChatBubble from './MessageBubble';
import TypingIndicator from './TypingIndicator';
import chatService from '../services/chatService';
import websocketService from '../services/websocketService';
import './ChatWidget.css';

const ChatWidget = () => {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState('');
    const [isTyping, setIsTyping] = useState(false);

    const handleInputChange = (event) => {
        setInput(event.target.value);
    };

    const handleSendMessage = async () => {
        if (input.trim()) {
            const newMessage = { text: input, sender: 'user' };
            setMessages([...messages, newMessage]);
            setInput('');
            setIsTyping(true);

            const response = await chatService.sendMessage(input);
            setMessages((prevMessages) => [...prevMessages, response]);
            setIsTyping(false);
        }
    };

    return (
        <div className="chat-widget">
            <div className="chat-messages">
                {messages.map((msg, index) => (
                    <ChatBubble key={index} message={msg} />
                ))}
                {isTyping && <TypingIndicator />}
            </div>
            <input
                type="text"
                value={input}
                onChange={handleInputChange}
                onKeyPress={(event) => {
                    if (event.key === 'Enter') {
                        handleSendMessage();
                    }
                }}
                placeholder="Type a message..."
            />
            <button onClick={handleSendMessage}>Send</button>
        </div>
    );
};

export default ChatWidget;