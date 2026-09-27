from flask import Flask, render_template, request, redirect, url_for
from utils import process_uploaded_image

app = Flask(__name__)

# Route principale : Le Dashboard d'accueil (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route pour la page de Test / Analyse d'image
@app.route('/test', methods=['GET', 'POST'])
def test_page():
    # Récupère le choix du modèle depuis l'URL (en GET) ou le formulaire (en POST)
    model_choice = request.args.get('model_choice') or request.form.get('model_choice', 'online')

    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        
        file = request.files['image']
        original_img, result_img, animal_name = process_uploaded_image(file, model_choice)
        
        if original_img and result_img:
            return render_template('test.html', 
                                   original_image=original_img, 
                                   result_image=result_img, 
                                   animal_name=animal_name,
                                   model_choice=model_choice)
            
        return redirect(request.url)

    # En mode GET, on affiche simplement la page de test avec le modèle choisi pré-sélectionné
    return render_template('test.html', original_image=None, result_image=None, animal_name=None, model_choice=model_choice)# Route pour le Dashboard secondaire (si vous voulez garder les deux séparés)
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route pour Data Seeker
@app.route('/seeker')
def seeker():
    return render_template('seeker.html')

# Route pour Training
@app.route('/training', methods=['GET', 'POST'])
def training():
    message = None
    if request.method == 'POST':
        message = "Entraînement initié avec succès !"
    return render_template('training.html', message=message)

# Route pour Q&A
@app.route('/qa', methods=['GET', 'POST'])
def qa():
    answer = None
    if request.method == 'POST':
        question = request.form.get('question')
        answer = f"Réponse simulée pour : {question}"
    return render_template('qa.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)