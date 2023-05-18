import pyttsx3

def get_available_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.stop()
    return voices

def set_voice(voice_id):
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    engine.stop()

def set_speaking_rate(rate):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.stop()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Get available voices
voices = get_available_voices()
print("Available Voices:")
for idx, voice in enumerate(voices):
    print(f"{idx + 1}. {voice.name}")

# Prompt user to select a voice
selected_voice_index = int(input("Select the voice number: ")) - 1
selected_voice = voices[selected_voice_index]
set_voice(selected_voice.id)

# Prompt user to enter speaking rate
speaking_rate = int(input("Enter the speaking rate (words per minute): "))
set_speaking_rate(speaking_rate)

# Prompt user to enter the text to synthesize
text = input("Enter the text you want to synthesize: ")
speak(text)
