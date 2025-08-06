---
nav_title: Smartling
article_title: Smartling
description: "Este artículo de referencia describe la asociación entre Braze y Smartling, un software basado en la nube para la localización. El conector Braze admite la traducción de plantillas de correo electrónico HTML, bloques de contenido, lienzos y mensajes de correo electrónico de campaña."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> 



## Sobre la integración

El conector Braze admite la traducción de plantillas de correo electrónico HTML, bloques de contenido, lienzos y mensajes de correo electrónico de campaña. Las traducciones se solicitan a Smartling, y el contenido traducido se envía automáticamente a Braze.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Smartling |  |
| Proyecto de traducción de Smartling |  |
| Clave REST API de Braze | Una clave Braze REST API con todos los permisos de plantillas y Bloques de contenido. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze |  Tu punto final dependerá de la URL Braze de tu instancia. |
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
* 

## Integración

### Paso 1: Configurar el proyecto Braze en Smartling TMS

#### Conexión de Braze a Smartling

1. 
  - Asegúrate de que se añaden al proyecto todas las lenguas de destino necesarias.
2. En este proyecto, selecciona **Configuración** > **Configuración de Braze** > **Conectar a Braze**.
3. Introduce tu URL de la API de Braze y tu clave de API de Braze.
4. Seleccione **Guardar**.

#### Configuración completa del conector Braze



1. Selecciona cómo quieres la automatización de las solicitudes previas de traducción.
2. Configure los idiomas de origen y destino en **Configuración de idiomas**. El conector lo utilizará para ingerir contenido en Smartling TMS y entregar traducciones a Braze.



### Paso 2: Enviar contenido a Smartling

Una vez conectado y configurado el conector Braze, encontrarás contenido Braze en la pestaña **Braze** de tu proyecto Smartling. 

Smartling ofrece funciones avanzadas para buscar y seleccionar contenidos por:

* Búsqueda por palabra clave
* Tipo de contenido Braze
* Etiquetado Braze



### Paso 3: Añadir traducciones a Braze

A medida que se completan las traducciones en la plataforma Smartling, se envían automáticamente a Braze, sin necesidad de sincronizar manualmente el contenido entre Smartling y Braze.


