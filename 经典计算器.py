# 经典计算机
# 练习函数、异常处理、菜单。
# 核心功能：加减乘除√，支持连续计算√，处理除零错误√。

def add(x,y):
    return x+y
def delete(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        raise ValueError("除数不能为零")
    return x/y

def calculator():
    result = 0
    print("Welcome welcome welcome, this is a REALLY simple calculator! So let's go!")

    while True:
        try:
            num1 = float(input("Please enter the FIRST number: "))
            num2 = float(input("Please enter the SECOND number: "))
            print("q.Add w.Delete e.Multiply r.Divide other.Quit \n What do you want to do bro?")
            chioce = input()
            match chioce:
                case "q":
                    result = add(num1,num2)
                    print(f"{num1} + {num2} = {result}")
                case "w":
                    result = delete(num1,num2)
                    print(f"{num1} - {num2} = {result}")
                case "e":
                    result = multiply(num1,num2)
                    print(f"{num1} * {num2} = {result}")
                case "r":
                    result = divide(num1,num2)
                    print(f"{num1} / {num2} = {result}")
                case _:
                    print("Goodbye! See you next time!")
                    break

            print("Do you want to continue calculating with the result? (y/n)")
            cont = input()
            if cont.lower() == 'y':   
                while True:                
                    nextNum = float(input("Please enter the next number: "))
                    print("q.Add w.Delete e.Multiply r.Divide other.Quit \n What do you want to do bro?")
                    chioce = input()
                    match chioce:
                        case "q":
                            print(f"{result} + {nextNum} = {add(result,nextNum)}")
                            result = add(result,nextNum)
                        case "w":
                            print(f"{result} - {nextNum} = {delete(result,nextNum)}")    
                            result = delete(result,nextNum)
                        case "e":
                            print(f"{result} * {nextNum} = {multiply(result,nextNum)}")
                            result = multiply(result,nextNum)
                        case "r":
                            print(f"{result} / {nextNum} = {divide(result,nextNum)}")
                            result = divide(result,nextNum)
                        case _:
                            print("Let's start a new calculation!")
                            break
            elif cont.lower() == 'n':
                print("OK，let's start a new calculation!")
                continue
            else:
                print("MANBA OUT! All clear! You stupid idiot, We are done!")
                break
            
        except ValueError as e:
            print(f"Pls input the fuking number, you fucking idiot! Error: {e} \n Let's start a new calculation!")
            continue

    return

if __name__ == "__main__": 
    calculator()