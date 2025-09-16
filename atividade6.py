idade=int(input("digite a idade:"))
estudante=input("é estudante?(s/n):")
if idade <6 or idade >60: 
    print("passe livre")
elif estudante== "s" and 6<= idade <= 25:
    print("passe livre")
else:
    print("precisa pagar")