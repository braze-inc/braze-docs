---
nav_title: Segmentación de usuarios
article_title: Dirigirse a los usuarios
page_order: 9
page_type: reference
description: "Este artículo de referencia explica cómo dirigirte a tu audiencia en tu campaña y a los editores de Canvas."
tool:
    - Campaigns
    - Canvas
---

# Dirigirse a los usuarios

> Determinar cómo dirigirte a tus usuarios es uno de los pasos más cruciales a la hora de crear una campaña o Canvas. Si sabes cómo segmentar tu audiencia en función de sus comportamientos, preferencias y datos demográficos, podrás adaptar y personalizar tu mensajería.

## Crear una audiencia objetivo

### Paso 1: Elige usuarios

En **Opciones de segmentación**, puedes utilizar las siguientes opciones para elegir a qué usuarios quieres dirigir tu campaña o Canvas. Sólo los usuarios que coincidan con tus criterios definidos recibirán el mensaje. Tenga en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

{% tabs local %}
{% tab segmento único %}
Para dirigirse a los miembros de un segmento creado previamente, seleccione un segmento del desplegable en **Usuarios objetivo por segmento**.
{% endtab %}

{% tab segmentos múltiples %}
Para dirigirse a usuarios que pertenecen a varios segmentos creados previamente, añada varios segmentos desde el menú desplegable en **Usuarios objetivo por segmento**. La audiencia objetivo resultante serán usuarios tanto del primer segmento como del segundo y del tercero, etc.
{% endtab %}

{% tab filtros múltiples %}
Para dirigirse a los usuarios sin añadir un segmento, puede utilizar una serie de filtros. Se trata de una audiencia improvisada durante la creación del mensaje y te permite omitir la creación de segmentos cuando envías a audiencias puntuales.

![Filtros adicionales para un mensaje dirigido a usuarios que han abierto una aplicación por última vez en el día, que nunca han recibido una campaña o un paso en Canvas y que realizaron una compra hace menos de 30 días.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab segmentos y filtros %}
También puede dirigirse a los usuarios de uno o varios segmentos creados previamente que también estén incluidos en filtros adicionales. Después de seleccionar primero sus segmentos, puede refinar aún más su audiencia en la sección **Filtros adicionales**. Esto se demuestra en la siguiente captura de pantalla, que se dirige a los usuarios que están en el segmento "Usuarios activos diarios", en el segmento "Nunca han abierto el correo electrónico" y que hicieron una compra hace más de 30 días.

![Opciones de segmentación para un mensaje que incluye dos segmentos y tiene un filtro adicional para una última compra realizada hace menos de 30 días.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Aplicaciones específicas %}

Puedes entregar un mensaje de campaña o un paso en Canvas a aplicaciones específicas, como enviar un mensaje dentro de la aplicación o una notificación push sólo a aplicaciones Android o iOS.

Sin embargo, recuerda que es posible que un usuario utilice varias aplicaciones. El filtro "Tiene aplicación" identifica a todos los usuarios que tienen la aplicación seleccionada, pero no controla qué aplicaciones reciben mensajes. Por ejemplo, si aplicas un filtro de segmento en el que "Tiene aplicación" está configurado como Android, cualquier usuario que también tenga la aplicación iOS también recibirá el mensaje en su aplicación iOS.

![Un filtro para los usuarios que tienen la aplicación "Hola, Mundo (Android)".]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Supongamos que quieres enviar un mensaje dentro de la aplicación sólo a aplicaciones de Android.

1. Crea un segmento y establece **Aplicaciones y sitios web dirigidos** a **Usuarios de aplicaciones específicas**, luego selecciona tu aplicación Android.

![Un segmento dirigido a usuarios de una aplicación concreta, "Test_Android".]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2\. En tu campaña o Canvas, ve al paso **Audiencias objetivo** y confirma que tu segmento está añadido en la sección **Usuarios objetivo por segmento**. 

![El paso "Audiencias objetivo" con un segmento de ejemplo seleccionado.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Esto no funcionará si añades tu segmento en la sección **Filtros adicionales** a través de un filtro de pertenencia a un segmento. Debes hacer referencia directa a tu segmento en **Usuarios objetivo por segmento** para entregar tu mensaje sólo a esa aplicación.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
En el caso de las campañas por correo electrónico, puede dirigirse a los Grupos semilla en la sección **Grupos semilla**. Tenga en cuenta que los grupos de semillas no están disponibles para las campañas de API, aunque puede incluir grupos de semillas a través de una entrada activada por API en una campaña. Para más información, consulta [Grupos semilla]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).
{% endalert %}

### Paso 2: Pon a prueba a tu audiencia

Después de añadir segmentos y filtros a su público, puede probar si su público está configurado como se esperaba [buscando un usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar si coincide con los criterios del público.

![La sección "Búsqueda de usuarios" con un botón "Búsqueda de usuarios".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Resumen para la audiencia

El **Resumen de la audiencia** mostrará un resumen de quiénes forman parte de tu audiencia objetivo. Aquí puedes limitar aún más tu audiencia estableciendo un tope máximo de usuarios o una velocidad de entrega [con límite de tasa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/).

![La sección "Resumen de la audiencia" con opciones para establecer un tope máximo de usuarios o una velocidad de entrega con límite de tasa.]({% image_buster /assets/img_archive/audience_summary.png %})

#### Pruebas A/B

En la sección **Pruebas A/B**, puedes configurar una prueba para comparar las respuestas de los usuarios a varias versiones de la misma campaña de marketing. Estas versiones comparten objetivos de marketing similares, pero difieren en la redacción y el estilo. El objetivo es identificar la versión de la campaña que mejor cumpla sus objetivos de marketing. 

Para obtener más información y conocer las mejores prácticas, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

#### Estadísticas de audiencia

Braze proporciona estadísticas detalladas de audiencia de los canales seleccionados en el pie de página. Cuanto mayor sea tu base de usuarios, más probable es que la cantidad **de Usuarios alcanzables** sea una estimación aproximada. El número de usuarios accesibles puede disminuir si utiliza un [Grupo de Control Global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) o configura la elegibilidad de mensajes. 

- Para determinar un número exacto de tus usuarios alcanzables, selecciona [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics), ya que esto buscará entre todos los usuarios de tu base de usuarios.
- Para ver a qué porcentaje de tu base de usuarios se dirige o el valor de duración del ciclo de vida (LTV) de este segmento, selecciona **Mostrar estadísticas adicionales**.
- Para ver a qué porcentaje de tu base de usuarios se dirige o el valor de duración del ciclo de vida (LTV) de este segmento, selecciona **Mostrar estadísticas adicionales**.

##### Por qué el recuento de la audiencia objetivo puede diferir del recuento de usuarios alcanzables

{% multi_lang_include segments.md section='Diferentes tamaños de audiencia' %}

![La sección "Población total" con recuentos estimados de usuarios alcanzables en cada canal objetivo.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
Calcular las estadísticas exactas puede llevar unos minutos. Esta función sólo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros.<br><br>
En el caso de segmentos grandes, es normal que se produzcan ligeras variaciones incluso cuando se calculan estadísticas exactas. Se espera que la precisión de esta característica sea del 99,999 % o superior.
{% endalert %}

