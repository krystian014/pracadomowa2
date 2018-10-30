mylist=[1,2,3,4,5]
print (mylist)

a=input("Który element chcesz wybrac? ")
a=int(a)
try:
    if a>(len(mylist)-1):
        raise IndexError ("Nie ma takiego indeksu")
    if a<0:
        raise IndexError ("Nie ma takiego indeksu")    

except IndexError as g:
    print (g)

else:
    print(mylist[a])

