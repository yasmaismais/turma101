valor=float(input("digite o valor da compre: R$"))
cupom=input("possui cupom de desconto?(s/n):")
if valor >=100 and cupom == "s":
    codigo=input("digite o codigo do cupom:")
    if codigo=="cupom 10":
        desconto= valor*0.10
        valor_final=valor-desconto
        print(f"desconto aplicado. Valor final: R${valor_final:.2f}")
    else: 
        print("cupom invalido")
        print(f"valor original: R${valor:.2f}")
else:
    print(f"valor da compra:R${valor:.2f}")