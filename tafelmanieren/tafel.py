cijfer = input("Van welk cijfer wilt u de tafel weten? ")
print ("De tafel van ", cijfer)
cijfer = int(cijfer)
for teller in range(1,11):
    print(teller, " x ", cijfer, " = ", teller * cijfer)
