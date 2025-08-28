---
nav_title: Configuración de WhatsApp
article_title: Configuración de WhatsApp
alias: /partners/whatsapp/
description: "En este artículo se explica cómo configurar el canal de WhatsApp de Braze, incluidos los requisitos previos y los pasos siguientes sugeridos."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
search_rank: 2
---

# Configuración de WhatsApp

> La mensajería [WhatsApp](https://www.whatsapp.com/) Business es una popular plataforma de mensajería peer-to-peer utilizada en todo el mundo que ofrece mensajería basada en conversaciones para empresas.	

## Requisitos previos

Acepte lo siguiente antes de proceder a la integración:

- **Política de inclusión voluntaria:** WhatsApp exige a las empresas que los clientes opten por recibir mensajes.
- **Normas de contenido de WhatsApp:** WhatsApp tiene varias [normas de contenido](https://www.whatsapp.com/legal/commerce-policy?l=en) que hay que seguir.
- **Conformidad:** Cumplir con toda la documentación aplicable de Braze y Meta y con cualquier [política aplicable de Meta](https://www.whatsapp.com/legal/?lang=en).
- **Límites de conversación de 24 horas:** Después de que una empresa envíe un mensaje inicial planificado o un usuario envíe un mensaje, se abrirá una ventana de 24 horas en la que las dos partes podrán intercambiar mensajes. 
- **Iniciar la conversación:** Los usuarios pueden iniciar una conversación en cualquier momento. Una empresa sólo puede iniciar una conversación a través de una plantilla de mensajes aprobada.
<br><br>

| Requisito| Descripción|
| ---| --- |
| Cuenta de administrador Meta Business | Se requiere una cuenta Meta Business para aprovechar este canal de mensajería. |
| Cuenta de WhatsApp Business | Para aprovechar este canal de mensajería es necesario disponer de una cuenta de WhatsApp Business. |
| Número de teléfono de WhatsApp | Debe adquirir un número de teléfono que cumpla los requisitos de WhatsApp para [la API en la nube](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) o [la API local](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) para utilizar el canal de mensajería.  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Conecta WhatsApp Messenger a Braze

En Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y busque **WhatsApp**.

En la página de socios de WhatsApp, seleccione **Iniciar integración**.

![Página del socio de WhatsApp con un botón para iniciar la integración.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

En la ventana abierta, seleccione **Siguiente** hasta que aparezca el botón **Iniciar integración**. Seleccione el botón para iniciar el proceso de integración.

![Instrucciones para conectar Braze a WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Paso 2: Configuración de WhatsApp

A continuación, aparecerá el flujo de trabajo de configuración de Braze. Para obtener información paso a paso, consulta el [registro integrado de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/). 

Dentro de este flujo, harás lo siguiente:
1. Crea o selecciona tus cuentas Meta y WhatsApp Business. Asegúrate de revisar [las directrices sobre nombres de usuario de WhatsApp](https://www.facebook.com/business/help/757569725593362). <br><br>Es probable que ya tengas al menos una cuenta Meta Business en tu empresa. Si ese es el caso, selecciona la que quieras que contenga tu cuenta de WhatsApp Business. Los permisos de usuario y la verificación empresarial para WhatsApp se controlarán de forma centralizada en tu cuenta Meta Business.<br><br>
2. Crea tu perfil de WhatsApp Business.
3. Verifica tu número de WhatsApp Business.<br><br>

Una vez finalizada la configuración, se creará un grupo de suscripción de WhatsApp específico para sus usuarios.

### Paso 3: Crear plantillas de WhatsApp

Solo se pueden utilizar plantillas de mensajes de WhatsApp aprobadas para iniciar conversaciones con los clientes. Las plantillas de WhatsApp pueden crearse en el [Meta Business Manager](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343). Para obtener una lista de las características de mensajería de WhatsApp compatibles con Braze, consulta [Características de WhatsApp compatibles]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features).

1. **Vaya al [gestor de plantillas](https://business.facebook.com/wa/manage/message-templates)**<br>
En el Meta Business Manager, en **Herramientas de la cuenta**, seleccione **Plantillas de mensajes**.
A continuación, seleccione **Crear plantillas**.<br><br>![]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Configuración de la mensajería**<br>
En el nuevo compositor de plantillas de mensajes, seleccione la categoría de su mensaje, nombre su plantilla y elija los idiomas que desea admitir. Puede eliminar o añadir más idiomas más adelante.<br><br> 
	Las categorías de plantillas de mensajes disponibles son las siguientes:
	- Marketing: Envíe ofertas promocionales, anuncios de productos y mucho más para aumentar la concienciación y el compromiso.
	- Utilidad: Envíe actualizaciones de cuentas, pedidos, alertas y mucho más para compartir información importante
	- Autentificación: Envíe códigos que permitan a sus clientes acceder a sus cuentas<br><br> 
	![]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Editar plantilla**<br>
A continuación, se le pedirá que cree su plantilla de mensaje. <br><br>Aquí puede incluir un encabezado de texto o multimedia, el cuerpo del texto, un pie de mensaje y botones. Tenga en cuenta que las cabeceras de vídeo y de documento no están disponibles actualmente, y que las cabeceras deben ser de tipo texto o imagen. A la derecha aparecerá una vista previa de tu mensaje. <br><br>Aunque Meta no es compatible con Liquid, se pueden introducir variables en la plantilla que luego se pueden sustituir en Braze por variables de Liquid. Seleccione el botón **\+ Añadir variable** para hacerlo.<br><br>![]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}<br><br>Cuando hayas completado tu plantilla, pulsa **Enviar**. 

#### Tiempo de aprobación de la plantilla

Puede comprobar el estado de aprobación de su plantilla de mensaje en la página **Plantilla de mensaje** en el Meta Business Manager, o al crear una campaña o Canvas en Braze. Además, el equipo de WhatsApp puede enviarte notificaciones por correo electrónico en función de tus permisos de notificación. 

{% alert note %}
Las plantillas aprobadas pueden utilizarse en tantas campañas y lienzos como desee. También se pueden enviar a tantos usuarios de adhesión voluntaria como quieras. Esto es así a menos que disminuya la calidad de la plantilla.
{% endalert %}

### Paso 4: Crear una campaña de WhatsApp

Una vez aprobadas las plantillas de WhatsApp, puedes ir al panel de control para crear un [lienzo o una campaña de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/). 

{% alert note %}
Una vez creada tu cuenta de WhatsApp Business, Meta determinará tu límite de mensajería inicial. Para saber más, consulta el [rendimiento]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput).
{% endalert %}

## Próximos pasos

Tras completar la integración, te recomendamos que completes los dos procesos Meta siguientes:
- [Verificación de empresas](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Es posible que ya dispongas de una verificación empresarial si has utilizado un Meta Business Manager existente. 
- [Cuenta oficial de empresa](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

También recomendamos leer acerca de [los números de teléfono de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) y añadir los usuarios que necesitarán acceso para crear [plantillas de mensajes en su organización](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143).

### Almacenamiento local de la API de WhatsApp Cloud

Braze es compatible con [el almacenamiento local de la API en la nube](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) de WhatsApp. Para activarlo, póngase en contacto con el servicio de atención al cliente de Braze.

