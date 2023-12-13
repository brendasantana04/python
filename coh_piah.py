import re

def le_assinatura():
  '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
  print("Bem-vindo ao detector automático de COH-PIAH.")

  wal = float(input("Entre o tamanho medio de palavra:"))
  ttr = float(input("Entre a relação Type-Token:"))
  hlr = float(input("Entre a Razão Hapax Legomana:"))
  sal = float(input("Entre o tamanho médio de sentença:"))
  sac = float(input("Entre a complexidade média da sentença:"))
  pal = float(input("Entre o tamanho medio de frase:"))

  return [wal, ttr, hlr, sal, sac, pal]
  
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
        
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    S = 0
    for i in range (0, 6):
        S = S+ (abs(as_a[i] - as_b[i]))
    grau = S/6
    if grau < 0:
        grau = grau * (-1)
    return grau
    pass

def calcula_assinatura(texto):
    lp = separa_palavras(texto)
    ntp = len(lp)

    tp = 0
    for i in range (ntp):
        tp = tp + len(lp[i]) 
        
    tmp = tp/ntp
    type_token = n_palavras_diferentes(texto)/ntp
    hapax_legomana = n_palavras_unicas(texto)/ntp
    
    ts = len(separa_sentencas(texto))
    tf = len(separa_frases(texto))
    
    tms = tp/ts
    cs = tf/ts
    tmf = tp/tf

    assinatura = [tmp, type_token, hapax_legomana, tms, cs, tmf]

    return assinatura
    
    pass

def avalia_textos(textos, ass_cp):
    i = 1
    asst = calcula_assinatura(textos[i]) 
    gs = compara_assinatura(asst, ass_cp)
                                                                           
    mg = gs  
    ti = i   
    i = i+1
    while i <(len (textos)): 
        asst = calcula_assinatura(textos[i])
        gs = compara_assinatura(asst, ass_cp) 
        if gs < mg:  
            mg = gs  
            ti = i             
        i = i+1
                  
    print ("O autor do texto %d está infectado com COH-PIAH" %(ti))
    return ti
    pass

def main():
    asscp = le_assinatura()
    txtl = le_textos() 
    avalia_textos(txtl, asscp) 

main()