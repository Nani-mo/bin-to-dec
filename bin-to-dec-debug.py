print("It's a trap")
import colorama
from colorama import Fore, Back, Style
colorama.init()

print("umrechnen von einenm belibigen Zahlensystem in das Dezimalsystem")
print("")

# main Funktion mit Logik
def operation():
	basis, sysZahl_liste = eingabe()
	ueberpruefen(basis, sysZahl_liste)
	decZahl = 0
	laenge = len(sysZahl_liste)
	re_sysZahl_liste = list(reversed(sysZahl_liste))
	print(re_sysZahl_liste)
	print("laenge: " + str(laenge))
	print("----------------------")

	for n in range(laenge):                           # Umrechnung zum Dezimalsystem
		print("Exoponent: " + str(n))
		print("Basis: " + str(basis))
		y = basis ** n
		print("potenzieren der Basis mit Exponenten: " + str(y))
		print("Koeffizient: " + str(re_sysZahl_liste[n]))
		y = re_sysZahl_liste[n] * y
		print("multiplizieren des Koeffizienten mit vorherigem Ergebnis: " + str(y))
		print("Endsumme vor der Addition: " + str(decZahl))
		decZahl = decZahl + y
		print("addieren des vorherigen Ergebnises zur Endsumme: " + str(decZahl))
		print("----------------------")

	print(Fore.GREEN + str(decZahl) + "\033[39m")

#allgemeiner input
def eingabe():
	basis = int(input('Basis eingeben (Kennzeichnung des Zahlensystems): '))
	sysZahl_liste = [int(item) for item in input("Zahl aus belibigem Zahlensystem (mit Leerzeichen abtrennen): ").split()]
	print("Basis: " + str(basis))
	print(sysZahl_liste)
	return(basis, sysZahl_liste)

# eingabe ueberpruefen
def ueberpruefen(basis, sysZahl_liste):  # wenn basis kleiner 1 dann Programm neustarten
	if basis <= 1:
		print(Fore.LIGHTRED_EX + "¯\_(ツ)_/¯ Basis darf nicht kleiner gleich 1 sein" + "\033[39m")
		run()
	for n in sysZahl_liste:
		if n >= basis:
			print(Fore.LIGHTRED_EX + "¯\_(ツ)_/¯ Die Zahlenwerte duerfen nicht groesser gleich der Basis sein" + "\033[39m")
			run()

def run():
	while True:
		operation()

try:
	run()
except KeyboardInterrupt:
	exit()

