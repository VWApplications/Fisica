from .fisica import Basico, Ultrapassagem, MU, MUV, LancamentoVertical


class Cinematica(object):
    """
    Classe que organiza todos os tópicos de cinemática.
    """

    BASICO = 1
    ULTRAPASSAGEM = 2
    MU = 3
    MUV = 4
    LANCAMENTO_VERTICAL = 5

    def __init__(self, operacao):
        """
        Construtor de operações de cinemática

        :param operacao: Constante que representa o conteúdo de cinempatica,
        opções: BASICO, ULTRAPASSAGEM, MU, MUV, LANCAMENTO_VERTICAL
        """

        if operacao == self.BASICO:
            self.cinematica = Basico()
        elif operacao == self.ULTRAPASSAGEM:
            self.cinematica = Ultrapassagem()
        elif operacao == self.MU:
            self.cinematica = MU()
        elif operacao == self.MUV:
            self.cinematica = MUV()
        elif operacao == self.LANCAMENTO_VERTICAL:
            self.cinematica = LancamentoVertical()
        else:
            raise NameError("Operação Invalida!")

    def calcular(self, operacao, **kwargs):
        """
        Calcula as operações de cinemática

        :param operacao: Constante que representa o conteúdo de cinempatica,
        opções: BASICO, ULTRAPASSAGEM, MU, MUV, LANCAMENTO_VERTICAL
        :param kwargs: Variáveis da operação, por exemplo, Vo, V, t, dependendo da operação que for calcular
        :return: O valor da operação
        """

        return self.cinematica.calcular(operacao, kwargs)
