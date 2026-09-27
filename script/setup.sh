#!/bin/bash

echo "=== Vérification de l'environnement pour le projet d'IA ==="

# 1. Vérification de Python 3
if ! command -v python3 &> /dev/null; then
    echo "[ERREUR] Python 3 n'est pas installé."
    exit 1
else
    echo "[OK] Python 3 est détecté."
fi

# 2. Vérification / Création de l'environnement virtuel (.venv)
VENV_DIR=".venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "[ATTENTION] Aucun environnement virtuel détecté."
    read -p "Voulez-vous créer un environnement virtuel et installer les dépendances ? (y/n) : " choice
    case "$choice" in
      y|Y )
        echo "Création de l'environnement virtuel..."
        python3 -m venv "$VENV_DIR"
        
        echo "Activation et installation des dépendances..."
        ./$VENV_DIR/bin/python -m pip install --upgrade pip
        ./$VENV_DIR/bin/python -m pip install scikit-learn pillow numpy
        echo "=== Environnement configuré avec succès ! ==="
        ;;
      * )
        echo "Installation annulée."
        exit 1
        ;;
    esac
else
    # Vérification des bibliothèques à l'intérieur du venv
    MISSING_LIBS=()
    for lib in numpy PIL sklearn; do
        if ! ./$VENV_DIR/bin/python -c "import $lib" &> /dev/null; then
            MISSING_LIBS+=("$lib")
        fi
    done

    if [ ${#MISSING_LIBS[@]} -eq 0 ]; then
        echo "=== L'environnement est optimal ! Tout est déjà prêt. ==="
    else
        echo "[ATTENTION] Des bibliothèques manquent dans l'environnement virtuel."
        read -p "Voulez-vous les installer ? (y/n) : " choice
        case "$choice" in
          y|Y )
            ./$VENV_DIR/bin/python -m pip install scikit-learn pillow numpy
            echo "=== Installation terminée avec succès ! ==="
            ;;
          * )
            echo "Installation annulée."
            exit 1
            ;;
        esac
    fi
fi