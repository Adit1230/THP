from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

file_path = "Project_Updates.txt" #Path to the file to be read

path = "C:\\Users\\aditp\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\TTS\\.models.json"
model_manager = ModelManager(path)

#Load the tts model
model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/tacotron2-DDC")
#Load vocoder
voc_path, voc_config_path, x = model_manager.download_model( model_item["default_vocoder"] )
#Create synthesiser object for converting text to speech
syn = Synthesizer(tts_checkpoint = model_path, tts_config_path = config_path, vocoder_checkpoint = voc_path, vocoder_config = voc_config_path)

#Open the file and read its contents
file = open(file_path, 'r')
text = file.read()
file.close()

#Convert the text into audio and save it
output = syn.tts(text)
syn.save_wav(output, "audio.wav")
