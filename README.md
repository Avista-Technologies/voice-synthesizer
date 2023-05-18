# Voice Synthesis Application

This is a Python application that uses the `pyttsx3` library to synthesize text into speech.

## Installation

1. Clone the repository or download the source code.
```bash
git clone https://github.com/Avista-Technologies/voice-synthesizer.git
```

3. Navigate to the project directory.
```shell
cd voice-synthesis-application
```

Install the dependencies using pip and the requirements.txt file.
```bash
pip install -r requirements.txt
```

## Usage
Run the voice_synthesis.py script.
```bash
python voice_synthesis.py
```

The program will display a list of available voices. Enter the corresponding number to select a voice.

Enter the desired speaking rate (words per minute).

Enter the text you want to synthesize.

The application will convert the text into speech using the selected voice and speaking rate.

## Customization
You can customize the voice and speaking rate by modifying the respective parameters in the voice_synthesis.py script. The available voices and their IDs can be obtained by running the script with the get_available_voices() function.

## License
This project is licensed under the MIT License.
