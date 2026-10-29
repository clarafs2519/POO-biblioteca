from livros import Livros
from usuarios import Usuario
from biblioteca import Biblioteca



def main():
  
    livro1 = Livros("Gato", "Ana", 2001)
    user1 = Usuario("Maria", "mari@gmail.com")

    biblioteca = Biblioteca()

    biblioteca.colocar_biblioteca(livro1)
    livro1.emprestimo()
    biblioteca.listar_informacoes()


if __name__ =="__main__":
    main()

