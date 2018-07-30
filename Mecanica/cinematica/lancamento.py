from math import pow, sqrt


class LancamentoVertical(object):
    """
    Lançamento vertical para cima.
    """

    ERROR = "Parâmentros invalidos, por favor verifique a documentação do método"

    @classmethod
    def tempo_de_subida(cls, Ts: float=None, Vo: float=None, g: float=10.0) -> dict:
        """
        Calcular o tempo de subida do lançamento.

        :param Ts: Tempo de subida
        :param Vo: Velocidade Inicial
        :param g: Aceleração da Gravidade
        :return: Dicionario {'Ts', 'Vo', 'g'}
        """

        if (Ts is None and
            Vo is not None and
            g is not None):

            Ts = Vo/g

        elif (Vo is None and
              Ts is not None and
              g is not None):

            Vo = Ts * g

        elif (g is None and
              Vo is not None and
              Ts is not None):

            g = Vo/Ts

        else:
            Exception(cls.Error)

        resultado = {
            'Ts': Ts,
            'Vo': Vo,
            'g': g
        }

        return resultado

    @classmethod
    def altura_maxima(cls, Hm: float=None, Vo: float=None, g: float=10.0) -> dict:
        """
        Altura máxima do lançamento.

        :param Hm: Altura máxima
        :param Vo: Velocidade Inicial
        :param g: Aceleração da gravidade
        :return: Dicionário {'Hm', 'Vo', 'g'}
        """

        if (Hm is None and
            Vo is not None and
            g is not None):

            Hm = pow(Vo, 2)/(2*g)

        elif (Vo is None and
              Hm is not None and
              g is not None):

            Vo = sqrt(2*g*Hm)

        elif (g is None and
              Vo is not None and
              Hm is not None):

            g = pow(Vo, 2)/(2*Hm)

        else:
            Exception(cls.ERROR)

        resultado = {
            'Hm': Hm,
            'Vo': Vo,
            'g': g
        }

        return resultado
