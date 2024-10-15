from keras.models import load_model  
from PIL import Image, ImageOps 
import numpy as np
import sys

def init():
    np.set_printoptions(suppress=True)

def load_image(file_path):
    image = Image.open(file_path).convert("RGB")
    return image

def load_my_model():
    model = load_model(r"C:\Users\Risha\OneDrive\Desktop\05\model\keras_model.h5")

    class_names = open(r"C:\Users\Risha\OneDrive\Desktop\05\model\labels.txt", "r").readlines()

    return model, class_names

def prep_input(image):
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    return data

def predict(model, class_names, data):
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    print("Class:", class_name.strip())
    print("Confidence Score:", confidence_score)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rock-paper-scissors.py <path_to_image>")
        sys.exit(1)

    file_path = sys.argv[1]

    init()
    image = load_image(file_path)
    model, class_names = load_my_model()
    data = prep_input(image)
    predict(model, class_names, data)
