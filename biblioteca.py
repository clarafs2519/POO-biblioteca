
class Biblioteca:
    def __init__(self):
        self.bibliotecas = []

    def colocar_biblioteca(self, livro):
        self.bibliotecas.append(livro)


    def listar_informacoes(self):
    
        for livro in self.bibliotecas:
            print(f" Titulo:{livro.titulo} Autor:{livro.autor} Ano:{livro.ano} Disponivel:{livro.disponivel} ") 
            print("-"*50)