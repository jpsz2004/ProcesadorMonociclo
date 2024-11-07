# PROCESADOR MONOCICLO
Este proyecto contiene el circuito combinacional de un procesador monociclo para arquitectura RISC-V y sus componentes en la aplicación para simulación "Digital". 


## Salvedades
> * La aplicación usada para realizar los componentes fue "Digital" Tomado de [https://github.com/hneemann/Digital.git]  
> * "Digital" necesita que la memoria esté precargada. Es necesario que al intentar simular el circuito, se precargue la memoria según la dirección en donde se guardó todo el proyecto. El archivo se llama:
```
insts.hex
```  
> * Sin precargar la memoria, el proyecto mostrará todo en cero ya que la memoria del programa no tiene datos almacenados.  
> * Las instrucciones de corrimiento sll, srl, sra, slt, sltu aún no se ejectuan como una operación original en la ALU. En su defecto, para esta versión, los displays muestran el nombre de la instrucción.
> * Si una de las instruccions no sigue el formato adecuado o tiene errores en su formato, "Digital" mostrará error.
> * Este procesador no procesa pseudo instrucciones, sin embargo estas se pueden traducir fácilmente a instrucciones canónicas del RISC-V

# APÉNDICES

Para la construcción de este procesador y su correcto funcionamiento es fundamental comprender la carga de la memoria del programa en "Digital". 

>[!NOTE]
> Se debe precargar un archivo con extensión .hex que debe seguir el formato intel hex. Este formato es solicitado por "Digital".

## Formato INTEL HEX
![](https://www.flx.cat/media/2010-11-17/featured.jpg)

>[!NOTE]
> El formato debe seguirse al construir el archivo .hex e indica lo siguiente:
> * Amarillo: Son los dos puntos que dan inicio.
> * Verde: Estos dos digitos indican de cuantos bytes es la instrucción.
> * Morado: Son cuatro dígitos que indican la dirección de memoria donde se va a cargar la instrucción.
> * Rojo: El tipo de guardado.
> * Azul: Dependiendo de la cantidad de bytes establecidos, se escribe la instrucción.
> * Gris: Es el checksum.

## Checksum

El checksum es una función matemática de redundancia cuyo principal objetivo es el de detectar cambios malintencionados o accidentales en la instrucción. Es necesario que esté calculada correctamente, de lo contrario, "Digital" reconoce que es un error de checksum y no comenzará la simulación.  

>[!NOTE]
> Para calcular el checksum se deben seguir los siguientes pasos:
> * Se suman todos los bytes (de a 2 caracteres del mensaje) de la línea (excepto el checksum) en hexadecimal.
> * Se toman los últimos dos dígitos de la suma en hexadecimal. (Último byte)
> * Se realiza el complemento A2 del valor anterior y ese es el checksum

Calcular esto a mano puede ser tedioso, por lo tanto, para este proyecto, se realizó un programa que calcula el checksum para mensajes de este tipo.  
Para ejecutar este programa, estando en el directorio mismo de este proyecto, ejecuta: 
```
python checksum.py
```
Posteriormente, ingresa la linea hexadecimal a la cual le deseas calcular el checksum sin poner ':'

## Pruebas
Para la prueba de este procesador, se pueden extraer instrucciones compiladas de un código en C++, o el lenguaje de preferencia usando: [https://godbolt.org]  
La memoria está cargada con las instrucciones generadas para un código simple en C++:

```C++
#include <stdio.h>

int suma(){
    int x = 2;
    int y = 4;
    return x + y;
}
```

Las instrucciones que genera este código y su traducción a hexadecimal se encuentran en:
```
instruccionesTest.txt
```

## Comentario sobre la Unidad de Control
Para construir el circuito de la unidad de control y direccionar correctamente las señales según el tipo de instrucción y operación, se construyó una hoja de cálculo que permite tener control visual de cómo trabaja la unidad de control. (Adjunto al repositorio).

# COMENTARIO FINAL
Este proyectó se sustentó el día 06 del mes 11 del año 2024 para la materia "Arquitectura de Computadores" de la carrera de Ingeniería de Sistemas y Computación de la Universidad Tecnológica de Pereira.

Docente: Juan Manuel Velásquez Isaza

Presentado por: Juan Pablo Sánchez Zapata y Juan Esteban García Pulgarín


