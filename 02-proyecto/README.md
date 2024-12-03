# 02-proyecto

Este README es temporal, solo para mostrar cómo se podrían ejecutar [`api`](./api/).

En la carpeta [`api`](./api/) es donde estaría alojada la API, en el archivo [`main.py`](./api/main.py) especificamente, si se ejecuta la API con uvicorn directamente (es decir, ejecutando en consola `uvicorn api.main:app` por ejemplo), pues no habria que realizar nada, pero para ejecutar el archivo sin ningun problema, escribiendo `python` en consola, se deben seguir los siguientes comandos

``` bash
$cd 02-proyecto
02-proyecto$python -m api.main
```

Y ya con eso debería bastar
