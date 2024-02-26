# global scope
my_global = 10

def fn1():
    enclosed_V = 8
    def fn2():
    
        local_v = 5
        print('Access to Global', my_global)
        print('Access to Enclosed', enclosed_V)
    
    fn2()
    
fn1()

print('................................................................')



#  Enclosing scope
def get_totals(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    #double variable will not be accessible
    # print(double)

    return total

print('................................................................')

#  Global scope


special = 5

def get_all(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_itt():
        #local variable
        double = total * 2
        return double
        print(special)

       

    double_itt()

    return total

get_all(3, 56)    

print('................................................................')
# Local scope

def get_total(a, b):
    #local variable declared inside a function
    total = a + b;
    return total

print(get_total(5, 9))


# Accessing variable outside of the function:
print(total)
# NameError: name 'total' is not defined

