import RPi.GPIO as GPIO #Llamar a la libreria que permite utilizar los pines GPIO y renonmbrarla de una manera mas accesible 
import time #Llamar a la libreria que permite trabajar con funciones de manejo de tiempo

PIN_BOTON = 3 
PIN_LED = 7 

estadoBoton = 0 #Inicializar una variable para almacenar el estado del boton. 

GPIO.setmode(GPIO.BOARD) #Configurar los pines de raspberry segun la numeración física
GPIO.setup(PIN_LED, GPIO.OUT) # Configurar el PIN FÍSICO 7 como salida. 
GPIO.setup(PIN_BOTON, GPIO.IN) #Configurar el pin fisico 3 como entrada.

while True: #Ciclo infinito (void loop).
	estadoBoton = GPIO.input (PIN_BOTON) #Leer entrada digital.
	GPIO.output(7, estadoBoton) #Enviar el estado del boton al pin 7 (digitalWrite).

	if estadoBoton == 1: # si el boton esta presionado:
		print("ENCENDIDO") #imprima boton de encendido
		time.sleep(1) # Realizar una pausa de 1 seg.
	else: # Si el boton NO esta presionado, entonces:
		print("APAGADO")  # ¿ IMprime mensaje de APAGADO 
		time.sleep(1)

