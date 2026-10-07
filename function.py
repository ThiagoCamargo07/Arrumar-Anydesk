import pyautogui
from time import sleep
import shutil
from pathlib import Path



class Espera:
    def esperar_1_segundo():
        sleep(1)
        
    def esperar_2_segundos():
            sleep(2)
        
    
class Ação:
    def abrir_caminho(): # Abrir win + r
        pyautogui.hotkey('win', 'r')
        Espera.esperar_1_segundo()
        pyautogui.write('%appdata%', interval=0.03)
        Espera.esperar_1_segundo()
        pyautogui.press('enter')
        

    def excluir_pasta_appdata(): # excluir a pasta appdata
        Espera.esperar_2_segundos()
        pyautogui.hotkey("ctrl", "e")  
        Espera.esperar_1_segundo()
        pyautogui.write("anydesk", interval=0.03)
        Espera.esperar_2_segundos()
        pyautogui.press("enter")
        Espera.esperar_2_segundos()
        pyautogui.press("down")
        Espera.esperar_2_segundos() 
        pyautogui.press("up")  
        Espera.esperar_2_segundos()
        pyautogui.hotkey('shift', 'delete') 
        Espera.esperar_2_segundos()
        pyautogui.press("enter")
        Espera.esperar_1_segundo()
        pyautogui.hotkey('alt', 'f4')
        Espera.esperar_1_segundo()
        

    def abrir_anydesk(): # Abrir anydesk novamente
        pyautogui.press("win")
        Espera.esperar_1_segundo()
        pyautogui.write("anydesk", interval=0.03)
        Espera.esperar_2_segundos()
        pyautogui.press("enter")  
        Espera.esperar_1_segundo()





