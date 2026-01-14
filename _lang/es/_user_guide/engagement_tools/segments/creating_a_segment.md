---
nav_title: Crear un segmento
article_title: Crear un segmento
page_order: 0
page_type: tutorial
description: "Este artículo te mostrará cómo configurar y crear un segmento con Braze."
tool: Segments
search_rank: 3
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"} Crear un segmento

> La segmentación te permite dirigirte a los usuarios en función de sus características y acciones demográficas, de comportamiento o técnicas. El uso creativo e inteligente de la segmentación y la automatización de la mensajería te habilita para pasar fácilmente a tus usuarios del primer contacto al cliente a largo plazo. Los segmentos se actualizan en tiempo real a medida que cambian los datos, y puedes crear tantos segmentos como necesites para tus objetivos de segmentación y mensajería.

## Paso 1: Navega hasta la sección de segmentos

Ve a **Audiencia** > Segmentos.

## Paso 2: Nombra tu segmento

Selecciona **Crear segmento** para empezar a crear tu segmento. Nombra tu segmento describiendo el tipo de usuario por el que pretendes filtrar. Esto te ayudará a identificar el segmento cuando quieras segmentarlo para tus campañas o Lienzos. Los títulos imprecisos de los segmentos pueden resultar confusos.

Opcionalmente, puedes hacer lo siguiente:
- Añade una descripción al segmento para dar más detalles sobre la intención de esta audiencia y deja notas para que otros miembros del equipo puedan consultarlas.
- Añade un [equipo]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) a tu segmento.
- Añade [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) a tu segmento para organizarlo mejor.

\![Crear segmento modal en el que el segmento se denomina "Usuarios caducados" con la descripción del segmento "Este es nuestro segmento principal de usuarios caducados para dirigirnos a los no activos en los últimos catorce días" con dos botones: Cancelar y Crear segmento.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## Paso 3: Elige tu aplicación o plataforma

Elige a qué aplicaciones o plataformas quieres dirigirte seleccionando **Usuarios de todas las aplicaciones** (predeterminado) o **Usuarios de aplicaciones específicas**. **Los usuarios de aplicaciones específicas** se dirigen a usuarios con al menos una sesión en las aplicaciones especificadas.

Por ejemplo, si quieres enviar un mensaje dentro de la aplicación sólo a dispositivos iOS, selecciona tu aplicación iOS. Esto garantizará que los usuarios que puedan utilizar tanto un dispositivo iOS como Android sólo reciban el mensaje en su dispositivo iOS. En la lista de aplicaciones específicas, la opción **Usuarios de ninguna aplicación** te permite incluir usuarios sin sesiones ni datos de aplicación (normalmente creados mediante importación de usuarios o API REST).

\![Panel de detalles del segmento con la opción "Usuarios de todas las aplicaciones" seleccionada en la sección Aplicaciones utilizadas.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Paso 4: Añade filtros a tu segmento

Añade al menos un filtro a tu segmento. Puedes combinar tantos filtros como quieras para que tu segmentación sea más específica. 

{% alert note %}
Braze no genera perfiles para los usuarios hasta que han utilizado la aplicación por primera vez, por lo que no puedes dirigirte a usuarios que aún no han abierto tu aplicación.
{% endalert %}

#### Filtrar grupos

Los filtros se organizan en grupos de filtros. Cada filtro debe formar parte de un grupo de filtros que tenga como mínimo un filtro. Un segmento puede tener varios grupos de filtrado. Para añadir uno, selecciona **Añadir grupo de filtros**. Edita el nombre del grupo de filtros seleccionando el icono que aparece cuando pasas el ratón por encima.

Grupo filtrar con un icono de edición junto a su nombre.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Selecciona los iconos situados junto a cada filtro para contraer el editor de filtros o duplicar filtros individuales. Tras duplicar un filtro, puedes ajustar sus valores dentro de cada desplegable.

#### Lógica de segmentación mediante AND y OR

Dentro de un grupo de filtros, los filtros se pueden unir mediante "Y" u "O". Entre grupos de filtros, los grupos se pueden unir mediante "Y" u "O". Al utilizar grupos de filtrado, puedes crear lógicas de segmentación como las siguientes:
- (A Y B Y C) O (C Y E Y F)
- (A O B O C) Y (C O D O F)

Seleccionar "O" para tus filtros significa que tu segmento contendrá usuarios que satisfagan cualquier combinación de uno, algunos o todos esos filtros. Seleccionar "Y" significa que los usuarios que no pasen ese filtro no se incluirán en tu segmento.

{% alert tip %}
Cuando selecciones "O" para filtros que incluyan un filtro negativo (como "no está" en un grupo de suscripción), recuerda que los usuarios sólo tienen que cumplir uno de los filtros "O" para ser incluidos en el segmento. Para aplicar el filtro negativo independientemente de los demás filtros, utiliza un [grupo de exclusión](#exclusion).
{% endalert %}

{% details When to avoid the OR operator %}

Puede haber situaciones de selección de usuarios en las que deba evitarse utilizar el operador `OR`. El operador `OR` crea una sentencia que se evalúa como verdadera si un usuario cumple los criterios de uno o varios de los filtros de una sentencia. Por ejemplo, si quieres crear un segmento de usuarios que pertenezcan a "Foodies" pero que no pertenezcan ni a "Non-foodies" ni a "Candy-lovers", en este caso funcionaría el operador `OR`.

Filtrar grupo para usuarios del segmento "amantes de la comida" y no de los segmentos "no amantes de la comida" o "amantes de los dulces".]({% image_buster /assets/img_archive/or_operator_segment.png %})

Sin embargo, si tu objetivo es segmentar a usuarios que pertenezcan al segmento "Foodies" y no estén en ninguno de los segmentos "Non-foodies" y "Candy-lovers", entonces utiliza el operador `AND`. De este modo, los usuarios que reciben la campaña o el Canvas están en el segmento previsto ("foodies") y no en los otros segmentos ("Non-foodies" y "Candy-lovers") al mismo tiempo. 

Los siguientes criterios negativos de selección no deben utilizarse con el operador `OR` cuando dos o más filtros hagan referencia al mismo atributo:

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

Si `not included`, `is not`, `does not equal`, o `does not match regex` se utilizan con el operador `OR` dos o más veces en una frase, se seleccionarán los usuarios con todos los valores del atributo correspondiente.

{% enddetails %}

#### Operadores de filtrado

Dependiendo del filtro concreto que selecciones, dispondrás de distintos operadores para identificar los valores del filtro. Para profundizar en los operadores disponibles para los distintos tipos de atributos personalizados, consulta [Almacenamiento de atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes). Ten en cuenta que al utilizar el operador "es cualquiera de", el número máximo de elementos que puedes incluir en ese campo es 256.

{% alert note %}
Braze no genera perfiles para los usuarios hasta que han utilizado la aplicación por primera vez, por lo que no puedes dirigirte a usuarios que aún no han abierto tu aplicación.
{% endalert %}

\![El segmentador filtra los grupos con el operador AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Los segmentos que ya utilizan el filtro **Pertenencia a segmento** no pueden incluirse ni anidarse en otros segmentos. Esto evita un ciclo en el que el segmento A incluye al segmento B, que a su vez intenta incluir de nuevo al segmento A. Si eso ocurriera, el segmento seguiría haciendo referencia a sí mismo, haciendo imposible calcular quién pertenece realmente a él.

Además, anidar segmentos de este modo añade complejidad y puede ralentizar las cosas. En su lugar, recrea el segmento que intentas incluir utilizando los mismos filtros.
{% endalert %}

#### Grupos de exclusión (opcional) {#exclusion}

Al crear un segmento, puedes aplicar uno o varios grupos de exclusión. Los grupos de exclusión contienen criterios que identifican a los usuarios que debes excluir de tu segmento, y siempre estarán conectados a tus grupos de filtrado con un operador "Y NO".

Los grupos de exclusión anulan los criterios de segmentación. Si un usuario entra dentro de los criterios de tu grupo de exclusión, no formará parte de tu segmento, aunque cumpla los criterios de tus grupos de filtrado.

Crea un grupo de exclusión añadiendo filtros como harías con los grupos de filtros. La estadística _Usuarios alcanzables estimados_ en un grupo de exclusión muestra el número estimado de usuarios que quedan en tu segmento después de aplicar los criterios de exclusión.

Los usuarios excluidos no se contabilizarán en la estadística _Total de usuarios accesibles_ de tu segmento.

Un grupo de exclusión con dos filtros.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

#### Visualización de las estadísticas del embudo

Selecciona **Ver estadísticas del embudo** para mostrar las estadísticas de ese grupo de filtros y ver cómo afecta cada filtro añadido a tus estadísticas de segmento. Verás un recuento estimado y el porcentaje de usuarios a los que se dirigen todos los filtros hasta ese momento. Una vez mostradas las estadísticas de un grupo de filtros, se actualizarán automáticamente cada vez que cambies los filtros. Estas estadísticas son estimadas y pueden tardar un momento en generarse.

Ten en cuenta que si utilizas AND entre tus filtros, las estadísticas del embudo disminuirán; si utilizas OR entre tus filtros, las estadísticas del embudo aumentarán.

\![Dos filtros con estadísticas de embudo de segmento.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

Si añades filtros que documenten tu flujo de usuarios, podrás ver los puntos en los que los usuarios se caen. Por ejemplo, si tienes una aplicación de redes sociales y quieres ver dónde puedes estar perdiendo usuarios durante tu proceso de incorporación, quizá quieras añadir filtros de datos personalizados para registrarte, añadir amigos y enviar el primer mensaje. Si descubres que el 85% de los usuarios se registra y añade amigos, pero sólo el 45% envía el primer mensaje, sabrás que debes centrarte en fomentar más envíos de mensajes durante tus campañas de incorporación y de mensajería.

#### Segmentos de prueba

Después de añadir aplicaciones y filtros a tu segmento, puedes probar si tu segmento está configurado como esperabas buscando a un usuario para confirmar si coincide con los criterios del segmento. Para ello, busca la dirección `external_id` o `braze_id` de un usuario en la sección **Búsqueda de usuarios**. Ten en cuenta que no puedes buscar por dirección de correo electrónico en **la Búsqueda de usuarios**.

Sección de búsqueda de usuarios con un campo de búsqueda.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

La búsqueda de usuarios está disponible cuando:
- Crear un segmento
- Configurar una campaña o una audiencia de Canvas
- Paso de configuración de las rutas de audiencia

Cuando un usuario coincida con los criterios de segmento, filtrar y aplicación, una alerta lo indicará.

Una búsqueda de usuario "usuarioprueba" desencadena una alerta que dice: "usuarioprueba coincide con todos los segmentos, filtros y aplicaciones".]({% image_buster /assets/img_archive/user_lookup_match.png %})

Cuando un usuario no coincide en parte o en su totalidad con los criterios del segmento, filtro o aplicación, se enumeran los criterios que faltan para la solución de problemas.

Una búsqueda de usuario con una alerta que dice: "prueba1 no coincide con los siguientes criterios de selección:" y muestra los criterios que faltan.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

#### Segmentos de usuario único

Puedes crear segmentos de usuarios únicos (o segmentos de un puñado de usuarios) utilizando atributos únicos que identifiquen a los usuarios, como un nombre de usuario o un ID de usuario.

Sin embargo, es posible que las estadísticas de segmentación o la vista previa no muestren a este usuario individual porque las estadísticas de segmento se calculan a partir de una muestra aleatoria con un intervalo de confianza del 95% de que el resultado está dentro de +/- 1%. Cuanto mayor sea tu base de usuarios, más probable es que el tamaño de tu segmento sea una estimación aproximada. Para asegurarte de que tu segmento contiene al único usuario al que te diriges, selecciona **Calcular estadísticas exactas**. Esto calculará el número exacto de usuarios de tu segmento con una precisión superior al 99,999%.

Braze tiene filtros de prueba para dirigirse a usuarios específicos por ID de usuario o dirección de correo electrónico.

## Paso 5: Guarda tu segmento

Selecciona **Guardar**. ¡Ahora ya puedes empezar a enviar mensajes a tus usuarios!

## Medición del tamaño del segmento

Para saber cómo controlar la composición y el tamaño de tu segmento, consulta [Medir el tamaño del segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

## Segmentos de archivo

Si ya no necesitas o deseas retirar un segmento concreto, puedes archivarlo yendo a la página **Segmentos** y seleccionando **Archivar** en el menú de la fila de ese segmento.

{% alert warning %}
Cuando archives un segmento, también se archivarán todas las campañas o Canvas que lo utilicen (aunque el segmento sólo se utilice en un único componente de Canvas). Esto también incluye los segmentos anidados, en los que también se archivarán tanto los segmentos como cualquier campaña o Lienzo que los utilice.
<br><br>
Recibirás una advertencia que te indicará qué campañas y Lienzos están a punto de ser archivados al archivar el segmento asociado.
{% endalert %}

Puedes desarchivar el segmento navegando hasta él en la página **Segmentos** y seleccionando **Desarchivar**.

## Dirigir el comportamiento cuando los usuarios tienen varios dispositivos

Los usuarios tienen más de un dispositivo si acceden a la misma cuenta en varios dispositivos. Puedes buscar varios dispositivos en la sección **Dispositivos recientes** de un [perfil de usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/).

Al segmentar con filtros dependientes del dispositivo (modelo de dispositivo, SO del dispositivo y versión de la aplicación), tu segmento contendrá a todos los usuarios que coincidan con tus criterios de filtrado. A estos usuarios se les enviará un mensaje a todos sus dispositivos, incluidos aquellos que no cumplan tus criterios de filtrado. Por ejemplo, supongamos que el usuario A tiene dos dispositivos: El dispositivo 1 tiene el SO 13.0, y el dispositivo 2 tiene el SO 10.0. Si un segmento se dirige a usuarios con OS 10.0, este usuario formará parte de ese segmento y recibirá mensajes en sus dos dispositivos.

### Notificaciones push

Puedes especificar que sólo se envíe una notificación push a cada usuario. Cuando [redactes tu mensaje]({{ssite.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-4-compose-your-push-message), selecciona **Sólo enviar al último dispositivo utilizado por el usuario** en **Configuración adicional**.

\!["Configuración adicional" con una casilla de verificación para que sólo se envíe al último dispositivo utilizado por el usuario.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Consideraciones

- **Los mensajes enviados pueden superar el tamaño de la audiencia.** Cuando algunos usuarios tienen más de un dispositivo, cada dispositivo puede recibir un mensaje. Esto provoca un mayor número de envíos de mensajes que los usuarios de tu segmento.
- **La pertenencia a un segmento de un usuario puede no tener el aspecto que esperas.**
    - Un usuario puede ser seleccionado en su dispositivo actual basándose en atributos asociados a un dispositivo diferente. Si no esperabas que un usuario recibiera un mensaje, comprueba su perfil de usuario en varios dispositivos.
    - Un usuario puede haber estado en tu segmento objetivo en el momento del envío, pero debido a comportamientos asociados a cualquiera de sus dispositivos, puede no formar parte de ese segmento después. Esto puede dar lugar a que un usuario reciba una campaña o Canvas aunque actualmente no coincida con los criterios de filtrado. <br><br>Por ejemplo, un usuario podría recibir un mensaje dirigido a usuarios con una versión de aplicación más reciente de OS 10.0 aunque actualmente tengan OS 13.0. En este caso, el usuario tenía el SO 10.0 cuando se envió el mensaje y se actualizó al SO 13.0 después.<br><br> Del mismo modo, si un usuario utiliza posteriormente un dispositivo con una versión de aplicación diferente, su perfil de usuario se actualizará con la nueva versión más reciente de la aplicación. Esto puede hacer que parezca que el usuario no debería haber cumplido los requisitos para recibir el mensaje, aunque los cumpliera cuando se envió.


