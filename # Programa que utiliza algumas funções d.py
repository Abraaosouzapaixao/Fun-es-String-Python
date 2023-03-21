# Programa que utiliza algumas funções de string em Python

while True:
    # Solicita que o usuário insira um texto
    texto = input("Digite um texto: ")

    # Transforma a string em minúsculas
    texto = texto.casefold()
    print("Casefold:", texto)

    # Conta quantas vezes uma substring aparece na string
    ocorrencias = texto.count("o")
    print("Count:", ocorrencias)

    # Encontra a posição da primeira ocorrência de uma substring
    posicao = texto.find("python")
    print("Find:", posicao)

    # Formata uma string com valores variáveis
    nome = "Maria"
    idade = 30
    frase = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
    print("Format:", frase)

    # Verifica se a string contém apenas caracteres alfanuméricos
    alfanumerico = texto.isalnum()
    print("Isalnum:", alfanumerico)

    # Verifica se a string contém apenas caracteres alfabéticos
    alfabetico = texto.isalpha()
    print("Isalpha:", alfabetico)

    # Verifica se a string contém apenas caracteres numéricos
    numerico = texto.isnumeric()
    print("Isnumeric:", numerico)

    # Substitui uma substring por outra
    novo_texto = texto.replace("mundo", "planeta")
    print("Replace:", novo_texto)

    # Separa a string em uma lista de substrings com base em um delimitador
    palavras = texto.split(" ")
    print("Split:", palavras)

    # Separa a string em uma lista de substrings com base em quebras de linha
    linhas = texto.splitlines()
    print("Splitlines:", linhas)

    # Verifica se a string começa com uma determinada substring
    comeca_com = texto.startswith("olá")
    print("Startswith:", comeca_com)

    # Remove caracteres de espaço em branco no início e no final da string
    texto_sem_espaco = texto.strip()
    print("Strip:", texto_sem_espaco)

    # Transforma a string em título (primeira letra de cada palavra em maiúscula)
    titulo = texto.title()
    print("Title:", titulo)

    # Transforma a string em maiúsculas
    maiuscula = texto.upper()
    print("Upper:", maiuscula)

    # Pergunta ao usuário se ele deseja continuar
    opcao = input("Deseja continuar? (s/n) ")
    if opcao.lower() == "n":
        break
