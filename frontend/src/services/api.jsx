import axios from "axios";

// We use the root URL as the base for maximum flexibility
const API_BASE_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

const api = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
});

// Interceptor to add Token to headers
api.interceptors.request.use((config) => {
  const user = JSON.parse(localStorage.getItem("user"));
  if (user && user.token) {
    config.headers.Authorization = `Token ${user.token}`;
  }
  return config;
}, (error) => {
  return Promise.reject(error);
});

export default api;
