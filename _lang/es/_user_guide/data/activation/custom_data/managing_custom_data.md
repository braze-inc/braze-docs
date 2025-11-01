---
nav_title: Gestión de datos personalizados
article_title: Gestión de datos personalizados
page_order: 20
page_type: reference
description: "Este artículo de referencia explica cómo gestionar datos personalizados, como la prepoblación de campañas y segmentos o el bloqueo y la eliminación de datos."
---

# Gestión de datos personalizados

> Esta página explica cómo rellenar previamente datos personalizados en tus campañas y segmentos, bloquear datos que ya no son útiles y gestionar eventos y atributos personalizados y propiedades.<br><br>Para saber cómo gestionar atributos personalizados en particular, consulta [Gestionar atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).

## Pre-población de datos personalizados

Puede haber ocasiones en las que quieras configurar campañas y segmentos utilizando datos personalizados antes de que tu equipo de desarrolladores haya integrado esos datos personalizados. Braze te permite rellenar previamente eventos y atributos personalizados en el panel antes de que estos datos empiecen a ser objeto de seguimiento, de modo que estos eventos y atributos estén disponibles para su uso en desplegables y como parte del proceso de creación de campañas.

Para rellenar previamente eventos y atributos personalizados, haz lo siguiente:

1. Ve a **Configuración de datos** > Eventos personalizados o **Atributos personalizados o Productos.** 

\![Navega a Atributos personalizados o Eventos o productos personalizados.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2\. Para añadir un atributo personalizado, un evento o un producto, ve a la página correspondiente y selecciona **Añadir atributos personalizados** o **Añadir eventos personalizados** o **Añadir productos**.<br><br>Para los atributos personalizados, selecciona un [tipo de datos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para este atributo (por ejemplo, booleano o cadena). El tipo de datos de un atributo determinará los filtros de segmentación disponibles para ese atributo. <br><br>\![Añadir nuevo atributo o evento]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3\. Selecciona **Guardar**.

### Nombrar eventos personalizados y atributos personalizados

Los eventos personalizados y los atributos personalizados distinguen entre mayúsculas y minúsculas. Tenlo en cuenta cuando tu equipo de desarrolladores integre posteriormente estos eventos personalizados o atributos. Deben nombrar los eventos o atributos personalizados exactamente como los has nombrado aquí, o Braze generará un evento o atributo personalizado diferente.

## Administrador de propiedades

Después de crear un evento personalizado o un producto, selecciona **Gestionar propiedades** de ese evento o producto para añadir nuevas propiedades, bloquear propiedades existentes y ver qué campañas o Lienzos utilizan esta propiedad en un [evento desencadenante]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

\![Propiedades personalizadas para un evento personalizado.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

Para que estos atributos personalizados, eventos, productos o propiedades del evento añadidos sean rastreables, debes pedir a tu equipo desarrollador que los cree en el SDK utilizando el nombre exacto que utilizaste para añadirlos anteriormente. O puedes utilizar [la API de]({{site.baseurl}}/api/basics/) Braze para importar datos sobre ese atributo. Después, el atributo personalizado, evento u otro será procesable y se aplicará a tus usuarios.

{% alert note %}
Todos los datos del perfil de usuario (eventos personalizados, atributos personalizados, datos personalizados) se almacenan mientras esos perfiles estén activos.
{% endalert %}

## Bloqueo de datos personalizados

Ocasionalmente puedes identificar atributos personalizados, eventos personalizados o eventos de compra que registran demasiados puntos de datos, ya no son útiles para tu estrategia de marketing o se registraron por error. 

Para impedir que estos datos se envíen a Braze, puedes bloquear un objeto personalizado de datos mientras tu equipo de ingeniería trabaja para eliminarlo del backend de tu aplicación o sitio web. El bloqueo impide que Braze registre un objeto de datos personalizado concreto en el futuro, lo que significa que no aparecerá cuando se busque a un usuario concreto.

{% alert important %}
Para bloquear datos de clientes, necesitas [permisos del usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) para acceder y editar campañas, Lienzos y segmentos.
{% endalert %}

Los datos bloqueados no serán enviados por el SDK, y el panel Braze no procesará los datos bloqueados de otras fuentes (por ejemplo, la API). Sin embargo, las listas de bloqueo no eliminan datos de los perfiles de usuario ni disminuyen retroactivamente la cantidad de puntos de datos incurridos para ese objeto personalizado.

### Bloqueo de atributos personalizados, eventos personalizados y productos

{% alert important %}
Cuando se bloquea un evento o atributo, se archivará cualquier segmento, campaña o Canvas que utilice ese evento o atributo.
{% endalert %}

Para detener el seguimiento de un atributo personalizado, evento o producto específico, sigue estos pasos:

1. Búscalo en las páginas **Atributos personalizados**, **Eventos personalizados** o **Productos**.
2. Selecciona el atributo personalizado, evento o producto. Para atributos y eventos personalizados, puedes seleccionar hasta 100 a la vez para bloquearlos.
3. Selecciona **Lista de bloqueo**.

Múltiples atributos personalizados seleccionados que aparecen bloqueados en la página Atributos personalizados.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Puedes bloquear hasta 300 atributos personalizados y 300 eventos personalizados. Para evitar que se recojan determinados atributos de los dispositivos, consulta nuestra [guía del SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection). 

{% alert important %}
Los atributos personalizados o eventos personalizados con un estado de **Eliminado** contarán para el límite de la lista de bloqueados hasta que se eliminen.
{% endalert %}

Cuando se bloquea un evento personalizado o un atributo, se aplica lo siguiente:

- No se procesará ningún dato enviado a Braze, y los eventos y atributos de la lista de bloqueo ya no contarán como puntos de datos.
- Los datos existentes no estarán disponibles a menos que se reactiven
- Los eventos y atributos bloqueados no aparecerán en los filtros ni en los gráficos
- Las referencias a datos bloqueados dentro de borradores de Lienzos activos se cargarán como valores no válidos, lo que puede provocar errores
- Todo lo que utilice el evento o atributo bloqueado se archivará

Para ello, Braze envía la información de la lista de bloqueo a cada dispositivo. Esto es importante cuando se piensa en bloquear un gran número de sucesos y atributos (cientos de miles o millones), ya que sería una operación que requeriría muchos datos.

### Consideraciones para la lista de bloqueo

Es posible bloquear un gran número de eventos y atributos, pero no es aconsejable. Esto se debe a que cada vez que se realiza un evento o se envía (potencialmente) un atributo a Braze, este evento o atributo tiene que comprobarse con toda la lista de bloqueo.

Se envían hasta 300 artículos al SDK para bloquearlos. Si bloqueas más de 300 elementos, estos datos se enviarán desde el SDK. Si no necesitas utilizar el evento o atributo en el futuro, considera la posibilidad de eliminarlo del código de tu aplicación durante tu próxima versión. Los cambios en la lista de bloqueo pueden tardar unos minutos en propagarse. Puedes volver a habilitar cualquier evento o atributo de la lista de bloqueo en cualquier momento.

## Borrar datos personalizados

A medida que construyas campañas y segmentos específicos, puede que te des cuenta de que ya no necesitas un evento personalizado o un atributo personalizado. Por ejemplo, si utilizaste un atributo personalizado específico como parte de una campaña única, puedes eliminar estos datos después de [bloquearlos](#blocklisting-custom-attributes-custom-events-and-products) y eliminar sus referencias de tu aplicación. Puedes eliminar cualquier tipo de datos (como cadenas, números y atributos personalizados anidados).

{% alert important %}
Debes ser [administrador de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) para eliminar datos personalizados.
{% endalert %}

Para eliminar un evento personalizado o un atributo personalizado, haz lo siguiente:

1. Ve a **Configuración de datos** > **Atributos personalizados** o **Eventos personalizados**, según el tipo de datos que quieras eliminar.
2. Ve a los datos de clientes y selecciona <i class="fa-solid fa-ellipsis-vertical"></i> **Acciones** > **Lista de bloqueos**.
3. Cuando tus datos personalizados hayan estado bloqueados durante 7 días, selecciona <i class="fa-solid fa-ellipsis-vertical"></i> **Acciones** > Eliminar **.**

### Cómo funciona la eliminación

Cuando eliminas datos personalizados, ocurre lo siguiente: 

- **Para atributos personalizados:** Elimina permanentemente los datos de atributos del perfil de cada usuario.
- **Para eventos personalizados:** Elimina permanentemente los metadatos de eventos del perfil de cada usuario.

Cuando se selecciona un atributo o evento para eliminarlo, su estado cambia a **Papelera**. Durante los siete días siguientes, es posible restaurar el atributo o evento. Si no la restauras al cabo de siete días, los datos se borrarán permanentemente. Si restableces el atributo o evento, volverá al estado de bloqueo.

La eliminación no impide el registro adicional de los objetos de datos personalizados en los perfiles de usuario, así que asegúrate de que los datos personalizados ya no se están registrando antes de eliminar el evento o atributo.

### Lo que debes saber

Cuando elimines datos personalizados, ten en cuenta los siguientes detalles:

* **La eliminación es permanente**. No se pueden recuperar los datos.
* Los datos se eliminan de la plataforma Braze y de los perfiles de usuario.
* Puedes "reutilizar" el nombre del atributo personalizado o el nombre del evento personalizado después de eliminarlo. Esto significa que si observas que los datos personalizados "reaparecen" en Braze después de eliminarlos, puede deberse a una integración que no se ha detenido y está enviando datos con el mismo nombre de datos personalizados.
* Puede que tengas que volver a bloquear un elemento si al borrarlo vuelven a aparecer datos personalizados. El estado de la lista de bloqueo no se conserva porque se han eliminado los datos personalizados.
* Eliminar datos personalizados no registra ningún [punto de datos]({{site.baseurl}}/user_guide/data/data_points) y tampoco genera nuevos puntos de datos para utilizar.

## Forzar comparaciones de tipos de datos

Braze reconoce automáticamente los tipos de datos de atributo que se nos envían. Sin embargo, en el caso de que se apliquen varios tipos de datos a un mismo atributo, puedes forzar el tipo de datos de cualquier atributo para que sepamos cuál es. Selecciónalo en el desplegable de la columna **Tipo de datos**.

{% alert note %}
Forzar tipos de datos no se aplica a las propiedades del evento ni a las propiedades de la compra.
{% endalert %}

Desplegable de tipo de datos de atributos personalizados]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
Si eliges forzar el tipo de datos de un atributo, cualquier dato que entre que no sea del tipo especificado será forzado a ese tipo. Si tal coacción es imposible (por ejemplo, que una cadena que contiene letras se convierta en un número), se ignorarán los datos. Cualquier dato ingestado antes del cambio de tipo seguirá almacenándose como el tipo antiguo (y, por tanto, puede no ser segmentable), y aparecerá una advertencia junto al atributo en los perfiles de los usuarios afectados.
{% endalert %}

### Coerción de tipos de datos

| Tipo de datos forzados | Descripción |
|------------------|-------------|
| Booleano | Las entradas de `1`, `true`, `t` (sin distinguir mayúsculas de minúsculas) se almacenarán como `true` |
| Booleano | Las entradas de `0`, `false`, `f` (sin distinguir mayúsculas de minúsculas) se almacenarán como `false` |
| Número | Los números enteros o flotantes (como `1`, `1.5`) se almacenarán como números |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener más información sobre las opciones específicas de filtrar expuestas por las diferentes comparaciones de tipos de datos, consulta [Configurar informes]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting). Para más información sobre los distintos tipos de datos disponibles, consulta [Tipos de datos de atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).

{% alert note %}
Los datos enviados a Braze son inmutables y no pueden borrarse ni modificarse después de que los hayamos recibido. Sin embargo, puedes utilizar cualquiera de los pasos indicados en las secciones anteriores para ejercer el control sobre lo que estás siguiendo en tu panel.
{% endalert %}


