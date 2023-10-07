import tkinter as tk
from tkinter import filedialog 

from question import poser_questions_et_reponses

# Fonction appelée lorsque le bouton est cliqué
def click():
    texte = champ_texte.get()  # Obtenir le texte du premier champ de texte
    liste = champ_liste.get("1.0", tk.END)  # Obtenir le texte du champ de texte multiligne
    liste = liste.strip()  # Supprimer les espaces au début et à la fin

    # Diviser la chaîne en paires en utilisant '\n' comme séparateur et supprimer les espaces
    paires = liste.split('\n')

    # Diviser chaque paire en utilisant '/' comme séparateur
    question = []
    reponse = []

    for paire in paires:
        elements = paire.split(texte)
        question.append(elements[0])
        reponse.append(elements[1])

    
    print("Question =", question)
    print("Reponse =", reponse)
    poser_questions_et_reponses(questions=question, reponses=reponse)

def ouvrir_fichier():
    chemin_fichier = tk.filedialog.askopenfilename(initialdir = "/", title = "Sélectionner un fichier texte", filetypes = (("noot files","*.noot"), ("Tous les fichiers", "*.*")))
    if chemin_fichier:
        # Si un fichier a été sélectionné, on lit son contenu et on l'affiche dans le widget texte
        with open(chemin_fichier, "r") as fichier:
            contenu = fichier.read()
            champ_liste.delete("1.0", tk.END)
            champ_liste.insert("1.0", contenu)

def save():
    filename = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("noot files","*.noot"), ("all files","*.*"))) 
    fichier = open(filename, "a")
    fichier.write(champ_liste.get("1.0", tk.END))
    fichier.close()


# Créer une fenêtre
fenetre = tk.Tk()
fenetre.title("LearnNoot")
p1 = tk.PhotoImage(file = 'unnamed.png') 
  
# Setting icon of master window 
fenetre.iconphoto(False, p1) 

menubar = tk.Menu(fenetre)
fenetre.config(menu=menubar)
menufichier = tk.Menu(menubar,tearoff=0)
menubar.add_cascade(label="Fichier", menu=menufichier)
menufichier.add_command(label="Ouvrir", command=ouvrir_fichier)
menufichier.add_separator()
menufichier.add_command(label="Enregistrer sous", command=save)
menufichier.add_separator()
menufichier.add_command(label="Quitter", command=quit)

etiquette_haut = tk.Label(fenetre, text="Object de séparation")
etiquette_haut.pack(pady=5)

# Créer un champ de texte
champ_texte = tk.Entry(fenetre)
champ_texte.pack(pady=5)  # Ajouter un espace autour du champ de texte
champ_texte.insert(0, "séparation")  # Texte par défaut dans le champ de texte

etiquette_haut = tk.Label(fenetre, text="Liste : ")
etiquette_haut.pack(pady=5)

# Créer un champ de texte multiligne
champ_liste = tk.Text(fenetre, height=5, width=40)
champ_liste.pack(pady=10)  # Ajouter un espace autour du champ de texte

# Créer un bouton pour afficher le texte
bouton = tk.Button(fenetre, text="Afficher le texte", command=click)
bouton.pack()

# Créer une étiquette pour afficher le texte saisi
etiquette = tk.Label(fenetre, text="")
etiquette.pack(pady=20)  # Ajouter un espace autour de l'étiquette

# Lancer la boucle principale
fenetre.mainloop()
