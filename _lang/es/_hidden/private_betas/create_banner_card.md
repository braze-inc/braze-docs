---
nav_title: Crear una tarjeta Banner
article_title: Crear una tarjeta Banner
permalink: "/create_banner_card/"
description: "Este artículo de referencia explica cómo crear y enviar tarjetas de visita utilizando campañas Braze."
page_type: reference
---

# Crear una tarjeta Banner

> Este artículo explica cómo crear una tarjeta Banner en Braze cuando creas campañas.

Al igual que [las tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/), las tarjetas de banners se incrustan directamente en tu aplicación o sitio web para que puedas atraer a los usuarios con una experiencia natural. Son una solución rápida y sin complicaciones para crear mensajes personalizados para tus usuarios, al tiempo que amplías el alcance de otros canales (como el correo electrónico o las notificaciones push). 

Las tarjetas Banner son geniales para:

- Destacar contenido destacado
- Notificar a los usuarios los próximos eventos
- Compartir actualizaciones sobre programas de fidelización

Como las tarjetas de presentación se personalizan cada vez que un usuario inicia una nueva sesión y pueden configurarse para que no caduquen nunca, son una herramienta útil para añadir a tu estrategia de interacción.

{% alert important %}
Las tarjetas de estandarte están actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Requisito previo: Determinar la ubicación

Antes de crear una Tarjeta Banner, debes designar las áreas de tu aplicación en las que quieres mostrar la Tarjeta Banner. También se denomina colocación. Después de crear un emplazamiento, puedes seleccionarlo al crear tu campaña de tarjeta Banner. Si ya tienes una colocación, salta al [paso 1](#step-1-create-your-campaign).

Para crear una colocación:

1. Ve a **Configuración** > **Colocación de tarjetas de banner**.
2. Dale un nombre a la colocación de tu tarjeta Banner.
3. (Opcional) Añade una descripción para explicar dónde se pretende colocar esta tarjeta Banner.
4. Introduce un ID de colocación único. Trabaja con tu equipo de desarrolladores para definir este ID, porque tendrán que utilizarlo durante la integración. Evita editar tu ID de ubicación después del lanzamiento, ya que esto puede romper la integración con tu aplicación o sitio web.
5. Selecciona **Guardar**.

Cada emplazamiento puede utilizarse hasta en 10 campañas. 

{% alert important %}
Los ID de colocación son únicos por espacio de trabajo.
{% endalert %}

## Paso 1: Crea tu campaña

Después de determinar la ubicación de tu tarjeta Banner, es hora de crear tu campaña.

1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Selecciona **Tarjeta Banner**.
3. Pon a tu campaña un nombre claro y significativo.
4. Añade equipos y etiquetas según sea necesario. Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el generador de informes, puedes filtrar por las etiquetas correspondientes.
5. Selecciona una [ubicación](#prerequisite-determine-placement) para asociarla a tu campaña. Aquí es donde aparecerá la tarjeta Banner en tu aplicación o sitio web.
6. Añade y nombra tantas variantes como quieras para tu campaña. Puedes elegir distintos tipos de mensajes y diseños para cada variante añadida. Para obtener más información sobre las variantes, consulta [Pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

## Paso 2: Componer una tarjeta Banner

Para editar los detalles del contenido de tu mensaje:

1. Selecciona **Editar mensaje**. El compositor se abrirá.
2. Elige un estilo de fila que se adapte a tu mensaje. Arrastra y suelta una fila en el área del Canvas.
3. Arrastra y suelta bloques en la fila para construir tu mensaje.
4. Define el [estilo](#styles) de tu mensaje.

### Estilos

Selecciona **Estilo** para ajustar la configuración que se aplicará a todos los bloques del mensaje.

![Panel de estilo del compositor de la tarjeta Banner.]({% image_buster /assets/img/banner_cards/banner_card_styles.png %})

Aquí puedes proporcionar un estilo personalizado, como propiedades de fondo, configuración de bordes y valores predeterminados a tus tarjetas de presentación. Los estilos aplicados aquí pueden anularse para un bloque o fila concretos. Para anular los estilos, selecciona el bloque o la fila concretos para ver sus propiedades y realizar cambios.

### Comportamiento al hacer clic

Cuando tu cliente haga clic en un enlace de la tarjeta de presentación, puedes guiarle más profundamente dentro de tu aplicación o redirigirle a otra página web.

También puedes elegir registrar un atributo personalizado o un evento personalizado. Esto actualizará el perfil de tus clientes con datos personalizados cuando hagan clic en la tarjeta Banner.

## Paso 3: Construye el resto de tu campaña

A continuación, ¡construye el resto de tu campaña! Consulta las siguientes secciones para obtener más detalles sobre la mejor manera de utilizar nuestras herramientas para crear tarjetas de presentación.

### Elige la duración de la campaña

Selecciona la fecha y hora de inicio de la campaña de la tarjeta Banner. 

Por predeterminado, las tarjetas Estandarte duran indefinidamente. Si lo deseas, selecciona **Hora de finalización** para especificar una fecha y hora de finalización.

### Elige los usuarios a los que dirigirte

A continuación, dirígete a los usuarios eligiendo segmentos o filtros para reducir tu audiencia. Automáticamente recibirás una instantánea de cómo es la población aproximada de ese segmento en este momento. Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

### Elige eventos de conversión

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, y eventos de conversión, después de recibir una campaña. Puedes permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

## Paso 4: Probar y desplegar

Después de crear tu campaña, pruébala y revísala para asegurarte de que funciona como esperabas. Entonces, ¡ya estás listo para lanzar tu campaña con la tarjeta Banner!

## Lo que hay que saber

### Caducidad de las tarjetas Banner

Por defecto, las tarjetas Banner no tienen fecha de caducidad, pero puedes añadir una fecha final opcional.

### Gestión de la colocación

Las ubicaciones son únicas por espacio de trabajo, y cada ubicación puede utilizarse en hasta 10 campañas.

Los ID de colocación deben ser únicos para un espacio de trabajo, y no deben editarse después del lanzamiento. Trabaja con tu equipo de desarrolladores para definir este ID, porque tendrán que utilizarlo durante la integración. 

### Análisis

La siguiente tabla define las métricas clave de la Tarjeta Banner.

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href='https://braze.com/docs/user_guide/data_and_analytics/report_metrics#total-impressions'>Impresiones totales</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Impressions' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-impressions'>Impresiones únicas</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Impressions' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#total-clicks'>Clics totales</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Total Clicks' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#unique-clicks'>Clics únicos</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Unique Clicks' %} Each user is only counted once.</td>
        </tr>
        <tr>
            <td class="no-split"><a href='https://www.braze.com/docs/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event'>Conversiones primarias</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %}<ul><li>{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %}</li><li>{% multi_lang_include metrics.md metric='Conversion Rate' %}</li></ul></td>
        </tr>
    </tbody>
</table>

Para obtener una lista completa de métricas, definiciones y cálculos, consulta nuestro [Glosario de métricas de los informes]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/).