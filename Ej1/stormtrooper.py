class Stormtrooper:
    def __init__(self,nombre,rango):
        self.nombre = nombre
        self.rango = rango
        
        print("soldado creado con éxito")

    def calificaciones(self,codigo):
        self.codigo_legion = codigo[:2]
        self.id_cohoerte = codigo[3:4]
        self.id_siglo = codigo[4:5]
        self.id_escuadra = codigo[5:6]
        self.id_trooper = codigo[6:7]