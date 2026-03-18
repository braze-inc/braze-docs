---
nav_title: Tipos de entrega y entrada
article_title: Tipos de entrega y entrada
page_order: 5
page_type: reference
description: "Este artículo de referencia describe los tipos de entrega para campañas, los tipos de entrada para Canvas y las características basadas en el tiempo al configurar una campaña o un Canvas."
tool:
    - Campaigns
    - Canvas
---

# Tipos de entrega y entrada

> En Braze, hay tres formas diferentes de programar tus mensajes: programados, basados en acciones y activados por API. Elegir cómo y cuándo se entrega tu mensaje es fundamental para desarrollar un mensaje eficaz. 

En el caso de las campañas, el tipo de entrega determina cuándo los usuarios entrarán en tu campaña y cuándo se enviará. Dado que Canvas se ha diseñado como un recorrido continuo para el usuario, el concepto de mensajería de una programación se denomina tipo de entrada.

| Tipos de entrega<nobr> y entrada | Descripción                                                                                                                                                                                                                                                                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Planificada**       | Este tipo de programación está diseñado para mensajes puntuales que deseas enviar de inmediato, como campañas sobre un evento actual. <br><br>Al enviar mensajes de prueba dirigidos solo a ti o a tu equipo, esta opción te permite entregarlos de inmediato.                                                                                   |
| **Basado en acciones**    | La entrega basada en acciones, o las campañas y lienzos desencadenados por eventos, son muy eficaces para los mensajes transaccionales o basados en logros. Puedes desencadenarlos para que se envíen después de que un usuario complete un evento determinado, en lugar de enviar tu mensaje en días concretos.                                                                                           |
| **Desencadenado por API**   | Los mensajes desencadenados por API te permiten administrar el texto de los mensajes, las pruebas multivariante y las reglas de reelegibilidad en el panel de Braze, al tiempo que desencadenas la entrega de ese contenido desde tus propios servidores y sistemas. <br><br>La solicitud de la API para desencadenar el mensaje también puede incluir datos adicionales que se incorporarán al mensaje en tiempo real. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Opciones basadas en el tiempo

{% tabs %}
{% tab campaign %}
Puedes elegir entre las siguientes opciones cuando utilices la entrega programada:

- Enviar en cuanto se lance la campaña
- Enviar a una hora determinada
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
{% endtab %}

{% tab canvas %}
Con la entrega programada, los usuarios entrarán en un horario, de forma similar a como se programaría una campaña. Puedes inscribir a los usuarios en un Canvas tan pronto como se lance o en el momento que se desee.

### Horarios designados

Puedes elegir enviar tu Canvas con una frecuencia específica, incluyendo una sola vez, diariamente, semanalmente o mensualmente. En el caso de los Canvas con una entrega programada recurrente, puedes configurar la recurrencia para permitir a los usuarios acceder al Canvas hasta 30 veces designadas.
{% endtab %}
{% endtabs %}

## Opciones basadas en acciones

{% tabs %}
{% tab campaign %}
La entrega basada en acciones enviará campañas a los usuarios que realicen una acción específica. Una vez realizada esta acción, puedes decidir cuándo enviar la campaña: inmediatamente, después de un tiempo determinado, en un momento específico o en un momento futuro.
{% endtab %}

{% tab canvas %}
Las opciones basadas en acciones determinan qué acciones (o desencadenantes) debe realizar un usuario para entrar en un Canvas y en qué momento específico se le permite empezar a entrar. Por ejemplo, podrías evaluar a tus usuarios mediante las siguientes acciones:

- Abrir tu aplicación
- Añadir una dirección de correo electrónico
- Introducir una ubicación

### Ventana de entrada

La ventana de entrada de tu Canvas determina qué usuarios pueden entrar en el Canvas a la hora de inicio designada (y a la hora de finalización opcional). Al igual que en las campañas basadas en acciones, puedes optar por introducir a los usuarios en su zona horaria local.
{% endtab %}
{% endtabs %}

## Opciones para desencadenar API

{% tabs %}
{% tab campaign %}
Cuando selecciones «API-triggered» como opción de entrega, recibirás un identificador de campaña para identificar qué campaña enviar con el[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#prerequisites)[punto final]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#prerequisites).
{% endtab %}

{% tab canvas %}
Cuando selecciones «API-triggered» (Activado por API) como tipo de entrada, recibirás un ID de Canvas para obtener el identificador de la campaña a enviar con el[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)[punto final]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endtab %}
{% endtabs %}
