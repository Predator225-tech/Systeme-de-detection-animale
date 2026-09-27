import psycopg2
from datetime import datetime

def save_training_to_db(epochs, dataset_size, map50, map_full, weights_path, classes_list):
    """Enregistre les métriques de l'IA et ses classes dans PostgreSQL."""
    try:
        # Connexion à votre base PostgreSQL
        connection = psycopg2.connect(
            dbname="votre_base",
            user="votre_utilisateur",
            password="votre_mot_de_passe",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # 1. Insérer la session d'entraînement
        insert_session_query = """
            INSERT INTO training_sessions (epochs, dataset_size, map50, map_full, weights_path)
            VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """
        cursor.execute(insert_session_query, (epochs, dataset_size, map50, map_full, weights_path))
        session_id = cursor.fetchone()[0]

        # 2. Insérer les classes personnalisées associées
        for class_name in classes_list:
            insert_class_query = """
                INSERT INTO model_classes (session_id, class_name)
                VALUES (%s, %s);
            """
            cursor.execute(insert_class_query, (session_id, class_name))

        connection.commit()
        cursor.close()
        connection.close()
        print("✅ Session et classes enregistrées dans PostgreSQL avec succès !")

    except Exception as error:
        print(f"❌ Erreur de connexion à PostgreSQL : {error}")