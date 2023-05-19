import speech_recognition as sr
import pyaudio
from voz import say
import subprocess

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

            # Verifica se a palavra em (text) foi falada
            # Substitua "nome_do_programa" pelo nome ou caminho do programa que deseja abrir
            # subprocess.Popen(["nome_do_programa"])
            
            if "encerrar processo" in text.lower():
                say("Encerrando processo")
                break

            elif "abrir steam" in text.lower():
                say("Abrindo Steam")
                subprocess.Popen(["C:\Program Files (x86)\Steam\steam.exe"])

            elif "fechar steam" in text.lower():
                say("Fechando Steam")
                subprocess.Popen(["taskkill", "/F", "/IM", "steam.exe"])

            elif "abrir bloco de notas" in text.lower():
                say("Abrindo Bloco de notas")
                subprocess.Popen(["notepad.exe"])
            
            elif "fechar steam" in text.lower():
                say("Fechando Bloco de notas")
                subprocess.Popen(["taskkill", "/F", "/IM", "notepad.exe"])

        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio.")
        except sr.RequestError as e:
            print("Erro na solicitação ao serviço de reconhecimento de voz: {0}".format(e))

if __name__ == '__main__':
    main()