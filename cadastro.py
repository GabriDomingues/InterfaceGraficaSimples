from PySimpleGUI import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('Default1')
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(40,0), key='nome')],
            [sg.Text('E-mail', size=(5, 0)), sg.Input(size=(40, 0), key='email')],
            [sg.Text('CPF', size=(5, 0)), sg.Input(size=(25, 0), key='cpf')],
            [sg.Text('Provedores aceitos')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('hotmail', key='hotmail')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartões', key='aceitaCartao'), sg.Radio('Não', 'cartões', key='naoAceitaCartao')],
            [sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(15,20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(50, 10))]
        ]
        #janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        #extrair dados da tela


    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            cpf = self.values['cpf']
            email = self.values['email']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_hotmail = self.values['hotmail']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'email: {email}')
            print(f'cpf: {cpf}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita hotmail: {aceita_hotmail}')
            print(f'Aceita cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceita_cartao}')
            print(f'Velocidade Scripts: {velocidade_script}')


tela = TelaPython()
tela.Iniciar()