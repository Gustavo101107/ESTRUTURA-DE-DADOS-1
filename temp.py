
class FilaVIP:
    def __init__(self):
        self.LEN = 8
        self.arrayList = [None] * self.LEN
        self.insertPosition = 0

    def insert(self, data, position):

        if position < 0 or position > self.insertPosition:
            print("Posição inválida")
            return

        if self.isMemoryFull():
            self.increaseMemory()

        for i in range(self.insertPosition, position, -1):
            self.arrayList[i] = self.arrayList[i - 1]

        self.arrayList[position] = data
        self.insertPosition += 1

    def remove(self):

        if self.isEmpty():
            print("Fila vazia")
            return None

        cliente = self.arrayList[0]

        for i in range(self.insertPosition - 1):
            self.arrayList[i] = self.arrayList[i + 1]

        self.arrayList[self.insertPosition - 1] = None
        self.insertPosition -= 1

        return cliente

    def isEmpty(self):
        return self.insertPosition == 0

    def isMemoryFull(self):
        return self.insertPosition == len(self.arrayList)

    def increaseMemory(self):
        newArray = [None] * (2 * len(self.arrayList))

        for i in range(len(self.arrayList)):
            newArray[i] = self.arrayList[i]

        self.arrayList = newArray

    def print(self):

        if self.isEmpty():
            print("\nFila vazia")
            return

        print("\n--- FILA DO EVENTO ---")

        for position in range(self.insertPosition):
            print(position + 1, "-", self.arrayList[position])


fila = FilaVIP()

while True:

    print("\n EVENTO ")
    print("1 - Cadastrar pessoa")
    print("2 - Ver tipo de ingresso")
    print("3 - Chamar próximo")
    print("4 - Mostrar fila")
    print("5 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        nome = input("Digite o nome da pessoa: ")

        print("\nEscolha o tipo de ingresso:")
        print("1 - VIP")
        print("2 - Camarote")
        print("3 - Lounge")
        print("4 - Pista")

        classe = input("Classe: ")

        if classe == "1":
            tipo = "VIP"
        elif classe == "2":
            tipo = "Camarote"
        elif classe == "3":
            tipo = "Lounge"
        elif classe == "4":
            tipo = "Pista"
        else:
            print("Classe inválida")
            continue

        pessoa = nome + " - " + tipo

        if tipo == "VIP":

            posicao = 0

        elif tipo == "Camarote":

            posicao = 0

            for i in range(fila.insertPosition):
                tipo_cadastrado = fila.arrayList[i].split(" - ")[1]

                if tipo_cadastrado == "VIP":
                    posicao += 1

        elif tipo == "Lounge":

            posicao = 0

            for i in range(fila.insertPosition):
                tipo_cadastrado = fila.arrayList[i].split(" - ")[1]

                if tipo_cadastrado == "VIP" or tipo_cadastrado == "Camarote":
                    posicao += 1

        else:

            posicao = fila.insertPosition

        fila.insert(pessoa, posicao)

        print(nome, "foi cadastrado como", tipo)

    elif opcao == "2":

        nome = input("Digite o nome da pessoa: ")

        encontrou = False

        for i in range(fila.insertPosition):

            pessoa = fila.arrayList[i]

            nome_cadastrado = pessoa.split(" - ")[0]
            classe_cadastrada = pessoa.split(" - ")[1]

            if nome.lower() == nome_cadastrado.lower():

                print("\nPessoa:", nome_cadastrado)
                print("Classe:", classe_cadastrada)

                encontrou = True
                break

        if not encontrou:
            print("Pessoa não encontrada.")

    elif opcao == "3":

        cliente = fila.remove()

        if cliente is not None:
            print("\nPróximo:", cliente)

    elif opcao == "4":

        fila.print()

    elif opcao == "5":

        resposta = input("\nDeseja mostrar a lista final? (s/n): ")

        if resposta.lower() == "s":
            fila.print()

        print("\nPrograma encerrado.")
        break

    else:

        print("Opção inválida.")



