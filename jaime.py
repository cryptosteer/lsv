n = 5
#Inicializando la serie
ser = [i if i<=1 else 0 for i in range(n)]
# Calculando la serie fibonnaci
for i in range(2, n):
 	ser[i] = ser[i-1] + ser[i-2]
print(ser)
