import networkx as nx

def construir_topologia():
    #Constrói a topologia da rede para refletir o diagrama.
    G = nx.DiGraph()

    # ==============
    # ADIÇÃO DOS NÓS
    # ==============

    # Hosts
    for i in range(1, 11):
        G.add_node(f"h{i}", tipo="host", ip=f"10.0.{i}.1")

    # Switches de borda (e1 a e4)
    for i in range(1, 5):
        G.add_node(f"e{i}", tipo="switch", ip=f"10.0.{i}.254")

    # Roteadores de agregação (a1, a2)
    G.add_node("a1", tipo="roteador", ip="10.0.100.1")
    G.add_node("a2", tipo="roteador", ip="10.0.100.2")

    # Roteador central (Core)
    G.add_node("Core", tipo="roteador", ip="10.0.200.1")

    # ========
    # CONEXÕES
    # ========

    # Conexões Hosts -> Switches de Borda
    # Sub-rede e1
    G.add_edge("h1", "e1", latencia=20); G.add_edge("e1", "h1", latencia=20)
    G.add_edge("h2", "e1", latencia=20); G.add_edge("e1", "h2", latencia=20)
    G.add_edge("h3", "e1", latencia=20); G.add_edge("e1", "h3", latencia=20)

    # Sub-rede e2
    G.add_edge("h4", "e2", latencia=20); G.add_edge("e2", "h4", latencia=20)
    G.add_edge("h5", "e2", latencia=20); G.add_edge("e2", "h5", latencia=20)
    G.add_edge("h6", "e2", latencia=20); G.add_edge("e2", "h6", latencia=20)

    # Sub-rede e3
    G.add_edge("h7", "e3", latencia=20); G.add_edge("e3", "h7", latencia=20)
    G.add_edge("h8", "e3", latencia=20); G.add_edge("e3", "h8", latencia=20)

    # Sub-rede e4
    G.add_edge("h9", "e4", latencia=20); G.add_edge("e4", "h9", latencia=20)
    G.add_edge("h10", "e4", latencia=20); G.add_edge("e4", "h10", latencia=20)


    # Conexões Switches de Borda -> Roteadores de Agregação
    G.add_edge("e1", "a1", latencia=10); G.add_edge("a1", "e1", latencia=10)
    G.add_edge("e2", "a1", latencia=10); G.add_edge("a1", "e2", latencia=10)
    G.add_edge("e3", "a2", latencia=10); G.add_edge("a2", "e3", latencia=10)
    G.add_edge("e4", "a2", latencia=10); G.add_edge("a2", "e4", latencia=10)

    # Conexões Roteadores de Agregação -> Core
    G.add_edge("a1", "Core", latencia=5); G.add_edge("Core", "a1", latencia=5)
    G.add_edge("a2", "Core", latencia=5); G.add_edge("Core", "a2", latencia=5)

    return G