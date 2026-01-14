---
nav_title: Dyspatch
article_title: Dyspatch
alias: /partners/dyspatch
description: "Este artículo de referencia describe la asociación entre Braze y Dyspatch, un creador de correos electrónicos de arrastrar y soltar que permite crear correos electrónicos atractivos, con capacidad de respuesta y atractivos sin necesidad de escribir código."
page_type: partner
search_tag: Partner

---

# Dyspatch

> [Dyspatch](https://www.dyspatch.io) ofrece un intuitivo creador de correo electrónico de arrastrar y soltar que se utiliza para crear correos electrónicos atractivos, receptivos y con interacción sin necesidad de escribir código. Colabore con su equipo para crear y aprobar correos electrónicos dentro de Dyspatch y luego expórtelos a Braze, ¡todo en unos pocos pasos! 

_Esta integración está mantenida por Dyspatch._

## Sobre la integración

La integración de Dyspatch y Braze le permite simplificar su ciclo de vida de creación de correo electrónico exportando plantillas de correo electrónico de Dyspatch directamente a Braze.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Dyspatch | Para beneficiarse de esta asociación, es necesario disponer de una [cuenta Dyspatch](https://www.dyspatch.io/login/) con un [rol de propietario o administrador](https://docs.dyspatch.io/administration/dyspatch_roles/). |
| Clave REST API de Braze | Una clave Braze REST API con permisos **Templates** completos. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

La integración de Braze y Dyspatch le permite exportar plantillas de correo electrónico de Dyspatch directamente a su biblioteca multimedia de Braze o descargar su plantilla y cargarla manualmente. 

### Paso 1: Crear la integración Braze

En el portal de administración de Dyspatch, abre el menú desplegable de tu nombre de usuario y selecciona **Integraciones**. Cree una nueva integración, seleccione **Braze** e introduzca su clave API Braze.

En el campo **Localizar exportaciones por**, puede elegir cómo desea gestionar la localización. Este campo le permite [localizar sus plantillas de correo electrónico](https://docs.dyspatch.io/localization/localizing_a_template/) y exportarlas a Braze para enviar fácilmente correos personalizados por idioma o configuración regional. 

![Plantilla de exportación Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_integration_create.png %}){: style="max-width:50%;"}

### Paso 2: Exportar plantilla a Braze

Después de completar un correo electrónico en Dyspatch, para enviar su plantilla a Braze, vea la plantilla de correo electrónico publicada y haga clic en **Descargar/Exportar** y luego en **Exportar a integración**.

Si desea cargar su plantilla manualmente, vea la plantilla de correo electrónico publicada y haga clic en **Descargar/Exportar** y, a continuación, en **Descargar HTML**. A continuación, en la sección **Plantillas y medios > Plantillas de correo electrónico** de su cuenta Braze, seleccione **Desde archivo** para cargar su plantilla.

![Plantilla de exportación Dyspatch]({% image_buster /assets/img/dyspatch/dyspatch_export.gif %})

{% alert important %}
No seleccione **CSS en línea** en la sección **Información de envío** de ninguna plantilla de correo electrónico de Dyspatch en Braze. Dyspatch se encarga de ello asegurándose de que sus mensajes de correo electrónico sean sólidos, receptivos y estén listos para ser enviados.
{% endalert %}

### Uso

Busque la plantilla Dyspatch que ha cargado en la sección **Plantillas y medios > Plantillas de correo electrónico** de su cuenta Braze. Ya puede utilizar esta plantilla de correo electrónico para empezar a enviar mensajes atractivos a sus clientes.


