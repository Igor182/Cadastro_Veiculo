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
    def __init__(self):
        self.placa = ""
        self.marca = ""
        self.modelo = ""
        self.ano = 0
        self.codigo = 0

    #def __init__(self, cadastrar, remover, consultar):
        #self.cadastrar = cadastrar
        #self.remover = remover
        #self.consultar = consultar

class ListaCarro():
    def __init__(self):
        self.lista = []

    def CadastroCarros(self):
        carro = CarrosCadastro()
        carro.placa = input("Digite a placa: ")
        carro.marca = input("Digite a marca: ")
        carro.modelo = input("Digite o modelo: ")
        carro.ano = int(input("Digite o ano: "))
        carro.codigo = int(input("Digite o código: "))
        self.lista.append(carro)

    def lista_vazia(self):
        return len(self.lista) == 0

    def remove_carro(self):
        if self.lista_vazia():
            print("A lista está vazia!")
        else:
            placa = input("Digite a placa do carro que será removida: ")
            for carro in self.lista:
                if carro.placa == placa:
                    self.lista.remove(carro)

    def imprime_carro(self):
        for carro in self.lista:
            print("PLaca... " , carro.placa)
            print("Modelo... ", carro.modelo)
            print("Ano... ", carro.ano)
            print("Código... ",carro.codigo)
            print("Marca... ",carro.marca)

carros = ListaCarro()
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
        carros.CadastroCarros()
    elif x == 2:
        carros.remove_carro()

    elif x == 3:
        carros.imprime_carro()