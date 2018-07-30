from unittest import TestCase
from pytest import raises

from cinematica import Basico


class TestVelocidadeMedia(TestCase):
    """
    Teste para os calculos de velocidade média de cinemática básica
    """

    def test_velocidade_media(self):
        """
        Qual a velocidade media dado: Vo = 10 m/s e V = 40 m/s
        DV = V - Vo
        Dv = 40 - 10
        DV = 30 m/s
        """

        Vo = 10 # m/s
        V = 40 # m/s

        velocidade_media = Basico.velocidade_media(
            V=V,
            Vo=Vo
        )

        self.assertEqual(velocidade_media, 30)

    def test_velocidade_media_usando_deslocamento(self):
        """
        Num Aeroporto há um corredor eletronico com 10m que transporta uma
        pessoa entre duas estaçôes consecutivas num intervalo de tempo de 20s.
        A velocidade média desta pessoa, em m/s, é:

        Vm = DS/DT
        Vm = 10/20
        Vm = 0,5 m/s
        """

        DS = 10 # metros
        DT = 20 # segundos

        velocidade_media = Basico.velocidade_media(
            DS=DS,
            DT=DT
        )

        self.assertEqual(velocidade_media, 0.5)

    def test_velocidade_media_error(self):
        """
        Teste de velocidade sem algum argumento
        """

        with raises(Exception) as error:
            velocidade_media = Basico.velocidade_media()

            self.assertEqual(error.value, "Argumentos invalidos, verifique a documentação do método.")