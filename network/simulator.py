# network/simulator.py
from network.routing import proximo_salto

def listar_hosts(grafo):
    """Retorna uma lista dos hosts disponíveis na rede, ordenada numericamente."""
    hosts = [no for no, attr in grafo.nodes(data=True) if attr.get('tipo') == 'host']
    return sorted(hosts, key=lambda host_name: int(host_name[1:]))

def buscar_ip(grafo, no):
    """Retorna o IP do nó na rede."""
    return grafo.nodes[no].get("ip") if no in grafo.nodes else None

def encontrar_caminho(grafo, origem, destino):
    """
    Simula o roteamento para encontrar o caminho do pacote.
    Retorna uma tupla: (caminho, mensagem_de_erro)
    """
    if origem not in grafo:
        return None, f"Host de origem '{origem}' não existe na rede!"
    if destino not in grafo:
        return None, f"Host de destino '{destino}' não existe na rede!"

    caminho = [origem]
    atual = origem
    destino_ip = buscar_ip(grafo, destino)
    
    # Conjunto para detectar loops
    visitados = {origem}
    
    while atual != destino:
        # O primeiro salto de um host é sempre para seu gateway (o único vizinho "para cima")
        if grafo.nodes[atual]['tipo'] == 'host' and atual == origem:
            # Encontra o único vizinho que não é um host (ou seja, o switch)
            proximo_no = next((v for v in grafo.successors(atual) if grafo.nodes[v]['tipo'] != 'host'), None)
        else: # Para switches e roteadores, consulta a lógica de roteamento
            proximo_no = proximo_salto(grafo, atual, destino_ip)

        if proximo_no is None:
            return None, f"Não há rota definida a partir de '{atual}' para o destino '{destino}'"

        # Detecção de Loop
        if proximo_no in visitados:
            caminho.append(proximo_no) # Adiciona o nó para mostrar onde o loop aconteceu
            return None, f"Loop de roteamento detectado em '{proximo_no}'. O caminho até agora era: {' -> '.join(caminho)}"

        caminho.append(proximo_no)
        visitados.add(proximo_no)
        atual = proximo_no

    return caminho, None

def xping(grafo, origem, destino):
    """Executa a simulação de ping e exibe as estatísticas, incluindo latência."""
    print(f"\n[XPING] De {origem} para {destino}")
    
    caminho, erro = encontrar_caminho(grafo, origem, destino)
    
    if erro:
        print(f"Falha: {erro}")
        return

    if caminho:
        latencia_ida = 0
        for i in range(len(caminho) - 1):
            no_atual = caminho[i]
            proximo_no = caminho[i+1]
            latencia_enlace = grafo.edges[no_atual, proximo_no].get('latencia', 0)
            latencia_ida += latencia_enlace
        
        rtt_simulado = latencia_ida * 2

        print(f"Pacote entregue com sucesso!")
        print(f"Caminho: {' → '.join(caminho)}")
        print(f"Número de saltos: {len(caminho) - 1}")
        print(f"Latência (RTT) simulada: {rtt_simulado}ms")

def xtraceroute(grafo, origem, destino):
    """Executa a simulação de traceroute."""
    print(f"\n[XTRACEROUTE] Rastreando rota de {origem} até {destino}")

    caminho, erro = encontrar_caminho(grafo, origem, destino)

    if erro:
        print(f"Falha: {erro}")
        return

    if caminho:
        for i, hop in enumerate(caminho):
            ip_hop = buscar_ip(grafo, hop)
            print(f"Salto {i}: {hop} (IP: {ip_hop})")
        print(f"Total de saltos: {len(caminho) - 1}")