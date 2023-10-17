import time
import pyautogui
import keyboard

def encontre_e_clique_na_imagem(imagem_path):
    posicao = pyautogui.locateOnScreen(imagem_path)
    if posicao is not None:
        x, y, largura, altura = posicao
        centro_x = x + largura // 2
        centro_y = y + altura // 2
        pyautogui.click(centro_x, centro_y)
    else:
        print("Imagem não encontrada.")

# Loop infinito
while True:
    # Pressiona a tecla "Page Down" duas vezes
    keyboard.press_and_release("page down")
    #keyboard.press_and_release("page down")

    # Aguarde 0.4 segundos antes de clicar na imagem novamente
    time.sleep(0.3)

    # Chame a função para encontrar e clicar na imagem
    encontre_e_clique_na_imagem('coracao.png')  # Substitua pelo caminho da sua imagem

    # Adicione 0.5 um pequeno atraso entre os loops para evitar que seja muito rápido
    time.sleep(0.4)
