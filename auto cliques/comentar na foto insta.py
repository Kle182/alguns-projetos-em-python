import time
import pyautogui
from pynput.keyboard import Key, Controller

# Função para encontrar e clicar na imagem
def encontre_e_clique_na_imagem(nome_imagem):
    localizacao = pyautogui.locateOnScreen(nome_imagem)
    if localizacao is not None:
        x, y = pyautogui.center(localizacao)
        pyautogui.click(x, y)

# Inicialize o controlador do teclado
keyboard = Controller()

# Loop infinito
while True:
    # Pressione a tecla Page Down do teclado
    keyboard.press(Key.page_down)
    keyboard.release(Key.page_down)
    time.sleep(0.2)

    # Encontre e clique na primeira imagem que você deseja
    encontre_e_clique_na_imagem('addcoment.png')
    time.sleep(0.4)
    
    # Digite a frase desejada
    pyautogui.write("Muito Bem!!", interval=0.1)
    time.sleep(0.1)

    # Encontre e clique em outra imagem diferente
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    # Aguarde um pouco antes de reiniciar o loop
    time.sleep(2)  # Ajuste o tempo de espera conforme necessário
