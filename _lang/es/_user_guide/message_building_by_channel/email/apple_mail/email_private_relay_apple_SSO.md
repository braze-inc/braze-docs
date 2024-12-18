---
nav_title: Envío de correos electrónicos a Apple Private Relay
article_title: Envío de correos electrónicos a Apple Private Relay
alias: /email_relay/
page_order: 0
description: "Este artículo cubre el proceso de envío de correos electrónicos al sistema de Relay privado de Apple."
channel:
  - email
  
---

# Envío de correos electrónicos a Apple Private Relay

> Con el lanzamiento de iOS 13, Apple ha introducido una funcionalidad para los clientes de Apple que afecta a la forma en que se les envían los correos electrónicos. La función de inicio de sesión único (SSO) de Apple permite a sus usuarios compartir sus direcciones de correo electrónico (`example@icloud.com`) u ocultar sus direcciones de correo electrónico enmascarando lo que se proporciona a las marcas (`tq1234snin@privaterelay.appleid.com`) en lugar de su dirección de correo electrónico personal.

Estos usuarios pueden gestionar las aplicaciones que utilizan el inicio de sesión con Apple desde la página de configuración de su ID de Apple (consulte [la documentación de Apple](https://support.apple.com/en-us/HT210426)). Si un usuario decide desactivar el reenvío de correo electrónico al correo electrónico de retransmisión de su aplicación, Braze recibirá la información de rebote de correo electrónico como de costumbre. Para enviar correos electrónicos al relé de correo electrónico privado de Apple, registra tus dominios de envío con Apple.

## Envío de correos electrónicos para SendGrid

Si utiliza SendGrid como proveedor de correo electrónico, puede enviar correos electrónicos a Apple sin realizar cambios en los DNS. Vaya a su página **de certificados de Apple** y permita la dirección de correo electrónico que desea utilizar para el envío a través del servicio de retransmisión de correo electrónico de Apple (la dirección "De" que desee).  

![Opción para permitir direcciones de correo electrónico individuales en la página de certificados de Apple.]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

La dirección debe tener el formato siguiente: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`(e.g., `bounces+1234567@braze.online.docs.com`). Una vez añadida la dirección a la página de certificados de Apple, los correos electrónicos de este dominio se enviarán a través del sistema de retransmisión privada de Apple.

{% alert important %}
Si su dirección "De" deseada es una dirección `abmail`, inclúyala en su subdominio. Por ejemplo, utilice `abmail.docs.braze.com` en lugar de `docs.braze.com`. Puede que no sea el caso de tu dirección. Compruebe sus registros DNS en SendGrid.
{% endalert %}

### Valores de la dirección de origen

Consulte en esta tabla los componentes utilizados al añadir direcciones de correo electrónico con Apple Private Relay.

| Valor | Descripción |
|---|---|
| UID | Este valor se proporciona en sus registros DNS proporcionados por Braze (de SendGrid). No incluyas la letra "u" de tu UID en la dirección de correo electrónico. Por ejemplo, si tu UID se presenta en SendGrid como `u1234567.wl134.sendgrid.net`, entonces `1234567` es el valor del UID. <br><br> Si no tiene acceso a sus registros DNS, póngase en contacto con su gestor de éxito de clientes de Braze para que le proporcione su UID. |
| Subdominio y dominio con etiqueta blanca | El dominio y subdominio iniciales que introdujo en SendGrid. También puede utilizar el **valor HOST** en sus registros DNS en SendGrid. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Envío de correos electrónicos para SparkPost

Para configurar Apple Private Relay para SparkPost, siga estos pasos: 

1. Inicia sesión con Apple. 
2. Añade los dominios de correo electrónico. 
3. Apple comprobará automáticamente los dominios y mostrará cuáles están verificados, además de ofrecer la opción de reverificar o eliminar los dominios.

{% alert important %}
Asegúrese de completar este proceso en los 2 o 3 días siguientes a la creación de los archivos de verificación, o de lo contrario caducarán. Apple no revela durante cuánto tiempo son válidos.
{% endalert %}

Si tiene más preguntas, abra un [ticket de soporte]({{site.baseurl}}/braze_support/).
