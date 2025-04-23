from nltk.translate.meteor_score import meteor_score
from nltk.tokenize import word_tokenize
import nltk
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

def calculate_meteor(reference: str, translated: str) -> float:
    if not reference.strip() or not translated.strip():
        return 0.0
    try:
        ref_tokens = [w for w in word_tokenize(reference.lower()) if w not in string.punctuation]
        hyp_tokens = [w for w in word_tokenize(translated.lower()) if w not in string.punctuation]
        if not ref_tokens or not hyp_tokens:
            return 0.0
        score = meteor_score([ref_tokens], hyp_tokens)
        return score
    except Exception as e:
        return 0.0