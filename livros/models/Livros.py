class Livros:

    def __init__(self, titulo, autor, ano_publicacao, numero_paginas, pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.pagina_atual = pagina_atual

    def avancar_pagina(self):
      if self.pagina_atual < self.numero_paginas:
        self.pagina_atual += 1
      else:
        print("Você já está na última página.")

    def voltar_pagina(self):
      if self.pagina_atual > 1:
          self.pagina_atual -= 1
      else:
        print("Você já está na última página.")

    def exibir_info(self):
      print(f"Título: {self.titulo}")
      print(f"Autor: {self.autor}")
      print(f"Ano de publicação: {self.ano_publicacao}")
      print(f"Número total de páginas: {self.numero_paginas}")
      print(f"Página atual: {self.pagina_atual}")

