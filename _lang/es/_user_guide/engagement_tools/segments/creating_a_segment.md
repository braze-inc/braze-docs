---
nav_title: Creación de un segmento
article_title: Creación de un segmento
page_order: 0
page_type: tutorial
description: "Este artículo explica cómo configurar y crear un segmento con Braze."
tool: Segments
search_rank: 3
---

# [![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Creación de un segmento

> La segmentación le permite dirigirse a los usuarios en función de sus características y acciones demográficas, de comportamiento o técnicas. El uso creativo e inteligente de la segmentación y la automatización de la mensajería le permite hacer que sus usuarios pasen sin problemas del primer contacto al cliente a largo plazo. Los segmentos se actualizan en tiempo real a medida que cambian los datos, y usted puede crear tantos segmentos como necesite para sus fines de segmentación y mensajería.

## Paso 1: Navegue hasta la sección de segmentos

Vaya a **Audiencia** > **Segmentos**.

## Paso 2: Nombra tu segmento

Seleccione **Crear segmento** para empezar a crear su segmento. Nombre su segmento describiendo el tipo de usuario por el que pretende filtrar. Esto le ayudará a identificar el segmento cuando quiera dirigirlo a sus campañas o Canvases. Los títulos imprecisos de los segmentos pueden confundir.

Opcionalmente, puedes hacer lo siguiente:
- Añada una descripción al segmento para ofrecer más detalles sobre la intención de este público y deje notas para que otros miembros del equipo puedan consultarlas.
- Añade un [equipo]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) a tu segmento.
- Añade [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) a tu segmento para organizarlo mejor.

![Crear Segmento modal donde el segmento se llama "Usuarios Caducados" con la Descripción del Segmento como "Este es nuestro segmento principal de Usuarios Caducados para dirigirnos a los no activos en los últimos catorce días" con dos botones: Cancelar y crear segmento.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## Paso 3: Elija su aplicación o plataforma

Elige a qué aplicaciones o plataformas deseas dirigirte seleccionando **Usuarios de todas las aplicaciones** (por defecto) o **Usuarios de aplicaciones específicas**. Si selecciona **Usuarios de todas las aplicaciones**, el segmento incluye a todos los usuarios independientemente de cualquier dato de sesión o aplicación. Si eliges **Usuarios de aplicaciones específicas**, puedes seleccionar qué aplicaciones o plataformas quieres incluir en tu segmento.

Por ejemplo, si quieres enviar un mensaje dentro de la aplicación solo a dispositivos iOS, selecciona tu aplicación iOS. De este modo, los usuarios que utilicen tanto un dispositivo iOS como Android sólo recibirán el mensaje en su dispositivo iOS. En la lista de aplicaciones específicas, la opción **Usuarios sin aplicaciones** permite incluir usuarios sin sesiones y sin datos de aplicaciones (normalmente creados mediante importación de usuarios o API REST).

![Panel de detalles del segmento con la opción "Usuarios de todas las aplicaciones" seleccionada en la sección Aplicaciones utilizadas.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Paso 4: Añade filtros a tu segmento

Añade al menos un filtro a tu segmento. Puede combinar tantos filtros como desee para que su segmentación sea más específica.

{% alert note %}
Braze no genera perfiles para los usuarios hasta que han utilizado la aplicación por primera vez, por lo que no puedes dirigirte a usuarios que aún no han abierto tu aplicación.
{% endalert %}

#### Filtrar grupos

Los filtros se organizan en grupos de filtros. Cada filtro debe formar parte de un grupo de filtros que tenga como mínimo un filtro. Un segmento puede tener varios grupos de filtros. Para añadir uno, seleccione **Añadir grupo de filtros**. Edite el nombre del grupo de filtros seleccionando el icono que aparece al pasar el ratón junto a él.

![Filtrar grupo con un icono de edición junto a su nombre.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Selecciona los iconos situados junto a cada filtro para contraer el editor de filtros o duplicar filtros individuales. Después de duplicar un filtro, puede ajustar sus valores dentro de cada desplegable.

#### Lógica de segmentación mediante AND y OR

Dentro de un grupo de filtros, los filtros pueden unirse mediante "Y" u "O". Entre grupos de filtros, los grupos pueden unirse mediante "Y" u "O". Al utilizar grupos de filtros, puede crear lógicas de segmentación como:
- (A Y B Y C) O (C Y E Y F)
- (A O B O C) Y (C O D O F)

Si selecciona "O" para sus filtros, su segmento contendrá usuarios que satisfagan cualquier combinación de uno, algunos o todos esos filtros. Seleccionar "Y" significa que los usuarios que no pasen ese filtro no se incluirán en su segmento.

{% alert tip %}
Cuando seleccione "O" para filtros que incluyan un filtro negativo (como "no está" en un grupo de suscripción), recuerde que los usuarios sólo necesitan cumplir uno de los filtros "O" para ser incluidos en el segmento. Para aplicar el filtro negativo independientemente de los demás filtros, utilice un [grupo de exclusión](#exclusion).
{% endalert %}

#### Operadores de filtrado

Dependiendo del filtro específico que seleccione, dispondrá de distintos operadores para identificar los valores del filtro. Para profundizar en los operadores disponibles para los distintos tipos de atributos personalizados, consulte [Almacenamiento de atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes). Tenga en cuenta que al utilizar el operador "es cualquiera de", el número máximo de elementos que puede incluir en ese campo es 256.

{% alert note %}
Braze no genera perfiles para los usuarios hasta que han utilizado la aplicación por primera vez, por lo que no puedes dirigirte a usuarios que aún no han abierto tu aplicación.
{% endalert %}

![El segmentador filtra los grupos con el operador AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Los segmentos que ya utilizan el filtro **Pertenencia a segmento** no pueden incluirse ni anidarse en otros segmentos. Esto evita un ciclo en el que el segmento A incluye al segmento B, que a su vez intenta incluir de nuevo al segmento A. Si eso ocurriera, el segmento seguiría haciendo referencia a sí mismo, haciendo imposible calcular quién pertenece realmente a él.

Además, anidar segmentos de este modo añade complejidad y puede ralentizar las cosas. En su lugar, recrea el segmento que intentas incluir utilizando los mismos filtros.
{% endalert %}

#### Grupos de exclusión (opcional) {#exclusion}

Al crear un segmento, puede aplicar uno o varios grupos de exclusión. Los grupos de exclusión contienen criterios que identifican a los usuarios a excluir de su segmento, y siempre estarán conectados a sus grupos de filtros con un operador "Y NO".

Los grupos de exclusión anulan los criterios de segmento. Si un usuario entra dentro de los criterios de su grupo de exclusión, no formará parte de su segmento, aunque cumpla los criterios de sus grupos de filtrado.

Cree un grupo de exclusión añadiendo filtros como lo haría para los grupos de filtros. La estadística _Usuarios alcanzables estimados_ en un grupo de exclusión muestra el número estimado de usuarios que quedan en su segmento después de aplicar los criterios de exclusión.

Los usuarios excluidos no se contabilizarán en la estadística _Total de usuarios accesibles_ de su segmento.

![Un grupo de exclusión con dos filtros.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

#### Segmentos de prueba

Después de añadir aplicaciones y filtros a su segmento, puede probar si su segmento está configurado como se esperaba buscando un usuario para confirmar si coincide con los criterios del segmento. Para ello, busque la dirección `external_id` o `braze_id` de un usuario en la sección **Búsqueda de usuarios**.

![Sección de búsqueda de usuarios con un campo de búsqueda.]({% image_buster /assets/img_archive/user_lookup.png %})

La búsqueda de usuarios está disponible cuando:
- Crear un segmento
- Configurar una campaña o un público de Canvas
- Configuración del paso de rutas de audiencia

Cuando un usuario coincida con los criterios de segmento, filtro y aplicación, se emitirá una alerta.

![Una búsqueda de usuario "usuarioprueba" desencadena una alerta que dice: "usuarioprueba coincide con todos los segmentos, filtros y aplicaciones.]({% image_buster /assets/img_archive/user_lookup_match.png %})

Cuando un usuario no coincide con parte o la totalidad de los criterios de segmento, filtro o aplicación, los criterios que faltan se enumeran a efectos de resolución de problemas.

![Una búsqueda de usuario con una alerta que dice: "test1 no coincide con los siguientes criterios de selección:" y muestra los criterios que faltan.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

#### Segmentos de usuario único

Puede crear segmentos de usuarios individuales (o segmentos de un puñado de usuarios) utilizando atributos únicos que identifiquen a los usuarios, como un nombre de usuario o un ID de usuario.

Sin embargo, es posible que las estadísticas de segmentación o la vista previa no muestren este usuario individual porque las estadísticas de segmento se calculan a partir de una muestra aleatoria con un intervalo de confianza del 95% en el que el resultado está dentro de +/- 1%. Cuanto mayor sea su base de usuarios, más probable es que el tamaño de su segmento sea una estimación aproximada. Para asegurarse de que su segmento contiene el único usuario al que se dirige, seleccione **Calcular estadísticas exactas**. Esto calculará el número exacto de usuarios de su segmento con una precisión superior al 99,999%.

Braze dispone de filtros de prueba para dirigirse a usuarios específicos por ID de usuario o dirección de correo electrónico.

## Paso 5: Guarda tu segmento

Seleccione **Guardar**. Ya puedes empezar a enviar mensajes a tus usuarios.

## Medición del tamaño del segmento

Para saber cómo controlar la composición y el tamaño de tu segmento, consulta [Medir el tamaño del segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

## Archivar segmentos

Si ya no necesita o desea retirar un segmento concreto, puede archivarlo accediendo a la página **Segmentos** y seleccionando **Archivar** en el menú de la fila de ese segmento.

{% alert warning %}
Al archivar un segmento, también se archivarán todas las campañas o lienzos que lo utilicen (aunque el segmento sólo se utilice en un único componente del lienzo). Esto también incluye los segmentos anidados, en los que tanto los segmentos como las campañas o lienzos que los utilicen también se archivarán.
<br><br>
Recibirá un aviso que le indicará qué campañas y lienzos están a punto de ser archivados al archivar el segmento asociado.
{% endalert %}

Para desarchivar un segmento, vaya a la página **Segmentos** y seleccione **Desarchivar**.

## Dirigir el comportamiento cuando los usuarios tienen varios dispositivos

Los usuarios tienen más de un dispositivo si se conectan a la misma cuenta en varios dispositivos. Puede comprobar si hay varios dispositivos en la sección **Dispositivos recientes** del [perfil de un usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/).

Al segmentar con filtros dependientes del dispositivo (modelo de dispositivo, sistema operativo del dispositivo y versión de la aplicación), el segmento contendrá todos los usuarios que coincidan con los criterios de filtrado. Estos usuarios recibirán un mensaje en todos sus dispositivos, incluidos aquellos que no cumplan tus criterios de filtrado. Por ejemplo, supongamos que el usuario A tiene dos dispositivos: El dispositivo 1 tiene el SO 13.0, y el dispositivo 2 tiene el SO 10.0. Si un segmento se dirige a usuarios con OS 10.0, este usuario formará parte de ese segmento y recibirá mensajes en sus dos dispositivos.

### Notificaciones push

Puede especificar que sólo se envíe una notificación push a cada usuario. Al [redactar el mensaje]({{ssite.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-4-compose-your-push-message), seleccione **Sólo enviar al último dispositivo utilizado por el usuario** en **Configuración adicional**.

!["Configuración adicional" con una casilla de verificación para que sólo se envíe al último dispositivo utilizado por el usuario.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Consideraciones

- **Los mensajes enviados pueden superar el tamaño de la audiencia.** Cuando algunos usuarios tienen más de un dispositivo, cada uno de ellos puede recibir un mensaje. Esto provoca un mayor número de envíos de mensajes que los usuarios de su segmento.
- **Es posible que la pertenencia a un segmento de un usuario no tenga el aspecto que cabría esperar.**
    - Un usuario puede ser seleccionado en su dispositivo actual basándose en atributos asociados a un dispositivo diferente. Si no esperabas que un usuario recibiera un mensaje, comprueba si hay varios dispositivos en su perfil de usuario.
    - Un usuario puede haber estado en su segmento objetivo en el momento del envío, pero debido a comportamientos asociados a cualquiera de sus dispositivos, puede no formar parte de ese segmento después. Esto puede dar lugar a que un usuario reciba una campaña o un Canvas aunque en ese momento no coincida con los criterios de filtrado. <br><br>Por ejemplo, un usuario podría recibir un mensaje dirigido a usuarios con una versión de aplicación más reciente de SO 10.0 aunque actualmente tengan SO 13.0. En este caso, el usuario tenía el SO 10.0 cuando se envió el mensaje y después actualizó a SO 13.0.<br><br> Del mismo modo, si un usuario utiliza más tarde un dispositivo con una versión diferente de la aplicación, su perfil de usuario se actualizará con la nueva versión más reciente de la aplicación. Esto puede hacer que parezca que el usuario no debería haber cumplido los requisitos para recibir el mensaje, aunque los cumpliera cuando se envió.


