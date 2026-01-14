---
title: Ketch
nav_title: Ketch
description: "Este artículo de referencia cubre la integración de Braze y Ketch. Ketch proporciona operaciones de privacidad simplificadas y un control de datos completo y dinámico, así como inteligencia."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com) permite a las empresas ser administradoras responsables de sus datos. Ketch proporciona operaciones de privacidad simplificadas y un control y una inteligencia de datos completos y dinámicos. 

_Esta integración está mantenida por Ketch._

## Sobre la integración

La integración de Braze y Ketch permite controlar las preferencias de comunicación de los clientes en el centro de preferencias de Ketch y propagar automáticamente estos cambios a Braze. 

{% alert note %}
¿Busca orientación para crear grupos de suscripción? Consulta nuestros artículos sobre <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>grupos de suscripción por SMS</a> y <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>grupos de suscripción por correo electrónico</a>.
{% endalert %}

## Requisitos previos

| Requisitos | Descripción |
|---|---|
| Cuenta Ketch | Se requiere una cuenta [Ketch](https://www.ketch.com) con privilegios de administrador para activar esta integración. |
| Clave API Braze | Una clave de API REST de Braze con permisos `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe`, y `email.blacklist`. <br><br> Se puede crear en el panel de Braze**(Consola para desarrolladores** > **Clave de API REST** > **Crear nueva clave de API**). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Establecer la conexión Braze

1. En su [instancia de Ketch](https://app.ketch.com), vaya a **Sistemas de datos** y seleccione **Braze**. A continuación, haga clic en **Nueva conexión**.
2. Dé a su conexión Braze un nombre identificable, que se utilizará para referirse a esta conexión en los procesos basados en API. Tenga en cuenta que también se creará un código para esa conexión. Este código debe ser único para todas las conexiones.
3. Confirme la asignación de identidad de sus usuarios. Por defecto, Ketch asignará las identidades de los usuarios por su dirección de correo electrónico o por `external_id` en Braze.
4. Añade la clave de API de Braze y proporciona el punto final de la API. Tenga en cuenta que este [punto final de la API]({{site.baseurl}}/api/basics/#endpoints) depende de la instancia de Braze que utilice su organización.

### Paso 2: Configurar las preferencias de suscripción

1. Vaya a **Centro de políticas > Suscripciones**. Si no ve la pestaña de suscripciones en **el Centro de políticas**, asegúrese de que tiene acceso al centro de preferencias de marketing y compruebe que dispone de los permisos de cuenta correctos para acceder a esta parte del producto.
2. Haga clic en **Crear nueva suscripción** para crear un nuevo tema. Cada abono tendrá un nombre y un código.
3. Añada los canales para enviar sus temas de suscripción. Cada canal se mostrará en el centro de preferencias de marketing para sus usuarios. También puede añadir los detalles de cómo desea que el centro de preferencias de Ketch orqueste una determinada señal de inclusión o exclusión.
4. Seleccione la conexión Braze que desea utilizar para orquestar las señales de inclusión y exclusión.
5. Introduzca la dirección Braze `subscription_group_id` para el grupo de suscripción al que desea enviar las preferencias de usuario de Ketch.

![ID del grupo de suscripción Braze.]({% image_buster /assets/img/ketch/ketch1.png %})

{% alert note %}
Para recoger y orquestar las señales de opt-in y opt-out de los usuarios, las identidades deben estar correctamente configuradas. Ketch recomienda configurar el correo electrónico como identificador para orquestar las señales de preferencia del usuario para esta integración.
{% endalert %}


### Paso 3: Configurar identidades

Un usuario sólo puede ver el centro de preferencias de marketing cuando Ketch puede confirmar la identidad de preferencias de marketing de ese usuario. Si Ketch no puede capturar correctamente la identidad del usuario, la página de preferencias de marketing no se mostrará a dicho usuario, ya que Ketch no podrá gestionar sus preferencias de usuario.

1. Para configurar la identidad de preferencias de marketing, vaya a la página **Configuración** en Ketch y haga clic en **Espacio de identidad**. Deberá crear un nuevo espacio de identidad o editar un espacio de identidad existente para asignar ese espacio de identidad como identidad de preferencia de marketing. Compruebe que la etiqueta Ketch desplegada en la propiedad captura correctamente ese espacio de identidad.
2. Vaya a **Experience Server** > **Propiedades**, y edite la propiedad deseada. En la capa de datos de esa propiedad, asegúrese de activar el espacio de identidad personalizado. A continuación, configure cómo se captura la identidad de preferencia de marketing en este sitio.
3. Una vez configurado el espacio de identidad, comprueba si aparece el centro de preferencias abriéndolo en el sitio web en el que se ha desplegado la etiqueta Ketch.


