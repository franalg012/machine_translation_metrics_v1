from bleurt import score

def calculate_bleurt(source: str, translated: str) -> float:
    scorer = score.BleurtScorer()
    scores = scorer.score(references=[source], candidates=[translated])
    return scores[0]