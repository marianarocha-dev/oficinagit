nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))


def verificar_rato(nome, nota):
    if (nome == "Mariana" or nome == "Joaquim") and nota >= 5:
        return True
    else:
        return False