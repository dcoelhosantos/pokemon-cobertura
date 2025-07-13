import itertools

efetividade = {
    'Normal': [],
    'Fogo': ['Planta', 'Gelo', 'Inseto', 'Aço'],
    'Água': ['Fogo', 'Pedra', 'Terrestre'],
    'Planta': ['Água', 'Pedra', 'Terrestre'],
    'Elétrico': ['Água', 'Voador'],
    'Gelo': ['Planta', 'Terrestre', 'Voador', 'Dragão'],
    'Lutador': ['Normal', 'Pedra', 'Aço', 'Sombrio', 'Gelo'],
    'Venenoso': ['Planta', 'Fada'],
    'Terrestre': ['Fogo', 'Elétrico', 'Veneno', 'Aço', 'Pedra'],
    'Voador': ['Planta', 'Lutador', 'Inseto'],
    'Psíquico': ['Lutador', 'Venenoso'],
    'Inseto': ['Planta', 'Psíquico', 'Sombrio'],
    'Pedra': ['Fogo', 'Gelo', 'Voador', 'Inseto'],
    'Fantasma': ['Psíquico', 'Fantasma'],
    'Dragão': ['Dragão'],
    'Sombrio': ['Psíquico', 'Fantasma'],
    'Aço': ['Fada', 'Gelo', 'Pedra'],
    'Fada': ['Dragão', 'Lutador', 'Sombrio']
}

def verificarCoberturaVariosTipos(combinacao):
    tipos_atingidos = set()
    for tipo in combinacao:
        tipos_atingidos.update(efetividade.get(tipo, []))
    return tipos_atingidos

def verificarCoberturaUmTipo(tipo, cobertos):
    tipos_atingidos = efetividade.get(tipo,[])
    return list(set(tipos_atingidos) - set(cobertos))

def algoritmoExaustivo(tipos_disponiveis, num_ataques):
    melhor_solucao = []
    melhor_tamanho = 0

    combinacoes = itertools.combinations(tipos_disponiveis, num_ataques)

    for combinacao in combinacoes:
        cobertos = verificarCoberturaVariosTipos(combinacao)
        if len(cobertos) > melhor_tamanho:
            melhor_tamanho = len(cobertos)
            melhor_solucao = combinacao

    return melhor_solucao, melhor_tamanho

def algoritmoGuloso(num_ataques, tipos_disponiveis):
    selecionados = []
    cobertos = []

    while len(selecionados) < num_ataques:
        melhor = None
        maior_ganho = -1
        tipos_restantes = list(set(tipos_disponiveis) - set(selecionados))

        for tipo in tipos_restantes:
            ganho = len(verificarCoberturaUmTipo(tipo, cobertos))
            if ganho > maior_ganho:
                maior_ganho = ganho
                melhor = tipo

        selecionados.append(melhor)
        cobertos = verificarCoberturaVariosTipos(selecionados)

    return selecionados