# Global variable and Local variable

# URL: https://ide.geeksforgeeks.org/MgQJSImWEx

#code
x = 77

def rg():
    x = 20
    
    def hr():
        global x 
        x = 71
    print("before calling the hr: ",x)
    hr()
    print("after calling the hr: ",x)
    
rg()
print(x)


##OUTPUT
20
20
71
