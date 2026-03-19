---
nav_title: Crear un banner
article_title: Crear un banner
page_order: 1
description: "Este artículo de referencia explica cómo crear, componer, configurar y enviar banners utilizando campañas y lienzos de Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Crear un banner

> Aprende a crear banners cuando crees campañas y lienzos en Braze. Para obtener información más general, consulta [Acerca de los banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

{% alert important %}
La creación de mensajes de banner en Canvas se encuentra en fase de acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Requisitos previos

Antes de poder lanzar tu banner, tu equipo de desarrollo debe [configurar las ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/creating_placements/). Mientras tanto, puedes seguir redactando tu campaña de banners, pero no podrás lanzarla hasta que se hayan configurado las ubicaciones.

## Crear un mensaje de banner

{% multi_lang_include banners/creating_placements.md section="user" %}

### Paso 2: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son más adecuadas para campañas de mensajería única y específica, mientras que los lienzos son más adecuados para recorridos de usuarios de varios pasos.

{% tabs %}
{% tab Campaign %}

1. Vaya a **Mensajería** > **Campañas** y seleccione **Crear campaña**.
2. Selecciona **Banner**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario. Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas. Por ejemplo, cuando usas el generador de informes, puedes filtrar por las etiquetas relevantes.
5. Selecciona la ubicación que creaste anteriormente para asociarla a tu campaña.
6. Añade variantes según sea necesario. Puedes elegir un tipo de mensaje y un diseño diferentes para cada uno. Para obtener más información sobre las variantes, consulta Pruebas [multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).
7. Elige una fecha y hora de inicio para tu campaña de banners. Predeterminadamente, los banners duran indefinidamente. Puedes cambiar esto seleccionando **«Hora de finalización»** y especificando una fecha y hora de finalización.

{% alert tip %}
Si todos los mensajes de su campaña van a ser similares o van a tener el mismo contenido, redacte su mensaje antes de añadir variantes adicionales. A continuación, puedes seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Cree su lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de lienzos.
2. Después de configurar tu Canvas, añade un paso en Mensaje en el constructor de Canvas. Nombra tu paso con algo claro y significativo.
3. Selecciona **Banner** como tu canal de mensajería.
4. Selecciona una ubicación para el banner.
5. Establece la prioridad para el banner. [La prioridad de los banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) determina el orden en que se muestran los banners si comparten la misma ubicación.
6. Establece una fecha de caducidad para el banner. Esto puede ser después de un período de tiempo una vez que el paso esté disponible o en una fecha y hora específicas.

{% endtab %}
{% endtabs %}

### Paso 3: Crear un banner {#compose-a-banner}

Para crear tu banner, puedes elegir entre:

- Comienza con una plantilla en blanco.
- Utiliza una plantilla de banner de Braze.
- Selecciona una plantilla de banner guardada.

![Opción de elegir un banner en blanco o una plantilla.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Paso 3.1: Diseña el banner

Puedes arrastrar y soltar bloques y filas en el área del Canvas para empezar a crear tu mensaje.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

Para personalizar las propiedades del fondo del mensaje, la configuración de los bordes y mucho más, selecciona **Estilos**. Si solo deseas personalizar el estilo de un bloque o fila específicos, selecciónalos para realizar los cambios.

![Panel de estilo del compositor de banners.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Paso 3.2: Define el comportamiento al hacer clic (opcional)

Cuando un usuario hace un clic en un enlace del banner, puedes elegir entre llevarlo a una sección más profunda de tu aplicación o redirigirlo a otra página web. Además, puedes optar por [registrar un atributo o evento personalizado]({{site.baseurl}}/developer_guide/analytics/), que actualiza el perfil de usuario con datos personalizados cuando hace clic en el banner.

{% alert important %}
{::nomarkdown}
El comportamiento al hacer clic se puede anular si un elemento específico (como un botón, un enlace o una imagen del banner) tiene su propio comportamiento al hacer clic. Por ejemplo, dados los siguientes comportamientos al hacer clic:<br><ul><li>Un banner tiene una función que, al hacer clic sobre él, redirige a la página de inicio de un sitio web.</li><li>Una imagen del banner tiene una función que, al hacer clic sobre ella, redirige a la página de productos de un sitio web.</li></ul>Si un usuario hace un clic en la imagen, se le redirige a la página del producto. Sin embargo, al hacer un clic en el área circundante del banner, se redirige a la página de inicio.
{:/}
{% endalert %}

#### Paso 3.3: Añadir propiedades personalizadas (opcional) {#custom-properties}

Puedes añadir propiedades personalizadas a un banner para adjuntar metadatos estructurados, como cadenas u objetos JSON. Estas propiedades no afectan a la forma en que se muestra el banner, pero se puede [acceder]({{site.baseurl}}/developer_guide/banners/placements/) a [ellas a través del SDK de Braze]({{site.baseurl}}/developer_guide/banners/placements/) para modificar el comportamiento o la apariencia de tu aplicación. Por ejemplo, tú podrías:

- Envía metadatos para tus análisis o integraciones de terceros.
- Utiliza metadatos como un`timestamp`  o un objeto JSON para desencadear la lógica condicional.
- Controla el comportamiento de un banner basándose en metadatos incluidos como`ratio`  o `format`.

Para añadir una propiedad personalizada, selecciona **Configuración** > **Propiedades** > **Añadir propiedad**.

![La página de propiedades que muestra la opción para añadir la primera propiedad personalizada a una campaña de Banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propiedad que quieras añadir, rellena lo siguiente:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| Tipo de propiedad | El tipo de datos de la propiedad. Los tipos compatibles incluyen cadenas, booleanos, números, marcas de tiempo, URL de imágenes y objetos JSON. | Cadena |
| Clave de la propiedad | El identificador único de la propiedad. Esta clave se utiliza en el SDK para acceder a la propiedad. | `color` |
| Valor | El valor asignado a la propiedad. Debe coincidir con el tipo de propiedad seleccionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Cuando hayas terminado, selecciona **Hecho**.

![La página de propiedades con una propiedad de cadena con una clave de color y un valor de #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Paso 4: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

#### Establecer prioridad del banner (opcional)

[La prioridad de los banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) determina el orden en que se muestran los banners si comparten la misma ubicación. Para establecer manualmente la prioridad:

1. Selecciona **Establecer prioridad exacta**.
2. Arrastre y suelte las campañas para ordenarlas con la prioridad correcta.
3. Selecciona **Aplicar ordenación**.

{% alert tip %}
Si tienes varias campañas de Banner que utilizan el mismo ID de ubicación, te recomendamos utilizar el clasificador de prioridades de arrastrar y soltar para definir la prioridad exacta.
{% endalert %}

#### Elige tu audiencia

1. En **Audiencias objetivo**, elige segmentos o filtros para reducir tu audiencia. Recibirás automáticamente una vista previa de la población aproximada del segmento. La pertenencia exacta al segmento se calcula antes de enviar el mensaje.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. En **Asignar conversiones**, realiza un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas después de recibir una campaña definiendo eventos de conversión con un plazo de hasta 30 días para contar la acción como una conversión.

{% multi_lang_include target_audiences.md %}

#### Elegir eventos de conversión

Braze te permite realizar el seguimiento de [los eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), es decir, la frecuencia con la que los usuarios realizan acciones específicas después de recibir una campaña. Tienes la opción de permitir un plazo de hasta 30 días durante el cual se contabiliza una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo ha hecho, complete las secciones restantes de su componente Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar [pruebas multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) e [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), y mucho más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación sobre Canvas.

{% endtab %}
{% endtabs %}

### Paso 5: Prueba tu mensaje (opcional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Paso 6: Revisar y desplegar

Una vez que hayas terminado de crear tu campaña o Canvas, revisa los detalles, [pruébalo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) y envíalo cuando estés listo.
