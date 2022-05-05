import random
import os
import PySimpleGUI as sg
from interface import *


Palavra_S = ["OI", "TCHAU", "QUEIJO", "NOME", "PAO", "MANGA", "JUMENTO", "BOLA", "FORCA", "MAÇA", "ARANHA", "MARCELINHO", "VASCO", "FLAMENGO", "FLUMINESE"]
Palavra_Secretas = random.choice(Palavra_S)

Letras_Digitadas = []
Chances = 10

janela = Jogodaforca()

while True:

    window, events, values = sg.read_all_windows()
    if window == janela and events == sg.WIN_CLOSED:
        break

    if window == janela and events == 'ok':
        Letra = values['Letra'].upper()

        if len(Letra) > 1:
            window['msg'].update("Não Pode Digitar mais de uma Letra")
            continue

        Letras_Digitadas.append(Letra)

        Palavra = ''
        for Letra_secreta in Palavra_Secretas:
            if Letra_secreta in Letras_Digitadas:
                Palavra += Letra_secreta
            else:
                Palavra += '_'
        
        
        if Palavra == Palavra_Secretas:
            sg.popup('Você Venceu a Forca')
            window['msg'].update("Você Venceu a Forca")
            break
        else:
            window['pal'].update(f'A Palavra Secreta está assim: {Palavra}')
        
        if Letra not in Palavra_Secretas:
            Chances -= 1
        
        if Chances <= 0:
            sg.popup(f"Você Perdeu!! A palavra secreta era {Palavra_Secretas}")
            break

        window['pal'].update(f'Letras:{Letras_Digitadas}')
        window['chance'].update(f'{Chances}')
        window['palavra'].update(f'Forca: {Palavra}')
    