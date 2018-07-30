from math import fabs


class MU(object):
    """
    Métodos para resolução de tópicos de física: MU
    Obs: Utilize parâmetros nomeados
    """

    ERROR = "Argumentos invalidos, verifique a documentação do método."

    @classmethod
    def posicao(cls, S: float=None, So: float=None, V: float=None, T: float=None) -> dict:
        """
        Calcular a função horária do movimento uniforme MU.

        :param S: Posição final
        :param So: Posição inicial
        :param V: Velocidade
        :param T: Tempo
        :return: Dicionário {S, So, V, T}
        """

        if (S is None and
            So is not None and
            V is not None and
            T is not None):

            S = So + V*T

        elif (So is None and
              S is not None and
              V is not None and
              T is not None):

            So = S - V*T

        elif (V is None and
              S is not None and
              So is not None and
              T is not None):

            V = (S - So)/T

        elif (V is None and
              S is not None and
              So is not None and
              T is not None):

            T = (S - So)/V

        else:
            raise Exception(cls.ERROR)

        resultado = {
            'S': S,
            'So': So,
            'V': V,
            'T': T
        }

        return resultado

    @classmethod
    def tempo_de_encontro(cls, So1: float=None, V1: float=None, So2: float=None, V2: float=None) -> float:
        """
        Tempo de encontre entre dois objetos.

        :param So1: Posição inicial do primeiro objeto.
        :param V1: Velocidade do primeiro objeto
        :param So2: Posição inicial do segundo objeto
        :param V2: Velocidade do segundo objeto
        :return: Momento do encontro entre o objeto 1 e o objeto 2 (T)
        """

        if (So1 is None or
            V1 is None or
            So2 is None or
            V2 is None):

            raise Exception(cls.ERROR)

        T = (So2 - So1)/(V1 - V2)

        return fabs(T)

    @classmethod
    def instante_de_encontro(cls, So1: float=None, V1: float=None, So2: float=None, V2: float=None) -> dict:
        """
        Instante ou posição do encontro.

        :param So1: Posição inicial do primeiro objeto.
        :param V1: Velocidade do primeiro objeto
        :param So2: Posição inicial do segundo objeto
        :param V2: Velocidade do segundo objeto

        :return: Posição de encontro de S1 e S2 (S)
        """

        T = self.tempo_de_encontro(So1, V1, So2, V2)

        # Para calcular o instante de encontro só usar o tempo
        # em qualquer uma das equações, no caso foi do objeto 01
        resultado = MU.posicao(So=So1, V=V1, T=T)

        return resultado['S']
