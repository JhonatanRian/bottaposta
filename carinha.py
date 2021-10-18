def funcao(numero):
    lista = []
    cont = 0
    for num in range(1, numero+1):
        cont += 1
        for i in range(1, cont+1):
            mult = i
        numero =  numero**mult
        print(numero)
        if cont == 3:
            cont = 0
        
while True:
    try:
        valor = int(input("quantidade de termos a ser somada: "))
    except:
        ...
    if valor > 0:
        resultado = funcao(valor)
        print(f"Resultado: {resultado}")