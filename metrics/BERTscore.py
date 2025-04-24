from bert_score import score

def calculate_bertscore(source_text: str, translated_text: str) -> float:
    try:
        # Validar que los textos no estén vacíos
        if not source_text or not translated_text:
            raise ValueError("Source or translated text is empty")

        # Calcular BERTScore
        print(f"BERTScore: Calculating for source='{source_text}', translated='{translated_text}'")
        P, R, F1 = score(
            [translated_text],
            [source_text],
            model_type="microsoft/mdeberta-v3-base",
            lang=None,
            verbose=True,
            device="cpu"
        )

        # Verificar si F1 tiene un valor válido
        if F1 is None or len(F1) == 0:
            raise ValueError("F1 score is empty or None")

        # Calcular el puntaje base
        raw_score = F1.mean().item()
        print(f"BERTScore: Raw score = {raw_score}")

        return max(min(raw_score, 1.0), 0.0)

    except Exception as e:
        raise Exception(f"Failed to calculate BERTScore: {str(e)}")