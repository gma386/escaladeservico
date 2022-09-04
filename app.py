import PySimpleGUI as sg 

def front():
    layout = [
        [sg.Text('Usuário')],
        [sg.Input(key='-USUARIO-')],
        [sg.Text('Senha')],
        [sg.Input(key='-SENHA-')],
        [sg.Button('Login'), sg.Button('Cadastrar')],
    ]

    window = sg.Window('Escala de Serviço - Login',layout)

    while True:

        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'login':
            usuario = values['usuario']
            senha = values['senha']
            #função de conectar e depois fechar a janela de login
            window.close()
        else: #event == 'cadastrar':
            window.close()

layout = [
    [sg.Button('escala')],
    [sg.Button('cadastrar militar')],
    [sg.Button('situação militar')],
]

front()

window = sg.Window('Main', layout)
event, values = window.read()