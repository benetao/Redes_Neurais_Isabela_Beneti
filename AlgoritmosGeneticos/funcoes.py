## Bem vindo ao arquivo "funcoes"! Aqui armazenamos as funções que desenvolvemos ao longo dos experimentos
# As funções estão divididas em "setores", que dizem respeito a em qual experimento ela foi inicialmente desenvolvida.

import random

###############################################################################
#                             Experimento 1                                   #
###############################################################################

def gene_cb(): 
    """ Função que gera um gene válido (0 ou 1) para o problema das caixas binárias 
    
    Retorna valor 0 ou 1"""
    lista= [0,1]
    gene= random.choice(lista)
    return gene

def individuo_cb(n):
    """ Função que gera um indivíduo válido para o problema das caixas binárias
    
    Argumentos: n= número de genes do indivíduo
    
    Retorna lista com n genes. Cada gene é um valor de 0 ou 1"""
    
    individuo=[]
    for i in range(n):
        gene= gene_cb()
        individuo.append(gene)
    return individuo

def funcao_objetivo_cb(individuo):
    """ Computa a fução objetiva no problema das caixas binárias
    
    Argumentos: lista contendo genes das caixas binárias
    
    Retorna o valor da soma dos genes do indivíduo"""
    return sum(individuo)


###############################################################################
#                             Experimento 3                                   #
###############################################################################

    
def populacao_cb(tamanho, n):
    """ Cria uma população no problema das caixas binárias
    
    Argumentos: n= número de genes
    tamanho= tamanho da população (número de indivíduos)
    
    Retorna: uma lista onde cada lista é um indivíduo. Um indivíduo é uma lista com genes"""
    populacao=[]
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao

def selecao_roleta_max(populacao, fitness):
    """Seleciona Indivíduos de uma população usando o método da roleta. Apenas funciona para problemas de maximização.
    
    Argumentos: populacao= lista com todos os indivíduos da população
    fitness= valor da função objetivo dos indivíduos da população
    
    Retorna: população dos indivíduos selecionados """
    populacao_selecionada= random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada

def cruzamento_ponto_simples(pai, mae):
   
    
    ponto_de_corte= random.randint(1, len(pai)-1 )
    
    filho1= pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2= mae[:ponto_de_corte] + pai [ponto_de_corte:]
    
    return filho1,filho2

def mutacao_cb(individuo):
    """ Realiza a mutação de um gene no problema das caixas binárias
    
    Argumento: indivíduo= lista que representa individuo no problema das caixas binárias

    
    Retorna: indivíduo com um gene mutado.
    
    """
    gene_a_ser_mutado= random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado]= gene_cb()
    return individuo





def funcao_objetivo_pop_cb(populacao):
    """Calcula a função objetivo para todos os membros de uma população
    
    
    Argumentos: populacao= lista com todos os indivíduos da população
    
    Retorna: lista de valores representando a fitness de cada indivíduo da população"""
    fitness=[]
    for individuo in populacao:
        fobj= funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    return fitness

def populacao_cnb(tamanho, n_genes, valor_max_caixa):
    """Cria uma população no problema das caixas não-binárias.
    
    Argumentos: tamanho= tamanho da população.
      n_genes= número de genes do indivíduo.
      valor_max_caixa= maior número inteiro possível dentro de uma caixa
      
    Retorna: lista em que cada item é um indiviuo. Um individuo é uma lista com
      `n_genes` genes.
    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cnb(n_genes, valor_max_caixa))
    return populacao

###############################################################################
#                             Experimento 4                                   #
###############################################################################


def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    
    Argumentos
      tamanho= tamanho da população.
      tamanho_senha= inteiro representando o tamanho da senha.
      letras= letras possíveis de serem sorteadas.
      
    Retorna:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao


def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio. Só funciona em problemas de
    minimização.
    
    Argumentos: populacao= população do problema
      fun_objetivo= função objetivo
      tamanho_torneio= quantidade de invidiuos que batalham entre si
    
    Retorna: individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness:
                selecionado = individuo
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados


# NOVIDADE
def mutacao_cnb(individuo, valor_max_caixa):
    """Realiza a mutação de um gene no problema das caixas não-binárias
    Argumentos: individuo= lista que representa individuo no problema das caixas não-binárias
      valor_max_caixa= maior número inteiro possível dentro de uma caixa
    Return:
      Um individuo com um gene mutado.
    """
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo


# NOVIDADE
def mutacao_senha(individuo, letras):
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo


# NOVIDADE
def funcao_objetivo_cnb(individuo):
    """Computa a função objetivo no problema das caixas não-binárias.
    Args:
      individiuo: lista contendo os genes das caixas não-binárias
    Return:
      Um valor representando a soma dos genes do individuo.
    """
    return sum(individuo)


# NOVIDADE
def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))

    return diferenca


# NOVIDADE
def funcao_objetivo_pop_cnb(populacao):
    """Calcula a funcao objetivo para todos os membros de uma população
    Args:
      populacao: lista com todos os individuos da população
    Return:
      Lista de valores represestando a fitness de cada individuo da população.
    """
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cnb(individuo)
        fitness.append(fobj)
    return fitness


# NOVIDADE
def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado

# NOVIDADE
def individuo_cnb(n_genes, valor_max_caixa):
    """Gera um individuo para o problema das caixas não-binárias.
    Args:
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa
    Return:
       Uma lista com n genes. Cada gene é um valor entre zero e
       `valor_max_caixa`.
    """
    individuo = []
    for i in range(n_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo


# NOVIDADE
def gene_cnb(valor_max_caixa):
    """Gera um gene válido para o problema das caixas não-binárias
    Args:
      valor_max_caixa: número inteiro representando o maior valor possível que
      pode existir dentro de uma caixa.
    Return:
      Um valor entre zero a `valor_max_caixa` (inclusive).
    """
    gene = random.randint(0, valor_max_caixa)
    return gene

def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato


def gene_letra(letras):
    """Sorteia uma letra.
    Args:
      letras: letras possíveis de serem sorteadas.
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra