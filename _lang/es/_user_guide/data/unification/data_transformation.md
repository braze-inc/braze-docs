---
nav_title: Transformación de datos
article_title: Transformación de datos
page_order: 0.3
layout: dev_guide
guide_top_header: "Transformación de datos"
guide_top_text: "La Transformación de Datos Braze te permite construir y administrar integraciones webhook para automatizar el flujo de datos desde plataformas externas a Braze. Estos datos de usuario recién integrados pueden alimentar casos de uso de marketing aún más sofisticados. La Transformación de Datos Braze puede agilizar tu integración de datos, aunque tengas muy poca experiencia en codificación, y puede ayudar a sustituir la dependencia de tu equipo de llamadas manuales a API, herramientas de integración de terceros o incluso plataformas de datos de los clientes."
page_type: landing
description: "Esta página de inicio contiene artículos sobre la Transformación de Datos Braze, incluyendo cómo crear una transformación de datos y casos de uso."
alias: /data_transformation/

guide_featured_title: "Artículos de sección"
guide_featured_list:
  - name: Crear una transformación
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation/
    image: /assets/img/braze_icons/flip-forward.svg
  - name: Casos de uso
    link: /docs/user_guide/data/unification/data_transformation/use_cases/
    image: /assets/img/braze_icons/users-01.svg
---

## Cómo funciona

Muchas plataformas actuales tienen "webhooks", o notificaciones API en tiempo real, para enviar información sobre un nuevo evento o nuevos datos de una plataforma a otra. La Transformación de Datos proporciona:

* Una dirección URL Braze para recibir dichos webhooks.
* Capacidades para transformar la carga útil del webhook con código JavaScript para crear solicitudes válidas a varios puntos finales de la API Braze, incluidos Braze `/users/track` o `/catalogs`. Por ejemplo, para el destino `/users/track`, puedes elegir qué información utilizar del webhook y cómo quieres que se representen los datos en los perfiles de usuario de Braze como atributos de usuario, eventos o compras.
* Registro para realizar el control de calidad, solucionar problemas y supervisar el rendimiento de tus transformaciones.

El resultado final es una integración webhook que conecta una plataforma fuente de tu elección convirtiendo sus webhooks en actualizaciones Braze.

{% details More on webhooks %}
Los webhooks son notificaciones en tiempo real que se envían mediante una solicitud HTTP POST a un destino específico. Los webhooks se utilizan a menudo para enviar datos de un punto a otro, en los que el webhook puede pasar datos sobre una acción que se ha producido y quién ha participado en esa acción.

Por ejemplo, una plataforma de cuestionarios puede enviar un webhook a un destino de tu elección cada vez que se reciba una respuesta a un formulario online. O bien, una plataforma de servicio al cliente puede enviar un webhook a un destino de su elección cada vez que se cree un ticket de servicio al cliente.
{% enddetails %}

## Niveles de transformación de datos

La siguiente tabla describe las diferencias entre la versión gratuita y la versión profesional de Transformación de Datos.

| Área | Versión gratuita | Transformación de Datos Pro |
|----|----|----|
| Transformaciones activas | Hasta 5 por empresa | Hasta 55 por empresa |
| Al mes | 300.000 solicitudes entrantes al mes | 10.300.000 solicitudes entrantes al mes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Para solicitar una actualización a Transformación de datos Pro, ponte en contacto con tu director de cuentas Braze o selecciona el botón **Solicitar actualización** en el panel Braze.
{% endalert %}

### Límites de velocidad

El límite de velocidad para las Transformaciones de Datos Braze es de 1.000 solicitudes entrantes por minuto y espacio de trabajo. Si tienes Transformación de datos Pro y necesitas un límite de velocidad superior, ponte en contacto con tu administrador de cuentas Braze.

## Preguntas más frecuentes

### ¿Qué se sincroniza con la Transformación de Datos Braze?

Cualquier dato que la plataforma externa ponga a disposición en un webhook puede sincronizarse con Braze. Cuanto más envíe una plataforma externa a través de webhooks, más opciones tendrás para elegir lo que se sincroniza.

### Soy especialista en marketing. ¿Necesito recursos de desarrollador para utilizar la Transformación de Datos Braze?

Aunque nos encantaría que los desarrolladores también utilizaran esta característica, ¡no necesitas ser uno para usarla! Los especialistas en marketing también pueden configurar transformaciones con éxito sin recursos de desarrollador.

### ¿Puedo seguir utilizando la Transformación de Datos Braze si mi plataforma externa sólo proporciona una dirección de correo electrónico o un número de teléfono como identificador?

Sí. Puedes hacer que tus transformaciones actualicen el punto final `/users/track` con la [dirección de correo electrónico o el número de teléfono como identificador]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address).

Esto funciona utilizando `email` o `phone` como tu propiedad identificadora en el código de transformación en lugar de `external_id` o `braze_id`. El [código de transformación]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/use_cases/#example-transformation-code) de ejemplo utiliza esta función.

{% alert note %}
Los usuarios de acceso temprano de la Transformación de Datos Braze que empezaron antes de abril de 2023 pueden estar familiarizados con una función de `get_user_by_email` que ayudó en este caso de uso. Esa función ha quedado obsoleta.
{% endalert %}

### ¿La Transformación de Datos Braze registra puntos de datos?

Sí, en la mayoría de los casos. La Transformación de Datos Braze crea finalmente una llamada a `/users/track` que escribe los atributos, eventos y compras que desees. Estos registrarán los puntos de datos de la misma forma que si la llamada a `/users/track` se realizara de forma independiente. Tienes control sobre cuántos puntos de datos se registran en función de cómo escribas tu transformación.

### ¿Cómo puedo obtener ayuda para configurar mi caso de uso o con mi código de transformación?

Ponte en contacto con tu director de cuentas Braze para obtener más ayuda.
