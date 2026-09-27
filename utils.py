import os
from werkzeug.utils import secure_filename
from Model import LocalYoloDetector
from Modelv2 import AnimalDetector

# Initialisation des deux détecteurs
yolo_detector = LocalYoloDetector()
gemini_detector = AnimalDetector()

UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def process_uploaded_image(file, model_choice='online'):
    """Traite l'image selon le modèle choisi ('local' ou 'online')."""
    if file and file.filename != '':
        filename = secure_filename(file.filename)
        input_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(input_path)
        
        # Choix du modèle
        if model_choice == 'local':
            animal_name = yolo_detector.detect(input_path)
        else:
            animal_name = gemini_detector.detect(input_path)
            
        return filename, filename, animal_name
    
    return None, None, None