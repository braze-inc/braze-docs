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

> La característica de inicio de sesión único (SSO) de Apple permite a sus usuarios compartir sus direcciones de correo electrónico (`example@icloud.com`) u ocultar sus direcciones de correo electrónico enmascarando lo que se proporciona a las marcas (`tq1234snin@privaterelay.appleid.com`) en lugar de su dirección de correo electrónico personal. Apple reenviará los mensajes enviados a las direcciones de retransmisión a la dirección de correo electrónico real del usuario. 

Para enviar correos electrónicos al relé de correo electrónico privado de Apple, registra tus dominios de envío con Apple. Si no configuras tus dominios con Apple, los correos electrónicos enviados a direcciones de retransmisión resultarán rebotados.

Si un usuario decide desactivar el reenvío de correo electrónico al correo electrónico de retransmisión de su aplicación, Braze recibirá la información de rebote de correo electrónico como de costumbre. Estos usuarios pueden gestionar las aplicaciones que utilizan el inicio de sesión con Apple desde la página de configuración de su ID de Apple (consulte [la documentación de Apple](https://support.apple.com/en-us/HT210426)).

## Envío de correos electrónicos para SendGrid

Si utiliza SendGrid como proveedor de correo electrónico, puede enviar correos electrónicos a Apple sin realizar cambios en los DNS. 

1. Entra en el [Portal del Desarrollador de Apple](https://developer.apple.com/)
2. Ve a la página **Certificados, identificadores y perfiles**.
3. Selecciona **Servicios** > **Iniciar sesión con Apple para comunicación por correo electrónico**.
4. En la sección **Fuentes de correo electrónico**, añade los dominios y subdominios.
- La dirección debe tener el formato : `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (un ejemplo es: `bounces+1234567@braze.online.docs.com`). 

Si su dirección "De" deseada es una dirección `abmail`, inclúyala en su subdominio. Por ejemplo, utilice `abmail.docs.braze.com` en lugar de `docs.braze.com`.

## Envío de correos electrónicos para SparkPost

Para configurar Apple Private Relay para SparkPost, siga estos pasos: 

1. Inicia sesión con Apple.
2. Sigue [la documentación de Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) para registrar los dominios de correo electrónico.
3. Apple comprobará automáticamente los dominios, mostrará cuáles están verificados y ofrecerá la opción de reverificarlos o eliminarlos.

### Consideraciones

Si un dominio de envío también se utiliza como dominio de rebote, no podrás almacenar ningún registro y tendrás que seguir estos pasos adicionales:

1. Si el dominio ya ha sido verificado en SparkPost, **debes** crear los registros MX y TXT: 

| Instancia | Registro MX                   | Registro TXT                                    |
|----------|-----------------------------|-----------------------------------------------|
| US       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
Para evitar fallos SPF, debes crear los registros MX y TXT y hacer que se propaguen en el DNS **antes de** eliminar el registro CNAME.
{% endalert %}

{:start="2"}
2\. Elimina el registro CNAME.
3\. Sustitúyelo por los registros MX y TXT para un correcto enrutamiento.
4\. Crea tu registro A para que apunte a tu CDN o alojamiento de archivos.

Si tiene más preguntas, abra un [ticket de soporte]({{site.baseurl}}/braze_support/).
