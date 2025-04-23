from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from metrics.bleu import calculate_bleu
from metrics.meteor import calculate_meteor
from metrics.rouge import calculate_rouge
from metrics.comet import calculate_comet
from metrics.bleurt import calculate_bleurt
from metrics.BERTscore import calculate_bertscore

router = APIRouter()

class TranslationPair(BaseModel):
    source_text: str
    translated_text: str
    reference_text: Optional[str] = None

class MetricsRequest(BaseModel):
    pairs: List[TranslationPair]
    metrics: List[str]

@router.post("/evaluate")
async def evaluate_metrics(request: MetricsRequest):
    available_metrics = {"bleu", "meteor", "rougeL", "comet", "bleurt", "bertscore"}
    invalid_metrics = set(request.metrics) - available_metrics
    if invalid_metrics:
        raise HTTPException(status_code=400, detail=f"Invalid metrics: {invalid_metrics}")

    results = []
    for pair in request.pairs:
        reference_text = pair.reference_text
        metrics_requiring_reference = {"bleu", "meteor", "rougeL", "bleurt"}
        metrics_not_using_reference = {"comet", "bertscore"}

        missing_reference_metrics = metrics_requiring_reference.intersection(request.metrics)
        if missing_reference_metrics and reference_text is None:
            pass

        reference_present_metrics = metrics_not_using_reference.intersection(request.metrics)
        if reference_present_metrics and reference_text is not None:
            pass

        pair_result = {
            "source": pair.source_text,
            "translated": pair.translated_text,
            "reference": reference_text if reference_text else "Not provided",
            "scores": {}
        }

        for metric in request.metrics:
            try:
                if metric == "bleu":
                    if not reference_text:
                        pair_result["scores"]["bleu"] = "Error: BLEU requires reference_text"
                        continue
                    score = calculate_bleu(reference_text, pair.translated_text)
                    pair_result["scores"]["bleu"] = score
                elif metric == "meteor":
                    if not reference_text:
                        pair_result["scores"]["meteor"] = "Error: METEOR requires reference_text"
                        continue
                    score = calculate_meteor(reference_text, pair.translated_text)
                    pair_result["scores"]["meteor"] = score
                elif metric == "rougeL":
                    if not reference_text:
                        pair_result["scores"]["rougeL"] = "Error: ROUGE-L requires reference_text"
                        continue
                    score = calculate_rouge(reference_text, pair.translated_text)
                    pair_result["scores"]["rouge"] = score
                elif metric == "comet":
                    if reference_text is not None:
                        pair_result["scores"]["comet"] = "Error: COMET should not be used with reference_text"
                        continue
                    score = calculate_comet(source_text=pair.source_text, translated_text=pair.translated_text)
                    pair_result["scores"]["comet"] = score
                elif metric == "bleurt":
                    if not reference_text:
                        pair_result["scores"]["bleurt"] = "Error: BLEURT requires reference_text"
                        continue
                    score = calculate_bleurt(reference_text, pair.translated_text)
                    pair_result["scores"]["bleurt"] = score
                elif metric == "bertscore":
                    if reference_text is not None:
                        pair_result["scores"]["bertscore"] = "Error: BERTScore should not be used with reference_text"
                        continue
                    score = calculate_bertscore(source_text=pair.source_text, translated_text=pair.translated_text)
                    pair_result["scores"]["bertscore"] = score
            except Exception as e:
                pair_result["scores"][metric] = f"Error: {str(e)}"

        results.append(pair_result)

    return {"results": results}