## **APIRestConPython**

------

## **Instalación:** 

**Requisitos**: 

- Python 3.x.x

Para instalar, clona el respositorio en tu disco local. Luego abre la carpeta con cmd o powershell:

```
cd C:\Users\user\Documents\APIRestConPython
```

Una vez ahí, ejecutar el comando para instalar las dependencias:

```
pip install -r requirements.txt
```

Listo!, el programa ya esta instalado. Ahora hay que crear el archivo que almacenará las claves de cifrado. Para eso en la carpeta raíz creamos un archivo que se llame **.env**. Y en la primer línea de código escribimos clave especificada en la consigna de la siguiente manera:

```
SECRET_KEY=*********
```

Lo siguiente es iniciar el programa, con el comando que se detalla a continuación, posicionados sobre la carpeta que abrimos mas arriba:

```
python manage.py runserver
```

------

## Llamando a la API:

La API consta de 3 endpoints: */login,* */me*, */get-links*. Para ejecutarlos usaremos [POSTMAN](https://www.postman.com/).



**/login**: este endpoint nos permite loguearnos, nos devuelve dos **tokens**: 

- access token: nos permite acceder a los otros endpoints. Tiene una duración limitada.
- refresh token: se usa para refrescar el access token cuando este se expira.

Ejemplo:

```
http://127.0.0.1:8000/login

body
{
    "username":"demo@usuario.com",
    "password": "aquiLaPassDeLaConsigna"
}
```

En POSTMAN sería algo asi:

![](https://raw.githubusercontent.com/JoaquinChartier/APIRestConPython/master/DocsImages/1.png)

Nos devuelve una respuesta como esta:

![](https://raw.githubusercontent.com/JoaquinChartier/APIRestConPython/master/DocsImages/2.png)



**/me**: este endpoint nos devuelve algunos datos relacionados al payload del token y nuestro username (email). En los headers debemos enviar el access token recibido en el proceso anterior de la manera que se muestra en el ejemplo.

Ejemplo: 

```
http://127.0.0.1:8000/me

headers
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjo...
Content-Type: application/json
```

En POSTMAN sería algo asi:

![](https://raw.githubusercontent.com/JoaquinChartier/APIRestConPython/master/DocsImages/3.png)

Nos devuelve una respuesta como esta:

![](https://raw.githubusercontent.com/JoaquinChartier/APIRestConPython/master/DocsImages/4.png)



**/get-links**: este es el mas importante de todos, este endpoint recibe un enlace de una página web y un tipo de output (csv o xlsx), el servidor scrapea la página, extrae los anchors y nos devuelve un archivo para descargar. También esta protegido asi que debemos enviar el Bearer token otra vez.

Ejemplo:

```
http://127.0.0.1:8000/get-links

headers
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjo...

body
{
    "url":"https://startuplinks.world/",
    "output":"xlsx"
}
```

En POSTMAN sería algo asi:

![](https://raw.githubusercontent.com/JoaquinChartier/APIRestConPython/master/DocsImages/5.png)

Nos devuelve una respuesta como esta:

![](https://raw.githubusercontent.com/JoaquinChartier/APIRestConPython/master/DocsImages/6.png)

Que podremos descargar haciendo click en "Save Response" en la esquina superior derecha.