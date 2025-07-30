---
nav_title: Resumen
article_title: Descripción general de la transformación de datos Braze
page_order: 0
page_type: reference
alias: /data_transformation/
description: "Este artículo de referencia proporciona un resumen de la Transformación de datos de Braze, las preguntas más frecuentes y las limitaciones del producto."
---

# Visión general de la transformación de datos Braze

> Braze Data Transformation le permite crear y gestionar integraciones webhook para automatizar el flujo de datos desde plataformas externas a Braze. Estos datos de usuario recién integrados pueden impulsar casos de uso de marketing aún más sofisticados. La Transformación de Datos Braze puede agilizar tu integración de datos, aunque tengas muy poca experiencia en codificación, y puede ayudar a sustituir la dependencia de tu equipo de llamadas manuales a API, herramientas de integración de terceros o incluso plataformas de datos de los clientes.

## Cómo funciona

Muchas plataformas actuales disponen de "webhooks", o notificaciones API en tiempo real, para enviar información sobre un nuevo evento o nuevos datos de una plataforma a otra. La Transformación de datos proporciona:

* Una dirección URL Braze para recibir dichos webhooks.
* Capacidades para transformar la carga útil del webhook con código JavaScript para crear solicitudes válidas a varios puntos finales de la API Braze, incluidos Braze `/users/track` o `/catalogs`. Por ejemplo, para el destino `/users/track`, puede elegir qué información utilizar del webhook y cómo desea que se representen los datos en los perfiles de usuario Braze como atributos de usuario, eventos o compras.
* Registro para realizar el control de calidad, solucionar problemas y supervisar el rendimiento de sus transformaciones.

El resultado final es una integración webhook que conecta una plataforma fuente de su elección convirtiendo sus webhooks en actualizaciones Braze.

{% details Más sobre webhooks %}
Los webhooks son notificaciones en tiempo real enviadas a través de una solicitud HTTP POST a un destino específico. Los webhooks se utilizan a menudo para enviar datos de un punto a otro, en el que el webhook puede pasar datos sobre una acción que se ha producido y quién estaba involucrado en esa acción.

Por ejemplo, una plataforma de encuestas puede enviar un webhook a un destino de su elección cada vez que se reciba una respuesta a un formulario en línea. O bien, una plataforma de atención al cliente puede enviar un webhook a un destino de su elección cada vez que se cree un ticket de atención al cliente.
{% enddetails %}

## Niveles de transformación de datos

La siguiente tabla describe las diferencias entre la versión gratuita y la versión pro de Transformación de Datos.

| Área | Versión gratuita | Transformación de datos Pro |
|----|----|----|
| Transformaciones activas | Hasta 5 por empresa | Hasta 55 por empresa |
| Al mes | 300 000 solicitudes entrantes al mes | 10.300.000 solicitudes entrantes al mes |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Para solicitar una actualización a Data Transformation Pro, póngase en contacto con su gestor de cuenta Braze o seleccione el botón **Solicitar actualización** en el panel Braze.
{% endalert %}

### Límites de tarifa

El límite de velocidad para las Transformaciones de Datos Braze es de 1.000 solicitudes entrantes por minuto y espacio de trabajo. Si tienes Transformación de datos Pro y necesitas un límite de velocidad superior, ponte en contacto con tu director de cuentas Braze.

## Preguntas más frecuentes

### ¿Qué se sincroniza con Braze Data Transformation?

Cualquier dato que la plataforma externa ponga a disposición en un webhook puede sincronizarse con Braze. Cuanto más envíe una plataforma externa a través de webhooks, más opciones habrá para elegir lo que se sincroniza.

### Soy especialista en marketing. ¿Necesito recursos de desarrollador para utilizar Braze Data Transformation?

Aunque nos encantaría que los desarrolladores también utilizaran esta función, no es necesario ser uno de ellos para utilizarla. Los responsables de marketing también pueden establecer transformaciones con éxito sin recursos de desarrollador.

### ¿Puedo seguir utilizando Braze Data Transformation si mi plataforma externa sólo proporciona una dirección de correo electrónico o un número de teléfono como identificador?

Sí. Puede hacer que sus transformaciones actualicen el punto final `/users/track` con la [dirección de correo electrónico o el número de teléfono como identificador]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address).

Esto funciona utilizando `email` o `phone` como su propiedad identificadora en el código de transformación en lugar de `external_id` o `braze_id`. El [código de transformación de]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/use_cases/#example-transformation-code) ejemplo utiliza esta funcionalidad.

{% alert note %}
Los usuarios de acceso temprano de Braze Data Transformation que empezaron antes de abril de 2023 pueden estar familiarizados con una función de `get_user_by_email` que ayudó con este caso de uso. Esta función ha quedado obsoleta.
{% endalert %}

### ¿Consume Braze Data Transformation puntos de datos?

En la mayoría de los casos, sí. La Transformación de datos de Braze crea, finalmente, una llamada a `/users/track` que escribe los atributos, eventos y compras que desees. Éstos consumirán puntos de datos del mismo modo que si la llamada a `/users/track` se realizara de forma independiente. Tienes control sobre cuántos puntos de datos se escribirán en función de cómo escribas tu transformación.

### ¿Cómo puedo obtener ayuda para configurar mi caso de uso o con mi código de transformación?

Póngase en contacto con su gestor de cuentas Braze para obtener más ayuda.


