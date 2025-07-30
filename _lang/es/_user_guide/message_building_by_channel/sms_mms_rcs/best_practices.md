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

## Recomendaciones de control de la exclusión voluntaria

La ley exige que se atiendan las solicitudes de los destinatarios de no recibir comunicaciones. El incumplimiento de las peticiones de los destinatarios de SMS de darse de baja del canal puede acarrear sanciones, incluidas multas, y dar lugar a demandas judiciales. Braze cuenta con características que habilitan una sólida gestión de la adhesión voluntaria y la exclusión de SMS y MMS, además de mecanismos que ayudan a garantizar que las solicitudes se procesan correctamente.

En virtud de sus acuerdos de suscripción con nosotros, nuestros clientes son los únicos responsables del cumplimiento de la legislación aplicable en el uso de nuestros servicios. En consecuencia, recomendamos encarecidamente a los clientes que presten especial atención a la correcta configuración de sus SMS y que prueben a fondo dicha configuración, tomen medidas para controlar el cumplimiento de la opción de exclusión y actúen con prontitud si detectan casos de incumplimiento de las solicitudes de exclusión.

Cuando configures SMS y MMS en Braze para gestionar las adhesiones voluntarias y las bajas, consulta la siguiente lista de recursos:
* [Grupos de suscripción SMS]({{site.baseurl}}/sms_rcs_subscription_groups/): Grupos de suscripción y métodos y estados de suscripción/desconexión.
* [API REST de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups): Cómo procesar las adhesiones voluntarias y las cancelaciones que reciben de una fuente distinta a la respuesta directa a un mensaje.
* [Tratamiento de palabras clave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/): Explicaciones sobre cómo Braze aborda el procesamiento y la gestión de palabras clave.
* [Doble adhesión voluntaria por SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/): Requiere que los usuarios confirmen explícitamente su intención de inclusión antes de poder recibir mensajes SMS. La doble adhesión voluntaria por SMS es un requisito para algunos países, por lo que Braze recomienda configurarla.
* [Envío de mensajes SMS]({{site.baseurl}}/sending_phone_numbers/): Fundamentos del envío de SMS en Braze, incluida la importancia de los grupos de suscripción, los requisitos para los segmentos de SMS y los cuerpos de los mensajes, etc.

### Consideraciones

Cuando se han configurado SMS y MMS en varias instancias y, debido a una configuración incorrecta, una campaña o las adhesiones a Canvas se envían al espacio de trabajo equivocado.

* Braze dispone de un sistema de vigilancia para detectar estos casos. Si se marca este comportamiento, Braze reasignará las cancelaciones a la instancia correcta y rellenará las cancelaciones que se hayan producido durante ese período.
* Recomendamos encarecidamente a los clientes que prueben las exclusiones voluntarias para cada grupo de suscripción que tengan en Braze. Identificar este problema antes de lanzar un mensaje es mejor que mitigarlo después de haberlo identificado.

Braze gestiona las suscripciones SMS/MMS tanto a nivel de perfil de usuario (`user_id`) como de número de teléfono (`channel_id`). Cuando se opta por incluir o excluir un número de teléfono, la actualización se aplica a todos los perfiles que comparten ese número. En el caso de que un usuario final haya optado por un determinado número de teléfono, pero luego cambie de número de teléfono, el nuevo número de teléfono heredará el estado del grupo de suscripción del usuario. Por consiguiente, si un usuario final se ha dado de baja, pero vuelve a entrar en la aplicación o el sitio web con un nuevo número de teléfono, no recibirá mensajes no deseados.

## Recomendaciones para el bombeo de tráfico

### ¿Qué es el bombeo de tráfico?

El bombeo de tráfico es una forma de fraude que se produce cuando un malhechor utiliza un formulario en línea para desencadenar el envío de un gran volumen de mensajes SMS (por ejemplo, mensajes de suscripción o contraseñas de un solo uso). El malhechor crea un número de teléfono de tarificación adicional para que se envíen estos mensajes y reclama una parte de los ingresos al operador de telefonía móvil con el que se ha creado el número de tarificación adicional, generando así ingresos ilícitos.

### Cómo detectar el bombeo de tráfico

* Los números de tarificación adicional que apoyan este tipo de estafa suelen estar, aunque no siempre, establecidos en países fuera de sus geografías de envío habituales.
* Los picos inusuales en el envío de mensajes desde formularios en línea podrían indicar un bombeo de tráfico.
    * Recomendamos configurar [alertas de campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) para limitar y notificar si se envía un número inverosímilmente alto de mensajes.
* Los formularios en línea incompletos pueden indicar una cumplimentación programática.
* A la hora de crear formularios en línea, recomendamos establecer reglas para garantizar que los formularios estén totalmente completos y utilizar herramientas como CAPTCHA para minimizar el riesgo.

### Impacto del bombeo de tráfico

Los clientes son responsables de controlar el tráfico que envían y se les facturarán todos los SMS enviados a través de su cuenta. Entre Braze y el Cliente, el Cliente es la parte que se encuentra en mejor posición para detectar y evitar el bombeo de tráfico.

