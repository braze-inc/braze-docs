---
nav_title: SSL en Braze
article_title: Descripción general de SSL
page_order: 5
page_type: reference
description: "Este artículo de referencia trata sobre SSL, para qué se utiliza y cómo se utiliza en Braze."
channel: email

---

# SSL en Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> Una capa de conexión segura (SSL) cifra una URL con HTTPS en lugar de HTTP. HTTPS indica que existe un certificado SSL o TLS válido y fiable y que el sitio web es seguro para visitar.

## ¿Por qué es importante el SSL?

La mayoría de los dominios no requieren SSL, pero Braze recomienda encarecidamente utilizar SSL por los siguientes motivos.

Proteger su sitio web y sus enlaces con SSL es una práctica habitual incluso para las empresas que no manejan directamente información confidencial de sus clientes. Los usuarios confían más en los enlaces protegidos con SSL, y la capa adicional de autenticación ayuda a proteger sus datos.

### Necesario para el seguimiento de clics y aperturas

Braze transforma tus enlaces utilizando tu subdominio de seguimiento de enlaces de marca para realizar el seguimiento de los clics y las aperturas. Predeterminadamente, estos enlaces comienzan con HTTP. Los usuarios con navegadores o extensiones que restringen el tráfico no seguro pueden tener dificultades para pasar por la redirección antes de la URL de destino, incluso si la URL es segura. Esto puede provocar imágenes rotas y un seguimiento inexacto. Aplica SSL al subdominio de seguimiento de enlaces para confirmar que las redirecciones son seguras.

### Requisitos del navegador

Los principales navegadores, como Google Chrome, restringen el tráfico a través de URL no seguras para proteger a los usuarios. El uso de SSL ayuda a confirmar que el contenido es fiable y minimiza problemas como enlaces e imágenes rotos en los correos electrónicos.

### Requisito de dominios HSTS 

Si tienes un dominio HTTP Strict Transport Security (HSTS), configura SSL y configura una CDN para enviar los certificados de seguridad necesarios. Sin SSL, los enlaces de imágenes y Web se rompen.

## Adquisición de un certificado SSL

Adquiere un certificado SSL a través de un tercero, normalmente una CDN. Una CDN aloja el certificado y lo envía al navegador cuando un usuario hace clic en un enlace, redirigiendo el tráfico a través de la CDN para aplicar los certificados antes de enviarlo a SendGrid o SparkPost.

Para iniciar la configuración de SSL, ponte en contacto con tu administrador del éxito del cliente de Braze para iniciar una configuración completa del correo electrónico de Braze.

Una vez que Braze haya iniciado la configuración, sigue estos pasos:
1. Braze le proporcionará registros DNS para que los añada al registro de su dominio.
2. Braze verificará si los registros se han añadido correctamente a su registro.
3. Después de esto, seleccionarás una CDN y obtendrás certificados SSL de un proveedor externo. 
4. En este punto, configurarás tu CDN. Ten en cuenta que Braze no podrá ayudarte a solucionar problemas de configuración de CDN. Ponte en contacto con tu proveedor de CDN si necesitas más ayuda.
5. Ponte en contacto con tu administrador del éxito del cliente para activar SSL.

### ¿Qué es una CDN y por qué la necesito?

Una red de entrega de contenidos (CDN) es una plataforma de servidores que ayuda a garantizar tiempos de carga rápidos de contenidos en múltiples medios, al tiempo que gestiona los certificados de seguridad. 

{% alert important %}
La configuración de la CDN se realiza siempre después de que Braze haya validado sus registros DNS. Si aún no has iniciado este paso, ponte en contacto con tu administrador del éxito del cliente para obtener más información sobre cómo empezar.
{% endalert %}

Para el seguimiento de clics y aperturas, los socios de entrega transforman los enlaces utilizando un subdominio de marca y la CDN aplica el certificado SSL a esos enlaces transformados. Los socios a menudo deben presentar certificados válidos al navegador del destinatario para que los enlaces y las imágenes se muestren correctamente. Dado que Braze no solicita ni administra certificados, debes configurarlo a través de una CDN. 

{% alert note %}
Si no puedes o no deseas utilizar las CDN indicadas para el seguimiento de clics y aperturas SSL, puedes configurar una configuración SSL personalizada. Las CDN alternativas o los proxies personalizados pueden dar lugar a una configuración más compleja. Consulta la documentación de [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) y [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

#### Recursos adicionales

{% alert important %}
Para la solución de problemas relacionados con la configuración de tu CDN, ponte en contacto con tu proveedor de CDN.
{% endalert %}

La siguiente tabla incluye guías paso a paso escritas por socios de ESP sobre cómo configurar determinadas CDN. Aunque es posible que su CDN específica no aparezca en la lista, debe asegurarse de que su CDN tiene la capacidad de aplicar certificados SSL.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para Amazon SES, consulta la [Opción 2: Configura un dominio HTTPS](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) y especifica el dominio de seguimiento de AWS por región en función de tu clúster de Braze:

- **Clústeres Braze US:** `r.us-east-1.awstrack.me`
- **Clústeres Braze UE:** `r.eu-central-1.awstrack.me`

{% alert important %}
Cuando configures el dominio de seguimiento de clics de tu CDN, habilita el`X-Forwarded-Host`encabezado  para evitar posibles problemas de seguridad, como los ataques de encabezado de host. Consulta la documentación de CDN o a tu equipo de soporte para conocer los pasos a seguir.
{% endalert %}

#### Solución de problemas

Aunque debes gestionar la configuración de la CDN, los certificados y los problemas de proxy con tu CDN, utiliza estos consejos para identificar los problemas habituales de seguimiento de clics SSL.

##### Problemas con el registro de dominios

Ejecuta un comando dig para confirmar que el seguimiento del enlace apunta a la CDN. En tu terminal, ejecuta `dig CNAME link_tracking_subdomain`. En `ANSWER SECTION`, se indica dónde apunta tu CNAME. Si apunta al proveedor de servicios de correo electrónico (SendGrid o SparkPost) y no a tu CDN, reconfigura el registro de tu dominio para que apunte a tu CDN.

##### Problemas de CDN

Si los enlaces de correo electrónico activos se rompen durante la configuración, es probable que hayas dirigido el DNS hacia tu CDN antes de realizar la configuración adecuada. Esto puede aparecer como un error de "enlace incorrecto". Ponte en contacto con tu proveedor de CDN y revisa su documentación para la solución de problemas de configuración.

##### Estado de activación de SSL

Si completas la configuración de SSL y los enlaces siguen apareciendo como HTTP, ponte en contacto con tu administrador del éxito del cliente de Braze para confirmar que Braze ha habilitado SSL. Braze solo habilita SSL una vez completados todos los pasos de configuración.

