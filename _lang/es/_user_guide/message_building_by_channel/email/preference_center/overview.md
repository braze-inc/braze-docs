---
nav_title: Resumen
article_title: Resumen del centro de preferencias
page_order: 1
description: "Este artículo describe el centro de preferencias de correo electrónico y cómo personalizarlo."
channel:
  - email
---

# Resumen del centro de preferencias

> La creación de un centro de preferencias permite a los usuarios editar y gestionar sus preferencias de notificación de [mensajes de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/). Este artículo incluye los pasos para crear un centro de preferencias generado por la API, pero también puedes crear un centro de preferencias utilizando el [editor de arrastrar y soltar]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/).

En el panel de control de Braze, vaya a **Audiencia** > **Suscripciones** > **Centro de preferencias de correo electrónico**.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), esta página se encuentra en **Usuarios** > **Grupos de suscripción** > **Centro de preferencias de correo electrónico**.
{% endalert %}

Aquí es donde puede gestionar y ver cada grupo de suscripción. Cada grupo de suscripción que se crea se añade a esta lista del centro de preferencias. Puede crear varios centros de preferencias.

{% alert important %}
El centro de preferencias está pensado para ser utilizado dentro del canal de correo electrónico Braze. Los enlaces del centro de preferencias son dinámicos en función de cada usuario y no pueden alojarse externamente.
{% endalert %}

## Crear un centro de preferencias con API

Al utilizar [los puntos finales Braze del Centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center), puede crear un centro de preferencias, un sitio web alojado por Braze, que puede mostrar el estado de suscripción de sus usuarios y los estados de los grupos de suscripción. Mediante HTML y CSS, tu equipo de desarrolladores puede construir el centro de preferencias utilizando HTML y CSS para que el estilo de la página se ajuste a las directrices de tu marca.

El uso de Liquid le permite recuperar los nombres de sus grupos de suscripción y el estado de cada usuario. De este modo, Braze almacena y recupera estos datos cuando se carga la página.

### Requisitos previos

| Requisito | Descripción |
|---|---|
| Centro de preferencias activado | Tu panel de control Braze tiene permisos para utilizar la función del centro de preferencias. |
| Espacio de trabajo válido con un grupo de suscripción por correo electrónico, SMS o WhatsApp | Un espacio de trabajo con usuarios válidos y un grupo de suscripción por correo electrónico, SMS o WhatsApp. |
| Usuario válido | Un usuario con una dirección de correo electrónico y un identificador externo. |
| Clave API generada con permisos del centro de preferencias | En el panel de control de Braze, vaya a **Configuración** > **Claves de** API para confirmar que tiene acceso a una clave de API con permisos del centro de preferencias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), puede crear una clave de API desde **Consola de desarrollador** > **Configuración de API**.
{% endalert %}

### Paso 1: Utiliza el punto final Crear centro de preferencias

Empecemos a crear un centro de preferencias utilizando el [punto final Crear centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/). Para personalizar su centro de preferencias, puede incluir código HTML acorde con su marca en los campos `preference_center_page_html` y `confirmation_page_html`.

El [punto final Generar URL del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) te permite obtener la URL del centro de preferencias de un usuario concreto fuera de un correo electrónico enviado a través de Braze.

### Paso 2: Incluir en tu campaña de correo electrónico

{% multi_lang_include preference_center_warning.md %}

Para colocar un enlace al centro de preferencias en sus correos electrónicos, utilice la siguiente etiqueta Liquid en el lugar deseado de su correo electrónico, de forma similar a como insertaría las URL de cancelación de suscripción.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

También puede utilizar una combinación de HTML que incluya Liquid. Por ejemplo, puede pegar lo siguiente como URL en el editor HTML o en el editor de arrastrar y soltar. Esto mostrará el diseño básico del centro de preferencias que enumera automáticamente todos los grupos de suscripción de correo electrónico. 

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}">Edit your preferences</a>
```
{%endraw%}

El centro de preferencias tiene una casilla de verificación que permitirá a sus usuarios darse de baja de todos los correos electrónicos. Tenga en cuenta que no podrá guardar estas preferencias si las envía como mensaje de prueba.

{% alert important %}
La etiqueta Liquid anterior sólo funcionará al lanzar una campaña o Canvas. El envío de un correo electrónico de prueba no generará un enlace válido.
{% endalert %}

#### Editar un centro de preferencias

Puedes editar y actualizar tu centro de preferencias utilizando el [punto final Actualizar centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/). 

#### Identificación de los centros de preferencia y detalles

Para identificar sus centros de preferencias, utilice el [punto final Ver detalles del centro de preferencias]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) para obtener información relacionada, como la fecha y hora de la última actualización, el ID del centro de preferencias, etc.

## Personalización

Braze gestiona las actualizaciones del estado de suscripción desde el centro de preferencias, lo que lo mantiene sincronizado. Sin embargo, también puede crear y alojar su propio centro de preferencias utilizando [las API de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/) con las siguientes opciones.

### Opción 1: Enlace con parámetros de consulta de cadena

Utilice pares campo-valor de cadena de consulta en el cuerpo de la URL para pasar el ID de usuario y la categoría de correo electrónico a la página, de modo que los usuarios sólo tengan que confirmar su decisión de darse de baja. Esta opción es buena para aquellos que almacenan un identificador de usuario en formato hash y no tienen ya un centro de suscripción.

Para esta opción, cada categoría de correo electrónico requerirá su propio enlace de cancelación de suscripción específico:<br>
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

Utilice un [token web JSON](https://auth0.com/learn/json-web-tokens/) para autenticar a los usuarios en una parte de su servidor web (por ejemplo, las preferencias de cuenta) que normalmente está detrás de una capa de autenticación como el inicio de sesión con nombre de usuario y contraseña. 

Este enfoque no requiere pares de valores de cadena de consulta incrustados en la URL, ya que estos se pueden pasar en la carga útil del token web JSON, por ejemplo:

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