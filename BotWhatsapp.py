import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
import time


driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# Iniciar el driver de Selenium
driver.get('https://web.whatsapp.com/')

# Escanear el código QR
input("Escanee el código QR y presione Enter")

# Lista de números de contactos
numbers_list = ["numero telefono"]

# Bucle para enviar mensajes a cada número
for number in numbers_list:
    # Seleccionar el contacto
    contact = driver.find_element_by_xpath(f'//span[@title = "{number}"]')
    contact.click()

    # Enviar el mensaje
    message = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    message.send_keys("Hola, ¿cómo estás?")
    sendbutton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]')
    sendbutton.click()

# Cerrar el driver
driver.quit()