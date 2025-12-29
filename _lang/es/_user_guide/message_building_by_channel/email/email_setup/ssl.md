---
nav_title: SSL en Braze
article_title: Resumen de SSL
page_order: 5
page_type: reference
description: "Este artículo de referencia trata sobre SSL, para qué se utiliza y cómo se utiliza en Braze."
channel: email

---

# SSL en Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> Una capa de conexión segura (SSL) encripta una URL con HTTPS, en lugar de la menos segura HTTP. HTTPS en una URL indica que existe un certificado SSL o TLS válido y de confianza, y que el sitio web es seguro de visitar y no es una fuente de malware peligroso.

## ¿Por qué es importante el SSL?

Aunque la mayoría de los dominios no requieren SSL, Braze recomienda encarecidamente el uso de SSL por estas razones clave.

Proteger tu sitio web y tus enlaces con SSL es una práctica habitual, incluso para las empresas que no manejan directamente información confidencial de sus clientes. Los usuarios confían más en los enlaces protegidos con SSL, y la capa adicional de autenticación ayuda a proteger tus datos.

### Necesario para el seguimiento de clics y aperturas

En Braze, cuando enviamos correos electrónicos, primero transformamos tus enlaces utilizando el subdominio de seguimiento de enlaces de tu marca para hacer un seguimiento de los clics y aperturas de los usuarios. Por defecto, estos enlaces empezarán por HTTP. Esto significa que los usuarios con un navegador o extensión que restrinja el tráfico no seguro pueden tener dificultades para pasar por la redirección antes de aterrizar en la URL de destino, aunque la URL sea segura. Esto puede dar lugar a imágenes rotas y a un seguimiento inexacto de clics y aperturas en todos tus correos electrónicos. Por esta razón, es una buena práctica aplicar una capa SSL al subdominio de seguimiento de enlaces para confirmar redireccionamientos seguros en tus correos electrónicos. 

### Requisitos del navegador

Los protocolos SSL son cada vez más frecuentes hoy en día, ya que los principales navegadores, como Google Chrome, están empezando a restringir el tráfico a través de URL no seguras para proteger a sus usuarios. Las empresas con SSL en su sitio web confirman con estos navegadores principales que su contenido es de confianza, lo que minimiza los problemas de visualización de contenido, como enlaces rotos e imágenes en sus correos electrónicos.

### Requisito de dominios HSTS 

Independientemente de los navegadores desde los que tus usuarios accedan a tus correos electrónicos, debes configurar SSL si tienes un dominio HTTP Strict Transport Security (HSTS) y configurar una CDN para que envíe los certificados de seguridad necesarios. Si no se configura SSL, se romperán los enlaces de imagen y Web.

## Adquirir un certificado SSL

Puedes adquirir un certificado SSL utilizando un tercero, normalmente una Red de Entrega de Contenidos (CDN). Una CDN puede alojar el certificado SSL y servirlo al navegador cada vez que se haga clic en uno de tus enlaces. Esto se hace redirigiendo el tráfico a través de la CDN para aplicar los certificados necesarios antes de enviarlo a nuestros socios de correo electrónico SendGrid o SparkPost.

Para empezar a configurar tu SSL, ponte en contacto con tu administrador del éxito del cliente Braze para iniciar la configuración completa del correo electrónico Braze.

Después de que Braze haya iniciado esta configuración, sigue estos pasos:
1. Braze te proporcionará registros de DNS para que los añadas a tu registro de dominios.
2. Braze verificará si los registros se han añadido correctamente a tu registro.
3. Después de esto, seleccionarás una CDN y obtendrás certificados SSL de un proveedor externo. 
4. En este punto, configurarás tu CDN. Ten en cuenta que Braze no podrá ayudarte a solucionar problemas de configuración de CDN. Ponte en contacto con tu proveedor de CDN para obtener más ayuda.
5. Ponte en contacto con tu administrador del éxito del cliente para activar el SSL.

### ¿Qué es una CDN y por qué la necesito?

Una red de entrega de contenidos (CDN) es una plataforma de servidores que ayuda a garantizar tiempos de carga rápidos de contenidos de alta calidad a través de múltiples medios, a la vez que gestiona certificados de seguridad. 

{% alert important %}
La configuración de la CDN se realiza siempre después de que Braze haya validado tus registros de DNS. Si aún no has iniciado este paso, ponte en contacto con tu administrador del éxito del cliente para obtener más información sobre cómo empezar.
{% endalert %}

En Braze, para hacer el seguimiento de clics y aperturas, nuestros socios de entrega transforman los enlaces utilizando un subdominio de marca, y la CDN aplica el certificado SSL a esos enlaces recién transformados. A menudo, nuestros socios de entrega deben presentar certificados válidos y de confianza al navegador del destinatario de tu correo electrónico para que los enlaces y las imágenes se muestren correctamente. Dado que Braze no solicita ni gestiona dichos certificados, deberás configurarlos tú mismo a través de una CDN. 

{% alert note %}
Si no puedes o no deseas utilizar las CDN enumeradas al configurar SSL para el seguimiento de clics y aperturas, puedes establecer una configuración SSL personalizada. Ten en cuenta que las CDN alternativas o los proxies personalizados pueden dar lugar a una configuración más compleja y matizada. Consulta los artículos de [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) y [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) sobre este tema.
{% endalert %}

#### Recursos adicionales

{% alert important %}
Para obtener más ayuda con la solución de problemas de tu configuración de CDN, debes ponerte en contacto con tu proveedor de CDN.
{% endalert %}

La siguiente tabla incluye guías paso a paso escritas por socios de ESP sobre cómo configurar determinadas CDN. Aunque puede que tu CDN específica no aparezca en la lista, debes asegurarte de que tu CDN tiene capacidad para aplicar certificados SSL.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Rápidamente](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Rápidamente](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Plataforma en la nube de Google](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para Amazon SES, consulta [Opción 2: Configuración de un dominio HTTPS](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) y especifica el dominio de seguimiento de AWS por tu región en función de tu clúster de Braze:

- **Agrupaciones Braze US:** `r.us-east-1.awstrack.me`
- **Braze racimos UE:** `r.eu-central-1.awstrack.me`

{% alert important %}
Cuando configures el dominio de seguimiento de clics de tu CDN, asegúrate de habilitar la cabecera `X-Forwarded-Host`. Se utiliza para evitar posibles problemas de seguridad, como ataques a la cabecera del host. Consulta la documentación de la CDN o a tu equipo de soporte para saber cómo hacerlo, ya que varía en función de la CDN.
{% endalert %}

#### Solución de problemas

Aunque la configuración de la CDN, los certificados y los problemas con el proxy deben gestionarse con tu CDN, aquí tienes algunos consejos generales para la solución de problemas que te ayudarán a identificar los problemas más comunes con la configuración del seguimiento de clics SSL.

##### Problemas con el registro de dominios

Un comando dig puede decirte si estás apuntando tu seguimiento de enlaces a la CDN. Puedes hacerlo en tu terminal ejecutando `dig CNAME link_tracking_subdomain`. Una vez ejecutado el comando, en `ANSWER SECTION`, debería aparecer una lista de dónde apunta tu CNAME. Si apuntaba al proveedor de servicios de correo electrónico que elegiste (SendGrid o SparkPost) y no a tu CDN, prueba a reconfigurar el registro de tu dominio para que apunte a tu CDN.

##### Problemas de CDN

Si tus enlaces de correo electrónico en vivo empiezan a romperse durante la configuración, esto generalmente significa que has apuntado tus DNS hacia tu CDN sin que esté correctamente configurado. Esto puede aparecer como un error de "enlace incorrecto". Ponte en contacto con tu proveedor de CDN y revisa su documentación para que te ayude a solucionar los problemas de configuración de tu CDN.

##### Estado de habilitación de SSL

Si has completado la configuración de SSL y tus enlaces siguen apareciendo como HTTP y no como HTTPS, ponte en contacto con tu administrador del éxito del cliente de Braze para asegurarte de que Braze ha habilitado SSL. Braze sólo puede habilitar SSL una vez que se hayan completado todos los aspectos de la configuración de SSL.

