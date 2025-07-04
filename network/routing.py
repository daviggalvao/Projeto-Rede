# network/routing.py

# Tabelas de roteamento por roteador
# Cada entrada: destino_em_forma_de_prefixo: próximo_salto
# Obs: usamos prefixo só como string simplificada, não CIDR real por enquanto.

tabelas_roteamento = {
    "a0": {
        "10.0.1.": "a1",  # h1 via a1->e1
        "10.0.2.": "a1",  # h3 e h4 via a1->e2
        "10.0.3.": "a2",  # h5 e h6 via a2->e3
        "10.0.4.": "a1",  # h3 e h4 via a1->e2
        "10.0.5.": "a2",  # h5 e h6 via a2->e3
        "10.0.6.": "a2",  # h5 e h6 via a2->e3
        "10.0.7.": "a2",  # h7 e h8 via a2->e4
        "10.0.8.": "a2",  # h7 e h8 via a2->e4
    },
    "a1": {
        "10.0.1.": "e1",  # h1 e h2 via e1
        "10.0.2.": "e2",  # h3 e h4 via e2
        "10.0.3.": "a0",  # h5 e h6 via a0->a2->e3
        "10.0.4.": "e2",  # h3 e h4 via e2
        "10.0.5.": "a0",  # h5 e h6 via a0->a2->e3
        "10.0.6.": "a0",  # h5 e h6 via a0->a2->e3
        "10.0.7.": "a0",  # h7 e h8 via a0->a2->e4
        "10.0.8.": "a0",  # h7 e h8 via a0->a2->e4
    },
    "a2": {
        "10.0.1.": "a0",  # h1 e h2 via a0->a1->e1
        "10.0.2.": "a0",  # h3 e h4 via a0->a1->e2
        "10.0.3.": "e3",  # h5 e h6 via e3
        "10.0.4.": "a0",  # h3 e h4 via a0->a1->e2
        "10.0.5.": "e3",  # h5 e h6 via e3
        "10.0.6.": "e3",  # h5 e h6 via e3
        "10.0.7.": "e4",  # h7 e h8 via e4
        "10.0.8.": "e4",  # h7 e h8 via e4
    }
}

def proximo_salto(roteador, destino_ip):
    """
    Dado um roteador e o IP de destino, retorna o próximo salto segundo a tabela estática.
    """
    if roteador not in tabelas_roteamento:
        return None

    for prefixo, saida in tabelas_roteamento[roteador].items():
        if destino_ip.startswith(prefixo):
            return saida

    return None
