import os
from time import sleep
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

def win_act(win_name):
    import win32gui
    import re

    class WindowMgr:
        """Encapsulates some calls to the winapi for window management"""

        def __init__(self):
            """Constructor"""
            self._handle = None

        def find_window(self, class_name, window_name=None):
            """find a window by its class_name"""
            self._handle = win32gui.FindWindow(class_name, window_name)

        def _window_enum_callback(self, hwnd, wildcard):
            """Pass to win32gui.EnumWindows() to check all the opened windows"""
            if re.match(wildcard,
                         str(win32gui.GetWindowText(hwnd))) is not None:
                self._handle = hwnd

        def find_window_wildcard(self, wildcard):
            """find a window whose title matches the wildcard regex"""
            self._handle = None
            win32gui.EnumWindows(self._window_enum_callback, wildcard)

        def set_foreground(self):
            """put the window in the foreground"""
            win32gui.SetForegroundWindow(self._handle)

    w = WindowMgr()
    for x in range(3):
        w.find_window_wildcard(f".*{win_name}*")
        w.set_foreground()

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
    
    url: str = "https://www.bet365.com/#/HO/"
        
    def __init__(self, usuario: str, senha: str, time: str, valor: str, vezes: int) -> None:
        super().__init__(usuario, senha)
        self.__driver: webdriver.Firefox = None
        self.time: str = time
        self.valor: str = valor
        self.vezes: int = vezes
    
    @classmethod
    def url(cls):
        return cls.url
        
    @property
    def drive(self: object) -> webdriver.Firefox:
        return self.__driver
    
    def time(self: object, novo_time: str) -> None:
        self.time = novo_time
        
    def valor(self: object, novo_valor) -> None:
        self.valor = novo_valor
        
    def vezes(self: object, mudar) -> None:
        self.vezes = mudar
        
    def _init(self: object) -> None:
        """Abre o navegador firefox"""
        self.__driver: webdriver.Firefox = webdriver.Firefox()
    
    def _init_url(self: object) -> None:
        """Abre a url do site"""
        self.__driver.get(self.url)
        self.__driver.set_page_load_timeout(15)
        
    def procura_botao_login(self: object) -> webdriver.Firefox:
        """
        Objetivo:
        - Procurar botão login
        - retorna um elemento da classe webdrive
        """
        sleep(2)
        element: webdriver.Firefox = self.__driver.find_elements(By.TAG_NAME, "div")
        for el in element:
            if el.text == "Login":
                var = el
                return var
    
    def clica_botao_login(self: object) -> None:
        """
        Usa o retorno da função "procura_botao_login" e
        clica no elemento que ela retorna
        """
        botão_para_login: webdriver.Firefox = self.procura_botao_login()
        botão_para_login.click()
    
    def escrever_dados(self: object) -> None:
        """
        Procura os inputs da tela de login e escreve os dados
        do usuario
        """
        element: webdriver.Firefox = self.__driver.find_elements(By.TAG_NAME ,"input")
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
        element: webdriver = self.__driver.find_element(By.CLASS_NAME ,"lms-StandardLogin_LoginButton ")
        element.click()
       
    def procurar_botao_menu(self: object) -> None:
        element: webdriver.Firefox = self.__driver.find_elements(By.TAG_NAME, "div")
        for el in element:
            if el.get_attribute("class") == "hm-MainHeaderMembersWide_MembersMenuIcon ":
                return el
       
    def menu_clica(self: object) -> None:
        menu: webdriver = self.procurar_botao_menu
        if menu:
            menu.click()
       
    def pesquisar_no_menu(self: object) -> None:
        element: webdriver.Firefox = self.__driver.find_elements(By.TAG_NAME, "div")
        for el in element:
            if el.get_attribute("class") == "wn-SiteSearch_SearchInput ":
                el.click()
                break
       
    def procurar_botao_pesquisar(self: object) -> webdriver.Firefox:
        """Procura o botão que abre a caixa de pesquisa e retorna um o elemento em objeto webdrive"""
        element: webdriver = self.__driver.find_elements(By.TAG_NAME, "div")
        for el in element:
            if el.get_attribute("class") == "hm-SiteSearchIconLoggedIn ":
                return el
        
    def clicar_botao_pesquisar(self: object) -> None:
        """Clica no botao de pesquisa"""
        botao_pesquisar: webdriver.Firefox = self.procurar_botao_pesquisar()
        botao_pesquisar.click()
        
    def procurar_caixa_pesquisa(self: object) -> webdriver.Firefox:
        """Procura a caixa que será inserido a pesquisa"""
        element = self.__driver.find_elements(By.TAG_NAME, "input")
        for el in element:
            if el.get_attribute("class") == "sml-SearchTextInput ":
                return el
        
    def pesquisa(self: object) -> None:
        """Escreve na caixa de pesquisa o time do objeto"""
        caixa_pesquisa: webdriver.Firefox = self.procurar_caixa_pesquisa()
        caixa_pesquisa.send_keys(self.time)
        
    def capturar_jogos(self: object) -> list:
        """Captura na tela os jogos referente a pesquisa e os retorna em uma lista"""
        lista_jogos: list = []
        element = self.__driver.find_elements(By.TAG_NAME, "div")
        for el in element:
            if el.get_attribute("class") == "ssm-SiteSearchLabelOnlyParticipant gl-Market_General-cn1 ":
                jogo = el.find_element(By.TAG_NAME ,"span")
                lista_jogos.append(jogo)
        return lista_jogos 
    
    def capturar_jogos_string(self: object):
        jogos: list = self.capturar_jogos_string()
        lista_jogos: list = []
        for jogo in jogos:
            var_jogo = jogo.text
            lista_jogos.append(var_jogo)
    
    def escolher_jogo(self: object, escolha: int) -> str:
        """
        - O parametro "escolha" deverá vir do usuario.
        - "escolha" será o indice que indicará o jogo escolhido
        - Será retornado o jogo escolhido em formato string
        """
        jogos = self.capturar_jogos()
        return jogos[escolha]
    
    def clicar_jogo(self: object) -> None:
        jogo: webdriver.Firefox = self.escolher_jogo()
        jogo.click()
    
    def separar_times(self: object) -> list:
        jogo: webdriver.Firefox = self.escolher_jogo()
        var = jogo.text
        var_jogo = var.split()
        del(var_jogo[1])
        return var_jogo
        
    def lado_para_apostar(self: object) -> None:
        ...
        
    def apostar(self: object) -> None:
        ...
    
    def fechar(self: object) -> None:
        self.__driver.close()
    
def iniciar() -> None:
    
    bot._init()
    bot._init_url()
    bot.clicar_botao_login()
    bot.escrever_dados()
    bot.fazer_login()

    
if __name__ == "__main__":
    help(action_chains)