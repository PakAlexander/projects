# put your python code here
def fun(val):
    if val % 2 == 0:
        return True
    return False


while (val := int(input())) != 1:
    if fun(val):
        print(val)