from machine import Pin as pin
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
puerto=[15,2,16,4,5,22,21,19,23,18]
tod=[]
for i in puerto:
  tod.append (pin(i,pin.OUT))
print (tod)
def derecha():
  for i in tod:
    for j in range (2):
      i.value(not i.value())
    pausam(100)
while True:
  derecha()