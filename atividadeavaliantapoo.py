# Allef Braz , Isaías Marques
class Poligono: 
    def __init__(self,numerolados):
        self.numerolados = numerolados

    def getnumerolados(self):
        return self.numerolados
    
    def setnumerolados(self,numerolados):
        self.numerolados = numerolados

    def calcularperimetro(self):
        soma = 0
        for i in range(self.numerolados):
            lado = float(input("Digite o valor do lado: "))
            soma = soma + lado

        print(f"O perímetro do polígono é: {soma}")
        return soma
    
class testarpoligono:
    def main():
        num = int(input("Digite o número de lados do polígono: "))
        p = Poligono(num)
        p.calcularperimetro()
        novo = int(input("Digite o novo número de lados: "))
        p.setnumerolados(novo)
        p.calcularperimetro()
testarpoligono.main()