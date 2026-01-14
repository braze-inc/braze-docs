---
nav_title: Adquisición de números de teléfono
article_title: Número de teléfono Adquisición
page_order: 3
description: "Este artículo de referencia explica cómo adquirir un número de teléfono de Twilio e Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Adquisición de números de teléfono

> Para utilizar el canal de mensajería de WhatsApp, necesitarás un número de teléfono que cumpla los requisitos de WhatsApp para su [API en la nube](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) o [su API local](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers).

Debes adquirir tu número de teléfono tú mismo, ya que Braze no te lo proporcionará. Puedes comprar un teléfono físico con una tarjeta SIM a través de tu proveedor de telefonía profesional o utilizar uno de nuestros socios: Twilio o Infoblip. **Debes tener tu propia cuenta de Twilio o Infobip porque esto no se puede hacer a través de Braze.**

## Requisitos de la API de WhatsApp

Tu número de teléfono debe cumplir estos requisitos de la API de WhatsApp:

- Propiedad de tu empresa 
- Tener un código de país y de área (como los números de teléfono fijo y móvil)
- Capaz de recibir llamadas de voz o SMS
- Accesible durante la configuración de la cuenta (para recibir códigos de verificación)
- No es un código abreviado
- No utilizado previamente con la plataforma WhatsApp Business
- No conectado a una cuenta personal de WhatsApp

## Adquirir un número de teléfono Twilio

### Paso 1: Comprar un número de teléfono desde la consola o API de Twilio

1. Desde la consola de Twilio, ve a **Desarrollo** > **Números de teléfono** > **Gestionar** > **Comprar un número**. Si no ves esta opción, selecciona **Explorar productos**, desplázate hasta **Superredes** y, a continuación, selecciona **Número de teléfono** > **Comprar un número**. <br><br>\![Consola de Twilio con la pestaña "Desarrollar" abierta y la opción "Comprar un número".]({% image_buster /assets/img/whatsapp/develop_buy_number.png %}){: style="max-width:20%;"}<br><br>

2. Introduce el código de área o localidad que desees (si lo tienes). Busca un número y selecciona **Comprar**. <br><br> \![Un botón para comprar el número de teléfono de la lista.]({% image_buster /assets/img/whatsapp/buy.png %})<br><br>

3. Después de comprar tu número de teléfono, ve a **Números activos** y selecciona el número de teléfono que acabas de comprar. <br><br>\!["Números activos" que muestra el número de teléfono comprado.]({% image_buster /assets/img/whatsapp/active_numbers.png %}){: style="max-width:70%;"}<br><br>

### Paso 2: Configura tu número de teléfono

Sigue las instrucciones de Twilio para [configurar tu número de teléfono Twilio para recibir el código de verificación por correo electrónico utilizando Sólo Voz Twilio](https://www.twilio.com/docs/whatsapp/self-sign-up#verify-your-whatsapp-sender). **No sigas las instrucciones de ningún otro paso, ya que eso conectará tu número de teléfono a Twilio, no a Braze.**

{% alert warning %}
**Sólo tienes que seguir las instrucciones de Twilio para recibir un código de verificación.**

Si sigues los siguientes pasos de las instrucciones de Twilio, conectarás tu número de teléfono a Twilio. Eso significa que no puedes conectar ese número a Braze a menos que hagas una migración o compres un número diferente.
{% endalert %}

### Paso 3: Completa el flujo de trabajo de registro integrado

1. Una vez configurado Twilio, ve a tu panel Braze > **Socios tecnológicos** > **WhatsApp** y selecciona **Iniciar integración** o **Añadir cuenta de WhatsApp Business**, lo que aparezca, para desencadenar el [flujo de trabajo de registro integrado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br>En el paso **Añadir un número de teléfono para WhatsApp**, selecciona **Llamada telefónica** para saber cómo quieres verificar tu número de teléfono. <br><br>Sección con las opciones para verificar tu número de teléfono mediante un mensaje de texto o una llamada telefónica.]({% image_buster /assets/img/whatsapp/verify.png %}){: style="max-width:50%;"}<br><br>

2. Espera unos minutos a que el código de verificación se envíe a tu buzón de entrada de correo electrónico y, a continuación, introduce el código de verificación y completa la configuración.

## Adquirir un número de teléfono Infobip 

1. En la consola Infobip, ve a **Canales y Números** y selecciona **Números**.<br><br>Sección "Canales y Números" de Infoblip con "Números" debajo.]({% image_buster /assets/img/whatsapp/infoblip_numbers.png %}){: style="max-width:30%;"}<br><br>

2. Selecciona **Comprar número** > el país al que quieres enviar mensajes > SMS.<br><br>\![Botón para comprar un número.]({% image_buster /assets/img/whatsapp/infoblip_buy.png %})<br><br>

3. Dependiendo del país seleccionado, puede que tengas que completar un proceso de registro adicional (como seleccionar una opción de 10 DLC o de llamada gratuita para los números de teléfono de EE.UU.). Asegúrate de seleccionar la opción disponible.<br><br>Aparece una página que te pide que selecciones el tipo de número: 10 DLC o gratuito.]({% image_buster /assets/img/whatsapp/infoblip_10dlc.png %}){: style="max-width:70%;"}<br><br>

4. Selecciona la oferta disponible, sigue el resto de los pasos y espera a que se procese tu solicitud. Puedes comprobar el estado yendo a **Números** > **Mi solicitud**. <br><br>Una oferta con información, incluidas las tarifas y la cobertura.]({% image_buster /assets/img/whatsapp/infoblip_offer.png %}){: style="max-width:70%;"}<br><br>

5. Dependiendo del país que hayas elegido, espera a que el equipo de Infobip se ponga en contacto contigo para facilitarte los datos de registro (como en el caso de 10DLC en EE.UU.).<br><br>

6. Cuando tu número de teléfono esté listo en Infobip, ve a tu panel Braze > **Socios tecnológicos** > **WhatsApp** y selecciona **Iniciar integración** o **Añadir cuenta de WhatsApp Business**, lo que aparezca, para desencadenar el [flujo de trabajo de registro integrado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).<br><br> En el paso **Añadir un número de teléfono para WhatsApp**, selecciona **Mensaje de texto** para saber cómo quieres verificar tu número de teléfono.<br><br>Sección con las opciones para verificar tu número de teléfono mediante un mensaje de texto o una llamada telefónica.]({% image_buster /assets/img/whatsapp/infoblip_verify.png %})<br><br>

7. Comprueba [los registros de análisis](https://www.infobip.com/docs/analyze/analyze-logs) de Infobip en su portal de clientes para ver el código de verificación, que puede tardar unos minutos en aparecer, después introduce el código de verificación y completa la configuración.




