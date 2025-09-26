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

> Una capa de conexión segura (SSL) cifra una URL con HTTPS, en lugar de la menos segura HTTP. HTTPS en una URL indica que existe un certificado SSL o TLS válido y de confianza, y que el sitio web es seguro de visitar y no es una fuente de malware peligroso.

## ¿Por qué es importante el SSL?

Aunque la mayoría de los dominios no requieren SSL, Braze recomienda encarecidamente el uso de SSL por estas razones clave.

Proteger su sitio web y sus enlaces con SSL es una práctica habitual incluso para las empresas que no manejan directamente información confidencial de sus clientes. Los usuarios confían más en los enlaces protegidos con SSL, y la capa adicional de autenticación ayuda a proteger sus datos.

### Necesario para el seguimiento de clics y aperturas

En Braze, cuando enviamos correos electrónicos, primero transformamos sus enlaces utilizando su subdominio de seguimiento de enlaces de marca para realizar un seguimiento de los clics y aperturas de los usuarios. Por defecto, estos enlaces comenzarán por HTTP. Esto significa que los usuarios con un navegador o extensión que restrinja el tráfico no seguro pueden tener dificultades para pasar a través de la redirección antes de aterrizar en la URL de destino, incluso si la URL es segura. Esto puede dar lugar a imágenes rotas y a un seguimiento inexacto de los clics y las aperturas en todos sus mensajes de correo electrónico. Por este motivo, es una buena práctica aplicar una capa SSL al subdominio de seguimiento de enlaces para confirmar redireccionamientos seguros en sus correos electrónicos. 

### Requisitos del navegador

Los protocolos SSL son cada vez más frecuentes hoy en día, ya que los principales navegadores, como Google Chrome, están empezando a restringir el tráfico a través de URL no seguras para proteger a sus usuarios. Las empresas con SSL en su sitio web confirman con estos navegadores principales que su contenido es de confianza, lo que minimiza los problemas de visualización de contenido, como enlaces rotos e imágenes en sus correos electrónicos.

### Requisito de dominios HSTS 

Independientemente de los navegadores desde los que sus usuarios puedan acceder a sus correos electrónicos, debe configurar SSL si tiene un dominio HTTP Strict Transport Security (HSTS) y configurar una CDN para que envíe los certificados de seguridad necesarios. Si no se configura SSL, se romperán tanto las imágenes como los enlaces web.

## Adquisición de un certificado SSL

Puede adquirir un certificado SSL a través de un tercero, normalmente una red de distribución de contenidos (CDN). Una CDN puede alojar el certificado SSL y servirlo al navegador cada vez que se haga clic en uno de sus enlaces. Esto se hace redirigiendo el tráfico a través de la CDN para aplicar los certificados necesarios antes de enviarlo a través de nuestros socios de correo electrónico SendGrid o SparkPost.

Para empezar con la configuración de SSL, póngase en contacto con su gestor de éxito de clientes de Braze para iniciar una configuración completa de correo electrónico Braze.

Después de que Braze haya iniciado esta configuración, sigue estos pasos:
1. Braze le proporcionará registros DNS para que los añada al registro de su dominio.
2. Braze verificará si los registros se han añadido correctamente a su registro.
3. Después de esto, seleccionarás una CDN y obtendrás certificados SSL de un proveedor externo. 
4. En este punto, configurarás tu CDN. Ten en cuenta que Braze no podrá ayudarte a solucionar problemas de configuración de CDN. Póngase en contacto con su proveedor de CDN para obtener más ayuda.
5. Póngase en contacto con su gestor de atención al cliente para activar SSL.

### ¿Qué es una CDN y por qué la necesito?

Una red de distribución de contenidos (CDN) es una plataforma de servidores que ayuda a garantizar tiempos de carga rápidos de contenidos de alta calidad a través de múltiples medios, al tiempo que gestiona los certificados de seguridad. 

{% alert important %}
La configuración de la CDN se realiza siempre después de que Braze haya validado sus registros DNS. Si aún no ha iniciado este paso, póngase en contacto con su gestor de éxito de clientes para obtener más información sobre cómo empezar.
{% endalert %}

En Braze, para realizar el seguimiento de clics y aperturas, nuestros socios de distribución transforman los enlaces utilizando un subdominio de marca, y la CDN aplica el certificado SSL a esos enlaces recién transformados. A menudo, nuestros socios de entrega deben presentar certificados válidos y fiables al navegador del destinatario de su correo electrónico para que los enlaces y las imágenes se muestren correctamente. Dado que Braze no solicita ni gestiona dichos certificados, deberás configurarlos tú mismo a través de una CDN. 

{% alert note %}
Si no puede o no desea utilizar las CDN enumeradas al configurar SSL para el seguimiento de clics y aperturas, puede establecer una configuración SSL personalizada. Tenga en cuenta que las CDN alternativas o los proxies personalizados pueden dar lugar a una configuración más compleja y matizada. Consulte los artículos de [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) y [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) sobre este tema.
{% endalert %}

#### Recursos adicionales

{% alert important %}
Para obtener más ayuda con la solución de problemas de tu configuración de CDN, debes ponerte en contacto con tu proveedor de CDN.
{% endalert %}

La siguiente tabla incluye guías paso a paso escritas por socios de ESP sobre cómo configurar determinadas CDN. Aunque es posible que su CDN específica no aparezca en la lista, debe asegurarse de que su CDN tiene la capacidad de aplicar certificados SSL.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud Platform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para Amazon SES, consulta [Opción 2: Configuración de un dominio HTTPS](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) y especifica el dominio de seguimiento de AWS por tu región en función de tu clúster de Braze:

- **Clústeres Braze US:** `r.us-east-1.awstrack.me`
- **Clústeres Braze UE:** `r.eu-central-1.awstrack.me`

{% alert important %}
Cuando configures el dominio de seguimiento de clics de tu CDN, asegúrate de habilitar la cabecera `X-Forwarded-Host`. Se utiliza para evitar posibles problemas de seguridad, como ataques a la cabecera del host. Consulta la documentación de la CDN o a tu equipo de soporte para saber cómo hacerlo, ya que varía en función de la CDN.
{% endalert %}

#### Solución de problemas

Aunque la configuración de la CDN, los certificados y los problemas de proxy deben tratarse con la CDN, a continuación se ofrecen algunos consejos generales para la solución de problemas que le ayudarán a identificar los problemas más comunes con la configuración del seguimiento de clics SSL.

##### Problemas con el registro de dominios

Un comando dig puede decirle si está apuntando su seguimiento de enlaces al CDN. Puedes hacerlo en tu terminal ejecutando `dig CNAME link_tracking_subdomain`. Una vez ejecutado el comando, en `ANSWER SECTION`, debería aparecer una lista de dónde apunta su CNAME. Si apuntaba a su proveedor de servicios de correo electrónico elegido (SendGrid o SparkPost) y no a su CDN, intente reconfigurar el registro de su dominio para que apunte a su CDN.

##### Problemas de CDN

Si sus enlaces de correo electrónico en vivo comienzan a romperse durante la configuración, esto generalmente significa que ha apuntado su DNS hacia su CDN sin que esté configurado correctamente. Esto puede aparecer como un error de "enlace incorrecto". Póngase en contacto con su proveedor de CDN y revise su documentación para ayudarle a solucionar los problemas de configuración de su CDN.

##### Estado de activación de SSL

Si ha completado la configuración de SSL y sus enlaces siguen apareciendo como HTTP y no como HTTPS, póngase en contacto con su gestor de éxito de clientes de Braze para asegurarse de que Braze ha habilitado SSL. Braze sólo puede activar SSL una vez que se hayan completado todos los aspectos de la configuración de SSL.

