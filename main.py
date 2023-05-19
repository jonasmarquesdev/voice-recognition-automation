import speech_recognition as sr
import pyaudio
from voz import say

def main():
    r = sr.Recognizer()
    mic = sr.Microphone()

    say("Diga algo...")
    while True:
        try:
            with mic as source:
                print("Diga algo...")
                audio = r.listen(source)

            text = r.recognize_google(audio, language="pt-BR")
            print("Você disse:", text)

        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio.")
        except sr.RequestError as e:
            print("Erro na solicitação ao serviço de reconhecimento de voz: {0}".format(e))

if __name__ == '__main__':
    main()