def my_function(glue=":",*args):
    ciag=""
    for arg in args:
        ciag=ciag+arg+glue
        
    print(ciag)
    
my_function(":","pies","kot","dom","auto")
