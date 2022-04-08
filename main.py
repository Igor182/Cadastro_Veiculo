from Locadora import Locadora

locadora = Locadora()

x = -1
while x != 4:
    print('Bem-vindo ao nosso cadastramento de veículos!')
    print(''' MENU:
           [1] - Cadastrar novo veículo
           [2] - Remover um veículo
           [3] - Consultar cadastro
           [4] - sair
       ''')

    x = int(input('Escolha uma opção: \n'))
    if x == 1:
        locadora.CadastroCarros()
    elif x == 2:
        locadora.remove_carro()

    elif x == 3:
        locadora.imprime_carro()
