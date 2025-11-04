---
nav_title: Configuración de IP y dominios
article_title: Configuración de IP y dominios
page_order: 0
page_type: tutorial
channel: email
description: "Este artículo te explicará cómo configurar tus IP y dominios para enviar correos electrónicos a través de Braze."

---

# Configuración de IP y dominios

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

> Este artículo te guiará a través de los requisitos y pasos necesarios para configurar tus direcciones IP y pools, así como los dominios y subdominios necesarios antes de que puedas empezar a enviar correos electrónicos con Braze.<br><br>Aunque la mayor parte del proceso de configuración la realiza Braze, hemos descrito los requisitos y materiales para esta configuración.

## Método 1: Coordinar con Braze (recomendado)

### Paso 1: Información general

Envía la siguiente información a tu representante de Braze:

* Tus dominios y subdominios elegidos
* El número aproximado de correos electrónicos que enviarás cada mes, lo que te ayudará a determinar cuántas IP necesitarás
* Cómo prefieres mapear tus dominios de envío a tu IP asignada

### Paso 2: Braze configura la información

Tras recibir tu correo electrónico, nos pondremos manos a la obra para configurar tus IP, dominios y subdominios, y grupos de IP.

### Paso 3: Añadir registros de DNS

Una vez configuradas tus IP, dominios, subdominios y grupos de IP, te enviaremos una lista de registros de DNS. Pide a tus ingenieros y desarrolladores que añadan estos registros de DNS cuando sea necesario y, una vez incorporados, informa al equipo de incorporación de Braze.

### Próximos pasos

Comprobaremos tu configuración y validaremos toda la información en nuestros sistemas internos. El equipo de incorporación de Braze te avisará cuando estés listo para empezar, o si hay problemas con tus registros de DNS que debas solucionar con tu equipo de ingeniería.

## Método 2: Configuración de correo electrónico de autoservicio

Este método configurará un dominio de envío, un dominio de seguimiento y una IP en total para una empresa. Si tienes pensado configurar más, consulta con el equipo de incorporación de Braze (método 1).

{% alert important %}
Esta característica de configuración de correo electrónico de autoservicio está actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en la beta.<br>Si utilizas la característica de configuración de correo electrónico de autoservicio, asegúrate de consultar también con el equipo de incorporación de Braze.
{% endalert %}

### Requisitos previos

Para utilizar el autoservicio de configuración de correo electrónico, debes cumplir los siguientes requisitos previos:

1. Eres un nuevo cliente en incorporación.
2. Tienes el permiso "Puede administrar la configuración de la empresa" a nivel de empresa.

### Paso 1: Iniciar la configuración

1. Ve a **Configuración** > **Configuración del administrador** en **Configuración de la empresa**. 
2. A continuación, selecciona la pestaña **Verificación del remitente**. Para ver esta pestaña, debes tener el permiso de nivel de empresa "Puede administrar configuración de la empresa".
3. Haz clic en el botón **Iniciar configuración**.

### Paso 2: Añadir y verificar un dominio de envío

Un dominio de envío se utiliza en la dirección "de" al enviar un correo electrónico. Introduce un dominio de envío y haz clic en **Enviar**. 

A continuación, añade los registros TXT y CNAME de la parte inferior de la página a tu proveedor de DNS. A continuación, vuelve al panel de Braze y haz clic en **Verificar**.

\![]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

{% alert important %}
El dominio de envío debe estar subordinado a un dominio de tu propiedad. Por ejemplo, si eres propietario de "example.com", un subdominio podría ser "mail.example.com", lo que te permitiría utilizar la dirección de envío "@mail.example.com".
{% endalert %}

### Paso 3: Añadir y verificar un dominio de seguimiento

Un dominio de seguimiento se utiliza para envolver enlaces en tus correos electrónicos con fines de seguimiento de clics y de marca. Esto será visible para los usuarios cuando pasen por encima o hagan clic en tus enlaces de correo electrónico. Te recomendamos que lo hagas coincidir con tu dominio de envío.

Introduce un dominio de seguimiento y haz clic en **Enviar**. A continuación, añade los registros CNAME de la parte inferior de la página a tu proveedor de DNS. A continuación, vuelve al panel de Braze y haz clic en **Verificar**.

### Paso 4: Añadir una dirección IP

Braze generará un registro A para asociar tu dirección IP a tu subdominio de envío en una configuración denominada DNS inverso (rDNS). Añade el registro de DNS en tu proveedor de DNS y, a continuación, haz clic en **Configurar rDNS** para admitir la capacidad de entrega.

Ten en cuenta que los dominios adicionales que se hayan añadido no aparecerán en la sección **Verificación del remitente**. Para añadir más dominios, ponte en contacto con el equipo de soporte de Braze.

### Próximos pasos

Una vez completada la verificación del remitente, te recomendamos el calentamiento de IP para que tus mensajes lleguen a los buzones de entrada de destino a una tasa elevada y constante. Después de completar esta configuración, asegúrate también de consultar con el equipo de incorporación de Braze para confirmar si tus dominios y tu [dirección IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) funcionan.

