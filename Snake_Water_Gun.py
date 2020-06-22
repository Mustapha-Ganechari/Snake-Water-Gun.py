print("Snake-Water-Gun GAME : ")

"""import random"""
import random

computer = 0
human = 0
element = 0
while(element<10):
    swg = input("Enter your choice s/w/g ? : ")
    random_list = ["Snake","Water","Gun"]
    a = random.choice(random_list)
    print(a)
    if swg == "s"and (a=="Water"):
        print("human win")
        human+=1
        element+=1
    elif swg == "s"and a=="Gun":
        print("Computer win")
        computer+=1
        element+=1
    elif swg == "s"and a=="Snake" :
        print("Draw")
        element+=1
    elif swg == "w"and a=="Water":
        print("Draw")
        element+=1
    elif swg == "w"and a=="Snake":
        print("computer win")
        computer+=1
        element+=1
    elif swg == "w"and a=="Gun":
        print("human win")
        human+=1
        element+=1
    elif swg == "g"and a=="Water":
        print("computer win")
        computer+=1
        element+=1
    elif swg == "g"and a=="Snake":
        print("human win")
        human+=1
        element+=1
    elif swg == "g"and a=="Gun":
        print("Draw")
        element+=1    
    else:
        element+=1 
        print("Enter Valid input")
        
print("\t\t Game Over")
print(f"human points {human} and Computer points {computer}")
if human >computer:
    print(f" So human win points are  : {human}")
elif human == computer:
    print(f"SO draw {human} == {computer}")
else:
    print(f" So compter win pionts are : {computer}")

