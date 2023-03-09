 # Resolução do problema proposto
# Escolhermos usar uma LISTA para representar o indivíduo
# Quantidade de elementos na lista é o número de genes do indivíduo
# Genes podem receber valores de 0 ou 1, gerados aleatoriamente

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

    
