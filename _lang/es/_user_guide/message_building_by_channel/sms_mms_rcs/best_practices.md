---
nav_title: "Buenas prácticas"
article_title: "Buenas prácticas para SMS, MMS y RCS" 
page_order: 15
description: "Este artículo de referencia cubre las mejores prácticas para SMS/MMS."
alias: /sms_mms_rcs_best_practices/
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Buenas prácticas para SMS, MMS y RCS 

> Obtén más información sobre las mejores prácticas para SMS, MMS y RCS con Braze, incluidas nuestras recomendaciones para la supervisión de la adhesión voluntaria y el bombeo de tráfico.

## Recomendaciones de seguimiento de la adhesión voluntaria

Cumplir con las solicitudes de los destinatarios de exclusión voluntaria de las comunicaciones es obligatorio por ley. El incumplimiento de las peticiones de los destinatarios de SMS de darse de baja del canal puede acarrear sanciones, incluidas multas, y puede dar lugar a demandas judiciales. Braze cuenta con características que habilitan una sólida gestión de la adhesión voluntaria y la exclusión de SMS y MMS, además de mecanismos que ayudan a garantizar que las solicitudes se procesan correctamente.

En virtud de sus acuerdos de suscripción con nosotros, nuestros clientes son los únicos responsables del cumplimiento de la legislación aplicable en el uso de nuestros servicios. En consecuencia, recomendamos encarecidamente a los clientes que presten mucha atención a la correcta configuración de sus SMS y que prueben a fondo dicha configuración, tomen medidas para controlar el cumplimiento de la adhesión voluntaria y actúen con prontitud si detectan instancias de incumplimiento de las solicitudes de adhesión voluntaria.

Cuando configures SMS y MMS en Braze para gestionar las adhesiones voluntarias y las bajas, consulta la siguiente lista de recursos:
* [Grupos de suscripción SMS]({{site.baseurl}}/sms_rcs_subscription_groups/): Grupos de suscripción y métodos y estados de adhesión voluntaria.
* [API REST de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups): Cómo procesar las adhesiones voluntarias y las bajas que reciben de una fuente distinta a la respuesta directa a un mensaje.
* [Procesamiento de palabras clave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/): Explicaciones sobre cómo Braze aborda el procesamiento de palabras clave y su administración.
* [Doble adhesión voluntaria por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/): Requiere que los usuarios confirmen explícitamente su intención de adhesión voluntaria antes de poder recibir mensajes SMS. La doble adhesión voluntaria por SMS es un requisito para algunos países, por lo que Braze recomienda configurarla.
* [Envío de mensajes SMS]({{site.baseurl}}/sending_phone_numbers/): Fundamentos del envío de SMS en Braze, incluida la importancia de los grupos de suscripción, los requisitos para los segmentos de SMS y los cuerpos de los mensajes, y mucho más.

### Consideraciones

Cuando se han configurado SMS y MMS en varias instancias y, debido a una configuración incorrecta, una campaña o las adhesiones a Canvas se envían al espacio de trabajo equivocado.

* Braze dispone de un sistema de control para identificar dichas instancias. Si se marca este comportamiento, Braze reasignará las adhesiones voluntarias a la instancia correcta y rellenará las adhesiones voluntarias que se hayan producido durante el periodo.
* Recomendamos encarecidamente a los clientes que prueben las exclusiones voluntarias para cada grupo de suscripción que tengan en Braze. Identificar este problema antes de lanzar un mensaje es mejor que mitigarlo después de haberlo identificado.

Braze gestiona las suscripciones SMS/MMS tanto a nivel de perfil de usuario (`user_id`) como de número de teléfono (`channel_id`). Cuando un número de teléfono es objeto de adhesión voluntaria o de exclusión, la actualización se aplica a todos los perfiles que comparten ese número. En el caso de que un usuario final se haya adherido voluntariamente con un número de teléfono determinado, pero luego cambie de número de teléfono, el nuevo número de teléfono heredará el estado del grupo de suscripción del usuario. En consecuencia, si un usuario final ha optado por la exclusión, pero luego vuelve a entrar en la aplicación o sitio web con un nuevo número de teléfono, no recibirá mensajes no deseados.

## Recomendaciones para el bombeo de tráfico

### ¿Qué es el bombeo de tráfico?

El bombeo de tráfico es una forma de fraude que se produce cuando un malhechor utiliza un formulario online para desencadenar el envío de mensajes SMS a gran volumen (por ejemplo, mensajes de adhesión voluntaria o contraseñas de un solo uso). El malhechor configura un número de teléfono de tarificación adicional para que se envíen estos mensajes y reclama una parte de los ingresos al operador de telefonía móvil con el que se ha configurado el número de tarificación adicional, generando así ingresos ilícitos.

### Cómo detectar el bombeo de tráfico

* Los números de tarificación adicional que apoyan este tipo de estafa suelen estar configurados, aunque no siempre, en países fuera de tus zonas geográficas de envío habituales.
* Los picos inusuales en el envío de mensajes desde formularios online podrían indicar un bombeo de tráfico.
    * Recomendamos configurar [alertas de campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) para limitar y notificar si se envía un número inverosímilmente alto de mensajes.
* Los formularios online incompletos pueden indicar que se han rellenado de forma programática.
* Cuando crees formularios online, te recomendamos que establezcas reglas para asegurarte de que los formularios están totalmente completos y que utilices herramientas como CAPTCHA para minimizar el riesgo.

### Impacto del bombeo de tráfico

Los clientes son responsables de controlar el tráfico que envían y se les facturarán todos los SMS enviados a través de su cuenta. Entre Braze y el Cliente, el Cliente es la parte que está en mejor posición para detectar y evitar el bombeo de tráfico.

