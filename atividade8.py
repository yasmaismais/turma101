matriculado=input("está matriculado? (s/n):")
multa=input("aluno tem multa pendente? (s/n):")
livros=int(input("quantos livros já emprestou?"))
if matriculado=="s" and multa=="n" and livros<3:
    print("emprestimo altorizado")
else:
    print("emprestimo negado")