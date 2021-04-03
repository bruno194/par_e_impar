import PySimpleGUI as sg
sg.theme('Material2')
def principal():
    layout = [
        [sg.Text('-- PAR OU IMPAR --')],
        [sg.Text('digite um numero'), sg.Input(key='pergunta')],
        [sg.Button('ver'), sg.Button('sair')],
        [sg.Text(size=(40,20), key='texto')],
    ]
    janela = sg.Window('ola').layout(layout)
    while True:
        event, value = janela.read()
        try:
            if event == sg.WINDOW_CLOSED or event == 'sair':
                break
            if event == 'ver':
                alo = int(value['pergunta'])
                if alo % 2 == 0:
                    janela['texto'].update(f'o numero {alo} é par')
                else:
                    janela['texto'].update(f'o numero {alo} é impar')
        except:
            janela['texto'].update('erro')


principal()