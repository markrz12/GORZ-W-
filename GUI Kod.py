
from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()

class Gracz():

    def __init__(self):
        self.talia = ["walet", "dama", "król", "szóstka", "siódemka", "ósemka", "dziewiątka", "dziesiątka", "as"]
        self.punkty_gracza = 0
        self.duze_pkt_gracza = 0
        self.talia_gracza = []

    def wylosuj_karte(self):
        self.los = random.choice(self.talia)
        self.talia_gracza.append(self.los)

        if self.los == "walet":
            self.punkty_gracza += 2
        elif self.los == "dama":
            self.punkty_gracza += 3
        elif self.los == "król":
            self.punkty_gracza += 4
        elif self.los == "szóstka":
            self.punkty_gracza += 6
        elif self.los == "siódemka":
            self.punkty_gracza += 7
        elif self.los == "ósemka":
            self.punkty_gracza += 8
        elif self.los == "dziewiątka":
            self.punkty_gracza += 9
        elif self.los == "dziesiątka":
            self.punkty_gracza += 10
        else:
            self.punkty_gracza += 11

gracz = Gracz()
komputer = Gracz()

#klasa okna z grą
class GameMainWindow():
    def __init__(self):
        self.punkty_gracza_var = StringVar()
        self.punkty_gracza_var.set(str(gracz.punkty_gracza))
        self.duze_punkty_gracza_var = StringVar()
        self.duze_punkty_gracza_var.set(str(gracz.duze_pkt_gracza))

        self.punkty_komputera_var = StringVar()
        self.punkty_komputera_var.set(str(komputer.punkty_gracza))
        self.duze_punkty_komputera_var = StringVar()
        self.duze_punkty_komputera_var.set(str(komputer.duze_pkt_gracza))


### Otwieranie okna z grą
    def open_main_game_window(self):
        main_game_window = Toplevel(root)
        main_game_window.title("Gra w Oczko")
        main_game_window.geometry("1980x1080")
        main_game_window.configure(background = 'black')
        Label(main_game_window, image = background_image).place(relwidth = 1, relheight = 1)

#Punkty i talia gracza
        punkty_gracza_tekst = Label(main_game_window, text= "Punkty gracza:", font =("Times New Roman", 20), foreground = "white", background = "black")
        punkty_gracza_tekst.place(x=28, y=28)
        punkty_gracza = Label(main_game_window, textvariable=self.punkty_gracza_var, font =("Times New Roman", 20), foreground = "white", background = "black")
        punkty_gracza.place(x=228, y=28)

        duze_punkty_gracza_tekst = Label(main_game_window, text = "Duże punkty gracza:", font =("Times New Roman", 20), foreground = "white", background = "black")
        duze_punkty_gracza_tekst.place(x=800, y=28)
        duze_punkty_gracza = Label(main_game_window, textvariable=self.duze_punkty_gracza_var, font =("Times New Roman", 20), foreground ="white", background ="black")
        duze_punkty_gracza.place(x=1050, y=28)

        #talia gracza tu będzie

        #Punkty i talia komputera
        punkty_komputera_tekst = Label(main_game_window, text= "Punkty komputera:", font =("Times New Roman", 20), foreground = "white", background = "black")
        punkty_komputera_tekst.place(x=28, y=400)
        punkty_komputera = Label(main_game_window, textvariable =self.punkty_komputera_var, font =("Times New Roman", 20), foreground = "white", background = "black")
        punkty_komputera.place(x=258, y=400)

        duze_punkty_komputera_tekst = Label(main_game_window, text = "Duże punkty komputera:", font =("Times New Roman", 20), foreground = "white", background = "black")
        duze_punkty_komputera_tekst.place(x=800, y=400)
        duze_punkty_komputera = Label(main_game_window, textvariable=self.duze_punkty_komputera_var, font =("Times New Roman", 20), foreground ="white", background ="black")
        duze_punkty_komputera.place(x=1050, y=400)

        # talia komputera bedzie tutaj


        ### Przyciski w oknie gry
        taking_card_button = Button(main_game_window, command = self.take_card, image = button4, background ='black', overrelief = FLAT)
        taking_card_button.pack(side = BOTTOM)

        checking_button = Button(main_game_window, command =self.check_out, image = button5, background = 'black', overrelief = FLAT)
        checking_button.pack(side = BOTTOM)

    # funkcja dobierz karte w oknie gry
    def take_card(self):
        gracz.wylosuj_karte()
        if komputer.punkty_gracza < 21:
            komputer.wylosuj_karte()
        self.punkty_gracza_var.set(str(gracz.punkty_gracza))
        self.punkty_komputera_var.set(str(komputer.punkty_gracza))

    #funkcja sprawdz w oknie gry
    def check_out(self):
        while komputer.punkty_gracza < 21:
            komputer.wylosuj_karte()
        self.punkty_komputera_var.set(str(komputer.punkty_gracza))

        # TUTAJ BEDA WARUNKI AKA KIEDY GRACZ A KIEDY KOMPUTER DOSTANIE DUZY PUNKT

        # [...]



gameMainWindow = GameMainWindow()



### Otwieranie okna z zasadami gry
def open_game_rules_window():
    game_rules_window = Toplevel(root)
    game_rules_window.title("Zasady gry")
    game_rules_window.geometry("1500x500")
    game_rules_window.configure(background = 'black')
    Label(game_rules_window, image = background_image).place(relwidth = 1, relheight = 1)

    logo_photo = Label(game_rules_window, image = logo, background = 'black')
    logo_photo.pack()

    rules_title = Label(game_rules_window, text = 'Zasady gry', font = ("Times New Roman", 20), foreground = 'white', background = 'black')
    rules_title.pack(side = TOP)

    rules_main_text = Label(game_rules_window, text = 'Gracz i bankier losują karty (z talii od szóstek do asów), otrzymując punkty: za szóstkę - 6, siódemkę - 7, ..., dziesiątkę - 10, waleta - 2, damę - 3, króla - 4, asa - 11. \nZadaniem obu jest zgromadzenie możliwie największej ilości punktów w kartach, jednakże nie przekraczającej 21. \nOczko gracza (tj. 21 punktów w kartach lub perskie, czyli dwa asy w dwóch pierwszych kartach) powoduje zwycięstwo w rozdaniu i uzyskanie przez niego dużego punktu. \nOczko bankiera to wygrane przez niego rozdanie. W przypadku przekroczenia 21 punktów delikwent (zarówno gracz, jak i bankier) automatycznie przegrywa rozdanie, a jego rywal zyskuje duży punkt. \nJeśli gracz i bankier uzyskali poniżej 21 punktów, wygrywa ten który zebrał ich więcej, a w przypadku uzyskania równej ilości punktów przez obu, wygrywa bankier i to on zyskuje duży punkt. \nBankier mając 15 punktów w kartach musi wziąć kartę, zaś przy 18 musi zakończyć dobieranie kart. Gracza nie obowiązują ograniczenia z poprzedniego punktu. \nGra kończy się po 21 wygranych rozdaniach (przez gracza lub bankiera). Pojedyncza gra nie może trwać dłużej niż 60 minut (czas zalogowania)', font = ("Times New Roman", 11), foreground = 'white', background = 'black')
    rules_main_text.pack(side = TOP)

    authors = Label(game_rules_window, text = 'Twórcy: Krzemińska M., Moryson J., Gawęcka P., Gbur K.', foreground = 'white', background = 'black')
    authors.pack(side = BOTTOM)

root=Tk()
root.geometry('500x500')
root.title('Zacznij Grę w Oczko!')
root.configure(background = "black")

### Tło okien
background_image = PhotoImage(file = "images/background.png")
Label(root, image = background_image).place(relwidth = 1, relheight = 1)

### Pobieranie obrazków
logo = PhotoImage(file = 'images/logo.png')
button1 = PhotoImage(file = 'images/button.png')
button2 = PhotoImage(file = 'images/button_rules.png')
button3 = PhotoImage(file = 'images/button_start.png')
button4 = PhotoImage(file = 'images/button_dobierz.png')
button5 = PhotoImage(file = 'images/button_sprawdz.png')

### Pobieranie obrazków kart
nine_t = PhotoImage(file = 'images/9-trefl.png')
ten_t = PhotoImage(file = 'images/10-trefl.png')
W_t = PhotoImage(file = 'images/walet-trefl.png')
D_t = PhotoImage(file = 'images/dama-trefl.png')
K_t = PhotoImage(file = 'images/krol-trefl.png')
A_t = PhotoImage(file = 'images/as-trefl.png')
nine_ka = PhotoImage(file = 'images/9-karo.png')
ten_ka = PhotoImage(file = 'images/10-karo.png')
W_ka = PhotoImage(file = 'images/walet-karo.png')
D_ka = PhotoImage(file = 'images/dama-karo.png')
K_ka = PhotoImage(file = 'images/krol-karo.png')
A_ka = PhotoImage(file = 'images/as-karo.png')
nine_ki = PhotoImage(file = 'images/9-kier.png')
ten_ki = PhotoImage(file = 'images/10-kier.png')
W_ki = PhotoImage(file = 'images/walet-kier.png')
D_ki = PhotoImage(file = 'images/dama-kier.png')
K_ki = PhotoImage(file = 'images/krol-kier.png')
A_ki = PhotoImage(file = 'images/as-kier.png')
nine_p = PhotoImage(file = 'images/9-pik.png')
ten_p = PhotoImage(file = 'images/10-pik.png')
W_p = PhotoImage(file = 'images/walet-pik.png')
D_p = PhotoImage(file = 'images/dama-pik.png')
K_p = PhotoImage(file = 'images/krol-pik.png')
A_p = PhotoImage(file = 'images/as-pik.png')
druga_strona = PhotoImage(file = 'images/druga-strona.png')

### Wyświetlanie logo
logo_photo = Label(root, image = logo, background = 'black')
logo_photo.pack(fill = BOTH)

### Przyciski w głównym oknie
starting_button = Button(root, image = button1, command = open_main_game_window, background = 'black', overrelief = FLAT)
starting_button.pack(side = TOP)

gamerules_button = Button(root, image = button2, command = open_game_rules_window, background = 'black', overrelief = FLAT)
gamerules_button.pack(side = TOP)

### Stopka
copyrights = Label(root, text = 'All rights reserved', foreground = 'white', background = 'black')
copyrights.pack(side = BOTTOM)

root.mainloop()
