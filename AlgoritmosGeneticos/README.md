# Experimentos de otimização e algoritmos genéticos
Olá, leitor! Nessa pasta, você encontra todos os experimentos realizados por mim, Isabela Beneti, na disciplina de Redes Neurais e Algorítmos Genéticos (RNAG). Para saber mais sobre eles, você pode acessar os notebooks, ou clicar nos subtópicos abaixo:
<details><summary><b>Experimento A0.1</b></summary>


O primeiro experimento, resolvido no notebook "experimento A.01" foi resolvido em classe utilizando python puro, isto é, apenas python e as bibliotecas já embutidas no JupyterNotebook. Nele, nós resolvemos o problema de **4 caixas binárias** utilizando o método de **busca aleatória**. Para tanto, escrevemos 3 funções que, ao final, devolviam uma resposta diferente a cada vez que rodávamos a célula


Logo, concluímos que o método de busca aleatória é **probabilístico**, e não determinístico.

  
ATUALIZAÇÃO 16/03: ao invés de definirmos as funções nesse notebook, transferimo-nas para o arquivo "funcoes.py" e importamo-nas
  
</details>
<details><summary><b>Experimento A0.2</b></summary>


No segundo experimento,  resolvemos o problema de **caixas binárias** utilizando o método de **busca em grade**. Para tanto, importamos uma função entre as funções escritas no experimento A.01. A partir desse método, conseguimos analisar todas os indivíduos (candidatos) possíveis, e, por isso, o código sempre nos retornava a mesma resposta.

Logo, concluímos que o método de busca em grade **determinístico**, e não probabilístico .
</p>
</details>
<details><summary><b>Experimento A0.3</b></summary>


Na segunda aula de Redes Neurais e Algorítmos genéticos, desenvolvemos o nosso primeiro **algorítmo genético**, com o intuito de resolver o nosso problema das **caixas binárias**, seguindo o mesmo modelo dos outros experimentos.

No experimento 3, concluímos que o método de algorítimos genéticos é **probabilístico**, pois depende de fatores aleatórios, incluindo constantes como a chance de mutação e de cruzamento, que, inclusive, podem determinar quão boa será a sua resposta.

</details>
<details><summary><b>Experimento A0.4</b></summary>


Na aula do dia 23/03/2023, ministrada pelo nosso querido professor e colega [João Pedro Brito](https://github.com/jpab2004), nós desenvolvemos um **algorítmo genético** para resolver o problema das caixas **NÃO binárias**. O código é muito parecido com o do experimento anterior, mudando apenas o valor dos genes que, ao invés de variarem entre 0 e 1, podem ir de 0 a 100 (incluindo 100).  Por isso, mudamos não só a função que cria genes, como também a que cria indivíduos, populações e as duas funções relacionadas a função objetivo. Tudo isso foi implementado no documento "funcoes.py".

Nesse experimento, ao mudarmos o valor das constantes de busca, ficou mais claro qual o impacto de cada uma delas na eficiência do código.

Ao aumentarmos a chance de mutação por exemplo, o código tende a dar resultados melores até um DETERMINADO PONTO, pois, se a aumentarmos demais, as mutações começarão a ser numerosas demais, resultando num código pouco eficiente. O mesmo vale para a redução excessiva dessa constante. Por isso, é bom fazer testes com esse valor para definir o melhor valor para essa constante.

No entanto, é sempre bom relembrar que esse algorítimo é **probabilístico**, e não determinístico. Por isso, mesmo mudando as constantes, nós estaremos lidando com  fatores aleatórios (de sorte)!

</details>
<details><summary><b>Experimento A0.5</b></summary>


Agora, temos um problema um pouco mais complexo, que foge do padrão das caixas binárias: precisamos descobrir uma senha, ou, pelo menos, chegar o mais próximo possível dela, sempre quantificando o quão perto um indivíduo está da resposta.  (através da função objetivo, ou fitness).

Para tanto utilizamos algoritmo genético cuja função objetivo transforma a string da senha em um vetor, e cada letra da senha corresponde a um número dentro desse vetor. Para saber quão distante um canditato está da senha que deve ser descoberta, faz-se a subtração desses vetores: quanto **menor** o valor dessa subtração, melhor o candidato! Por isso, podemos classificar esse problema como um problema de **minimização**.

Como conclusão desse experimento, pudemos perceber natureza customizável dos algoritmos genéticos. Afinal, podemos mudar várias partes do código para que ele retorne resultados melhores e mais rápido, como, por exemplo, na função de mutação, tomar em conta as distâncias entre palavras para todas as letras, e não só letra por letra. 
</details>


<details><summary><b>Experimento GA0.6</b></summary>
Esse experimento foi totalmente desenvolvido por mim, utilizando apenas algumas das funções e códigos já desenvolvidos nas aulas anteriores. Nele, escrevi um algoritmo genético que calcula o mínimo global da função de Himmelblau, uma função que possui 4 mínimos locais e que é geralmente usada como um problema de teste para algoritmos de otimização. A fórmula dessa função é dada por $f(x,y)= (x² + y - 11)² + (x+ y²- 7)²$ e seu gráfico, em 3 dimensões, é:

<div align="center">
      <img src="https://user-images.githubusercontent.com/106626661/230447980-5a84ec1c-eb23-4f45-9b2e-ea0488479c0b.png" alt="Logo" width="560" height="440">
  </a>

Para resolver esse problema por meio de algoritmos genéticos, é necessário pensar o que eu consideraria como: `Gene`, `Indivíduo`, `Função objetivo`, `Mutação`, `Seleção`, `Cruzamento`.

Os `genes` serão valores de x e de y em um determinado intervalo de números. Logo, em cada `ìndivíduo` há dois genes apenas, cada um representando uma coordenada do ponto.

O que buscamos, no problema, é o ponto de menor valor da função em um determinado intervalo. Logo, a `função objetivo` deve retornar a projeção de cada ponto (indivíduo) na função $f(x,y)= (x² + y - 11)² + (x+ y²- 7)²$. Por fim, como é uma função de minimização, utilizaremos a mesma seleção utilizada no experimento 0.6 das senhas, assim como as mesmas funções de `mutação` e de `cruzamento`.



</details>
<details><summary><b>funcoes.py</b></summary>
  

Nesse documento, armazenamos funções criandas nos notebooks, o que diminui o risco de perdê-las e facilita o nosso acesso a elas. Dessa forma, criamos a nossa própria biblioteca de funções! As funções estão divididas em "setores", que dizem respeito a em qual experimento ela foi inicialmente desenvolvida.

</details>
