---
nav_title: Crea un Banner
article_title: Crea un Banner
page_order: 1
description: "Este artículo de referencia explica cómo crear, componer, configurar y enviar Banners mediante campañas y Lienzos Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Crea un Banner

> Aprende a crear Banners cuando construyas campañas y Lienzos en Braze. Para más información general, consulta [Acerca de los banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

{% alert important %}
Crear un mensaje de Banner en Canvas está en acceso temprano. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Requisitos previos

Antes de que puedas lanzar tu Banner, tu equipo de desarrolladores debe [configurar las ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/creating_placements/). Mientras tanto, puedes redactar el borrador de tu campaña de banners, pero no podrás lanzar la campaña hasta que las ubicaciones estén configuradas.

## Crear un mensaje de Banner

{% multi_lang_include banners/creating_placements.md section="user" %}

### Paso 2: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y específicas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

1. Vaya a **Mensajería** > **Campañas** y seleccione **Crear campaña**.
2. Selecciona **Banner**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario. Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el generador de informes, puedes filtrar por las etiquetas correspondientes.
5. Selecciona el emplazamiento que creaste previamente para asociarlo a tu campaña.
6. Añade variantes si es necesario. Puedes elegir un tipo de mensaje y un diseño diferentes para cada uno. Para obtener más información sobre las variantes, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).
7. Elige una fecha y hora de inicio para tu campaña de banners. Por predeterminado, los Banners duran indefinidamente. Puedes cambiarlo seleccionando **Hora de finalización** y especificando una fecha y hora de finalización.

{% alert tip %}
Si todos los mensajes de su campaña van a ser similares o van a tener el mismo contenido, redacte su mensaje antes de añadir variantes adicionales. A continuación, puedes seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Cree su lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de lienzos.
2. Después de configurar tu Canvas, añade un paso en Mensaje en el constructor de Canvas. Nombra tu paso con algo claro y significativo.
3. Selecciona **Banner** como canal de mensajería.
4. Selecciona una ubicación para el Banner.
5. Configura la prioridad del Banner. [La prioridad de los]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) banners determina el orden en que se muestran los banners si comparten la misma ubicación.
6. Establece una caducidad para el Banner. Puede ser tras un periodo de tiempo después de que el paso esté disponible o en una fecha y hora concretas.

{% endtab %}
{% endtabs %}

### Paso 3: Componer un Banner {#compose-a-banner}

Para componer tu Banner, puedes elegir entre:

- Empieza con una plantilla en blanco
- Utiliza una plantilla de pancarta Braze
- Selecciona una plantilla de banner guardada

![Opción de elegir un Banner en blanco o una plantilla.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Paso 3.1: Estiliza la pancarta

Puedes arrastrar y soltar bloques y filas en el área del lienzo para empezar a construir tu mensaje.

Para personalizar las propiedades del fondo de tu mensaje, la configuración de los bordes y mucho más, selecciona **Estilos**. Si sólo quieres personalizar el estilo de un bloque o fila concretos, selecciónalo para realizar los cambios.

![Panel de estilo del compositor del Banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Paso 3.2: Definir el comportamiento al hacer clic (opcional)

Cuando un usuario hace clic en un enlace del Banner, puedes elegir que navegue más profundamente en tu aplicación o redirigirlo a otra página web. Además, puedes elegir [registrar un atributo personalizado o un evento]({{site.baseurl}}/developer_guide/analytics/), que actualiza el perfil de tu usuario con datos personalizados cuando hace clic en el Banner.

{% alert important %}
{::nomarkdown}
El comportamiento al hacer clic puede anularse si un elemento específico (como un botón, un enlace o una imagen, del Banner) tiene su propio comportamiento al hacer clic. Por ejemplo, dados los siguientes comportamientos al hacer clic:<br><ul><li>Un Banner tiene un comportamiento al hacer clic que redirige a la página de inicio de un sitio web.</li><li>Una imagen del Banner tiene un comportamiento al hacer clic que redirige a la página de producto de un sitio web.</li></ul>Si un usuario hace clic en la imagen, se le redirige a la página del producto. Sin embargo, al hacer clic en la zona circundante del Banner, se les redirige a la página de inicio.
{:/}
{% endalert %}

#### Paso 3.3: Añadir propiedades personalizadas (opcional) {#custom-properties}

Puedes añadir propiedades personalizadas a un Banner para adjuntar metadatos estructurados, como cadenas u objetos JSON. Estas propiedades no afectan a la forma en que se muestra el Banner, pero se puede [acceder a ellas a través del SDK de Braze]({{site.baseurl}}/developer_guide/banners/placements/) para modificar el comportamiento o la apariencia de tu aplicación. Por ejemplo, podrías

- Envía metadatos para tus análisis o integraciones de terceros.
- Utiliza metadatos como un objeto `timestamp` o JSON para desencadenar la lógica condicional.
- Controla el comportamiento de un banner en función de los metadatos incluidos, como `ratio` o `format`.

Para añadir una propiedad personalizada, selecciona **Configuración** > **Propiedades** > **Añadir propiedad**.

![La página de propiedades muestra la opción de añadir la primera propiedad personalizada a una campaña de Banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propiedad que quieras añadir, rellena lo siguiente:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| Tipo de propiedad | El tipo de datos de la propiedad. Los tipos admitidos son cadena, booleano, número, marca de tiempo, URL de imagen y objeto JSON. | Cadena |
| Clave de la propiedad | El identificador único de la propiedad. Esta clave se utiliza en el SDK para acceder a la propiedad. | `color` |
| Valor | El valor asignado a la propiedad. Debe coincidir con el tipo de propiedad seleccionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Cuando hayas terminado, selecciona **Hecho**.

![La página de propiedades con una propiedad de cadena con clave de color y valor de #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Paso 4: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

#### Establecer la prioridad del Banner (opcional)

[La prioridad de los]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) banners determina el orden en que se muestran los banners si comparten la misma ubicación. Para configurar manualmente la prioridad:

1. Selecciona **Establecer prioridad exacta**.
2. Arrastra y suelta las campañas para ordenarlas con la prioridad correcta.
3. Selecciona **Aplicar clasificación**.

{% alert tip %}
Si tienes varias campañas de Banner que utilizan el mismo ID de colocación, te recomendamos que utilices el clasificador de prioridades arrastrar y soltar para definir la prioridad exacta.
{% endalert %}

#### Elige tu audiencia

1. En **Audiencias objetivo**, elige segmentos o filtros para limitar tu audiencia. Recibirás automáticamente una vista previa aproximada de la población del segmento. La pertenencia exacta a un segmento se calcula antes de enviar el mensaje.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. En **Asignar conversiones**, haz un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas tras recibir una campaña, definiendo eventos de conversión con una ventana de hasta 30 días para contabilizar la acción como una conversión.

{% multi_lang_include target_audiences.md %}

#### Elegir eventos de conversión

Braze te permite hacer un seguimiento de [los eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), es decir, la frecuencia con la que los usuarios realizan acciones específicas tras recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se cuenta una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo ha hecho, complete las secciones restantes de su componente Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar [pruebas multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) e [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), y mucho más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación sobre Canvas.

{% endtab %}
{% endtabs %}

### Paso 5: Prueba tu mensaje (opcional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Paso 6: Revisar y desplegar

Cuando hayas terminado de crear tu campaña o Canvas, revisa sus detalles, [pruébala]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) y envíala cuando estés listo.
