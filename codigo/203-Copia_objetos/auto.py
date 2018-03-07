class Auto:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __eq__(self, obj):
        return self.marca == obj.marca and self.modelo == obj.modelo and self.año == obj.año

    def __str__(self):
        return "Marca: {}\nModelo: {}\nAño: {}".format(self.marca, self.modelo, self.año)