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

> Aprovecha los avanzados sistemas de IA de Meta para entregar tus mensajes de marketing a más usuarios que tengan más probabilidades de interactuar con ellos, aumentando significativamente la capacidad de entrega y la interacción con los mensajes.

Los mensajes de WhatsApp con entrega optimizada se envían utilizando la nueva [API Lite de Mensajes de Marketing](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) de Meta, que proporciona un rendimiento superior en comparación con la API tradicional de la Nube. Este nuevo canal de envío te ayuda a llegar mejor a los usuarios que valoran y quieren recibir tus mensajes.

Las ventajas de utilizar la entrega optimizada incluyen:

- **Límites de la mensajería dinámica:** La nueva API ofrece límites de mensajería por usuario más dinámicos, lo que permite que los mensajes de marketing de alto nivel de interacción (los que tienen más probabilidades de ser leídos o de que se haga clic en ellos) lleguen a más usuarios.
- **Capacidad de entrega optimizada:** Puedes esperar tasas de entrega más bajas pero tasas de interacción más altas para los mensajes entregados, ya que la IA avanzada de Meta optimizará para los usuarios que espera que valoren y se comprometan con el mensaje. 
- **Resultados probados:** En la India, los mensajes identificados como más propensos a ser leídos o a hacer clic tuvieron hasta un 9% más de mensajes entregados en comparación con el envío a través de Cloud API.
- **Entrega selectiva:** La IA avanzada de Meta identifica los mensajes de alta interacción y los entrega a más usuarios, permitiéndote entregar el mensaje adecuado a más personas en WhatsApp.

### Disponibilidad regional

La disponibilidad y la capacidad de optimización de la entrega dependen de la región del número de teléfono profesional y del usuario. Para saber más, consulta [Disponibilidad geográfica de las características](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features). 

## Configuración de la entrega optimizada

1. En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** > **WhatsApp**.
2. En la sección **Optimiza tus envíos con la entrega optimizada**, selecciona **Actualizar configuración** para desencadenar el [flujo de trabajo de registro integrado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

\![La sección de integración de mensajes de WhatsApp con una opción para optimizar el envío con entrega optimizada.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\. Una vez habilitada la entrega optimizada, los detalles de tu cuenta en **la administración de cuentas de WhatsApp Business** mostrarán el estado de la entrega optimizada.

\![Sección de gestión de cuentas de WhatsApp Business con un grupo de suscripción listado que tiene un estado de número Activo.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

También puedes habilitar la entrega optimizada directamente en tu administrador de WhatsApp y luego empezar a enviar en Braze.

### Solución de problemas de configuración

- **Error general:** Si algo va mal durante la actualización, aparecerá este banner de error y te aconsejará que [te pongas en contacto con el servicio de asistencia]({{site.baseurl}}/braze_support/).
- **Error no elegible:** Si estás restringido por Meta, aparecerá este banner de error: "Al menos una cuenta de WhatsApp Business está restringida por Meta. Las cuentas deben estar al corriente de pago para actualizar". Esto no puede descartarse hasta que se resuelva el problema.

## Utilizar la entrega optimizada en campañas y Lienzos

La entrega optimizada debe utilizarse para los **mensajes de marketing**. Braze eliminará automáticamente la opción de entrega optimizada para **los mensajes de utilidad, autenticación, servicio y respuesta**, que deberán seguir enviándose a través de la API de la Nube, que es la configuración predeterminada. 

### Selección del método de entrega

1. En el paso Braze WhatsApp composer para una campaña o un mensaje Canvas, ve a la pestaña **Configuración**.
2. En la sección **Método de entrega**, la casilla de verificación **Entrega optimizada (Recomendada** ) estará marcada predeterminadamente si tu cuenta de WhatsApp Business (WABA) está habilitada. Si no quieres utilizar la entrega optimizada para ese mensaje concreto, desmarca la casilla.
- Si seleccionas la entrega optimizada pero no está disponible, el mensaje volverá automáticamente al método de la API en la nube.

\![Creador de mensajes con una pestaña de vista previa que tiene una casilla de verificación para seleccionar la entrega optimizada.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})