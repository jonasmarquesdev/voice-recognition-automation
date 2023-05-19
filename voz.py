import pyttsx3

def configurar_voz(engine):
    # Obtém a lista de vozes disponíveis
    voices = engine.getProperty('voices')

    # Percorre as vozes e encontra uma voz mais humana (se disponível)
    for voice in voices:
        if 'pt' in voice.languages:
            if 'feminino' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
    # Configura outras propriedades da voz, se necessário
    engine.setProperty('rate', 150) # Velocidade de fala (padrão é 200)
    engine.setProperty('volume', 0.8) # Volume da voz (padrão é 1.0)
    
def say(frase):
    engine = pyttsx3.init()
    configurar_voz(engine)
    engine.say(frase)
    engine.runAndWait()

# Mensagem inicial
frase = "Olá, eu sou uma Automação com reconhecimento de voz em Python"
print(frase); say(frase)