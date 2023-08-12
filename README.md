# Project Title: Image Classification with Updated AlexNet

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Model Architecture](#model-architecture)
7. [Data Preprocessing](#data-preprocessing)
8. [Training](#training)
9. [Deployment](#deployment)
10. [API Endpoints](#api-endpoints)
11. [License](#license)
12. [Acknowledgments](#acknowledgments)

## Introduction

This project is an implementation of an updated version of the AlexNet architecture for image classification. It classifies images into three categories: dogs, vehicles, and food. The model is trained using TensorFlow and deployed as a web application using Flask. This README provides comprehensive details about the project, including its features, technologies, installation, usage, and more.

## Features

- **Modernized AlexNet Architecture**: Incorporates improvements to the original AlexNet design.
- **Custom Training Loop**: Enables fine-tuning of the training process.
- **Web Interface**: Allows users to classify images through a web browser.
- **Integration with Google Cloud AI Platform**: Ensures scalable and efficient predictions.

## Technologies

- **Python**: The primary programming language used.
- **TensorFlow**: For building and training the deep learning model.
- **Flask**: For web application development.
- **OpenCV**: For image processing.
- **Google Cloud AI Platform**: For deploying the model.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- TensorFlow 2.12
- Flask
- OpenCV
- Google Cloud SDK

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd your-repo-name
   ```

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Web Application

1. **Start the Flask Application**:
   ```bash
   python app.py
   ```

2. **Open a Web Browser** and navigate to `http://0.0.0.0:5106`.

3. **Upload an Image** and click on the "Predict" button to classify it.

### Using the Model Programmatically

You can also use the trained model programmatically by importing it into your Python script.

## Model Architecture

The updated AlexNet architecture consists of:

- **5 Convolutional Layers**: With varying numbers of filters and kernel sizes.
- **3 Max-Pooling Layers**: For down-sampling the feature maps.
- **Batch Normalization**: Applied after each convolutional layer.
- **3 Fully Connected Layers**: Including two with 2048 units and one with the number of classes.
- **Dropout Layers**: To prevent overfitting.

## Data Preprocessing

The data preprocessing includes:

- **Resizing Images**: To a uniform size of 64x64 pixels.
- **Normalization**: Scaling pixel values to the range [0, 1].
- **Data Augmentation**: Optional techniques to increase the diversity of the training data.

## Training

The training process includes:

- **Custom Training Loop**: With gradient descent optimization.
- **Early Stopping**: To prevent overfitting.
- **Metrics Tracking**: Including training accuracy, validation accuracy, and loss.
- **Model Saving**: The best model is saved based on validation accuracy.

## Deployment

The model is deployed as a Flask web application, with the following features:

- **User-Friendly Interface**: For uploading and classifying images.
- **Integration with Google Cloud AI Platform**: For scalable predictions.
- **Secure Data Handling**: Ensuring that user data is handled securely.

## API Endpoints

- **`/`**: The main page for uploading images.
- **`/predict`**: The endpoint for receiving image uploads and returning predictions.

# License and Academic Integrity Statement
This project is licensed under the MIT License.

By using this code, you agree to abide by the principles of academic integrity. Utilizing this code in academic projects or coursework without proper attribution may constitute plagiarism or other violations of academic integrity policies.

It is your responsibility to understand and comply with your institution's academic integrity guidelines. If you intend to use this code as part of an academic assignment or research, make sure to properly cite it, and consult with your instructor, supervisor, or appropriate academic staff to ensure that you are in compliance with all relevant policies and regulations.

## Acknowledgments

- **Original AlexNet Paper**: By Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton.
- **TensorFlow Community**: For providing an excellent deep learning framework.
- **Flask Community**: For enabling easy web deployment.

