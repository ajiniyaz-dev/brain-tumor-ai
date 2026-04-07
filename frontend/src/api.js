import axios from "axios";

const API = axios.create({
  baseURL: "https://brain-tumor-ai-1-hm7r.onrender.com",
  timeout: 120000, // ✅ prevent timeout
});

export const predictTumor = (file) => {
  const formData = new FormData();
  formData.append("file", file);

  return API.post("/predict", formData);
};

export const sendFeedback = (file, predicted, actual) => {
  const formData = new FormData();
  formData.append("file", file);
  formData.append("predicted", predicted);
  formData.append("actual", actual);

  return API.post("/feedback", formData);
};