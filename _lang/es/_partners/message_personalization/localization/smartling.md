---
nav_title: Smartling
article_title: Smartling
description: "Este artículo de referencia describe la asociación entre Braze y Smartling, un software basado en la nube para la localización. Esta integración te permite traducir plantillas de correo electrónico y bloques de contenido en Braze."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling][2] es un software integral de gestión de la traducción en la nube para clientes que buscan automatizar la traducción de sitios web, aplicaciones y experiencias de cliente.

La integración de Braze y Smartling te permite traducir plantillas de correo electrónico y bloques de contenido. Smartling proporciona a los lingüistas la ventaja del contexto visual durante la traducción, lo que reduce los errores y mantiene la calidad.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Smartling | Se necesita una [cuenta Smartling][2] para beneficiarse de esta asociación. |
| Proyecto de traducción de Smartling | Para conectar tu cuenta Braze con Smartling, primero debes registrarte y [crear un proyecto de traducción][3]. |
| Clave REST API de Braze | Una clave Braze REST API con todos los permisos de plantillas y Bloques de contenido. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST][1]. Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

La integración Smartling con Braze te permitirá traducir plantillas de correo electrónico y bloques de contenido. 

Plantillas de correo electrónico: 
* Sólo se admiten correos electrónicos del editor HTML. 
* Cada traducción se almacenará como su propia plantilla de correo electrónico. 

Bloques de contenido: 
* Se admiten todos los bloques de contenido. 
* Los bloques de contenido contienen tanto la versión original como la traducida.
* El script de Liquid determina el idioma correcto para la visualización en función de la preferencia de idioma del destinatario.

### Paso 1: Configurar el proyecto Braze en Smartling TMS

#### Conexión de Braze a Smartling

1. En [Smartling][2], crea un tipo de proyecto [Braze Connector][6] en tu cuenta de Smartling. 
  - Asegúrate de que se añaden al proyecto todas las lenguas de destino necesarias.
2. Desde este proyecto, haz clic en **Configuración** > **Configuración Braze** > **Conectar a Braze**.
3. Introduce tu URL de la API de Braze y tu clave de API de Braze.
4. Haga clic en **Guardar**.

#### Configuración completa del conector Braze

Consulte [la documentación][3] de Smartling para obtener información detallada sobre la configuración de los conectores.

Selecciona cómo quieres la automatización de las solicitudes previas de traducción.

Configure los idiomas de origen y destino en **Configuración de idiomas**. Lo utilizará el conector para ingerir contenido en Smartling TMS y entregar traducciones a Braze.

![][8]

### Paso 2: Enviar contenido a Smartling

Una vez conectado y configurado el conector Braze, encontrarás contenido Braze en la pestaña **Braze** de tu proyecto Smartling. Consulte [la documentación][7] de Smartling para obtener más información.

Smartling ofrece funciones avanzadas para buscar y seleccionar contenidos por:
* Búsqueda por palabra clave
* Tipo de contenido Braze
* Etiquetado Braze

![][9]

### Paso 3: Añadir traducciones a Braze

A medida que se completan las traducciones en la plataforma Smartling, se envían automáticamente a Braze, sin necesidad de sincronizar manualmente el contenido entre Smartling y Braze.

[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://help.smartling.com/hc/article_attachments/13946813331739
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}