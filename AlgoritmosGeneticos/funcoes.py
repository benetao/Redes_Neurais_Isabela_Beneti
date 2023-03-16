 # Resolução do problema proposto
# Escolhermos usar uma LISTA para representar o indivíduo
# Quantidade de elementos na lista é o número de genes do indivíduo
# Genes podem receber valores de 0 ou 1, gerados aleatoriamente
import random
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

    
def populacao_cb(tamanho, n):
    """ Cria uma população no problema das caixas binárias
    
    Argumentos: n= número de genes
    tamanho= tamanho da população (número de indivíduos)
    
    Retorna uma lista onde cada lista é um indivíduo. Um indivíduo é uma lista com genes"""
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