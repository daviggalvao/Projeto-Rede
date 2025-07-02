tabelas_roteamento = {
    "a1": {
        "10.0.1.0/24": "s1",
        "10.0.2.0/24": "s2"
    }
}

def proximo_salto(origem, destino_ip):
    # Função simples que escolhe próximo salto com base na tabela do roteador
    if origem in tabelas_roteamento:
        for rede, saida in tabelas_roteamento[origem].items():
            if destino_ip.startswith(rede[:-3]):
                return saida
    return None
