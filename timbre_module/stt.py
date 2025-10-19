import whisper

class Stt:

    def __init__(self, model: str = "base"):
        self.model = whisper.load_model(model)
           
    def generate(self, path: str):
        result = self.model.transcribe(path)
        return(result["text"])
