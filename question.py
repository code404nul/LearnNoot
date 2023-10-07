import tkinter as tk

def poser_questions_et_reponses(questions, reponses):
    # Indice de la question actuelle
    question_index = 0
    revoir_question = []
    revoir_reponse = []


    # Fonction pour vérifier la réponse
    def verifier_reponse():
        nonlocal question_index
        nonlocal revoir_reponse
        nonlocal revoir_question

        reponse_utilisateur = reponse_entry.get()
        if reponse_utilisateur.lower() == reponses[question_index].lower():
            resultat_label.config(text="Bonne réponse!")
            fenetre.config(bg="green")
            question_index += 1
            if question_index < len(questions):
                fenetre.after(2000, poser_question)
            else:
                if len(revoir_question) != 0:
                    poser_questions_et_reponses(revoir_question, revoir_reponse)
                else:
                    resultat_label.config(text="Toutes les questions sont terminées.")
        else:
            
            revoir_question.append(questions[question_index])
            revoir_reponse.append(reponses[question_index])
            print(revoir_question, revoir_reponse)
            resultat_label.config(text=f"Mauvaise réponse. {reponses[question_index]}")
            fenetre.config(bg="red")
            fenetre.after(5000, poser_question)
            question_index += 1# Délai de 2 secondes avant de poser la question suivante
 

    # Fonction pour poser une nouvelle question
    def poser_question():
        nonlocal question_index
        nonlocal revoir_reponse
        nonlocal revoir_question

        fenetre['background']="#d9d9d9"
        if question_index < len(questions):
            question_label.config(text=questions[question_index])
            reponse_entry.delete(0, tk.END)
            resultat_label.config(text="")
        else:
            if len(revoir_question) != 0:
                poser_questions_et_reponses(revoir_question, revoir_reponse)
            else:
                resultat_label.config(text="Bravo! Toutes les questions sont terminées.")

    # Création de la fenêtre
    fenetre = tk.Tk()
    fenetre.title("Question-Noot")

# Set window color
    fenetre['background']="#d9d9d9"
    # Label pour afficher la question
    question_label = tk.Label(fenetre, text="", font=("Helvetica", 14))
    question_label.pack(pady=20)

    # Champ de saisie pour la réponse
    reponse_entry = tk.Entry(fenetre, font=("Helvetica", 12))
    reponse_entry.pack()

    # Bouton pour soumettre la réponse
    soumettre_bouton = tk.Button(fenetre, text="Soumettre", command=verifier_reponse)
    soumettre_bouton.pack(pady=10)

    # Label pour afficher le résultat
    resultat_label = tk.Label(fenetre, text="", font=("Helvetica", 12))
    resultat_label.pack(pady=10)

    # Commencer avec la première question
    poser_question()

    fenetre.mainloop()

#
