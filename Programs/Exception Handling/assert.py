def ktf(t):
    assert(t>=0),"colder than absolute"
    return ((t-273)*18)+32
try:
    print(ktf(273))
    print(ktf(505.78))
    print(ktf(-5))
except(AssertionError):
    print("error occured")
            
