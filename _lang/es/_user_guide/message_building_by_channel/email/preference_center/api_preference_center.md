---
nav_title: Centro de preferencias de correo electrónico de la API
article_title: Centro de preferencias de correo electrónico de la API
page_order: 1
description: "Este artículo describe el centro de preferencias de correo electrónico de la API y cómo personalizarlo."
channel:
  - email
---

# Centro de preferencias de correo electrónico de la API

> La creación de un centro de preferencias permite a los usuarios editar y gestionar sus preferencias de notificación de [mensajes de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/). Este artículo incluye los pasos para crear un centro de preferencias generado por la API, pero también puedes crear un centro de preferencias utilizando el [editor de arrastrar y soltar]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/).

En el panel de Braze, ve a **Audiencia** > **Centros de preferencias de correo electrónico**.

Aquí es donde puedes gestionar y ver cada grupo de suscripción. Cada grupo de suscripción que creas se añade a esta lista del centro de preferencias. Puedes crear varios centros de preferencias.

{% alert important %}
El centro de preferencias está pensado para ser utilizado dentro del canal de correo electrónico de Braze. Los enlaces del centro de preferencias son dinámicos en función de cada usuario y no pueden alojarse externamente.
{% endalert %}

## Crear un centro de preferencias con API

Al utilizar los [puntos finales de Braze del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center), puedes crear un centro de preferencias, un sitio web alojado por Braze, que puede mostrar el estado de suscripción de tus usuarios y los estados de los grupos de suscripción. Mediante HTML y CSS, tu equipo de desarrolladores puede construir el centro de preferencias para que el estilo de la página se ajuste a las directrices de tu marca.

El uso de Liquid te permite recuperar los nombres de tus grupos de suscripción y el estado de cada usuario. De este modo, Braze almacena y recupera estos datos cuando se carga la página.

### Requisitos previos

| Requisito | Descripción |
|---|---|
| Centro de preferencias habilitado | Tu panel de Braze tiene permisos para utilizar la característica del centro de preferencias. |
| Espacio de trabajo válido con un grupo de suscripción por correo electrónico, SMS o WhatsApp | Un espacio de trabajo con usuarios válidos y un grupo de suscripción por correo electrónico, SMS o WhatsApp. |
| Usuario válido | Un usuario con una dirección de correo electrónico y un ID externo. |
| Clave de API generada con permisos del centro de preferencias | En el panel de Braze, ve a **Configuración** > **Claves de API** para confirmar que tienes acceso a una clave de API con permisos del centro de preferencias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 1: Utiliza el punto final Crear centro de preferencias

Empecemos a crear un centro de preferencias utilizando el [punto final Crear centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/). Para personalizar tu centro de preferencias, puedes incluir código HTML acorde con tu marca en los campos `preference_center_page_html` y `confirmation_page_html`.

El [punto final Generar URL del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) te permite obtener la URL del centro de preferencias de un usuario concreto fuera de un correo electrónico enviado a través de Braze.

### Paso 2: Incluir en tu campaña de correo electrónico

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Para colocar un enlace al centro de preferencias en tus correos electrónicos, utiliza la siguiente etiqueta de Liquid en el lugar deseado de tu correo electrónico, de forma similar a como insertarías las URL de cancelación de suscripción.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

También puedes utilizar una combinación de HTML que incluya Liquid. Por ejemplo, puedes pegar lo siguiente como URL en el editor HTML o en el editor de arrastrar y soltar. Esto mostrará el diseño básico del centro de preferencias que enumera automáticamente todos los grupos de suscripción de correo electrónico. Si utilizas [aliasing de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/), añade un signo de interrogación (`?`) después de la etiqueta de Liquid para que Braze pueda agregar los parámetros de seguimiento.

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

El centro de preferencias tiene una casilla de verificación que permitirá a tus usuarios cancelar la suscripción de todos los correos electrónicos. Ten en cuenta que no podrás guardar estas preferencias si las envías como mensaje de prueba.

{% alert important %}
La etiqueta de Liquid anterior solo funcionará al lanzar una campaña o Canvas. El envío de un correo electrónico de prueba no generará un enlace válido. Para verificar el enlace del centro de preferencias, lanza el mensaje en una campaña dirigida únicamente a tu perfil de prueba.
{% endalert %}

#### Editar un centro de preferencias

Puedes editar y actualizar tu centro de preferencias utilizando el [punto final Actualizar centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/). 

#### Identificación de los centros de preferencias y detalles

Para identificar tus centros de preferencias, utiliza el [punto final Ver detalles del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) para obtener información relacionada, como la marca de tiempo de la última actualización, el ID del centro de preferencias, y más.

## Personalización

Braze gestiona las actualizaciones del estado de suscripción desde el centro de preferencias, lo que lo mantiene sincronizado. Sin embargo, también puedes crear y alojar tu propio centro de preferencias utilizando las [API de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/) con las siguientes opciones.

### Opción 1: Enlace con parámetros de consulta de cadena

Utiliza pares campo-valor de cadena de consulta en el cuerpo de la URL para pasar el ID de usuario y la categoría de correo electrónico a la página, de modo que los usuarios solo tengan que confirmar su decisión de cancelar la suscripción. Esta opción es buena para aquellos que almacenan un identificador de usuario en formato hash y no tienen ya un centro de suscripción.

Para esta opción, cada categoría de correo electrónico requerirá su propio enlace de cancelación de suscripción específico:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
También es posible hacer un hash del ID externo del usuario en el punto de envío utilizando un filtro de Liquid. Esto convertirá el `user_id` en un valor hash MD5, por ejemplo:
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Opción 2: Autenticar con token web JSON

Utiliza un [token web JSON](https://auth0.com/learn/json-web-tokens/) para autenticar a los usuarios en una parte de tu servidor web (por ejemplo, las preferencias de cuenta) que normalmente está detrás de una capa de autenticación como el inicio de sesión con nombre de usuario y contraseña. 

Este enfoque no requiere pares de valores de cadena de consulta incrustados en la URL, ya que estos se pueden pasar en la carga útil del token web JSON, por ejemplo:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": "offers"
}
```

## Preguntas frecuentes

### No he creado un centro de preferencias. ¿Por qué veo "PreferenceCenterBrazeDefault" en mi dashboard?

Se utiliza para mostrar el centro de preferencias cuando se usa el Liquid heredado {%raw%}`${preference_center_url}`{%endraw%}, lo que significa que los pasos en Canvas o las plantillas que hagan referencia a {%raw%}`${preference_center_url}` o `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} no funcionarán. Esto también se aplica a los mensajes enviados anteriormente que incluían el Liquid heredado o "PreferenceCenterBrazeDefault" como parte del mensaje. 

Si vuelves a hacer referencia a {%raw%}`${preference_center_url}`{%endraw%} en un mensaje nuevo, se creará de nuevo un centro de preferencias denominado "PreferenceCenterBrazeDefault".

### ¿Los centros de preferencias admiten varios idiomas?

No. Sin embargo, puedes aprovechar Liquid al escribir el código HTML para las páginas personalizadas de adhesión voluntaria y cancelación de suscripción. Si utilizas enlaces dinámicos para administrar las cancelaciones de suscripción, se trata de un único enlace. 

Por ejemplo, si estás realizando un seguimiento de la tasa de cancelación de suscripciones de los usuarios hispanohablantes, tendrás que utilizar campañas independientes o aprovechar los análisis de Currents (por ejemplo, comprobando cuándo un usuario cancela su suscripción y verificando el idioma preferido de ese usuario).

Como otro ejemplo, para realizar el seguimiento de las tasas de cancelación de suscripciones de los usuarios hispanohablantes, podrías añadir una cadena de parámetros de consulta como `?Spanish=true` a la URL de cancelación de suscripción si el idioma del usuario es español y utilizar un enlace de cancelación de suscripción normal si no lo es:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

A continuación, a través de Currents, puedes identificar qué usuarios hablan español y cuántos eventos de clic se han producido en ese enlace para cancelar la suscripción.

### ¿Son necesarios tanto los enlaces para cancelar la suscripción como los centros de preferencias de correo electrónico para el envío?

No. Si ves el mensaje "El cuerpo de tu correo electrónico no incluye un enlace para cancelar suscripción" al redactar una campaña de correo electrónico, esta advertencia es normal si el enlace para cancelar suscripción se encuentra en un bloque de contenido.

### ¿Cómo actualizo el icono predeterminado del navegador?

De forma predeterminada, el icono situado junto al nombre de la pestaña del navegador (favicon) utiliza el logotipo de Braze. Para añadir un favicon personalizado, configúralo mediante el atributo `links-tags` en tu llamada a la API de [Crear o actualizar centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center). A continuación, Braze inserta la etiqueta {% raw %}`<link rel="icon" ...>`{% endraw %} en la página alojada.

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}