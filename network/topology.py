import networkx as nx

def construir_topologia():
    G = nx.DiGraph()

    # =========================
    # ADIÇÃO DOS NÓS
    # =========================

    # Hosts
    for i in range(1, 9):
        G.add_node(f"h{i}", tipo="host", ip=f"10.0.{i}.1")

    # Switches de borda (edge switches)
    for i in range(1, 5):
        G.add_node(f"e{i}", tipo="switch", ip=f"10.0.{i}.254")

    # Switches de agregação
    G.add_node("a1", tipo="roteador", ip="10.0.100.1")
    G.add_node("a2", tipo="roteador", ip="10.0.100.2")

    # Switch central
    G.add_node("a0", tipo="roteador", ip="10.0.200.1")

    # =========================
    # CONEXÕES DOS HOSTS AOS SWITCHES DE BORDA
    # =========================

    G.add_edge("h1", "e1", tipo_enlace="par trançado", capacidade="1Gbps")
    G.add_edge("h2", "e1", tipo_enlace="par trançado", capacidade="1Gbps")
    G.add_edge("e1", "h1", tipo_enlace="par trançado", capacidade="1Gbps")  # Enlace de volta
    G.add_edge("e1", "h2", tipo_enlace="par trançado", capacidade="1Gbps")  # Enlace de volta

    G.add_edge("h3", "e2", tipo_enlace="par trançado", capacidade="1Gbps")
    G.add_edge("h4", "e2", tipo_enlace="par trançado", capacidade="1Gbps")
    G.add_edge("e2", "h3", tipo_enlace="par trançado", capacidade="1Gbps")  # Enlace de volta
    G.add_edge("e2", "h4", tipo_enlace="par trançado", capacidade="1Gbps")  # Enlace de volta

    G.add_edge("h5", "e3", tipo_enlace="par trançado", capacidade="1Gbps")
    G.add_edge("h6", "e3", tipo_enlace="par trançado", capacidade="1Gbps")
    G.add_edge("e3", "h5", tipo_enlace="par trançado", capacidade="1Gbps")  # Enlace de volta
    G.add_edge("e3", "h6", tipo_enlace="par trançado", capacidade="1Gbps")  # Enlace de volta

    G.add_edge("h7", "e4", tipo_enlace="par trançado", capacidade="1Gbps")
    G.add_edge("h8", "e4", tipo_enlace="par trançado", capacidade="1Gbps")
    G.add_edge("e4", "h7", tipo_enlace="par trançado", capacidade="1Gbps")  # Enlace de volta
    G.add_edge("e4", "h8", tipo_enlace="par trançado", capacidade="1Gbps")  # Enlace de volta

    # =========================
    # CONEXÕES ENTRE SWITCHES DE BORDA E ROTEADORES DE AGREGAÇÃO
    # =========================

    G.add_edge("e1", "a1", tipo_enlace="fibra óptica", capacidade="10Gbps")
    G.add_edge("e2", "a1", tipo_enlace="fibra óptica", capacidade="10Gbps")
    G.add_edge("a1", "e1", tipo_enlace="fibra óptica", capacidade="10Gbps")  # Enlace de volta
    G.add_edge("a1", "e2", tipo_enlace="fibra óptica", capacidade="10Gbps")  # Enlace de volta

    G.add_edge("e3", "a2", tipo_enlace="fibra óptica", capacidade="10Gbps")
    G.add_edge("e4", "a2", tipo_enlace="fibra óptica", capacidade="10Gbps")
    G.add_edge("a2", "e3", tipo_enlace="fibra óptica", capacidade="10Gbps")  # Enlace de volta
    G.add_edge("a2", "e4", tipo_enlace="fibra óptica", capacidade="10Gbps")  # Enlace de volta

    # =========================
    # CONEXÕES ENTRE ROTEADORES DE AGREGAÇÃO E ROTEADOR CENTRAL
    # =========================

    G.add_edge("a1", "a0", tipo_enlace="fibra óptica", capacidade="40Gbps")
    G.add_edge("a2", "a0", tipo_enlace="fibra óptica", capacidade="40Gbps")
    G.add_edge("a0", "a1", tipo_enlace="fibra óptica", capacidade="40Gbps")  # Enlace de volta
    G.add_edge("a0", "a2", tipo_enlace="fibra óptica", capacidade="40Gbps")  # Enlace de volta

    return G
