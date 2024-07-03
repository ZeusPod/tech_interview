## INSTALACION 

correr el siguiente comando para instalar las dependencias

```sh 
pip install -r requirements.txt

```

## base de datos

Se debe crear una base de datos postgresql o en su defecto cargar el archivo db.sql
que se encuentra en siguiente enlace 

https://drive.google.com/file/d/1ssV_NVkGZ5qQY3NqKuwbCH4Z5ZaP9ifx/view?usp=sharing


 ## archivo .env
una vez cargada la base de datos se debe crear un archivo 

.env en la raiz del proyecto

con las siguientes variables de entorno

DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=


## correr el proyecto 

```sh

python app.py

```


#### generar pdf ejemplo

localhost:5000/generate_pdf/1



