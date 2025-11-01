---
nav_title: Centro de preferencias de correo electrónico API
article_title: Centro de preferencias de correo electrónico API
page_order: 1
description: "Este artículo describe el centro de preferencias de correo electrónico de la API y cómo personalizarlo."
channel:
  - email
---

# Centro de preferencias de correo electrónico API

> Configurar un centro de preferencias proporciona una ventanilla única para que tus usuarios editen y administren sus preferencias de notificación para tu [mensajería por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/). Este artículo incluye los pasos para crear un centro de preferencias generado por la API, pero también puedes crear un centro de preferencias utilizando el [editor de arrastrar y soltar]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/).

En el panel de Braze, ve a **Audiencia** > **Centros de preferencias de correo electrónico**.

Aquí es donde puedes gestionar y ver cada grupo de suscripción. Cada grupo de suscripción que crees se añade a esta lista del centro de preferencias. Puedes crear varios centros de preferencias.

{% alert important %}
El centro de preferencias está pensado para ser utilizado dentro del canal de correo electrónico Braze. Los enlaces del centro de preferencias son dinámicos en función de cada usuario y no pueden alojarse externamente.
{% endalert %}

## Crear un centro de preferencias con API

Utilizando los [puntos finales del Centro de preferencias Braze]({{site.baseurl}}/api/endpoints/preference_center), puedes crear un centro de preferencias, un sitio web alojado en Braze, que puede mostrar el estado de suscripción de tu usuario y los estados del grupo de suscripción. Mediante HTML y CSS, tu equipo de desarrolladores puede construir el centro de preferencias utilizando HTML y CSS para que el estilo de la página se ajuste a las directrices de tu marca.

Utilizar Liquid te habilita para recuperar los nombres de tus grupos de suscripción y el estado de cada usuario. De esta forma, Braze almacena y recupera estos datos cuando se carga la página.

### Requisitos previos

| Requisito | Descripción |
|---|---|
| Centro de preferencias habilitado | Tu panel de Braze tiene permisos para utilizar la característica del centro de preferencias. |
| Espacio de trabajo válido con un grupo de suscripción por correo electrónico, SMS o WhatsApp | Un espacio de trabajo con usuarios válidos y un grupo de suscripción por correo electrónico, SMS o WhatsApp. |
| Usuario válido | Un usuario con una dirección de correo electrónico y un ID externo. |
| Clave de API generada con permisos del centro de preferencias | En el panel de Braze, ve a **Configuración** > **Claves de API** para confirmar que tienes acceso a una clave de API con permisos del centro de preferencias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 1: Utiliza el punto final Crear centro de preferencias

Empecemos a crear un centro de preferencias utilizando el [punto final Crear centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/). Para personalizar tu centro de preferencias, puedes incluir HTML que se ajuste a tu marca en el campo `preference_center_page_html` y en el campo `confirmation_page_html`.

El [punto final Generar URL del]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) centro de preferencias te permite obtener la URL del centro de preferencias de un usuario concreto fuera de un correo electrónico enviado a través de Braze.

### Paso 2: Incluir en tu campaña de correo electrónico

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Para colocar un enlace al centro de preferencias en tus correos electrónicos, utiliza la siguiente etiqueta de Liquid en el lugar deseado de tu correo electrónico, de forma similar a como insertarías las URL para cancelar suscripción.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

También puedes utilizar una combinación de HTML que incluya Liquid. Por ejemplo, puedes pegar lo siguiente como URL en el editor HTML o en el editor de arrastrar y soltar. Esto mostrará el diseño básico del centro de preferencias que enumera automáticamente todos los grupos de suscripción por correo electrónico. 

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}">Edit your preferences</a>
```
{%endraw%}

El centro de preferencias tiene una casilla de verificación que permitirá a tus usuarios cancelar suscripción a todos los correos electrónicos. Ten en cuenta que no podrás guardar estas preferencias si las envías como mensaje de prueba.

{% alert important %}
La etiqueta de Liquid anterior sólo funcionará al lanzar una campaña o Canvas. El envío de un correo electrónico de prueba no generará un enlace válido.
{% endalert %}

#### Editar un centro de preferencias

Puedes editar y actualizar tu centro de preferencias utilizando el [punto final Actualizar centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/). 

#### Centros de preferencia identificadores y detalles

Para identificar tus centros de preferencias, utiliza el [punto final Ver detalles del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) para obtener información relacionada, como la fecha y hora de la última actualización, el ID del centro de preferencias, etc.

## Personalización

Braze gestiona las actualizaciones del estado de suscripción desde el centro de preferencias, lo que lo mantiene sincronizado. Sin embargo, también puedes crear y alojar tu propio centro de preferencias utilizando [las API de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/) con las siguientes opciones.

### Opción 1: Enlace con parámetros de consulta de cadena

Utiliza pares campo-valor de cadena de consulta en el cuerpo de la URL para pasar el ID del usuario y la categoría de correo electrónico a la página, de modo que los usuarios sólo tengan que confirmar su elección de cancelar suscripción. Esta opción es buena para quienes almacenan un identificador de usuario en formato hash y aún no tienen un centro de suscripción.

Para esta opción, cada categoría de correo electrónico requerirá su propio enlace específico para cancelar suscripción:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
También es posible hacer un hash del ID externo del usuario en el punto de envío utilizando un filtro Liquid. Esto convertirá el `user_id` en un valor hash MD5, por ejemplo:
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Opción 2: Autenticar con token Web JSON

Utiliza [un token Web JSON](https://auth0.com/learn/json-web-tokens/) para autenticar a los usuarios en una parte de tu servidor Web (por ejemplo, las preferencias de cuenta) que normalmente está detrás de una capa de autenticación como la de iniciar sesión con nombre de usuario y contraseña. 

Este enfoque no requiere pares de valores de cadena de consulta incrustados en la URL, ya que éstos pueden pasarse en la carga útil del token Web JSON, por ejemplo:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```

## Preguntas más frecuentes

### No he creado un centro de preferencias. ¿Por qué veo "PreferenceCenterBrazeDefault" en mi panel?

Se utiliza para mostrar el centro de preferencias cuando se utiliza la versión Liquid {%raw%}`${preference_center_url}`{%endraw%}, lo que significa que los pasos en Canvas o las plantillas que hagan referencia a {%raw%}`${preference_center_url}` o `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} no funcionarán. Esto también se aplica a los mensajes enviados anteriormente que incluían el legado Liquid o "PreferenceCenterBrazeDefault" como parte del mensaje. 

Si vuelves a hacer referencia a {%raw%}`${preference_center_url}`{%endraw%} en un mensaje nuevo, se creará de nuevo un centro de preferencias denominado "PreferenceCenterBrazeDefault".

### ¿Los centros de preferencias admiten varias lenguas?

No. Sin embargo, puedes aprovechar Liquid para escribir el HTML de las páginas personalizadas de adhesión voluntaria y exclusión voluntaria. Si utilizas enlaces dinámicos para administrar las cancelaciones de suscripción, éste es un enlace único. 

Por ejemplo, si estás haciendo un seguimiento de la tasa de cancelación de suscripciones de los usuarios hispanohablantes, tendrías que utilizar campañas separadas o aprovechar los análisis en torno a Currents (como ver cuándo se da de baja un usuario y comprobar el idioma preferido de ese usuario).

Como otro ejemplo, para el seguimiento de las tasas de cancelar suscripción de los usuarios hispanohablantes, podrías añadir una cadena de parámetro de consulta como `?Spanish=true` a la URL de cancelar suscripción si el idioma de los usuarios es el alemán y utilizar un enlace de cancelar suscripción normal si no lo es:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Luego, a través de Currents, podrías identificar qué usuarios hablan español y cuántos clics hubo para ese enlace de cancelar suscripción.

### ¿Son necesarios para el envío tanto los enlaces para cancelar suscripción como los centros de preferencias de correo electrónico?

No. Si ves el mensaje "El cuerpo de tu correo electrónico no incluye un enlace para cancelar suscripción" al redactar una campaña de correo electrónico, esta advertencia es de esperar si tu enlace para cancelar suscripción está en un bloque de contenido.
