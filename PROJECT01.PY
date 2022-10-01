import random

def sps(sys,user):
    if(sys==user):
        return None
    if(sys=='stone'and user=='paper'):
        return True
    elif(sys=='sci' and user=='stone'):
        return True
    elif(sys=='paper'and user=='sci'):
        return True
    else:
        return False


objects=('stone','paper','sci')
system=random.randint(0,2)
system=objects[system]
user=input("Choose Stone/paper/sci: ")

result=sps(system,user)
print(f"You chose {user} and system choes {system}.")
if(result is None):
    print("Match is drawn")
if(result is True):
    print("You have won")
elif(result is False):
    print("You lose")