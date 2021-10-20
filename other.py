import pyautogui as auto
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class Usuario:
    def __init__(self: object, usuario: str, senha: str) -> None:
        self.__usuario: str = usuario
        self.__senha: str = senha

    @property
    def usuario(self: object) -> str:
        return self.__usuario

    @property
    def senha(self: object) -> str:
        return self.__senha

    @senha.setter
    def senha(self: object, nova_senha: str) -> None:
        self.__senha = nova_senha

    @usuario.setter
    def usuario(self: object, novo_usuario: str) -> None:
        self.__usuario = novo_usuario


class Bot(Usuario):

    def __init__(self, usuario: str = "usuario", senha: str = "senha", time: str = "final", valor: float = 1,
                 url: str = "https://www.bet365.com/#/HO/") -> None:
        super().__init__(usuario, senha)
        self.__driver: webdriver.Firefox = None
        self.time: str = time
        self.valor: str = valor
        self.url: str = url

    @property
    def drive(self: object) -> webdriver.Firefox:
        return self.__driver

    def find(self, *locator):
        element = WebDriverWait(self.__driver, 300).until(visibility_of_element_located(*locator))
        return element

    def iniciar(self: object) -> None:
        """Abre o navegador firefox"""
        self.__driver: webdriver.Firefox = webdriver.Firefox()
        self.__driver.delete_all_cookies()

    def abrir_url(self: object) -> None:
        """Abre a url do site"""
        self.__driver.get(self.url)

    def clica_botao_login(self: object) -> None:
        """
        clicar no botão que leva a tela de login
        """
        var = By.CLASS_NAME, "hm-MainHeaderRHSLoggedOutWide_Login "
        self.find(var)
        botao = self.__driver.find_element(By.CLASS_NAME, "hm-MainHeaderRHSLoggedOutWide_Login ")
        botao.click()

    def escrever_dados(self: object) -> None:
        """
        Procura os inputs da tela de login e escreve os dados
        do usuario
        """
        var = By.TAG_NAME, "input"
        self.find(var)
        element: webdriver.Firefox = self.__driver.find_elements(By.TAG_NAME, "input")
        for el in element:
            if el.get_attribute("placeholder") == "Usuário":
                el.send_keys(self.usuario)
                break
        for el in element:
            if el.get_attribute("placeholder") == "Senha":
                el.send_keys(self.senha)
                break

    def fazer_login(self: object) -> None:
        """Clica no botão que valida o login"""
        element: webdriver = self.__driver.find_element(By.CLASS_NAME, "lms-StandardLogin_LoginButton ")
        element.click()

    def menu_clica(self: object) -> None:
        """
        Procura butão de menu para acessar a barra de pesquisa
        Usado quando a tela está pequena e a barra de pesquisa se esconde no menu
        Clica no botão de menu
        """
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for el in element:
            if el.get_attribute("class") == "hm-MainHeaderLHSNarrow_AZIcon ":
                el.click()
                break

    def pesquisar_menu(self: object) -> None:
        """clica na caixa de pesquisa dentro do menu"""
        element = self.__driver.find_elements(By.TAG_NAME, "input")
        for el in element:
            if el.get_attribute("class") == "wn-SiteSearch_SearchInput ":
                el.click()
                break
        element = self.__driver.find_elements(By.TAG_NAME, "input")
        for el in element:
            if el.get_attribute("class") == "sml-SearchTextInput ":
                var = el
                break
        var.send_keys(self.time)

    def pesquisar(self: object) -> None:
        """Escreve na caixa de pesquisa o time escolhido"""
        var = By.CLASS_NAME, "hm-SiteSearchIconLoggedIn "
        self.find(var)
        ele = self.__driver.find_element(By.CLASS_NAME, "hm-SiteSearchIconLoggedIn ")
        ele.click()
        element = self.__driver.find_elements(By.TAG_NAME, "input")
        for el in element:
            if el.get_attribute("class") == "sml-SearchTextInput ":
                var = el
                break
        var.send_keys(self.time)

    def capturar_jogos(self: object) -> list:
        """Captura na tela os jogos referente a pesquisa e os retorna em uma lista de webdriver"""
        self.__driver.set_page_load_timeout(5)
        lista_jogos = list()
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for el in element:
            if el.get_attribute("class") == "ssm-SiteSearchLabelOnlyParticipant gl-Market_General-cn1 ":
                jogo = el.find_element(By.TAG_NAME, "span")
                lista_jogos.append(jogo)
        return lista_jogos

    def clicar_jogo(self: object, escolha: int) -> None:
        """- O parametro "escolha" deverá vir do usuario.
        - "escolha" será o indice que indicará o jogo escolhido
        """
        self.__driver.set_page_load_timeout(5)
        lista_jogos = list()
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for el in element:
            if el.get_attribute("class") == "ssm-SiteSearchLabelOnlyParticipant gl-Market_General-cn1 ":
                jogo = el.find_element(By.TAG_NAME, "span")
                lista_jogos.append(jogo)
        lista_jogos[escolha].click()

    def clicar_time(self: object) -> None:
        self.__driver.set_page_load_timeout(5)
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for elem in element:
            if elem.get_attribute("class") == "gl-MarketGroup ":
                elemento = elem
                break
        lista = elemento.find_elements(By.TAG_NAME, "div")
        for l in lista:
            if l.get_attribute("class") == "gl-Participant gl-Participant_General gl-Market_General-cn3 ":
                if self.time in l.text:
                    time_aposta = l
                    break
        time_aposta.click()

    def primeiro_escrever_valor_aposta(self: object) -> None:
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for elem in element:
            if elem.get_attribute("class") == "qbs-StakeBox_StakeInput ":
                butao_valor = elem
                break
        butao_valor.click()
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for elem in element:
            if elem.get_attribute("class") == "qbs-RememberStakeButtonNonTouch ":
                butao_valor = elem
                break
        butao_valor.click()
        janela_bot = auto.getWindowsWithTitle("bet365 - Apostas Desportivas Online - Mozilla Firefox")[0]
        try:
            janela_bot.restore()
            janela_bot.maximize()
            janela_bot.activate()
        except:
            ...
        auto.write(self.valor)

    def apostar(self: object) -> None:
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for elem in element:
            if elem.get_attribute("class") == "qbs-PlaceBetButton_Wrapper":
                elem.click()
                break

    def concluir_aposta(self: object) -> None:
        """Conclui a aposta"""
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for elem in element:
            if elem.get_attribute("class") == "qbs-NormalBetItem_Indicator ":
                elem.click()
                break

    def minhas_apostas(self: object) -> None:
        """Clica em minhas apostas"""
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for elem in element:
            if elem.get_attribute("class") == "hm-MainHeaderCentreWide_Link hm-HeaderMenuItemMyBets ":
                elem.click()
                break

    def encerra_aposta(self: object) -> None:
        """Encerra a primeira aposta encontrada"""
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for elem in element:
            if elem.get_attribute("class") == "myb-CloseBetButtonBase_WrapperInner ":
                if "Encerrar Aposta" in elem.text:
                    elem.click()
                    elem.click()
                    break

    def voltar_minhas_apostas(self: object) -> None:
        """aperta no botão voltar em minhas apostas"""
        self.__driver.back()

    def tela_cheia(self: object) -> bool:
        tela = auto.getWindowsWithTitle("bet365 - Apostas Desportivas Online - Mozilla Firefox")[0]
        very = tela.isMaximized
        return very

    def fechar(self: object) -> None:
        self.__driver.close()


if __name__ == '__main__':
    from time import sleep

    bot = Bot("Kele51", "3122477", "Flamengo", "5")
    bot.iniciar()
    sleep(2)
    bot.abrir_url()
    bot.clica_botao_login()
    bot.escrever_dados()
    bot.fazer_login()
    sleep(3)
    x = input("- ")
    # bot.menu_clica()
    sleep(2)
    # bot.pesquisar_menu()
    bot.pesquisar()
    sleep(2)
    jogos = bot.capturar_jogos()
    bot.clicar_jogo(2)
    sleep(2)
    bot.clicar_time()
    sleep(1)
    bot.escrever_valor_aposta()
    bot.apostar()
    sleep(1)
    bot.concluir_aposta()
    sleep(1)
    bot.minhas_apostas()
    sleep(2)
    bot.encerra_aposta()
    sleep(1)
    bot.voltar_minhas_apostas()