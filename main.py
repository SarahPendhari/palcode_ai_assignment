from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from ultralytics import YOLO
from PIL import Image
import io
import os
import requests

app = FastAPI()

MODEL_PATH = "best.pt"
MODEL_URL = "https://github.com/YOUR_USERNAME/YOUR_REPO/releases/download/v1.0/best.pt"

# Download model weights if not present
if not os.path.exists(MODEL_PATH):
    print("Downloading model weights...")
    r = requests.get(MODEL_URL)
    with open(MODEL_PATH, "wb") as f:
        f.write(r.content)

# Load the YOLO model
model = YOLO(MODEL_PATH)

@app.post("/detect")
async def detect(image: UploadFile = File(...)):
    contents = await image.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB")
    results = model(img)

    detections = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            w, h = x2 - x1, y2 - y1
            label = model.names[int(box.cls)]
            confidence = round(float(box.conf), 2)
            detections.append({
                "label": label,
                "confidence": confidence,
                "bbox": [int(x1), int(y1), int(w), int(h)]
            })

    return JSONResponse(content={"detections": detections})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
