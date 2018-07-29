from unittest import TestCase
from pytest import raises

from cinematica import Cinematica
from cinematica.fisica import Basico


class TestDeslocamentoEscalar(TestCase):
    """
    Teste para os calculos de deslocamento escalar de cinemática básica
    """

    def setUp(self):
        """
        Código que executa antes de cada teste
        """

        self.cinematica = Cinematica(Cinematica.BASICO)

    def tearDown(self):
        """
        Código que executa depois de cada teste
        """

        self.cinematica = None

    def test_deslocamento_escalar(self):
        """
        Um móvel parte do km 50, indo até o km 60, onde, mudando o sentido do movimento, vai até o km 32.

        DS = S - S0
        DS = 32 - 50
        DS = -18 km
        """

        posicao_final = 32
        posicao_inicial = 50

        deslocamento_escalar = self.cinematica.calcular(
            Basico.DESLOCAMENTO_ESCALAR,
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

        deslocamento = self.cinematica.calcular(
            Basico.DESLOCAMENTO_ESCALAR,
            Vm=velocidade,
            DT=tempo
        )

        self.assertEqual(deslocamento, 300)

    def test_deslocamento_escalar_error(self):
        """
        Teste do deslocamento escalar sem os devidos argumentos
        """

        with raises(Exception) as error:
            deslocamento_escalar = self.cinematica.calcular(
                Basico.DESLOCAMENTO_ESCALAR
            )

            self.assertEqual(error.value, "Argumentos invalidos, verifique a documentação do método.")