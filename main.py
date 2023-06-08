from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
     Hello, my name is Abid Ali. And, uh -- and I like cheeseburgers. [laughs] 
     But I also have other interests such as playing online games like Dota 2.
"""
audio_array = generate_audio(text_prompt)

# play text in notebook
Audio(audio_array, rate=SAMPLE_RATE)