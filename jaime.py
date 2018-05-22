from pprint import pprint
import time
n = 4000
start = time.perf_counter()
#Inicializando la serie
ser = [i if i<=1 else 0 for i in range(n)]
# Calculando la serie fibonnaci
for i in range(2, n):
 	ser[i] = ser[i-1] + ser[i-2]
end = time.perf_counter()
pprint(ser)
print("="*30+"\n","Calculada en {} segundos".format(end-start))
