import random
while True:
       print("Welcome to snake-water-gun game.\nLets go!!!!!!")
       
       print("Press 1 for Snake 🐍")
       print("Press 2 for Water 💧")
       print("Press 3 for Gun 🔫")
       user=int(input("Enter: "))
       comp= random.random()
       if(comp ==  user):
                   print("Its a tie");
       elif(comp<0.333):
                   print("Computer choice is Snake 🐍")
                   if(user==3):
                       print("Congo!You Win.Here here is your Bournvita Hamper");
                   elif(user==1):
                        print("It's a tie");
                   else:
                       print("You lose")
       elif(comp<0.666):
                   print("Computer choice is Water 💧")
                   if(user==1):
                       print("Congo!You Win.Here is your Bournvita Hamper");
                   elif(user==2):
                        print("Its a tie");
                   else:
                       print("You Lose")
       elif(comp>0.666):
                   print("Computer choice is Gun 🔫")
                   if(user==3):
                        print("Its a tie");
                   elif(user==2):
                       print("Congo!You Win.Here is your Bournvita hamper");
       else:
                   print("You lose")      
       x=int(input("Press 1 for play again otherwise 0 :"))   
       match x:
               case 1:
                   continue  
               case 0:
                   print("Okay, byeeeeee!")  
                   break  
               case _:
                   print("Invalid choice, exiting the game") 
                   break  
             



 


