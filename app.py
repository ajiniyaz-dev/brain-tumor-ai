import gradio as gr
import numpy as np
from PIL import Image

from app.services.brain_detector import detect_brain_mri
from app.services.tumor_predictor import predict_tumor


def predict(image):
    try:
        if image is None:
            return "Please upload an image"

        # Convert PIL → numpy
        if isinstance(image, Image.Image):
            image = np.array(image)

        # Step 1: MRI detection
        mri_result = detect_brain_mri(image)

        if mri_result["status"] == "not_brain":
            return f" Not a brain MRI (confidence: {mri_result['confidence']:.2f})"

        if mri_result["status"] == "uncertain":
            return f" Uncertain image (confidence: {mri_result['confidence']:.2f})"

        if mri_result["status"] == "error":
            return f" Error: {mri_result['message']}"

        # Step 2: Tumor prediction
        tumor_result = predict_tumor(image)

        return f" MRI Confirmed\n{tumor_result}"

    except Exception as e:
        return f" Error: {str(e)}"


demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Brain MRI Tumor Detection",
    description="Upload an image to verify MRI and detect tumor type"
)

demo.launch()