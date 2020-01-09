# bomberman-simulation

Aplicação desenvolvida em Python para simular o estado de um grid retangular de Bomberman após
uma quantidade de segundos definida pelo usuário.

**Execução**

Para rodar a aplicação por meio da imagem docker, utilize o comando abaixo:

    sudo docker run -it lucasmacedose/bomberman-simulation:latest

Caso já possua Python em sua máquina e deseje utilizá-lo para rodar a aplicação, primeiramente
clone este repositório, então abra o terminal na pasta e execute o seguinte comando:

    python main.py
    
*Observação*: A aplicação foi desenvolvida para Python 2 e pode não funcionar corretamente com outras versões.

**Detalhes de implementação**

A seguir, serão listadas as classes do programa juntamente com seus detalhes de implementação.

  - **Constantes**: Responsável por manter as constantes de como são representadas as bombas, obstáculos e pontos vazios no grid.

  - **Posicao**: Foi criada uma classe Posicao. Esta classe representa qualquer celula do grid, possuindo como atributos
    a linha e coluna de seu posicionamento, seu tipo (podendo ser Bomba, Obstáculo ou Vazio) e o momento em que a instância
    foi criada.
    
  - **Grid**: Responsável por gerenciar o grid do bomberman e orquestrar os eventos que nele ocorrem. Armazena como atributos
    o total de segundos a serem simulados, o segundo atual, uma lista de posições (instâncias de Posicao) e uma lista de bombas
    (também instâncias de Posicao).

O fluxo se segue da seguinte forma: o arquivo main obtém os dados do usuário como as posições dos itens no grid e a quantidade de
segundos a serem simulados e cria assim uma instância de Grid. Sobre este grid é chamado o método passar_segundos informando a quantidade de
segundos para realizar a simulação. A cada segundo simulado, a lista de bombas é percorrida e é chamado o método explodir sobre as que foram implantadas
há 3 segundos. Além disto, se o segundo atual for par, o grid será preenchido com bombas nas posições vazias.
