
rozsah = int(input('Insert a number (from 1 up) as an upper limit of numbers to be evaluated as prime numbers: '))
hledane_cislo = int(input('Insert a number you want to evaluate (is or is not a prime number): '))

def list_primes(rozsah):
    '''Function creating list of prime numbers '''
    cisla = []
    for i in range(2, rozsah +1):
        cisla.append(i)

    for cislo in cisla:
        nasobek = cislo
        while nasobek < rozsah:
            nasobek+= cislo
            if nasobek in cisla:
                cisla.remove(nasobek)       
    return cisla

def is_prime(hledane_cislo):
    '''Function determining whether the number in listprimes() is prime number or not. Printing list of such a numbers '''
    if hledane_cislo in list_primes(rozsah):
        print(f'Inserted number {hledane_cislo} IS prime number!')
    else:
        print(f'Inserted number {hledane_cislo} IS NOT a prime number.')

print(list_primes(rozsah))
is_prime(hledane_cislo)
