"""
"""
from os import  system
from time import sleep
from other import Bot
from selenium import webdriver
from prettytable import PrettyTable

def traco() -> None:
    print(45*"=")

def primeiro_executar(bot, op) -> None:
    bot.clicar_jogo(op)
    sleep(2)
    bot.clicar_time()
    sleep(2)
    bot.escrever_valor_aposta()
    bot.apostar()
    sleep(2)
    bot.concluir_aposta()
    sleep(2)
    bot.minhas_apostas()
    sleep(2)
    bot.encerra_aposta()
    sleep(2)
    bot.voltar_minhas_apostas()

def mostrar_jogos(jogos: webdriver.Firefox) -> None:
    x = PrettyTable()
    lista_jogos = []
    for jogo in jogos:
        lista_jogos.append(jogo.text)
    x.field_names = ["opções", "jogos"]
    for i in range(len(lista_jogos)):
        x.add_row([str(i), lista_jogos[i]])
    x.add_row(["99", "digite 'q' para sair"])
    print(x)

def loguin(BOT: Bot) -> None:
    cont = 0
    while True:
        cont += 1
        try:
            BOT.clica_botao_login()
            break
        except:
            print("\033[1;32mAguarde um pouco...\033[0;0m")
        if cont == 7:
            break
    if cont == 7:
        print("\033[1;33mAlgo deu errado, por favor tente novamente\033[0;0m")
        sleep(3)
        principal()
    cont = 0
    while True:
        cont += 1
        try:
            BOT.escrever_dados()
            BOT.fazer_login()
            break
        except:
            print("\033[1;32mAguarde um pouco...\033[0;0m")
        if cont == 4:
            break
    if cont == 4:
        print("\033[1;33mAlgo deu errado, por favor tente novamente\033[0;0m")
        sleep(3)
        principal()

def painel() -> None:
    system("cls")
    titulo = "\033[1;32mBOT-BET365\033[0;0m"
    traco()
    print(titulo.center(57))
    traco()
    
def painel_principal() -> dict:
    system("cls")
    titulo = "\033[1;32mBOT-BET365\033[0;0m"
    traco()
    print(titulo.center(57))
    traco()
    usuario = input("\033[1;32mInforme o Usuario:\033[0;0m\n\033[1;33m>>> \033[0;0m").strip()
    senha = input("\033[1;32mInforme sua senha:\033[0;0m\n\033[1;33m>>> \033[0;0m").strip()
    time = input("\033[1;32mInforme o time que deseja apostar:\033[0;0m\n\033[1;33m>>> \033[0;0m").strip().title()
    while True:
        try:
            valor = float(input("\033[1;32mInforme o valor da aposta:\033[0;0m\n\033[1;33m>>> \033[0;0m"))
            break
        except ValueError:
            print("\033[1;91mTente adicionar um numero\033[0;0m")
    valor = str(valor)
    while True:
        try:
            vezes = int(input("\033[1;32mInforme quantas vezes deseja apostar:\033[0;0m\n\033[1;33m>>> \033[0;0m"))
            break
        except ValueError:
            print("\033[0;0mTente adicionar um numero\033[0;0m")
    dados = {"usuario":usuario, "senha":senha, "time":time, "valor":valor, "vezes":vezes}
    return dados

def principal() -> None:
    dados = painel_principal()
    usuario = dados["usuario"]
    senha = dados["senha"]
    time = dados["time"]
    vezes = dados["vezes"]
    valor = dados["valor"]
    bot = Bot(usuario, senha, time, valor)
    bot.iniciar()
    sleep(2)
    bot.abrir_url()
    sleep(2)
    painel()
    print("\033[1;36m>>>O BOT está analizando o site para fazer o login <<<\033[0;0m")
    loguin(bot)
    painel()
    print("\033[1;32mPor favor, feche todas as caixas de alerta, exemplo:\033[0;0m\n\033[1;36m    - atualização de email\n    - verificação de identidade\n    - novas menagens\033[0;0m")
    print("\n\033[1;32mDepois que que fechar tudo pode continuar. Ou, pressione 'x' para reinscrecrer os dados\033[0;0m")
    x = input("\033[1;33m>>> \033[0;0m").upper()
    if x == "X":
        bot.fechar()
        principal()
    painel()
    print("\033[1;32m>>> Fazendo a pesquisa do time<<< \033[0;0m")
    very = bot.tela_cheia()
    count = 0
    while True:
        count += 1
        try:
            bot.menu_clica()
            sleep(1)
            bot.pesquisar_menu()
            break
        except:
            ...
        if count == 3:
            break
    count = 0
    while True:
        count += 1
        try:
            bot.pesquisar()
            break
        except:
            ...
        if count == 3:
            break
    sleep(1)
    jogos = bot.capturar_jogos()
    painel()
    print("\033[1;32mTabela de opções de jogos, digit o valor que quer escolher\033[0;0m\033[1;33m")
    mostrar_jogos(jogos)
    op = int(input(">>> \033[0;0m"))
    sleep(2)
    if vezes > 1:
        for i in range(0, vezes+1):
            if i == 0:
                bot.clicar_jogo(op)
                sleep(2)
                bot.clicar_time()
                sleep(2)
                bot.escrever_valor_aposta()
                bot.apostar()
                sleep(2)
                bot.concluir_aposta()
                sleep(2)
                bot.minhas_apostas()
                sleep(2)
                bot.encerra_aposta()
                sleep(2)
                bot.voltar_minhas_apostas()
            else:
                sleep(2)
                bot.clicar_time()
                sleep(2)
                bot.escrever_valor_aposta()
                bot.apostar()
                sleep(2)
                bot.concluir_aposta()
                sleep(2)
                bot.minhas_apostas()
                sleep(2)
                bot.encerra_aposta()
                sleep(2)
                bot.voltar_minhas_apostas()
    else:
        primeiro_executar(bot, op)

    bot.fechar()
    exit()
    
if __name__ == '__main__':
    principal()