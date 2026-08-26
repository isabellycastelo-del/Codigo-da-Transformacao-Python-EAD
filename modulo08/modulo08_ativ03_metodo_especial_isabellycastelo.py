#class adicionada para mostrar a marca e o modelo do carro, mostrando as informações na tela.
class Carro:
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

#class criada para mostrar a informação do carro como marca, 
class CarroEletrico(Carro):
    def __init__(self, marca, modelo, autonomia_bateria):
        super().__init__(marca, modelo)
        self.autonomia = autonomia_bateria


    def exibir_info(self):
        info_base = super().exibir_info()
        return f"{info_base} | Autonomia da Bateria: {self.autonomia} km"

meu_carro = CarroEletrico("Cadillac", "Deville", 600)
print(meu_carro.exibir_info())