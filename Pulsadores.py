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

def secuenciaUno():
	contador = 0
	while(contador != 2):
		gpio.output(16, True)
		gpio.output(18, True)
		gpio.output(22, True)
		gpio.output(36, True)
		gpio.output(11, True)
		gpio.output(13, True)
		gpio.output(15, True)
		gpio.output(37, True)
		time.sleep(1)
		gpio.output(16, False)
		time.sleep(1)
		gpio.output(18, False)
		time.sleep(1)
		gpio.output(22, False)
		time.sleep(1)
		gpio.output(36, False)
		time.sleep(1)
		gpio.output(11, False)
		time.sleep(1)
		gpio.output(13, False)
		time.sleep(1)
		gpio.output(15, False)
		time.sleep(1)
		gpio.output(37, False)
		time.sleep(2)
		contador = contador + 1

def secuenciaDos():
	contador = 0
	while(contador != 2):
		gpio.output(16, True)
		gpio.output(18, True)
		gpio.output(22, True)
		gpio.output(36, True)
		gpio.output(11, True)
		gpio.output(13, True)
		gpio.output(15, True)
		gpio.output(37, True)
		time.sleep(1)
		gpio.output(36, False)
		gpio.output(11, False)
		time.sleep(1)
		gpio.output(22, False)
		gpio.output(13, False)
		time.sleep(1)
		gpio.output(18, False)
		gpio.output(15, False)
		time.sleep(1)
		gpio.output(16, False)
		gpio.output(37, False)
		time.sleep(2)
		contador = contador + 1

def secuenciaTres():
	contador = 0
	while(contador != 2):
		gpio.output(16, True)
		gpio.output(18, True)
		gpio.output(22, True)
		gpio.output(36, True)
		gpio.output(11, True)
		gpio.output(13, True)
		gpio.output(15, True)
		gpio.output(37, True)
		time.sleep(1)
		gpio.output(16, False)
		gpio.output(37, False)
		time.sleep(1)
		gpio.output(18, False)
		gpio.output(15, False)
		time.sleep(1)
		gpio.output(22, False)
		gpio.output(13, False)
		time.sleep(1)
		gpio.output(36, False)
		gpio.output(11, False)
		time.sleep(2)
		contador = contador + 1

def secuenciaCuatro():
	contador = 0
	while(contador != 2):
		gpio.output(16, True)
		gpio.output(18, True)
		gpio.output(22, True)
		gpio.output(36, True)
		gpio.output(11, True)
		gpio.output(13, True)
		gpio.output(15, True)
		gpio.output(37, True)
		time.sleep(1)
		gpio.output(18, False)
		time.sleep(1)
		gpio.output(36, False)
		time.sleep(1)
		gpio.output(13, False)
		time.sleep(1)
		gpio.output(37, False)
		time.sleep(2)
		contador = contador + 1

def menu():
	while(True):
		

menu()
