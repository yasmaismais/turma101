
estudante=input("é estudante?(s/n):")
idade=int(input("digite a idade:"))
if estudante=="s" or idade < 12:
    print("paga meia")
else:
    print("paga inteira")