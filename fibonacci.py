fibonacci = []

# Controllo sulla validità dell'input
while True :
    nfib = input("Quanti numeri vuoi stampare? ")
    try:
        nfib = int(nfib)
        if nfib > 0:
            break
        else:
            print("ATTENZIONE:",nfib,"non è maggiore di zero. Riprova...\n\n")
        
    except ValueError:
        print("ATTENZIONE: " + nfib + " non è un numero intero. Riprova...\n\n")
        continue
    
# Generazione della serie
for n in range(nfib):
    if n < 2:
	fibonacci.append(1)
    else:
	fibonacci.append(fibonacci[n-1] + fibonacci[n-2])

print(fibonacci)
