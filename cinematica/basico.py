from math import fabs


class Basico(object):
    """
    Métodos básicos para resolução de tópicos de cinemática como
    deslocamento escalar, distância percorrida, intervalo de tempo e
    velocidade média.

    Obs: Utilize parâmetros nomeados
    """

    ERROR = "Parâmentros invalidos, por favor verifique a documentação do método"

    @classmethod
    def deslocamento_escalar(cls, S: float=None, So: float=None, Vm: float=None,
                             DT: float=None, TP: float=0) -> float:
        """
        Deslocamento escalar (DS) é o deslocamento entre o destino (S)
        e o ponto de partida (So) ou é a velocidade média (Vm) vezes
        o intervalo de tempo (DT) + tempo de parada (TP) caso tiver

        :param S: Destino
        :param So: Ponto de partida
        :param Vm: Velocidade média
        :param DT: Intervalo de tempo
        :param TP: Tempo de parada
        :return: Deslocamento escalar ou DS
        """

        if S is not None and So is not None:
            DS = S - So

        elif Vm is not None and DT is not None:
            DS = Vm * (DT + TP)

        else:
            raise Exception(cls.ERROR)

        return DS

    @classmethod
    def distancia_percorrida(cls, S: float=None, So: float=None) -> float:
        """
        Distância percorrida (D)

        :param S: Destino
        :param So: Ponto de partida
        :return: Distância percorrida ou D
        """

        if S is None or So is None:
            raise Exception(cls.ERROR)

        if fabs(S) > fabs(So):
            D = fabs(S) - fabs(So)
        else:
            D = fabs(So) - fabs(S)

        return D

    @classmethod
    def intervalo_de_tempo(cls, T: float=None, To: float=None, DS: float=None,
                           Vm: float=None, TP: float=None) -> float:
        """
        Calculo do intervalor de tempo (DT)

        :param T: Tempo final
        :param To: Tempo inicial
        :param DS: Deslocamento escalar
        :param Vm: Velocidade média
        :param TP: Tempo de parada
        :return: Intervalo de tempo (DT)
        """

        if T is not None and To is not None:
            DT = T - To

        elif Vm is not None and DS is not None:
            DT = DS/Vm

        else:
            raise Exception(cls.ERROR)

        if TP:
            return DT + TP

        return DT

    @classmethod
    def velocidade_media(cls, V: float=None, Vo: float=None, DT: float=None,
                         DS: float=None, TP: int=0) -> float:
        """
        Calculo da velocidade escalar média (Vm)

        :param V: Velocidade final
        :param Vo: Velocidade inicial
        :param DT: Intervalo de tempo
        :param DS: Deslocamento escalar
        :param TP: Tempo de parada
        :return: Velocidade (V)
        """

        if V is not None or Vo is not None:
            Vm = V - Vo

        elif DS is not None and DT is not None:
            Vm = DS/(DT + TP)

        else:
            raise Exception(cls.ERROR)

        return Vm