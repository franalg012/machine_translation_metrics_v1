from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from metrics.bleu import calculate_bleu
from metrics.meteor import calculate_meteor
from metrics.rouge import calculate_rouge
from metrics.comet import calculate_comet
from metrics.bleurt import calculate_bleurt

router = APIRouter()

class TranslationPair(BaseModel):
    source_text: str
    translated_text: str

class MetricsRequest(BaseModel):
    pairs: List[TranslationPair]
    metrics: List[str]

@router.post("/evaluate")
async def evaluate_metrics(request: MetricsRequest):
    available_metrics = {"bleu", "meteor", "rougeL", "comet", "bleurt"}
    invalid_metrics = set(request.metrics) - available_metrics
    if invalid_metrics:
        raise HTTPException(status_code=400, detail=f"Invalid metrics: {invalid_metrics}")

    results = []
    for pair in request.pairs:
        pair_result = {"source": pair.source_text, "translated": pair.translated_text, "scores": {}}
        
        for metric in request.metrics:
            try:
                if metric == "bleu":
                    pair_result["scores"]["bleu"] = calculate_bleu(pair.source_text, pair.translated_text)
                elif metric == "meteor":
                    pair_result["scores"]["meteor"] = calculate_meteor(pair.source_text, pair.translated_text)
                elif metric == "rougeL":
                    pair_result["scores"]["rouge"] = calculate_rouge(pair.source_text, pair.translated_text)
                elif metric == "comet":
                    pair_result["scores"]["comet"] = calculate_comet(source_text=pair.source_text,translated_text= pair.translated_text)
                elif metric == "bleurt":
                    pair_result["scores"]["bleurt"] = calculate_bleurt(pair.source_text, pair.translated_text)
            except Exception as e:
                pair_result["scores"][metric] = f"Error: {str(e)}"
        
        results.append(pair_result)
    
    return {"results": results}