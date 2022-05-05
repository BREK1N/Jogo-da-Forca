import PySimpleGUI as sg


def Jogodaforca():
    layout = [
        [sg.Text('Chances:'), sg.Text('', key="chance")],
        [sg.Text(" ", key='pal')],
        [sg.Text(" ", key='palavra')],
        [sg.Text("Letra:")],
        [sg.Input(key="Letra")],
        [sg.Text(" ", key='msg')],
        [sg.Button("Enviar", key='ok')]

    ]
    return sg.Window('Jogo da forca', layout=layout, finalize=True)

