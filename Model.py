import os
from ultralytics import YOLO

class LocalYoloDetector:
    def __init__(self):
        print("Chargement du modèle YOLO local...")
        # Utilise le fichier yolov8n.pt présent dans votre dossier
        self.model = YOLO('yolov8n.pt')

    def detect(self, source_path):
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Le fichier '{source_path}' est introuvable.")
        
        # Exécute la prédiction
        results = self.model(source_path)
        
        # Récupère les noms des classes détectées
        names = self.model.names
        detected_animals = []
        
        for r in results:
            for c in r.boxes.cls:
                cls_name = names[int(c)]
                detected_animals.append(cls_name)
                
        if detected_animals:
            # Retourne le premier animal trouvé (en français ou nom de classe YOLO)
            return f"Détecté par YOLO (Local) : {', '.join(set(detected_animals))}"
        else:
            return "Aucun animal détecté par YOLO."