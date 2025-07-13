## 📋 Descrição
O objetivo deste projeto é resolver o problema de cobertura ofensiva máxima (`Max-k-Cover`) no universo Pokémon. Dado um conjunto de tipos ofensivos disponíveis e um número máximo de ataques (`k`), o programa escolhe o melhor conjunto de tipos que cobre o maior número possível de tipos defensivos.

Dois algoritmos foram implementados:

- **Algoritmo Exaustivo** — percorre todas as combinações possíveis
- **Algoritmo Guloso** — seleciona iterativamente o tipo com maior ganho

## 🗂 Estrutura
├── algoritmo.py # Implementação dos algoritmos

├── interface.py # Interface interativa via terminal

├── casos_teste/ # Casos de teste no formato .txt

├── relatorio/ # Relatórios gerados automaticamente

└── README.md # Este arquivo

## ▶️ Como executar
  1. Execute a interface:
```bash
python3 interface.py
```
Você verá uma lista de casos de teste disponíveis. Basta escolher um número, e os algoritmos serão executados. Se você digitar 0, uma entrada manual poderá ser feita. O resultado será exibido no terminal e salvo em um arquivo .txt na pasta relatorio/.

OBS: Ao adicionar uma entrada manual, coloque os tipos separados por vírgula e respeitando a acentuação.

## 🧪 Casos de Teste
Os casos de teste estão no diretório casos_teste/. Cada arquivo segue este formato:
  
Tipos: Água, Sombrio, Venenoso, Dragão, Fogo, Inseto

Número de ataques: 6
  
Você pode adicionar seus próprios arquivos com novos cenários de teste.

## 📄 Relatórios
Cada execução gera um relatório com:

- Entrada recebida
- A melhor solução encontrada por cada algoritmo
- Tipos cobertos
- Tempo de execução de cada algoritmo

Os relatórios são salvos automaticamente com timestamp em relatorio/.

## 🧑‍💻 Autores
- Daniel Coelho Santos
- Paulo Sérgio da Silva Júnior

Projeto desenvolvido como parte da disciplina de Grafos — Bacharelado em Tecnologia da Informação — UFRN

