# 经典计算机
# 练习函数、异常处理、菜单。
# 核心功能：加减乘除，支持连续计算，处理除零错误。

def add(x,y):
    return x+y
def delete(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide (x,y):
    if y == 0:
        raise ValueError("除数不能为零")
    return x/y

def calculator():
    
    
    return