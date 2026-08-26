import random
import tkinter as tk
from tkinter import messagebox

# --- VARIÁVEIS GLOBAIS ---
# O código amador costuma usar variáveis soltas no topo
numero_secreto = random.randint(1, 24)
tentativas = 6


# --- FUNÇÃO PRINCIPAL ---
def chutar():
  global tentativas, numero_secreto  # Uso de 'global' para alterar as variáveis

  # Pega o que o usuário digitou
  palpite_texto = entrada.get()

  # Transforma em número inteiro
  palpite = int(palpite_texto)

  # Limpa o campo de texto
  entrada.delete(0, tk.END)

  # Verifica se acertou
  if palpite == numero_secreto:
    messagebox.showinfo("Ganhou!", "Você acertou o número!")
    # Reinicia o jogo
    numero_secreto = random.randint(1, 24)
    tentativas = 6
    label_status.config(text="Novo jogo! Tentativas: 6")

  else:
    # Se errou, diminui uma tentativa
    tentativas = tentativas - 1

    if tentativas == 0:
      messagebox.showerror(
          "Perdeu!", f"Acabaram as tentativas! O número era {numero_secreto}"
      )
      # Reinicia o jogo
      numero_secreto = random.randint(1, 24)
      tentativas = 6
      label_status.config(text="Novo jogo! Tentativas: 6")
    else:
      # Dá a dica
      if palpite < numero_secreto:
        dica = "MAIOR➕"
      else:
        dica = "MENOR➖"

      label_status.config(
          text=f"❌Errou! O número é {dica}.\nTentativas restantes: {tentativas}❌"
      )


# --- INTERFACE GRÁFICA ---
janela = tk.Tk()
janela.title("Jogo de Adivinhar")
janela.geometry("300x250")

# Texto de instrução
label_titulo = tk.Label(janela, text="Adivinhe o número (1 a 24):")
label_titulo.pack()

# Caixinha para digitar
entrada = tk.Entry(janela)
entrada.pack()

# Botão de enviar
botao = tk.Button(janela, text="Tentar🔁", command=chutar)
botao.pack()

# Texto com as tentativas e dicas
label_status = tk.Label(janela, text="Tentativas restantes: 6❗")
label_status.pack()

# Roda o aplicativo
janela.mainloop()