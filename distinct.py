def distinct(arr): 
    
    n = len(arr)
    dist = []
    
    for i in range(0, n): 
  
        d = 0
        for j in range(0, i): 
            if (arr[i] == arr[j]): 
                d = 1
                break
  
        if (d == 0): 
            dist.append(arr[i]) 
    
    return dist


elementos = [1,0,2,8,2,1,1,3] 
print( distinct(elementos) )