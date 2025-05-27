import tkinter as tk

def imprimir_infos():  
    global trocar_msg
    trocar_msg = not trocar_msg
    if trocar_msg:
        rotulo.config(text="Olá, Mundo!")
    else:
        rotulo.config(text="Adeus, Mundo!")

trocar_msg = False
    
janela = tk.Tk() 
janela.title("Minha Janela")
janela.geometry("600x400")

rotulo = tk.Label(janela, text="Olá, Mundo!")
rotulo.pack(padx=20, pady=20)

botao = tk.Button(janela, text="Clique aqui", command=imprimir_infos)
botao.pack(padx=20, pady=20)

janela.mainloop()
