"""def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return num1 + num2
    if operacion == 'resta':
        return num1 - num2
    if operacion == 'multiplicacion':
        return num1 * num2
    if operacion == 'division':
        if num2 != 0:
            return num1 / num2
        else:
            print("No se puede dividir entre cero.")
    else:
        print("Operación no soportada.")"""

class Calculadora():

    def suma(self, num1, num2):
        return num1 + num2
    
    def resta(self, num1, num2):
        return num1 - num2
    
    def producto(self, num1, num2):
        return num1 * num2
    
    def division(self, num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("No se puede dividir entre cero.")
        
