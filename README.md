# 8-puzzle
Programa criado para a tarefa de busca no problema 8-puzzle na disciplina de IA - UFF

Para solução da tarefa foi utilizado como base o código [eightpuzzle.py](http://www-inst.eecs.berkeley.edu/~cs188/sp07/assignments/assignment2/eightpuzzle.py) provido pelo item 1.B do seguinte exercício:

<http://www-inst.eecs.berkeley.edu/~cs188/sp07/assignments/assignment2/sp07-assignment%202.html>

O exercício fornece as classes básicas com partes em branco para implementação dos métodos de busca.

O objetivo é implementar uma busca que movimente o espaço vazio(representado pelo 0) do puzzle até chegar no estado meta, representado abaixo:

       -------------
       | 1 | 2 | 3 |
       -------------
       | 8 | 0 | 4 |
       -------------
       | 7 | 6 | 5 |
       -------------

# Executando o programa

1.Abrir o arqivo main.py em um editor.

2.Selecionar o puzzle a ser resolvido com o seguinte comando:

  puzz = puzzle.loadEightPuzzle(0)

O parâmetro seleciona um dos seguintes quebra-cabeças que estão definidos no arquivo puzzle.py:

~~~
  EIGHT_PUZZLE_DATA = [[1, 2, 3, 8, 4, 0, 7, 6, 5],  
                       [1, 2, 3, 8, 4, 5, 7, 0, 6], 
                       [1, 2, 3, 8, 4, 5, 0, 7, 6], 
                       [5, 4, 3, 6, 1, 8, 7, 0, 2]]
~~~

O parâmetro 0 no exemplo acima seleciona o primeiro quebra-cabeças [1, 2, 3, 8, 4, 0, 7, 6, 5].

OBS: Repare que o quarto quebra cabeças está no espaço de busca inacessível considerando o estado meta, ver:
[Reachable state space of an 8-puzzle](http://cs.stackexchange.com/questions/16515/reachable-state-space-of-an-8-puzzle)

3.Para selecionar o tipo de busca, basta tirar o comentário da linha correspondete a busca que se quer fazer, no exemplo abaixo está selecionada a busca Manhattan:

~~~
# Seleciona o tipo de busca
#s = search.BreadthFirstSearchAgent() #BFS
#s = search.AStarSearchAgent(puzzle.misplacedTiles) #Heuristic Misplace Tiles
s = search.AStarSearchAgent(puzzle.manhattanDistance) #Heuristic Manhattan Distance
~~~