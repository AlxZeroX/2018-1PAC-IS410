[Principal](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410)

# Git Remoto
## Clonar un proyecto
Si se tiene un proyecto en un repositorio remoto pero no existe un repositorio local, se puede descargar los archivos remotos:
```bash
git clone [direccion del repositorio remoto]
```
## Establecer un repositorio remoto
Si ya se tiene un repositorio local es posible incorporar un repositorio remoto. Esto funciona si existen los accesos necesarios para tal cometido.
```bash
git remote add [nombre del repositorio remoto] [direccion del repositorio remoto]
```
El nombre del repositorio remoto, por convención es **origin**.

Para visualizar el repositorio remoto:
```bash
git remote -v
```

Para eliminar el enlace a un repositorio remoto:
```bash
git remote remove [nombre del repositorio]
```

## Intercambio de información con el repositorio remoto

Para recibir cambios en archivos e incorporarlos a nuestro espacio local de trabajo se utiliza el comando:
```bash
git pull [nombre del repositorio][nombre de la rama]
```

Para recibir cambios en archivos remotos e incorporarlos posteriormente:
```bash
git fetch [nombre del repositorio][nombre de la rama]
```

Para enviar cambios al repositorio remoto:
```bash
git push [nombre del repositorio][nombre de la rama]
```

---
[Principal](https://github.com/UNAH-SISTEMAS/2018-1PAC-IS410)