import networkx as nx

def xping(G, origem, destino):
    try:
        caminho = nx.shortest_path(G, origem, destino)
        print(f"[XPING] Conectado de {origem} até {destino}")
        print(" → ".join(caminho))
    except nx.NetworkXNoPath:
        print("[XPING] Sem caminho possível.")

def xtraceroute(G, origem, destino):
    try:
        caminho = nx.shortest_path(G, origem, destino)
        print("[XTRACEROUTE] Caminho traçado:")
        for hop in caminho:
            print(f" - {hop}")
    except nx.NetworkXNoPath:
        print("[XTRACEROUTE] Sem rota.")
