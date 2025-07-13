#!/usr/bin/env python3

import os
from algoritmo import algoritmoExaustivo, algoritmoGuloso, verificarCoberturaVariosTipos
import time
import datetime

def carregar_caso(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    
    tipos = []
    num_ataques = 0
    for linha in linhas:
        if linha.lower().startswith('tipos'):
            tipos = [t.strip().capitalize() for t in linha.split(':')[1].split(',')]
        elif linha.lower().startswith('k') or 'número de ataques' in linha.lower():
            num_ataques = int(linha.split(':')[1].strip())

    return tipos, num_ataques

def salvar_relatorio(nome_base, conteudo):
    os.makedirs('relatorio', exist_ok=True)

    # Gerar timestamp curto para evitar sobrescrita
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    nome_final = f"{nome_base}_{timestamp}.txt"
    caminho = os.path.join('relatorio', nome_final)

    with open(caminho, 'w') as f:
        f.write(conteudo)

    return nome_final

def main():
    print("Casos de teste disponíveis:\n")
    casos = [f for f in os.listdir('casos_teste') if f.endswith('.txt')]
    for i, nome in enumerate(casos):
        print(f"{i + 1}. {nome}")

    while True:
        try:
            escolha = int(input("\nEscolha o número do caso de teste: "))
            if 1 <= escolha <= len(casos):
                break
            else:
                print(f"Por favor, digite um número entre 1 e {len(casos)}.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")
    
    caso_nome = casos[escolha - 1]
    tipos_disponiveis, k = carregar_caso(os.path.join('casos_teste', caso_nome))

    print(f"\nTipos disponíveis: {tipos_disponiveis}")
    print(f"Número de ataques: {k}")

    # Exaustivo
    t0 = time.time()
    sol_ex, tam_ex = algoritmoExaustivo(tipos_disponiveis, k)
    t1 = time.time()
    cobertos_ex = verificarCoberturaVariosTipos(sol_ex)

    # Guloso
    t2 = time.time()
    sol_gul = algoritmoGuloso(k, tipos_disponiveis)
    t3 = time.time()
    cobertos_gul = verificarCoberturaVariosTipos(sol_gul)

    print("\n--- RESULTADOS ---\n")
    print("Exaustivo:")
    print(f"Melhor solução: {sol_ex}")
    print(f"Cobre {tam_ex} tipos: {cobertos_ex}")
    print(f"Tempo: {t1 - t0:.6f} s")

    print("\nGuloso:")
    print(f"Melhor solução: {sol_gul}")
    print(f"Cobre {len(cobertos_gul)} tipos: {cobertos_gul}")
    print(f"Tempo: {t3 - t2:.6f} s")

    relatorio = f"""RELATÓRIO DO EXPERIMENTO

Caso de teste: {caso_nome}

--- Entrada ---
Tipos disponíveis: {tipos_disponiveis}
Número de ataques permitidos: {k}

=== Algoritmo Exaustivo ===
Solução: {sol_ex}
Cobre {tam_ex} tipos: {cobertos_ex}
Tempo: {t1 - t0:.6f} s

=== Algoritmo Guloso ===
Solução: {sol_gul}
Cobre {len(cobertos_gul)} tipos: {cobertos_gul}
Tempo: {t3 - t2:.6f} s
"""

    nome_base = f"experimento_{caso_nome.replace('.txt', '')}"
    arquivo_salvo = salvar_relatorio(nome_base, relatorio)
    print(f"\nRelatório salvo em: relatorio/{arquivo_salvo}")

if __name__ == "__main__":
    main()