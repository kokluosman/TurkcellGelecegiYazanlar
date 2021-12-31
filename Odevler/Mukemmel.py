


def Mukemmel(x):
    toplam = 0
    for i in range(1,x+1):
        if (x % i) == 0:
            toplam = toplam+i
        else:
            None
    if toplam == x : 
        return True
    else:
        return False    
    
    
print(Mukemmel(6))



