-- Table des sessions d'entraînement
CREATE TABLE training_sessions (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    epochs INT NOT NULL,
    dataset_size INT NOT NULL,
    map50 FLOAT NOT NULL,
    map_full FLOAT NOT NULL,
    weights_path VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'Terminé'
);

-- Table des classes associées à l'entraînement
CREATE TABLE model_classes (
    id SERIAL PRIMARY KEY,
    session_id INT REFERENCES training_sessions(id) ON DELETE CASCADE,
    class_name VARCHAR(100) NOT NULL
);