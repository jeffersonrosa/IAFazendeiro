# Problema do Fazendeiro, Cachorro, Galinha e Milho

## Descrição do Problema

Um fazendeiro precisa cruzar um rio com um cachorro, uma galinha e um saco de milho. Ele tem um barco que só pode transportar ele mesmo e um de seus itens por vez. Existem regras específicas a serem seguidas para garantir que nenhum item seja prejudicado:

- O cachorro não pode ser deixado sozinho com a galinha (o cachorro comerá a galinha).
- A galinha não pode ser deixada sozinha com o milho (a galinha comerá o milho).

O objetivo é descobrir uma sequência de movimentos que permita ao fazendeiro cruzar o rio com todos intactos.

## Como Funciona

O script utiliza a inteligência artificial para simular e resolver o problema. A abordagem usada é uma busca em largura para explorar todas as possíveis combinações de movimentos e verificar se eles são seguros.

### Algoritmo de Busca

O algoritmo de busca usado é a busca em largura. É uma estratégia de busca cega que explora sistematicamente todos os movimentos em uma ordem específica. Neste caso, o algoritmo explora todos os movimentos possíveis do fazendeiro e suas compras até encontrar uma solução.

A principal vantagem é que ela sempre encontrará a solução mais curta (se houver uma), pois explora todas as possíveis sequências de movimentos em ordem.

### Inteligência Artificial no Script

A IA é aplicada de duas maneiras principais neste script:

1. **Representação do Estado**: O estado atual do problema é representado como um dicionário em Python, onde as chaves são as entidades (fazendeiro, cachorro, galinha, milho) e os valores são suas posições atuais (esquerda ou direita do rio).

2. **Expansão do Estado**: O script gera todos os movimentos possíveis a partir de um estado atual. Ele verifica se o fazendeiro pode se mover sozinho ou com uma das entidades e, em seguida, verifica se o movimento resultante é seguro. Se for seguro, o estado é adicionado à lista de estados a serem explorados.

O algoritmo continua a expandir e explorar os estados até que encontre uma sequência de movimentos que leve todas as entidades com segurança para o outro lado do rio.

---

## Saída
O programa irá imprimir a sequência de movimentos que o fazendeiro deve fazer para cruzar o rio com sucesso sem violar as regras nesse formato:

### Saída Formatada
```
O caminho completo é:
1 - Esquerda [Fazendeiro, Galinha, Cachorro, Milho] - Rio - [] Direita
2 - Esquerda [Cachorro, Milho] - Rio - [Fazendeiro, Galinha] Direita
3 - Esquerda [Fazendeiro, Cachorro, Milho] - Rio - [Galinha] Direita
4 - Esquerda [Milho] - Rio - [Fazendeiro, Galinha, Cachorro] Direita
5 - Esquerda [Fazendeiro, Galinha, Milho] - Rio - [Cachorro] Direita
6 - Esquerda [Galinha] - Rio - [Fazendeiro, Cachorro, Milho] Direita
7 - Esquerda [Fazendeiro, Galinha] - Rio - [Cachorro, Milho] Direita
8 - Esquerda [] - Rio - [Fazendeiro, Galinha, Cachorro, Milho] Direita
```

## Autor
- **Nome**: Jefferson Rosa
- **Github**: [jeffersonrosa](https://github.com/jeffersonrosa)
- **Email**: jeffersonrosabr@gmail.com
