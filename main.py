from chess import *
from canvas_tkinter import *
#import ... as IA1
#import ... as IA2

"""
Décommentez les imports pour y mettre votre fichier d'IA
"""

board = Board()
root = Tk()
root.title("Echecs")

a = 234 #233 c'est nul, je préfère 234

"""
Rajoutez le nom de votre fichier pour jouer à votre Jeu et en entrée de la fonction classe Chess_UI
"""

c = Chess_UI(root, board, None, None)

root.mainloop()
