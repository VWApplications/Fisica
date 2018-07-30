from unittest import TestCase

from pytest import raises

from cinematica import Basico


class TestDistanciaPercorrida(TestCase):
    """
    Teste para os calculos de distância percorrida de cinemática básica
    """

    def test_distancia_percorrida(self):
        """
        Um móvel parte do km 50, indo até o km 60, onde, mudando o sentido do movimento, vai até o km 32.

        d = d1 + d2
        d = (60 - 50) + (60 - 32)
        d = 10 + 28
        d = 38 km
        """

        posicao_inicial1 = 50
        posicao_final1 = 60

        distancia_percorrida1 = Basico.distancia_percorrida(
            S=posicao_final1,
            So=posicao_inicial1
        )

        self.assertEqual(distancia_percorrida1, 10)

        posicao_inicial2 = 60
        posicao_final2 = 32

        distancia_percorrida2 =Basico.distancia_percorrida(
            S=posicao_final2,
            So=posicao_inicial2
        )

        self.assertEqual(distancia_percorrida2, 28)
        self.assertEqual(38, distancia_percorrida1 + distancia_percorrida2)

    def test_distancia_percorrida_error(self):
        """
        Testar a exceção que da ao não ter argumentos
        """

        with raises(Exception) as error:
            distancia_percorrida = Basico.distancia_percorrida()

            self.assertEqual(error.value, "Argumentos invalidos, verifique a documentação do método.")

