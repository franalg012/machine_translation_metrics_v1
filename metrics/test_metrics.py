from metrics.bleu import calculate_bleu
from metrics.rouge import calculate_rouge
from metrics.meteor import calculate_meteor

def test_metrics():
    text = "Me gusta comer tartas"
    print(f"Testing with text: '{text}'")
    print(f"BLEU: {calculate_bleu(text, text)}")
    print(f"ROUGE: {calculate_rouge(text, text)}")
    print(f"METEOR: {calculate_meteor(text, text)}")

if __name__ == "__main__":
      test_metrics()