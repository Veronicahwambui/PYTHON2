

num= 5
num_of_tries = 0
print("welcome to number guessing game!!")

while True:
     try:
         lucky_num =int(input("please enter your lucky number 1 to 10:"))

         if lucky_num >11 or lucky_num<1:
             print("please entry number from 1 to 10")
             continue

         if lucky_num == num:
              print("you won!")
              again =input("would you like to play again?Enter Y/N")

         if again == "N":
              print("Thank you for paying with us")
              break
         else:
             print("Sorry !!Its wrong number")
             num_of_tries += 1

         if num_of_tries ==3:
              print("Your 3 attempt exceeded")
              print("Better luck next time")
              break

     except:
         print("please enter number from 1 to 10:")
         continue