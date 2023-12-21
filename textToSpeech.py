from google.cloud import texttospeech
from google.oauth2 import service_account

# SPEAK MODELS

# tr-TR-Wavenet-A
# tr-TR-Wavenet-B
# tr-TR-Wavenet-C
# tr-TR-Wavenet-D
# tr-TR-Wavenet-E

class TextToSpeech:
    def __init__(self,input_text) -> None:
        self.input_text     =   input_text
        self.output_file    =   "text.wav"
        self.language_code  =   "tr-TR"
        self.voice_name     =   "tr-TR-Wavenet-B"
    
    def textToSpeech(self):
    
        credentials     =   service_account.Credentials.from_service_account_file('WRITE-HERE') # We are adding the API file we received from google cloud here
    
        client          =   texttospeech.TextToSpeechClient(credentials=credentials)
    
        synthesis_input =   texttospeech.SynthesisInput(text=self.input_text)

        voice = texttospeech.VoiceSelectionParams(
            language_code   =   self.language_code,
            name            =   self.voice_name,
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding  =   texttospeech.AudioEncoding.LINEAR16
        )

        response = client.synthesize_speech(
            input           =   synthesis_input,
            voice           =   voice,
            audio_config    =   audio_config
        )

        with open(self.output_file, 'wb') as file:
            file.write(response.audio_content)


