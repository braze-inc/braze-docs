---
nav_title: Dirigirse a los usuarios
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

En **Opciones de segmentación**, puedes utilizar las siguientes opciones para elegir a qué usuarios quieres dirigir tu campaña o Canvas. Sólo los usuarios que coincidan con tus criterios definidos recibirán el mensaje. Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

{% tabs local %}
{% tab single segment %}
Para dirigirte a los miembros de un segmento creado previamente, selecciona un segmento en el desplegable de **Usuarios objetivo por segmento**.
{% endtab %}

{% tab multiple segments %}
Para dirigirte a usuarios que pertenecen a varios segmentos creados previamente, añade varios segmentos desde el desplegable de **Usuarios objetivo por segmento**. La audiencia objetivo resultante serán usuarios tanto del primer segmento como del segundo y del tercero, etc.
{% endtab %}

{% tab multiple filters %}
Para dirigirte a los usuarios sin añadir un segmento, puedes utilizar una serie de filtros. Se trata de una audiencia improvisada durante la creación del mensaje y te permite omitir la creación de segmentos cuando envías a audiencias puntuales.

\![Filtros adicionales para un mensaje dirigido a usuarios que han abierto por última vez una aplicación en el día, que nunca han recibido una campaña o un paso en Canvas y que realizaron una compra hace menos de 30 días.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab segments & filters %}
También puedes dirigirte a los usuarios de uno o varios segmentos creados previamente que también estén sujetos a filtros adicionales. Tras seleccionar primero tus segmentos, puedes afinar aún más tu audiencia en la sección **Filtros adicionales**. Esto se demuestra en la siguiente captura de pantalla, que se dirige a los usuarios que están en el segmento "Usuarios activos diarios", en el segmento "Nunca han abierto el correo electrónico" y que hicieron una compra hace más de 30 días.

\![Opciones de segmentación de un mensaje que incluyen dos segmentos y tienen un filtro adicional para una última compra realizada hace menos de 30 días.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Specific apps %}

Puedes entregar un mensaje de campaña o un paso en Canvas a aplicaciones específicas, como enviar un mensaje dentro de la aplicación o una notificación push sólo a aplicaciones Android o iOS.

Sin embargo, recuerda que es posible que un usuario utilice varias aplicaciones. El filtro "Tiene aplicación" identifica a todos los usuarios que tienen la aplicación seleccionada, pero no controla qué aplicaciones reciben mensajes. Por ejemplo, si aplicas un filtro de segmento en el que "Tiene aplicación" está configurado como Android, los usuarios que también tengan la aplicación iOS también recibirán el mensaje en su aplicación iOS.

Filtrar para usuarios que tengan la aplicación "Hola, mundo (Android)".]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Supongamos que quieres enviar un mensaje dentro de la aplicación sólo a aplicaciones de Android.

1. Crea un segmento y establece **Aplicaciones y sitios web dirigidos** a **Usuarios de aplicaciones específicas**, luego selecciona tu aplicación Android.

\![Un segmento dirigido a usuarios de una aplicación concreta, "Test_Android".]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2\. En tu campaña o Canvas, ve al paso **Audiencias objetivo** y confirma que tu segmento está añadido en la sección **Usuarios objetivo por segmento**. 

\![El paso "Audiencias objetivo" con un segmento de ejemplo seleccionado.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Esto no funcionará si añades tu segmento en la sección **Filtros adicionales** a través de un filtro de pertenencia a un segmento. Debes hacer referencia directa a tu segmento en **Usuarios objetivo por segmento** para entregar tu mensaje sólo a esa aplicación.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Para las campañas de correo electrónico, puedes dirigirte a Grupos semilla en la sección **Grupos semilla**. Ten en cuenta que los Grupos semilla no están disponibles para las campañas API, aunque puedes incluir Grupos semilla a través de una entrada desencadenada por la API en una campaña. Para más información, consulta [Grupos semilla]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).
{% endalert %}

### Paso 2: Pon a prueba a tu audiencia

Después de añadir segmentos y filtros a tu audiencia, puedes probar si tu audiencia está configurada como esperabas [buscando a un usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar si coincide con los criterios de audiencia.

La sección "Buscar usuario" con un botón "Buscar usuario".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Resumen de la audiencia

El **Resumen de la audiencia** mostrará un resumen de quiénes forman parte de tu audiencia objetivo. Aquí puedes limitar aún más tu audiencia estableciendo un tope máximo de usuarios o una velocidad de entrega [con límite de tasa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/).

\![La sección "Resumen de audiencia" con opciones para establecer un tope máximo de usuarios o una velocidad de entrega con límite de tasa.]({% image_buster /assets/img_archive/audience_summary.png %})

#### Pruebas A/B

En la sección **Pruebas A/B**, puedes configurar una prueba para comparar las respuestas de los usuarios a varias versiones de la misma campaña de marketing. Estas versiones comparten objetivos de marketing similares, pero difieren en la redacción y el estilo. El objetivo es identificar la versión de la campaña que mejor cumpla tus objetivos de marketing. 

Para obtener más información y las mejores prácticas, consulta [Multivariante & Pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

#### Estadísticas de audiencia

Braze proporciona estadísticas detalladas de audiencia de los canales objetivo en el pie de página. Cuanto mayor sea tu base de usuarios, más probable es que la cantidad **de Usuarios alcanzables** sea una estimación aproximada. El número de usuarios accesibles puede disminuir si utilizas un [grupo de control global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) o configuras la elegibilidad de los mensajes. 

- Para determinar un número exacto de tus usuarios alcanzables, selecciona [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics), ya que esto buscará entre todos los usuarios de tu base de usuarios.
- Para ver a qué porcentaje de tu base de usuarios se dirige o el valor de duración del ciclo de vida (LTV) de este segmento, selecciona **Mostrar estadísticas adicionales**.

##### Por qué el recuento de la audiencia objetivo puede diferir del recuento de usuarios alcanzables

{% multi_lang_include segments.md section='Differing audience size' %}

\![La sección "Población total" con recuentos estimados de usuarios alcanzables en cada canal objetivo.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
Calcular las estadísticas exactas puede llevar unos minutos de ejecución. Esta función sólo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros.<br><br>
En los segmentos grandes, es normal que se produzcan ligeras variaciones incluso al calcular las estadísticas exactas. Se espera que la precisión de esta característica sea del 99,999% o superior.
{% endalert %}

## Cómo funcionan conjuntamente la audiencia objetivo y los criterios de entrada

Cuando creas una campaña o Canvas en Braze, la segmentación se realiza en dos partes:

1. **Audiencia objetivo:** Quién cumple los requisitos
2. **Criterios de entrada:** Qué desencadena la entrega

El orden importa: Braze comprueba si alguien pertenece a la audiencia objetivo antes de evaluar los criterios de entrada. Si un usuario no cumple los requisitos para formar parte de la audiencia en ese momento, no entrará en la campaña ni en Canvas, aunque desencadene el evento de entrada más tarde. Piensa en la audiencia objetivo como en una sala de espera: sólo los usuarios que ya están dentro cuando se produce el desencadenamiento pueden avanzar.

### Ejemplo 1

Quieres enviar un mensaje push durante la primera sesión de un usuario.

Tú configuras:

- **Audiencia objetivo:** Usuarios con recuento de sesiones = 0
- **Acto de entrada:** Inicio de la sesión

Cuando el usuario abre tu aplicación, Braze ve que su recuento de sesiones es ahora 1, y que ya no cumple los requisitos para formar parte de la audiencia. El evento de entrada ocurre después de que sean elegibles, por lo que el mensaje no se enviará.

Para que esto funcione, el usuario tiene que clasificarse para la audiencia antes de que empiece la sesión (dar la vuelta a la audiencia objetivo y al desencadenante de entrada).

### Ejemplo 2

Quieres enviar un correo electrónico a los usuarios que han gastado más de 10 $ en los últimos 7 días.

Tú configuras:

- **Audiencia objetivo:** Usuarios que gastaron más de 10 $ en los últimos 7 días
- **Acto de entrada:** Cualquier compra

Ahora imagina que un usuario se gasta hoy 12 $. Eso no desencadena el mensaje, sólo los hace elegibles para entrar en la audiencia. No recibirán el correo electrónico a menos que realicen otra compra más adelante.

Un enfoque mejor sería utilizar una audiencia más amplia y trasladar el filtro a los criterios de entrada:

- **Audiencia:** Todos los usuarios (o tu audiencia base)
- **Acto de entrada:** Haz una compra
- **Filtrar entrada:** Gasto total en los últimos 7 días > 10

De este modo, una compra que cumpla los requisitos cumple el filtro y desencadena el mensaje, sin necesidad de una segunda acción.

## Buenas prácticas

- Asegúrate de que el segmento de audiencia incluye a los usuarios antes de que se produzcan los criterios de entrada.
- Evita utilizar filtros de audiencia que sólo se apliquen después de tu evento. Si un filtro depende de algo que ocurre en el momento de desencadenar (como "recuento de sesiones = 0"), puede que el usuario ya no cumpla los requisitos en el momento en que Braze lo compruebe.
- Utiliza cuidadosamente la lógica temporal. Por ejemplo, si quieres dirigirte a nuevos usuarios:
    - Configura tu audiencia objetivo como "primera aplicación utilizada en los últimos 7 días".
    - Configura tu evento de entrada como "inicio de sesión".
    - De esta forma, sólo los usuarios que aún estén dentro de su primera semana cumplirán los requisitos y entrarán cuando inicien una sesión.
