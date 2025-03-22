class Solution:
    def poli(self, x):
        if x < 0:
            return print("Diferente")
        
        lista = list(str(x))
        lista_R = lista[::-1]
        #verd = [False, True] #[True]*2
        verd = False
        for i, num in enumerate(lista):
            if lista[i] != lista_R[i]:
                verd = True

        if verd:
            return print("Diferente")
        else:
            return print("Igual")

v = Solution()
v.poli(1001001)