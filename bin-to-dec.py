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

	for n in range(laenge):                           # Umrechnung zum Dezimalsystem
		y = basis ** n
		y = re_sysZahl_liste[n] * y
		decZahl = decZahl + y

	print(Fore.GREEN + str(decZahl) + "\033[39m")

#allgemeiner input
def eingabe():
	basis = int(input('Basis eingeben (Kennzeichnung des Zahlensystems): '))
	sysZahl_liste = [int(item) for item in input("Zahl aus belibigem Zahlensystem (mit Leerzeichen abtrennen): ").split()]
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

