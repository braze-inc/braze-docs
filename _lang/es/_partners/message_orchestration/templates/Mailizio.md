---
nav_title: Mailizio
article_title: Mailizio
alias: /partners/mailizio
description: "Este artículo de referencia describe la asociación entre Braze y Mailizio, una plataforma de creación y gestión de correo electrónico que te permite diseñar contenido reutilizable y seguro para tu marca y exportarlo a Braze."
page_type: partner
search_tag: Partner

---

# Mailizio

> [Mailizio](https://mailizio.com/) es una plataforma de creación y gestión de correo electrónico que facilita el diseño de contenidos reutilizables y seguros para la marca mediante un editor visual intuitivo. Con la integración de Mailizio en Braze, puedes exportar tus bloques de contenido y plantillas de correo electrónico y, a continuación, generar automáticamente mensajes dentro de la aplicación a partir de esos mismos activos, habilitando un despliegue de campaña rápido y totalmente controlado.

_Esta integración está mantenida por Mailizio._

## Sobre la integración

La integración de Mailizio y Braze te permite diseñar plantillas de correo electrónico dinámicas utilizando el editor de Mailizio, aprovechar las variables de Liquid utilizadas en tus configuraciones de Braze, y empujarlas a Braze para una ejecución de campaña optimizada.

## Ejemplos

- Push plantillas de correo electrónico listas para enviar directamente a Braze para campañas y mensajes transaccionales.
- Construye módulos de contenido reutilizables (cabeceras, pies de página, promociones, etc.) para agilizar la producción en múltiples campañas y canales.
- Genera mensajes dentro de la aplicación a partir de correos electrónicos: Mailizio identifica las secciones relevantes de tu correo electrónico y te permite exportar el HTML para utilizarlo en tus campañas dentro de la aplicación.
- Personaliza a escala con variables Liquid compatibles con Braze, tanto en correos electrónicos como en mensajes dentro de la aplicación.
- Mantén la coherencia de tu marca gestionando los activos creativos en Mailizio y actualizándolos en Braze con una sola exportación.

## Requisitos previos

| Requisito | Descripción |                          
| ----------- | ----------- |  
| Cuenta Mailizio | Se necesita una cuenta Mailizio para beneficiarse de esta asociación. |  
| Clave de API REST de Braze | Una clave Braze REST API con permisos **Templates** completos.<br><br>Puedes crear una clave de API REST Braze en el panel Braze desde **Configuración** > Claves de API. |  
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final depende de la URL Braze de tu instancia. |  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

Proporciona tu clave de API REST de Braze y tu instancia de clúster a tu administrador del éxito del cliente de Mailizio. A continuación, el equipo de Mailizio configura la integración inicial por ti.

{% alert important %}
Se trata de una configuración única, y cualquier exportación en el futuro utilizará automáticamente esta clave de API.
{% endalert %}

### Paso 1: Crear un correo electrónico en Mailizio

En Mailizio, utiliza el editor de arrastrar y soltar para crear un correo electrónico que refleje la identidad de tu marca, y luego haz clic en **Guardar** para conservar tu trabajo.

![captura de pantalla del editor de arrastrar y soltar]({% image_buster /assets/img/mailizio/screenshot_1.png %})

### Paso 2: Exporta tu plantilla de correo electrónico a Braze

Cuando estés listo, haz clic en **Exportar boletín**. En la ventana emergente, selecciona **Braze-correo electrónico** y confirma la exportación.

Si actualizas tu contenido más tarde, vuelve a exportarlo desde Mailizio para actualizarlo en Braze.

![exportar captura de pantalla modal]({% image_buster /assets/img/mailizio/screenshot_2.png %})

{% alert important %}  
Puedes crear y exportar bloques de contenido del mismo modo utilizando el editor de **módulos** de Mailizio.  
{% endalert %}

## Uso

Encuentra tu plantilla Mailizio cargada en la sección **Plantillas** de tu cuenta Braze ** & Medios > Plantillas de correo electrónico**. Ya puede utilizar esta plantilla de correo electrónico para empezar a enviar mensajes atractivos a sus clientes.
