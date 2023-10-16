from pywebio.input import input
from pywebio.output import put_text, popup
import random
def sontop(x=10):
    tasodifiy_son = random.randint(1, x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end="")
    while True:
        kiritilganSon = int(input("Son kiriting: "))
        if kiritilganSon < tasodifiy_son:
            put_text("Kattaroq son ayting")
        elif kiritilganSon > tasodifiy_son:
            put_text("Kichikroq son ayting")
        else:
            popup("Yutdingiz!")
            break


from pywebio.output import put_buttons
import pywebio
from time import sleep



def sontop_pc(x=10):
    pywebio.output.clear(scope=-1)
    global quyi, yuqori, taxmin


    quyi = 1
    yuqori = x
    put_text(f"1 dan {x} gacha son o'ylang.\nSizga 3 soniya vaqt!")
    for i in [3, 2, 1, "Boshladik!"]:
        put_text(str(i))
        sleep(1)


    def guess():
        pywebio.output.clear(scope=-1)
        global taxmin
        taxmin = random.randint(quyi, yuqori)
        put_text(f"Siz {taxmin} sonini o'yladingiz!")
        put_buttons(["Kattaroq", "To'g'ri", "Kichikroq"], onclick=[katta, bingo, kichik])
        pywebio.session.hold()


    def kichik():
        global yuqori
        yuqori = taxmin - 1
        guess()


    def katta():
        global quyi
        quyi = taxmin + 1
        guess()


    def bingo():
        put_text("Men yutdim!")


    guess()


