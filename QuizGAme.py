print("Welcome to my Computer Quiz!!")

playing = input("Do you Want to play? ")

if playing.lower() != "yes":
    quit()

print("Ok lets play : )")
score = 0

answer = input("What does CPU standa for? ").lower()
if answer == "central processing unit" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU standa for? ").lower()
if answer == "graphic processing unit" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM standa for? ").lower()
if answer == "random access memory" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU standa for? ").lower()
if answer == "power supply unit" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You scored " + str(score)+" Out of 4 in Quiz game")
print("You scored " + str((score/4)*100)+"%")





















