from network.topology import construir_topologia
from network.simulator import xping, xtraceroute

# Monta a rede como grafo
G = construir_topologia()

# Executa simulações
xping(G, "h1", "h4")
xtraceroute(G, "h1", "h4")
