date = input("Entertodays day: ")
mood = input("milla mielella tanaan from 1 to 10  :")
ajatukset = input("mitka ajatukset mielessa tanaan :\n")

with open(f"../journal/{date}.txt","w")as file:
    file.write(mood+2*'\n')
    file.write(ajatukset)