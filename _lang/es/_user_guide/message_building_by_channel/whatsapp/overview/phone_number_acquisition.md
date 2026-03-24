---
nav_title: Adquisición de número de teléfono
article_title: Adquisición de número de teléfono
page_order: 4
description: "Este artículo de referencia cubre cómo adquirir un número de teléfono de Twilio e Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Adquisición de número de teléfono

> Para utilizar el canal de mensajería de WhatsApp, necesitarás un número de teléfono que cumpla los requisitos de WhatsApp para su [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) o [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

Debes adquirir tu número de teléfono tú mismo, ya que Braze no te lo proporcionará. Puedes adquirir un teléfono físico con una tarjeta SIM a través de tu proveedor de telefonía profesional o recurrir a uno de nuestros socios: Twilio o Infobip. **Debes tener tu propia cuenta de Twilio o Infobip porque esto no se puede hacer a través de Braze.**

## Requisitos de la API de WhatsApp

Tu número de teléfono debe cumplir estos requisitos de la API de WhatsApp:

- Ser propiedad de tu empresa 
- Tener un código de país y de área (como los números de teléfono fijo y móvil)
- Poder recibir llamadas de voz o SMS
- Ser accesible durante la configuración de la cuenta (para recibir códigos de verificación)
- No ser un código abreviado
- No haberse utilizado anteriormente con la plataforma WhatsApp Business
- No estar conectado a una cuenta personal de WhatsApp

## Adquirir un número de teléfono de Twilio

### Paso 1: Comprar un número de teléfono desde la consola o la API de Twilio

1. Desde la consola de Twilio, ve a **Develop** > **Phone Numbers** > **Manage** > **Buy a number**. Si no ves esta opción, selecciona **Explore Products**, desplázate hasta **Super Networks** y, a continuación, selecciona **Phone Number** > **Buy a number**. <br><br>![Consola de Twilio con la pestaña "Develop" abierta y la opción "Buy a number".]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Introduce el código de área o localidad que desees (si lo tienes). Busca un número y selecciona **Buy**. <br><br> ![Un botón para comprar el número de teléfono indicado.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Después de comprar tu número de teléfono, ve a **Active Numbers** y selecciona el número de teléfono que acabas de comprar. <br><br>!["Active Numbers", que muestra el número de teléfono adquirido.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Paso 2: Configura tu número de teléfono

Sigue las instrucciones de Twilio para configurar tu número de teléfono de Twilio y recibir el código de verificación por correo electrónico utilizando **únicamente** [Twilio Voice](https://www.twilio.com/docs/whatsapp/self-sign-up#add-your-whatsapp-phone-number). **No sigas las instrucciones de ningún otro paso.**

{% alert warning %}
Solo sigue las instrucciones de Twilio para recibir un código de verificación.
Si sigues los siguientes pasos, conectarás tu número de teléfono a Twilio, lo que significa que no podrás conectar ese número a Braze a menos que hagas una migración o compres un número diferente.
{% endalert %}

1. En la consola de Twilio, ve a la [página de Active Numbers](https://www.twilio.com/console/phone-numbers/incoming) y selecciona el número de teléfono que compraste.
2. Ve a la sección **Voice Configuration** y en el desplegable **Configure with**, selecciona **Webhook, TwiML Bin, Function, Studio Flow, Proxy Service**.
3. En la fila **A call comes in**, selecciona **Webhook** y establece la URL como `https://twimlets.com/voicemail?Email=YOUR_EMAIL_ADDRESS`, reemplazando `YOUR_EMAIL_ADDRESS` con tu dirección de correo electrónico.
4. En la consola de Twilio, ve a **2. Link WhatsApp Business Account with your number** > **2. Copy the phone number you register** y selecciona **Copy** junto al número de teléfono.
5. En la ventana **Self Sign-up**, en la página **Add your WhatsApp phone number**, selecciona **Add a new phone number** y pega el número de teléfono.
6. Selecciona **Phone call** como método de verificación y luego selecciona **Next**.
7. Recibirás el código de verificación en tu correo electrónico en un plazo de 10 minutos.

### Paso 3: Completa el flujo de trabajo de registro integrado

1. Una vez configurado Twilio, ve a tu dashboard de Braze > **Technology Partners** > **WhatsApp** y selecciona **Begin integration** o **Add WhatsApp Business Account**, lo que aparezca, para activar el [flujo de trabajo de registro integrado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br>En el paso **Add a phone number for WhatsApp**, selecciona **Phone call** para verificar tu número de teléfono. <br><br>![Sección con las opciones para verificar tu número de teléfono a través de un mensaje de texto o una llamada telefónica.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Espera unos minutos a que el código de verificación se envíe a tu buzón de correo electrónico y, a continuación, introduce el código de verificación y completa la configuración.

## Adquirir un número de teléfono de Infobip 

1. En la consola de Infobip, ve a **Channels and Numbers** y selecciona **Numbers**.<br><br>![Sección "Channels and Numbers" de Infobip con "Numbers" debajo.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Selecciona **Buy Number** > el país al que deseas enviar mensajes > **SMS**.<br><br>![Botón para comprar un número.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Dependiendo del país seleccionado, es posible que tengas que completar un proceso de registro adicional (como seleccionar una opción 10DLC o de número gratuito para los números de teléfono de EE. UU.). Asegúrate de seleccionar la opción disponible.<br><br>![Una página que te pide que selecciones el tipo de número: 10DLC o número gratuito.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Selecciona la oferta disponible, sigue el resto de los pasos y espera a que se procese tu solicitud. Puedes comprobar el estado accediendo a **Numbers** > **My Request**. <br><br>![Una oferta con información que incluye tarifas y cobertura.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Dependiendo del país que hayas elegido, espera a que el equipo de Infobip se ponga en contacto contigo para darte los detalles del registro (como en el caso de 10DLC en EE. UU.).<br><br>

6. Cuando tu número de teléfono esté listo en Infobip, ve a tu dashboard de Braze > **Technology Partners** > **WhatsApp** y selecciona **Begin integration** o **Add WhatsApp Business Account**, lo que aparezca, para activar el [flujo de trabajo de registro integrado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br> En el paso **Add a phone number for WhatsApp**, selecciona **Text message** para verificar tu número de teléfono.<br><br>![Sección con las opciones para verificar tu número de teléfono a través de un mensaje de texto o una llamada telefónica.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Comprueba los [registros de análisis](https://www.infobip.com/docs/analyze/analyze-logs) de Infobip en su portal de clientes para ver el código de verificación, que puede tardar unos minutos en aparecer. A continuación, introduce el código de verificación y completa la configuración.