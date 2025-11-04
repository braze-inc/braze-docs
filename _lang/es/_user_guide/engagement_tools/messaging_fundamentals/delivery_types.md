---
nav_title: Tipos de entrega y entrada
article_title: Tipos de entrega y entrada
page_order: 5
page_type: reference
description: "Este artículo de referencia describe los tipos de entrega para las campañas, los tipos de entrada para los Canvas y las características basadas en el tiempo al configurar una campaña o un Canvas."
tool:
    - Campaigns
    - Canvas
---

# Programar tu mensaje

> En Braze, hay tres formas diferentes de programar tu mensaje: programado, basado en acciones y desencadenado por API. Elegir cómo y cuándo se entrega tu mensaje es crucial para desarrollar un mensaje eficaz. 

## Tipos de entrega y entrada

Para las campañas, el tipo de entrega determina cuándo entrarán tus usuarios en tu campaña y cuándo se enviará. Puesto que un Canvas se construye como un viaje continuo del usuario, el concepto de mensajería de una programación se denomina tipo de entrada.

| Entrega<nobr> y tipos de entrada | Descripción                                                                                                                                                                                                                                                                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Programado**       | Este tipo de programación está diseñado para mensajes puntuales que deseas enviar inmediatamente, como campañas sobre un acontecimiento actual. <br><br>Cuando envíes mensajes de prueba dirigidos sólo a ti o a tu equipo, esta opción te permite entregarlos inmediatamente.                                                                                   |
| **Basado en la acción**    | Los mensajes de entrega basada en acciones, o las campañas desencadenadas por eventos y las Lonas, son muy eficaces para los mensajes transaccionales o basados en logros. Puedes desencadenarlos para que se envíen después de que un usuario complete un determinado evento, en lugar de enviar tu mensaje en determinados días.                                                                                           |
| **Desencadenado por API**   | Los mensajes desencadenados por API te permiten gestionar la copia de mensajes, las pruebas multivariantes y las reglas de reelegibilidad en el panel de Braze, al tiempo que desencadenan la entrega de ese contenido desde tus propios servidores y sistemas. <br><br>La solicitud de la API para desencadenar el mensaje también puede incluir datos adicionales que se incorporarán al mensaje en tiempo real. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Opciones temporales

{% tabs %}
{% tab campaign %}
Puedes elegir entre las siguientes opciones cuando utilices la entrega programada:

- Enviar en cuanto se lance la campaña
- Enviar a una hora determinada
- [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
{% endtab %}

{% tab canvas %}
Con la entrega programada, los usuarios entrarán en un horario, de forma similar a como programarías una campaña. Puedes inscribir usuarios en un Canvas tan pronto como se lance o en un momento determinado.

#### Horarios designados

Puedes elegir enviar tu Canvas con una frecuencia de entrada específica, incluyendo sólo una vez, diaria, semanal o mensualmente. Para los Canvas con una entrega programada recurrente, puedes configurar la recurrencia para permitir a los usuarios entrar en el Canvas hasta 30 veces designadas.
{% endtab %}
{% endtabs %}

### Opciones basadas en la acción

{% tabs %}
{% tab campaign %}
La entrega basada en acciones enviará campañas a los usuarios que realicen una acción específica. Después de que se produzca esta acción, puedes decidir cuándo enviar la campaña: inmediatamente, después de un tiempo determinado, en un momento concreto o en un momento futuro.
{% endtab %}

{% tab canvas %}
Las opciones basadas en la acción determinan qué acciones (o desencadenantes) debe realizar un usuario para entrar en un Canvas y a qué hora concreta se le permite empezar a entrar. Por ejemplo, podrías evaluar a tus usuarios mediante las siguientes acciones:

- Abrir tu aplicación
- Añadir una dirección de correo electrónico
- Introducir una ubicación

#### Ventana de entrada

La ventana de entrada de tu Canvas determina qué usuarios pueden entrar en el Canvas a la hora de inicio designada (y a la hora de finalización opcional). De forma similar a las campañas basadas en acciones, puedes elegir introducir a los usuarios en su zona horaria local.
{% endtab %}
{% endtabs %}

### Opciones para desencadenar la API

{% tabs %}
{% tab campaign %}
Cuando selecciones la opción de entrega desencadenada por API, recibirás un ID de campaña para identificar qué campaña enviar con el [punto final`/campaigns/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#prerequisites).
{% endtab %}

{% tab canvas %}
Cuando selecciones desencadenada por API como tipo de entrada, recibirás un ID de Canvas para identificar qué campaña enviar con el [punto final`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endtab %}
{% endtabs %}
