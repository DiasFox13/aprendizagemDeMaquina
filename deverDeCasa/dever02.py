def verificar_entrada(frase):
    if not frase.strip():
        raise ValueError("A entrada não pode estar vazia.")
    return frase

def contar_caracteres(frase):
    return len(frase)

def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

def encontrar_maior_palavra(frase):
    palavras = frase.split()
    return max(palavras, key=len)

def inverter_frase_caracteres(frase):
    return frase[::-1]

def inverter_frase_palavras(frase):
    palavras = frase.split()
    return ' '.join(palavras[::-1])

def converter_maiusculas(frase):
    return frase.upper()

def converter_minusculas(frase):
    return frase.lower()

def criar_tupla_palavras(frase):
    return tuple(frase.split())

# Entrada do usuário
try:
    frase = input("Digite uma frase: ")
    frase = verificar_entrada(frase)
except ValueError as e:
    print(e)
    exit()

# Análise da frase
num_caracteres = contar_caracteres(frase)
num_palavras = contar_palavras(frase)
maior_palavra = encontrar_maior_palavra(frase)

# Manipulação e formatação
frase_invertida_caracteres = inverter_frase_caracteres(frase)
frase_invertida_palavras = inverter_frase_palavras(frase)
frase_maiusculas = converter_maiusculas(frase)
frase_minusculas = converter_minusculas(frase)
tupla_palavras = criar_tupla_palavras(frase)

# Saída formatada
print(f"""
Número de caracteres da frase: {num_caracteres}
Número de palavras: {num_palavras}
A palavra com maior comprimento: {maior_palavra}
Frase invertida (por caracteres): {frase_invertida_caracteres}
Frase invertida (por palavras): {frase_invertida_palavras}
Frase em maiúsculas: {frase_maiusculas}
Frase em minúsculas: {frase_minusculas}
Tupla formada pelas palavras da frase: {tupla_palavras}
""")