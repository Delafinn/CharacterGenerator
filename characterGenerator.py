# Create a random sentence generator with the following format.
# $name, hair color, age use lists to store these values
import random
import sys

namelist = ["alvin", "bob", "robert", "obiwan", "bill", "Morpheus", "lisa", "annie", "aang", "katara", "momo", "fred", "lola", "patrick", "pascal","Yoda","bill", "Darth","Rocco", "Rafael","Francis","Hugo"
 ,"Justin", "Solomon", "Ryan", "Milo", "Layla", "Carmen", "Olivia", "Evelyn", "Edie", "Tia"]
haircolor = ["black", "blonde", "white", "red", "blue", "brown", "bald"]
eyelist= ["brown", "blue", "Hazel", "amber", "gray", "green"]
# Make the app randomly select in the lists for a name, color, age. Populate these lists in your script with random data at least 3 values each
# now do this randomization 3 times ****

while True:
    Genquestion = input("Do you want to generate characters?")
    if Genquestion =="no" or Genquestion == " no":
        sys.exit("quitting")
    if Genquestion == "yes" or Genquestion == " yes":
        name1 = random.choice(namelist)
        print("First users name is is " + name1)
        hair1 = random.choice(haircolor)
        print(name1 + "s hair color is "+ hair1)
        age1 = random.randint(1,100)
        print(name1 + "s age is " + str(age1))
        eyeColor1 = random.choice(eyelist)
        print(name1 +"s eye color is " +  eyeColor1)


        name2 = random.choice(namelist)
        print("Second users name is is " + name2)
        hair2 = random.choice(haircolor)
        print(name2 + "s hair color is "+ hair2)
        age2 = random.randint(1,100)
        print(name2 + "s age is " + str(age2))
        eyeColor2 = random.choice(eyelist)
        print(name2 +"s eye color is " +  eyeColor2)

        name3 = random.choice(namelist)
        print("Third users name is is " + name3)
        hair3 = random.choice(haircolor)
        print(name3 + "s hair color is "+ hair3)
        age3 = random.randint(1,100)
        print(name3 + "s age is " + str(age3))
        eyeColor3 = random.choice(eyelist)
        print(name3 +"s eye color is " +  eyeColor3)

        if age1 > age2 and age1 > age3:
            print(name1 + " is older than " + name2 + " and " + name3)

        if age2 > age1 and age2 > age3:
            print(name2 + " is older than " + name1 + " and " + name3)

        if age3 > age1 and age3 > age2:
            print(name3 + " is older than " + name1 + " and " + name2)
