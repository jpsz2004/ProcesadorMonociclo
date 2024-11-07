# Procesador Monociclo
Este proyecto contiene el circuito combinacional de un procesador monociclo y sus componentes en la aplicación para simulación "Digital". 


## Salvedades
> * La aplicación usada para realizar los componentes fue "Digital" Tomado de [https://github.com/hneemann/Digital.git]  
> * "Digital" necesita que la memoria esté precargada. Es necesario que al intentar simular el circuito, sea necesario precargar la memoria según la dirección en donde se guardó todo el proyecto. El archivo se llama 'insts.hex'  
> * Sin precargar la memoria, el proyecto mostrará todo en cero ya que la memoria del programa no tiene datos almacenados.  
> * Las instrucciones de corrimiento sll, srl, sra, slt, sltu aún no se ejectuan como una operación original en la ALU. En su defecto, para esta versión, los displays muestran el nombre de la instrucción.

# APÉNDICES

Para la construcción de este procesador y su correcto funcionamiento es fundamental comprender la carga de la memoria del programa en "Digital". 

>[!NOTE]
> Se debe precargar un archivo con extensión .hex que debe seguir el formato intel hex. Este formato es solicitado por "Digital".

## Formato INTEL HEX
![](https://www.flx.cat/media/2010-11-17/featured.jpg)



