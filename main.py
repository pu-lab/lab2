#zad1
filmy = ['szybcy i wsciekli', 'krol lew', 'wladca pierscieni', 'piraci z karaibow', ' DAS BOOT']
print(filmy)
filmy.reverse()
print(filmy)
filmy.insert(5, 'dobry zly i brzytki')
filmy.insert(5, 'jarhead')
filmy.insert(5, 'Forrest Gump')
filmy.insert(5, 'Pulp Fiction')
filmy.insert(5, 'Chlopcy z ferajny')
print(filmy)
#zad2
slownikFilmy = {"wyscigowy":"szybcy i wsciekli","animowany":"krol lew","fantasy":"wladca pierscieni","piracki":"piraci z karaibow",
         'western':"dobry zly i brzytki","wojenny":"DAS BOOT","afganistan":"jarhead","dramat":"Forest Gump",
         "miedzygatunkowy":"pulp ficton","gangsterski":"chlopcy z ferajny"}
#zad3
slownikPrzedmioty = {"CAD":"komputerowe wspomaganie programowania","WD":"Wizualizacja danych","ETY":"etyka",
                   "JA":"jezyk angielski","RRIC":"rachunek rozniczkowy i calkowy","EMD":"elementy matematyki dyskretnej",
                   "PS":"programowanie strukturalne","WZ":"wizualizacja danych"}
print(len(slownikPrzedmioty))
#zad4
liczba = input("Podaj liczbe: ")
liczba = int(liczba)
wynik = liczba*liczba
print(wynik)
#zad5
licznik = 0
import sys as system
system.stdout.write("wpisz dowolny komunikat: ")
napis = system.stdin.readline()
for x in napis:
    if x == 'a': licznik = licznik+1

print(licznik)
#zad6
a = input("Podaj liczbe: ")
a = int(a)
b = input("Podaj liczbe: ")
b = int(b)
c = input("Podaj liczbe: ")
c = int(c)
if a % 2 == 0 and b > c: print("wszystko zgodne")
else: print("nie zgodne")
#zad7
wynik1 = float(wynik)
lista = [1, 2, 3, 4, 5, 6]
for x in lista:
    if x > 1: x*x-1
    print(wynik1)
