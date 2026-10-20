# SENTINEL — Real-Time Computer Vision System

SENTINEL is a Python-based computer vision project that detects faces in a live webcam feed and monitors their position relative to a predefined region.

When a detected face remains outside the designated monitoring zone for more than one second, SENTINEL displays an on-screen alert.

This project was developed to explore real-time image processing, face detection, and computer vision application development.

## Features

- **Real-Time Face Detection:** Detects faces using a webcam feed.
- **Monitoring Zone:** Defines a region within the camera frame.
- **Boundary Monitoring:** Checks whether a detected face's centre lies inside or outside the designated zone.
- **Alert System:** Displays an alert when a face remains outside the zone beyond a one-second grace period.
- **Fullscreen Interface:** Provides a fullscreen camera-monitoring display.
- **Local Processing:** Processes camera frames locally without requiring cloud-based vision processing.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam capture, image processing, and visualisation |
| MediaPipe | Face detection framework |
| TensorFlow Lite (TFLite) | Lightweight model format used by the face detector |

## How It Works

1. SENTINEL captures frames from the computer's webcam.
2. Each frame is converted from BGR to RGB for processing.
3. MediaPipe's face detector analyses the image using a TensorFlow Lite model.
4. SENTINEL calculates the centre of the detected face's bounding box.
5. The face's position is compared with the predefined monitoring zone.
6. If the face remains outside the zone for at least one second, an on-screen alert appears.

## Requirements

- Python 3.10 or another Python version compatible with your installed dependencies
- A working webcam
- OpenCV
- MediaPipe
- The `face_detector.tflite` model file

## Acknowledgements

SENTINEL uses the following computer vision technologies:

- **MediaPipe** — Face detection framework and model integration.
  https://ai.google.dev/edge/mediapipe/solutions/vision/face_detector

- **TensorFlow Lite (TFLite)** — Model format and inference ecosystem.
  https://www.tensorflow.org/lite

The face detection model is a third-party asset. Credit and licensing
terms should be verified against the original model source.

SENTINEL's application code and its dependencies may have separate
licensing terms.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Mukesh-Kiran101/sentinel.git
cd sentinel
