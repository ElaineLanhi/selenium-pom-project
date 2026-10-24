import pytest

class TestSimulacao: #criando uma classe no pytest. e quando é uma classe, precisa adicionar o 'self' nos parenteses dos metodos
        
    @pytest.mark.simulacao #marcando a classe com o nome 'simulacao', para que seja possível rodar apenas os testes dessa classe, usando o comando: pytest -m simulacao // se não for marcado, o pytest vai rodar todos os testes do projeto.
    def test_simulacao_1(self):
        assert 1 == 1

    @pytest.mark.simulacao
    @pytest.mark.skip #marcando o teste para ser ignorado, ou seja, não será executado. // se quiser rodar apenas os testes que não estão marcados com skip, usar o comando: pytest -m "not skip"
    def test_simulacao_2(self):
            assert 2 == 2