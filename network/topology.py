import networkx as nx

def construir_topologia():
    G = nx.DiGraph()

    # ==============
    # ADIÇÃO DOS NÓS
    # ==============

    # Hosts
    host_ips = {
        'h1': '192.168.0.2',
        'h2': '192.168.0.3',
        'h3': '192.168.0.4',  
        'h4': '192.168.0.34', 
        'h5': '192.168.0.35',
        'h6': '192.168.0.36', 
        'h7': '192.168.0.66',
        'h8': '192.168.0.67',
        'h9': '192.168.0.98',
        'h10': '192.168.0.99'
    }
    for host, ip in host_ips.items():
        G.add_node(host, tipo="host", ip=ip)

    # Switches de borda (e1 a e4)
    # O IP do gateway da sub-rede foi usado como IP de gerenciamento para o switch.
    switch_ips = {
        'e1': '192.168.0.1',
        'e2': '192.168.0.33',
        'e3': '192.168.0.65',
        'e4': '192.168.0.97'
    }
    for switch, ip in switch_ips.items():
        G.add_node(switch, tipo="switch", ip=ip)


    # Roteadores de agregação (a1, a2)
    G.add_node("a1", tipo="roteador", ip="192.168.0.130")
    G.add_node("a2", tipo="roteador", ip="192.168.0.134")

    # Roteador central (Core)
    G.add_node("Core", tipo="roteador", ip="192.168.0.129")

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
