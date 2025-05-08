---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "La integración de Braze y Alpaco aprovecha la sintaxis de Alpaco para crear y exportar a Braze plantillas de correo electrónico basadas en datos."
page_type: partner
search_tag: Partner

---

# Alpaco

> [Alpaco](https://alpaco.email/) es una herramienta de marketing por correo electrónico en línea que ofrece un editor de arrastrar y soltar para un nuevo nivel de control del diseño y el resultado. La integración de Braze y Alpaco te permite exportar a Braze correos electrónicos basados en datos. 

{% alert note %}
Alpaco es [totalmente compatible con las variables de Liquid](https://shopify.github.io/liquid/) y, como tal, también es totalmente compatible con cualquier variable de Liquid utilizada en tus configuraciones Braze.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| ------------| ----------- |
| Cuenta Alpaco | Se necesita una cuenta Alpaco para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave Braze REST API con permisos **Templates** completos. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Instancia de clúster | Tu [instancia de clúster]({{site.baseurl}}/api/basics/#endpoints) Braze se alinea con tu panel de Braze y tu punto final REST. <br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-03.braze.com`, tu punto final será `dashboard-03`.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

Proporciona tu clave de API REST de Braze y tu instancia de clúster al equipo de éxito del cliente de Alpaco. A continuación, el equipo configurará la integración inicial por ti.

{% alert note %}
Se trata de una configuración única y cualquier exportación que se realice en el futuro utilizará automáticamente esta clave de API.
{% endalert %}

## Exportación de envíos por correo electrónico de Alpaco a Braze

### Paso 1: Crear una plantilla de correo electrónico en Alpaco

En la plataforma Alpaco, utiliza las diferentes configuraciones y opciones para crear una plantilla que exprese la identidad de tu marca. Selecciona **Guardar** cuando estés satisfecho con tu plantilla.

![Alpaco Crear plantilla]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Paso 2: Crear un correo electrónico

Una vez creada la plantilla, navega hasta el lobby y crea un correo electrónico con la plantilla. Selecciona **Revisar** para asegurarte de que todo parece correcto.

![Alpaco - Crear correo electrónico]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Paso 3: Revisar y exportar correo electrónico a Braze

Selecciona **Exportar** y elige la integración Braze para exportar tu plantilla de correo electrónico a Braze. 

Si quieres hacer cambios en tu plantilla de correo electrónico, hazlos en Alpaco, y luego exporta de nuevo el correo electrónico a Braze. Esto actualizará el correo electrónico en Braze con tus cambios.

![Alpaco - Exportar correo electrónico]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Uso de plantillas de correo electrónico Alpaco en Braze

Encuentra tu correo electrónico de Alpaco cargado navegando a **Plantillas y medios > Plantillas de correo electrónico** en el panel de Braze. Ahora puedes utilizar esta plantilla para enviar correos electrónicos basados en datos a tus usuarios.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
