# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # Conjunto dos nós já expandidos
    expandidos = set()
    
    # Pilha usada para a DFS
    fronteira = util.Stack()
    
    estadoInicial = problem.getStartState()
    
    # Inicia a fronteira com o estado inicial e a lista de ações vazia
    fronteira.push((estadoInicial, []))

    # Enquanto existir nós na fronteira
    while not fronteira.isEmpty():
        # Obtém e remove o próximo nó da fronteira
        proximoEstado, acoes = fronteira.pop()

        # Se o nó obtido é um estado objetivo
        if problem.isGoalState(proximoEstado):
            # Retorna as ações tomadas para chegar ao objetivo
            return acoes
        
        # Se o nó obtido já foi expandido, ele é ignorado
        if proximoEstado in expandidos:
            continue
        
        # Coloca o nó obtido no conjunto dos nós expandidos
        expandidos.add(proximoEstado)

        # Expande o nó
        sucessores = problem.getSuccessors(proximoEstado)

        # Itera pelos sucessores do nó
        for (sucessor, acao, custo) in sucessores:
            # Se o sucessor não foi expandido ainda
            if sucessor not in expandidos:
                # Adiciona a ação para mover do nó atual para o sucessor
                novasAcoes = acoes + [acao]

                # Coloca o sucessor na fronteira, com as ações tomadas para alcançá-lo
                fronteira.push((sucessor, novasAcoes.copy()))
        
    # Caso não encontrou o estado objetivo na busca, não realiza nenhuma ação
    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # Conjunto dos nós já expandidos
    expandidos = set()
    
    # Fila usada para a BFS
    fronteira = util.Queue()
    
    estadoInicial = problem.getStartState()
    
    # Inicia a fronteira com o estado inicial e a lista de ações vazia
    fronteira.push((estadoInicial, []))
    # Enquanto existir nós na fronteira
    while not fronteira.isEmpty():
        # Obtém e remove o próximo nó da fronteira
        proximoEstado, acoes = fronteira.pop()

        # Se o nó obtido é um estado objetivo
        if problem.isGoalState(proximoEstado):
            # Retorna as ações tomadas para chegar ao objetivo
            return acoes
        
        # Se o nó obtido já foi expandido, ele é ignorado
        if proximoEstado in expandidos:
            continue
        
        # Coloca o nó obtido no conjunto dos nós expandidos
        expandidos.add(proximoEstado)

        # Expande o nó
        sucessores = problem.getSuccessors(proximoEstado)

        # Itera pelos sucessores do nó
        for (sucessor, acao, custo) in sucessores:
            # Se o sucessor não foi expandido ainda
            if sucessor not in expandidos:
                # Adiciona a ação para mover do nó atual para o sucessor
                novasAcoes = acoes + [acao]

                # Coloca o sucessor na fronteira, com as ações tomadas para alcançá-lo
                fronteira.push((sucessor, novasAcoes.copy()))
        
    # Caso não encontrou o estado objetivo na busca, não realiza nenhuma ação
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # Importa a biblioteca de matemática para ter acesso à constante inf
    import math

    # Dicionário do custo para ir do nó inicial aos nós expandidos
    custos = dict()
    
    # Conjunto dos nós expandidos
    expandidos = set()
    
    # Fila de prioridade usada na UCS
    fronteira = util.PriorityQueue()
    
    estadoInicial = problem.getStartState()
    
    # Inicia a fronteira com o estado inicial, custo 0 e a lista de ações vazia
    fronteira.push((estadoInicial, []), 0)

    # Inicia o dicionário dos custos para o estado inicial com 0
    custos[estadoInicial] = 0

    # Enquanto existe nós na fronteira
    while not fronteira.isEmpty():
        # Obtém e remove o próximo nó da fronteira
        proximoEstado, acoes = fronteira.pop()
        
        # Se o nó obtido é o objetivo
        if problem.isGoalState(proximoEstado):
            # Retorna as ações tomadas para alcançá-lo
            return acoes
        
        # Se o nó obtido já foi expandido, o ignora
        if proximoEstado in expandidos:
            continue
        
        # Adiciona o nó obtido ao conjunto dos nós expandidos
        expandidos.add(proximoEstado)

        # Obtém os sucessores do nó
        sucessores = problem.getSuccessors(proximoEstado)

        # Itera pelos sucessores do nó
        for (sucessor, acao, custo) in sucessores:
            # Se o sucessor não foi expandido e o custo para alcançá-lo até o momento é maior do que o
            # custo de ir do nó inicial até o nó atual somado do custo de ir do nó atual até o sucessor
            if sucessor not in expandidos and custos.get(sucessor, math.inf) > custos.get(proximoEstado, math.inf) + custo:
                # Atualiza o novo menor custo de alcançar o sucessor a partir do nó inicial
                custos[sucessor] = custos.get(proximoEstado, math.inf) + custo

                # Acrescenta a ação tomada para alcançá-lo
                novasAcoes = acoes + [acao]

                # Coloca o sucessor na fronteira, com seu novo custo e lista de ações tomadas
                fronteira.push((sucessor, novasAcoes.copy()), custos[sucessor])
    
    # Caso não encontrou o estado objetivo na busca, não realiza nenhuma ação
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def greedySearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest heuristic first."""
    # Conjunto dos nós expandidos
    expandidos = set()

    # Fila de prioridade usada na GS
    fronteira = util.PriorityQueue()

    estadoInicial = problem.getStartState()

    # Inicia a fronteira com o estado inicial, custo igual a sua heurística
    # e a lista de ações vazia
    fronteira.push((estadoInicial, []), heuristic(estadoInicial, problem))

    # Enquanto existe nós na fronteira
    while not fronteira.isEmpty():
        # Obtém e remove o próximo nó da fronteira
        proximoEstado, acoes = fronteira.pop()

         # Se o nó obtido é o objetivo
        if problem.isGoalState(proximoEstado):
            # Retorna as ações tomadas para alcançá-lo
            return acoes
        
        # Se o nó obtido já foi expandido, o ignora
        if proximoEstado in expandidos:
            continue

        # Adiciona o nó obtido ao conjunto dos nós expandidos
        expandidos.add(proximoEstado)

        # Obtém os sucessores do nó
        sucessores = problem.getSuccessors(proximoEstado)

        # Itera pelos sucessores do nó
        for (sucessor, acao, custo) in sucessores:

            # Se o sucessor não foi expandido
            if sucessor not in expandidos:
                # Acrescenta a ação tomada para alcançá-lo
                novasAcoes = acoes + [acao]

                # Coloca o sucessor na fronteira, com seu custo igual ao valor da 
                # heurística para ele e com a lista de ações tomadas
                fronteira.push((sucessor, novasAcoes.copy()), heuristic(sucessor, problem))
                
    # Caso não encontrou o estado objetivo na busca, não realiza nenhuma ação
    return []


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    # Importa a biblioteca de matemática para ter acesso à constante inf
    import math
    
    # Dicionário do custo para ir do nó inicial aos nós expandidos
    custos = dict()
    
    # Conjunto dos nós expandidos
    expandidos = set()
    
    # Fila de prioridade usada na UCS
    fronteira = util.PriorityQueue()
    
    estadoInicial = problem.getStartState()

    # Inicia a fronteira com o estado inicial, custo igual a sua heurística
    # e a lista de ações vazia
    fronteira.push((estadoInicial, []), heuristic(estadoInicial, problem))

    # Inicia o dicionário dos custos para o estado inicial com 0
    custos[estadoInicial] = 0

    # Enquanto existe nós na fronteira
    while not fronteira.isEmpty():
        # Obtém e remove o próximo nó da fronteira
        proximoEstado, acoes = fronteira.pop()

        # Se o nó obtido é o objetivo
        if problem.isGoalState(proximoEstado):
            # Retorna as ações tomadas para alcançá-lo
            return acoes
        
        # Se o nó obtido já foi expandido, o ignora
        if proximoEstado in expandidos:
            continue

        # Adiciona o nó obtido ao conjunto dos nós expandidos
        expandidos.add(proximoEstado)

        # Obtém os sucessores do nó
        sucessores = problem.getSuccessors(proximoEstado)

        # Itera pelos sucessores do nó
        for (sucessor, acao, custo) in sucessores:

            # Se o sucessor não foi expandido e o custo para alcançá-lo até o momento é maior do que o
            # custo de ir do nó inicial até o nó atual somado do custo de ir do nó atual até o sucessor
            if sucessor not in expandidos and custos.get(sucessor, math.inf) > custos.get(proximoEstado, math.inf) + custo:

                # Atualiza o novo menor custo de alcançar o sucessor a partir do nó inicial
                custos[sucessor] = custos.get(proximoEstado, math.inf) + custo

                # Acrescenta a ação tomada para alcançá-lo
                novasAcoes = acoes + [acao]

                # Coloca o sucessor na fronteira, com seu novo custo somado à sua heurística
                # e com a lista de ações tomadas
                fronteira.push((sucessor, novasAcoes.copy()), custos[sucessor]+heuristic(sucessor, problem))
    
    # Caso não encontrou o estado objetivo na busca, não realiza nenhuma ação
    return []


def foodHeuristic(state, problem):
    """
    Your heuristic for the FoodSearchProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come
    up with an admissible heuristic; almost all admissible heuristics will be
    consistent as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the
    other hand, inadmissible or inconsistent heuristics may find optimal
    solutions, so be careful.

    The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a Grid
    (see game.py) of either True or False. You can call foodGrid.asList() to get
    a list of food coordinates instead.

    If you want access to info like walls, capsules, etc., you can query the
    problem.  For example, problem.walls gives you a Grid of where the walls
    are.

    If you want to *store* information to be reused in other calls to the
    heuristic, there is a dictionary called problem.heuristicInfo that you can
    use. For example, if you only want to count the walls once and store that
    value, try: problem.heuristicInfo['wallCount'] = problem.walls.count()
    Subsequent calls to this heuristic can access
    problem.heuristicInfo['wallCount']
    """
    import math
    paredes = problem.walls.asList()

    # Função para calcular o custo do pacman andar entre dois pontos do labirinto
    # Cálculo feito usando bfs e considerando o custo de mover entre dois pontos
    # adjacentes válidos como 1
    def distanciaReal(inicial, destino):
        # Se algum dos pontos é uma parede
        if inicial in paredes or destino in paredes:
            return math.inf
        
        # BFS para encontrar o custo de andar entre os dois pontos
        # Conjunto dos nós expandidos
        expandidos = set()
        # Fila usada na BFS
        fronteira = util.Queue()
        # Inicializa a fronteira com o ponto inicial
        fronteira.push((inicial, 0))
        # Enquanto existir nós na fronteira
        while not fronteira.isEmpty():
            # Obtém e remove o próximo nó da fronteira
            proximoEstado, custo = fronteira.pop()
            # Se o nó obtido é o destino
            if proximoEstado == destino:
                # Retorna o custo de alcançá-lo
                return custo
            # Se o nó já foi expandido, o ignora
            if proximoEstado in expandidos:
                continue
            # Adiciona o nó no conjunto dos nós expandidos
            expandidos.add(proximoEstado)
            # Determina quais pontos são válidos para o pacman visitar
            # Expansão do nó atual, já que os pontos válidos são seus
            # sucessores
            for direcao in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                potencialVizinho = (proximoEstado[0]+direcao[0], proximoEstado[1]+direcao[1])
                # Se o vizinho não é uma parede
                if potencialVizinho not in paredes:
                    # Se o vizinho já não foi expandido
                    if potencialVizinho not in expandidos:
                        # Adiciona o vizinho na fronteira
                        fronteira.push((potencialVizinho, custo+1))

        # Se o destino nunca é alcançado, o custo é infinito
        return math.inf

    # Salva as distâncias já calculadas para evitar recálculo
    dicionarioDistancias = {}

    # Busca o dicionário de outras instâncias da heurística
    if 'distancias' in problem.heuristicInfo:
        dicionarioDistancias = problem.heuristicInfo['distancias']

    posicao, foodGrid = state

    # Obtém a lista das posições das comidas
    posicoesComidas = foodGrid.asList()

    # Inicialmente, o custo 0 é colocado, como elemento neutro para o max
    valores = [0]

    # Itera pelas posições das comidas
    for posicaoComida in posicoesComidas:
        # Se distância entre a posição do pacman e da comida ainda não foi calculada, 
        # calcula essa distância e salva no dicionário
        if (posicao, posicaoComida) not in dicionarioDistancias:
            dicionarioDistancias[(posicao, posicaoComida)] = distanciaReal(posicao, posicaoComida)
        # Busca custo do pacman andar até a comida
        custoQuaseReal = dicionarioDistancias[(posicao, posicaoComida)]
        valores.append(custoQuaseReal)

    # Salva o dicionário gerado para outras instâncias da heurística
    problem.heuristicInfo['distancias'] = dicionarioDistancias

    # Retorna a maior distância encontrada como valor da heurística
    # Se não existe comida, esse retorno é 0
    return max(valores)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
ucs = uniformCostSearch
gs = greedySearch
astar = aStarSearch
