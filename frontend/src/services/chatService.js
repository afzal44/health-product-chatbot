import axios from 'axios';

const API_URL = process.env.API_URL || 'http://localhost:3000/api/chat';

export const sendMessage = async (message) => {
    try {
        const response = await axios.post(`${API_URL}/send`, { message });
        return response.data;
    } catch (error) {
        console.error('Error sending message:', error);
        throw error;
    }
};

export const receiveMessages = async () => {
    try {
        const response = await axios.get(`${API_URL}/receive`);
        return response.data;
    } catch (error) {
        console.error('Error receiving messages:', error);
        throw error;
    }
};