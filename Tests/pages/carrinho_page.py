from Tests.pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By

class CarrinhoPage(BasePage): #a class no python é usada para criar objetos que possuem atributos e métodos. No caso, estou criando uma classe chamada LoginPage que representa a página de login do site. Dentro da classe, estou definindo os elementos da página e os métodos para interagir com eles.

    def __init__(self): #o def __init__ é um método especial em Python que é chamado quando uma nova instância da classe é criada. Ele é usado para inicializar os atributos da classe e configurar o estado inicial do objeto. No caso, estou usando o __init__ para inicializar o driver do Selenium e os localizadores dos elementos da página de login.
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//div[contains(@class, 'inventory_item_name') and contains(normalize-space(text()), '{}')]")
        self.botao_continuar_comprando = (By.ID, "continue-shopping")

    def verificar_produto_carrinho_existe(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_elemento_visivel(item)

    def clicar_botao_continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando)