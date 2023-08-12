from flask import Flask, render_template, request
from google.cloud import aiplatform
import numpy as np
import cv2
import base64


app = Flask(__name__)
endpoint = aiplatform.Endpoint(
    endpoint_name="projects/891542847217/locations/us-central1/endpoints/7980662213700485120")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image file
    image_file = request.files['image']

    # Read the image data
    image_data = image_file.read()

    # Preprocess the image
    preprocessed_image = preprocess_input_image(image_data)
    
    # Make a prediction using the model
    predictions = endpoint.predict(instances=preprocessed_image).predictions
    predicted_index = np.argmax(predictions[0])
    categories = ['dogs', 'vehicles', 'food']
    predicted_category = categories[predicted_index]
    confidence = predictions[0][predicted_index]

    # Convert the image to base64
    img_base64 = base64.b64encode(image_data).decode('utf-8')

    # Return the prediction as a JSON response
    return render_template('index.html', prediction=predicted_category, img_data=img_base64, confidence=confidence)

def preprocess_input_image(image_data):
    img = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (64, 64))
    return np.expand_dims(img, axis=0).tolist()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5106)
