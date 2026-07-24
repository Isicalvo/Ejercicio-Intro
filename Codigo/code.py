# Rellenar con el código solución
class monstruo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.magia = 100

    def __str__(self):
        return f"RAAAWR, soy {self.nombre}"

    def luchar(self, nivel_ataque, tipo_ataque):
        nivel_contra = nivel_ataque + 1
        if (nivel_contra >= self.magia):
            self.magia -= nivel_contra
        else:
             nivel_contra = self.magia
             self.magia = 0
        if tipo_ataque == "AGUA":
            return f"PLANTA {nivel_contra}"
        elif tipo_ataque == "FUEGO":
            return f"AGUA {nivel_contra}"
        elif tipo_ataque == "PLANTA":
            return f"FUEGO {nivel_contra}"

    def derrota(self):
         return f"Nadie... lo lamento X o X"
