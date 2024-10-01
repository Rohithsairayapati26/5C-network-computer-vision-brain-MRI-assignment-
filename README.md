
# Brain Metastasis Segmentation

This repository contains code for brain metastasis segmentation using MRI images. We implemented two deep learning architectures: Nested U-Net (U-Net++) and Attention U-Net, and developed a web application with FastAPI and Streamlit to visualize segmentation results.

## Table of Contents
- [Data Preprocessing](#data-preprocessing)
- [Model Implementation](#model-implementation)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Web Application](#web-application)
- [How to Run](#how-to-run)
- [Challenges and Solutions](#challenges-and-solutions)

## Data Preprocessing

We applied Contrast Limited Adaptive Histogram Equalization (CLAHE) to enhance the visibility of brain metastases in the MRI images. We also normalized the images and used data augmentation techniques (such as rotations and flips) to improve model generalization and performance.

## Model Implementation

### a. Nested U-Net (U-Net++)
Nested U-Net (U-Net++) uses nested and dense skip connections to improve segmentation accuracy. This architecture helps capture fine details, making it effective for detecting small metastases.

### b. Attention U-Net
Attention U-Net adds attention gates to the U-Net architecture. These gates help the model focus on the metastases by highlighting important regions in the MRI images, improving segmentation performance.

## Model Training and Evaluation

We trained both models on the preprocessed dataset. We used the Dice Score as the main evaluation metric to measure how well the models segmented the metastases compared to the ground truth.

### Performance Comparison
- **Nested U-Net (U-Net++)**: Dice Score: `XX%`
- **Attention U-Net**: Dice Score: `YY%`

The Attention U-Net performed better with smaller metastases, while U-Net++ handled complex structures more effectively.

## Web Application

We built a web application to serve the best-performing model (Attention U-Net). The app uses:
- **FastAPI**: For the backend, to serve segmentation results.
- **Streamlit**: For the frontend, where users can upload MRI images and see segmentation results.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/brain-metastasis-segmentation.git
   cd brain-metastasis-segmentation
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI backend:
   ```bash
   uvicorn app.main:app --reload
   ```

4. Launch the Streamlit frontend:
   ```bash
   streamlit run app/frontend.py
   ```

5. Open `http://localhost:8501` in your browser to upload MRI images and view segmentation results.

## Challenges and Solutions

### Challenges:
1. **Small Lesions**: Brain metastases are often small, making them hard to detect.
2. **Data Imbalance**: Metastases appear less frequently compared to normal brain tissue.

### Solutions:
- We used **CLAHE** to improve image contrast, making it easier to detect small metastases.
- We integrated **Attention U-Net** to focus on small, important areas in the MRI images.

## Conclusion

In this project, we successfully implemented Nested U-Net and Attention U-Net architectures to tackle brain metastasis segmentation. Our web application provides a user-friendly interface for uploading MRI images and viewing the segmentation results.
