from unittest import TestCase
from pytest import raises

from cinematica import Basico


class TestIntervaloDeTempo(TestCase):
    """
    Teste para os calculos de intervalo de tempo de cinemática básica
    """

    def test_intervalor_de_tempo(self):
        """
        Qual o intervalo de tempo dado: T0 = 10 minutos e T = 45 minutos
        DT = T - To
        DT = 45 - 10
        DT = 35 minutos
        """

        tempo_inicial = 10 # minutos
        tempo_final = 45 # minutos

        intervalo_de_tempo = Basico.intervalo_de_tempo(
            T=tempo_final,
            To=tempo_inicial
        )

        self.assertEqual(intervalo_de_tempo, 35)

    def test_intervalo_de_tempo_usando_velocidade(self):
        """
        Após uma chuva torrencial as águas da chuva desceram o rio A até o rio B, percorrendo
        cerca de 1.000 km. Sendo de 4 km/h a velocidade média das águas, o percurso
        mencionado será cumprido pelas águas da chuva em aproximadamente:

        Vm = DS/DT
         4 = 1000/DT
        DT = 1000/4
        DT = 250 horas
        """

        Vm = 4 # km/h
        DS = 1000 # km

        intervalo_de_tempo = Basico.intervalo_de_tempo(
            Vm=Vm,
            DS=DS
        )

        self.assertEqual(intervalo_de_tempo, 250)

    def test_intervalo_de_tempo_error(self):
        """
        Teste de intervalo de tempo sem algum argumento
        """

        with raises(Exception) as error:
            intervalo_de_tempo = Basico.intervalo_de_tempo()

            self.assertEqual(error.value, "Argumentos invalidos, verifique a documentação do método.")