WTS = input("what do you want me to say: ")
HT = int(input("how many times should i say this: "))

HT = min(HT, 99)

i=1

while i<=HT:
    print(i,"",WTS)
    i= i + 1
    