import tkinter as tk
import time
import pyautogui
from pynput.keyboard import Key, Controller

# Inicialize o controlador do teclado
keyboard = Controller()

# Função para encontrar e clicar na imagem
def encontre_e_clique_na_imagem(nome_imagem):
    localizacao = pyautogui.locateOnScreen(nome_imagem)
    if localizacao is not None:
        x, y = pyautogui.center(localizacao)
        pyautogui.click(x, y)

# Função para executar o loop
def executar_loop():
    # Obtém a lista de frases do campo de entrada
    frases = entrada_frases.get("1.0", "end-1c").split('\n')
    frases = [frase.strip() for frase in frases if frase.strip()]  # Remove linhas em branco

    if not frases:
        resultado.config(text="Nenhuma frase fornecida.")
        return

    # Inicializa o contador para acompanhar as frases
    contador_frases = 0

    while True:
        # Pressiona a tecla Page Down do teclado
        keyboard.press(Key.page_down)
        keyboard.release(Key.page_down)
        time.sleep(0.5)

        # Chama a função para encontrar e clicar na imagem
        encontre_e_clique_na_imagem('coracao.png')  # Substitua pelo caminho da sua imagem
        time.sleep(0.4)

        # Encontra e clica na imagem "addcoment.png"
        encontre_e_clique_na_imagem('addcoment.png')
        time.sleep(0.5)

        # Escreve a próxima frase da lista e atualiza o contador
        frase_atual = frases[contador_frases]
        pyautogui.write(frase_atual, interval=0.1)
        contador_frases = (contador_frases + 1) % len(frases)

        # Encontra e clica em outra imagem diferente
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        # Aguarda um pouco antes de reiniciar o loop
        time.sleep(2)  # Ajuste o tempo de espera conforme necessário

# Configura a janela
janela = tk.Tk()
janela.title("Automatizador de Comentários")

# Cria um rótulo
rotulo = tk.Label(janela, text="Digite as frases (uma por linha):")
rotulo.pack()

# Cria uma caixa de texto para inserção de frases
entrada_frases = tk.Text(janela, width=40, height=5)
entrada_frases.pack()

# Cria um botão para iniciar o loop
botao_iniciar = tk.Button(janela, text="Iniciar", command=executar_loop)
botao_iniciar.pack()

# Cria um rótulo para exibir resultados ou mensagens de erro
resultado = tk.Label(janela, text="")
resultado.pack()

# Inicia a interface gráfica
janela.mainloop()
