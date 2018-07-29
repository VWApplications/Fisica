from math import fabs


class Basico(object):
    """
    Métodos básicos para resolução de tópicos de cinemática como
    deslocamento escalar, distância percorrida, intervalo de tempo e
    velocidade média.

    Obs: Utilize parâmetros nomeados
    """

    DESLOCAMENTO_ESCALAR = 1
    DISTANCIA_PERCORRIDA = 2
    INTERVALO_DE_TEMPO = 3
    VELOCIDADE_MEDIA = 4

    ERROR = "Argumentos invalidos, verifique a documentação do método."

    def calcular(self, operacao, kwargs):
        """
        Calcula as operações de cinemática

        :param operacao: DESLOCAMENTO_ESCALAR, DISTANCIA_PERCORRIDA, INTERVALO_DE_TEMPO e VELOCIDADE_MEDIA
        :param kwargs: Variáveis da operação, por exemplo, Vo, V, t
        :return: O valor da operação
        """

        if operacao == 1:
            resultado = self.deslocamento_escalar(
                S=kwargs.get('S', None),
                So=kwargs.get('So', None),
                Vm=kwargs.get('Vm', None),
                DT=kwargs.get('DT', None),
                TP=kwargs.get('TP', 0)
            )
        elif operacao == 2:
            resultado = self.distancia_percorrida(
                S=kwargs.get('S', None),
                So=kwargs.get('So', None)
            )
        elif operacao == 3:
            resultado = self.intervalo_de_tempo(
                T=kwargs.get('T', None),
                To=kwargs.get('To', None),
                Vm=kwargs.get('Vm', None),
                DS=kwargs.get('DS', None),
                TP=kwargs.get('TP', 0)
            )
        elif operacao == 4:
            resultado = self.velocidade_media(
                V=kwargs.get('V', None),
                Vo=kwargs.get('Vo', None),
                DS=kwargs.get('DS', None),
                DT=kwargs.get('DT', None),
                TP=kwargs.get('TP', 0)
            )
        else:
            raise Exception("Operação invalida!")

        return resultado

    def deslocamento_escalar(self, S:float=None, So:float=None, Vm:float=None,
                             DT:float=None, TP:float=0) -> float:
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
            raise Exception(self.ERROR)

        return DS

    def distancia_percorrida(self, S:float=None, So:float=None) -> float:
        """
        Distância percorrida (D)

        :param S: Destino
        :param So: Ponto de partida
        :return: Distância percorrida ou D
        """

        if S is None or So is None:
            raise Exception(self.ERROR)

        if fabs(S) > fabs(So):
            D = fabs(S) - fabs(So)
        else:
            D = fabs(So) - fabs(S)

        return D

    def intervalo_de_tempo(self, T:float=None, To:float=None, DS:float=None,
                           Vm:float=None, TP:float=None) -> float:
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
            raise Exception(self.ERROR)

        return DT + TP

    def velocidade_media(self, V:float=None, Vo:float=None, DT:float=None,
                         DS:float=None, TP:int=0) -> float:
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
            raise Exception(self.ERROR)

        return Vm