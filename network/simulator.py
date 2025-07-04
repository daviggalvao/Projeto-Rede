from network.routing import proximo_salto

def listar_hosts(grafo):
    """Retorna uma lista dos hosts disponíveis na rede."""
    return sorted([no for no, attr in grafo.nodes(data=True) 
                  if attr.get('tipo') == 'host'])

def buscar_ip(grafo, no):
    """Retorna o IP do nó na rede."""
    return grafo.nodes[no]["ip"] if no in grafo.nodes else None

def encontrar_caminho(grafo, origem, destino):
    """
    Simula o roteamento baseado nas tabelas estáticas (routing.py).
    Retorna o caminho completo como lista de nós, ou None se não houver rota.
    """
    caminho = [origem]
    atual = origem
    destino_ip = buscar_ip(grafo, destino)

    if destino_ip is None:
        return None

    # Para evitar loops infinitos
    visitados = set([origem])
    
    while atual != destino:
        vizinhos = list(grafo.successors(atual))

        # Se o destino é um vizinho direto, podemos ir direto para ele
        if destino in vizinhos:
            caminho.append(destino)
            break

        if grafo.nodes[atual]["tipo"] == "roteador":
            # Roteadores usam tabelas de roteamento
            saida = proximo_salto(atual, destino_ip)
            if saida is None or saida not in vizinhos:
                return None
            caminho.append(saida)
            atual = saida
        elif grafo.nodes[atual]["tipo"] == "switch":
            # Switches em redes locais precisam decidir para onde encaminhar
            # Verifica se algum dos vizinhos é um roteador ou outro switch (preferência para roteadores)
            roteadores = [v for v in vizinhos if v not in visitados and grafo.nodes[v]["tipo"] == "roteador"]
            switches = [v for v in vizinhos if v not in visitados and grafo.nodes[v]["tipo"] == "switch"]
            
            if roteadores:
                # Prefere encaminhar para um roteador
                proximo = roteadores[0]
                caminho.append(proximo)
                atual = proximo
            elif switches:
                # Senão, encaminha para outro switch
                proximo = switches[0]
                caminho.append(proximo)
                atual = proximo
            else:
                # Se não há para onde ir, falha
                return None
        elif len(vizinhos) == 1 and vizinhos[0] not in visitados:
            # Host com um único caminho
            atual = vizinhos[0]
            caminho.append(atual)
        else:
            # Não tem para onde ir
            return None
            
        # Marca como visitado para evitar loops
        visitados.add(atual)
        
        # Evita loops infinitos
        if len(caminho) > 10:  # Limite arbitrário para evitar loops
            return None

    return caminho

def xping(grafo, origem, destino):
    print(f"[XPING] De {origem} para {destino}")
    caminho = encontrar_caminho(grafo, origem, destino)
    if caminho:
        print(f"Pacote entregue com sucesso!")
        print(f"Caminho: {' → '.join(caminho)}")
        print(f"Número de saltos: {len(caminho) - 1}")
    else:
        print("Falha: não há caminho válido baseado nas tabelas de roteamento.")

def xtraceroute(grafo, origem, destino):
    print(f"[XTRACEROUTE] Rastreando rota de {origem} até {destino}")
    caminho = encontrar_caminho(grafo, origem, destino)
    if caminho:
        for i, hop in enumerate(caminho):
            print(f"Salto {i}: {hop}")
        print(f"Total de saltos: {len(caminho) - 1}")
    else:
        print("Falha: rota não encontrada com base nas tabelas.")
