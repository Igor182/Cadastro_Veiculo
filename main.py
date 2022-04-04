#Um programa que vai gerenciar um cadastro de veículos como uma lista na mémoria do computador.
#Usar os tipos de estruturas de dados com veículo e explorar os recursos de listas em python
#Operações do programa >> Inserir um veículo na lista
#   Remover um veículo da lista]
#   Remover um veículo da lista, dada a placa deste (executar a operação somente se a lista não estiver vazia e se a placa de fato existir)
#   Consultar cadastro >>> Dada a placa do veículo, se ela existir, mostrar todos os dados do veículo
#   Se for dado apenas um inteiro de 0 a 9, o programa escreverá todos os dados dos veículos cujos finais de placa sejam o tal número


#Atributos -TAD
#- placa (string composta de 7 dígitos sendo três letras seguidas de quatro números),
#- marca (String que identifica o fabricante),
#- modelo (string com o nome do modelo dado pelo fabricante),
#- ano (ano de fabricação – uma string),
#- cod (código do proprietário – um número inteiro).
#Interface:
#- imprimeVeiculo() - Escreve os dados do Veiculo na saída padrão
#- imprimeFinalPlaca() - Retorna o algarismo final da placa deste veículo.

class CarrosCadastro():
    def __init__(self, placa, marca, modelo, ano, cpf):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cpf = cpf

    #def __init__(self, cadastrar, remover, consultar):
        #self.cadastrar = cadastrar
        #self.remover = remover
        #self.consultar = consultar


print('Bem-vindo ao nosso cadastramento de veículos!')
print(''' MENU:

        [1] - Cadastrar novo veículo
        [2] - Remover um veículo
        [3] - Consultar cadastro
        [4] - sair
    ''')

x = int(input('Escolha uma opção: \n'))
if x == 1:
        placa = int(input('Qual a placa do veículo'))
        marca = str(input('Qual a marca do veículo'))
        modelo = str(input('Qual o modelo do veículo'))
        ano = int(input('Qual o ano do veículo'))
        cpf = int(input('Qual o CPF do dono'))

carroscadastro = CarrosCadastro(placa,marca,modelo,ano,cpf)
print('Placa:', carroscadastro.placa)
print('Marca:', carroscadastro.marca)
print('Modelo:',carroscadastro.modelo)
print('Ano:',carroscadastro.ano)
print('CPF:',carroscadastro.cpf)
