'''
Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je placen po radnom satu.
Koristite ugradenu Python metodu input().
Nakon toga izracunajte koliko je korisnik zaradio i ispišite na ekran.
Na kraju prepravite rješenje na nacin da ukupni iznos izracunavate u zasebnoj funkciji naziva ˇ total_euro.
'''


def total_euro(WorkingHours, WorkingRate):
    return WorkingHours * WorkingRate


WorkingHours = float(input("Etner working hours: "))
WorkingRate = float(input("Etner working rate: "))
print(f"Total: {total_euro(WorkingHours, WorkingRate)}")
