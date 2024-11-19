---
nav_title: Calificación de calidad y límites de mensajería
article_title: Calificación de calidad y límites de mensajería 
description: "Este artículo de referencia explica cómo influye Meta en tu índice de calidad y en los límites de mensajería del canal WhatsApp."
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# Clasificación de calidad y límites de mensajería

> Meta influye en tu índice de calidad y en tus [límites de mensajería](https://developers.facebook.com/docs/whatsapp/messaging-limits) desde el momento en que empiezas a utilizar el canal de WhatsApp, y seguirá influyendo en ellos en función del uso que hagas de WhatsApp.

## Definiciones

| Palabra | Definición |
| --- | --- |
| Índice de calidad | Una clasificación basada en los mensajes recientes que sus clientes han recibido en los últimos siete días. Esta calificación viene determinada por los comentarios de sus clientes, como el motivo para bloquear su número de teléfono y otros problemas de notificación. Consulta la documentación de Meta para saber más [sobre tu tasa de calidad](https://www.facebook.com/business/help/896873687365001).|
| Límite de mensajes | El número máximo de conversaciones iniciadas por la empresa que puede iniciar con cada uno de sus números de teléfono en un período continuo de 24 horas. |
{: .reset-td-br-1 .reset-td-br-2 }

## Incorporación  

Cuando se crea una nueva cuenta de WhatsApp Business, Meta utiliza diversos factores para determinar el límite de envío inicial. Puedes encontrar este límite en tu WhatsApp Business Manager, y detalles adicionales en tu página Phone Number Insights. 

Consulta la documentación de Meta para saber más sobre la [comprobación de tus requisitos de límite](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) y [número de teléfono](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).

## Rendimiento

Meta inicia cada número de teléfono de empresa registrado con un rendimiento de 80 mensajes por segundo. Las actualizaciones a 1.000 mensajes por segundo pueden realizarse automáticamente o previa solicitud. Información. 

Consulta la documentación de Meta para saber más sobre tu [rendimiento](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput).

## Ritmo de plantillas

Las plantillas de marketing creadas recientemente y las plantillas de marketing en pausa que se quedan sin pausa están potencialmente sujetas al ritmo. El criterio de selección de ritmo de Meta se basa principalmente en el historial de calidad de su plantilla. Cuando se utiliza una plantilla de marketing creada recientemente o una plantilla de marketing no utilizada recientemente, los mensajes se enviarán normalmente hasta que se alcance un umbral no especificado. Una vez alcanzado este umbral, los mensajes posteriores que utilicen esa plantilla se retendrán para dar tiempo suficiente a la reacción del cliente. 

Consulte la documentación de Meta para obtener más información sobre [el espaciado de plantillas](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing).