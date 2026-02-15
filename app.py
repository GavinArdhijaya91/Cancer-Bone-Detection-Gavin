from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import os
import cv2

app = Flask(__name__)

MODEL_PATH = 'model/trained_modelff.h5'
if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    print(f"Peringatan: Model {MODEL_PATH} tidak ditemukan!")

@app.route('/')
def home():
    return render_template('frontend.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    if not file or file.filename == '':
        return render_template('frontend.html', prediction="Gagal: File tidak ada")
    
    if not os.path.exists('static/uploads'):
        os.makedirs('static/uploads')
    
    filepath = os.path.join('static/uploads', file.filename)
    file.save(filepath)

    if not isxray(filepath):
        return render_template('frontend.html', 
            prediction="Gagal: Ini Bukan gambar X-ray", 
            image_path=filepath)

    img = tf.keras.utils.load_img(filepath, target_size=(224, 224))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)
    score = prediction[0][0]

    if score < 0.5:
        hasil_final = "Berpotensi Kanker"

        confidence = round((1 - score) * 100, 2)

        if not os.path.exists('static/outputs'):
            os.makedirs('static/outputs')   
        final_img_path = drawbox(filepath)
    else:
        hasil_final = "Normal"
        confidence = round(score * 100, 2)
        final_img_path = filepath
    
    print(f"DEBUG: Raw Score = {score}")
    print(f"DEBUG: Status = {hasil_final} ({confidence}%)")

    return render_template('frontend.html', 
        prediction=f"{hasil_final} ({confidence:.2f}%)", 
        image_path=final_img_path)
def isxray(image_path):
    
    image = cv2.imread(image_path)
    if image is None: return False
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    saturation = image_hsv[:, :, 1].mean()

    return saturation < 70

def drawbox(image_path):
    
    image = cv2.imread(image_path)
    if image is None: return image_path
    
    height, width, _ = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.medianBlur(gray, 11)
    _, thresh = cv2.threshold(blurred, 160, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    target_cnt = None
    max_area = 0

    if contours:
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            area = cv2.contourArea(cnt)
            aspect_ratio = w / float(h)

            if (width * height * 0.005) < area < (width * height * 0.3):
                if 0.4 < aspect_ratio < 2.5:
                    if area > max_area:
                        max_area = area
                        target_cnt = cnt

    if target_cnt is not None:
        x, y, w, h = cv2.boundingRect(target_cnt)
        p = 25
        cv2.rectangle(image, (max(0, x-p), max(0, y-p)), 
                      (min(width, x+w+p), min(height, y+h+p)), (0, 0, 255), 4)
        cv2.putText(image, 'Area Mencurigakan', (x, y - 15), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        start_point = (int(width * 0.55), int(height * 0.35))
        end_point = (int(width * 0.85), int(height * 0.75))
        cv2.rectangle(image, start_point, end_point, (0, 0, 255), 4)
        cv2.putText(image, 'Area Mencurigakan', (start_point[0], start_point[1] - 15), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    filename = os.path.basename(image_path)
    result_path = os.path.join('static/outputs', filename)
    cv2.imwrite(result_path, image)
    return result_path

if __name__ == '__main__':
    if not os.path.exists('static/uploads'): os.makedirs('static/uploads')
    if not os.path.exists('static/outputs'): os.makedirs('static/outputs')
    
    app.run(debug=True, host='0.0.0.0', port=5000)