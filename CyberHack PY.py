import random
import time

reponse = ""
wallet = 0
userID = 0
money = 0
lucky = 0

def fonction_play():
    global money, userID, wallet
    print("Chargement en cours..")
    time.sleep(random.randint(1, 5))
    print("Commence pars lancer une recherche d'utilisateur. ")
    time.sleep(2)
    print("Pour cela tu vas devoir écrire < search > juste en dessous")
    fonction_tuto1()
    
def fonction_command():
    global wallet, userID, money, lucky
    reponse = input("\033[34mEntre la commande. Faite < help > pour en savoir plus. ")
    if reponse == "search":
        print("\033[93mRecherche d'un utilisateur en cours..")
        time.sleep(random.randint(5, 10))
        userID = random.randint(100,999)
        wallet = random.randint(100,800)
        print("\033[92mTa cible trouver est user" + str(userID) + ".")
        fonction_command()
    elif reponse == "profil":
        if userID == 0:
            print("\033[91mTu doit faire une recherche d'utulisateur pour avoir un profil.")
            fonction_command()
        else:
          print("User: " + str(userID))
          print("Wallet: " + str(wallet) + "$")
          fonction_command()
    elif reponse == "hacking":
        if userID == 0:
            print("\033[91mTu doit faire une recherche d'utulisateur pour avoir un profil.")
            fonction_command()
        else:
            print("\033[93mTest de combinaison de crack en cours..")
            time.sleep(random.randint(3,5))
            lucky = random.randint(1, 3)
            if lucky == 1:
                print("\033[91mCe compte a une protection trop forte pour pouvoir le décripté.")
                userID = 0
                wallet = 0
                fonction_command()
            else: 
                print("\033[93mLe transfert des ressources commence..")
                lucky = random.randint(1, 3)
                if lucky == 1:
                    print("\033[913mLes informations de l'utilisateur ne permette pas de rediriger vers un compte en banque.")
                    userID = 0
                    wallet = 0
                    fonction_command()
                else:
                    print("\033[92mUn compte en banque a etait trouver!")
                    time.sleep(2)
                    print("\033[92mVirement de " + str(wallet) + "$ en cours sur ton compte..")
                    time.sleep(random.randint(3,5))
                    money += wallet
                    print("\033[92mTu as etait crédité de " + str(wallet) + "$ sur ton compte.")
                    userID = 0
                    wallet = 0
                    fonction_command()
    elif reponse == "help":
        print("Voici la listes des commandes disponibles: search - trouver un utilisateur. / profil - avoir le profil de l'utilisateur rechercher. / hacking - commencer le hack de l'utilisateur rechercher. / account - regarder les statistiques que tu dispose. / help - te sert pour avoir la liste des commandes disponibles.")
        fonction_command()
    elif reponse == "account":
        print("Vous avez " + str(money) + "$")
        fonction_command()
    else:
        fonction_command()


def fonction_tuto1():
    global userID, money, wallet
    reponse = input("")
    if reponse == "search":
        userID = random.randint(100,999)
        print("Ta cible trouver est user" + str(userID) + ".")
        time.sleep(1)
        fonction_tuto2()
    else:
        fonction_tuto1()
    
    
def fonction_tuto2():
 global wallet, money, userID
 print("Maintenant avec < profil > tu pourras afficher les informations de cette utilisateur.")
 reponse = input("")
 if reponse == "profil":
     print("User: " + str(userID))
     wallet = random.randint(100, 400)
     print("Wallet: " + str(wallet) + "$")
     time.sleep(1)
     fonction_tuto3()
 else:
   fonction_tuto2()

def fonction_tuto3():
    global wallet, money, userID
    print("Pars chance, user" + str(userID) + " n'a pas de mot de passe.")
    time.sleep(1)
    print("Le transfert de l'argent vers ton compte commence..")
    time.sleep(2)
    money += wallet
    print("\033[92mOpération terminer.")
    time.sleep(1)
    print("\033[92mTu as etait credité de " + str(wallet) + "$")
    print("\033[92mTu as donc maitenant " + str(money) + "$ sur ton compte.")
    wallet = 0
    userID = 0
    fonction_command()
        
def fonction_start():
    global wallet, money, userID
    reponse = input("\033[34mtu veux jouer et devenir un hacker dans ce jeu de simulation? ")
    if reponse == "oui":
        fonction_play()
    elif reponse == "non":
        reponse = input("D'accord. Si jamais tu change d'avis, envoie < play > ")
        if reponse == "play":
            fonction_play()
        else:
            fonction_start()
    else: 
        print("Tu doit entrer oui ou non. merci de ne pas mettre de majuscule si vous en avez mis. ")
        fonction_start()

fonction_start()