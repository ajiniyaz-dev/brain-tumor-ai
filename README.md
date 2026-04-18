#  Brain Tumor Detection AI

A full-stack AI-powered web application for automated **brain MRI validation** and **brain tumor classification** using deep learning.

The system combines:

- **FastAPI backend** for model inference and REST API
- **React frontend** for user interaction
- **TensorFlow / Keras models** for medical image analysis

Two separate deep learning models are used:

1. **MRI Detector Model** – Checks whether the uploaded image is a valid brain MRI scan  
2. **Tumor Classification Model** – Predicts tumor type from valid MRI images

---

# Features

## Frontend
- Modern React web interface
- Upload MRI images easily
- Display predictions with confidence scores
- User-friendly experience

## Backend
- FastAPI REST API
- Real-time predictions
- Feedback collection system
- SQLite integration

## AI Models
- Brain MRI image validation
- Multi-class tumor classification
- Confidence score output

---

#  Tumor Classes

The classifier predicts one of the following:

- Glioma
- Meningioma
- Pituitary
- No Tumor

---

#  Tech Stack

## Frontend
- React.js
- JavaScript
- CSS
- Axios / Fetch API

## Backend
- FastAPI
- Uvicorn
- Python

## Deep Learning
- TensorFlow
- Keras
- ResNet50
- NumPy
- OpenCV
- Pillow

## Database
- SQLite

---

#  Project Structure

```text
brain-tumor-ai/
│
├── app/                     # FastAPI Backend
│   ├── main.py
│   ├── services/
│   ├── utils/
│   ├── models/
│   ├── database/
│   └── feedback/
│
├── frontend/               # React Frontend
│   ├── src/
│   ├── public/
│   └── build/
│
├── requirements.txt
├── package.json
└── README.md