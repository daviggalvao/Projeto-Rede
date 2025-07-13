import ipaddress

# =====================
# TABELAS DE ROTEAMENTO
# =====================

ROUTING_TABLES = {
    # Switches de borda têm uma rota padrão para seu roteador de agregação.
    'e1': [{'destination': '0.0.0.0/0', 'next_hop': 'a1'}],
    'e2': [{'destination': '0.0.0.0/0', 'next_hop': 'a1'}],
    'e3': [{'destination': '0.0.0.0/0', 'next_hop': 'a2'}],
    'e4': [{'destination': '0.0.0.0/0', 'next_hop': 'a2'}],

    # Roteadores de agregação conhecem as sub-redes "abaixo" e têm uma rota padrão "para cima".
    # A ordem é crucial: rotas mais específicas primeiro.
    'a1': [
        # Rotas para as sub-redes de borda
        {'destination': '192.168.0.0/27', 'next_hop': 'e1'},
        {'destination': '192.168.0.32/27', 'next_hop': 'e2'},
        # Rota padrão "para cima" para o Core
        {'destination': '0.0.0.0/0', 'next_hop': 'Core'}
    ],
    'a2': [
        # Rotas para as sub-redes de borda
        {'destination': '192.168.0.64/27', 'next_hop': 'e3'},
        {'destination': '192.168.0.96/27', 'next_hop': 'e4'},
        # Rota padrão "para cima" para o Core
        {'destination': '0.0.0.0/0', 'next_hop': 'Core'}
    ],

    # O Core conhece o caminho para todas as sub-redes através dos roteadores de agregação.
    'Core': [
        # Sub-redes acessíveis via a1
        {'destination': '192.168.0.0/27', 'next_hop': 'a1'},
        {'destination': '192.168.0.32/27', 'next_hop': 'a1'},
        # Sub-redes acessíveis via a2
        {'destination': '192.168.0.64/27', 'next_hop': 'a2'},
        {'destination': '192.168.0.96/27', 'next_hop': 'a2'},
    ]
}

def ip_in_subnet(ip_addr, subnet):
    # Verifica se uma string de IP pertence a uma string de sub-rede CIDR.
    try:
        return ipaddress.ip_address(ip_addr) in ipaddress.ip_network(subnet)
    except (ValueError, TypeError):
        return False

def proximo_salto(grafo, no_atual, ip_destino):
    # Determina o próximo salto para um pacote com base na lógica de roteamento correta.
    node_data = grafo.nodes[no_atual]
    
    # Se o nó atual for um switch, a lógica é um pouco diferente.
    if node_data['tipo'] == 'switch':
        # Primeiro, verifica se o destino é um host diretamente conectado.
        for vizinho in grafo.successors(no_atual):
            vizinho_data = grafo.nodes[vizinho]
            if vizinho_data.get('tipo') == 'host' and vizinho_data.get('ip') == ip_destino:
                return vizinho
        
        # Se não for um host local, usa a rota padrão (sempre a primeira e única rota para um switch).
        tabela = ROUTING_TABLES.get(no_atual, [])
        if tabela:
            return tabela[0]['next_hop']

    # Se o nó atual for um roteador, consulta sua tabela de roteamento.
    elif node_data['tipo'] == 'roteador':
        tabela = ROUTING_TABLES.get(no_atual, [])
        # Itera na tabela para encontrar a rota mais específica que corresponde ao destino.
        for rota in tabela:
            subnet = rota['destination']
            if ip_in_subnet(ip_destino, subnet):
                return rota['next_hop']

    # Se nenhuma rota for encontrada, retorna None.
    return None
