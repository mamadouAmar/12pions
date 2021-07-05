

# class Position:
    
#     def __init__(self, abscisse, ordonnee):
#         self.abscisse = abscisse
#         self.ordonnee = ordonne


class Pion:

    def __init__(self, couleur, abscisse, ordonnee):
        self.couleur = couleur
        self.abscisse = abscisse
        self.ordonnee = ordonnee
    
    def changer_position(self, abscisse, ordonnee):
        plateau[self.abscisse][self.ordonnee] = "vide"
        self.abscisse = abscisse
        self.ordonnee = ordonnee
        plateau[self.abscisse][self.ordonnee] = "occupee"

    def deplacer_gauche(self):
        if plateau[self.abscisse-1][self.ordonnee] == "vide":
            self.changer_position(self.abscisse-1, self.ordonnee)
    

