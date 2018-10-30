def my_function(napis,flaga=True):
    napis=str(napis)
    if flaga==True:
        print(napis.upper())
    if flaga==False:
        print(napis.lower())

my_function("Test")
my_function("Test", True)
my_function("Test",False)
    
