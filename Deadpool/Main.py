def main():
    idade = int(input ("digite a sua idade"))
    if idade >= 18: 
            print("vc pode entrar")
    elif idade >=16:
           acompanhante = input("vc esta acompanhado")
           if acompanhante == "sim":
             print("vc pode entrar")
           else:
             print("vc n pode entrar")
    else:
      print("vc não pode entrar")
    



    return 0
main()
    