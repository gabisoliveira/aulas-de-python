def main():
    num = int (input("digite um número:") )
    divisore = ""
    i = 2
    j = 0
    while num != i and num != 1:
        if num % i == 0:
            divisores += " " + str ( i )
            j += 1
        i += 1

    if j == 0:
        print ("némero primo")
    elif num == 1:
        print("1 não é primo")
    elif num == 1:
        print("1 não é primo")
    else:
        print ("Não é primo pois é divivel por", j, "números e mais e eles não", divisores)

    return 0
main() 
