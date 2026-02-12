---
nav_title: Crear campañas
article_title: Crear campañas de banners en Braze
page_order: 1
description: "Este artículo de referencia explica cómo crear, componer, configurar y enviar Banners mediante campañas Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Crear campañas de banners

> Aprende a crear Banners cuando construyas una campaña en Braze. Para más información general, consulta [Acerca de los banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

## Requisitos previos

Antes de lanzar tu campaña de banners, tu equipo de desarrolladores tendrá que [configurar las ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/creating_placements/). Mientras tanto, puedes redactar el borrador de tu campaña Banner, pero no podrás lanzarla.

## Crear una campaña de banners

{% multi_lang_include banners/creating_placements.md section="user" %}

### Paso 2: Crea una campaña

1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Selecciona **Banner**.
3. Pon a tu campaña un nombre claro y significativo.
4. Añade equipos y etiquetas según sea necesario. Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el generador de informes, puedes filtrar por las etiquetas correspondientes.
5. Selecciona el emplazamiento que creaste previamente para asociarlo a tu campaña.
6. Añade variantes si es necesario. Puedes elegir un tipo de mensaje y un diseño diferentes para cada uno. Para obtener más información sobre las variantes, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).

### Paso 3: Componer un Banner {#compose-a-banner}

Para componer tu Banner, puedes optar por:

- Empieza con una plantilla en blanco
- Utiliza una plantilla de pancarta Braze
- Selecciona una plantilla de banner guardada

\![Opción de elegir un Banner en blanco o una plantilla.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Paso 3.1: Estiliza el Banner

Puedes arrastrar y soltar bloques y filas en el área del lienzo para empezar a construir tu mensaje.

Para personalizar las propiedades del fondo de tu mensaje, la configuración de los bordes y mucho más, selecciona **Estilos**. Si sólo quieres personalizar el estilo de un bloque o fila concretos, selecciónalo para realizar los cambios.

\![Panel Estilo del compositor del Banner.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Paso 3.2: Definir el comportamiento al hacer clic (opcional)

Cuando un usuario hace clic en un enlace del Banner, puedes elegir que navegue más profundamente en tu aplicación o redirigirlo a otra página web. Además, puedes elegir [registrar un atributo personalizado o un evento]({{site.baseurl}}/developer_guide/analytics/), que actualizará el perfil de tu usuario con datos personalizados cuando haga clic en el Banner.

{% alert important %}
{::nomarkdown}
El comportamiento al hacer clic puede anularse si un elemento específico (como un botón, un enlace o una imagen, del Banner) tiene su propio comportamiento al hacer clic. Por ejemplo, dados los siguientes comportamientos al hacer clic:<br><ul><li>Un Banner tiene un comportamiento al hacer clic que redirige a la página de inicio de un sitio web.</li><li>Una imagen del Banner tiene un comportamiento al hacer clic que redirige a la página de producto de un sitio web.</li></ul>Si un usuario hace clic en la imagen, será redirigido a la página del producto. Sin embargo, al hacer clic en la zona circundante del Banner, se les redirigirá a la página de inicio.
{:/}
{% endalert %}

#### Paso 3.3: Añadir propiedades personalizadas (opcional) {#custom-properties}

Puedes añadir propiedades personalizadas a un Banner para adjuntar metadatos estructurados, como cadenas u objetos JSON. Estas propiedades no afectan a la forma en que se muestra el Banner, pero se puede [acceder a ellas a través del SDK de Braze]({{site.baseurl}}/developer_guide/banners/placements/) para modificar el comportamiento o la apariencia de tu aplicación. Por ejemplo, podrías

- Envía metadatos para tus análisis o integraciones de terceros.
- Utiliza metadatos como un objeto `timestamp` o JSON para desencadenar la lógica condicional.
- Controla el comportamiento de un banner en función de los metadatos incluidos, como `ratio` o `format`.

Para añadir una propiedad personalizada, selecciona **Configuración** > **Propiedades** > **Añadir propiedad**.

La página de propiedades muestra la opción de añadir la primera propiedad personalizada a una campaña de Banner.]({% image_buster /assets/img/banners/add_property.png %})

Para cada propiedad que quieras añadir, rellena lo siguiente:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| Tipo de propiedad | El tipo de datos de la propiedad. Los tipos admitidos son cadena, booleano, número, marca de tiempo, URL de imagen y objeto JSON. | Cadena |
| Clave de la propiedad | El identificador único de la propiedad. Esta clave se utiliza en el SDK para acceder a la propiedad. | `color` |
| Valor | El valor asignado a la propiedad. Debe coincidir con el tipo de propiedad seleccionado. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Cuando hayas terminado, selecciona **Hecho**.

\![La página de propiedades con una propiedad de cadena con clave color y valor #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Paso 4: Configurar la duración de la campaña

Elige una fecha y hora de inicio para tu campaña de banners. Por predeterminado, los Banners duran indefinidamente. Puedes cambiarlo seleccionando **Hora de finalización** y especificando una fecha y hora de finalización.

### Paso 5: Establecer la prioridad del Banner (opcional)

[La prioridad de los]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) banners determina el orden en que se muestran los banners si comparten la misma ubicación. Para configurar manualmente la prioridad:

1. Selecciona **Establecer prioridad exacta**.
2. Arrastra y suelta las campañas para ordenarlas con la prioridad correcta.
3. Selecciona **Aplicar clasificación**.

{% alert tip %}
Si tienes varias campañas de Banner que utilizan el mismo ID de colocación, te recomendamos que utilices el clasificador de prioridades arrastrar y soltar para definir la prioridad exacta.
{% endalert %}

### Paso 6: Prueba tu mensaje (opcional)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Paso 7: Termina de construir la campaña

Termina de construir tu campaña completando lo siguiente:

1. En **Audiencias objetivo**, elige segmentos o filtros para acotar tu audiencia. Automáticamente recibirás una vista previa de la población aproximada del segmento. La pertenencia exacta a un segmento se calcula justo antes de enviar el mensaje.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. En **Asignar conversiones**, haz un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas tras recibir una campaña, definiendo eventos de conversión con una ventana de hasta 30 días para contabilizar la acción como una conversión.

### Paso 8: Lanza tu campaña

Cuando hayas terminado de crear y probar tu campaña de banners, ¡estarás listo para lanzarla!
