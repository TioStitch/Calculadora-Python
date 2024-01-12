import tkinter as tk

first = int(input("Insira o valor do primeiro número:"))
second = int(input("Insira o valor do segundo número:"))

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("400x200")

result = tk.Label(janela, text="Resultado: " + str((first+second)))
result.pack(pady=10)

janela.mainloop()
