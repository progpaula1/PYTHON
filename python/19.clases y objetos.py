class Casa:

    def __init__(self, color):
        self.color = color
        self.consumo_de_luz = 0
        self.consumo_de_agua = 0

    def pintar(self, color):
        self.color = color 

    def prender_luz(self):
        self.consumo_de_luz +=10
        
    def abrir_ducha(self):
        self.consumo_de_agua += 10


    def tocar_timbre(self):
        print("RRRIIIIIIIIING")
        self.consumo_de_luz += 2 
        
class Mansion(Casa):
    def prender_luz(self):
        self.consumo_de_luz +=50
    
    def abrir_ducha(self):
        self.consumo_de_agua += 50
    
    def tocar_timbre(self):
        print("DING DONG")
        self.consumo_de_luz +=3
        
mi_mansion = Mansion ("blanco")   
print (mi_mansion.color)

mi_mansion.pintar("verde")
print(mi_mansion.color)
