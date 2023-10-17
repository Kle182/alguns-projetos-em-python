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

# Lista de frases disponíveis
frases = ["www.mundoacupuntura.com.br", "Adorei!", "Gracias!", "Ja conhece o Mundo Acupuntura?"]

# Inicialize o contador para acompanhar as frases
contador_frases = 0

# Loop infinito
while True:
    # Pressione a tecla Page Down do teclado
    keyboard.press(Key.page_down)
    keyboard.release(Key.page_down)
    time.sleep(0.5)

    # Encontre e clique na primeira imagem que você deseja
    encontre_e_clique_na_imagem('addcoment.png')
    time.sleep(1)
    
    # Escreva a próxima frase da lista e atualize o contador
    frase_atual = frases[contador_frases]
    pyautogui.write(frase_atual, interval=0.1)
    contador_frases = (contador_frases + 1) % len(frases)
    # Avança para a próxima frase circularmente
    time.sleep(2)
    # Encontre e clique em outra imagem diferente
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    # Aguarde um pouco antes de reiniciar o loop
    time.sleep(1)  # Ajuste o tempo de espera conforme necessário
