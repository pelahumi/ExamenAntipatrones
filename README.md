# ExamenAntipatrones

Link a mi repositorio de [GitHub](https://github.com/pelahumi/ExamenAntipatrones)

## Identificación del antipatrón
Podemos ver que el código proporcionado es una única función llamada ```calcular()``` que almacena todas los tipos de operaciones aritméticas que se quieren realizar. Esta función filtra a través de condicionales el tipo de operación que quiere realizar el usuario.

## Refactorización del código
Para mejorar y hacer más legible dicho código, cambiamos lo siguiente: Creamos una clase llamada ```Calculadora``` que será la encargada de gestionar las operaciones aritméticas. Además, para cada operación hemos creado un método que la lleve a cabo.

Así nuestro código queda mucho más claro, ya que las operaciones quedan definidas por separado, y más legible, ya que al separar todas las operaciones en diferentes funciones el código se hace más comprensible.
