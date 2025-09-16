usuario=input("usuário:")
if usuario=="admin":
    senha=input("senha:")
    if senha=="1234":
        print("acesso permitido")
    else:
        print("senha incorreta")
        print("tente novamente")
else:
    print("usuário invalido")