---
nav_title: Crear una tarjeta de contenido
article_title: Crear una tarjeta de contenido
page_order: 0
description: "Este artículo de referencia explica cómo crear, componer, configurar y enviar tarjetas de contenido utilizando campañas y lienzos Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Crear una tarjeta de contenido

> Este artículo explica cómo crear una tarjeta de contenido en Braze cuando construyes campañas y lienzos. Aquí te guiaremos para que elijas un tipo de mensajería, compongas tu tarjeta y programes la entrega de tu mensaje.

## Paso 1: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse con una campaña o con un Canvas? Las campañas son mejores para campañas de mensajería únicas y sencillas (como informar a los usuarios sobre un nuevo producto con un solo mensaje), mientras que los Canvases son mejores para recorridos de usuario de varios pasos (como enviar sugerencias de productos personalizadas basadas en el comportamiento del usuario a lo largo del tiempo).

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Selecciona **Tarjetas de contenido** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3. Pon a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por las etiquetas correspondientes.
5. Añade y nombra tantas variantes como quieras para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de tus variantes añadidas. Para saber más sobre las variantes, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o van a tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. A continuación, puedes seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en Mensaje en el constructor de Canvas. Nombra tu paso con algo claro y significativo.
3. Selecciona **Tarjetas de contenido** como canal de mensajería.
4. Elige cuándo calcula Braze la elegibilidad de la audiencia y la personalización de la tarjeta de contenido. Puede ser a la entrada o en la primera impresión (recomendado). Los pasos que contienen tarjetas de contenido pueden programarse o basarse en acciones.
5. Elige si quieres eliminar las tarjetas de contenido cuando los usuarios completen una compra o realicen un evento personalizado.
6. Establece una caducidad para la tarjeta de contenido (tiempo en la fuente). Puede ser al cabo de un tiempo o a una hora determinada.
7. Filtra tu audiencia, o los destinatarios, para este paso según sea necesario en la **Configuración de entrega**. Puedes refinar aún más tu audiencia especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso, en el momento en que se envíen los mensajes.
8. Elige cualquier otro canal de mensajería que quieras asociar a tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Especifica tus tipos de mensajes

Selecciona uno de los tres tipos esenciales de tarjeta de contenido: **Clásico**, **Imagen con subtítulos** y **Sólo imagen**. 

Para saber más sobre el comportamiento esperado y el aspecto de cada tipo, consulta [Detalles creativos]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/), o echa un vistazo a los enlaces de la siguiente tabla. Estos tipos de tarjeta de contenido son aceptados tanto por aplicaciones móviles como por aplicaciones Web.

| Tipo de mensaje | Ejemplo | Descripción |
|---|---|---|
|[Clásico]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| \![Una tarjeta de contenido clásica con un pequeño icono y texto para animar a reservar una clase de entrenamiento.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |La tarjeta Clásica tiene un diseño sencillo con un título en negrita, el texto del mensaje y una imagen opcional a la izquierda del título y el texto. Es mejor utilizar una imagen cuadrada o un icono con la Tarjeta Clásica. |
|[Imagen subtitulada]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| Una tarjeta de contenido subtitulada con una imagen de un levantador de pesas y texto para animar a reservar una clase de entrenamiento.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | La tarjeta de imagen subtitulada muestra tu contenido con un texto y una imagen llamativa. |
|[Sólo imagen]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| \![Una tarjeta de contenido de sólo imagen con sólo texto.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | La tarjeta "Sólo imagen" llama la atención con espacio para imágenes, GIF y otros contenidos creativos no textuales. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Paso 3: Componer una tarjeta de contenido

Puedes editar todos los aspectos del contenido y comportamiento de tu mensaje en la pestaña **Redactar** del editor de mensajes.

\![Muestra los detalles de la tarjeta de contenido en la pestaña Redactar del editor de mensajes.]({% image_buster /assets/img/content_card_compose.png %})

El contenido aquí varía en función del **Tipo de Tarjeta** elegido en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

#### Lengua

Selecciona **Añadir idiomas** para añadir los idiomas que desees de la lista proporcionada. Esto insertará [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) en tu mensaje. Te recomendamos que selecciones tus idiomas antes de escribir el contenido, para que puedas rellenar el texto donde corresponda en el Liquid. Para consultar nuestra lista completa de idiomas disponibles que puedes utilizar, consulta [Idiomas admitidos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

\![Una ventana con el inglés, el español y el francés seleccionados para los idiomas, y el título, la descripción y el texto del enlace seleccionados para los campos a internacionalizar.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Crear mensajes de derecha a izquierda

El aspecto final de los mensajes de derecha a izquierda depende en gran medida de cómo los presten los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha [a]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Título y mensaje

Escribe lo que quieras. No hay límites, pero cuanto más rápido transmitas tu mensaje y consigas que tu cliente haga clic, ¡mejor! Recomendamos títulos y contenidos de mensaje claros y concisos. Ten en cuenta que estos campos no se proporcionan para las tarjetas de sólo imagen.

#### Imagen

Añade una imagen a tu tarjeta de contenido seleccionando **Añadir imagen** o proporcionando una URL de la imagen. Al seleccionar **Añadir imagen** se abre la **biblioteca multimedia**, donde puedes seleccionar una imagen cargada previamente o añadir una nueva. Cada tipo de mensaje y plataforma puede tener sus propias proporciones y requisitos sugeridos, así que asegúrate de comprobar cuáles son antes de encargar o hacer una imagen desde cero. Ten en cuenta que los campos de mensaje de la tarjeta de contenido están limitados a 2 KB de tamaño total.

#### Pin arriba

Una tarjeta anclada se mostrará en la parte superior de la fuente de un usuario y no podrá ser descartada por el usuario. Si hay más de una tarjeta anclada en la fuente de un usuario, las tarjetas ancladas se mostrarán en orden cronológico. Después de enviar una tarjeta, no puedes actualizar retroactivamente su opción anclada. Cambiar esta opción después de haber enviado una campaña sólo afectará a futuros envíos.

Vista previa de la tarjeta de contenido en Braze para móvil y Web con la opción "Anclar esta tarjeta a la parte superior de la fuente" seleccionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportamiento al hacer clic

Cuando tu cliente hace clic en un enlace presentado en la tarjeta, tu enlace puede llevarle más adentro de tu aplicación o a otro sitio. Si eliges un comportamiento de "al hacer clic" para tu tarjeta de contenido, recuerda actualizar tu **Texto de enlace** en consecuencia.

Las siguientes acciones están disponibles para los enlaces de la tarjeta de contenido:

| Acción | Descripción |
|---|---|
| Redirigir a URL Web | Abre una página Web no nativa. |
| [Enlace profundo a la aplicación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Vincula en profundidad una pantalla existente en tu aplicación. |
| Registrar evento personalizado | Elige un [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) para desencadenar. Puede utilizarse para mostrar otra tarjeta de contenido o desencadenar mensajería adicional. |
| Atributo personalizado de registro | Elige un [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) para el usuario actual. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Las opciones **Registrar evento personalizado** y **Registrar atributo** personalizado requieren la compatibilidad con la siguiente versión del SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Paso 4: Configurar ajustes adicionales (opcional)

Puedes utilizar [pares clave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para crear categorías para tus tarjetas, crear [múltiples fuentes de tarjetas de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) y personalizar cómo se ordenan las tarjetas.

Para añadir **pares** clave-valor a tu mensaje, ve a la pestaña **Configuración** y selecciona **Añadir nuevo par**.

## Paso 5: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

Construye el resto de tu campaña. Continúa en las siguientes secciones para obtener más detalles sobre cómo utilizar mejor nuestras herramientas para crear tarjetas de contenido.

#### Elige un programa o desencadenante de entrega

Las tarjetas de contenido pueden entregarse en función de una hora programada, una acción o un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

También puedes establecer la duración de la campaña y [las horas tranquilas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) y determinar la caducidad de la tarjeta de contenido. Establece una fecha de caducidad específica o los días que faltan para que caduque una tarjeta, hasta 30 días. Todas las variantes tienen fechas de caducidad idénticas.

{% alert note %}
La limitación de frecuencia no se aplica a las tarjetas de contenido.
{% endalert %}

##### Entrega programada

Para las campañas de tarjeta de contenido con entrega programada, puedes elegir cuándo Braze evalúa la elegibilidad de la audiencia y la personalización para las nuevas campañas de tarjeta de contenido especificando cuándo se crea la tarjeta. Para más información, consulta la [creación de tarjetas]({{site.baseurl}}/card_creation).

#### Elige los usuarios a los que dirigirte

A continuación, [dirígete a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. Automáticamente recibirás una vista previa de cómo es la población aproximada de ese segmento en este momento. Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

{% multi_lang_include target_audiences.md %}

#### Elige eventos de conversión

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar [pruebas multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) e [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), y mucho más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación sobre Canvas.

{% endtab %}
{% endtabs %}

## Paso 6: Revisar y desplegar

Cuando hayas terminado de construir lo último de tu campaña o Canvas, revisa sus detalles, [pruébala]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/) y envíala cuando estés listo.

{% alert warning %}
Una vez lanzada una tarjeta de contenido, no se puede editar. Sólo se puede impedir el envío a nuevos usuarios y eliminarlo de las fuentes de los usuarios. Consulta [Actualizar tarjetas enviadas]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards) para entender cómo puedes enfocar este escenario.
{% endalert %}

A continuación, consulta [los informes de la tarjeta]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) de contenido para saber cómo puedes acceder a los resultados de tus campañas con la tarjeta de contenido.

## Lo que debes saber

### Limitaciones de tamaño para las tarjetas de contenido

El tamaño de la carga útil de una tarjeta de contenido puede ser de hasta 2 KB tras la renderización de Liquid. Esto incluye el **Título**, el **Mensaje**, la **URL de la imagen**, el **Texto del enlace**, la **(s) URL del enlace** y **los Pares clave-valor** (nombres y valores). Sin embargo, este límite no incluye el tamaño de la imagen, sólo la longitud de la URL de la imagen.

{% alert important %}
No se enviarán mensajes de más de 2 KB. Durante los envíos de prueba, las tarjetas de contenido que superen los 2 KB pueden seguir entregándose y mostrándose correctamente.
{% endalert %}

### Número de tarjetas en la fuente

Cada usuario puede tener hasta 250 tarjetas de contenido no caducadas en su fuente en un momento dado. Cuando se supere este límite, Braze dejará de devolver las tarjetas más antiguas, aunque no se hayan leído. Las tarjetas descartadas también cuentan para este límite, lo que significa que un número elevado de tarjetas descartadas puede reducir el espacio disponible para las nuevas.

### Comportamiento de envío

Una vez enviadas las tarjetas de contenido, quedan en espera en un "buzón de entrada" listas para ser entregadas al usuario (de forma similar a lo que ocurre con los correos electrónicos). Después de introducir el contenido en la tarjeta de contenido (en el momento de la visualización), no se puede cambiar durante su vida útil. Esto se aplica incluso si estás llamando a una API a través de Contenido conectado, y los datos del punto final cambian. Estos datos no se actualizarán. Sólo se puede impedir el envío a nuevos usuarios y eliminarlo de las fuentes de los usuarios. Si modificas una campaña, sólo las futuras tarjetas que se envíen tendrán la actualización.

Si necesitas eliminar tarjetas antiguas, primero debes detener la campaña. Para detener una campaña, abre tu campaña de tarjeta de contenido y selecciona **Detener campaña**. Si detienes la campaña, deberás decidir cómo tratar a los usuarios que ya hayan recibido tu tarjeta. 

Si quieres eliminar la tarjeta de contenido de las fuentes de tus usuarios, selecciona **Eliminar tarjeta de la fuente**. El SDK ocultará la tarjeta en la siguiente sincronización.

\![Diálogo para confirmar la desactivación de la tarjeta de contenido]({% image_buster /assets/img/cc_remove.png %}){: style="max-width:75%" }

{% alert tip %}
¿Quieres que tu contenido dure más de 30 días? Prueba [los Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

### Eventos de retirada de tarjetas {#action-based-card-removal}

Algunas tarjetas de contenido sólo son relevantes hasta que el usuario realiza alguna acción. Por ejemplo, una tarjeta que inste a los usuarios a activar su cuenta no debería mostrarse después de que el usuario complete esa tarea de incorporación.

Dentro de una campaña o mensaje Canvas, puedes añadir opcionalmente un **Evento de eliminación** para especificar qué eventos personalizados o compras deben hacer que las tarjetas enviadas previamente se eliminen de la fuente de ese usuario, desencadenado por el SDK o la API REST.

Las tarjetas se eliminarán en las siguientes actualizaciones, una vez que Braze haya procesado el evento especificado.

{% alert tip %}
Puedes especificar varios eventos personalizados y compras que deben eliminar una tarjeta de la fuente de un usuario. Cuando el usuario realice **cualquiera** de esas acciones, se eliminarán todas las tarjetas existentes enviadas por las tarjetas de la campaña. Las futuras tarjetas elegibles seguirán enviándose según la programación del mensaje.
{% endalert %}

\![Panel de Condiciones de Eliminación de la Tarjeta de Contenido con la opción Evento de Eliminación de la Tarjeta de Contenido.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### Actualización de tarjetas lanzadas

Las tarjetas de contenido no se pueden editar una vez enviadas. Si necesitas hacer cambios en tarjetas que ya han sido enviadas, considera la posibilidad de [volver a ser elegible para la campaña]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/), como se muestra en las siguientes opciones.

{% alert note %}
Cuando una tarjeta de contenido vuelve a ser elegible, puede enviarse de nuevo cuando la tarjeta original aún está en la aplicación de un usuario. Para evitar la duplicación de tarjetas en la aplicación de un usuario, puedes desactivar la reelegibilidad o ampliar la ventana de reelegibilidad para que no se envíe a los usuarios una nueva tarjeta hasta que la original haya caducado.
{% endalert %}

Ten en cuenta también que las tarjetas de contenido que se utilizan [en la primera impresión]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) utilizan el tiempo de impresión para calcular la nueva elegibilidad. Sin embargo, las tarjetas de contenido creadas en el lanzamiento de la campaña o en la entrada en Canvas utilizan la hora de envío o de impresión que sea más tardía.

#### Opción 1: Duplicar la campaña

Un método consiste en archivar la campaña y eliminar las tarjetas activas de la fuente. Luego puedes duplicar la campaña y lanzarla con actualizaciones para que todos los usuarios elegibles reciban las tarjetas actualizadas.

* Si los usuarios no deben volver a ser elegibles para una tarjeta de contenido, puedes filtrar a los usuarios que no hayan recibido la versión anterior de la tarjeta de contenido configurando el filtro `Received Message from Campaign` a la condición de `Has Not`.
* Si los usuarios que recibieron la tarjeta anterior deben volver a ser elegibles en X días, puedes configurar el filtro para `Last Received Message from specific campaign` a más de X días atrás **O** `Received Message from Campaign` con la condición `Has Not`.

##### Casos de uso

Digamos que has configurado una campaña para que se desencadene con el inicio de una sesión, y que tiene la reelegibilidad establecida en 30 días. Un usuario recibió la campaña hace dos días, y quieres cambiar la copia. Primero, archivarías la campaña y eliminarías las tarjetas de la fuente. En segundo lugar, duplicarías la campaña y la relanzarías con el nuevo texto. Si el usuario tiene otra sesión, recibirá inmediatamente la nueva tarjeta.

##### Impacto

* **Informar:** Cada versión de la tarjeta tendría sus propios análisis.
* **Destinatarios existentes:** Los destinatarios nuevos y existentes verían la tarjeta actualizada en la siguiente actualización de la fuente si son elegibles.

{% alert tip %}
Recomendamos esta opción para mensajes en los que muestres el contenido más reciente de la tarjeta (como los banners de la página de inicio), los cambios deban mostrarse inmediatamente o cuando la reelegibilidad esté desactivada.
{% endalert %}

#### Opción 2: Parar y relanzar

Si una tarjeta tiene activada la reelegibilidad, puedes optar por:

1. Detén tu campaña.
2. Elimina las tarjetas de contenido activas de las fuentes de los usuarios.
3. Edita tu campaña según sea necesario.
4. Reinicia tu campaña.

Con este planteamiento, los nuevos usuarios elegibles obtendrán la nueva tarjeta, y los anteriores destinatarios obtendrán la nueva tarjeta cuando vuelvan a ser elegibles.

##### Casos de uso

Supongamos que tienes una campaña desencadenada por el inicio de una sesión y con la posibilidad de volver a ser elegible establecida en 30 días. Un usuario recibió la campaña hace dos días, y quieres cambiar la copia. Primero, detén la campaña y retira la tarjeta de la fuente. En segundo lugar, vuelve a publicar la campaña con el nuevo texto. Si el usuario tiene otra sesión, recibirá la nueva tarjeta en 28 días.

##### Impacto

* **Informar:** Una campaña contendrá todos los análisis de tarjeta lanzados. Braze no diferenciará entre las versiones lanzadas.
* **Destinatarios existentes:** Los usuarios que ya hayan recibido la tarjeta no recibirán las tarjetas actualizadas hasta que vuelvan a ser elegibles. Si se desactiva la reelegibilidad, nunca recibirían la nueva tarjeta.

{% alert tip %}
Recomendamos utilizar esta opción para mensajes únicos en un centro de notificaciones o buzón de entrada de mensajes (como promociones), cuando sea importante que los análisis estén unificados o cuando la puntualidad del mensaje no sea una preocupación (como cuando los destinatarios existentes pueden esperar a la ventana de elegibilidad antes de ver las tarjetas actualizadas).
{% endalert %}

#### Mantener tarjetas en las fuentes de los usuarios

Si lo deseas, puedes mantener una campaña de tarjeta de contenido activa en las fuentes de los usuarios y no eliminarla. Cuando se edita la campaña en vivo, la versión anterior no editada de la tarjeta de campaña seguirá en vivo, y sólo los usuarios que cumplan los criterios tras las ediciones verán la nueva versión. Sin embargo, los usuarios ya expuestos a la campaña pueden ver dos versiones de la tarjeta.

