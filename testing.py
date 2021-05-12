test = None 

def my_func(): 
    global test 
    test = [1,2,3]
    return test 
    
my_func()
print(test)