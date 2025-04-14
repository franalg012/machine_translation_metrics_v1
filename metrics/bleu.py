from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction

def calculate_bleu(reference: str, hypothesis: str) -> float:
    ref_tokens = reference.lower().split()
    hyp_tokens = hypothesis.lower().split()
    
    smoothie = SmoothingFunction().method4
    score = sentence_bleu([ref_tokens], hyp_tokens, smoothing_function=smoothie)
    return round(score, 4)
