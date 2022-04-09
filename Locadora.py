from Carro import Carro
class Locadora():
    def __init__(self):
        self.lista = []

    def CadastroCarros(self):
        carro = Carro()

        placa = input("Digite a placa do carro que será cadastrada: ")

        if len(placa) == 7 and placa[:3].isalpha() and placa[3:7].isnumeric():
            carro.placa = placa
            carro.marca = input("Digite a marca: ")
            carro.modelo = input("Digite o modelo: ")
            carro.ano = input("Digite o ano: ")
            carro.codigo = int(input("Digite o código: "))
            print("Carro cadastrado!")
            self.lista.append(carro)
        else:
            print("Formato de placa inválida!")


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
            print("Carro removido com sucesso!")

    def imprime_carro(self):
        if self.lista_vazia():
            print("A lista está vazia!")
        else:
            placa = input("Digite a placa do carro que será consultado: ")
            for carro in self.lista:
                if carro.placa == placa:
                    print("Placa do veículo: ", carro.placa)
                    print("Modelo do veículo: ", carro.modelo)
                    print("Ano de fabricação: ", carro.ano)
                    print("Código do veículo: ", carro.codigo)
                    print("Marca do veículo: ", carro.marca)
                    print("último algarismo da placa: ", carro.placa[-1])
