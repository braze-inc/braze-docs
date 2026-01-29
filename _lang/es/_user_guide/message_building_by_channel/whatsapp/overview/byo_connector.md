---
nav_title: Conector BYO WhatsApp
article_title: "Conector \"Trae tu propio WhatsApp"
page_order: 0
description: "Este artículo de referencia proporciona una guía paso a paso para configurar un conector WhatsApp Bring Your Own, que da acceso a Braze a tu administrador de negocios WhatsApp de Infobip."
page_type: reference
channel:
  - WhatsApp
---

# Conector "Trae tu propio WhatsApp

> El conector Bring Your Own (BYO) WhatsApp ofrece una asociación entre Braze e Infobip, en la que das acceso a Braze a tu administrador de negocios WhatsApp de Infobip (WABA). Esto te permite gestionar y pagar los costes de mensajería directamente con Infobip, a la vez que utilizas Braze para la segmentación, personalización y orquestación de campañas. Braze mantiene toda la funcionalidad existente que ofrece el canal de WhatsApp, como mensajes salientes, procesamiento de mensajes entrantes, flujos de WhatsApp y análisis.

## Requisitos 

| Requisito | Descripción |
| --- | --- |
| Cuenta Infobip | Se necesita una cuenta Infobip para utilizar el conector BYO WhatsApp.
| Créditos de mensajería | Consumes créditos de mensajería Braze cuando envías mensajes de WhatsApp. |
| Requisitos de WhatsApp | Completa todos los [requisitos de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#prerequisites). |
| Número de teléfono | Te sugerimos que [adquieras un número de teléfono a través de Infobip](https://www.infobip.com/docs/numbers/getting-started) para mayor comodidad. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Configurar 

Antes de configurar el conector BYO WhatsApp, confirma que el envío anterior de tu cuenta de WhatsApp Business no se ha realizado a través de Infobip.

### Casos admitidos

- La cuenta de WhatsApp Business y el número de teléfono nunca antes se habían conectado a un socio
- La cuenta de WhatsApp Business está conectada directamente a Braze a través de la integración nativa.
    - Sigue los pasos de la [migración de números de teléfono de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/) para migrar tus números de teléfono a una nueva cuenta de WhatsApp Business, número a número.
- La cuenta de WhatsApp Business está conectada a un proveedor de soluciones distinto de Braze e Infobip
    - Sigue los pasos de la [migración de números de teléfono de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration/) para migrar tus números de teléfono a una nueva cuenta de WhatsApp Business, número a número.

## Paso 1: Recuperar información de la cuenta Infobip {#step-1}

1. En Infobip, identifica la cuenta que quieres utilizar con tu cuenta de WhatsApp Business. 
2. Ve a **Herramientas del desarrollador** > **Claves de API** y selecciona **Crear clave de API**.

![Página "Crear clave de API" con fecha de creación "16/12/2025" y fecha de caducidad "16/12/36".]({% image_buster /assets/img/whatsapp/byo_connector/create_api_key.png %})

{: start="3"}
3\. Dale a la clave un nombre significativo, como "Braze - Nombre de mi espacio de trabajo - Nombre de mi WABA".
4\. Añade una fecha de caducidad lejana en el tiempo para evitar problemas con la caducidad del token.
    \- Toma nota para generar una nueva clave de API y vuelve a conectar tu WABA antes de la fecha de caducidad.
5\. Selecciona estos ámbitos:
- `Message:send`
- `Whatsapp:manage`
- `Whatsapp:message:send`
- `Account-management:manage`
- `Subscriptions:manage`
- `Metrics:manage`
6. Después de crear la clave, copia la clave de API.
    - La clave sólo puede copiarse durante un tiempo limitado tras su creación. Puedes repetir estos pasos para crear una nueva clave si necesitas conectar otra cuenta de WhatsApp Business en el futuro.

!["Ejemplo Braze de clave de API" con 6 ámbitos añadidos.]({% image_buster /assets/img/whatsapp/byo_connector/api_key.png %})

{: start="7"}
7\. Copia la URL base de la API de la cuenta.

![Página "Claves de API" con una URl base de API resaltada.]({% image_buster /assets/img/whatsapp/byo_connector/api_base_url.png %})

## Paso 2: Iniciar el registro incrustado

1. En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** > **WhatsApp**
2. Selecciona la pestaña **Conector BYO - Infobip**.

![La página de socios tecnológicos de WhatsApp.]({% image_buster /assets/img/whatsapp/byo_connector/byo_tab_tech_parners.png %})

{: start="3"}
3\. Introduce la clave de API y la URL base del [Paso 1](#step-1).
4\. Selecciona **Conectar**.
5\. Procede con el [flujo de trabajo de Registro incrustado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/#whatsapp-embedded-signup-workflow) teniendo en cuenta estas consideraciones:
- No puedes seleccionar la misma cartera de negocios que utiliza otro Proveedor de Soluciones Empresariales.
- No puedes seleccionar un número de teléfono que utilice otro Proveedor de Soluciones Empresariales.
- Debes crear un nuevo WABA, no seleccionar uno existente.

{% alert note %}
Para recibir el código de verificación, ve a tu panel Infobip > **Analizar** > **Registros**, y extrae el código del mensaje SMS entrante.  
{% endalert %}

![Registros de mensajes que muestran un mensaje SMS entrante con el código de verificación.]({% image_buster /assets/img/whatsapp/byo_connector/verification_code.png %})

Una vez completada la configuración, tu número de teléfono aparecerá como grupo de suscripción en tu grupo de WhatsApp Business. El grupo de WhatsApp Business contiene el nombre de la cuenta de Infobip y la URL base de la API a la que está conectado. Las cuentas conectadas a través de la integración nativa no tienen un nombre de cuenta Infobip.

{% alert note %}
Conecta cada cuenta de WhatsApp Business a una única cuenta de Infobip. Cada vez que conectes un número de teléfono o grupo de suscripción adicional, si la cuenta de WhatsApp Business ya está conectada a una cuenta de Infobip, deberás volver a introducir las credenciales API de la cuenta existente.
{% endalert %}

## Paso 3: Envío de mensajes

Sigue el proceso de envío de la integración nativa, incluyendo:
- [Suscripción de usuarios al grupo de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)
- [Crear un mensaje de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/)

## Solución de problemas de configuración

### No se ha podido recuperar el ID de la cuenta de WhatsApp Business

Confirma que tu cuenta de WhatsApp Business no está conectada a otro espacio de trabajo de Braze.

### No se ha podido compartir el ID de la cuenta de WhatsApp Business con Infobip

1. Confirma que tu cuenta de WhatsApp Business no está conectada a Braze o a otro socio.
2. Confirma que ningún número de teléfono de tu cuenta de WhatsApp Business está conectado a otra cuenta de Infobip. Para los números importados, puedes buscar el número en Infobip y seleccionar **Cancelar número**.

![El botón "Anular número" de un número Infobip.]({% image_buster /assets/img/whatsapp/byo_connector/cancel_number.png %})

## Consideraciones 


Aunque todas las funciones existentes con Braze son compatibles, estos casos de uso no lo son actualmente.

| Casos de uso | Causa |
| --- | --- |
| Procesamiento de mensajes entrantes en Braze e Infobip | Esto evita que los trenes lógicos desencadenados por uno u otro sistema generen hilos de mensajes duplicados y potencialmente contradictorios. |
| Envío de mensajes desde Braze e Infobip | Para las cuentas de WhatsApp Business conectadas a Braze, todos los envíos se originan en Braze. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation” }

