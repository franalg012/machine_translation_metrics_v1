from rouge_score import rouge_scorer

def calculate_rouge(source: str, translated: str) -> float:
    scorer = rouge_scorer.RougeScorer(['rougeL'], use_stemmer=True)
    scores = scorer.score(source, translated)
    return scores['rougeL'].fmeasure


'''
El RougeScorer se tiene que cambiar, si solo se pone rouge dara error
"rouge": "Error: Invalid rouge type: rouge",

Elegir entre:
rouge1 = unigrama como en Bleu
rouge2 = bigrama
rougeL = mas de uno
rougeLsum = para textos mas largos

!!CAMBIAR tanbien en routes.py en la parte de elif

'''