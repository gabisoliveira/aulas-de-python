def main():
    numero = int(input ("digite um número:"))
                

    i = 2

    while numero != 1 and numero != 1:
        if numero  % i == 0:
            break
        i += 1

    if numero == i:
         print ("o número", numero, "é primo")   
    elif numero == 1:
        print("o número 1 não é primo")
    
    else:
         print("o número", numero, "não é primo porque é divisível por", i)


    return 0
main()
    