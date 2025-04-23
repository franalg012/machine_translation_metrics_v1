from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from nltk.tokenize import word_tokenize
import nltk
import string

nltk.download('punkt')

def calculate_bleu(reference: str, hypothesis: str) -> float:
    if not reference.strip() or not hypothesis.strip():
        return 0.0
    try:
        ref_tokens = [w for w in word_tokenize(reference.lower()) if w not in string.punctuation]
        hyp_tokens = [w for w in word_tokenize(hypothesis.lower()) if w not in string.punctuation]
        if not ref_tokens or not hyp_tokens:
            return 0.0
        smoothie = SmoothingFunction().method4
        score = sentence_bleu([ref_tokens], hyp_tokens, smoothing_function=smoothie)
        return round(score, 4)
    except Exception as e:
        return 0.0