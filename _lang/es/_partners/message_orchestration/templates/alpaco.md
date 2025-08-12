---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "La integración de Braze y Alpaco te permite exportar a Braze plantillas de correo electrónico y bloques de contenido compatibles con Liquid, listos para su uso en correo electrónico y mensajería dentro de la aplicación."
page_type: partner
search_tag: Partner
---

# Alpaco

> [Alpaco](https://alpaco.email/) es una herramienta de gestión creativa en línea que ofrece un editor de arrastrar y soltar para crear contenido reutilizable y seguro para Braze. La integración de Alpaco y Braze te permite exportar bloques de contenido, plantillas de correo electrónico y plantillas de mensajes dentro de la aplicación.

_Esta integración está mantenida por Alpaco._

{% alert note %}
Alpaco es [totalmente compatible con las variables de Liquid](https://shopify.github.io/liquid/) y, como tal, también es totalmente compatible con cualquier variable de Liquid utilizada en tus configuraciones Braze.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| ------------| ----------- |
| Cuenta Alpaco | Se necesita una cuenta Alpaco para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave Braze REST API con permisos **Templates** completos. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Instancia de clúster | Tu [instancia de clúster]({{site.baseurl}}/api/basics/#endpoints) Braze se alinea con tu panel de Braze y tu punto final REST. <br><br> Por ejemplo, si la URL de tu panel es `https://dashboard-03.braze.com`, tu punto final será `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Ejemplos

- Exporta **plantillas de correo electrónico** totalmente diseñadas para su uso en campañas Braze y mensajería transaccional.
- Crea y gestiona **bloques de contenido modulares** (e.g., cabeceras, pies de página, promociones) que puedan reutilizarse en varios canales.
- Diseña **mensajes** atractivos **dentro de la aplicación** con la misma flexibilidad creativa que los correos electrónicos, lo que facilita entregar experiencias coherentes y acordes con la marca en todos los canales.
- Habilita la **personalización** incluyendo etiquetas de Liquid compatibles con Braze, como `{{first_name}}` o `{{custom_attribute}}`.
- Mantén **la coherencia de la marca** centralizando el diseño creativo en Alpaco y empujando las actualizaciones a Braze con una sola exportación.

## Integración

Proporciona tu clave de API REST de Braze y tu instancia de clúster al equipo de éxito del cliente de Alpaco. A continuación, el equipo configurará la integración inicial por ti.

{% alert note %}
Se trata de una configuración única y cualquier exportación que se realice en el futuro utilizará automáticamente esta clave de API.
{% endalert %}

## Exportar mensajes de Alpaco a Braze

### Paso 1: Crear una plantilla en Alpaco

En Alpaco, crea una plantilla que exprese la identidad de tu marca. Cuando estés listo, selecciona **Guardar**.

![Alpaco Crear plantilla]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Paso 2: Redacta un mensaje utilizando la plantilla

A continuación, ve al vestíbulo de Alpaco y utiliza tu plantilla para crear un correo electrónico, un mensaje dentro de la aplicación o un bloque de contenido. Para volver a comprobar tu mensaje antes de exportarlo, selecciona **Revisar**.

![Alpaco - Crear correo electrónico]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Paso 3: Exporta tu mensaje a Braze

Selecciona **Exportar**, luego elige la integración Braze y especifica si vas a exportar una plantilla de correo electrónico o un bloque de contenido.

Si haces cambios después de la exportación, puedes volver a exportar el contenido desde Alpaco para actualizarlo en Braze.

![Alpaco - Exportar correo electrónico]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Uso de plantillas y bloques Alpaco en Braze

Dependiendo del tipo de contenido que exportes, tu plantilla aparecerá en una de las siguientes secciones:

- **Plantillas y medios > Plantillas de correo electrónico**
- **Plantillas y medios > Bloques de contenido**

Las plantillas Alpaco son ideales para las organizaciones que desean gestionar de forma centralizada la coherencia de la marca. También son compatibles con las etiquetas integradas de Braze para facilitar la categorización y la gestión de contenidos.
