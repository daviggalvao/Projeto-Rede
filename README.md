# Simulador de Rede Hierárquica

Este repositório contém o código-fonte para o projeto da disciplina de Redes de Computadores, do Departamento de Ciência da Computação da Universidade de Brasília (UnB).

## 🎯 Objetivo do Projeto

O objetivo deste projeto é aprofundar os conceitos das camadas de rede e de enlace através do projeto e da simulação de uma rede com topologia em árvore, comum em data centers.

## ✨ Funcionalidades Implementadas

O simulador foi desenvolvido em Python e permite a execução dos seguintes comandos sobre uma topologia de rede customizada:

* **`xping`**: Testa a conectividade entre dois hosts na rede simulada. 
* **`xtraceroute`**: Mostra a rota (sequência de roteadores) que um pacote percorre entre um host de origem e um de destino. 

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Bibliotecas:** NetworkX (para a implementação do grafo da rede)

## 🚀 Como Executar o Projeto

<details>
  <summary>Clique para expandir os passos de configuração e execução</summary>
  <br>

### **Pré-requisitos**

-   Python 3.9 ou superior
-   Gerenciador de pacotes `pip` (geralmente incluído com Python)
-   Um IDE ou editor de texto de sua preferência (VS Code, PyCharm, etc.)

---

### **Passos para Configuração e Execução**

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/daviggalvao/Projeto-Rede.git
    cd Projeto-Rede
    ```

2.  **Instale as Dependências:**
    * O projeto requer a biblioteca `NetworkX`. Instale-a via `pip`:
        ```bash
        pip install networkx
        ```

3.  **Execute o Simulador:**
    * Com as dependências instaladas, execute o script principal para iniciar o programa:
        ```bash
        python3 main.py
        ```

4.  **Utilize o Simulador:**
    * Ao ser executado, o programa apresentará um menu interativo.
    * Você deve primeiro escolher a operação desejada (1 para `xping`, 2 para `xtraceroute`) e, em seguida, fornecer os hosts de origem e destino quando solicitado.
    
    * **Exemplo de uma sessão de uso:**
        ```text
        ===== SIMULADOR DE REDE =====

        Hosts disponíveis: h1, h2, h3, h4, h5, h6, h7, h8, h9, h10

        Opções:
        1. Executar xping
        2. Executar xtraceroute
        3. Sair

        Escolha uma opção (1-3): 1
        Digite o host de origem: h1
        Digite o host de destino: h10

        [XPING] De h1 para h10
        Pacote entregue com sucesso!
        Caminho: h1 → e1 → a1 → Core → a2 → e4 → h10
        Número de saltos: 6
        Latência (RTT) simulada: 140ms

        ===== SIMULADOR DE REDE =====
        (O menu é exibido novamente para a próxima operação)
        Escolha uma opção (1-3): 3
        Encerrando o simulador.
        ```
</details>

## 👥 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<br>

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/daviggalvao">
        <img src="https://github.com/daviggalvao.png?size=100" width="100px;" alt="Foto de Davi Galvão"/>
        <br />
        <sub>
          <b>daviggalvao</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/toninhobc">
        <img src="https://github.com/toninhobc.png?size=100" width="100px;" alt="Foto de Antonio Carlos"/>
        <br />
        <sub>
          <b>toninhobc</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Leo3107">
        <img src="https://github.com/Leo3107.png?size=100" width="100px;" alt="Foto de Leonardo"/>
        <br />
        <sub>
          <b>Leo3107</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
