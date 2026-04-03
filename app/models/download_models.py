import os
import gdown

MODEL_DIR = "app/models"
os.makedirs(MODEL_DIR, exist_ok=True)

MODELS = {
    "brain_tumor.weights.h5": "1NRDolErsri2I4FneT6Ov_0jRJpkA6NoE",
    "mri_detector.weights.h5": "1jW18EZOnl1nYcEyjZ8Cc_dFEqATwk7VO"
}

def download_models():
    for filename, file_id in MODELS.items():
        path = os.path.join(MODEL_DIR, filename)

        if not os.path.exists(path):
            print(f"Downloading {filename}...")
            url = f"https://drive.google.com/uc?id={file_id}"
            gdown.download(url, path, quiet=False)
        else:
            print(f"{filename} already exists")