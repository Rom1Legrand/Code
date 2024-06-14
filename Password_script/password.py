choixmdp = input("choix du mdp: ")
mdp = "test"
while choixmdp != mdp:
        print ("mauvais mdp")
        choixmdp = input("choix du mdp : ")
if choixmdp == mdp:
        print ("accès autorisé")
