# RotacionCuboOpenGL
Pregunta 4 de la primera pc de matematica computacional

# Controles
* Click izquierdo: rotar horario respecto al eje y
<img src="https://raw.githubusercontent.com/gestorHan/RotacionCuboOpenGL/master/images/izq.png" height="48" width="48" >
* Click derecho: rotar antihorario respecto al eje y
<img src="https://raw.githubusercontent.com/gestorHan/RotacionCuboOpenGL/master/images/der.png" height="48" width="48" >
* Espacio: rotar antihorario de 0°-> 30° y horario de 30° -> 0° respecto al vector (1,1,1)
<img src="https://github.com/gestorHan/RotacionCuboOpenGL/blob/master/images/space.jpg" height="20" width="80" >

# Instrucciones de ejecución
0. Cambiar la terminal a la carpeta donde se realizara la descarga y clonar el repositorio
```console
  cd <carpeta donde se descargara>
  git clone https://github.com/gestorHan/RotacionCuboOpenGL.git
  cd RotacionCuboOpenGL/
  ```  
  1. Verificar la variable de entorno correspondiente a python>=3.6.9 Puede ser: 
  ```console
  python --version
  ``` 
  ..o 
  ```console
  python3 --version
  ``` 
  ..-Apartir de ahora nos referiremos a esta variable como ```python3```

  2.Instalar librerias necesarias
  ```console
    python3 -m pip install PyOpenGL PyOpenGL_accelerate
    python3 -m pip install glfw
    python3 -m pip install numpy
  ```
  5.Ejecutar index.py
  ```console
    python3 index.py
   ```
  6.Si se obtiene el error
  ```console
   ImportError("Failed to load GLFW3 shared library.")
   ```
  Instalar ejecutando:
  ```console
    sudo apt-get install libglfw3
    suedo apt-get install libglfw3-dev
  ```
  
  
