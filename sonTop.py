import random
def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    while True:
        kiritilganSon = int(input("Son kiriting: "))
        if kiritilganSon < tasodifiy_son:
            print("Kattaroq son ayting")
        elif kiritilganSon > tasodifiy_son:
            print("Kichikroq son ayting")
        else:
            print("Yutdingiz!")
            break

