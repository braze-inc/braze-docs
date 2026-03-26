---
nav_title: Eventos de compra
article_title: Eventos de compra
page_order: 8
page_type: reference
description: "Este artículo de referencia describe los eventos y propiedades de compra, su uso, segmentación, dónde ver los análisis relevantes, etc."
search_rank: 3
---

# Eventos de compra

> Esta página cubre los eventos y propiedades de la compra, su uso, segmentación, dónde ver los análisis relevantes y mucho más.

Los eventos de compra son acciones de compra realizadas por tus usuarios, y se utilizan para registrar las compras dentro de la aplicación y establecer el valor de duración del ciclo de vida (LTV) para cada perfil de usuario. Estos eventos deben ser configurados por tu equipo. El registro de eventos de compra te permite añadir propiedades como la cantidad y el tipo, lo que te ayuda a segmentar aún más a tus usuarios en función de estas propiedades.

## Registro de eventos de compra

Puedes registrar las compras pasando un [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) a través del [punto de conexión `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), o utilizando una de nuestras bibliotecas SDK que se enumeran a continuación.

A continuación se enumeran los métodos utilizados en diversas plataformas para registrar las compras. En estas páginas también encontrarás documentación sobre cómo añadir propiedades y cantidades a tu evento de compra. En función de estas propiedades, puedes segmentar aún más a tus usuarios.

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=unity)
- [.NET MAUI (antes Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=roku)

## Ver datos de compra

Una vez que hayas configurado y comenzado a registrar los eventos de compra, podrás ver estos datos de compra en el perfil de un usuario en la [pestaña Resumen]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab).

## Utilización de los datos de compra

Existen varias formas de utilizar los datos de compra en Braze:

- **[Segmentación](#purchase-event-segmentation):** Utiliza los datos de compra para crear segmentos de usuarios en función de su comportamiento de compra.
- **[Personalización](#personalization):** Utiliza los datos de compra para personalizar los mensajes a los usuarios.
- **[Mensajes desencadenados](#trigger-messages):** Configura los mensajes para que se desencadenen en función de los eventos de compra.
- **[Análisis](#analytics):** Analiza tus datos de compra para obtener información sobre el comportamiento de los usuarios y la eficacia de tus campañas de marketing.

### Segmentación {#purchase-event-segmentation}

Puedes desencadenar cualquier número o tipo de campañas de seguimiento basadas en eventos de compra registrados. Por ejemplo, puedes crear un segmento de usuarios que hayan realizado una compra en los últimos 30 días, o un segmento de usuarios que hayan gastado más de una determinada cantidad.

Los siguientes filtros de segmentación están disponibles a la hora de segmentar usuarios:

- Primera compra realizada
- Primera compra en la aplicación
- Último producto comprado
- Dinero gastado
- Producto comprado
- Cantidad total de compras
- X dinero gastado en Y días
- X productos comprados en Y días
- X propiedad de compra en Y días
- X compras en los últimos Y días

Para más detalles sobre cada filtro, consulta el glosario de [filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) y filtra por "Comportamiento de compra".

![Filtrado de usuarios que han realizado exactamente tres compras]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
Para segmentar en función del número de veces que se ha producido una compra concreta, registra esa compra individualmente como un [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

### Personalización

Al igual que cualquier otro tipo de datos que recopiles de tus usuarios, puedes utilizar los datos de compra para personalizar tus mensajes a través de Liquid. Por ejemplo, puedes enviar un correo electrónico personalizado a un usuario recomendándole productos similares a los que acaba de comprar.

Supongamos que tienes una propiedad del evento de compra llamada `last_purchased_product` que almacena el nombre del último producto que compró un usuario. Puedes utilizar esta propiedad para personalizar un mensaje de correo electrónico como este:

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

En este ejemplo, el mensaje se personaliza en función de la propiedad `last_purchased_product`. Si el último producto que compró el usuario fue "Running Shoes", recibirá un mensaje recomendándole pantalones cortos para correr y botellas de agua. Si el último producto fue "Yoga Mat", recibirá un mensaje recomendándole bloques y correas de yoga. Si `last_purchased_product` es cualquier otra cosa, recibirá un mensaje genérico de agradecimiento.

### Mensajes desencadenados

Un caso de uso común es enviar automáticamente un mensaje, como un correo electrónico, cuando un usuario realiza una compra. Por ejemplo, puedes enviar un mensaje de agradecimiento o un código de descuento para una futura compra.

Para ello, crea una campaña basada en acciones o un Canvas y, a continuación, define la acción desencadenante como **Realizar compra**. También puedes especificar condiciones adicionales para el desencadenante, como el producto adquirido o el importe de la compra.

También puedes personalizar tu mensaje desencadenado con Liquid. En el siguiente ejemplo, `${purchase_product_name}` es un atributo personalizado que sustituirías por el nombre real del atributo que almacena el nombre del producto adquirido en tu configuración de Braze.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Análisis

Además de realizar un seguimiento de las métricas de compra para la segmentación, Braze también registra el número de compras de cada producto y los ingresos generados a lo largo del tiempo. Esto puede ser útil para identificar los productos más populares o medir el impacto de una campaña promocional en las ventas.

Puedes encontrar estos datos en la página [Informe de ingresos]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

### Comprender los cálculos de ingresos

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
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Ingresos del ciclo de vida</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valor de duración del ciclo de vida por usuario</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Ingresos medios diarios</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics#daily-purchases">Compras diarias</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Ingresos diarios por usuario</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### Conversión de divisas

Cuando los eventos de compra se registran en una divisa distinta al USD, Braze convierte el importe a USD utilizando los tipos de cambio de [Open Exchange Rates](http://openexchangerates.org). Estos tipos se actualizan una vez cada 24 horas. Dado que los tipos de cambio se almacenan en caché, puede haber ligeras diferencias con respecto al tipo de mercado en tiempo real, especialmente en el caso de divisas que experimentan fluctuaciones rápidas.

#### Cálculo de los ingresos del ciclo de vida

Braze utiliza los eventos de compra para calcular los ingresos del ciclo de vida (también llamados valor de duración del ciclo de vida o LTV) de un usuario, que es una predicción del beneficio neto atribuido a toda la relación futura con un cliente. Esto puede ayudarte a tomar decisiones informadas sobre las estrategias de adquisición y retención de clientes.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

Hay dos lugares principales en Braze que puedes consultar para comprender el LTV de tus usuarios:

- Para obtener métricas generales como los *ingresos del ciclo de vida* y el *valor de duración del ciclo de vida por usuario* para cada aplicación y sitio, consulta tu [Informe de ingresos]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
- Para conocer los ingresos del ciclo de vida de un usuario concreto, consulta su [perfil de usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab).

##### Impacto de las devoluciones en los ingresos del ciclo de vida

Cuando utilices eventos de compra para realizar un seguimiento de los datos de compra, debes registrar los reembolsos como un evento de compra de Braze con una propiedad `price` negativa. Este enfoque mantiene un total exacto de los ingresos del ciclo de vida.

Sin embargo, ten en cuenta que el reembolso contará como un evento de compra adicional. Veamos el siguiente ejemplo. Sam hace su primera compra por $12 pero devuelve parte de la compra para que le reembolsen $5. El perfil de Sam registraría:

- 1 compra con un precio de $12
- 1 compra con un precio de -$5
- Ingresos del ciclo de vida de $7

Aunque Sam tendría dos eventos de compra en su perfil, en realidad solo hizo una compra. Es importante tener esto en cuenta si tienes segmentos o casos de uso creados en torno al número de compras que ha realizado un usuario. Los reembolsos constantes inflarán el recuento de compras en el perfil del usuario.

## Propiedades de eventos de compra {#purchase-properties}

Con las propiedades de eventos de compra, puedes establecer propiedades en las compras que se pueden utilizar para calificar aún más las condiciones de activación, aumentar la personalización en la mensajería y generar análisis más sofisticados a través de la exportación de datos sin procesar. Los tipos de valores de las propiedades (cadena, numérico, booleano, fecha) varían según la plataforma y suelen asignarse como pares clave-valor.

{% alert warning %}
Las siguientes claves están reservadas y no pueden utilizarse como nombres de propiedades del evento de compra: `time`, `product_id`, `quantity`, `event_name`, `price` y `currency`. Si usas una clave reservada en el objeto `properties`, se devolverá el error "Campo 'properties' no válido".
{% endalert %}

Por ejemplo, si tienes una aplicación de comercio electrónico y quieres enviar un mensaje a un usuario tras realizar una compra, podrías mejorar adicionalmente tu audiencia objetivo y permitir una mayor personalización de la campaña añadiendo una propiedad de evento de compra de `brand_name`.

**Ejemplo de activación basada en las propiedades del evento de compra:**

![Configuración de entrega basada en acciones para enviar una campaña a los usuarios que compren auriculares con una marca igual a HeadphoneMart]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Consulta el [objeto de propiedades de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) para obtener más información.

### Segmentación de propiedades de eventos

La segmentación de propiedades de eventos te permite dirigirte a los usuarios no solo en función de los eventos personalizados realizados, sino también de las propiedades asociadas a esos eventos. Esto añade opciones de filtrado adicionales al segmentar eventos de compra y eventos personalizados.

![Filtros de segmentación para propiedades del evento de compra, que muestran opciones para filtrar a los usuarios en función de valores específicos de propiedades del evento de compra, como filtrar a los usuarios que compraron un producto con una propiedad determinada dentro de un plazo establecido.]({% image_buster /assets/img/purchase_event_property.png %}){: style="max-width:80%;margin-left:15px;"}

Estos filtros de segmentación incluyen:
- Ha realizado el evento personalizado con la propiedad Y con el valor V X veces en los últimos Y días
- Ha realizado compras con la propiedad Y con un valor V X veces en los últimos Y días
- Añade una segmentación de 1 a 30 días en todas las compras, eventos y propiedades dentro de las compras y eventos

A diferencia de las [extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), los segmentos utilizados se actualizan en tiempo real, admiten una cantidad ilimitada de segmentos, ofrecen un historial retrospectivo de 30 días como máximo e incurren en puntos de datos. Debido al cargo adicional por punto de datos, debes ponerte en contacto con tu administrador del éxito del cliente de Braze para activar las propiedades de eventos para tus eventos personalizados.

Una vez aprobadas, se pueden añadir propiedades adicionales en el dashboard en **Configuración de datos** > **Eventos personalizados** seleccionando **Administrar propiedades**. A continuación, puedes utilizar estas propiedades de evento en el paso de objetivo del constructor de campañas o Canvas.

### Propiedades de entrada en Canvas y propiedades de eventos

{% multi_lang_include canvas_entry_event_properties.md %}

### Registrar las compras a nivel de pedido

Para registrar las compras a nivel de pedido en lugar de a nivel de producto, utiliza el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación de objetos de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

### Convenciones de nomenclatura de ID de producto

En Braze ofrecemos algunas convenciones generales de nomenclatura para el `product_id` del objeto de compra. Al elegir `product_id`, Braze sugiere utilizar nombres simplificados como el nombre del producto o la categoría del producto (en lugar de SKU) con la intención de agrupar todos los artículos registrados por este `product_id`.

Esto hace que los productos sean fáciles de identificar para su segmentación y activación. 

## Bloquear eventos de compra

En ocasiones, es posible que identifiques eventos de compra que registran demasiados puntos de datos, que ya no son útiles para tu estrategia de marketing o que se registraron por error. Para impedir que estos datos se envíen a Braze, puedes bloquear el objeto de datos personalizados mientras tu equipo de ingeniería trabaja para eliminarlo del backend de tu aplicación o sitio web.

En el dashboard de Braze, puedes gestionar las listas de bloqueo desde **Configuración de datos** > **Productos**. Consulta [Gestión de datos personalizados]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) para obtener más información.