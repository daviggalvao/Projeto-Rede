import argparse
import sys
from network.topology import construir_topologia
from network.simulator import xping, xtraceroute, listar_hosts

def interface_interativa(grafo):
    """Interface interativa para o simulador de rede."""
    print("\n===== SIMULADOR DE REDE =====")
    hosts_disponiveis = listar_hosts(grafo)
    print("\nHosts disponíveis:", ", ".join(hosts_disponiveis))
    
    while True:
        print("\nOpções:")
        print("1. Executar xping")
        print("2. Executar xtraceroute")
        print("3. Sair")
        
        escolha = input("\nEscolha uma opção (1-3): ")
        
        if escolha.lower() == 'sair' or escolha == '3':
            print("Encerrando simulador...")
            break
        
        if escolha == '1' or escolha == '2':
            origem = input("Host de origem: ")
            if origem.lower() == 'sair':
                break
            
            if origem not in hosts_disponiveis:
                print(f"Erro: Host '{origem}' não existe na rede!")
                continue
            
            destino = input("Host de destino: ")
            if destino.lower() == 'sair':
                break
            
            if destino not in hosts_disponiveis:
                print(f"Erro: Host '{destino}' não existe na rede!")
                continue
            
            if escolha == '1':
                xping(grafo, origem, destino)
            else:
                xtraceroute(grafo, origem, destino)
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

def main():
    # Configuração dos argumentos de linha de comando
    parser = argparse.ArgumentParser(description='Simulador de Rede')
    parser.add_argument('-i', '--interativo', action='store_true', 
                        help='Executar em modo interativo')
    parser.add_argument('-p', '--ping', nargs=2, metavar=('ORIGEM', 'DESTINO'),
                        help='Executar xping de ORIGEM para DESTINO')
    parser.add_argument('-t', '--traceroute', nargs=2, metavar=('ORIGEM', 'DESTINO'),
                        help='Executar xtraceroute de ORIGEM para DESTINO')
    
    args = parser.parse_args()
    
    # Monta a rede como grafo
    G = construir_topologia()
    
    # Modo de execução baseado nos argumentos
    if args.interativo:
        interface_interativa(G)
    elif args.ping:
        xping(G, args.ping[0], args.ping[1])
    elif args.traceroute:
        xtraceroute(G, args.traceroute[0], args.traceroute[1])
    else:
        # Sem argumentos, executa o modo interativo
        interface_interativa(G)

if __name__ == "__main__":
    main()
