import pyautogui
from time import sleep
import shutil
from pathlib import Path


def abrir_caminho(): # Abrir win + r
    
    sleep(2.3)
    pyautogui.hotkey('win', 'r')
    sleep(0.5)
    pyautogui.write('%appdata%', interval=0.03)
    pyautogui.press('enter')
    

def excluir_pasta_appdata(): # excluir a pasta appdata
    
    sleep(1)
    pyautogui.hotkey("ctrl", "e")  
    sleep(0.5)
    pyautogui.write("anydesk", interval=0.03)
    sleep(1)
    pyautogui.press("enter")
    sleep(1)
    pyautogui.press("down")
    sleep(1)
    pyautogui.press("up")  
    sleep(1)
    pyautogui.hotkey('shift', 'delete') 
    sleep(2.0)
    pyautogui.press("enter")
    sleep(1.0)
    pyautogui.hotkey('alt', 'f4')
    sleep(1.0)
    

def abrir_anydesk(): # Abrir anydesk novamente
    pyautogui.press("win")
    sleep(1)
    pyautogui.write("anydesk", interval=0.03)
    sleep(1.5)
    pyautogui.press("enter")  
    sleep(1)





