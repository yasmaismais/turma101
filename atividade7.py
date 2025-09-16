idade=int(input("dgite a idade:"))
acompanhado=input("esta acompanhado dos pais?(s/n):")
ingresso=input("possui ingresso valido? (s/n)")
if idade  >=18  or acompanhado=="s":
    if ingresso=="s":
        print("entrada permitida")
    else:
      print("entrada negada")
else:
    print("entrada negada")
