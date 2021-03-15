from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import authenticate


class lang_translator:
    
    _API_KEY=authenticate.api_key_for_translator
    URL=authenticate.URL_for_translator
    authenticator=IAMAuthenticator(_API_KEY)
    Lt=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
    Lt.set_service_url(URL)

    lang_conv_to=None
    lang_conv_from=None
    model_id=None


    def __init__(self,lang_con_to="English"):
        self.lang_conv_to=lang_con_to
        

    def code_to_lang(self,code):
        swicher={
            "ar":"Arabic",
            "bn":"Bengali",
            "zh":"Chinese (Simplified)",
            "zh-TW":"Chinese (Traditional)",
            "da":"Danish",
            "nl":"Dutch",
            "en":"English",
            "fr":"French",
            "de":"German",
            "el":"Greek",
            "gu":"Gujarati",
            "he":"Hebrew",
            "hi":"Hindi",
            "it":"Italian",
            "el":"Greek",
            "ja":"Japanese",
            "ur":"Urdu",
            "th":"Thai",
            "te":"Telugu",
            "te":"Tamil",
            "sv":"Swedish",
            "ed":"Spanish",
            "ru":"Russian",
            "pt":"Portuguese",
            "ne":"Nepali",
            "ko":"Korean",


        }
        return swicher.get(code,"Invalid")
    
    def lang_to_code(self,lang):
        swicher={
            "Arabic":"ar",
            "Bengali":"bn",
            "Chinese (Simplified)":"zh",
            "Chinese (Traditional)":"zh-TW",
            "Danish":"da",
            "Dutch":"nl",
            "English":"en",
            "French":"fr",
            "German":"de",
            "Greek":"el",
            "Gujarati":"gu",
            "Hebrew":"he",
            "Hindi":"hi",
            "Italian":"it",
         
            "Japanese":"ja",
            "Urdu":"ur",
            "Thai":"th",
            "Telugu":"te",
            "Tamil":"te",
            "Swedish":"sv",
            "Spanish":"ed",
            "Russian":"ru",
            "Portuguese":"pt",
            "Nepali":"ne",
            "Korean":"ko",


        }
        return swicher.get(lang,"Invalid")
    
    
    def identify_lang(self,text):
        identify_language=self.Lt.identify(text).get_result()
        # print(identify_language['translations'][0]['translation'])
        identify_lang_code=identify_language['languages'][0]['language']
        identify_lang=self.code_to_lang(identify_lang_code)
        # print(identify_lang)
        self.lang_conv_from=identify_lang

        
        return identify_lang

    def model_id_string(self,text):

        # print(self.identify_lang(text) ,self.lang_conv_to)
        string_convo=""

        if (self.identify_lang(text) == self.lang_conv_to):
            return "invalid"
        else:
            string_convo=f"{self.lang_to_code(self.identify_lang(text))}-{self.lang_to_code(self.lang_conv_to)}"

            # print(string_convo)
            return string_convo


        

       

    
    def translator(self,text):

        if (self.identify_lang(text) == self.lang_conv_to): return f"Langauge is already in {self.lang_conv_from}"

        # print(self.identify_lang(text) ,self.lang_conv_to)

        self.model_id=self.model_id_string(text)

        if (self.model_id == "invalid"):
            return "Having an issue"


        transalation=self.Lt.translate(text=text,model_id=self.model_id).get_result()
        translated_lang=transalation['translations'][0]['translation']

        # print(translated_lang)

        return translated_lang

        

    
    def test(self):
            pass




# lt=lang_translator(lang_con_to="Italian")
lt=lang_translator()

# text="Hello World"
text="ওহে বিশ্ব"
# text="Ciao mondo"
# text="Olá Mundo"
print(lt.translator(text))
# print(lt.identify_lang(text))