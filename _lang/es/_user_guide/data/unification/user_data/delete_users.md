---
nav_title: Borrar usuarios
article_title: Borrar usuarios
page_order: 4.2
toc_headers: h2
description: "Aprende a eliminar un usuario individual o un segmento de usuarios directamente a través del panel de Braze."
alias: /delete_users/
hidden: true
---

# Borrar usuarios

> Aprende a eliminar un usuario individual o un segmento de usuarios directamente a través del panel de Braze.

{% alert important %}
El acceso anticipado a esta característica está temporalmente cerrado. Ponte en contacto con tu administrador del éxito del cliente para obtener más detalles.
{% endalert %}

## Requisitos previos

Debes ser administrador para eliminar usuarios.

## Acerca de la eliminación de usuarios

La eliminación de usuarios te permite administrar tu base de datos eliminando perfiles que ya no son necesarios, que se han creado por error o que deben eliminarse por motivos de cumplimiento normativo (como el RGPD o la CCPA).

| Consideración | Detalles |
|---------------|---------|
| Tamaño máximo | Puedes eliminar hasta 100 millones de perfiles de usuario al eliminar un segmento. |
| Período de espera | Todas las eliminaciones de segmentos requieren un período de espera de 7 días, más el tiempo que lleva procesar las eliminaciones. |
| Límites del trabajo | Solo se puede eliminar un segmento cada vez, lo que incluye el periodo de espera de 7 días. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Eliminación de usuarios

Puedes eliminar un [usuario individual](#delete-individual) o un [segmento de usuarios](#delete-segment) a través del panel de Braze:

### Eliminar a una persona {#delete-individual}

Para eliminar un usuario individual de Braze, ve a **Audiencia** > **Búsqueda **de **usuarios**, luego busca y selecciona un usuario. Si vas a eliminar un perfil de usuario duplicado, comprueba que has seleccionado el correcto.

![La página «Buscar usuarios» en Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Las eliminaciones de usuarios individuales son permanentes: los perfiles no se pueden recuperar una vez eliminados.  
{% endalert %}

En la página de perfil, selecciona<i class="fa-solid fa-ellipsis-vertical"></i>**Mostrar opciones** > **Eliminar usuario**. Ten en cuenta que pueden pasar unos minutos hasta que el usuario se elimine por completo de Braze.

![Un usuario en Braze con el menú de puntos suspensivos verticales abierto, que muestra la opción para eliminar al usuario.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Eliminar un segmento {#delete-segment}

Si aún no lo has hecho, [crea un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) que contenga los perfiles de usuario que deseas eliminar. Asegúrate de incluir todos los perfiles de usuario si vas a eliminar usuarios duplicados.

En Braze, ve a **Audiencia** > **Administrar audiencia** y, a continuación, selecciona la pestaña **Eliminar usuarios**.

![La pestaña «Eliminar usuarios» en la sección «Gestionar audiencia» del panel de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Selecciona **Eliminar usuarios**, elige el segmento que deseas eliminar y, a continuación, selecciona **Siguiente**.

![Una ventana emergente con un segmento seleccionado para su eliminación.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Escribe **DELETE** para confirmar tu solicitud y, a continuación, selecciona **Eliminar usuarios**.

![La página de confirmación con «DELETE» escrito en el cuadro de confirmación.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Los usuarios de este segmento no se eliminarán inmediatamente. En su lugar, se marcarán como pendientes de eliminación durante los próximos 7 días. Pasado este tiempo, se eliminarán y te enviaremos un correo electrónico para informarte.

{% alert tip %}
Para garantizar que estos usuarios concretos se eliminen independientemente de los cambios en los segmentos, se crea automáticamente un filtro de segmento denominado **«Pendiente de eliminación**». Puedes [utilizar este filtro]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) para comprobar el estado de las eliminaciones pendientes.
{% endalert %}

## Confirmación de eliminaciones de segmentos

Braze envía un correo electrónico de confirmación con el número de perfiles pendientes de eliminación.

Para continuar con la eliminación, inicia sesión en Braze y confirma la solicitud de eliminación.

Si no confirmas dentro del plazo indicado en el correo electrónico, la solicitud de eliminación caducará y no se llevará a cabo.

## Cancelación de eliminaciones de segmentos {#cancel}

Tienes 7 días para cancelar las eliminaciones de segmentos pendientes. Para cancelar, ve a **Audiencia** > **Administrar audiencia** y, a continuación, selecciona la pestaña **Eliminar usuarios**.

![La pestaña «Eliminar usuarios» en la sección «Gestionar audiencia» del panel de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Junto a una eliminación de segmento pendiente, selecciona<i class="fa-solid fa-eye"></i>  para abrir los detalles del registro de eliminación.

![Una eliminación de segmento pendiente en la pestaña «Eliminar usuarios».]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

En los detalles del registro de eliminación, selecciona **Cancelar eliminación**.

![La ventana «Detalles de eliminación de registro» en la pestaña «Eliminar usuarios».]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Cuando se está realizando una eliminación masiva de usuarios, puedes cancelarla en cualquier momento. Sin embargo, los usuarios que ya hayan sido eliminados antes de la cancelación no podrán ser restaurados.
{% endalert %}

## Comprobación del estado de eliminación {#status}

Puedes comprobar el estado de una eliminación utilizando [filtros de segmentos](#segment-filters), la página [de gestión de audiencias](#manage-audience) o [los informes de eventos de seguridad](#security-event-report).

### Filtros de segmentos

Cuando solicitas que se elimine un segmento de usuarios, se crea automáticamente un [filtro de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) denominado **«Pendiente de eliminación**». Puedes utilizarlo para:

- Ver el conjunto exacto de usuarios vinculados a una fecha de ejecución de eliminación específica.
- Excluye a esos usuarios de las campañas para que no reciban mensajes antes de su eliminación.
- Exporta la lista si la necesitas para fines de cumplimiento normativo o mantenimiento de registros.

### Administrar la audiencia

{% alert note %}
Para obtener la lista exacta de usuarios que se eliminarán, utiliza el [filtro del segmento de Eliminación pendiente](#segment-filters).
{% endalert %}

Ve a **Audiencia** > **Administrar audiencia** y, a continuación, selecciona la pestaña **Eliminar usuarios**.

![La pestaña «Eliminar usuarios» en la sección «Gestionar audiencia» del panel de Braze.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

En esta página, puedes encontrar la siguiente información general sobre todas las eliminaciones actuales y pendientes:

| Campo | Descripción |
|-------|-------------|
| Fecha de la solicitud | La fecha en que se realizó la solicitud originalmente. Úsalo para filtrar los perfiles pendientes de eliminación con el filtro **Eliminación pendiente**. |
| Solicitante | El usuario que inició la solicitud de eliminación. |
| Nombre del segmento | El nombre del segmento utilizado para seleccionar los usuarios pendientes de eliminación. |
| Estado | Muestra si la solicitud de eliminación está pendiente, en curso o completada. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para obtener más detalles sobre una solicitud específica, selecciona<i class="fa-solid fa-eye"></i>  para mostrar los detalles del registro de eliminación. Aquí también puedes [cancelar las eliminaciones de segmentos pendientes](#cancel).

![Una eliminación de segmento pendiente en la pestaña «Eliminar usuarios».]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Informe de sucesos de seguridad

También puedes consultar el estado de las eliminaciones anteriores descargando un informe de eventos de seguridad. Para obtener más información, consulta [Configuración de seguridad]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Preguntas más frecuentes {#faq}

### ¿Puedo eliminar segmentos con más de 100 millones de usuarios?

No. No puedes eliminar segmentos con más de 100 millones de usuarios. Si necesitas ayuda para eliminar un segmento de este tamaño, ponte en contacto con [support@braze.com](mailto:support@braze.com).

### Parece que no puedo eliminar 100 millones de usuarios y solo puedo eliminar 10 millones. ¿Es esto un error?

No, esto no es un error. Algunos clientes tienen un límite en el número de usuarios que pueden eliminar durante el programa de acceso anticipado (EA).

A medida que avanza el programa EA, esta capacidad está diseñada para aumentar hasta que todos los clientes puedan eliminar hasta 100 millones de usuarios.

Si deseas aumentar esta capacidad, ponte en contacto con tu director de cuentas de Braze. Las solicitudes se conceden a discreción del equipo de producto.

### ¿La automatización de la fusión de usuarios afecta a la eliminación de usuarios?

Si una fusión programada incluye perfiles de usuario pendientes de eliminación, Braze omite esos perfiles y no los fusiona. Para fusionar estos perfiles, debes eliminarlos de la lista de eliminación.

### ¿Qué ocurre con los datos enviados a los usuarios pendientes de eliminación?

Los datos enviados desde sistemas externos o SDK siguen siendo aceptados, pero los usuarios serán eliminados según lo previsto, independientemente de su actividad.

### ¿Desencadenarán los lienzos y las campañas para los usuarios pendientes de eliminación?

Sí. Sin embargo, puedes añadir un filtro de inclusión de segmento para excluir a todos los usuarios con el [filtro de segmento](#segment-filters) **Eliminación pendiente**.

### ¿Puedes recuperar perfiles de usuario eliminados?

La eliminación de usuarios individuales es permanente.

Puedes [cancelar las eliminaciones de segmentos](#cancel) en los primeros 7 días posteriores. Sin embargo, los usuarios que ya hayan sido eliminados antes de la cancelación no podrán ser restaurados.
