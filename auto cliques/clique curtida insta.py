import time
import pyautogui
from pynput.keyboard import Key, Controller

# Aguarde 5 segundos antes de iniciar o teste
time.sleep(5)

# Inicialize o controlador do teclado
keyboard = Controller()

# Loop infinito alternando entre a seta direita e o botão esquerdo do mouse
while True:
    # Pressione a seta direita do teclado
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(0.3)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(0.5)
    
    # Clique com o botão esquerdo do mouse na posição atual do cursor
    pyautogui.click()
    time.sleep(0.2)
    
    # Aguarde 0,5 segundos
    time.sleep(0.3)
