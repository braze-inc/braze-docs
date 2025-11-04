---
nav_title: OneTrust
article_title: OneTrust
description: "Este artículo de referencia describe la asociación entre Braze y OneTrust, un proveedor de software de seguridad y privacidad de datos, que le permite utilizar el generador de flujos de trabajo de OneTrust para crear flujos de trabajo de seguridad para su producto."
alias: /partners/onetrust/
page_type: partner
search_tag: Partner

---

# OneTrust

> [OneTrust](https://www.onetrust.com/) es un proveedor de software de privacidad y seguridad que proporciona la visibilidad que necesita para comprender mejor su panorama de confianza, la acción para aprovechar los potentes conocimientos y la automatización para mantenerle a la altura de la competencia. 

_Esta integración está mantenida por OneTrust._

## Sobre la integración

La integración de Braze y OneTrust le permite utilizar el creador de flujos de trabajo de OneTrust para crear flujos de trabajo de seguridad para su producto.
## Requisitos previos

| Requisitos | Descripción |
|---|---|
| Cuenta OneTrust | Una cuenta [OneTrust](https://www.onetrust.com/) para aprovechar esta asociación. |
| Clave API Braze | Una clave Braze REST API con los permisos necesarios para el endpoint que utilizará su acción OneTrust.<br><br>Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Instancia de soldadura | Puedes obtener tu instancia de Braze a través de tu administrador de incorporación a Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

La siguiente integración proporciona orientación para crear un flujo de trabajo de actualización de consentimiento de usuario y un flujo de trabajo de eliminación de usuario. Para más detalles sobre los puntos finales Braze soportados adicionalmente, consulta [Otras acciones soportadas](#Other-supported-actions).

### Añadir credenciales Braze a OneTrust

En el menú **Integraciones** de OneTrust, vaya a **Credenciales** > botón **Agregar nuevo** para abrir la pantalla **Seleccionar sistema**. Aquí, busque **Braze** y haga clic en el botón **Siguiente**.

Siga las instrucciones de la pantalla **Introducir detalles de credenciales** y proporcione la siguiente información. Guarda tus credenciales cuando hayas terminado.
  - Nombre de credencial
  - Establezca el tipo de conector en **Web App**
  - Nombre de host: `<your-braze-instance-url>`
  - **Encabezado de solicitud**:
    - **Autorización**: Portador
    - **Content-Type**: application/json
  - Token: `<your-braze-api-key>`

### Añadir Braze como sistema

#### Paso 1: Crear un flujo de trabajo

{% tabs %}
{% tab Actualización del consentimiento del usuario %}
1. En el menú de integraciones de OneTrust, vaya a **Galería** > **Braze** > **Añadir** para crear un nuevo flujo de trabajo.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Proporcione un nombre y un correo electrónico de notificación en el modal del flujo de trabajo. Haga clic en el botón **Crear**. Al crearlo, accederá al Generador de flujos de trabajo. Su flujo de trabajo Braze se sembrará con llamadas a la API y acciones que pueden utilizarse para procesar solicitudes de eliminación. <br><br>
3. En el Generador de flujos de trabajo, seleccione la acción que desea activar en el flujo de trabajo.<br>![]({% image_buster /assets/img/onetrust/onetrust2.png %})

{% endtab %}
{% tab Eliminación de usuarios %}

1. En el menú de integraciones de OneTrust, vaya a **Galería** > **Braze** > **Añadir** para crear un nuevo flujo de trabajo.![]({% image_buster /assets/img/onetrust/onetrust.png %})<br><br>
2. Proporcione un nombre y un correo electrónico de notificación en el modal del flujo de trabajo. Haga clic en el botón **Crear**. Al crearlo, accederá al Generador de flujos de trabajo. Su flujo de trabajo Braze se sembrará con llamadas a la API y acciones que pueden utilizarse para procesar solicitudes de eliminación. <br><br>
3. En el Generador de flujos de trabajo, seleccione la acción que desea activar en el flujo de trabajo.<br>![]({% image_buster /assets/img/onetrust/onetrust8.png %})
{% endtab %}
{% endtabs %}

#### Paso 2: Seleccionar acción
{% tabs %}
{% tab Actualización del consentimiento del usuario %}

1. Cuando haya terminado, haga clic en **Listo** y seleccione **Añadir acción**. Tenga en cuenta que la acción que elija dependerá del tipo de preferencia que se esté actualizando y de su punto final preferido.
- Para actualizar las preferencias globales de suscripción de un usuario, seleccione la acción **POST Seguimiento de usuario - atributos**.
- Para actualizar las preferencias del grupo de suscripción de un usuario, seleccione la acción **POST Seguimiento de usuarios - Atributos** o la acción **POST Establecer estado del grupo de suscripción de usuarios**.<br>![]({% image_buster /assets/img/onetrust/onetrust4.png %})<br><br>
2. Elija la Acción deseada, seleccione sus credenciales Braze previamente creadas y haga clic en **Siguiente**.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% tab Eliminación de usuarios %}

1. Cuando haya terminado, haga clic en **Listo** y seleccione **Añadir acción**.
- Para eliminar un usuario de Braze, seleccione la acción **POST User Delete Action**.
<br>![]({% image_buster /assets/img/onetrust/onetrust9.png %})<br><br>
2. Elija la Acción deseada, seleccione sus credenciales Braze previamente creadas y haga clic en **Siguiente**.<br>![]({% image_buster /assets/img/onetrust/onetrust5.png %})

{% endtab %}
{% endtabs %}
#### Paso 3: Actualizar el cuerpo de la solicitud
{% tabs %}
{% tab Actualización del consentimiento del usuario %}

1. Actualice el cuerpo para incluir los valores dinámicos necesarios. Asegúrate de que el cuerpo de la acción coincide con el [punto final`/users/track` ](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/) y con el [punto final`/subscription/status/set` ](https://www.braze.com/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).
2. Personalice el flujo de trabajo con parámetros adicionales o lógica condicional para satisfacer las necesidades de su organización.
3. Cuando termine de editar, haga clic en **Finalizar** y luego en **Activar** para habilitar el flujo de trabajo.

{% alert note %}
Al utilizar los flujos de trabajo de OneTrust para actualizar las preferencias del grupo de suscripción en Braze, `subscription_group_id` debe coincidir con el ID establecido por Braze cuando se creó el grupo de suscripción. Puede acceder a la página `subscription_group_id` de un grupo de suscripción accediendo a la página **Grupo de suscripción** en el panel de control de Braze.
{% endalert %}

![]({% image_buster /assets/img/onetrust/onetrust6.png %})

{% endtab %}
{% tab Eliminación de usuarios %}

1. Actualice el cuerpo para incluir los valores dinámicos necesarios. Asegúrese de que el cuerpo de la acción coincide con el [punto final`/users/delete` ]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/).
2. Cuando termine de editar, seleccione **Finalizar** y luego **Activar** para habilitar el flujo de trabajo.

![]({% image_buster /assets/img/onetrust/onetrust10.png %})

#### Actualizar el flujo de trabajo de solicitud del interesado
1. En el menú **Automatización de derechos de privacidad**, seleccione **Flujos de trabajo**. 
2. Seleccione el flujo de trabajo que desea actualizar con la integración Braze. 
3. Seleccione el botón **Editar** para habilitar la edición.
4. A continuación, seleccione el paso del flujo de trabajo al que desea añadir la integración Braze y haga clic en **Añadir conexión**.
5. Añada el flujo de trabajo Braze creado anteriormente como una subtarea del sistema.

{% endtab %}
{% endtabs %}

## Otras acciones apoyadas

Además de las acciones **POST Seguimiento de usuario - Atributos**, **POST Establecer estado de grupo de suscripción de usuarios** y **POST Eliminar usuario**, Braze admite otros puntos finales que pueden utilizarse para crear flujos de trabajo personalizados y utilizarse como subtareas dentro de flujos de trabajo existentes. 

Para ver la lista completa de acciones admitidas:
1. En OneTrust, haga clic en **Sistemas** en el menú **Integraciones**. 
2. Elija el sistema **Braze**.
3. Vaya a la pestaña **Acciones**.

![]({% image_buster /assets/img/onetrust/onetrust7.png %})


