from Carro import Carro
class Locadora():
    def __init__(self):
        self.lista = []

    def CadastroCarros(self):
        carro = Carro()
        verificacao = 0
        while verificacao != 5:
            placa = input("Digite a placa do carro que será cadastrada: ")
            if len(placa) > 6:
                verificacao +=1
                carro.placa = placa
            else:
                print("Formato de placa inválida!")
                break
            carro.marca = input("Digite a marca: ")
            carro.modelo = input("Digite o modelo: ")
            carro.ano = int(input("Digite o ano: "))
            carro.codigo = int(input("Digite o código: "))
            print("Carro cadastrado!")
            break
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
            print("Carro removido com sucesso!")

    def imprime_carro(self):
        if self.lista_vazia():
            print("A lista está vazia!")
        else:
            placa = input("Digite a placa do carro que será consultado: ")
            for carro in self.lista:
                if carro.placa == placa:
                    print("Placa: ", carro.placa)
                    print("Modelo: ", carro.modelo)
                    print("Ano: ", carro.ano)
                    print("Código: ", carro.codigo)
                    print("Marca: ", carro.marca)
