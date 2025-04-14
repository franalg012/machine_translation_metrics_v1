from comet import download_model, load_from_checkpoint

MODEL = download_model("wmt20-comet-da")  # o el modelo que funcione en tu versión
model = load_from_checkpoint(MODEL)

def calculate_comet(source_text: str, translated_text: str, reference_text: str = None) -> float:
    data = [{
        "src": source_text,
        "mt": translated_text,
        "ref": reference_text if reference_text else translated_text
    }]
    try:
        prediction = model.predict(data, batch_size=1, gpus=0)
        return prediction["scores"][0]
    except Exception as e:
        raise ValueError(f"Error en COMET: {str(e)}")
