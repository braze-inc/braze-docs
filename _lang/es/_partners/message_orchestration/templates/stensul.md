---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "Este artículo de referencia describe la asociación entre Braze y Stensul, una plataforma de correo electrónico empresarial que permite crear fácilmente plantillas de correo electrónico que responden a dispositivos móviles en todos los canales."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul](https://stensul.com/) permite a los profesionales del marketing por correo electrónico crear fácilmente en Stensul mensajes de correo electrónico adaptados a los dispositivos móviles y a la marca, antes de enviarlos a Braze, en tiempo real, para la creación de campañas.

_Esta integración está mantenida por Stensul._

## Sobre la integración

La integración de Braze y Stensul le permite exportar sus correos electrónicos con formato HTML de Stensul y cargarlos como plantillas dentro de Braze.

## Requisitos previos

| Requisito | Descripción |
| ------------| ----------- |
| Cuenta Stensul | Se necesita una cuenta Stensul para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave Braze REST API con permisos **Templates** completos. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Instancia de clúster | Tu [instancia de clúster]({{site.baseurl}}/api/basics/#endpoints) Braze se alinea con tu panel de Braze y tu punto final REST.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

Proporciona tu clave de API REST de Braze y tu instancia de clúster a tu equipo de éxito del cliente de Stensul. El equipo se encargará de la integración inicial.

{% alert important %}
Esta es una configuración única y cualquier exportación en el futuro utilizará automáticamente esta clave API.
{% endalert %}

### Paso 1: Crear correo electrónico Stensul

Cree un correo electrónico Stensul en la plataforma Stensul y haga clic en **Completar**.

![Opciones de guardado de Stensul]({% image_buster /assets/img_archive/stensul_save_options.png %})

### Paso 2: Exportar plantilla a Braze
En el nuevo cuadro de diálogo que aparece en la página de finalización, seleccione **Cargar en ESP**.

![Opciones de carga de Stensul]({% image_buster /assets/img_archive/stensul_upload_options.png %})

A continuación, introduzca el **nombre de la plantilla**, el **asunto** y el **preencabezado** de su correo electrónico y seleccione **Cargar**. A continuación, recibirá una confirmación de que la carga se ha realizado correctamente y un historial de cargas anteriores del archivo, si procede.

![Éxito de carga de Stensul]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Uso

Busque la plantilla Stensul que ha cargado en la sección **Plantillas y medios > Plantillas de correo electrónico** de su cuenta Braze. Ya puede utilizar esta plantilla de correo electrónico para empezar a enviar mensajes atractivos a sus clientes.


