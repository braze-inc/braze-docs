---
nav_title: Solución de problemas de webhook y solicitudes de contenido conectado
article_title: Solución de problemas de webhook y solicitudes de contenido conectado
page_order: 3
channel:
  - webhooks
description: "Este artículo explica cómo solucionar los códigos de error de webhook y Contenido conectado, incluyendo cuáles son los errores y los pasos para resolverlos."
---

# Solución de problemas de webhook y solicitudes de contenido conectado

> Este artículo explica cómo solucionar los códigos de error más comunes de los webhooks y el Contenido conectado, y ofrece más explicaciones sobre cómo pueden producirse estos errores en tus solicitudes.

## 4XX errores

`4XX` indican que hay un problema con la solicitud enviada al punto final. Estos errores suelen deberse a solicitudes erróneas, como parámetros mal formados, omisión de cabeceras de autenticación o URL incorrectas.

Consulta la tabla siguiente para ver los detalles del código de error y los pasos para solucionarlo:

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Código de error</th>
      <th>Qué significa</th>
      <th>Pasos para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Petición errónea</b></td>
      <td>Hay una sintaxis inválida en la petición.</td>
      <td>
        <ul>
          <li>Comprueba que la carga útil de la solicitud no contenga errores de sintaxis.</li>
          <li>Confirma que todos los campos obligatorios están incluidos y correctamente formateados.</li>
          <li>Si envías una carga útil JSON, valida la estructura JSON.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 No autorizado</b></td>
      <td>La solicitud requiere la autenticación del usuario.</td>
      <td>
        <ul>
          <li>Comprueba que se incluyen las credenciales de autenticación correctas (como claves de API o tokens) en los encabezados de solicitud.</li>
          <li>Confirma que tienes los permisos de usuario para acceder al punto final.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Prohibido</b></td>
      <td>El endpoint entiende la petición pero se niega a autorizarla.</td>
      <td>
        <ul>
          <li>Comprueba si la clave de API o el token tienen los permisos necesarios.</li>
          <li>Confirma que tienes los permisos de usuario para acceder al punto final.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 No encontrado</b></td>
      <td>El punto final no puede encontrar el recurso solicitado.</td>
      <td>
        <ul>
          <li>Comprueba si la URL del punto final contiene errores tipográficos o rutas incorrectas.</li>
          <li>Confirma que el recurso al que intentas acceder existe.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Método no permitido</b></td>
      <td>El método de solicitud es conocido por el punto final, pero no es compatible con el recurso de destino.</td>
      <td>
        <ul>
          <li>Comprueba el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el punto final admite el método que estás utilizando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Tiempo de espera de la solicitud</b></td>
      <td>El punto final ha agotado el tiempo de procesamiento de la solicitud.</td>
      <td>
        <ul>
          <li>Comprueba el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el punto final admite el método que estás utilizando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflicto</b></td>
      <td>La solicitud está incompleta debido a un conflicto con el estado actual del recurso.</td>
      <td>
        <ul>
          <li>Comprueba el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el punto final admite el método que estás utilizando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Demasiadas peticiones</b></td>
      <td>Se envían demasiadas solicitudes en un tiempo determinado.</td>
      <td>
        <ul>
          <li>Reduce el límite de velocidad en tu campaña o paso en Canvas.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## 5XX errores

`5XX` Los errores indican que hay un problema con el punto final. Estos errores suelen deberse a problemas del servidor.

| Código de error                    | Qué significa                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Error interno del servidor** | El punto final encontró una condición inesperada que le impidió completar la solicitud.                                                       |
| **502 Pasarela incorrecta**           | El punto final ha recibido una respuesta no válida del servidor ascendente.                                                                                   |
| **503 Servicio no disponible**   | El punto final no puede gestionar actualmente la solicitud debido a una sobrecarga temporal o a mantenimiento.                                                    |
| **504 Tiempo de espera de la puerta de enlace**       | El punto final no ha recibido una respuesta oportuna del servidor ascendente.                                                                               |
| **529 Anfitrión sobrecargado**       | El host del punto final está sobrecargado y no ha podido responder. |
| **598 Anfitrión no sano**        | Braze simuló la respuesta porque el host del punto final está marcado temporalmente como no saludable. Para saber más, consulta [Detección de host no sano](#unhealthy-host-detection). |
| **599 Error de conexión**      | Braze experimentó un error de tiempo de espera de conexión de red al intentar establecer una conexión con el punto final, lo que significa que el punto final puede ser inestable o estar caído. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Resolver errores 5XX

Aquí tienes consejos para la solución de problemas comunes en `5XX`:

- Revisa el mensaje de error para ver los detalles específicos disponibles en el **Registro de Actividad de Mensajes**. Para los webhooks, ve a la sección **Rendimiento en el tiempo** de la página de inicio de Braze y selecciona las estadísticas de los webhooks. Desde aquí, puedes encontrar la marca de tiempo que indica cuándo se produjeron los errores.
- Asegúrate de no enviar demasiadas peticiones que sobrecarguen el endpoint. Puedes enviar por lotes o ajustar el límite de velocidad para comprobar si así se reducen los errores.

## Detección de host no sano

Los webhooks Braze y el Contenido conectado emplean un mecanismo de detección de host no saludable para detectar cuando el host de destino experimenta una alta tasa de lentitud significativa o una sobrecarga que provoca tiempos de espera, demasiadas solicitudes u otros resultados que impiden que Braze se comunique correctamente con el punto final de destino. Actúa como salvaguarda para reducir la carga innecesaria que pueda estar causando dificultades al host de destino. También sirve para estabilizar la infraestructura de Braze y mantener velocidades rápidas de mensajería.

Los umbrales de detección difieren entre los webhooks y el Contenido conectado:
- **Para webhooks**: Si el número de **fallos supera los 3.000 en cualquier ventana de tiempo móvil de un minuto** (por combinación única de nombre de host y grupo de aplicaciones, **no** por ruta de punto final), Braze detendrá temporalmente las solicitudes al host de destino durante un minuto.
- **Para contenido conectado**: Si el número de **fallos supera los 3.000 Y la tasa de error supera el 90% en cualquier ventana de tiempo móvil de un minuto** (por combinación única de nombre de host y grupo de aplicaciones, **no** por ruta de punto final), Braze detendrá temporalmente las solicitudes al host de destino durante un minuto.

Cuando las peticiones se detienen, Braze simula respuestas con un código de error `598` para indicar la mala salud. Al cabo de un minuto, Braze reanudará las peticiones a toda velocidad si se comprueba que el anfitrión está sano. Si el anfitrión sigue sin estar sano, Braze esperará otro minuto antes de volver a intentarlo.

Los siguientes códigos de error contribuyen al recuento de fallos del detector de host insalubre: `408`, `429`, `502`, `503`, `504`, `529`.

Para los webhooks, Braze reintentará automáticamente las peticiones HTTP que fueron detenidas por el detector de host insalubre. Este reintento automático utiliza una retirada exponencial y sólo lo intentará unas pocas veces antes de fallar. Para más información sobre los errores de webhook, consulta [Errores, lógica de reintentos y tiempos de espera]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#errors-retry-logic-and-timeouts).

Para el Contenido conectado, si las solicitudes al anfitrión de destino se detienen por el detector de anfitrión insalubre, Braze continuará mostrando mensajes y seguirá su lógica Liquid como si hubiera recibido un código de respuesta de error. Si quieres asegurarte de que estas solicitudes de Contenido conectado se reintentan cuando son detenidas por el detector de host insalubre, utiliza la opción `:retry`. Para más información sobre la opción `:retry`, consulta [Reintentos de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Si crees que la detección de host no saludable puede estar causando problemas, ponte en contacto con [el soporte de Braze]({{site.baseurl}}/support_contact/).

## Automatización de envíos electrónicos y entradas en el registro de actividad de mensajes

### Configuración de envíos electrónicos automatizados

Si experimentas más de 100.000 errores de webhook o de punto final de contenido conectado (incluidos los reintentos) en un espacio de trabajo en un periodo de 24 horas, recibirás un correo electrónico con la siguiente información sobre cómo resolver los errores. 

- Nombre del espacio de trabajo
- Un enlace al Canvas o a la campaña
- URL del punto final
- Código de error
- Hora en que se observó el error por última vez
- Enlaces al registro de actividad de mensajes y documentación relacionada

{% alert note %}
Puedes configurar el umbral de error por espacio de trabajo. Para ajustar este umbral, ponte en contacto con [el soporte de Braze]({{site.baseurl}}/support_contact/).
{% endalert %}

Los errores del punto final son:

- **`4XX`:** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX`:** `500`, `502`, `503`, `504`, `598`, `599`

Estos correos electrónicos sólo se envían una vez al día a nivel de espacio de trabajo. Si ningún usuario se registra para recibir estos correos electrónicos, se notificará a todos los administradores de la empresa.

Para registrarte para recibir estos correos electrónicos, haz lo siguiente:

1. Vaya a **Configuración** > **Configuración del administrador** > **Preferencias de notificación**.
2. Selecciona **Errores de contenido conectado** y **Errores de webhook** en la **sección Canvas y campañas.** 

### Entradas del registro de actividad de mensajes

Habrá al menos una entrada en [el registro de actividades de mensajería]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) relacionada con el error que desencadenó el envío por correo electrónico automatizado.

### Información adicional sobre fallos en Braze Currents

Para aumentar la transparencia de los problemas relacionados con los webhooks, Braze transmite eventos detallados de fallos de webhooks a Currents y Snowflake Data Sharing. Estos eventos incluyen peticiones de webhook fallidas (como respuestas HTTP `4xx` o `5xx` ), lo que proporciona más capacidad de observación sobre cómo los problemas de webhook pueden afectar a la entrega de mensajes. Ten en cuenta que los eventos de fallo incluyen errores de terminal, así como errores que se están reintentando.

{% alert note %}
Las solicitudes de contenido conectado no se incluyen en estos eventos de fallo de webhook.
{% endalert %}

Para más información, consulta el [glosario de eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).
