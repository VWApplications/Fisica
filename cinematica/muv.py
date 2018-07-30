from math import pow, sqrt


class MUV(object):
    """
    Métodos para resolução de tópicos de física: MUV
    Obs: Utilize parâmetros nomeados
    """

    ERROR = "Argumentos invalidos, verifique a documentação do método."

    @classmethod
    def velocidade(cls, V: float=None, Vo: float=None, a: float=None, t: float=None) -> dict:
        """
        Equação horaria da velocidade do MUV.

        V = Vo + at

        :param V: Velocidade final
        :param Vo: Velocidade inicial
        :param a: Aceleração
        :param t: Tempo

        :return: Dicionário {V, Vo, a, t, movimento}

        Movimento: Acelerado e Progressivo, Retardado e Retrógrado, Retardado e Progressivo ou Acelerado e Retrógrado
        """

        if (V is None and
            a is not None and
            t is not None and
            Vo is not None):

            V = Vo + a*t

        elif (Vo is None and
              V is not None and
              a is not None and
              t is not None):

            Vo = V - a*t

        elif (a is None and
              V is not None and
              Vo is not None and
              t is not None):

            a = (V - Vo)/t

        elif (t is None and
              V is not None and
              Vo is not None and
              a is not None):

            t = (V - Vo)/a

        else:
            raise Exception(cls.ERROR)

        resultado = {
            'V': V,
            'Vo': Vo,
            'a': a,
            't': t
        }

        if a > 0:
            if V > 0:
                resultado['movimento'] = "Acelerado e Progressivo"
            else:
                resultado['movimento'] = "Retardado e Retrógrado"
        elif a < 0:
            if V > 0:
                resultado['movimento'] = "Retardado e Progressivo"
            else:
                resultado['movimento'] = "Acelerado e Retrógrado"

        return resultado

    @classmethod
    def aceleracao(cls, a: float=None, DV: float=None, DT: float=None)-> dict:
        """
        Aceleração ou coeficiente angular da reta ou declividade da reta (a)
        o quanto sua velocidade varia na unidade de tempo.

        a = DV/DT

        :param a: Aceleração
        :param DV: Velocidade
        :param DT: Intervalo de tempo

        :return: Dicionário {a, DV, DT, angulo}

        Angulo: Agudo ou Obtuso
        """

        if (a is None and
            DV is not None and
            DT is not None):

            a = DV/DT

        elif (DV is None and
              a is not None and
              DT is not None):

            DV = a * DT

        elif (DT is None and
              DV is not None and
              a is not None):

            DT = DV/a

        else:
            raise Exception(cls.ERROR)

        resultado = {
            'a': a,
            'DV': DV,
            'DT': DT
        }

        if a > 0:
            resultado['angulo'] = "Agudo"
        elif a < 0:
            resultado['angulo'] = "Obtuso"

        return resultado

    @classmethod
    def velocidade_media(cls, V: float=None, Vo: float=None, Vm: float=None) -> dict:
        """
        A velocidade média do MUV é a média aritmetica das velocidades nos
        instantes extremos de dois intervalos de tempo quaisquer.

        Vm = V - Vo

        :param V: Velocidade final
        :param Vo: Velocidade inicial
        :param Vm: Velocidade média

        :return: Dicionário {V, Vo, Vm}
        """

        if (V is None and
            Vo is not None and
            Vm is not None):

            V = 2*Vm - Vo

        elif (Vo is None and
              V is not None and
              Vm is not None):

            Vo = 2*Vm - V

        elif (Vm is None and
              V is not None and
              Vo is not None):

            Vm = (V + Vo)/2

        else:
            raise Exception(cls.ERROR)

        resultado = {
            'Vm': Vm,
            'V': V,
            'Vo': Vo
        }

        return resultado

    @classmethod
    def posicao(cls, S: float=None, So: float=None, Vo: float=None, t: float=None, a: float=None) -> dict:
        """
        Função horária do espaço (posição) de um móvel em MUV e Torricelli.

        S = So + Vot + at^2/2

        :param S: Posição Final
        :param So: Posição Inicial
        :param Vo: Velocidade Inicial
        :param t: Tempo
        :param a: Aceleração
        :return: Dicionário {S, So, Vo, t, a}
        """

        if (S is None and
            So is not None and
            Vo is not None and
            t is not None and
            a is not None):

            S = So + Vo*t + (a*pow(t, 2))/2

        elif (So is None and
              S is not None and
              Vo is not None and
              t is not None and
              a is not None):

            So = S - Vo*t - (a*pow(t, 2))/2

        elif (Vo is None and
              S is not None and
              So is not None and
              t is not None and
              a is not None):

            Vo = (2*S - 2*So - a*pow(t, 2))/(2*t)

        elif (t is None and
              S is not None and
              So is not None and
              Vo is not None and
              a is not None):

            resultado = self.torricelli(kwargs)
            V = resultado['V']
            t = (2*(S - So))/(Vo + V)

        elif (a is None and
              S is not None and
              So is not None and
              Vo is not None and
              t is not None):

            a = (2*(S - So - Vo*t))/(pow(t, 2))

        else:
            raise Exception(cls.ERROR)

        resultado = {
            'S': S,
            'So': So,
            'Vo': Vo,
            't': t,
            'a': a
        }

        return resultado

    @classmethod
    def torricelli(cls, V: float=None, S: float=None, So: float=None,
                   DS: float=None, Vo: float=None, a: float=None) -> dict:
        """
        Esquação de Torricelli, utilizada quando não aparece a variável tempo.

        V = Vo^2 + 2aDS

        DS = S - So

        :param V: Velocidade final
        :param S: Posição final
        :param So: Posição inicial
        :param DS: Deslocamento Escalar
        :param Vo: Velocidade inicial
        :param a: Aceleração
        :return: Dicionário {V, S, So, DS, Vo, a}
        """

        if (S is not None and
            So is not None and
            DS is None):

            DS = S - So

        if (V is None and
            DS is not None and
            Vo is not None and
            a is not None):

            V = sqrt(pow(Vo, 2) + 2*a*(DS))

        elif (DS is None and
              V is not None and
              Vo is not None and
              a is not None):

            DS = (pow(V, 2) - pow(Vo, 2))/(2*a)

        elif (Vo is None and
              V is not None and
              DS is not None and
              a is not None):

            Vo = sqrt(pow(V, 2) - 2*a*DS)

        elif (a is None and
              V is not None and
              DS is not None and
              Vo is not None):

            a = (pow(V, 2) - pow(Vo, 2))/(2*DS)

        else:
            raise Exception(cls.ERROR)

        resultado = {
            'V': V,
            'S': S,
            'So': So,
            'DS': DS,
            'Vo': Vo,
            'a': a
        }

        return resultado
