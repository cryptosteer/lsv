""" Fibonacci by Jesus Lemus """

end_number = int(raw_input("Ingresa el numero de iteraciones: "))

rango = range(end_number)

def Fibonacci(rango):

    for i in rango:
        if i == 0:
            print(i)
            buffer_item = i
            buffer_item_second = i + 1
            
            buffer_result = buffer_item + buffer_item_second

            print(buffer_item_second)
        elif i == 2 or i == 3:
            buffer_item = buffer_item_second
            buffer_item_second = buffer_result
            
            buffer_result = buffer_item + buffer_item_second

            print(buffer_item_second)
        elif i > 4:
            buffer_item = buffer_item_second
            buffer_item_second = buffer_result
            
            buffer_result = buffer_item + buffer_item_second

            print(buffer_item_second)
        

Fibonacci(rango)