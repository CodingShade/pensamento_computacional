import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo Radiobutton")
janela.geometry("250x150")
def mostrar_opcao(botao):
    print(botao)
    texto = f"Escolheu: {opcao1.get()}"
    texto += f" {opcao2.get()}"
    texto += f" {opcao3.get()}"
    rotulo.config(text= texto)

    op = [opcao1.get(), opcao2.get(), opcao3.get()]
    if op.count(True) == 3:
        if opcao1.get() and opcao2.get():
            if botao == "SAUDE":
                opcao1.set(False)
            if botao == "TEMPO":
                opcao3.set(False)
            if botao == "DINHEIRO":
                opcao2.set(False)
    

opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()

tk.Checkbutton(janela, text="DINHEIRO", variable=opcao1, command=lambda:mostrar_opcao("DINHEIRO")).pack()
tk.Checkbutton(janela, text="TEMPO", variable=opcao2, command=lambda:mostrar_opcao("TEMPO")).pack()
tk.Checkbutton(janela, text="SAUDE", variable=opcao3, command=lambda:mostrar_opcao("SAUDE")).pack()


rotulo = tk.Label(janela, text="Escolheu: A")
rotulo.pack(pady=10)
janela.mainloop()