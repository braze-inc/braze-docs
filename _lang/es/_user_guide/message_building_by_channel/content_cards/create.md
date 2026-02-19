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

> Este artículo explica cómo crear una tarjeta de contenido en Braze cuando creas campañas y lienzos. Aquí te guiaremos para que elijas un tipo de mensajería, compongas tu tarjeta y programes la entrega de tu mensaje.

## Paso 1: Elige dónde construir tu mensaje

Utiliza campañas para mensajes únicos y sencillos (como informar a los usuarios sobre un producto con un solo mensaje). Utiliza Canvases para recorridos de usuario de varios pasos (como el envío de sugerencias de productos a medida basadas en el comportamiento del usuario a lo largo del tiempo).

{% tabs %}
{% tab Campaign %}

1. Vaya a **Mensajería** > **Campañas** y seleccione **Crear campaña**.
2. Selecciona **Tarjetas de contenido** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por las etiquetas correspondientes.
5. Añade y nombra tantas variantes como quieras para tu campaña. Puede elegir diferentes plataformas, tipos de mensaje y diseños para cada una de sus variantes añadidas. Para saber más sobre las variantes, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si todos los mensajes de su campaña van a ser similares o van a tener el mismo contenido, redacte su mensaje antes de añadir variantes adicionales. A continuación, puedes seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Cree su lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de lienzos.
2. Después de configurar tu Canvas, añade un paso en Mensaje en el constructor de Canvas. Nombra tu paso con algo claro y significativo.
3. Seleccione **Tarjetas de contenido** como canal de mensajería.
4. Elija cuándo Braze calcula la elegibilidad de la audiencia y la personalización para la tarjeta de contenido. Puede ser a la entrada del paso o en la primera impresión (recomendado). Los pasos que contienen Fichas de Contenido pueden ser programados o basados en acciones.
5. Elija si desea eliminar las tarjetas de contenido cuando los usuarios completen una compra o realicen un evento personalizado.
6. Establece una caducidad para la tarjeta de contenido (tiempo en la fuente). Puede ser al cabo de un tiempo o a una hora determinada.
7. Filtra tu audiencia, o los destinatarios, para este paso según sea necesario en la **Configuración de entrega**. Puedes refinar aún más tu audiencia especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después de la demora, a la hora de envío de los mensajes.
8. Elige cualquier otro canal de mensajería que quieras asociar a tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Especifique sus tipos de mensajes

Selecciona uno de los tres tipos esenciales de tarjeta de contenido: **Clásico**, **Imagen con subtítulos** y **Sólo imagen**. 

Para saber más sobre el comportamiento esperado y el aspecto de cada tipo, consulta [Detalles creativos]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/), o echa un vistazo a los enlaces de la siguiente tabla. Estos tipos de tarjetas de contenido son aceptados tanto por aplicaciones móviles como por aplicaciones web.

| Tipo de mensaje | Ejemplo | Descripción |
|---|---|---|
|[Clásica]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![Una tarjeta de contenido clásica con un pequeño icono y texto para animar a reservar una clase de entrenamiento.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |La tarjeta Clásica tiene un diseño sencillo con un título en negrita, el texto del mensaje y una imagen opcional a la izquierda del título y el texto. Lo mejor es utilizar una imagen cuadrada o un icono con la tarjeta clásica. |
|[Imagen subtitulada]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![Una tarjeta de contenido subtitulada con una imagen de un levantador de pesas y texto para animar a reservar una clase de entrenamiento.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | La tarjeta de imagen subtitulada muestra tu contenido con un texto y una imagen llamativa. |
|[Solo imagen]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![Una tarjeta de contenido de sólo imagen con sólo texto.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | La tarjeta "Sólo imagen" llama la atención con espacio para imágenes, GIF y otros contenidos creativos no textuales. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Paso 3: Componer una tarjeta de contenido

Puedes editar todos los aspectos del contenido y el comportamiento de tu mensaje en la pestaña **Redactar** del editor de mensajes.

![Muestra los detalles de la tarjeta de contenido en la pestaña Redactar del editor de mensajes.]({% image_buster /assets/img/content_card_compose.png %})

El contenido aquí varía en función del **Tipo de Tarjeta** elegido en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

#### Idioma

Selecciona **Añadir idiomas** para añadir los idiomas que desees de la lista proporcionada. Esto insertará [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) en tu mensaje. Le recomendamos que seleccione sus idiomas antes de escribir el contenido para que pueda rellenar el texto donde corresponda en el Líquido. Para consultar nuestra lista completa de idiomas disponibles que puedes utilizar, consulta [Idiomas admitidos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

![Una ventana con el inglés, el español y el francés seleccionados para los idiomas, y el título, la descripción y el texto del enlace seleccionados para los campos a internacionalizar.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Crear mensajes de derecha a izquierda

El aspecto final de los mensajes de derecha a izquierda depende en gran medida de cómo los presten los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Título y mensaje

Escribe lo que quieras. No hay límites, pero cuanto más rápido transmitas tu mensaje y consigas que tu cliente haga clic, ¡mejor! Recomendamos títulos y contenidos de mensajes claros y concisos. Ten en cuenta que estos campos no se proporcionan para las tarjetas de sólo imagen.

#### Imagen

Añade una imagen a tu tarjeta de contenido seleccionando **Añadir imagen** o proporcionando una URL de la imagen. Al seleccionar **Añadir imagen** se abre la **biblioteca multimedia**, donde puedes seleccionar una imagen cargada previamente o añadir una nueva. Cada tipo de mensaje y plataforma puede tener sus propias proporciones y requisitos sugeridos, así que asegúrate de comprobar cuáles son antes de encargar o hacer una imagen desde cero. Ten en cuenta que los campos de mensaje de la tarjeta de contenido están limitados a 2 KB de tamaño total.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Anclar a la parte superior

Braze muestra una tarjeta anclada en la parte superior de la fuente de un usuario y éste no puede descartarla. Si la fuente de un usuario tiene varias tarjetas ancladas, Braze las ordena cronológicamente. Después de enviar una tarjeta, no puedes actualizar retroactivamente su opción anclada. Cambiar esta opción después de enviar una campaña sólo afecta a futuros envíos.

![Vista en paralelo de la vista previa de la tarjeta de contenido en Braze para móvil y Web con la opción "Anclar esta tarjeta a la parte superior del feed" seleccionada.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportamiento al hacer clic

Cuando tu cliente hace clic en un enlace presentado en la tarjeta, tu enlace puede llevarle más adentro de tu aplicación o a otro sitio. Si eliges un comportamiento de "al hacer clic" para tu tarjeta de contenido, recuerda actualizar tu **Texto de enlace** en consecuencia.

Las siguientes acciones están disponibles para los enlaces de la tarjeta de contenido:

| Acción | Descripción |
|---|---|
| Redirigir a URL de página web | Abrir una página web no nativa. |
| [Vínculo profundo a la aplicación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Enlace profundo a una pantalla existente en su aplicación. |
| Registrar evento personalizado | Elija un [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) para activar. Puede utilizarse para mostrar otra tarjeta de contenido o activar mensajes adicionales. |
| Registrar atributo personalizado | Elija un [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) para establecer para el usuario actual. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Las opciones **Registrar evento personalizado** y **Registrar atributo** personalizado requieren la compatibilidad con la siguiente versión del SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Paso 4: Configurar ajustes adicionales (opcional)

Puedes utilizar [pares clave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para crear categorías para tus tarjetas, crear [múltiples fuentes de tarjetas de contenido]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) y personalizar cómo se ordenan las tarjetas.

Para añadir pares clave-valor a tu mensaje, ve a la pestaña **Configuración** y selecciona **Añadir nuevo par**.

## Paso 5: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

Construye el resto de tu campaña. Continúa en las siguientes secciones para obtener más detalles sobre cómo utilizar mejor nuestras herramientas para crear tarjetas de contenido.

#### Elige la programación o desencadenante de la entrega

Las tarjetas de contenido pueden entregarse en función de una hora programada, una acción o un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

También puede establecer la duración de la campaña y [las horas de silencio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) y determinar la caducidad de la tarjeta de contenido. Establezca una fecha de caducidad específica o los días que faltan para que caduque una Tarjeta, hasta 30 días. Todas las variantes tienen fechas de caducidad idénticas.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

##### Entrega programada

Para las campañas de tarjetas de contenido con entrega programada, puede elegir cuándo Braze evalúa la elegibilidad de la audiencia y la personalización para nuevas campañas de tarjetas de contenido especificando cuándo se crea la tarjeta. Para más información, consulta la [creación de tarjetas]({{site.baseurl}}/card_creation).

#### Elige los usuarios a los que dirigirte

A continuación, [dirígete a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para limitar tu audiencia. Automáticamente recibirás una vista previa del aspecto aproximado de la población de ese segmento. Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula antes de enviar el mensaje.

{% multi_lang_include target_audiences.md %}

#### Elegir eventos de conversión

Braze le permite realizar un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), tras recibir una campaña. Tiene la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo ha hecho, complete las secciones restantes de su componente Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar [pruebas multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) e [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), y mucho más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación sobre Canvas.

{% endtab %}
{% endtabs %}

## Paso 6: Revisar y desplegar

Cuando hayas terminado de construir lo último de tu campaña o Canvas, revisa sus detalles, [pruébala]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) y envíala cuando estés listo.

{% alert warning %}
Una vez lanzada una tarjeta de contenido, no se puede editar. Sólo se puede impedir el envío a nuevos usuarios y eliminarlo de los feeds de los usuarios. Consulte [Actualización de las tarjetas enviadas]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards) para saber cómo puede enfocar este escenario.
{% endalert %}

A continuación, consulte [los informes de Content Card]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) para saber cómo puede acceder a los resultados de sus campañas de Content Card.

## Lo que hay que saber

### Limitaciones de la carga útil y de la fuente

Para favorecer el rendimiento, las tarjetas de contenido tienen dos restricciones clave: un límite en el tamaño de la carga útil de cada tarjeta y un número máximo de tarjetas que pueden aparecer en una fuente.

#### Limitaciones de tamaño para las tarjetas de contenido

La carga útil completa de datos de una sola tarjeta de contenido no puede superar los 2 KB **después de que** se realice cualquier personalización de Liquid. Esto incluye lo siguiente:

* Título
* Mensaje
* URL de la imagen (la longitud de la cadena de la URL en sí, no el tamaño del archivo de la imagen)
* Texto de enlace
* Enlaza URLs para todas las plataformas especificadas (las URLs separadas para iOS, Android y Web cuentan para el total)
* Pares clave-valor (tanto los nombres de las claves como sus valores)

Si utilizas Liquid para introducir cadenas largas de texto (por ejemplo, de atributos personalizados), puedes sobrepasar el límite. 

El compositor de campañas mostrará una advertencia si tu contenido estático supera el límite. (No predecimos el tamaño para el contenido dinámico utilizando Liquid). **Si el tamaño del mensaje supera los 2 KB, se cancelará en el momento del envío.** Puedes ver estos abortos en el Registro de Actividad de Mensajes con el motivo `Content card maximum size exceeded`.

{% alert important %}
Durante los envíos de prueba, las tarjetas de contenido que superen los 2 KB pueden seguir entregándose y mostrándose correctamente.
{% endalert %}

He aquí algunas buenas prácticas para administrar el tamaño de la carga útil de la tarjeta de contenido:

* Utiliza acortadores de URL para los enlaces largos. Las URL, especialmente las que tienen muchos parámetros de seguimiento, pueden tener problemas de límite de tamaño. Utilizar un servicio de acortamiento de URL puede reducir drásticamente el número de caracteres y liberar espacio en la carga útil.
* Trunca el contenido dinámico con Liquid. Al personalizar tarjetas con texto dinámico a partir de atributos de usuario o llamadas a la API, la longitud del contenido puede ser impredecible. Utiliza proactivamente filtros Liquid como `truncate` para limitar la longitud de cualquier texto dinámico.
* Sé eficiente con las URL multiplataforma. El límite de 2 KB incluye las URL de todas las plataformas que definas. Utilizar URL largas y únicas para cada plataforma puede multiplicar el tamaño de la carga útil. Si es posible, utiliza un único enlace que funcione en todas las plataformas, o utiliza acortadores de URL cuando sea necesario.
* Considera los banners para enriquecer el contenido. Para los casos de uso que requieren sistemáticamente grandes cantidades de contenido, puede que las tarjetas de contenido no sean el canal adecuado. Los banners no tienen la misma limitación de carga útil de 2 KB y son más adecuados para incrustar contenido más rico directamente en una aplicación o sitio web.

#### Número de tarjetas en la fuente

Cada usuario puede tener hasta 250 tarjetas de contenido no caducadas en su fuente en un momento dado. Cuando se supere este límite, Braze dejará de devolver las tarjetas más antiguas, aunque no se hayan leído. Las tarjetas descartadas también cuentan para este límite, lo que significa que un número elevado de tarjetas descartadas puede reducir el espacio disponible para las más antiguas.

Para evitar problemas con el límite de la tarjeta, te aconsejamos las siguientes buenas prácticas:

- **Utiliza fechas de caducidad más cortas:** Para las campañas que son sensibles al tiempo (como una venta de fin de semana), establece una fecha de caducidad específica. De este modo, las tarjetas se eliminan automáticamente de la fuente y no contarán para el límite cuando ya no sean relevantes.
- **Aprovecha la eliminación basada en acciones:** Configura eventos de eliminación para tarjetas transaccionales o basadas en objetivos. Por ejemplo, una tarjeta que pida a un usuario que complete su perfil debe eliminarse en cuanto se registre un evento `profile_completed`.
- **Audita las campañas de larga duración:** Revisa las campañas recurrentes o en curso para asegurarte de que no están creando una mala experiencia para tus usuarios al llenar la fuente con demasiadas tarjetas a lo largo del tiempo.

### Cómo volver a ser elegible para las tarjetas de contenido

La reelegibilidad determina si un usuario puede recibir un mensaje de la misma campaña más de una vez y cuándo. Para las tarjetas de contenido, entender cómo funciona esto es fundamental para gestionar campañas recurrentes y garantizar que los usuarios no reciban mensajes duplicados o caducados.

{% alert tip %}
¿Quieres que tu contenido dure más de 30 días? Prueba [los Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

#### Cómo se calcula la readmisibilidad

Si activas la reelegibilidad, la cuenta atrás para cuando un usuario puede "volver a entrar" en una campaña comienza después de que se le envíe el mensaje. El momento concreto en que comienza esta cuenta atrás depende de la configuración de creación de tu tarjeta:

* Las tarjetas de contenido que se utilizan [en la primera impresión]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) utilizan el tiempo de impresión para calcular la reelegibilidad.
* Las tarjetas de contenido creadas en el lanzamiento de la campaña o en la entrada en Canvas utilizan la hora de envío o de impresión que sea más tardía.

#### Los 30 días de caducidad y la posibilidad de volver a ser elegible

Una fuente común de confusión es la interacción entre la reelegibilidad de la campaña y la caducidad automática de 30 días de todas las tarjetas de contenido. 

Todas las tarjetas de contenido se purgan automáticamente de los sistemas de Braze 30 días después de su envío o eliminación. Si tienes una campaña recurrente de larga duración con la reelección **desactivada**, un usuario puede volver a recibir la misma tarjeta al cabo de 30 días. Cuando se elimina la tarjeta original, el sistema deja de ver un registro de que ese usuario ha recibido la campaña, por lo que vuelve a ser elegible en su próxima sesión. 

Para que los usuarios sólo reciban una vez un mensaje de una campaña específica, añade un filtro de audiencia a tu campaña o paso en Canvas para los usuarios que no hayan recibido un mensaje de esta campaña. Este filtro es la forma más fiable de evitar los envíos duplicados de las campañas de larga duración.

### Gestión de tarjetas de contenido en vivo

Una vez enviadas las tarjetas de contenido, quedan en espera en un "buzón de entrada" listas para ser entregadas al usuario (de forma similar a lo que ocurre con los correos electrónicos). Después de introducir el contenido en la tarjeta de contenido (en el momento de la visualización), no se puede cambiar durante su vida útil. Esto se aplica incluso si estás llamando a una API a través de Contenido conectado, y los datos del punto final cambian. Estos datos no se actualizarán. Sólo se puede impedir el envío a nuevos usuarios y eliminarlo de los feeds de los usuarios. Si modifica una campaña, sólo las futuras tarjetas que se envíen tendrán la actualización.

#### Actualización de las tarjetas lanzadas

Para cambiar una tarjeta para usuarios que ya la han recibido, debes utilizar uno de los siguientes métodos:

##### Opción 1: Duplicar la campaña (recomendado para cambios inmediatos)

{% alert tip %}
Recomendamos esta opción para mensajes en los que muestres el contenido más reciente de la tarjeta, los cambios deban mostrarse inmediatamente, o cuando la reelegibilidad esté desactivada.
{% endalert %}

El primer enfoque consiste en archivar la campaña y lanzar una nueva campaña duplicada:

1. Detén la campaña original y, cuando se te pida, selecciona `Remove card after the next sync`.
2. Duplica la campaña, edítala y lanza la nueva versión.

Cuando dupliques la campaña, tienes que definir la audiencia de la nueva versión. Utiliza filtros de segmentación para controlar quién recibe la tarjeta actualizada:
* Si los usuarios no deben volver a ser elegibles para una tarjeta de contenido, puedes filtrar a los usuarios que no hayan recibido la versión anterior de la tarjeta de contenido configurando el filtro `Received Message from Campaign` a la condición de `Has Not`.
* Si los usuarios que recibieron la tarjeta anterior deben volver a ser elegibles en X días, puede establecer el filtro para `Last Received Message from specific campaign` en hace más de X días **O** `Received Message from Campaign` con la condición `Has Not`.

###### Impacto

* **Beneficiarios existentes:** Los nuevos beneficiarios y los ya existentes verán la tarjeta actualizada en la próxima actualización del feed si cumplen los requisitos.
* **Informar:** Cada versión de la tarjeta tendría sus propios análisis.

Digamos que has configurado una campaña para que se desencadene con el inicio de una sesión, y que tiene la reelegibilidad establecida en 30 días. Un usuario recibió la campaña hace dos días y usted quiere cambiar la copia. Primero, archivarías la campaña y eliminarías las tarjetas de la fuente. En segundo lugar, duplicarías la campaña y la relanzarías con el nuevo texto. Si el usuario tiene otra sesión, recibirá inmediatamente la nueva tarjeta.

##### Opción 2: Detener y relanzar la misma campaña

{% alert tip %}
Recomendamos utilizar esta opción para mensajes únicos en un centro de notificaciones o buzón de entrada de mensajes (como promociones), cuando sea importante que los análisis estén unificados o cuando la puntualidad del mensaje no sea una preocupación (como cuando los destinatarios existentes pueden esperar a la ventana de elegibilidad antes de ver las tarjetas actualizadas).
{% endalert %}

Este enfoque mantiene todos tus análisis unificados en una sola campaña. Los nuevos usuarios elegibles recibirán la nueva tarjeta, pero se retrasa la actualización para los destinatarios existentes hasta que vuelvan a ser elegibles:

1. Detén tu campaña y, cuando se te solicite, selecciona **Eliminar tarjeta tras la siguiente sincronización**.
2. Edite su campaña según sea necesario.
3. Reinicia tu campaña.

###### Impacto

* **Beneficiarios existentes:** Los usuarios que ya hayan recibido la tarjeta no recibirán las tarjetas actualizadas hasta que vuelvan a ser elegibles. Si se desactiva la reelegibilidad, nunca recibirían la nueva tarjeta.
* **Informar:** Una campaña contendrá todos los informes analíticos de las versiones de tarjetas lanzadas. Braze no diferenciará entre las versiones lanzadas.

Supongamos que tienes una campaña desencadenada por el inicio de una sesión y con la posibilidad de volver a ser elegible establecida en 30 días. Un usuario recibió la campaña hace dos días y usted quiere cambiar la copia. Primero, detén la campaña y retira la tarjeta de la fuente. En segundo lugar, vuelve a publicar la campaña con el nuevo texto. Si el usuario tiene otra sesión, recibirá la nueva tarjeta en 28 días.

#### Eliminar y caducar tarjetas

##### Extracción manual de tarjetas

Puedes eliminar manualmente las tarjetas de las fuentes de todos los usuarios en cualquier momento deteniendo la campaña.

1. Abre la campaña de la tarjeta de contenido y selecciona Detener campaña.
2. Cuando se te pregunte, selecciona **Eliminar tarjeta tras la siguiente sincronización**. La tarjeta se eliminará en la siguiente actualización de la fuente.

##### Eliminación automatizada de tarjetas {#action-based-card-removal}

Puedes eliminar automáticamente una tarjeta cuando un usuario realice una acción concreta, como completar una compra o activar una característica.

En tu campaña o paso en Canvas, especifica un evento de eliminación. Cuando un usuario realice ese evento, la tarjeta se eliminará de su fuente en una actualización posterior, después de que Braze procese el evento. 

{% alert note %}
Esta eliminación no es instantánea. Hay un retraso en el procesamiento, por lo que pueden pasar varios minutos y más de una actualización de la fuente hasta que la tarjeta desaparezca.
{% endalert %}

{% alert tip %}
Puede especificar varios eventos personalizados y compras que deben eliminar una tarjeta del feed de un usuario. Cuando el usuario realice **cualquiera** de estas acciones, se eliminarán todas las tarjetas enviadas por las tarjetas de la campaña. Las futuras tarjetas que cumplan los requisitos seguirán enviándose de acuerdo con la programación del mensaje.
{% endalert %}

![Panel de Condiciones de Eliminación de Tarjetas de Contenido con la opción Evento de Eliminación de Tarjetas de Contenido.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Caducidad de la tarjeta

Las tarjetas de contenido permanecen disponibles durante un máximo de 30 días desde su envío; transcurridos 30 días, Braze las elimina de las fuentes de los usuarios y las purga de los sistemas de Braze.

#### Hacer que las tarjetas duren más de 30 días

{% alert tip %}
Para casos de uso que requieran que los mensajes persistan más tiempo que el límite de 30 días de la tarjeta de contenido, considera el uso de banners. Los banners están diseñados para persistir y no tienen una fecha de caducidad obligatoria, lo que les permite permanecer visibles mientras se necesiten.
{% endalert %}

Si quieres que parezca que una tarjeta está siempre disponible (i.e., dura más que el máximo de 30 días), puedes crear una campaña recurrente que sustituya efectivamente la tarjeta cada 30 días:

1. Fije la duración de la tarjeta de contenido en 30 días.
2. Establezca la reelegibilidad de la campaña en 30 días.
3. Configure la campaña para que se active en "Inicio de sesión".
