#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:41:08 2024

@author: agn
"""

from menu import menuLoad
from log import save_log_to_txt


def money(moneyList):
    for money in moneyList:
        print("monaies: acceptées", money, "P")

def find_combinations(returned, available_coins):
    # Trier les pièces par ordre décroissant pour prioriser les plus grandes pièces
    #valuePiece.sort(reverse=True)
   # print("value Piece ----Combination", available_coins)
    print("----------------------------------")



    available_coins.sort(key=lambda coin:coin['value'], reverse=True) 
    
    # Créer un dictionnaire pour stocker les différentes combinaisons
    solution = {coin['value']: 0 for coin in available_coins}  # Initialiser le nombre de chaque pièce à 0
    remaining_amount = returned

    # Essayer de donner la monnaie avec les pièces les plus grandes d'abord
    for coin in available_coins:
        print("coin: ", coin)
        coin_value = coin['value']
        coin_quantity = coin['quantity']
        
        if remaining_amount >= coin_value  and coin_quantity > 0:
            # Calculer le nombre de pièces de cette valeur
            num_coins = min(remaining_amount // coin_value, coin_quantity)
            solution[coin_value] = num_coins

            remaining_amount -= num_coins * coin_value
            
    # Afficher le résultat
    if remaining_amount == 0:
        print(f"Pour {returned} centimes, vous pouvez utiliser :")
        for coin in available_coins:
            coin_value = coin['value']
            coin_quantity = coin['quantity']

            if solution[coin_value] > 0:
                print(f"- {solution[coin_value]} pièces de {coin_value} centimes")
            coin_quantity= coin_quantity - solution[coin_value]
            coin["quantity"] = coin_quantity
        print("Apres rendu: ", solution, available_coins, "recap")

    else:
        print(f"Aucune combinaison possible pour {returned} centimes avec ces pièces.")
    print("----------------------------------")



def machine(choice):

    lists=[ 
    {"value": "Café noir ", "price": 30},
    {"value": "Café au lait ", "price": 25},
    {"value": "Thé", "price": 20},
    {"value": "Chocolat au lait", "price": 35},
    {"value": "Cappuccino", "price": 40}
    ]
    
    available_coins=[ 
        {"value": 5, "type": "piece_5_euro", "quantity": 5},
        {"value": 10, "type": "piece_10_euro", "quantity": 10},
        {"value": 15, "type": "piece_15_centimes", "quantity": 20},
        {"value": 20, "type": "piece_20_centimes", "quantity": 0},
        {"value": 50, "type": "piece_50_centimes", "quantity": 30}]
    
    
    #monaie
    moneyList=[5, 10, 20, 50]
    listIntro=[]
    listsBuy=[{}]
    
    
    if choice >=0:
        
        # Selectionne le choix
        
        select=int(input("Sélectionnez votre boisson !: "))  
        
        if 1<=select<=len(lists) :
            print("Vous avez choisi un", lists[select-1]["value"], ",", "Merci de payer svp!: ",  lists[select-1]["price"], "P")            
            
            money(moneyList)

            #-------------- 
            item_select= select-1
            #print("le prix entrée: ", lists[item_select]["price"])
            
            #---
            price = lists[select-1]["price"]
            value = lists[select-1]["value"]

            introducedPiece=int(input(" Saisir = "))
            
            if introducedPiece == price:
                print("Montant saisi = ", introducedPiece, "P .Votre boisson est prête !")
                # à cumuler la quantité 
                
                # fichier de log
                
                print(listsBuy)
                log= save_log_to_txt(listsBuy, value, price, "recap")


            if introducedPiece not in moneyList:
                print(" -- Monaies NON acceptées  -- ")
                money(moneyList)
            else: 
                
                price= lists[item_select]["price"]        
                listIntro.append(introducedPiece)
                #print(listIntro[0])
            
            # piece déja dispo
               
                while listIntro[0] <  price or  listIntro[0] >  price:
                    print("-----")
                    
                    somme= sum(listIntro)
                    print ("somme: ", somme)
                    
                    if somme > price:
                        
                        print("somme", somme)
                        returned= somme - price
                        print("Montant saisi = ", somme, "P. . Rendu = ", returned,"P.Votre boisson est prête !")
                        
                        # Gerer la quantité apres achat à faire 
                        
                        #log file
                        log= save_log_to_txt(listsBuy, value, price, "recap")
                        
                        find_combinations(returned, available_coins)
                        break
                    elif (somme == price):
                        print("Montant saisi = ", somme, "P .Votre boisson est prête !")
                        # Gerer la quantité apres achat à faire 

                        #log file 
                        log= save_log_to_txt(listsBuy, value, price, "recap")
                        break
                    else: 
                        print("-- La  saisie est Insuffisant -- ")
                        introducedPieceNew=int(input(" Saisir = "))
                        if introducedPieceNew not in moneyList:
                            print(" -- Monaies NON acceptées  -- ")
                        else: 
                            listIntro.append(introducedPieceNew)
                            print(listIntro)
                    
        else: print("la selection n'est pas bon")
       
def main():
   
    try:
        menu=menuLoad()
        choice = int(input("Saisir le choix: "))
    except ValueError:
        print("Entrer votre choix Svp! .")
        return
    
    match choice:
        case 0:
            print("Annuler")
        case 1:
             machine(choice)
        case _:
             print("")

if __name__ == "__main__":
    main()