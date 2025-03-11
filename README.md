 
<div>

  <h1>Sistema de Grafos em Python e algoritmos de buscas</h1>
</div>



<div>

  <h2>Grafos</h2>
</div>



<div>
  <h2>Algoritmos de Buscas</h2>
  
  <div id="deepth_search">
    <h3>Busca em Profundidade</h3>
    <p>
      Esse algortimo tem a função de visitar todos os nós do grafo sempre indo em direção ao ultimo nivel. <br>
      É necessário começar de um nó inicial, o algoritmo vai escolher um dos vizinhos não-visitado do nó inicial e vai mover-se até ele. Esse processo vai se repetir recursivamente, indo o mais profundo possivel. Quando um nó não tiver mais vizinhos não-visitado, o algoritmo volta para o nó anterior para tentar outro caminho.<br>
     Para utilizar esse algoritmo será necessário a estrutura de dados Pilha, sempre que o algoritmo visitar um nó será adicionado ao topo da pilha, assim que todos os vizinhos desse nó for visitado, o algoritmo remove o topo da pilha.</p>
      <img src="https://github.com/user-attachments/assets/981387f5-70cc-4c8b-9bee-80df147acfda">
    <br>
  </div>


  <div id="breadth_search">
      <h3>Busca em Largura</h3>
      <p>
        O algoritmo de busca em largura irá percorrer todos os nós do grafo em um nível antes de mover-se para o proximo             nível. Também é necessário começar por um nó incial, a partir dele é explorados os seus vizinhos e em seguida é explorado os vizinhos dos vizinhos, e assim por diante, seguindo por níveis de profundidade. Difrente da Busca em Profundidade que utiliza uma Pilha como estrutura de dados, a Busca em Largura utiliza uma Fila para explorar os nós
      </p>
      <img src="https://github.com/user-attachments/assets/0b892be6-2c0d-410c-a874-f782b25b956f">

  </div>
  
  
</div>

