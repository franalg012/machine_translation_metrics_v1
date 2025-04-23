from bert_score import score

def calculate_bertscore(source_text: str, translated_text: str) -> float:
    try:
        P, R, F1 = score(
            [translated_text],
            [source_text],
            lang="es", 
            model_type="xlm-roberta-base",
            verbose=False
        )
        return F1.mean().item()
    except Exception as e:
        return f"Error in BERTScore: {str(e)}"