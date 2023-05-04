# Experimentos de otimização e redes neurais
Olá, leitor! Nessa pasta, você encontra todos os experimentos de redes neurais realizados por mim, Isabela Beneti, na disciplina de Redes Neurais e Algorítmos Genéticos (RNAG). Para saber mais sobre eles, você pode acessar os notebooks, ou clicar nos subtópicos abaixo:
<details><summary><b>Primeira aula: Conceitos Básicos</b></summary>

Pelas palavras do professor, essa foi a aula mais importante de todo o nosso ano na disciplina de Redes Neuras e Algoritmos Genéticos!

Nela, nós aprendemos que, assim como algoritmos genéticos, são códigos inspirados em biologia, mais especificamente no funcionamento de neurônios biológicos. Os principais conceitos inspirados no funcionamento dos neurônios são os de:

* Conexão
* Passagem de sinal
* Função de Ativação

Podemos representar o esquema de uma rede neural simples pelo grafo abaixo:

<center>
  <img src= 'https://user-images.githubusercontent.com/106626661/234957554-3fb1db49-c7e4-4db8-9539-907c56d55b32.png' style="width:800px;height:400px"/>
</center>  


No grafo, os círculos com x são neurônios artificiais de input (ou de saída)), o círculo com y é o neurônio artificial de output(ou de saída), o círculo central é o neurônio artificial da camada oculta e as setas são sinapses artificiais.

As informações caminham nas sinapses artificiais, e toda sinapse tem um peso, que será multiplicado com o valor do input. Se o valor de input é $U$ , a informação transportada será $U*w_1$.

No neurônio central, temos um valor inerente $b$ (bias, ou viés) e uma função $g(x)$. A informação que ele recebe é a de $U * w_1 + T* w_2$ à qual ele soma com o valor b. Portanto, o que esse neurônio retorna é $g(U* w_1 + T* w_2+ b)$.

Logo, o neurônio de saída ($y$) receberá o valor de $g(U* w_1 + T* w_2+ b) * w_3$



## Backpropagation

Qualquer função pode ser representada por grafos! Por exemplo, as expressões $c= a + b$ e $e= c * d$ podem ser representadas por meio do grafo da figura 2:




Logo, podemos também representar a nossa rede neural simples, da figura 2, utilizando o grafo da figura 3:

<center>
  <img src= 'https://user-images.githubusercontent.com/106626661/234977331-b8bef9c4-8552-493a-b057-0239aaad51f7.png' style="width:800px;height:400px"/>
</center>  




A grande sacada das redes neurais foi feita pelo austríaco Linnainmaa: utilizar derivadas para sabermos o quanto cada parâmetro influencia no resultado! Afinal, a derivada mostra a variação, isto é , mostra o quanto a função está mudando em uma determinada direção. Logo, utilizando derivadas parciais, é possível descobrir o quanto y varia quando mudamos os parâmetros  $w_3$, $w_1$, $w_2$, $b$...

Se sabemos o quanto y varia conforme eu vario cada um desses parâmetros, eu podemos o quanto eu devo mudar esses parâmetros para chegar ao valor ideal de y. Essas derivadas parciais são chamadas de `Gradientes Locais do Parâmetro`. As primeiras derivadas parciais (mais próximas de y) podem ser calculadas de maneira mais direta. Conforme vamos retrocedendo nos parâmetros, é necessário ir aplicando a regra da cadeia para calcular a derivada, assim como mostra a figura 4:

<center>
  <img src= 'https://user-images.githubusercontent.com/106626661/234975100-d3bbd464-cedd-43f1-aa36-5f08d25c64c3.png' style="width:1000px;height:500px"/>
</center>  


Esse o método de ir calculando as derivadas de frente para trás é chamado de `backpropagation`. Isso é a base para vários modelos muuuito importantes, como o nosso querido ChatGPT! 



</details>
<details><summary><b>Experimento R.01</b></summary>

À espera da aula 2 para completar esse tópico :)
</p>
</details>

</details>
<details><summary><b>Experimento R.02</b></summary>

Nesse experimento, fomos introduzidos à estrutura de classes em Python, que junta ação e informação,. Ela é uma estrutura de dados muito poderosa, mas também muito complexa também.

Funções definidas dentro de classes são chamadas de `método`. O que não é função dentro da classe é chamada de `propriedade`. Para chamar o método, basta colocar um ponto final e o nome do método.
</p>
</details>

</details>
<details><summary><b>Experimento R.03</b></summary>

À espera da aula 2 para completar esse tópico :)
</p>
</details>
