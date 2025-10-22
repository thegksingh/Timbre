import asyncio
import edge_tts
import os

class Tts:
    def __init__(self):
        self.output_dir = "outputs/mp3"

    async def generate_audio(self,text: str, voice: str, rate: str , pitch: str , output_name: str = "output_audio"):
        output_path = os.path.join(self.output_dir, f"{output_name}.mp3")
       
        audio = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        await audio.save(output_path)
        return output_path
        

    def convert(self, text: str,voice: str, rate: str = "+0%", pitch: str = "+0Hz", output_name: str = "output_audio"):
        return asyncio.run(self.generate_audio(text, voice, rate, pitch, output_name))
