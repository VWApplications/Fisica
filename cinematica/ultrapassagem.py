class Ultrapassagem(object):
    """
    Métodos para resolução de tópicos de física: Ultrapassagem

    Obs: Utilize parâmetros nomeados
    """

    ERROR = "Argumentos invalidos, verifique a documentação do método."

    @classmethod
    def velocidade_relativa(cls, V1: float=None, V2: float=None, sentidos_opostos: bool=False) -> float:
        """
        Velocidade de ultrapassagem relativa depende do sentido de
        ultrapassagem, se o tiver o mesmo sentido que no caso é o padrão,
        (sentido_contrario=False) vai subtrair as velocidade, caso contrario
        irá somar.

        :param V1: Velocidade do objeto ultrapassando
        :param V2: Velocidade do objeto ultrapassado
        :param sentidos_opostos: Sentido da ultrapassagem, False se for no mesmo sentido (padrão) e True em
                                 sentidos contrarios
        :return: Velocidade Relativa (Vr)
        """

        if V1 is None or V2 is None:
            raise Exception(cls.ERROR)

        if sentidos_opostos:
            Vr = V1 + V2
        else:
            Vr = V1 - V2

        return Vr

    @classmethod
    def velocidade_de_ultrapassagem(cls, DS :float=None, DT :float=None) -> float:
        """
        Velocidade de ultrapassagem (Vu)

        :param DS: Comprimento dos corpos
        :param DT: Intervalo de duração da ultrapassagem
        :return: Velocidade de ultrapassagem (Vu)
        """

        if DS is None or DT is None:
            raise Exception(cls.ERROR)

        Vu = DS/DT

        return Vu

    @classmethod
    def comprimento_dos_corpos(cls, Vu :float=None, DT :float=None) -> float:
        """
        Comprimento do corpo (DS) ultrapassado

        :param Vu: Velocidade de ultrapassagem
        :param DT: Intervalo de duração da ultrapassagem
        :return: Comprimento do corpo ultrapassado (DS)
        """

        if Vu is None or DT is None:
            raise Exception(cls.ERROR)

        DS = Vu * DT

        return DS

    @classmethod
    def tempo_de_ultrapassagem(cls, DS :float=None, Vu :float=None) -> float:
        """
        Intervalo de duração da ultrapassagem (DT)

        :param DS: Comprimento dos corpos
        :param Vu: Velocidade de ultrapassagem
        :return: Intervalo de duração da ultrapassagem (DT)
        """

        if DS is None or Vu is None:
            raise Exception(cls.ERROR)

        DT = DS/Vu

        return DT
