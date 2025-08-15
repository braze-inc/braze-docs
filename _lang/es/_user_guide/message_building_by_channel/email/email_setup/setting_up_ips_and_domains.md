---
nav_title: Configuración de IP y dominios
article_title: Configuración de IP y dominios
page_order: 0
page_type: tutorial
channel: email
description: "Este artículo le mostrará cómo configurar sus IPs y Dominios para enviar correos electrónicos a través de Braze."

---

# Configuración de IP y dominios

{% multi_lang_include video.html id="iTm3yQkJ0UU" align="right"  %}

> Este artículo le guiará a través de los requisitos y pasos necesarios para configurar sus direcciones IP y pools, así como los dominios y subdominios necesarios antes de que pueda empezar a enviar correos electrónicos con Braze.<br><br>Aunque la mayor parte del proceso de configuración la realiza Braze, hemos descrito los requisitos y materiales para esta configuración.

## Método 1: Coordinar con Braze (recomendado)

### Paso 1: Información general

Envíe la siguiente información a su representante de Braze:

* Los dominios y subdominios que elija
* El número aproximado de correos electrónicos que enviará cada mes, lo que le ayudará a determinar cuántas IP necesitará.
* Cómo prefiere asignar sus dominios de envío a su IP asignada

### Paso 2: Braze configura la información

Tras recibir tu correo electrónico, nos pondremos manos a la obra para configurar tus IP, dominios y subdominios, y grupos de IP.

### Paso 3: Añadir registros DNS

Una vez configurados sus IP, dominios, subdominios y grupos de IP, le enviaremos una lista de registros DNS. Pida a sus ingenieros y desarrolladores que añadan estos registros DNS cuando sea necesario y, una vez añadidos, informe al equipo de Braze Onboarding.

### Próximos pasos

Comprobaremos su configuración y validaremos toda la información en nuestros sistemas internos. El equipo de Braze Onboarding le avisará cuando esté listo para empezar o si hay problemas con sus registros DNS que deba tratar con su equipo de ingeniería.

## Método 2: Configuración de correo electrónico de autoservicio

Este método establecerá un dominio de envío, un dominio de seguimiento y una IP en total para una empresa. Si tienes pensado configurar más, consulta con el equipo de incorporación de Braze (método 1).

{% alert important %}
Esta función de autoservicio para configurar el correo electrónico está actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en la versión beta.<br>Si utiliza la función de configuración de correo electrónico de autoservicio, asegúrese de consultar también con el equipo Braze Onboarding.
{% endalert %}

### Requisitos previos

Para utilizar el autoservicio de configuración de correo electrónico, debe cumplir los siguientes requisitos previos:

1. Usted es un nuevo cliente en proceso de incorporación.
2. Tiene el permiso a nivel de empresa "Puede gestionar la configuración de la empresa".

### Paso 1: Comenzar la configuración

1. Vaya a **Configuración** > **Configuración de administración** en **Configuración de la empresa**. 
2. A continuación, seleccione la pestaña **Verificación del remitente**. Para ver esta pestaña, debes tener el permiso de nivel de empresa "Puede administrar configuración de empresa".
3. Haga clic en el botón **Iniciar configuración**.

### Paso 2: Añadir y verificar un dominio de envío

Un dominio de envío se utiliza en la dirección "de" al enviar un correo electrónico. Introduzca un dominio de envío y haga clic en **Enviar**. 

A continuación, añada los registros TXT y CNAME de la parte inferior de la página a su proveedor de DNS. A continuación, vuelva al panel de control de Braze y haga clic en **Verificar**.

![]({% image_buster /assets/img_archive/email_setup_rdns_records.png %})

{% alert important %}
El dominio de envío debe estar subordinado a un dominio de su propiedad. Por ejemplo, si eres propietario de "example.com", un subdominio podría ser "mail.example.com", lo que te permitiría utilizar la dirección de envío "@mail.example.com".
{% endalert %}

### Paso 3: Añadir y verificar un dominio de seguimiento

Un dominio de seguimiento se utiliza para envolver enlaces en sus correos electrónicos con fines de seguimiento de clics y de marca. Esto será visible para los usuarios cuando pasen por encima o hagan clic en los enlaces de su correo electrónico. Le recomendamos que lo haga coincidir con su dominio de envío.

Introduzca un dominio de seguimiento y haga clic en **Enviar**. A continuación, añada los registros CNAME de la parte inferior de la página a su proveedor de DNS. A continuación, vuelva al panel de control de Braze y haga clic en **Verificar**.

### Paso 4: Añadir una dirección IP

Braze generará un registro A para asociar su dirección IP con su subdominio de envío en una configuración denominada DNS inverso (rDNS). Añada el registro A en su proveedor de DNS y, a continuación, haga clic en **Configurar rDNS** para admitir la entregabilidad.

Tenga en cuenta que los dominios adicionales que se hayan añadido no aparecerán en la sección **Verificación del remitente**. Para añadir más dominios, póngase en contacto con el equipo de asistencia de Braze.

### Próximos pasos

Una vez completada la verificación del remitente, recomendamos el calentamiento de IP para que sus mensajes lleguen a las bandejas de entrada de destino con una frecuencia elevada y constante. Después de completar esta configuración, asegúrese también de consultar con el equipo Braze Onboarding para confirmar si sus dominios y [dirección IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) están funcionando.

