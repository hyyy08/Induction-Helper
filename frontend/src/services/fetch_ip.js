// services/api.js
import axios from 'axios';

let serverIp = '';

export const getServerIp = async () => {
  try {
    const response = await axios.get('http://localhost:8000/get_serverIP/');
    serverIp = response.data.ip;
    return serverIp;
  } catch (error) {
    console.error('Error fetching server IP:', error);
    throw error;
  }
};

export const getApiUrl = () => {
  if (!serverIp) {
    throw new Error('Server IP not initialized');
  }
  return `http://${serverIp}:8000`;
};