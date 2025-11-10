import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import azure.cognitiveservices.speech as speech_sdk

speech_config = None

def main(): 
    global speech_config
    try: 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_deployment = os.getenv("AZURE_OAI_DEPLOYMENT")
        speech_key = os.getenv("AZURE_SPEECH_KEY")
        speech_region = os.getenv("AZURE_SPEECH_REGION")
        
        client = AzureOpenAI(
            azure_endpoint=azure_oai_endpoint, 
            api_key=azure_oai_key, 
            api_version="2024-02-15-preview"
        )
        
        system_message = """Eu sou um assistente de IA prestativo.
        Eu respondo perguntas de forma concisa e direta."""
        
        messages_array = [{"role": "system", "content": system_message}]

        print("--- Chatbot IA Iniciado (fale 'sair' para sair) ---")

        while True:
            speech_config = speech_sdk.SpeechConfig(speech_key, speech_region)
            
            speech_config.speech_recognition_language = "pt-BR"
            
            print("Serviço de reconhecimento de fala pronto.")

            print("Testando a função de ouvir... Fale algo!")
            
            texto_ouvido = ouvir_do_microfone()
            
            if texto_ouvido:
                print(f"\nLegal! O texto que eu ouvi e 'retornei' foi: '{texto_ouvido}'")
                if texto_ouvido.lower() == "sair":
                    break
            else:
                print("\nNão ouvi nada ou não entendi.")
            
            messages_array.append({"role": "user", "content": texto_ouvido})

            print("IA está pensando...")
            response = client.chat.completions.create(
                model=azure_oai_deployment,
                messages=messages_array
            )

            generated_text = response.choices[0].message.content

            messages_array.append({"role": "assistant", "content": generated_text})

            print("IA: " + generated_text + "\n")
            
           

    except Exception as ex:
        print(f"Ocorreu um erro: {ex}")


def ouvir_do_microfone():
    """
    Esta função escuta o microfone e retorna o que foi dito como uma string de texto.
    """
    global speech_config
    
    if not speech_config:
        print("Erro: A configuração de fala (speech_config) não foi inicializada.")
        return "" 
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

    print("Fale agora... (estou ouvindo)")

    speech = speech_recognizer.recognize_once_async().get()

    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        return speech.text
    elif speech.reason == speech_sdk.ResultReason.NoMatch:
        print("Não consegui entender o que você disse.")
    elif speech.reason == speech_sdk.ResultReason.Canceled:
        print("Reconhecimento cancelado.")
    else:
        print(f"Erro no reconhecimento: {speech.reason}")
        return ""

if __name__ == '__main__': 
    main()