import os
from google import genai
from PIL import Image
from google.genai.errors import ServerError

class AnimalDetector:
    def __init__(self):
        """Initialise le client officiel Google GenAI."""
        print("Initialisation du modèle multimodal Gemini...")
        self.client = genai.Client()

    def detect(self, source_path):
        """Envoie l'image optimisée à Gemini avec gestion des erreurs de réponse vide."""
        if not os.path.exists(source_path):
            raise FileNotFoundError(f"Le fichier '{source_path}' est introuvable.")

        image = Image.open(source_path)
        image.thumbnail((512, 512))

        try:
            # Appel au modèle
            response = self.client.models.generate_content(
                model='gemini-3.8-flash',
                contents=[
                    image, 
                    "Analyse cette image. Quel est cet animal précisément ? Réponds en français de manière directe et courte (2 ou 3 mots)."
                ],
                config={
                    "max_output_tokens": 15,
                    "temperature": 0.1
                }
            )
            
            # Vérification sécurisée si le texte est bien présent
            if response.text:
                return response.text.strip()
            else:
                return "Impossible d'identifier l'animal (réponse vide de l'IA)."
            
        except ServerError:
            return "⚠️ Le service Gemini est momentanément saturé (Erreur 503). Veuillez réessayer."
        except Exception as e:
            return f"Erreur lors de l'analyse : {str(e)}"