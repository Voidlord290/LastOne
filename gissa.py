import random
print ("---------------------------------------------------------------")
print (".:GissaTalet:.")

print ("gissa ett tal mellan 1 och 10 pröva lyckan, du får 3 försök!")
slumptal = random.randrange(1, 10)
#print (slumptal)
i = 0
hittat = False

while i < 3:
    gissatal =input ("mata in tal: ")
    if slumptal == int (gissatal):
        hittat = True
    print ("rätt svar!")
    break
i += 1
if hittat:
    print ("bra jobbat, här får du fem spänn")
else:
    print ("Bättre lycka nästa gång")
print("-------------------------------------------------------------------")