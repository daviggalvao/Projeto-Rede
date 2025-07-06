# network/routing.py
import ipaddress

# ==============================================================================
# TABELAS DE ROTEAMENTO FINAIS E DEFINITIVAS
# ==============================================================================
ROUTING_TABLES = {
    # Switches de borda têm apenas uma rota padrão "para cima".
    'e1': [{'destination': '0.0.0.0/0', 'next_hop': 'a1'}],
    'e2': [{'destination': '0.0.0.0/0', 'next_hop': 'a1'}],
    'e3': [{'destination': '0.0.0.0/0', 'next_hop': 'a2'}],
    'e4': [{'destination': '0.0.0.0/0', 'next_hop': 'a2'}],
    
    # Roteadores de agregação conhecem as redes dos switches abaixo deles
    # e têm uma rota padrão "para cima". A ordem é crucial: rotas específicas primeiro.
    'a1': [
        # Rotas específicas "para baixo":
        {'destination': '10.0.1.0/24', 'next_hop': 'e1'},
        {'destination': '10.0.2.0/24', 'next_hop': 'e1'},
        {'destination': '10.0.3.0/24', 'next_hop': 'e1'},
        {'destination': '10.0.4.0/24', 'next_hop': 'e2'},
        {'destination': '10.0.5.0/24', 'next_hop': 'e2'},
        {'destination': '10.0.6.0/24', 'next_hop': 'e2'},
        # Rota padrão "para cima":
        {'destination': '0.0.0.0/0', 'next_hop': 'Core'}
    ],
    'a2': [
        # Rotas específicas "para baixo":
        {'destination': '10.0.7.0/24', 'next_hop': 'e3'},
        {'destination': '10.0.8.0/24', 'next_hop': 'e3'},
        {'destination': '10.0.9.0/24', 'next_hop': 'e4'},
        {'destination': '10.0.10.0/24', 'next_hop': 'e4'},
        # Rota padrão "para cima":
        {'destination': '0.0.0.0/0', 'next_hop': 'Core'}
    ],

    # O Core conhece todas as sub-redes e para qual roteador de agregação encaminhar.
    'Core': [
        # Sub-redes sob a1
        {'destination': '10.0.1.0/24', 'next_hop': 'a1'},
        {'destination': '10.0.2.0/24', 'next_hop': 'a1'},
        {'destination': '10.0.3.0/24', 'next_hop': 'a1'},
        {'destination': '10.0.4.0/24', 'next_hop': 'a1'},
        {'destination': '10.0.5.0/24', 'next_hop': 'a1'},
        {'destination': '10.0.6.0/24', 'next_hop': 'a1'},

        # Sub-redes sob a2
        {'destination': '10.0.7.0/24', 'next_hop': 'a2'},
        {'destination': '10.0.8.0/24', 'next_hop': 'a2'},
        {'destination': '10.0.9.0/24', 'next_hop': 'a2'},
        {'destination': '10.0.10.0/24', 'next_hop': 'a2'},
    ]
}

# --- O RESTANTE DO ARQUIVO PERMANECE IGUAL ---

def ip_in_subnet(ip_addr, subnet):
    """Verifica se uma string de IP pertence a uma string de sub-rede CIDR."""
    try:
        return ipaddress.ip_address(ip_addr) in ipaddress.ip_network(subnet)
    except (ValueError, TypeError):
        return False

def proximo_salto(grafo, no_atual, ip_destino):
    """
    Determina o próximo salto para um pacote com base na lógica de roteamento correta.
    """
    node_data = grafo.nodes[no_atual]
    
    if node_data['tipo'] == 'switch':
        for vizinho in grafo.successors(no_atual):
            vizinho_data = grafo.nodes[vizinho]
            if vizinho_data.get('tipo') == 'host' and vizinho_data.get('ip') == ip_destino:
                return vizinho
        
        tabela = ROUTING_TABLES.get(no_atual, [])
        if tabela:
            return tabela[0]['next_hop']

    elif node_data['tipo'] == 'roteador':
        tabela = ROUTING_TABLES.get(no_atual, [])
        for rota in tabela:
            subnet = rota['destination']
            if ip_in_subnet(ip_destino, subnet):
                return rota['next_hop']

    return None