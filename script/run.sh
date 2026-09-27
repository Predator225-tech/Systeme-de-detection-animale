#!/bin/bash

echo "=== Lancement du projet de Détection de Chien ==="

VENV_DIR=".venv"

# 1. Vérifier si l'environnement virtuel existe
if [ ! -d "$VENV_DIR" ]; then
    echo "[ERREUR] L'environnement virtuel '$VENV_DIR' n'existe pas."
    echo "Veuillez d'abord exécuter './setup.sh' pour configurer le projet."
    exit 1
fi

# 2. Vérifier si le fichier main.py existe
if [ ! -f "main.py" ]; then
    echo "[ERREUR] Le fichier 'main.py' est introuvable dans ce répertoire."
    exit 1
fi

# 3. Exécution du script Python avec l'interpréteur du venv
echo "[OK] Exécution de main.py..."
echo "----------------------------------------"
./$VENV_DIR/bin/python main.py
echo "----------------------------------------"
echo "=== Fin de l'exécution ==="