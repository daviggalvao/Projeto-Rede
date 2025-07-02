# network/routing.py

# Tabelas de roteamento por roteador
# Cada entrada: destino_em_forma_de_prefixo: próximo_salto
# Obs: usamos prefixo só como string simplificada, não CIDR real por enquanto.

tabelas_roteamento = {
    "a0": {
        "10.0.1.": "a1",
        "10.0.2.": "a1",
        "10.0.3.": "a2",
        "10.0.4.": "a1",  # Correção: 10.0.4.x está conectado a e2 que está em a1
    },
    "a1": {
        "10.0.1.": "e1",
        "10.0.2.": "e2",
        "10.0.3.": "a0",  # Rota para rede 10.0.3.x via a0
        "10.0.4.": "e2",  # Correção: 10.0.4.x está conectado a e2
    },
    "a2": {
        "10.0.3.": "e3",
        "10.0.4.": "a0",  # Correção: 10.0.4.x via a0
        "10.0.1.": "a0",  # Rota para rede 10.0.1.x via a0
        "10.0.2.": "a0",  # Rota para rede 10.0.2.x via a0
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
