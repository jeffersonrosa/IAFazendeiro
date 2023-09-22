class Problema:
    def __init__(self, estado_inicial, estado_objetivo=None):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo


class ProblemaFazendeiro(Problema):
    entidades = ['galinha', 'cachorro', 'milho']

    def __init__(self, estado_inicial, estado_objetivo=None):
        super().__init__(estado_inicial, estado_objetivo)

    @staticmethod
    def estado_seguro(estado):
        if estado_de('fazendeiro', estado) == estado_de('galinha', estado):
            return True
        elif estado_de('galinha', estado) == estado_de('cachorro', estado):
            return False
        elif estado_de('galinha', estado) == estado_de('milho', estado):
            return False
        else:
            return True

    @staticmethod
    def objetivo_alcancado(estado):
        return all(estado_de(e, estado) == 'direita' for e in ['fazendeiro'] + ProblemaFazendeiro.entidades)

    @staticmethod
    def expande_estados(estado):
        filhos = []
        filho = estado.copy()
        mover('fazendeiro', filho)
        verifica_adiciona_filho(filho, filhos)
        for ent in ProblemaFazendeiro.entidades:
            if estado_de(ent, estado) == estado_de('fazendeiro', estado):
                filho = estado.copy()
                mover('fazendeiro', filho)
                mover(ent, filho)
                verifica_adiciona_filho(filho, filhos)
        return filhos

    def busca_solucao(self):
        caminho = [self.estado_inicial]
        proximo = self.estado_inicial.copy()
        while proximo and not self.objetivo_alcancado(proximo):
            nl = self.expande_estados(proximo)
            proximo = {}
            for filho in nl:
                if not (filho in caminho):
                    proximo = filho
                    caminho.append(proximo)
                    break
        return caminho


def estado_de(quem, estado):
    try:
        return estado[quem]
    except KeyError:
        estado[quem] = 'esquerda'
        return 'esquerda'


def mover(quem, estado):
    if estado[quem] == 'esquerda':
        estado[quem] = 'direita'
    else:
        estado[quem] = 'esquerda'
    return estado


def verifica_adiciona_filho(filho, lista_estados):
    if ProblemaFazendeiro.estado_seguro(filho):
        lista_estados.append(filho)
    return lista_estados


estado_inicial = {'fazendeiro': 'esquerda'}
for e in ProblemaFazendeiro.entidades:
    estado_inicial[e] = 'esquerda'

problema = ProblemaFazendeiro(estado_inicial)
caminho_solucao = problema.busca_solucao()
resultados_formatados = []


def formatar_saida_com_cores(estado):
    global resultados_formatados
    ESQUERDA = "\033[33;100m"
    DIREITA = "\033[33;100m"
    RIO_COR = "\033[97;44m"
    FAZENDEIRO_COR = "\033[93;43m"
    RESETAR = "\033[0m"

    esquerda = [k for k, v in estado.items() if v == 'esquerda']
    direita = [k for k, v in estado.items() if v == 'direita']
    esquerda_capitalizada = [e.capitalize() for e in esquerda]
    direita_capitalizada = [d.capitalize() for d in direita]

    esquerda_str = ', '.join(
        [ESQUERDA + e + RESETAR if e != "Fazendeiro" else FAZENDEIRO_COR + e + RESETAR for e in
         esquerda_capitalizada])
    direita_str = ', '.join(
        [DIREITA + d + RESETAR if d != "Fazendeiro" else FAZENDEIRO_COR + d + RESETAR for d in
         direita_capitalizada])

    saida_formatada = f"{len(resultados_formatados) + 1} - Esquerda [{esquerda_str}] - {RIO_COR}Rio{RESETAR} - [{direita_str}] Direita"
    resultados_formatados.append(saida_formatada)
    return saida_formatada


print("O caminho completo é:")
for estado in caminho_solucao:
    print(formatar_saida_com_cores(estado))