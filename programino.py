# Programma per verificare se un numero è primo

numero = int(input("Inserisci un numero: "))

# Verifica se il numero è primo
if numero < 2:
    print(f"{numero} non è primo")
else:
    is_primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            is_primo = False
            break
    
    if is_primo:
        print(f"{numero} è primo!")
    else:
        print(f"{numero} non è primo")
