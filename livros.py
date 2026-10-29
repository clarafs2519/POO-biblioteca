

class Livros:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True


    def emprestimo(self):
        self.disponivel = False

    def devolver(self):
        self.disponivel = True

