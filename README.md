
# Brain Metastasis Segmentation

This repository contains code for brain metastasis segmentation using MRI images. We implemented two deep learning architectures: Nested U-Net (U-Net++) and Attention U-Net, and developed a web application with FastAPI and Streamlit to visualize segmentation results.

## Table of Contents
- [Data Preprocessing](#data-preprocessing)
- [Model Implementation (InceptionV3) and Evaluation](#model-implementation)
- [Web Application](#web-application)

## Data Preprocessing

This code sets up data augmentation and preprocessing for training a convolutional neural network (CNN) using Keras's ImageDataGenerator. The train_datagen object applies a series of random transformations to the training images, including rescaling, rotation, shifts, shearing, zooming, and flipping, which helps the model generalize better by providing a more diverse set of images during training. The val_datagen only rescales the validation images, ensuring they remain unaltered for evaluation. Both train_generator and validation_generator load images from their respective directories, resize them to a fixed target size, and generate batches of data for multi-class classification, where the labels are represented as one-hot encoded vectors. This approach is commonly used to prevent overfitting and improve model performance in image classification tasks.

## Model Implementation

This code implements a **transfer learning** approach using the pre-trained **InceptionV3** model for a **segmentation task**, likely for binary segmentation like metastasis detection in MRI images. The **InceptionV3** model is used as the encoder (with `include_top=False` to remove the classification layers), serving as a powerful feature extractor. The model’s output is then passed through a series of **convolutional** layers (`Conv2D`) with ReLU activation to capture spatial features, followed by **UpSampling2D** layers to progressively increase the spatial resolution of the feature maps back to the input image size. The final layer uses a 1x1 convolution with a **sigmoid** activation to output a segmentation mask where each pixel represents the probability of belonging to the target class (e.g., metastasis). The model is compiled with the **Adam optimizer** and **binary cross-entropy loss**, making it suitable for binary segmentation tasks.

## Model Training and Evaluation

We trained both models on the preprocessed dataset. We used the main evaluation metric to measure how well the models segmented the metastases compared to the ground truth.

## Web Application

We built a web application to serve the best-performing model (Attention U-Net). The app uses:
- **FastAPI**: For the backend, to serve segmentation results.
- **Streamlit**: For the frontend, where users can upload MRI images and see segmentation results.

## Conclusion

In this project, we successfully implemented Nested U-Net architectures to tackle brain metastasis segmentation. Our web application provides a user-friendly interface for uploading MRI images and viewing the segmentation results.
