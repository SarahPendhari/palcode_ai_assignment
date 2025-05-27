# AI Vision Exercise - Object Detection & Classification API

A FastAPI-based computer vision application for object detection and classification using YOLO and custom trained models.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![YOLO](https://img.shields.io/badge/YOLO-00FFFF?style=flat)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📁 Project Structure

```
ai-vision-exercise/
├── images/          # Directory containing input images for detection
├── labels/          # YOLO format label annotations
├── models/          # Trained model files
├── main.py          # FastAPI application
├── classes.txt     # Class names file
├── requirements.txt # Python dependencies
├── best.pt
└── README.md       # Project documentation (this file)
```

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SarahPendhari/palcode_ai_assignment.git
cd palcode_ai_assignment
```

### 2. Install Dependencies

Requires Python 3.8+

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI Server

```bash
uvicorn app:app --host 0.0.0.0 --port 10000
```

The API will be available at `http://localhost:10000`

### 4. Label Images (Required)

Use LabelImg to annotate your images in YOLO format:

```bash
# Install LabelImg
pip install labelImg

# Launch annotation tool
labelImg images/ labels/ classes.txt
```

**Important**: Ensure you have properly labeled at least 50-100 images for effective training.

## 🔍 API Documentation

### Endpoint: `/predict`

- **Method**: `POST`
- **Content-Type**: `multipart/form-data`
- **Request**: Image file (JPG, PNG, etc.)
- **Response**: JSON with detection results including:
  - Bounding boxes coordinates
  - Class predictions
  - Confidence scores
  - Annotated image (base64 or file)

### Interactive API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:10000/docs`
- ReDoc: `http://localhost:10000/redoc`

## 🧪 Testing the API

### Using cURL

```bash
curl -X 'POST' \
  'https://palcode-ai-assignment.onrender.com/detect' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'image=@image1.png;type=image/png'
```

### Using Python requests

```python
import requests
import json

url = "https://your-app-name.onrender.com/predict"
files = {"file": open("test-image.jpg", "rb")}
response = requests.post(url, files=files)

# Parse detection results
results = response.json()
print("Detected objects:", results)
```

## 📸 Required Screenshots & Documentation

As per the exercise requirements, please include the following in the `screenshots/` folder:

- ✅ **LabelImg Screenshot**: Image labeling interface with annotations
- ![Screenshot 2025-05-26 165723](https://github.com/user-attachments/assets/39e36235-f6f4-4ddb-9662-75198ab0e4df)

- ![Screenshot 2025-05-26 170906](https://github.com/user-attachments/assets/47abfb25-d6e7-48d3-a9e5-748f11b186e1)


- ✅ **Training Process**: Console output or training progress/loss graphs
- ![results](https://github.com/user-attachments/assets/e5d79159-8d0e-49b0-b007-9210c6f13a25)

- ✅ **API Testing**: Screenshots of successful API calls and responses
![image](https://github.com/user-attachments/assets/c0ef9035-52da-47a7-9615-127b53d111d0)


## 🌐 Deployment

### Public API URL
```
https://palcode-ai-assignment.onrender.com/docs
```



## 🛠️ Technology Stack

- **Framework**: FastAPI
- **Computer Vision**: YOLOv8
- **Deep Learning**: PyTorch/TensorFlow
- **Image Processing**: OpenCV, PIL
- **Annotation Tool**: LabelImg
- **Deployment**: Render

## 📋 Requirements

Create a `requirements.txt` file with:

```txt
fastapi
uvicorn[standard]
python-multipart
opencv-python
pillow
torch
torchvision
ultralytics
numpy
matplotlib
labelImg
pyyaml
```

## ✍️ Author

**Sarah Pendhari**  
University of Mumbai
