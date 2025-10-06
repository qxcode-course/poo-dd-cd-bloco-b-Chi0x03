class Camisa:
    def __init__(self):
        self.__tamanho: str = ""
    
    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, tamanho: str):
        if tamanho != "PP" \
            and tamanho != "P" \
            and tamanho != "M" \
            and tamanho != "G" \
            and tamanho != "GG" \
            and tamanho != "XG":
            print("fail: tamanho errado")
            return
        
        self.__tamanho = tamanho

# loop principal
camisa = Camisa() # criando camisa com valor tamanho padrão

while camisa.getTamanho() == "": # mantendo usuário no loop
    print("Digite seu tamanho de camisa")
    tamanho = input() # lendo a resposta
    camisa.setTamanho(tamanho) # tentando atribuir e disparando erros

print("Parabens, você comprou uma camisa tamanho", camisa.getTamanho())