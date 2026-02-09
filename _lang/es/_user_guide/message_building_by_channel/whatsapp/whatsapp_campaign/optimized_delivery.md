---
nav_title: Mensajes de WhatsApp con entrega optimizada
article_title: Mensajes de WhatsApp con entrega optimizada
page_order: 1
description: "Este artículo de referencia cubre los pasos necesarios para elaborar y crear un mensaje de WhatsApp con entrega optimizada."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Mensajes de WhatsApp con entrega optimizada

> Aumenta la capacidad de entrega y la interacción llegando a más usuarios en WhatsApp con una entrega dinámica basada en la interacción.

Los mensajes de WhatsApp con entrega optimizada se envían utilizando [la API de mensajes de marketing](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) de Meta [para WhatsApp](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) (MM API para WhatsApp), que ofrece una entrega dinámica y basada en la interacción. Esto significa que tus mensajes de alto nivel de interacción (por ejemplo, los que tienen más probabilidades de ser leídos y de que se haga clic en ellos) pueden llegar a más usuarios que probablemente interactúen con ellos. WhatsApp considera que tus mensajes tienen una alta interacción si son esperados, relevantes y oportunos y, por tanto, tienen más probabilidades de ser leídos y de que se haga clic en ellos. 

Las marcas pueden esperar una capacidad de entrega igual o mayor con la API de MM para WhatsApp, en comparación con la API en la nube. En la India, se entregaron hasta un 9% más de mensajes de mensajería de alta interacción en comparación con la API en la nube, según Meta. Ten en cuenta que la API de MM para WhatsApp sigue sin garantizar una capacidad de entrega del 100%.

### Disponibilidad regional

La disponibilidad y la capacidad de optimización de la entrega dependen de la región del número de teléfono profesional y del usuario. Para saber más, consulta [Disponibilidad geográfica de las características](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features). 

## Configuración de la entrega optimizada

1. En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** > **WhatsApp**.
2. En la sección **Optimiza tus envíos con la entrega optimizada**, selecciona **Actualizar configuración** para desencadenar el [flujo de trabajo de registro integrado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

![La sección Integración de mensajes de WhatsApp con una opción para optimizar el envío con entrega optimizada.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\. Una vez habilitada la entrega optimizada, los detalles de tu cuenta en **la administración de cuentas de WhatsApp Business** mostrarán el estado de la entrega optimizada.

![Sección de gestión de cuentas de WhatsApp Business con un grupo de suscripción listado que tiene un estado de número Activo.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

También puedes habilitar la entrega optimizada directamente en tu administrador de WhatsApp y luego empezar a enviar en Braze.

### Solución de problemas de tu configuración

- **Error general:** Si algo va mal durante la actualización, aparecerá este banner de error y te aconsejará que [te pongas en contacto con el servicio de asistencia]({{site.baseurl}}/braze_support/).
- **Error no elegible:** Si estás restringido por Meta, aparecerá este banner de error: "Al menos una cuenta de WhatsApp Business está restringida por Meta. Las cuentas deben estar al corriente de pago para actualizar". Esto no puede descartarse hasta que se resuelva el problema.

## Utilizar la entrega optimizada en campañas y Lienzos

La entrega optimizada debe utilizarse para los **mensajes de marketing**. Braze eliminará automáticamente la opción de entrega optimizada para **los mensajes de utilidad, autenticación, servicio y respuesta**, que deberán seguir enviándose a través de la API de la Nube, que es la configuración predeterminada. 

### Selección del método de entrega

1. En el paso Braze WhatsApp composer para una campaña o un mensaje Canvas, ve a la pestaña **Configuración**.
2. En la sección **Método de entrega**, la casilla de verificación **Entrega optimizada (Recomendada** ) estará marcada predeterminadamente si tu cuenta de WhatsApp Business (WABA) está habilitada. Si no quieres utilizar la entrega optimizada para ese mensaje concreto, desmarca la casilla.
- Si seleccionas la entrega optimizada pero no está disponible, el mensaje volverá automáticamente al método de la API en la nube.

![Creador de mensajes con una pestaña de vista previa que tiene una casilla de verificación para seleccionar la entrega optimizada.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### Reorientar a los usuarios en otros canales Braze 

Como la API de MM para WhatsApp no ofrece una capacidad de entrega del 100%, es importante saber cómo reorientar a los usuarios que no hayan recibido tu mensaje en otros canales. 

Para reorientar a los usuarios, recomendamos crear un segmento de usuarios que no recibieron un mensaje específico. Para ello, filtra por el código de error `131049`, que indica que no se ha enviado un mensaje de plantilla de marketing debido a la aplicación del límite de plantillas de marketing por usuario de WhatsApp. Puedes hacerlo utilizando Braze Currents o Extensiones de segmento SQL:

- **Braze Currents:** Exporta eventos de fallo de mensajes mediante Braze Currents. A continuación, puedes utilizar estos datos para actualizar un atributo personalizado en el perfil de usuario (como `whatsapp_failed_last_msg: true`), que puedes utilizar como filtro para tu campaña de reorientación.
- **Extensiones de segmento SQL:** Si tienes acceso a esta característica, puedes utilizar SQL para consultar los registros de fallos de mensajes y crear un segmento de esos usuarios, y luego dirigir ese segmento a un canal diferente.
