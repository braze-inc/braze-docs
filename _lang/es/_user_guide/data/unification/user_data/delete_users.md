---
nav_title: Eliminar usuarios
article_title: Eliminar usuarios
page_order: 4.2
toc_headers: h2
description: "Aprende a eliminar un usuario individual o un segmento de usuarios directamente a través del panel de Braze." 
---

# Eliminar usuarios

> Aprende a eliminar un usuario individual o un segmento de usuarios directamente a través del panel de Braze.

{% alert important %}
Esta característica está actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar.
{% endalert %}

## Requisitos previos

Para eliminar usuarios, necesitarás ser administrador o tener permisos de **Eliminar usuario**.

## Acerca de la eliminación de usuarios

La eliminación de usuarios te permite gestionar tu base de datos eliminando perfiles que ya no son necesarios, que se crearon por error o que deben eliminarse por motivos de cumplimiento (como el RGPD o la CCPA).

| Consideración | Detalles |
|---------------|---------|
| Tamaño máximo | Puedes eliminar hasta 100 millones de perfiles de usuario al borrar un segmento. |
| Período de espera | Todas las supresiones de segmentos requieren un periodo de espera de 7 días más el tiempo que se tarde en procesar las supresiones. |
| Límites del trabajo | Sólo se puede eliminar un segmento a la vez, lo que incluye el periodo de espera de 7 días. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Eliminar usuarios

Puedes eliminar un [usuario individual](#delete-individual) o un [segmento de usuarios](#delete-segment) a través del panel Braze:

### Borrar un individuo {#delete-individual}

Para eliminar un usuario individual de Braze, ve a **Audiencia** > **Buscar usuarios** y, a continuación, busca y selecciona un usuario. Si vas a eliminar un perfil de usuario duplicado, comprueba que has seleccionado el correcto.

La página "Buscar usuarios" en Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Los borrados de un solo usuario son permanentes: los perfiles no pueden recuperarse después de ser borrados.  
{% endalert %}

En su página de perfil, selecciona <i class="fa-solid fa-ellipsis-vertical"></i> **Mostrar opciones** > **Eliminar usuario**. Ten en cuenta que la eliminación completa del usuario en Braze puede tardar unos minutos.

Un usuario en Braze con el menú de elipses verticales abierto, mostrando la opción de eliminar al usuario.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Borrar un segmento {#delete-segment}

Si aún no lo has hecho, [crea un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) que contenga los perfiles de usuario que quieras eliminar. Asegúrate de incluir todos los perfiles de usuario si vas a eliminar usuarios duplicados.

En Braze, ve a **Audiencia** > **Gestionar audiencia** y, a continuación, selecciona la pestaña **Eliminar usuarios**.

La pestaña "Eliminar usuarios" de la sección "Gestionar audiencia" del panel de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Selecciona **Eliminar usuarios**, elige el segmento que quieras eliminar y, a continuación, selecciona **Siguiente**.

\![Una ventana emergente con un segmento elegido para borrar.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Escribe **ELIMINAR** para confirmar tu solicitud y, a continuación, selecciona **Eliminar usuarios**.

\![La página de confirmación con "ELIMINAR" escrito en la casilla de confirmación.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Los usuarios de este segmento no se eliminarán inmediatamente. En su lugar, se marcarán como pendientes de eliminación durante los próximos 7 días. Transcurrido este tiempo, se eliminarán y te enviaremos un correo electrónico para comunicártelo.

{% alert tip %}
Para garantizar que estos usuarios exactos se eliminan independientemente de los cambios de segmento, se crea automáticamente un filtro de segmento llamado **Eliminación pendiente**. Puedes [utilizar este filtro]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) para comprobar el estado de las eliminaciones pendientes.
{% endalert %}

## Cancelación de la eliminación de segmentos {#cancel}

Tienes 7 días para cancelar las eliminaciones de segmentos pendientes. Para cancelarlo, ve a **Audiencia** > **Gestionar audiencia** y, a continuación, selecciona la pestaña **Eliminar usuarios**.

La pestaña "Eliminar usuarios" de la sección "Gestionar audiencia" del panel de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Junto a un segmento pendiente de borrar, selecciona <i class="fa-solid fa-eye"></i> para abrir los detalles del registro de borrado.

\![Un segmento pendiente de eliminar en la pestaña "Eliminar usuarios".]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

En los detalles del registro de borrado, selecciona **Cancelar borrado**.

\![La ventana "Detalles del registro de eliminación" en la pestaña "Eliminar usuarios".]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Cuando la eliminación masiva de usuarios está en curso, puedes cancelarla en cualquier momento. Sin embargo, los usuarios ya eliminados antes de la cancelación no podrán ser restaurados.
{% endalert %}

## Comprobación del estado de borrado {#status}

Puedes comprobar el estado de una eliminación utilizando [los filtros de segmento](#segment-filters), la página de [administrar audiencia](#manage-audience) o [los informes de eventos de seguridad](#security-event-report).

### Filtros de segmento

Cuando solicitas que se elimine un segmento de usuarios, se crea automáticamente un [filtro de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) llamado **Pendiente de eliminación**. Puedes utilizarlo para:

- Ver el conjunto exacto de usuarios vinculados a una fecha concreta de ejecución de borrado.
- Excluye a esos usuarios de las campañas para que no reciban mensajes antes de la eliminación.
- Exporta la lista si la necesitas para cumplir la normativa o llevar un registro.

### Administrar la audiencia

{% alert note %}
Para obtener la lista de usuarios exactos que serán eliminados, utiliza en su lugar el [filtro de segmentos Pendiente de eliminación](#segment-filters).
{% endalert %}

Ve a **Audiencia** > **Gestionar audiencia** y, a continuación, selecciona la pestaña **Eliminar usuarios**.

La pestaña "Eliminar usuarios" de la sección "Gestionar audiencia" del panel de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

En esta página, puedes encontrar la siguiente información general para todas las eliminaciones actuales y pendientes:

| Campo | Descripción |
|-------|-------------|
| Fecha de solicitud | La fecha en que se hizo la solicitud originalmente. Utilízalo con el filtro **Pendientes** de eliminación para obtener la lista de perfiles pendientes de eliminación. |
| Solicitante | El usuario que inició la solicitud de eliminación. |
| Nombre del segmento | El nombre del segmento utilizado para seleccionar a los usuarios pendientes de eliminación. |
| Estado | Muestra si la solicitud de borrado está pendiente, en curso o completada. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para más detalles sobre una solicitud concreta, selecciona <i class="fa-solid fa-eye"></i> para mostrar los detalles del registro de borrado. Aquí también puedes [cancelar las eliminaciones de segmentos pendientes](#cancel).

\![Un segmento pendiente de eliminar en la pestaña "Eliminar usuarios".]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Informe de sucesos de seguridad

También puedes comprobar el estado de eliminaciones anteriores descargando un informe de sucesos de seguridad. Para más información, consulta [Configuración de seguridad]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Preguntas más frecuentes {#faq}

### ¿Puedo eliminar segmentos con más de 100 millones de usuarios?

No. No puedes eliminar segmentos con más de 100 millones de usuarios. Si necesitas ayuda para eliminar un segmento de este tamaño, ponte en contacto con [support@braze.com](mailto:support@braze.com).

### ¿Afecta la automatización de la fusión de usuarios a la eliminación de usuarios?

Si una fusión programada incluye perfiles de usuario pendientes de eliminación, Braze omite esos perfiles y no los fusiona. Para fusionar estos perfiles, debes impedir que se borren.

### ¿Qué ocurre con los datos enviados a los usuarios pendientes de eliminación?

Se siguen aceptando los datos enviados desde sistemas externos o SDK, pero los usuarios se eliminarán según lo programado, independientemente de su actividad.

### ¿Se desencadenarán lienzos y campañas para los usuarios pendientes de eliminar?

Sí. Sin embargo, puedes añadir un filtro de inclusión de segmentos para excluir a todos los usuarios con el [filtro de segmentos](#segment-filters) **Pendiente de borrado**.

### ¿Puedo recuperar perfiles de usuario eliminados?

La eliminación de usuarios individuales es permanente.

Puedes [cancelar la eliminación de segmentos](#cancel) dentro de los 7 días siguientes. Sin embargo, los usuarios que ya hayan sido eliminados antes de la cancelación no podrán ser restaurados.
