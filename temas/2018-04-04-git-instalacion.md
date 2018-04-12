[Principal](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410)

# Instalación de Git
## Ventajas
- **Control de Versiones**: Poder identificar quién y qué cambios se han realizado en un proyecto.
- **Sistema de Respaldo:**: El proyecto es almacenado en uno o varios repositorios, y que incluso pueden estar ubicados remotamente.
- **Popularidad**: Es quizá el sistema de control de versiones más utilizado. Esto permite que existan sitios web que alojan, incluso de forma gratuita, repositorios remotos, como por ejemplo: [Github](https://github.com) y [BitBucket](https://bitbucket.com)

#### Trabajo compartido
![Repositorios compartidos](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410/blob/master/temas/imagenes/git/shared-repository.png)

#### Ramificaciones
![Ramificaciones](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410/blob/master/temas/imagenes/git/git-flow.jpg)

## Instalación
El archivo binario se puede descargar del sitio oficial: https://git-scm.com/downloads.

En ese mismo lugar encuentra una lista de programas con interfaces gráficas, que permiten una manipulación sencilla en Git: https://git-scm.com/downloads/guis

### Comprobación
El binario se instala como cualquier otro. Sin embargo es necesario determinar que está instalado para ello diríjase a la terminal y digite el comando: 
```bash
git
```
## Configuración inicial
Para evitar algunos problemas relacionados con la configuración del sistema, es necesario establecer ciertos valores iniciales.

- Para definir la identidad del usuario:

```bash
git config --global user.name “Nombre usuario”
git config --global user.email usuario@ejemplo.com
```
- Para determinar el comportamiento de Git
```bash
git config --global core.filemode false
git config --global core.autocrlf true
git config --global core.ignorecase false
git config --global rerere.enabled true
git config --global color.ui true
git config --global format.pretty oneline
```

## Estados de Git
![Estados](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410/blob/master/temas/imagenes/git/fases.jpg)

---
[Principal](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410)