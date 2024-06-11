def poser_question(question, reponse):
    print(question)
    chances_restantes = 3
    while chances_restantes > 0:
        proposition = input("Ta réponse ? : ")
        if proposition == reponse:
            print("Good job! This is the right answer")
            return True  # Retourne True si la réponse est correcte
        else:
            chances_restantes -= 1
            print("Too bad! that is not the correct answer")
            if chances_restantes == 0:
                print("Too bad, you lost the game!")
                return False  # Retourne False si l'utilisateur a épuisé ses chances
            else:
                print(f"Reste {chances_restantes} chance{'s' if chances_restantes > 1 else ''}!")

def run_quiz():
    print("Here you have our quiz!")
    print("---------")
    questions = [
        ("Question 1 : combien font 1+1 ?", "2"),
        ("Question 2 : Combien font 1977-1 ?", "1976"),
        ("Question 3 : Qui est le patron de Tesla ? (sans majuscule!)", "elon musk")
    ]

    gagne = True  # Variable pour suivre si l'utilisateur a gagné ou perdu

    for question, reponse in questions:
        reponse_correcte = poser_question(question, reponse)
        if not reponse_correcte:
            gagne = False
            break  # Sort de la boucle si l'utilisateur a épuisé ses chances

    if gagne:
        print("Bravo, vous avez gagné le quiz !")
    else:
        print("Dommage, vous avez perdu le quiz.")

# Exécution du quiz
run_quiz()



