---
nav_title: Gestión de datos personalizados
article_title: Gestión de datos personalizados
page_order: 20
page_type: reference
description: "Este artículo de referencia explica cómo gestionar los datos personalizados, como la prepoblación de campañas y segmentos o el bloqueo y la eliminación de datos."
---

# Gestión de datos personalizados

> Aprenda a rellenar previamente datos personalizados en sus campañas y segmentos, a bloquear datos que ya no son útiles y a gestionar eventos y atributos y propiedades personalizados.

## Introducción previa de datos personalizados

Puede haber ocasiones en las que desee configurar campañas y segmentos utilizando datos personalizados antes de que su equipo de desarrollo haya integrado esos datos personalizados. Braze le permite rellenar previamente eventos y atributos personalizados en el panel de control antes de que estos datos comiencen a rastrearse, de modo que estos eventos y atributos estén disponibles para su uso en desplegables y como parte del proceso de creación de campañas.

Para rellenar previamente eventos y atributos personalizados, haz lo siguiente:

1. Vaya a **Configuración de Datos** > **Eventos Personalizados** o **Atributos Personalizados** o **Productos**.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), encontrará estas páginas en **Gestionar configuración**.
{% endalert %}

![Navegue hasta Atributos personalizados o Eventos o productos personalizados.][21]{: style="max-width:90%;" }

{: start="2"}
2\. Para añadir un atributo personalizado, un evento o un producto, ve a la página correspondiente y selecciona **Añadir atributos personalizados** o **Añadir eventos personalizados** o **Añadir productos**.<br><br>Para los atributos personalizados, selecciona un [tipo de datos][20] para este atributo (por ejemplo, booleano o cadena). El tipo de datos de un atributo determinará los filtros de segmentación disponibles para ese atributo. <br><br>![Añadir nuevo atributo o evento][22]{: style="max-width:80%;" }
3\. Seleccione **Guardar**.

### Nombrar eventos y atributos personalizados

Los eventos y atributos personalizados distinguen entre mayúsculas y minúsculas. Tenga esto en cuenta cuando su equipo de desarrollo integre estos eventos o atributos personalizados más adelante. Deben nombrar los eventos o atributos personalizados exactamente como los nombró aquí, o Braze generará un evento o atributo personalizado diferente.

## Gestión de propiedades

Después de crear un evento personalizado o un producto, selecciona **Gestionar propiedades** de ese evento o producto para añadir nuevas propiedades, bloquear propiedades existentes y ver qué campañas o Lienzos utilizan esta propiedad en un [evento desencadenante]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-1-select-a-trigger-event).

![Propiedades personalizadas para un evento personalizado.][73]{: style="max-width:80%"}

Para que estos atributos personalizados, eventos, productos o propiedades de eventos añadidos sean rastreables, debe pedir a su equipo de desarrollo que lo cree en el SDK utilizando el nombre exacto que utilizó para añadirlo anteriormente. O puedes utilizar [la API]({{site.baseurl}}/api/basics/) de Braze para importar datos sobre ese atributo. Después de eso, el atributo personalizado, evento u otro será accionable y se aplicará a sus usuarios.

{% alert note %}
Todos los datos de los perfiles de usuario (eventos personalizados, atributos personalizados, datos personalizados) se almacenan mientras esos perfiles estén activos.
{% endalert %}

## Bloquear datos personalizados

Ocasionalmente puede identificar atributos personalizados, eventos personalizados o eventos de compra que consumen demasiados puntos de datos, ya no son útiles para su estrategia de marketing o se registraron por error. Para impedir que estos datos se envíen a Braze, puede bloquear un objeto de datos personalizado mientras su equipo de ingeniería trabaja para eliminarlo del backend de su aplicación o sitio web.

El bloqueo impide que un objeto de datos personalizados concreto sea registrado por Braze en el futuro, lo que significa que no aparecerá cuando se busque a un usuario concreto. Los datos bloqueados no serán enviados por el SDK, y el panel de Braze no procesará los datos bloqueados de otras fuentes (por ejemplo, la API). Sin embargo, el bloqueo no elimina los datos de los perfiles de usuario ni disminuye retroactivamente la cantidad de puntos de datos incurridos para ese objeto de datos personalizado.

### Bloqueo de atributos personalizados, eventos personalizados y productos

{% alert important %}
Cuando un evento o atributo es bloqueado, cualquier segmento, campaña o Canvas que utilice ese evento o atributo será archivado.
{% endalert %}

Para detener el seguimiento de un atributo personalizado, evento o producto específico, siga estos pasos:

1. Búsquelo en las páginas **Atributos personalizados**, **Eventos personalizados** o **Productos**.
2. Seleccione el atributo, evento o producto personalizado. Para atributos y eventos personalizados, puedes seleccionar hasta 10 a la vez para bloquearlos.
3. Selecciona **Lista de bloqueo**.

![Múltiples atributos personalizados seleccionados que aparecen bloqueados en la página Atributos personalizados.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Puedes bloquear hasta 300 atributos personalizados y 300 eventos personalizados. Para evitar que se recopilen determinados atributos de los dispositivos, consulta nuestra [Guía SDK][88].

Cuando se bloquea un evento o atributo personalizado, se aplica lo siguiente:

- No se procesará ningún dato enviado a Braze, y los eventos y atributos bloqueados ya no contarán como puntos de datos.
- Los datos existentes no estarán disponibles, a menos que se reactiven
- Los eventos y atributos bloqueados no aparecerán en los filtros ni en los gráficos.
- Las referencias a datos bloqueados en borradores de lienzos activos se cargarán como valores no válidos, lo que puede provocar errores.
- Se archivará todo lo que utilice el evento o atributo bloqueado

Para ello, Braze envía la información de la lista de bloqueo a cada dispositivo. Esto es importante cuando se piensa en bloquear un gran número de eventos y atributos (cientos de miles o millones), ya que sería una operación que requeriría muchos datos.

### Consideraciones sobre las listas de bloqueo

Hay que tener en cuenta que es posible bloquear un gran número de eventos y atributos, pero no es aconsejable. Esto se debe a que cada vez que se realiza un evento o se envía (potencialmente) un atributo a Braze, este evento o atributo tiene que comprobarse con toda la lista de bloqueo. Si aparece en la lista, no se enviará. Esta operación lleva tiempo, y si la lista crece lo suficiente, tu aplicación podría empezar a ralentizarse. Si no necesitas utilizar el evento o atributo en el futuro, deberás eliminarlo del código de tu aplicación en la próxima versión.

Los cambios en la lista de bloqueo pueden tardar unos minutos en propagarse. Puede volver a activar cualquier evento o atributo de la lista de bloqueo en cualquier momento.

## Borrar datos personalizados

A medida que construyas campañas y segmentos específicos, puede que te des cuenta de que ya no necesitas un evento personalizado o un atributo personalizado. Por ejemplo, si utilizaste un atributo personalizado específico como parte de una campaña única, puedes eliminar estos datos después de [bloquearlos](#blocklisting-custom-attributes-custom-events-and-products) y eliminar sus referencias de tu aplicación. 

Para eliminar un evento personalizado o un atributo personalizado, haz lo siguiente:

1. Ve a **Configuración de datos** > **Atributos personalizados** o **Eventos personalizados**, según el tipo de datos que quieras eliminar.
2. Ve a los datos personalizados y selecciona <i class="fa-solid fa-ellipsis-vertical"></i> **Acciones** > **Lista de bloqueos**.
3. Cuando tus datos personalizados hayan estado bloqueados durante 7 días, selecciona <i class="fa-solid fa-ellipsis-vertical"></i> **Acciones** > Eliminar **.**

### Cómo funciona la eliminación

Cuando eliminas datos personalizados, ocurre lo siguiente: 

- **Para atributos personalizados:** Elimina permanentemente los datos de atributos del perfil de cada usuario.
- **Para eventos personalizados:** Elimina permanentemente los metadatos de eventos del perfil de cada usuario.

Cuando se selecciona un atributo o evento para eliminarlo, su estado cambia a **Papelera**. Durante los siete días siguientes, es posible restaurar el atributo o evento. Si no restauras después de 7 días, los datos se borrarán permanentemente. Si restableces el atributo o evento, volverá al estado de bloqueo.

{% alert important %}
La eliminación de datos personalizados está actualmente en acceso temprano. Póngase en contacto con su gestor de cuenta Braze si está interesado en participar en el acceso anticipado. Para obtener más ayuda sobre la eliminación de datos personalizados, ponte en contacto con tu administrador del éxito del cliente o con el equipo de Soporte.<br><br>La eliminación no impide el registro adicional de los objetos de datos personalizados en los perfiles de usuario, así que asegúrate de que los datos personalizados ya no se están registrando antes de eliminar el evento o atributo.
{% endalert %}

### Lo que hay que saber

Cuando elimines datos personalizados, ten en cuenta los siguientes detalles:

* **La eliminación es permanente**. No se pueden recuperar los datos.
* Los datos se eliminan de la plataforma Braze y de los perfiles de usuario.
* Puedes "reutilizar" el nombre del atributo personalizado o el nombre del evento personalizado después de eliminarlo. Esto significa que si observas que los datos personalizados "reaparecen" en Braze después de eliminarlos, puede deberse a una integración que no se ha detenido y está enviando datos con el mismo nombre de datos personalizados.
* Puede que tengas que volver a bloquear un elemento si al borrarlo vuelven a aparecer datos personalizados. El estado de la lista de bloqueo no se conserva porque se han eliminado los datos personalizados.

## Forzar la comparación de tipos de datos

Braze reconoce automáticamente los tipos de datos de los atributos que se nos envían. Sin embargo, en el caso de que se apliquen varios tipos de datos a un mismo atributo, se puede forzar el tipo de datos de cualquier atributo para saber cuál es realmente. Selecciónalo en el desplegable de la columna **Tipo de datos**.

{% alert note %}
Forzar tipos de datos no se aplica a las propiedades del evento, ni a las propiedades de la compra.
{% endalert %}

![Desplegable de tipo de datos de atributos personalizados][75]

{% alert warning %}
Si eliges forzar el tipo de datos para un atributo, cualquier dato que entre que no sea del tipo especificado será ignorado.
{% endalert %}

### Coerción de tipos de datos

| Tipo de datos forzados | Descripción |
|------------------|-------------|
| Booleano | Las entradas de `1`, `true`, `t` (sin distinguir mayúsculas de minúsculas) se almacenarán como `true` |
| Booleano | Las entradas de `0`, `false`, `f` (sin distinguir mayúsculas de minúsculas) se almacenarán como `false` |
| Número | Los números enteros o flotantes (como `1`, `1.5`) se almacenarán como números |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para obtener más información sobre las opciones de filtrado específicas expuestas por las diferentes comparaciones de tipos de datos, consulte [Configuración de informes][43]. Y para más información sobre los distintos tipos de datos disponibles, consulta [Tipos de datos de atributos personalizados][44].

{% alert note %}
Los datos enviados a Braze son inmutables y no pueden borrarse ni modificarse después de que los hayamos recibido. Sin embargo, puede utilizar cualquiera de los pasos enumerados en las secciones anteriores para ejercer control sobre lo que está rastreando en su tablero.
{% endalert %}


[1]: {% image_buster/assets/img_archive/blocklist_warning.png %}
[20]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[21]: {% image_buster /assets/img_archive/prepopulate_page.png %}
[22]: {% image_buster /assets/img_archive/prepopulate_add.png %}
[43]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[44]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[73]: {% image_buster /assets/img_archive/manageproperties1.png %}
[75]: {% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %}
[88]: {{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection