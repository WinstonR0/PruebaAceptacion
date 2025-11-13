# Se debe importar el web driver para que detecte el navegador
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# se abre el navegador
driver = webdriver.Chrome()
# se llama al html
driver.get('file:///Users/rosdri/Documents/PruebaAceptacion/PruebaAceptacion/calculadora.html')


# Se encuentran los botones y se envian los datos
driver.find_element(By.ID, 'numero1').send_keys('-9')
driver.find_element(By.ID, 'numero2').send_keys('5.10')


# Se debe poner el texto dentro del boton, no como tal el ID
driver.find_element(By.XPATH, "//button[contains(text(), 'Suma')]").click()

# Se debe esperar la respuesta
time.sleep(2)
resultado = driver.find_element(By.ID,'resultado').text.strip() # Strip para quitar espacios

# Se hace el test
#PRIMERA FORMA

if '15' in resultado:
    print ("Prueba #1 suma superada")
else:
    print("Prueba #1 suma fallida", resultado)

'''
SEGUNDA FORMA

if resultado.lower == 'resultado: 15'.lower():
    print ("Prueba de aceptacion superada")
else:
    print("Prueba de aceptacion fallida", resultado)
'''

# Resta
# Se refresca la pagina
driver.refresh()

time.sleep(2)
driver.find_element(By.ID, "numero1").send_keys('10')
driver.find_element(By.ID, "numero2").send_keys('-10')

driver.find_element(By.XPATH, "//button[contains(text(), 'Resta')]").click()

time.sleep(2)
resultado = driver.find_element(By.ID,'resultado').text.strip() # Strip para quitar espacios

# Se hace el test

if '5' in resultado:
    print ("Prueba #2 resta superada")
else:
    print("Prueba #2 resta fallida", resultado)


# Multiplicacion
# Se refresca la pagina
driver.refresh()

time.sleep(2)

driver.find_element(By.ID, "numero1").send_keys('100')
driver.find_element(By.ID, "numero2").send_keys('0')

driver.find_element(By.XPATH, "//button[contains(text(), 'Multiplicacion')]").click()

time.sleep(2)
resultado = driver.find_element(By.ID,'resultado').text.strip() # Strip para quitar espacios

# Se hace el test

if '500' in resultado:
    print ("Prueba #3 Multiplicacion superada")
else:
    print("Prueba #3 Multiplicacion fallida", resultado)



# Division
# Se refresca la pagina
driver.refresh()

time.sleep(2)

driver.find_element(By.ID, "numero1").send_keys('-49218273')
driver.find_element(By.ID, "numero2").send_keys('50,817373')

driver.find_element(By.XPATH, "//button[contains(text(), 'Division')]").click()

time.sleep(2)
resultado = driver.find_element(By.ID,'resultado').text.strip() # Strip para quitar espacios

# Se hace el test

if '500' in resultado:
    print ("Prueba #4 Division superada")
else:
    print("Prueba #4 Divison fallida", resultado)

# Se cierra el navegador
#driver.quit()
