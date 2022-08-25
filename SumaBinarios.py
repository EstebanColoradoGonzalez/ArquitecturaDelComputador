import RPi.GPIO as gpio
import time

gpio.setwarnings(False)

gpio.setmode(gpio.BOARD)

gpio.setup(16, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(36, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(37, gpio.OUT)

def decimal_a_binario(decimal):
	binario = bin(decimal)
	binario = binario[2:]
	print(binario)

	for indice in range(len(binario), 9, 1):
		binario = '0' + str(binario)	

	return binario


def menu():
	controlador = True
	while(controlador):
		print("Ingrese el primer numero entre 0 y 255")
		numeroUno = input()
		print("Ingrese el segundo numero entre 0 y 255")
		numeroDos = input()
		resultado = numeroUno + numeroDos
		binario = decimal_a_binario(resultado)
		if(binario[1] == '1'):
			gpio.output(16, True)
		else:
			gpio.output(16, False)
		if(binario[2] == '1'):
			gpio.output(18, True)
		else:
			gpio.output(18, False)
		if(binario[3] == '1'):
			gpio.output(22, True)
		else:
			gpio.output(22, False)
		if(binario[4] == '1'):
			gpio.output(36, True)
		else:
			gpio.output(36, False)
		if(binario[5] == '1'):
			gpio.output(11, True)
		else:
			gpio.output(11, False)
		if(binario[6] == '1'):
			gpio.output(13, True)
		else:
			gpio.output(13, False)
		if(binario[7] == '1'):
			gpio.output(15, True)
		else:
			gpio.output(15, False)
		if(binario[8] == '1'):
			gpio.output(37, True)
		else:
			gpio.output(37, False)

menu()
