import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';  // FastAPI server URL

export const testCode = async (code: string) => {
  const response = await axios.post(`${API_BASE_URL}/api/execute`, { code });
  return response.data.result;
};

export const submitCode = async (code: string) => {
  const response = await axios.post(`${API_BASE_URL}/api/submit`, { code });
  return response.data.result;
};
