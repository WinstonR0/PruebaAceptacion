# Se debe importar el web driver para que detecte el navegador
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# se abre el navegador
driver = webdriver.Chrome()
# se llama al html
driver.get('file:///Users/rosdri/Documents/PruebaAceptacion/PruebaAceptacion/calculadora.html')


# Se encuentran los botones y se envian los datos
driver.find_element(By.ID, 'numero1').send_keys('9')
driver.find_element(By.ID, 'numero2').send_keys('5')
# se usa XPTAH ya que se debe buscar el nombre por la funcion debido a que hay mas de un boton ygit remote add origin https://<TOKEN>@github.com/WinstonR0/PruebaAceptacion.git


#Se espera a que el boton sea clickeable
# Se debe poner el texto dentro del boton, no como tal el ID
driver.find_element(By.XPATH, "//button[contains(text(), 'Suma')]").click()

# Se debe esperar la respuesta
time.sleep(3)
resultado = driver.find_element(By.ID,'resultado').text.strip() # Strip para quitar espacios

# Se hace el test
#PRIMERA FORMA

if '15' in resultado:
    print ("Prueba de aceptacion superada")
else:
    print("Prueba de aceptacion fallida", resultado)

'''
SEGUNDA FORMA

if resultado.lower == 'resultado: 15'.lower():
    print ("Prueba de aceptacion superada")
else:
    print("Prueba de aceptacion fallida", resultado)
'''



# Se cierra el navegador
driver.quit()
