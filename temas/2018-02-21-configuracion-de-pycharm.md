---
published: true
---
### Ventajas de utilizar un IDE
Por lo general, los IDEs tienen ya configurados elementos que permiten un proceso completo para proyectos de diversa índole. Esto puede ser un tanto negativo si se piensa que conocer los pasos necesarios para configurar un ambiente de trabajo son importantes.

Uno de los IDE más populares en la actualidad es PyCharm, del cual se mostrará como iniciar un proyecto.

### Definición
Una vez instalada la aplicación es necesario configurar o definir algunos elementos a fin de establecer proyectos hechos en Python.

Hay dos tipos de proyecto:
1. Proyecto con virtualenv: Este tipo de proyecto crear un ambiente virtual en el cual es contenido las librerías estándar y de terceros, los cuales son independientes de los paquetes instalados por parte de Python.
2. Proyecto simple: Este no almacena ninguna librería y es un proyecto más liviano.

#### 1. Crear un proyecto

![Crear nuevo proyecto](/public/images/pycharm/1.PNG)

#### 2. Definir el nombre del proyecto
En este caso se encuentra subrayado el nombre por defecto del proyecto, por lo que es necesario cambiarlo por el definitivo.

![Cambio de nombre de proyecto](/public/images/pycharm/2.PNG)

#### 3. Definir un proyecto con virtualenv
En este caso se define que se utilizará `virtualenv` dentro del proyecto. Esta herramienta permite aislar las librerías del proyecto. A fin de que no provoque problemas en las configuraciones de otros proyectos. 

Se puede observar las opción **Inherit global site-packages**, esta indica, si se selecciona que se tomaran en consideración las librerías base que están instaladas globalmente. En caso de no seleccionar esta opción el proyecto copiará localmente dichas librerías, quedando aisladas completamente.

![Virtualenv](/public/images/pycharm/3.PNG)

Se puede observar las librerías y archivos instalados. Lo cual hace que este tipo de proyectos contengan un número significativo de archivos previos a cualquiera que sea creado por el usuario.

![Librerias en virtualenv](/public/images/pycharm/4.PNG)

#### 4. Definir un proyecto sin virtualenv
Para proyecto más sencillos donde no será necesario colocar librerías de terceros, esta puede ser la mejor opción. Ya que no se cargan archivos que al final no se necesitarán. En este caso no se ha definido el interprete a utilizar. Como lo muestra el mensaje de advertencia.
Para seleccionar se da clic en el boton (logo engranaje).

![Proyecto sencillo](/public/images/pycharm/5.PNG)

Luego se selecciona el tipo de interprete que se utilizará. En este caso **Virtualenv Environment**, luego se escoje el archivo del interprete de Python que se ha instalado previamente. Para este caso el directorio es: `c:\Python36\python.exe`. Luego se selecciona la casilla **Make available to all projects**. Con esto no será necesario configurarlo de nuevo.

![Establecer interprete](/public/images/pycharm/7.PNG)

Una vez definido el interprete presione el botón **Crear** y tendrá una proyecto más ligero.

![Crear proyecto](/public/images/pycharm/8.PNG)

Como se puede observar con esta configuración no se observa ningun archivo agregado, con lo cual el tamaño de la carpeta es sumamente pequeño.

![Proyecto sin virtualenv](/public/images/pycharm/9.PNG)
