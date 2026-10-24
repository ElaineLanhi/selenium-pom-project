from Tests.pages.base_page import BasePage
from selenium.webdriver.common.by import By
import conftest


class HomePage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.titulo_page = (By.XPATH, "//span[@class='title']") #localizador do título da página inicial
        self.item_inventario = (By.XPATH, "//div[contains(@class, 'inventory_item_name') and contains(normalize-space(text()), '{}')]")
        self.botao_adicionar_carrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.icone_carrinho = (By.XPATH, "//*[@class='shopping_cart_link']") 

    def verificar_login_sucesso(self):
        self.verificar_elemento_visivel(self.titulo_page) #chamando o método verificar_elemento_visivel da classe BasePage para verificar se o título da página inicial está visível, indicando que o login foi bem-sucedido.

    def adicionar_produto_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item)) #formatando o localizador do item de inventário com o nome do item passado como parâmetro
        self.clicar(item) #clicando no item de inventário
        self.clicar(self.botao_adicionar_carrinho) #clicando no botão "Add to cart" para adicionar o item ao carrinho

    def clicar_icone_carrinho(self):
        self.clicar(self.icone_carrinho)