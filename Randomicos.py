import os
import random

Zero = random.randrange(0, 9999, 1)
Mil = 1606

while Zero != Mil:
    Zero = random.randrange(0, 9999, 1)
    print(Zero)
    os.system('cls')

print("Sua senha para esse serviço é: " + str(Zero))
os.system('pause')
