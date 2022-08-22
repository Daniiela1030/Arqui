from machine import Pin as pin
import utime
led1=pin(15,pin.OUT)
led2=pin(2,pin.OUT)
led3=pin(16,pin.OUT)
led4=pin(4,pin.OUT)
led5=pin(5,pin.OUT)
led6=pin(22,pin.OUT)
led7=pin(21,pin.OUT)
led8=pin(19,pin.OUT)
led9=pin(23,pin.OUT)
led10=pin(18,pin.OUT)
todos = [led1,led2,led3,led4,led5,led6,led7,led8,led9,led10]
def derecha():
 for elemento in todos:
  elemento.value(1)
  utime.sleep_ms(50)
  elemento.value(0)
  utime.sleep(0.2)
def izquierda():
 for elemento in reversed(todos):
   elemento.value(1)
   utime.sleep(0.05)
   elemento.value(0)
   utime.sleep(0.2)
while True:
  derecha()
