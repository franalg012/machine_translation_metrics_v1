from sentence_transformers import SentenceTransformer, util

def calculate_sbert(source_text: str, translated_text: str) -> float:
    try:
        # Cargar un modelo más robusto
        model = SentenceTransformer('distiluse-base-multilingual-cased-v1')

        # Generar embeddings para el texto fuente y traducido
        source_embedding = model.encode(source_text, convert_to_tensor=True)
        translated_embedding = model.encode(translated_text, convert_to_tensor=True)

        # Calcular la similitud coseno
        cosine_score = util.cos_sim(source_embedding, translated_embedding)[0][0].item()

        # Normalizar el puntaje para evitar sobreestimación
        normalized_score = cosine_score * 0.8  # Reducimos ligeramente los puntajes altos
        final_score = max(min(normalized_score, 1.0), 0.0)

        print(f"SBERT: Raw score = {cosine_score}, Normalized score = {final_score}")
        return final_score
    except Exception as e:
        raise Exception(f"Error in SBERT: {str(e)}")