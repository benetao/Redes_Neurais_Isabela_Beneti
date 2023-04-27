# Experimentos de otimização e redes neurais
Olá, leitor! Nessa pasta, você encontra todos os experimentos de redes neurais realizados por mim, Isabela Beneti, na disciplina de Redes Neurais e Algorítmos Genéticos (RNAG). Para saber mais sobre eles, você pode acessar os notebooks, ou clicar nos subtópicos abaixo:
<details><summary><b>Primeira aula: Conceitos Básicos</b></summary>

Pelas palavras do professor, essa foi a aula mais importante de todo o nosso ano!

Nela, nós aprendemos que, assim como algoritmos genéticos, são códigos inspirados em biologia, mais especificamente no funcionamento de neurônios biológicos. Os principais conceitos inspirados no funcionamento dos neurônios são os de:

* Conexão
* Passagem de sinal
* Função de Ativação

Podemos representar o esquema de uma rede neural simples pelo grafo abaixo:

<center>
  <img src= 'https://user-images.githubusercontent.com/106626661/234955474-93a2c0f5-4863-4c67-9dc8-54caa5d31407.png' style="width:800px;height:400px"/>
</center>  


No grafo, os círculos com x são neurônios artificiais de input (ou de saída)), os círculos com y são neurônios artificiais de output(ou de saída) e as setas são sinapses artificiais. As informações caminham nas sinapses artificiais, e toda sinapse tem um peso, que será multiplicado com o valor do input. Se o valor de input é $U$ , a informação transportada será $U*w_1$.

No neurônio central, temos um valor inerente $b$ (bias, ou viés) e uma função $g(x)$. A informação que ele recebe é a de $U * w_1 + T* w_2$ à qual ele soma com o valor b. Portanto, o que esse neurônio retorna é $g(U* w_1 + T* w_2+ b)$.

Logo, o neurônio de saída ($y$) receberá o valor de $g(U* w_1 + T* w_2+ b) * w_3$


</details>
<details><summary><b>Tópico 2</b></summary>

À espera da aula 2 para completar esse tópico :)
</p>
</details>
