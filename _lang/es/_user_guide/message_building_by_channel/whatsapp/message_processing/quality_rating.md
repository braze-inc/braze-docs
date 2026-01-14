---
nav_title: Tasa de calidad y límites de mensajería
article_title: Tasa de calidad y límites de mensajería 
description: "Este artículo de referencia explica cómo influye Meta en tu tasa de calidad y en los límites de mensajería del canal de WhatsApp."
page_type: partner
search_tag: Partner
page_order: 
channel:
  - WhatsApp
---

# Tasa de calidad y límites de mensajería

> Meta influye en tu tasa de calidad y en [los límites de mensajería](https://developers.facebook.com/docs/whatsapp/messaging-limits) desde el momento en que empiezas a utilizar el canal de WhatsApp, y seguirá influyendo en ellos en respuesta a tu uso de WhatsApp.

## Definiciones

| Palabra | Definición |
| --- | --- |
| Tasa de calidad | Una tasa basada en los mensajes recientes que tus clientes han recibido en los últimos siete días. Esta tasa viene determinada por las opiniones de tus clientes, como el motivo para bloquear tu número de teléfono y otros problemas de notificación. Consulta la documentación de Meta para saber más [sobre tu tasa de calidad](https://www.facebook.com/business/help/896873687365001).|
| Límite de mensajería | El número máximo de conversaciones iniciadas por la empresa que puedes iniciar con cada uno de tus números de teléfono en un periodo móvil de 24 horas. |
{: .reset-td-br-1 .reset-td-br-2 }

## Incorporación  

Cuando se crea una nueva cuenta de WhatsApp Business, Meta utiliza varios factores para determinar el límite de envío inicial. Puedes encontrar este límite en tu administrador de WhatsApp Business, así como información adicional en tu página de información sobre números de teléfono. 

Consulta la documentación de Meta para saber más sobre la [comprobación de tus](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) [requisitos de](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) [límite](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) y [número de teléfono](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).

## Rendimiento

Meta inicia cada número de teléfono de empresa registrado con un rendimiento de 80 mensajes por segundo. Las actualizaciones a 1.000 mensajes por segundo pueden realizarse automáticamente o previa solicitud. Información. 

Consulta la documentación de Meta para saber más sobre tu [rendimiento](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput).

## Plantilla de ritmo

Las plantillas de marketing creadas recientemente y las plantillas de marketing en pausa que se quedan sin pausa están potencialmente sujetas al ritmo. Los criterios de selección del ritmo de Meta se basan principalmente en el historial de calidad de tu plantilla. Cuando utilices una plantilla de marketing creada recientemente o una plantilla de marketing no utilizada recientemente, los mensajes se enviarán normalmente hasta que se alcance un umbral no especificado. Una vez alcanzado este umbral, los mensajes posteriores que utilicen esa plantilla se retendrán para dar tiempo suficiente a la respuesta del cliente. 

Consulta la documentación de Meta para saber más sobre [el ritmo de plantillas](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing).