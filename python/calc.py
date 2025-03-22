class Calculadora:
    def __init__(self):
        self
    
    def soma(sef, num, num2):
        tot = num + num2
        return print(tot)
    
    def sub(self, num, num2):
        tot = num - num2
        return print(tot)
    
    def multi(self, num, num2):
        tot = num * num2
        return print(tot)
    
    def div(self, num, num2):
        tot = num / num2
        return print(tot)
    
calc = Calculadora()
print("------------------------------------------------")
print("      E S C O L H A  U M A  O P Ç Ã O")

while True:
    print("1 - soma  2 - sub  3 - multi  4 - div")
    deci = int(input(""))
    if deci == 0:
        break
    nums = int(input("digite o primeiro num"))
    nums2 = int(input("digite o segundo"))
    match deci:
        case 1:
            calc.soma(nums, nums2)
        case 2:
            calc.sub(nums, nums2)
        case 3:
            calc.multi(nums, nums2)
        case 4:
            calc.div(nums, nums2)


