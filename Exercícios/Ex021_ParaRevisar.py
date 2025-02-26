#storage/emulated/0/snaptube/download/SnapTube Audio/Myfauty.mp3

import pygame

# Inicializa o mixer de áudio
pygame.mixer.init()

# Carrega o arquivo de som (substitua "audio.mp3" pelo nome do seu arquivo)
pygame.mixer.music.load("Myfauty.mp3")

# Reproduz o som
pygame.mixer.music.play()

# Mantém o programa rodando até o áudio terminar
while pygame.mixer.music.get_busy():
    pass