from comet import download_model, load_from_checkpoint

def calculate_comet(source_text: str, translated_text: str) -> float:
    try:
        model_path = download_model("wmt20-comet-qe-da")
        model = load_from_checkpoint(model_path)
        data = [{"src": source_text, "mt": translated_text}]
        predictions = model.predict(data, batch_size=1, gpus=0)
        score = predictions["scores"][0] if predictions["scores"] else 0.0
        return max(min(score, 1.0), -1.0)
    except Exception as e:
        return f"Error in COMET: {str(e)}"