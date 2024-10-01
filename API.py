
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import numpy as np
import cv2
from PIL import Image
import io
import torch

app = FastAPI()

# Load your best performing model (replace 'YourModel' with your model)
model = torch.load("path_to_your_best_model.pth", map_location='cpu')
model.eval()

class SegmentationResult(BaseModel):
    dice_score: float
    segmentation: list

@app.post("/predict", response_model=SegmentationResult)
async def predict(file: UploadFile = File(...)):
    # Read the uploaded image
    image = Image.open(io.BytesIO(await file.read()))
    image = np.array(image)

    # Preprocess the image
    image = cv2.resize(image, (256, 256))  # Adjust size as per your model
    image = image / 255.0  # Normalization

    # Convert to tensor and add batch dimension
    image_tensor = torch.tensor(image).unsqueeze(0).unsqueeze(0).float()

    # Perform prediction
    with torch.no_grad():
        output = model(image_tensor)
        # Assuming output contains segmentation results (you may need to adjust this)
        prediction = torch.sigmoid(output).squeeze().numpy().tolist()

    # Dummy DICE score for the response (replace with actual calculation)
    dice_score = 0.85

    return SegmentationResult(dice_score=dice_score, segmentation=prediction)
