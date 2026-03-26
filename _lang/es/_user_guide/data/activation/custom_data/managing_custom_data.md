---
nav_title: Gestionar datos personalizados
article_title: Administrar datos personalizados
page_order: 20
page_type: reference
description: "Este artículo de referencia explica cómo gestionar los datos personalizados, como la prepoblación de campañas y segmentos o el bloqueo y la eliminación de datos."
---

# Gestionar datos personalizados

> Esta página explica cómo rellenar previamente datos personalizados en tus campañas y segmentos, bloquear datos que ya no son útiles y gestionar eventos y atributos personalizados y propiedades.<br><br>Para saber cómo gestionar atributos personalizados en particular, consulta [Gestionar atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).

## Introducción previa de datos personalizados

Puede haber ocasiones en las que quieras configurar campañas y segmentos utilizando datos personalizados antes de que tu equipo de desarrollo haya integrado esos datos personalizados. Braze te permite rellenar previamente eventos y atributos personalizados en el dashboard antes de que estos datos comiencen a rastrearse, de modo que estos eventos y atributos estén disponibles para su uso en desplegables y como parte del proceso de creación de campañas.

Para rellenar previamente eventos y atributos personalizados, haz lo siguiente:

1. Ve a **Configuración de datos** > **Eventos personalizados** o **Atributos personalizados** o **Productos**.

![Navega hasta Atributos personalizados o Eventos personalizados o Productos.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2. Para añadir un atributo personalizado, un evento o un producto, ve a la página correspondiente y selecciona **Añadir atributos personalizados** o **Añadir eventos personalizados** o **Añadir productos**.<br><br>Para los atributos personalizados, selecciona un [tipo de datos]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para este atributo (por ejemplo, booleano o cadena). El tipo de datos de un atributo determinará los filtros de segmentación disponibles para ese atributo. <br><br>![Añadir nuevo atributo o evento]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3. Selecciona **Guardar**.

### Nombrar eventos y atributos personalizados

Los eventos y atributos personalizados distinguen entre mayúsculas y minúsculas. Ten esto en cuenta cuando tu equipo de desarrollo integre estos eventos o atributos personalizados más adelante. Deben nombrar los eventos o atributos personalizados exactamente como los nombraste aquí, o Braze generará un evento o atributo personalizado diferente.

## Gestión de propiedades

Después de crear un evento personalizado o un producto, selecciona **Gestionar propiedades** de ese evento o producto para añadir nuevas propiedades, bloquear propiedades existentes y ver qué campañas o Canvas utilizan esta propiedad en un [evento desencadenante]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

![Propiedades personalizadas para un evento personalizado.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

Para que estos atributos personalizados, eventos, productos o propiedades del evento añadidos sean rastreables, debes pedir a tu equipo de desarrollo que los cree en el SDK utilizando el nombre exacto que utilizaste para añadirlos anteriormente. O puedes utilizar la [API]({{site.baseurl}}/api/basics/) de Braze para importar datos sobre ese atributo. Después de eso, el atributo personalizado, evento u otro será accionable y se aplicará a tus usuarios.

{% multi_lang_include alerts/note_alerts.md alert='Manage custom data storage' %}

## Bloquear datos personalizados

En ocasiones, es posible que identifiques atributos personalizados, eventos personalizados o eventos de compra que registran demasiados puntos de datos, ya no son útiles para tu estrategia de marketing o se registraron por error. 

Para impedir que estos datos se envíen a Braze, puedes bloquear un objeto de datos personalizado mientras tu equipo de ingeniería trabaja para eliminarlo del backend de tu aplicación o sitio web. El bloqueo impide que Braze registre un objeto de datos personalizado concreto en el futuro, lo que significa que no aparecerá cuando busques un usuario concreto.

Los datos bloqueados no serán enviados por el SDK, y el dashboard de Braze no procesará los datos bloqueados de otras fuentes (por ejemplo, la API). Sin embargo, el bloqueo no elimina los datos de los perfiles de usuario ni disminuye retroactivamente la cantidad de puntos de datos incurridos para ese objeto de datos personalizado.

### Permisos de usuario necesarios

Para bloquear datos personalizados, necesitas los [permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) en el siguiente desplegable para tu espacio de trabajo.

{% details Permisos de usuario para bloquear datos personalizados %}

{% multi_lang_include deprecations/user_permissions.md %}

- Ver campañas
- Editar campañas
- Archivar campañas
- Ver Canvas
- Editar Canvas
- Archivar Canvas
- Ver reglas de limitación de frecuencia
- Editar reglas de limitación de frecuencia
- Ver priorización de mensajes
- Editar priorización de mensajes
- Ver bloques de contenido
- Ver conmutadores de características
- Editar conmutadores de características
- Archivar conmutadores de características
- Ver segmentos
- Editar segmentos
- Ver plantillas IAM
- Editar plantillas IAM
- Archivar plantillas IAM
- Ver plantillas de correo electrónico
- Editar plantillas de correo electrónico
- Archivar plantillas de correo electrónico
- Ver plantillas de webhook
- Editar plantillas de webhook
- Archivar plantillas de webhook
- Ver plantillas de enlaces de correo electrónico
- Editar plantillas de enlaces de correo electrónico
- Ver activos de la biblioteca de medios
- Editar activos de la biblioteca de medios
- Eliminar activos de la biblioteca de medios
- Ver ubicaciones
- Editar ubicaciones
- Archivar ubicaciones
- Ver códigos promocionales
- Editar códigos promocionales
- Exportar códigos promocionales
- Ver centros de preferencia
- Editar centros de preferencia
- Ver informes
- Editar informes

{% enddetails %}

### Bloqueo de atributos personalizados, eventos personalizados y productos

{% alert important %}
Cuando un evento o atributo es bloqueado, cualquier segmento, campaña o Canvas que utilice ese evento o atributo será archivado.
{% endalert %}

Para detener el seguimiento de un atributo personalizado, evento o producto específico, sigue estos pasos:

1. Búscalo en las páginas **Atributos personalizados**, **Eventos personalizados** o **Productos**.
2. Selecciona el atributo, evento o producto personalizado. Para atributos y eventos personalizados, puedes seleccionar hasta 100 a la vez para bloquearlos.
3. Selecciona **Lista de bloqueo**.

![Varios atributos personalizados seleccionados que están incluidos en la lista de bloqueados en la página Atributos personalizados.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Puedes bloquear hasta 300 atributos personalizados y 300 eventos personalizados. Para evitar la recopilación de determinados atributos del dispositivo, consulta nuestra [guía del SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection). 

{% alert important %}
Los atributos personalizados o los eventos personalizados con estado **En la papelera** se tendrán en cuenta para el límite de la lista de bloqueados hasta que se eliminen.
{% endalert %}

Cuando se bloquea un evento o atributo personalizado, se aplica lo siguiente:

- No se procesará ningún dato enviado a Braze, y los eventos y atributos bloqueados ya no contarán como puntos de datos
- Los datos existentes no estarán disponibles, a menos que se reactiven
- Los eventos y atributos bloqueados no aparecerán en los filtros ni en los gráficos
- Las referencias a datos bloqueados en borradores de Canvas activos se cargarán como valores no válidos, lo que puede provocar errores
- Se archivará todo lo que utilice el evento o atributo bloqueado

Para ello, Braze envía la información de la lista de bloqueo a cada dispositivo. Esto es importante cuando piensas en bloquear un gran número de eventos y atributos (cientos de miles o millones), ya que sería una operación que requeriría muchos datos.

### Consideraciones sobre las listas de bloqueo

Es posible bloquear un gran número de eventos y atributos, pero no es aconsejable. Esto se debe a que cada vez que se realiza un evento o se envía (potencialmente) un atributo a Braze, este evento o atributo tiene que comprobarse con toda la lista de bloqueo.

Se envían hasta 300 elementos al SDK para bloquearlos. Si bloqueas más de 300 elementos, estos datos se enviarán desde el SDK. Si no necesitas utilizar el evento o atributo en el futuro, considera la posibilidad de eliminarlo del código de tu aplicación durante tu próxima versión. Los cambios en la lista de bloqueo pueden tardar unos minutos en propagarse. Puedes volver a habilitar cualquier evento o atributo de la lista de bloqueo en cualquier momento.

## Eliminar datos personalizados

A medida que construyas campañas y segmentos específicos, puede que te des cuenta de que ya no necesitas un evento personalizado o un atributo personalizado. Por ejemplo, si utilizaste un atributo personalizado específico como parte de una campaña única, puedes eliminar estos datos después de [bloquearlos](#blocklisting-custom-attributes-custom-events-and-products) y eliminar sus referencias de tu aplicación. Puedes eliminar cualquier tipo de datos (como cadenas, números y atributos personalizados anidados).

{% alert important %}
Debes ser [administrador de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) para eliminar datos personalizados.
{% endalert %}

Para eliminar un evento personalizado o un atributo personalizado, haz lo siguiente:

1. Ve a **Configuración de datos** > **Atributos personalizados** o **Eventos personalizados**, según el tipo de datos que quieras eliminar.
2. Ve a los datos personalizados y selecciona <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Acciones** > **Lista de bloqueo**.
3. Cuando tus datos personalizados hayan estado bloqueados durante 7 días, selecciona <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Acciones** > **Eliminar**.

### Cómo funciona la eliminación

Cuando eliminas datos personalizados, ocurre lo siguiente: 

- **Para atributos personalizados:** Elimina permanentemente los datos de atributos del perfil de cada usuario.
- **Para eventos personalizados:** Elimina permanentemente los metadatos de eventos del perfil de cada usuario.

Cuando se selecciona un atributo o evento para eliminarlo, su estado cambia a **Papelera**. Durante los siete días siguientes, es posible restaurar el atributo o evento. Si no lo restauras al cabo de siete días, los datos se eliminarán permanentemente. Si restauras el atributo o evento, volverá al estado de bloqueado.

La eliminación no impide el registro adicional de los objetos de datos personalizados en los perfiles de usuario, así que asegúrate de que los datos personalizados ya no se están registrando antes de eliminar el evento o atributo.

### Lo que debes saber

Cuando elimines datos personalizados, ten en cuenta los siguientes detalles:

* **La eliminación es permanente**. No se pueden recuperar los datos.
* Los datos se eliminan de la plataforma Braze y de los perfiles de usuario.
* Puedes "reutilizar" el nombre del atributo personalizado o el nombre del evento personalizado después de eliminarlo. Esto significa que si observas que los datos personalizados "reaparecen" en Braze después de eliminarlos, puede deberse a una integración que no se ha detenido y está enviando datos con el mismo nombre de datos personalizados.
* Puede que tengas que volver a bloquear un elemento si al eliminarlo vuelven a aparecer datos personalizados. El estado de la lista de bloqueo no se conserva porque los datos personalizados se han eliminado.
* Eliminar datos personalizados no registra [puntos de datos]({{site.baseurl}}/user_guide/data/data_points) ni genera nuevos puntos de datos para su uso.

## Forzar la comparación de tipos de datos

Braze reconoce automáticamente los tipos de datos de los atributos que se nos envían. Sin embargo, en el caso de que se apliquen varios tipos de datos a un mismo atributo, puedes forzar el tipo de datos de cualquier atributo para que sepamos cuál es. Selecciónalo en el desplegable de la columna **Tipo de datos**.

{% alert note %}
Forzar tipos de datos no se aplica a las propiedades del evento ni a las propiedades de la compra.
{% endalert %}

![Desplegable de tipo de datos de atributos personalizados]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
Si eliges forzar el tipo de datos de un atributo, cualquier dato que entre que no sea del tipo especificado será convertido a ese tipo. Si tal conversión es imposible (por ejemplo, que una cadena que contiene letras se convierta en un número), se ignorarán los datos. Cualquier dato ingerido antes del cambio de tipo seguirá almacenándose como el tipo antiguo (y, por tanto, puede no ser segmentable), y aparecerá una advertencia junto al atributo en los perfiles de los usuarios afectados.
{% endalert %}

### Coerción de tipos de datos

| Tipo de datos forzado | Descripción |
|------------------|-------------|
| Booleano | Las entradas de `1`, `true`, `t` (sin distinguir mayúsculas de minúsculas) se almacenarán como `true` |
| Booleano | Las entradas de `0`, `false`, `f` (sin distinguir mayúsculas de minúsculas) se almacenarán como `false` |
| Número | Los números enteros o flotantes (como `1`, `1.5`) se almacenarán como números |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener más información sobre las opciones de filtro que ofrecen las diferentes comparaciones de tipos de datos, consulta [Configuración de informes]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting). Para obtener más información sobre los diferentes tipos de datos disponibles, consulta [Tipos de datos de atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).

{% alert note %}
Los datos enviados a Braze son inmutables y no pueden eliminarse ni modificarse después de que los hayamos recibido. Sin embargo, puedes utilizar cualquiera de los pasos enumerados en las secciones anteriores para ejercer control sobre lo que estás rastreando en tu dashboard.
{% endalert %}