import conftest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #passa com 'as' para que possa dar um apelido para a condição, dessa forma, na hora de chama-lo, coloca somente EC, ao invés de escrever o nome completo.
from selenium.webdriver import ActionChains, Keys

class BasePage:
    def __init__(self):
        self.driver = conftest.driver #o self é usado para referenciar a instância atual da classe, permitindo acessar os atributos e métodos da classe. Aqui, estou atribuindo o driver do conftest à variável self.driver, para que possamos usá-lo em outros métodos da classe.

    def encontrar_elemento(self, locator): #usando para encontrar elementos na página
        return self.driver.find_element(*locator) #aqui estou usando o operador * para desempacotar a tupla e passar os valores como argumentos para o método find_element

    def encontrar_elementos(self, locator): 
        return self.driver.find_elements(*locator) #passando find_elements para encontrar todos os elementos que correspondem ao localizador fornecido. Isso retorna uma lista de elementos encontrados, permitindo interagir com múltiplos elementos na página, se necessário. O de cima busca somente um, e neste busca vários.

    def escrever(self, locator, text): #usando para escrever em campos de entrada na página
        self.encontrar_elemento(locator).send_keys(text) #aqui estou chamando o método encontrar_elemento para localizar o elemento na página e, em seguida, usando o método send_keys para enviar o texto fornecido para esse elemento.

    def clicar(self, locator): #usando para clicar em elementos na página
        self.encontrar_elemento(locator).click() #aqui estou chamando o método encontrar_elemento para localizar o elemento na página e, em seguida, usando o método click para simular um clique nesse elemento.

    def verificar_elemento_visivel(self, locator): #usando para verificar se um elemento está visível na página
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela" #aqui estou chamando o método encontrar_elemento para localizar o elemento na página e, em seguida, usando o método is_displayed para verificar se o elemento está visível. Se o elemento não estiver visível, a asserção falhará, indicando que o teste não passou.

    def pegar_texto_elemento(self, locator): 
        self.esperar_elemento_aparecer(locator)
        return self.encontrar_elemento(locator).text #aqui estou chamando o método encontrar_elemento para localizar o elemento na página e, em seguida, usando a propriedade text para obter o texto contido nesse elemento.

    def esperar_elemento_aparecer(self, locator, timeout=10): #usando para esperar até que um elemento esteja presente na página antes de prosseguir com a execução do teste.
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator)) #aqui estou usando a classe WebDriverWait para aguardar até que o elemento especificado pelo localizador esteja presente na página. O tempo limite padrão é de 10 segundos, mas pode ser ajustado conforme necessário. Se o elemento não aparecer dentro do tempo limite, uma exceção será lançada.

    def verificar_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator), f"O elemento '{locator}' não foi encontrado na tela" #aqui estou chamando o método encontrar_elemento para localizar o elemento na página. Se o elemento não for encontrado, o assert falhará, indicando que o teste não passou.

    def verificar_elemento_nao_existe(self, locator):
        assert len(self.encontrar_elementos(locator)) == 0, f"O elemento '{locator}' foi encontrado na tela, mas não deveria estar presente" #aqui estou chamando o método encontrar_elementos para localizar todos os elementos correspondentes ao localizador na página. Se a lista de elementos encontrados tiver comprimento zero, significa que o elemento não está presente, e a asserção passará. Caso contrário, a asserção falhará, indicando que o teste não passou.

    def clique_duplo(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click(element).perform() #aqui estou usando a classe ActionChains para realizar uma ação de clique duplo no elemento localizado pelo localizador. O método perform() é chamado para executar a ação.

    def clique_botao_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click(element).perform() #aqui estou usando a classe ActionChains para realizar uma ação de clique com o botão direito do mouse no elemento localizado pelo localizador. O método perform() é chamado para executar a ação.

    def pressionar_tecla(self, locator, key):
        elem = self.esperar_elemento_aparecer(locator)
        if key == "ENTER": #o if é usado para verificar se a condição é verdadeira. Se for, o bloco de código dentro do if será executado.
            elem.send_keys(Keys.ENTER) #aqui estou usando a propriedade send_keys para enviar a tecla ENTER para o elemento localizado pelo localizador.
        elif key == "TAB": #elif é uma abreviação de "else if" e é usado para verificar uma condição adicional se a primeira condição não for atendida.
            elem.send_keys(Keys.TAB)
        elif key == "F1":
            elem.send_keys(Keys.F1) 