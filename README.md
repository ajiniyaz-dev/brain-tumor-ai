# Brain Tumor Detection AI

A full-stack AI-powered medical imaging web application for automated **brain MRI validation** and **brain tumor classification** using deep learning.

The platform helps users upload MRI scans and receive AI-assisted predictions through an interactive web interface.

## Core System Components

- **FastAPI Backend** – Handles REST API requests and model inference
- **React Frontend** – Provides a modern user interface for image upload and prediction results
- **TensorFlow / Keras Models** – Performs medical image analysis using deep learning

## AI Pipeline

Two separate models are used:

1. **MRI Detector Model** – Verifies whether the uploaded image is a valid brain MRI scan  
2. **Tumor Classification Model** – Predicts tumor type from valid MRI images


# Features

## Frontend
- Modern React-based user interface
- Easy MRI image upload system
- Real-time prediction results display
- Confidence score visualization
- Clean and user-friendly experience

## Backend
- FastAPI REST API architecture
- Real-time model inference
- Feedback collection system
- SQLite database integration
- Modular backend structure

## AI Capabilities
- Brain MRI image validation
- Multi-class tumor classification
- Confidence score generation
- Automated image preprocessing
- Fast prediction response time


# Tumor Classes

The classification model predicts one of the following categories:

- **Glioma** – Tumor that develops in the glial cells of the brain  
- **Meningioma** – Tumor that forms in the meninges surrounding the brain and spinal cord  
- **Pituitary** – Tumor located in the pituitary gland region  
- **No Tumor** – No detectable tumor pattern found in the MRI scan


# Tech Stack

## Frontend
- React.js
- JavaScript
- HTML5
- CSS3
- Axios / Fetch API

## Backend
- FastAPI
- Uvicorn
- Python

## Deep Learning / AI
- TensorFlow
- Keras
- ResNet50 (Transfer Learning)
- NumPy
- OpenCV
- Pillow

## Database
- SQLite

## Tools / Deployment
- GitHub
- Git
- Virtual Environment (venv)
- Cloud Deployment Ready


# Project Structure

```text
brain-tumor-ai/
│
├── app/                        # FastAPI backend
│   ├── main.py                 # Main API entry point
│   ├── services/              # Prediction and business logic
│   ├── utils/                 # Image preprocessing utilities
│   ├── models/                # AI model files / loaders
│   ├── database/             # SQLite database logic
│   └── feedback/             # Feedback handling system
│
├── frontend/                  # React frontend
│   ├── src/                  # Frontend source code
│   ├── public/               # Static assets
│   └── build/                # Production build files
│
├── requirements.txt          # Python dependencies
├── package.json              # Frontend dependencies
├── package-lock.json         # Locked npm versions
├── runtime.txt               # Deployment runtime version
├── .gitignore                # Ignored files/folders
└── README.md
``
# Installation & Local Setup

## 1. Clone Repository

```bash
git clone https://github.com/ajiniyaz-dev/brain-tumor-ai.git
cd brain-tumor-ai
