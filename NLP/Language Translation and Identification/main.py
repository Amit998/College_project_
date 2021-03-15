import authenticate


API_KEY=authenticate.api_key_for_translator
URL=authenticate.URL_for_translator

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator=IAMAuthenticator(API_KEY)
Lt=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

Lt.set_service_url(URL)



# # Translate Language
# transalation=Lt.translate(text='Hello World',model_id='en-bn').get_result()
# transalation=Lt.translate(text='Hello World',model_id='en-ga').get_result()


# # print(transalation)

# print(transalation['translations'][0]['translation'])



#identify The language


identify_language=Lt.identify("Hello an Domhan").get_result()

# print(identify_language)

#AI TRAVEL GUIDE

TTS_API_KEY=authenticate.api_key_for_text_to_speech
TTS_URL=authenticate.URL_for_text_to_speech

from ibm_watson import TextToSpeechV1


tts_authenticator=IAMAuthenticator(TTS_API_KEY)
tts=TextToSpeechV1(authenticator=tts_authenticator)

tts.set_service_url(TTS_URL)



# transalation=Lt.translate(text='Hello I Am Amit Please Help Me',model_id='en-de').get_result()
transalation=Lt.translate(text='Hallo Ich Bin Amit Bitte Helfen Sie Mir',model_id='de-en').get_result()


# print(transalation['translations'][0]['translation'])

text=transalation['translations'][0]['translation']

# print(text)

with open('./help.mp3','wb') as audio_file:
    res=tts.synthesize(text,accept='audio/mp3',voice='ar-MS_OmarVoice').get_result()
    audio_file.write(res.content)