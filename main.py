import sys
import pyttsx3

try:
    import pyttsx3
except ImportError:
   
    print('pip install pyttsx3')

    sys.exit()

tts = pyttsx3.init()  # Initialize the TTS engine.

print('Text To Speech Talker project, AKBogati123')
print('Text-to-speech using the pyttsx3 module, which in turn uses')
print('the NSSpeechSynthesizer (on macOS), SAPI5 (on Windows), or')
print('eSpeak (on Linux) speech engines.')
print()
print('Enter the text to speak, or QUIT to quit.')
while True:
    text = input('> ')

    if text.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()

    tts.say(text)  # Add some text for the TTS engine to say.
    tts.runAndWait()  # Make the TTS engine say the added text and wait for completion.
