---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "Este artículo de referencia describe la asociación entre Braze y Taxi for Email, una herramienta de marketing por correo electrónico en línea que permite a los clientes de Braze crear plantillas de correo electrónico inteligentes utilizando su interfaz de arrastrar y soltar y una sintaxis sencilla pero potente."
page_type: partner
search_tag: Partner

---

# Taxi for Email

> [Taxi for Email](http://taxiforemail.com/) es una herramienta de marketing por correo electrónico en línea que ofrece un editor de arrastrar y soltar de correo electrónico visual e intuitivo. Taxi anima a los equipos a colaborar fácilmente en campañas de correo electrónico, permitiendo a redactores y editores el acceso y los recursos que necesitan para crear correos electrónicos, todo ello sin código.

_Esta integración la mantiene Taxi for Email._

## Sobre la integración

La integración de Braze y Taxi aprovecha la sencilla pero potente sintaxis de Taxi para crear y exportar plantillas de correo electrónico inteligentes a Braze. 

## Requisitos previos

| Requisito | Descripción |
| ------------| ----------- |
| Cuenta Taxi for Email | Se necesita una cuenta de Taxi for Email para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave Braze REST API con permisos **Templates** completos. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Punto final Braze | [Tu punto final Braze]({{site.baseurl}}/api/basics/#endpoints) se alinea con la URL de tu panel Braze.<br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-03.braze.com`, tu punto final será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

### Paso 1: Crear una plantilla de correo electrónico para Taxi

Crea una plantilla de Taxi en la plataforma Taxi. Una vez creada la plantilla, ve a la **Configuración de tu Organización** y selecciona la pestaña **Conectores ESP**.

### Paso 2: Crear conector Braze

1. En el cuadro de diálogo que aparece, selecciona el botón **Añadir nuevo** y, a continuación, selecciona **Braze** en el menú desplegable. 
2. Selecciona **Braze** para editar la configuración del conector Braze.
3. Introduce tu punto final Braze y tu clave de API Braze.

El campo de tu conector cambiará de color una vez que se hayan proporcionado los detalles con los permisos correctos. Si este campo no cambia, comprueba que tus campos se ajustan a los requisitos indicados.

## Uso

Encuentra tu plantilla Taxi subida en la sección **Plantillas y medios > Plantillas de correo electrónico de tu cuenta** de Braze.  Ya puedes utilizar esta plantilla de correo electrónico para empezar a enviar mensajes de interacción a tus clientes.


