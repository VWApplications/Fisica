from unittest import TestCase
from pytest import raises

from cinematica import Basico


class TestDeslocamentoEscalar(TestCase):
    """
    Teste para os calculos de deslocamento escalar de cinemática básica
    """

    def test_deslocamento_escalar(self):
        """
        Um móvel parte do km 50, indo até o km 60, onde, mudando o sentido do movimento, vai até o km 32.

        DS = S - S0
        DS = 32 - 50
        DS = -18 km
        """

        posicao_final = 32
        posicao_inicial = 50

        deslocamento_escalar = Basico.deslocamento_escalar(
            S=posicao_final,
            So=posicao_inicial
        )

        self.assertEqual(deslocamento_escalar, -18)

    def test_deslocamento_escalar_apos_60_segundos(self):
        """
        Teste que verificar o deslocamento escalar apos 60 segundos de um atleta a 5 m/s
        utilizando a velocidade média e o tempo

        DS = V.DT
        DS = 5.60
        DS = 300 m
        """

        velocidade = 5 # m/s
        tempo = 60 # segundos

        deslocamento = Basico.deslocamento_escalar(
            Vm=velocidade,
            DT=tempo
        )

        self.assertEqual(deslocamento, 300)

    def test_deslocamento_escalar_error(self):
        """
        Teste do deslocamento escalar sem os devidos argumentos
        """

        with raises(Exception) as error:
            deslocamento_escalar = Basico.deslocamento_escalar()

            self.assertEqual(error.value, "Argumentos invalidos, verifique a documentação do método.")