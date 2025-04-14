from nltk.translate.meteor_score import meteor_score
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

def calculate_meteor(source: str, translated: str) -> float:
    return meteor_score([word_tokenize(source)], word_tokenize(translated))