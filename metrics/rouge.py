from rouge_score import rouge_scorer

def calculate_rouge(reference: str, translated: str) -> float:
    if not reference.strip() or not translated.strip():
        return 0.0
    try:
        scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
        scores = scorer.score(reference, translated)
        score = scores['rougeL'].fmeasure
        return score
    except Exception as e:
        return 0.0