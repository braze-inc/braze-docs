---
nav_title: Smartling
article_title: Smartling
description: "Este artículo de referencia describe la asociación entre Braze y Smartling, un software basado en la nube para la localización. El conector Braze admite la traducción de plantillas de correo electrónico HTML, bloques de contenido, lienzos y mensajes de correo electrónico de campaña."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) es un software integral de gestión de la traducción en la nube para clientes que buscan automatizar la traducción de sitios web, aplicaciones y experiencias de cliente.

_Esta integración está mantenida por Smartling._

## Sobre la integración

El conector Braze admite la traducción de plantillas de correo electrónico HTML, bloques de contenido, lienzos y mensajes de correo electrónico de campaña. Las traducciones se solicitan a Smartling, y el contenido traducido se envía automáticamente a Braze.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Smartling | Se necesita una [cuenta Smartling](https://dashboard.smartling.com/) para beneficiarse de esta asociación. |
| Proyecto de traducción de Smartling | Para conectar tu cuenta Braze con Smartling, primero debes registrarte y [crear un proyecto de traducción](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Clave REST API de Braze | Una clave Braze REST API con todos los permisos de plantillas y Bloques de contenido. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La integración Smartling Braze te permite traducir plantillas de correo electrónico HTML, bloques de contenido, lienzos y mensajes de correo electrónico de campaña. Ten en cuenta los siguientes detalles en función de lo que estés traduciendo:

**Plantillas de correo electrónico**
* Sólo se admiten plantillas de correo electrónico HTML.
* Tendrás que decidir cómo el conector entregará a Braze tus correos electrónicos traducidos:
  * **Un correo electrónico para todas las lenguas:** El conector entrega todos los idiomas en el mismo correo electrónico que la fuente.
  * **Un correo electrónico por idioma:** El conector crea un nuevo correo electrónico para cada idioma en Braze.

**Bloques de contenido**
* Se admiten todos los bloques de contenido.
* Los bloques de contenido contienen tanto la versión original como la traducida.
* El script de Liquid determina el idioma correcto para la visualización en función de la preferencia de idioma del destinatario.

**Campañas y Canvas**
* Asegúrate de que has añadido tus idiomas de destino en **Configuración de soporte multilingüe** de Braze.
* Consulte la [documentación de Smartling](https://help.smartling.com/hc/en-us/articles/13248549217435) para obtener información detallada sobre la configuración de los conectores.

## Integración

### Paso 1: Configurar el proyecto Braze en Smartling TMS

#### Conexión de Braze a Smartling

1. En [Smartling](https://dashboard.smartling.com/), crea un tipo de proyecto [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093) en tu cuenta de Smartling.
  - Asegúrate de que se añaden al proyecto todas las lenguas de destino necesarias.
2. En este proyecto, selecciona **Configuración** > **Configuración de Braze** > **Conectar a Braze**.
3. Introduce tu URL de la API de Braze y tu clave de API de Braze.
4. Seleccione **Guardar**.

#### Configuración completa del conector Braze

Consulte [la documentación](https://help.smartling.com/hc/en-us/articles/13248549217435) de Smartling para obtener información detallada sobre la configuración de los conectores.

1. Selecciona cómo quieres la automatización de las solicitudes previas de traducción.
2. Configure los idiomas de origen y destino en **Configuración de idiomas**. El conector lo utilizará para ingerir contenido en Smartling TMS y entregar traducciones a Braze.

![Configuración del idioma del conector.]({% image_buster /assets/img/smartling/smartling-braze-settings.png %})

### Paso 2: Enviar contenido a Smartling

Una vez conectado y configurado el conector Braze, encontrarás contenido Braze en la pestaña **Braze** de tu proyecto Smartling. Consulte [la documentación](https://help.smartling.com/hc/en-us/articles/13248577069979) de Smartling para obtener más información.

Smartling ofrece funciones avanzadas para buscar y seleccionar contenidos por:

* Búsqueda por palabra clave
* Tipo de contenido Braze
* Etiquetado Braze

![Lista de bloques de contenido.]({% image_buster /assets/img/smartling/smartling-content-blocks-list.png %})

### Paso 3: Añadir traducciones a Braze

A medida que se completan las traducciones en la plataforma Smartling, se envían automáticamente a Braze, sin necesidad de sincronizar manualmente el contenido entre Smartling y Braze.


