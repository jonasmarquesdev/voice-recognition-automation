# voice-recognition-automation

![Logo](https://firebasestorage.googleapis.com/v0/b/storage-1cbb2.appspot.com/o/Minimalist-BannerV2.png?alt=media&token=27299998-acf5-4edb-a34b-862622bf4718)

## Descrição
Automação com reconhecimento de voz em Python utilizando as bibliotecas pyttsx3, subprocess, pyaudio e speech_recognition envolve a criação de um programa que permite a interação com o computador por meio de comandos de voz.

## Instalação
Certifique-se de ter o Python instalado em seu sistema. Você pode verificar digitando o seguinte comando no prompt de comando ou terminal:

### `python --version`

Certifique-se de ter uma versão igual ou superior à 3.6.

## Instalação do SpeechRecognition
Para instalar a biblioteca SpeechRecognition, execute o seguinte comando no prompt de comando ou terminal:

### `pip install SpeechRecognition`

Isso instalará a biblioteca SpeechRecognition em seu ambiente Python.

## Instalação do PyAudio
A biblioteca PyAudio requer algumas dependências extras para funcionar corretamente. Siga as instruções abaixo com base no seu sistema operacional:

## Windows
* Instale o Visual Studio C++ Build Tools. Você pode baixá-lo no site oficial da Microsoft.
* Em seguida, instale o PyAudio executando o seguinte comando:

### `pip install PyAudio`

## macOS
* Instale o PortAudio usando o Homebrew, um gerenciador de pacotes para macOS. Se você ainda não tem o Homebrew, você pode instalá-lo executando o seguinte comando:

### `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

* Em seguida, instale o PortAudio com o seguinte comando:

### `brew install portaudio`
* Agora você pode instalar o PyAudio executando o seguinte comando:

### `pip install PyAudio`

## Linux (Debian/Ubuntu)
* Execute o seguinte comando para instalar o PortAudio:

## arduino

### `sudo apt-get install portaudio19-dev`

* Em seguida, você pode instalar o PyAudio com o seguinte comando:

### `pip install PyAudio`

### Após seguir essas etapas, você terá o SpeechRecognition e o PyAudio instalados em seu ambiente Python e poderá usá-los em seus projetos. Certifique-se de importar as bibliotecas corretamente em seus scripts para utilizá-las.
