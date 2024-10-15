from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys

def init():
    np.set_printoptions(suppress=True)

def load_my_model():
    model = load_model(r"C:\Users\Risha\OneDrive\Desktop\05\model\keras_model.h5", compile=False)
    
    with open(r"C:\Users\Risha\OneDrive\Desktop\05\model\labels.txt", "r") as f:
        class_names = f.read().splitlines()
    
    return model, class_names

def prep_input(frame):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = cv2.resize(frame, (224, 224))
    
    normalized_image_array = (image.astype(np.float32) / 127.5) - 1
    
    data[0] = normalized_image_array

    return data

def predict(model, class_names, data):
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    print("Class:", class_name)
    print("Confidence Score:", confidence_score)

    return class_name, confidence_score

def main():
    init()
    model, class_names = load_my_model()
    
    cap = cv2.VideoCapture(0)  

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        
        data = prep_input(frame)

        class_name, confidence_score = predict(model, class_names, data)
        cv2.putText(frame, f"{class_name}: {confidence_score:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Live Camera Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
