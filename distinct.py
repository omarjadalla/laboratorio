def distinct(arr): #cria a função
    
    n = len(arr) #tamanho do array
    dist = [] #lista para adicionar os elementos diferentes
    
    for i in range(0, n): #percorre um por um
  
        d = 0 #zera contador
        
        for j in range(0, i): #percorre um por um até a posição atual
            
            if (arr[i] == arr[j]):  #se for igual a algum
                d = 1  #incrementa o contador
                break  #sai do loop
            #fim do if
            
        #fim do for
        
        if (d == 0): #se contador for igual a zero
            dist.append(arr[i]) #adiciona a lista de diferentes
        #fim do if
    
    #fim do for    

    return dist #retorna a lista de diferentes
#fim da função

elementos = [1,0,2,'b',2,'b',1,3,0,0,2,0,1] #cria variavel com a lista de elementos repetidos 
print( distinct(elementos) ) #mostra na tela o retorno da função


# Usando not in
def unique(items):
    found = set([])
    keep = []

    for item in items:
        if item not in found:
            found.add(item)
            keep.append(item)

    return keep

print ( unique(elementos) )


#rodando online
#https://onlinegdb.com/SycomVEqX