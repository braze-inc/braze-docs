---
nav_title: Zonas horarias del espacio de trabajo
article_title: Zonas horarias del espacio de trabajo para el envío de mensajes
alias: /workspace_time_zones/
page_order: 3
description: "Este artículo de referencia explica cómo configurar diferentes zonas horarias para tus espacios de trabajo de Braze, lo que proporciona un mayor control sobre la programación de campañas y Canvas para equipos que operan en distintas ubicaciones geográficas."
---

# Zonas horarias del espacio de trabajo para el envío de mensajes

> Las zonas horarias del espacio de trabajo permiten a los administradores definir zonas horarias específicas para cada espacio de trabajo individual. Esto hace que las campañas programadas y los Canvases (que no utilizan la hora local ni Intelligent Timing) se envíen según la zona horaria designada por el espacio de trabajo, en lugar de la zona horaria general de la empresa.

{% multi_lang_include early_access_beta_alert.md feature='Workspace time zones' %}

De forma predeterminada, un nuevo espacio de trabajo hereda la zona horaria establecida para tu empresa. Los administradores pueden anular este valor predeterminado para uno o varios espacios de trabajo con zonas horarias de espacio de trabajo. Cuando se establece una zona horaria para un espacio de trabajo, las campañas programadas y los lienzos dentro de ese espacio de trabajo hacen referencia a esa nueva zona horaria para sus horas de envío.

Por ejemplo, si la zona horaria de un espacio de trabajo está configurada en PST y una campaña dentro de ese espacio de trabajo está programada para enviarse a las 3 p. m. PST, se entregará a las 3 p. m. PST. Esto es así incluso si la zona horaria general de tu empresa es diferente (como la EST, donde las 3 p. m. PST serían las 6 p. m. EST).

## Administración de las zonas horarias del espacio de trabajo

Si eres administrador, puedes acceder y gestionar las zonas horarias del espacio de trabajo en **Configuración** > **Configuración de administrador** > **Zonas horarias del espacio de trabajo**.

Aquí puedes ver una lista de todos tus espacios de trabajo, su zona horaria configurada y la última vez que se editó la zona horaria. Utiliza la barra de búsqueda para encontrar espacios de trabajo específicos por su nombre.

![Página «Zonas horarias del espacio de trabajo» con una lista de espacios de trabajo, sus respectivas zonas horarias y la fecha de la última modificación de las zonas horarias.]({% image_buster /assets/img/workspaces/time_zones/workspace_time_zones_page.png %})

### Configuración de la zona horaria 

{% alert note %}
Las actualizaciones de la zona horaria pueden tardar unos minutos en surtir efecto.
{% endalert %}

{% tabs %}
{% tab Single workspace %}
1. Busca el espacio de trabajo deseado en la lista.
2. Selecciona el icono **Editar** junto al nombre del espacio de trabajo.

![Botón «Editar» junto al nombre de un espacio de trabajo.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3\. En el menú desplegable, selecciona la zona horaria deseada para ese espacio de trabajo.
4\. Seleccione **Guardar**.

![Menú desplegable con la zona horaria GMT seleccionada.]({% image_buster /assets/img/workspaces/time_zones/edit_single_workspace.png %})
{% endtab %}
{% tab Multiple workspaces %}

Puedes aplicar una zona horaria específica a varios espacios de trabajo a la vez haciendo lo siguiente:

1. Selecciona las casillas junto a todos los espacios de trabajo que deseas actualizar.
2. Selecciona **Editar zona horaria**.
3. En el menú desplegable, selecciona una zona horaria para aplicarla a todos los espacios de trabajo seleccionados.

![Página «Zonas horarias del espacio de trabajo» con varios espacios de trabajo seleccionados y un botón «Editar zona horaria».]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4\. Seleccione **Guardar**. 

{% endtab %}
{% endtabs %}

## Impacto en las campañas y los lienzos

{% alert important %}
Informad a los equipos y partes interesadas pertinentes dentro de cada espacio de trabajo sobre cualquier cambio de zona horaria para evitar confusiones sobre los calendarios de las campañas.
{% endalert %}

- **Campañas de hora local y hora inteligente:** Las campañas y los lienzos que utilizan la hora local del usuario o [la hora inteligente]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#option-3-intelligent-timing) para la entrega seguirán funcionando como antes y no se verán afectados por las zonas horarias del espacio de trabajo.
- **Campañas programadas y lienzos:** Cualquier campaña programada o Canvas que no utilice la hora local del usuario o la hora inteligente para la entrega, ahora se enviará según la zona horaria seleccionada en el espacio de trabajo.
- **Campañas programadas antes de un cambio de zona horaria:** Si programaste una campaña o Canvas antes de cambiar la zona horaria del espacio de trabajo, Braze mantiene la hora de envío original y no la reprograma. Por ejemplo, si una campaña está configurada para enviarse a las 7 p. m. PST y la zona horaria del espacio de trabajo se cambia a EST, la campaña se seguirá enviando a las 7 p. m. PST (que ahora corresponde a las 10 p. m. EST). El sistema seguirá haciendo referencia a la hora original, pero la interpretará según la nueva zona horaria del espacio de trabajo.

## Impacto en los filtros de audiencia basados en fechas

Cuando se actualiza la zona horaria de un espacio de trabajo, los filtros de audiencia que utilizan criterios basados únicamente en la fecha (sin especificar una hora concreta) se reevalúan en función de los límites de la nueva zona horaria.

Para filtros como «Última vez que se realizó el evento personalizado X después de», Braze utiliza la zona horaria del espacio de trabajo para determinar el inicio y el final del día del calendario. Al cambiar esta configuración, se modifica la hora límite de las 11:59 p. m. para esa fecha específica.

### Ejemplo

Un espacio de trabajo actualiza tu zona horaria de hora del este (EST) a hora del Pacífico (PST).

- **Hora límite anterior:** 11:59 p. m. EST
- **Nueva hora límite:** 11:59 p. m. PST (que son las 2:59 a. m. EST del día siguiente)

Tras este cambio, un usuario que realice el evento personalizado a las 10 p. m. PST del 6 de marzo de 2026 (que es la 1 a. m. EST del 7 de marzo de 2026) ahora se incluye en la audiencia, ya que se encuentra dentro del límite del calendario PST para esa fecha.

## Discrepancias en los informes

Las zonas horarias del espacio de trabajo proporcionan un control preciso sobre el envío de campañas, pero debes tener en cuenta las posibles discrepancias en los informes mientras esta característica se encuentra en fase de acceso anticipado. Comprueba los puntos de datos de referencia cruzada y ten en cuenta la zona horaria al analizar informes de espacios de trabajo con modificaciones específicas de zona horaria.