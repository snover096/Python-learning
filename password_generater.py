#密码生成器
#随机生成√ 重复生成√


import string 
import random
import time

def generate_password(length=8,upper=True,lower=True,digit=True,symbol=True):
    
    #定义一个密码池 默认
    characters = ''
    if upper: characters += string.ascii_uppercase
    if lower: characters += string.ascii_lowercase
    if digit: characters += string.digits
    if symbol: characters += string.punctuation
    #强制选择
    if not characters: 
        characters += string.ascii_lowercase

    #生成密码
    password = ''.join(random.choice(characters)for _ in range(length)) #random.choice(~)随机选择
    return password


def main():
    print("--------超级无敌牛逼plusMax密码生成系统--------")
    while True:
        length = input("~密码位数（默认8位）： ")
        if length.isdigit():
            length = int(length)
        elif length == '':
            length = 8
        else:
            print("~Input number pls")
            continue   
        print(f"~OK, we will make a {length} digits password for you. Default only have lower letter, if you want more options, please answer the following questions.")
        isUpper = input("~upper letter?(y/n): ").lower() == 'y'
        print("Yes") if isUpper else print("No")

        isLower = input("~lower letter?(y/n): ").lower() == 'y'
        print("Yes") if isLower else print("No")

        isDigit = input("~number?(y/n): ").lower() == 'y'
        print("Yes") if isDigit else print("No")
        
        isSymbol = input("symbol?(y/n): ").lower() == 'y'
        print("Yes") if isSymbol else print("No")
        print("\n~OK,we will make it at soon, hold on......")
        #生成密码
        password = generate_password(length,isUpper,isLower,isDigit,isSymbol)
        #模拟生成过程
        time.sleep(random.randint(1,3))
        print("\n"+ '='*30)
        print(f"Your password: {password}")
        print('='*30)
        #是否重复生成
        if  input("\n~Do you want to generate another password?(y/n)").lower() != 'y':
            print("~Bye! See you next time!")
            break
    return
#程序入口
if __name__ == "__main__":
    main()