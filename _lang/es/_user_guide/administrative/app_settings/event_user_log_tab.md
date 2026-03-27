---
nav_title: Registro de usuarios del evento
article_title: Registro de usuarios del evento
page_order: 7
page_type: reference
description: "Este artículo de referencia trata del registro de usuarios del evento, que puede ayudarte a depurar o solucionar problemas en tu integración de Braze."

---

# Registro de usuarios del evento

> El registro de usuarios del evento puede ayudarte a desglosar, depurar o solucionar problemas de otro tipo en tu integración de Braze. Esta pestaña te ofrece un registro de errores que detalla el tipo de error, a qué aplicación está asociado, cuándo se produjo y, a menudo, la oportunidad de ver los datos sin procesar asociados.

{% alert tip %}
Además de este artículo, también recomendamos consultar nuestro curso de Braze Learning sobre [herramientas de control de calidad y depuración](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que trata sobre cómo utilizar el registro de usuarios del evento para llevar a cabo tu propia solución de problemas y depuración.
{% endalert %}

Para acceder al registro, ve a **Configuración** > **Registro de usuarios del evento**.

Para encontrar tus registros fácilmente, puedes filtrar en función de:

* SDK o API
* Nombres de aplicaciones
* Período de tiempo
* Usuario

Cada registro se divide en varias secciones, que pueden incluir:

* Atributos de dispositivo
* Atributos del usuario
* Eventos
* Eventos de campaña
* Datos de respuesta

Selecciona el icono **Expandir datos** para mostrar los datos JSON sin procesar de ese registro concreto.

![El icono "Expandir datos" junto a un registro concreto.]({% image_buster /assets/img_archive/expand_data.png %})

Los registros de usuarios del evento permanecerán en el dashboard durante los 30 días posteriores a su registro.

![Registros sin procesar de eventos]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Solución de problemas

### Faltan registros del SDK para los usuarios de prueba

Si has añadido un usuario a un grupo interno, pero no muestra ningún registro del SDK en el registro de usuarios del evento, puede deberse a que falta una opción de configuración. Para capturar los registros del SDK, asegúrate de seleccionar **Registrar eventos de usuario para los miembros del grupo** en la **Configuración del grupo interno** para ese [grupo interno]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/).

### Retraso en la actualización de los registros

Esto puede ser una lentitud normal de nuestra API.

Cuando llamas a métodos del SDK, el SDK suele almacenar esos eventos en caché local y los envía al servidor cada 10 segundos. Nuestra cola de procesamiento de trabajos puede tardar desde un segundo hasta varios minutos en ingerir los eventos, según la carga total en ese momento.  

Si quieres que los eventos lleguen lo antes posible, prueba a llamar a la función `requestImmediateDataFlush()`.

### Fallos en la impresión de mensajes dentro de la aplicación

Si un mensaje dentro de la aplicación no se muestra, puedes encontrar el motivo en el registro de usuarios del evento expandiendo los datos JSON sin procesar de la solicitud del SDK correspondiente y buscando el campo `error_code` en la respuesta. El `error_code` identifica el motivo específico por el que falló la impresión (por ejemplo, un valor de color no válido o un problema de renderizado). Comparte este código de error con el [soporte de Braze]({{site.baseurl}}/braze_support/) si se necesita una investigación más detallada.

### El final y el inicio de la sesión tienen marcas de tiempo similares (iOS)

El registro de usuarios del evento muestra la marca de tiempo del momento en que se notificó a Braze que la sesión había finalizado, que será milisegundos antes de que se inicie la siguiente sesión. Braze no puede saber si la sesión ha finalizado antes de que se vuelva a abrir la aplicación porque iOS es agresivo a la hora de detener la ejecución de subprocesos cuando la aplicación está en segundo plano, por lo que no se pueden enviar datos a Braze hasta que se vuelva a abrir la aplicación.

Mientras que la hora de finalización de la sesión se especificará como segundos antes del inicio de la sesión, cuando el evento se envía, la duración de la sesión se envía por separado y es correcta, reflejando el tiempo que la aplicación estuvo abierta. Por lo tanto, este comportamiento no afecta al filtro `Median Session Duration`.

En relación con las sesiones de usuario, puedes utilizar Braze para supervisar datos como:

- Cuántas sesiones ha tenido un usuario
- Cuándo fue la última vez que un usuario inició una sesión
- Si el usuario inicia una sesión tras recibir una campaña
- Cuál es la duración media de la sesión del usuario

Estos comportamientos no se ven afectados por el evento de fin de sesión que se envía en la siguiente sesión.