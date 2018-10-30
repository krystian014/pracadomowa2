a=input("wprowadz liczbe: ")
a=int(a)
try:
    if a%2==0:
        raise ValueError ("Liczba jest podzielna przez 2")
    if a<0:
        raise TypeError ("Liczba mniejsza od 0")
    if a>10:
        raise IndexError ("Liczba wieksza od 10")
    
except ValueError as e:
    print (e)


except TypeError as f:
    print (f)

except IndexError as g:
    print (g)
    
    
