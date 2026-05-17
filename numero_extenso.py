lista_unidade = [
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove"
]
lista_dezena = [
    "",
    "dez",
    "vinte",
    "trinta",
    "quarenta",
    "cinquenta",
    "sessenta",
    "setenta",
    "oitenta",
    "noventa"
]
lista_onze_dezenove = [
    ""
    "onze",
    "doze",
    "treze",
    "quatorze",
    "quinze",
    "dezesseis",
    "dezessete",
    "dezoito",
    "dezenove"
]
lista_centena = [
    "",
    "cento",
    "duzentos",
    "trezentos",
    "quatrocentos",
    "quinhentos",
    "seiscentos",
    "setecentos",
    "oitocentos",
    "novecentos"
]
lista_milhar = [
    "",
    "mil",
    "dois mil",
    "três mil",
    "quatro mil",
    "cinco mil",
    "seis mil",
    "sete mil",
    "oito mil",
    "nove mil"
]

num = int(input("Digite um número: "))

digitos = str(num)

if len(digitos) == 1:
    print(lista_unidade[num])

elif len(digitos) == 2:
    if digitos[0] == "0":
        print({lista_unidade[int(digitos[1])]})
    elif num > 10 and num < 20:
        print(lista_onze_dezenove[num - 11])
    elif lista_unidade[int(digitos[1])] == "zero":
        print(lista_dezena[int(digitos[0])])
    else:
        print(f"{lista_dezena[int(digitos[0])]} e {lista_unidade[int(digitos[1])]}")

elif len(digitos) == 3:
    if digitos[0] == "0":
        print(f"{lista_dezena[int(digitos[0])]} e {lista_unidade[int(digitos[0])]}")
    elif digitos[0:2] == "00":
        print({lista_unidade[int(digitos[1])]})
    elif 11 <= int(digitos[1:]) <= 19:
        print(f"{lista_centena[int(digitos[0])]} e {lista_onze_dezenove[int(digitos[2])]}")
    elif num == 100:
        print("Cem")
    elif digitos[1] == "0":
        print(f"{lista_centena[int(digitos[0])]} e {lista_unidade[int(digitos[2])]}")
    elif digitos[2] == "0":
        print(f"{lista_centena[int(digitos[0])]} e {lista_dezena[int(digitos[1])]}")
    else:
        print(f"{lista_centena[int(digitos[0])]} e {lista_dezena[int(digitos[1])]} e {lista_unidade[int(digitos[2])]}")

elif len(digitos) == 4:
    if digitos[0] == "0":
        print(f"{lista_centena[int(digitos[0])]} e {lista_dezena[int(digitos[1])]} e {lista_unidade[int(digitos[2])]}")
    elif digitos[0:2] == "00":
        print(f"{lista_dezena[int(digitos[0])]} e {lista_unidade[int(digitos[0])]}")
    elif digitos[0:3] == "000":
        print({lista_unidade[int(digitos[1])]})
    elif digitos[1:] == "000":
        print(lista_milhar[int(digitos[0])])
    elif 11 <= int(digitos[2:]) <= 19:
        print(f"{lista_milhar[int(digitos[0])]} e {lista_centena[int(digitos[1])]} e {lista_onze_dezenove[int(digitos[2])]}")
    elif digitos[1:4] == "100":
        print(f"{lista_milhar[int(digitos[0])]} e cem")
    elif digitos[2:4] == "00":
        print(f"{lista_milhar[int(digitos[0])]} e {lista_centena[int(digitos[1])]}")
    elif digitos[3:4] == "0":
        print(f"{lista_milhar[int(digitos[0])]} {lista_centena[int(digitos[1])]} e {lista_dezena[int(digitos[2])]}")
    else:
        print(f"{lista_milhar[int(digitos[0])]} {lista_centena[int(digitos[1])]} e {lista_dezena[int(digitos[2])]} e {lista_unidade[int(digitos[3])]}")