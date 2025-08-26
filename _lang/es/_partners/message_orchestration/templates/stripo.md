---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "Este artículo de referencia describe la asociación entre Braze y Stripo, un creador de plantillas de correo electrónico de arrastrar y soltar que te permite crear fácilmente sofisticados correos electrónicos con elementos interactivos."
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo](https://stripo.email/) es un creador de plantillas de correo electrónico de arrastrar y soltar que te ayuda a crear y diseñar correos electrónicos receptivos con elementos interactivos. Los usuarios de Stripo también pueden editar en HTML y decidir qué elementos mostrar u ocultar en los distintos dispositivos a través del editor de Stripo.

_Esta integración está mantenida por Stripo._

## Sobre la integración

La integración de Braze y Stripo te permite exportar tus correos electrónicos personalizados de Stripo y cargarlos como plantillas dentro de Braze.

## Requisitos previos

| Requisito | Descripción |
| ------------| ----------- |
| Cuenta Stripo | Se requiere una cuenta Stripo para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave Braze REST API con permisos **Templates** completos. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Instancia de clúster | Tu [instancia de clúster]({{site.baseurl}}/api/basics/#endpoints) Braze se alinea con tu panel de Braze y tu punto final REST.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

### Paso 1: Crear correo electrónico Stripo

Crea un correo electrónico Stripo en la plataforma Stripo y haz clic en **Exportar**. 

![Stripo Export]({% image_buster /assets/img_archive/stripo_export.png %})

### Paso 2: Exportar plantilla a Braze

En el cuadro de diálogo que aparece, selecciona **Braze** como método de exportación 

A continuación, introduce el **nombre de tu cuenta** (como el nombre del espacio de trabajo), la **clave de API** y tu **instancia de clúster**.

![Stripo Form]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
Se trata de una configuración única, y cualquier exportación en el futuro utilizará automáticamente esta clave de API.
{% endalert %}

## Uso

Encuentra tu plantilla Stripo cargada en la sección **Plantillas y medios > Plantillas de correo electrónico** de tu cuenta Braze. Ya puedes utilizar esta plantilla de correo electrónico para empezar a enviar mensajes de interacción a tus clientes.


