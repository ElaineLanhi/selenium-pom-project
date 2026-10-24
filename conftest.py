import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture #marcando a função como fixture, ou seja, uma função que será executada antes e depois do teste.
def setup_teardown():
    # setup 
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield #é um retorno do teste.

    driver.quit() #teardown, ou seja, finalizando o teste.