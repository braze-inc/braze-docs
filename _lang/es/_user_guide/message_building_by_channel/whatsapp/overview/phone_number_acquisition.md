---
nav_title: Adquisición de número de teléfono
article_title: Adquisición de número de teléfono
page_order: 3
description: "Este artículo de referencia cubre cómo adquirir un número de teléfono de Twilio e Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Adquisición de número de teléfono

> Para utilizar el canal de mensajería de WhatsApp, necesitarás un número de teléfono que cumpla los requisitos de WhatsApp para su [API en la nube](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) o [su API local](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

Debes adquirir tu número de teléfono tú mismo, ya que Braze no te lo proporcionará. Puede adquirir un teléfono físico con una tarjeta SIM a través de su proveedor de telefonía profesional o recurrir a uno de nuestros socios: Twilio o Infoblip. **Debes tener tu propia cuenta de Twilio o Infobip porque esto no se puede hacer a través de Braze.**

## Requisitos de la API de WhatsApp

Tu número de teléfono debe cumplir estos requisitos de la API de WhatsApp:

- Propiedad de tu empresa 
- Tener un código de país y de área (como los números de teléfono fijo y móvil)
- Capaz de recibir llamadas de voz o SMS
- Accesible durante la configuración de la cuenta (para recibir códigos de verificación)
- No es un código corto
- No se ha utilizado anteriormente con la plataforma WhatsApp Business
- No conectado a una cuenta personal de WhatsApp

## Adquirir un número de teléfono Twilio

### Paso 1: Comprar un número de teléfono desde la consola o la API de Twilio

1. Desde la consola de Twilio, vaya a **Desarrollo** > **Números de teléfono** > **Gestionar** > **Comprar un número**. Si no ve esta opción, seleccione **Explorar productos**, desplácese hasta **Superredes** y, a continuación, seleccione **Número de teléfono** > **Comprar un número**. <br><br>![Consola de Twilio con la pestaña "Desarrollar" abierta y la opción "Comprar un número".]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Introduce el código de área o localidad que desees (si lo tienes). Busque un número y seleccione **Comprar**. <br><br> ![Un botón para comprar el número de teléfono de la lista.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Después de comprar su número de teléfono, vaya a **Números activos** y seleccione el número de teléfono que acaba de comprar. <br><br>!["Números activos" que muestra el número de teléfono adquirido.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Paso 2: Configura tu número de teléfono

Siga las instrucciones de Twilio para [configurar su número de teléfono Twilio para recibir el código de verificación por correo electrónico utilizando la transcripción de correo de voz](https://www.twilio.com/docs/whatsapp/self-sign-up#setting-up-your-twilio-phone-number-to-receive-the-verification-code-via-email-using-voicemail-transcription). **No sigas las instrucciones de ningún otro paso, ya que eso conectará tu número de teléfono a Twilio, no a Braze.**

{% alert warning %}
**Sólo tienes que seguir las instrucciones de Twilio para recibir un código de verificación.**

Si sigues los siguientes pasos de las instrucciones de Twilio, conectarás tu número de teléfono a Twilio. Eso significa que no puedes conectar ese número a Braze a menos que hagas una migración o compres un número diferente.
{% endalert %}

### Paso 3: Complete el flujo de trabajo de registro integrado

1. Una vez configurado Twilio, vaya a su panel Braze > **Socios tecnológicos** > **WhatsApp** y seleccione **Iniciar integración** o **Añadir cuenta de WhatsApp Business**, lo que aparezca, para activar el [flujo de trabajo de registro integrado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br>En el paso **Añadir un número de teléfono para WhatsApp**, seleccione **Llamada telefónica** para verificar su número de teléfono. <br><br>![Sección con las opciones para verificar tu número de teléfono a través de un mensaje de texto o una llamada telefónica.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Espere unos minutos a que el código de verificación se envíe a su buzón de correo electrónico y, a continuación, introduzca el código de verificación y complete la configuración.

## Adquirir un número de teléfono Infobip 

1. En la consola Infobip, vaya a **Canales y Números** y seleccione **Números**.<br><br>![Sección "Canales y Números" de Infoblip con "Números" listados debajo.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Seleccione **Comprar número** > el país al que desea enviar mensajes > **SMS**.<br><br>![Botón para comprar un número.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Dependiendo del país seleccionado, es posible que tenga que completar un proceso de registro adicional (como seleccionar un 10 DLC o una opción gratuita para los números de teléfono de EE.UU.). Asegúrese de seleccionar la opción disponible.<br><br>![Una página que te pide que selecciones el tipo de número: 10 DLC o gratuito.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Seleccione la oferta disponible, siga el resto de los pasos y espere a que se procese su solicitud. Puede comprobar el estado accediendo a **Números** > **Mi solicitud**. <br><br>![Una oferta con información que incluye tarifas y cobertura.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Dependiendo del país que haya elegido, espere a que el equipo de Infobip se ponga en contacto con usted para facilitarle los datos de registro (como en el caso de 10DLC en EE.UU.).<br><br>

6. Cuando su número de teléfono esté listo en Infobip, vaya a su panel Braze > **Socios tecnológicos** > **WhatsApp** y seleccione **Iniciar integración** o **Añadir cuenta de WhatsApp Business**, lo que aparezca, para activar el [flujo de trabajo de registro integrado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br> En el paso **Añadir un número de teléfono para WhatsApp**, selecciona **Mensaje de texto** para saber cómo quieres verificar tu número de teléfono.<br><br>![Sección con las opciones para verificar tu número de teléfono a través de un mensaje de texto o una llamada telefónica.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Compruebe [los registros de análisis](https://www.infobip.com/docs/analyze/analyze-logs) de Infobip en su portal de clientes para ver el código de verificación, que puede tardar unos minutos en aparecer, a continuación, introduzca el código de verificación y complete la configuración.




