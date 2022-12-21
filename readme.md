# <span style="color:red">Pasos para ejecutar</span>

Realizar todo el proceso conectados a internet la 1ra vez que se vaya a correr el proyecto

## Correr Backend
### Situarse dentro de la carpeta backend.
```bash
>cd backend
```
### Instalar Python
https://www.python.org/downloads/
### Instalar Dependencias del requirements.txt, haciendo:
```bash
>pip install -r requirements.txt
```
### Correr los siguientes comandos:
```bash
>python main.py
```

```bash 
>python manage.py collectstatic
```

```bash 
>python manage.py runserver 
```

## Correr FrontEnd
### Instalar nodejs
https://nodejs.org/es/download/
### Instalar vue-quasar:
```bash 
>npm install -g @quasar/cli 
```

### Instalar dependencias de npm del proyecto en frontend:
```bash 
>cd frontend 
```

```bash 
>npm install 
```

### Ejecutar el proyecto frontend
```bash 
>quasar dev 
```

