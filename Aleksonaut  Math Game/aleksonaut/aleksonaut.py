import os
import random
import time
from colorama import init, Fore
from pyfiglet import Figlet

# Inicjalizacja kolorów
init(autoreset=True)

# Wycentrowanie tekstu
def center(text, width=80):
    lines = text.split('\n')
    return '\n'.join(line.center(width) for line in lines)

# Czyszczenie ekranu
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Baner ASCII
def ascii_banner():
    f = Figlet(font='slant')
    banner = f.renderText("aleksonaut")
    print(Fore.BLUE + center(banner))
    podpis()

# Podpis
def podpis():
    print(Fore.MAGENTA + center("made by Aleks Skrzypinski"))

# Bezpieczny input z opcją wyjścia
def bezpieczny_input(prompt="> "):
    odp = input(prompt).strip()
    if odp.lower() == "exit":
        print(Fore.YELLOW + center("👋 Do zobaczenia!"))
        podpis()
        exit()
    return odp

# Funkcja zadania z licznikami
def zadanie(typ, nick, min_val=1, max_val=50):
    poprawne = 0
    bledy = 0
    max_bledy = 5

    while True:
        if bledy >= max_bledy:
            clear()
            ascii_banner()
            print(Fore.RED + center(f"❌ Przekroczyłeś limit błędów ({max_bledy})!"))
            print(Fore.CYAN + center(f"Twój końcowy wynik: {poprawne} poprawnych odpowiedzi"))
            podpis()
            time.sleep(3)
            return

        clear()
        ascii_banner()

        if typ in ["1", "2", "3"]:
            a = random.randint(min_val, max_val)
            b = random.randint(min_val, max_val)
        elif typ == "4":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
        elif typ == "5":
            b = random.randint(2, 10)
            wynik = random.randint(2, 10)
            a = b * wynik

        if typ == "1":
            wynik = a + b
            pytanie = f"{a} + {b} = ?"
        elif typ == "2":
            wynik = a - b
            pytanie = f"{a} - {b} = ?"
        elif typ == "3":
            if random.choice([True, False]):
                wynik = a + b
                pytanie = f"{a} + {b} = ?"
            else:
                wynik = a - b
                pytanie = f"{a} - {b} = ?"
        elif typ == "4":
            wynik = a * b
            pytanie = f"{a} x {b} = ?"
        elif typ == "5":
            pytanie = f"{a} ÷ {b} = ?"

        print(Fore.YELLOW + center(f"✍️  {nick}, oto Twoje pytanie:"))
        print(Fore.CYAN + center(pytanie))
        print()
        print(Fore.GREEN + center(f"✅ Poprawne: {poprawne}"))
        print(Fore.RED + center(f"❌ Błędy: {bledy}/{max_bledy}"))
        print()
        print(Fore.WHITE + center("Wpisz swoją odpowiedź lub 'exit' aby zakończyć."))

        odp = bezpieczny_input("> ")

        if not odp.isdigit():
            print(Fore.RED + center("⚠️ Podaj liczbę lub wpisz 'exit'."))
            time.sleep(2)
            continue

        if int(odp) == wynik:
            print(Fore.GREEN + center("✅ Dobrze!"))
            poprawne += 1
        else:
            print(Fore.RED + center(f"❌ Źle! Prawidłowa odpowiedź to: {wynik}"))
            bledy += 1

        time.sleep(2)

# Główna funkcja programu
def main():
    clear()
    ascii_banner()
    print(Fore.CYAN + center("Podaj swój nick (albo wpisz 'exit'):"))
    nick = bezpieczny_input("> ")

    clear()
    ascii_banner()
    print(Fore.YELLOW + center("Czego chcesz się nauczyć?"))
    print()
    print(Fore.BLUE + center("1. Dodawanie"))
    print(Fore.BLUE + center("2. Odejmowanie"))
    print(Fore.BLUE + center("3. Dodawanie i odejmowanie"))
    print(Fore.BLUE + center("4. Tabliczka mnożenia"))
    print(Fore.BLUE + center("5. Dzielenie"))
    print()
    podpis()
    wybor = bezpieczny_input("> ")

    min_val, max_val = 1, 50
    if wybor in ["1", "2", "3"]:
        clear()
        ascii_banner()
        print(Fore.CYAN + center("Zakres liczb dla działań (np. 1 do 100)"))
        print(center("Minimalna wartość:"))
        min_val = int(bezpieczny_input("> "))
        print(center("Maksymalna wartość:"))
        max_val = int(bezpieczny_input("> "))

    zadanie(wybor, nick, min_val, max_val)

if __name__ == "__main__":
    main()