#Cálculo del complemento A2 de un número hexadecimal de 1 byte
def a2Complement(numHexa):
    num = bin(int(numHexa, 16))[2:]
    num = num.zfill(8)
    
    num = list(num)

    for i in range(len(num)):
        if num[i] == '0':
            num[i] = '1'
        else:
            num[i] = '0'
    
    num = ''.join(num) 
    num = bin(int(num, 2) + 1)[2:]
    num = num.zfill(8)
    num = hex(int(num, 2))[2:].upper()

    return num

#Cálculo del checksum de un mensaje
def checkSum(expressionHexa):
    #Se divide la expresion en partes de 2 caracteres
    expressionHexa = [expressionHexa[i:i+2] for i in range(0, len(expressionHexa), 2)]
    #Sumar los valores de los bytes
    sum = 0
    for i in expressionHexa:
        sum += int(i, 16)
    
    #Convertir la suma a hexadecimal
    sum = hex(sum)[2:].upper()

    #Tomar solo los últimos 8 bits
    sum = sum[-2:]

    return a2Complement(sum)

if __name__ == "__main__":
    #Se pide el mensaje hasta fin de archivo

    '''
    Ejemplo de entrada: 0400000000500393 (Todo el formato en una sola linea)
    '''
    while True:
        try:
            expression = input("Ingrese la expresión en hexadecimal: ")
            print(checkSum(expression))
        except EOFError:
            break
