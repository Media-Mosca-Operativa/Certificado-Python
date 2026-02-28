class Area:
    #Funcion iniciadora
    def __init__(self, i, x): #__init__ es un constructor que inicia los parametros
        self.i = i # Atributos de instancia
        self.x = x # Atributos de instancia

    def funcion(self):
        print(f"Se pasan {self.i}, al {self.x}.")

# Es posible crear varias instancias de una clase        
Objetos = Area("parametros", "constructor")
# Llamada a la función
Objetos.funcion() 

""" 
|--------------------------------------------|
|----METODOS @classmethod & @staticmethod----|
|--------------------------------------------|
"""
class Diferencia:
    
    metodo = "de clase"
    
    @classmethod
    def clase(cls):
        return cls.metodo
    
    def __init__(self, tipo):
        self.tipo = tipo
        
    @staticmethod
    def estatico(tipo):
        print(f"Metodo {tipo}")
        
Diferencia.estatico("estatico")

print("Metodo", Diferencia.clase())

