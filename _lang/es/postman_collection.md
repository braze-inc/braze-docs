---
nav_title: Cartero y solicitudes de muestras
article_title: Cartero y solicitudes de muestras
page_order: 3
description: "Este artículo de referencia cubre la colección Braze Postman, qué es, cómo configurar y utilizar la colección, así como la forma de editar y enviar solicitudes."
page_type: reference

---

# Cartero y solicitudes de muestras

> Braze te permite generar solicitudes de API de muestra para todos nuestros puntos finales a través de nuestra Postman Collection. Este artículo de referencia cubre la colección Braze Postman, qué es, cómo configurar y utilizar la colección, así como la forma de editar y enviar solicitudes.

## ¿Qué es Postman?

Postman es una herramienta de edición visual gratuita para crear y probar solicitudes API. A diferencia de otros métodos para interactuar con API (por ejemplo, usando cURL), Postman te permite editar fácilmente las solicitudes API, ver la información de cabecera, y mucho más. Postman tiene la capacidad de guardar colecciones o bibliotecas de ejemplos de solicitudes API prefabricadas. Para facilitar a nuestros clientes la puesta en marcha de nuestra API REST, hemos creado una colección con ejemplos prefabricados para todos nuestros puntos finales de API.

Vea o descargue nuestra Postman Collection haciendo clic en **Ejecutar en Postman** en nuestra [documentación de Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) para empezar.

## Utilización de la colección Braze Postman

Si tienes una cuenta Postman (puedes descargar las versiones para macOS, Windows y Linux desde el [sitio web de Postman](https://www.getpostman.com)), puedes abrir nuestra documentación Postman en tu propia aplicación Postman haciendo clic en el botón naranja **Ejecutar en Postman**. A continuación, puede [crear un entorno](#setting-up-your-postman-environment), o utilizar nuestro entorno Braze REST API como plantilla, y editar las solicitudes disponibles `POST` y `GET` para adaptarlas a sus propias necesidades.

### Configuración del entorno Postman

{% raw %}
Braze Postman Collection utiliza una variable de plantilla, `{{instance_url}}`, para sustituir la URL de la API REST de su instancia Braze en las solicitudes preconstruidas, y la variable `{{api_key}}` para su clave de API. En lugar de tener que editar manualmente todas las solicitudes de la Colección, puede configurar esta variable en su entorno Postman. Puede seleccionar nuestra plantilla de entorno (Braze REST API Environment Template) en el menú desplegable y sustituir los valores de las variables por los suyos propios, o puede configurar su propio entorno.
{% endraw %}

Para configurar tu propio entorno, realiza los siguientes pasos:

1. En la pestaña **Espacios de trabajo**, seleccione **Entornos**.
2. Haz clic en el botón **+** más para crear un nuevo entorno.
3. Dale un nombre a este entorno (por ejemplo, "Solicitudes de API Braze") y añade claves para `instance_url` y `api_key` con los valores correspondientes a tu [instancia de Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) y a [tu clave de API REST Braze]({{site.baseurl}}/api/api_key/).
4. Haga clic en **Guardar**.

{% alert note %}
En los cuerpos de solicitud de `POST`, `api_key` debe ir entre comillas: `"MY-API-KEY-EXAMPLE"`. En las URL de `GET`, no debería serlo. Ya te hemos proporcionado este formato en los cuerpos de solicitud de esta documentación `POST`, las URL de `GET` y la plantilla de entorno para `YOUR-API-KEY-HERE`.
{% endalert %}

![Añadir variables para la clave API y la URL de instancia al entorno Braze REST API en Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Utilizar las solicitudes preconstruidas de la colección

Una vez configurado el entorno, puede utilizar cualquiera de las solicitudes preconfiguradas de la colección como plantilla para crear nuevas solicitudes de API. Para empezar a utilizar una de las peticiones preconstruidas, haga clic en ella dentro del menú **Colecciones** de Postman. Esto abrirá la solicitud como una nueva pestaña en la ventana principal de la aplicación Postman.

En general, los puntos finales de la API de Braze aceptan dos tipos de solicitudes: `GET` y `POST`. Dependiendo del método `HTTP` que utilice el punto final, tendrá que editar la solicitud pre-construida de forma diferente.

#### Editar una solicitud POST

Para editar una solicitud `POST`, abra la solicitud y vaya a la sección **Cuerpo** del editor de solicitudes. Para facilitar la lectura, seleccione el botón de opción **sin formato** para dar formato al cuerpo de la solicitud `JSON`.

![Pestaña del cuerpo al editar una petición POST User Track en Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Editar una solicitud GET

Al editar una solicitud `GET`, edite los parámetros pasados en la URL de la solicitud. Para ello, seleccione la pestaña **Parámetros** y edite los pares clave-valor en los campos que aparecen.

![Pestaña Params al editar una solicitud GET Query List of Unsubscribed Email Addresses en Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Envía tu solicitud

Cuando tu solicitud API esté lista, haz clic en **Enviar**. La solicitud se envía y los datos de respuesta se rellenan en una sección debajo del editor de solicitudes. Desde aquí, puedes ver los datos sin procesar devueltos por la API de Braze, el código de respuesta HTTP, el tiempo que ha tardado en procesarse la solicitud y la información del encabezado.

![Ejemplo de datos de respuesta del cuerpo de una solicitud POST con un estado de 201 Creado y un tiempo de respuesta de 269 milisegundos.]({% image_buster /assets/img_archive/postman_response.png %})

