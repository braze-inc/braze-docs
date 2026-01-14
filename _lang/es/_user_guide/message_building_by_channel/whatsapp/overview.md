---
nav_title: Configuración de WhatsApp
article_title: Configuración de WhatsApp
alias: /partners/whatsapp/
description: "Este artículo explica cómo configurar el canal de WhatsApp de Braze, incluidos los requisitos previos y los siguientes pasos sugeridos."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
search_rank: 2
---

# Configuración de WhatsApp

> La mensajería [WhatsApp](https://www.whatsapp.com/) Business es una popular plataforma de mensajería entre pares utilizada en todo el mundo que ofrece mensajería basada en conversaciones para empresas.	

## Requisitos previos

Acepta lo siguiente antes de proceder a la integración:

- **Política de adhesión voluntaria:** WhatsApp exige a las empresas la adhesión voluntaria de los clientes a la mensajería.
- **Normas de contenido de WhatsApp:** WhatsApp tiene varias [normas de contenido](https://www.whatsapp.com/legal/commerce-policy?l=en) que hay que seguir.
- **Conformidad:** Cumplir con toda la documentación aplicable de Braze y Meta y con cualquier [política](https://www.whatsapp.com/legal/?lang=en) aplicable [de Meta](https://www.whatsapp.com/legal/?lang=en).
- **Límites de conversación de 24 horas:** Después de que una empresa envíe un mensaje inicial con una plantilla o un usuario envíe un mensaje, se abrirá una ventana de 24 horas en la que las dos partes podrán intercambiar mensajes. 
- **Iniciar la conversación:** Los usuarios pueden iniciar una conversación en cualquier momento. Una empresa sólo puede iniciar una conversación a través de una plantilla de mensajes aprobada.
<br><br>

| Requisito| Descripción|
| ---| --- |
| Cuenta Meta Business Manager | Se necesita una cuenta Meta Business para aprovechar este canal de mensajería. |
| Cuenta de WhatsApp Business | Se necesita una cuenta de WhatsApp Business para aprovechar este canal de mensajería. |
| Número de teléfono de WhatsApp | Debes adquirir un número de teléfono que cumpla los requisitos de WhatsApp para [la API en la nube](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) o [la API local](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers) para utilizar el canal de mensajería.  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Conecta WhatsApp Messenger a Braze

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y busca **WhatsApp**.

En la página del socio de WhatsApp, selecciona **Iniciar integración**.

\![Página del socio de WhatsApp con un botón para iniciar la integración.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:70%;"}

En la ventana abierta, selecciona **Siguiente** hasta que aparezca el botón **Iniciar integración**. Selecciona el botón para iniciar el proceso de integración.

Instrucciones para conectar Braze a WhatsApp.]({% image_buster /assets/img/whatsapp/instructions.png %}){: style="max-width:50%;"}

### Paso 2: Configuración de WhatsApp

A continuación, te aparecerá el flujo de trabajo de configuración de Braze. Para obtener información paso a paso, consulta el [registro integrado de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/). 

Dentro de este flujo, lo harás
1. Crea o selecciona tus cuentas Meta y WhatsApp Business. Asegúrate de revisar [las directrices sobre nombres de usuario de WhatsApp](https://www.facebook.com/business/help/757569725593362). <br><br>Es probable que ya tengas al menos una cuenta Meta Business en tu empresa. Si es así, selecciona en cuál quieres que viva tu cuenta de WhatsApp Business. Los permisos de usuario y la verificación empresarial para WhatsApp se controlarán de forma centralizada en tu cuenta Meta Business.<br><br>
2. Crea tu perfil de WhatsApp Business.
3. Verifica tu número de WhatsApp Business.<br><br>

Una vez completada la configuración, se creará un grupo de suscripción de WhatsApp específico para tus usuarios.

### Paso 3: Crear plantillas de WhatsApp

Sólo se pueden utilizar plantillas de mensajes de WhatsApp aprobadas para iniciar conversaciones con los clientes. Las plantillas de WhatsApp pueden crearse en el [Meta Administrador de Empresas](https://www.facebook.com/business/help/2055875911147364?id=2129163877102343). Para obtener una lista de las características de mensajería de WhatsApp compatibles con Braze, consulta [Características de WhatsApp compatibles]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#supported-whatsapp-features).

1. **Navega hasta el [administrador de plantillas](https://business.facebook.com/wa/manage/message-templates)**<br>
En el Meta Business Manager, en **Herramientas de cuentas**, selecciona **Plantillas de mensajes**.
A continuación, selecciona **Crear plantillas**.<br><br>\![Administrador de WhatsApp con una lista de plantillas de mensajes.]({% image_buster /assets/img/whatsapp/whatsapp2.png %}){: style="max-width:100%;"}<br><br>
2. **Configuración de la mensajería**<br>
En el nuevo creador de plantillas de mensajes, selecciona la categoría de tu mensaje, asigna un nombre a tu plantilla y elige los idiomas que deseas admitir. Puedes eliminar o añadir más idiomas más adelante.<br><br> 
	Las categorías de plantillas de mensajes disponibles son las siguientes:
	- Especialista en marketing: Envía ofertas promocionales, anuncios de productos y mucho más para aumentar el conocimiento y la interacción
	- Utilidad: Envía actualizaciones de cuentas, pedidos, alertas y mucho más para compartir información importante
	- Autentificación: Envía códigos que permitan a tus clientes acceder a sus cuentas<br><br> 
	\![Creador de plantillas de mensajes con categorías para marketing, utilidad y autenticación.]({% image_buster /assets/img/whatsapp/whatsapp3.png %}){: style="max-width:100%;"}<br><br>
3. **Editar plantilla**<br>
A continuación, crea tu plantilla de mensajes. <br><br>Puedes proporcionar una cabecera de texto o multimedia, el cuerpo del texto, un pie de mensaje y botones. Ten en cuenta que las cabeceras de video y documentación no están disponibles actualmente, y que las cabeceras deben ser de tipo texto o imagen. Cualquier medio que añadas sirve como ejemplo para el proceso de revisión y **no se** incluye en el mensaje de la plantilla. Los soportes deben añadirse en Braze. Aparecerá una vista previa de tu mensaje en un panel. <br><br>Aunque Meta no es compatible con Liquid, puedes introducir plantillas de variables que luego se pueden sustituir en Braze por variables de Liquid. Selecciona el botón **\+ Añadir variable** para hacerlo.<br><br>Compositor de plantillas.]({% image_buster /assets/img/whatsapp/whatsapp4.png %}){: style="max-width:100%;"}

Cuando hayas completado tu plantilla, pulsa **Enviar**. 

#### Tiempo de aprobación de la plantilla

Puedes comprobar el estado de aprobación de tu plantilla de mensajes en la página **Plantilla de mensajes** del Meta Business Manager, o al crear una campaña o Canvas en Braze. Además, el equipo de WhatsApp puede notificarte por correo electrónico en función de tus permisos de notificación. 

{% alert note %}
Las plantillas aprobadas pueden utilizarse en tantas campañas y lonas como quieras. También se pueden enviar a tantos usuarios de adhesión voluntaria como quieras. Esto es así a menos que disminuya la calidad de la plantilla.
{% endalert %}

### Paso 4: Crea una campaña de WhatsApp

Una vez aprobadas las plantillas de WhatsApp, puedes pasar al panel para crear un [WhatsApp Canvas o una campaña]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/). 

{% alert note %}
Una vez creada tu cuenta de WhatsApp Business, Meta determinará tu límite inicial de mensajería. Para saber más, consulta el [rendimiento]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/#throughput).
{% endalert %}

## Próximos pasos

Tras completar la integración, te recomendamos que completes los dos Metaprocesos siguientes:
- [Verificación empresarial](https://www.facebook.com/business/help/2058515294227817?id=180505742745347)
	- Es posible que ya dispongas de la verificación de empresa si has utilizado un administrador de Meta Business existente. 
- [Cuenta oficial de empresa](https://www.facebook.com/business/help/604726921052590?ref=search_new_0)

También te recomendamos que leas sobre [los números de teléfono de los usuarios]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/) y que añadas los usuarios que necesitarán acceso para crear [plantillas de](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143) mensajes [en tu organización](https://www.facebook.com/business/help/2169003770027706?id=2190812977867143).

### Almacenamiento local de la API de WhatsApp en la nube

Braze es compatible con el [almacenamiento local de la API en la nube](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/local-storage?content_id=ka6F9gESPqhQpm5) de WhatsApp. Para habilitarlo, ponte en contacto con tu administrador de asistencia al cliente de Braze.

