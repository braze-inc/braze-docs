---
nav_title: Eventos de compra
article_title: Eventos de compra
page_order: 8
page_type: reference
description: "Este artículo de referencia describe los eventos y propiedades de compra, su uso, segmentación, dónde ver los análisis relevantes, etc."
search_rank: 3
---

# Eventos de compra

> Conozca los eventos y propiedades de compra, su uso, segmentación, dónde ver los análisis relevantes y mucho más.

Los eventos de compra son acciones de compra realizadas por sus usuarios. Estos eventos se utilizan para registrar las compras dentro de la aplicación y establecer el valor de vida útil (LTV) de cada perfil de usuario. Estos eventos de compra deben ser configurados por su equipo. El registro de eventos de compra le permite añadir propiedades como la cantidad y el tipo, lo que le ayuda a segmentar aún más a sus usuarios en función de estas propiedades.

## Registro de eventos de compra

Puedes registrar las compras pasando un [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) a través del [punto final `/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

A continuación se enumeran los métodos utilizados en diversas plataformas para registrar las compras. En estas páginas también encontrará documentación sobre cómo añadir propiedades y cantidades a su evento de compra. En función de estas propiedades, puede segmentar aún más a sus usuarios.

- [Android y FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_purchases/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/)

## Ver datos de compra

Una vez que haya configurado y comenzado a registrar los eventos de compra, podrá ver estos datos de compra en el perfil de un usuario en la [pestaña Visión general]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab).

## Utilización de los datos de compra

Existen varias formas de utilizar los datos de compra en Braze:

- **[Segmentación](#purchase-event-segmentation):** Utilice los datos de compra para crear segmentos de usuarios en función de su comportamiento de compra.
- **[Personalización](#personalization):** Utilizar los datos de compra para personalizar los mensajes a los usuarios.
- **[Mensajes de activación](#trigger-messages):** Configure los mensajes para que se activen en función de los eventos de compra.
- **[Análisis](#analytics):** Analice sus datos de compra para obtener información sobre el comportamiento de los usuarios y la eficacia de sus campañas de marketing.

### Segmentación {#purchase-event-segmentation}

Puede activar cualquier número o tipo de campañas de seguimiento basadas en eventos de compra registrados. Por ejemplo, puede crear un segmento de usuarios que hayan realizado una compra en los últimos 30 días, o un segmento de usuarios que hayan gastado más de una determinada cantidad.

Los siguientes filtros de segmentación están disponibles a la hora de segmentar usuarios:

- Primera compra hecha
- Primera compra de la aplicación
- Último producto comprado
- Dinero gastado
- Producto comprado
- Cantidad total de compras
- X dinero gastado en Y días
- X productos comprados en Y días
- X Compra de propiedad en Y días
- X compras en los últimos Y días

Para más detalles sobre cada filtro, consulte el glosario de [filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) y filtre por "Comportamiento de compra".

![Filtrado de usuarios que han realizado exactamente tres compras][1]{: style="max-width:80%;"}

{% alert tip %}
Si desea segmentar en función del número de veces que se ha producido una compra específica, deberá registrar dicha compra individualmente como un [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

### Personalización

Al igual que cualquier otro tipo de datos que recopile de sus usuarios, puede utilizar los datos de compra para personalizar sus mensajes a través de Liquid. Por ejemplo, puede enviar un correo electrónico personalizado a un usuario recomendándole productos similares a los que acaba de comprar.

Digamos que tiene una propiedad de evento de compra llamada `last_purchased_product` que almacena el nombre del último producto que compró un usuario. Puede utilizar esta propiedad para personalizar un mensaje de correo electrónico de esta forma:

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

En este ejemplo, el mensaje se personaliza en función de la propiedad `last_purchased_product`. Si el último producto que compró el usuario fue "Zapatillas de correr", recibirá un mensaje recomendándole pantalones cortos para correr y botellas de agua. Si el último producto era un "Mat de yoga", reciben un mensaje recomendando bloques y correas de yoga. Si la dirección `last_purchased_product` es otra, reciben un mensaje genérico de agradecimiento.

### Mensajes de activación

Un caso de uso común es enviar automáticamente un mensaje, como un correo electrónico, cuando un usuario realiza una compra. Por ejemplo, puede enviar un mensaje de agradecimiento o un código de descuento para una futura compra.

Para ello, cree una campaña basada en acciones o Canvas y, a continuación, defina la acción desencadenante como **Realizar compra**. También puede especificar condiciones adicionales para el activador, como el producto adquirido o el importe de la compra.

También puede personalizar su mensaje activado con Liquid.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

En este ejemplo, `${purchase_product_name}` es un atributo personalizado que deberá sustituir por el nombre real del atributo que almacena el nombre del producto adquirido en su configuración de Braze.

### Análisis

Además de realizar un seguimiento de las métricas de compra para la segmentación, Braze también anota el número de compras de cada producto y los ingresos generados a lo largo del tiempo. Esto puede ser útil para ver qué productos son los más populares o medir el impacto de una campaña promocional en las ventas.

Puede consultar estos datos en la página [Informe de ingresos]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

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
            <td class="no-split">{% multi_lang_include metrics.md metric='Ingresos de toda la vida' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">Valor de duración del ciclo de vida por usuario</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Valor de duración del ciclo de vida por usuario' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">Ingresos medios diarios</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Ingresos medios diarios' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics#daily-purchases">Compras diarias</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Compras diarias' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">Ingresos diarios por usuario</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Ingresos diarios por usuario' %}</td>
        </tr>
    </tbody>
</table>

#### Cálculo de los ingresos del ciclo de vida

Braze utiliza los eventos de compra para calcular los ingresos de por vida (también llamados valor de por vida o LTV) de un usuario, que es una predicción del beneficio neto atribuido a toda la relación futura con un cliente. Esto puede ayudarle a tomar decisiones informadas sobre las estrategias de adquisición y retención de clientes.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

Hay dos lugares principales en Braze que puede consultar para comprender el LTV de sus usuarios:

- Para obtener métricas generales como los *ingresos de por vida* y el *valor de por vida por usuario* para cada aplicación y sitio, consulte su [Informe de ingresos]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
- Para conocer los ingresos de por vida de un usuario concreto, consulte su [perfil de usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab).

##### Impacto de las devoluciones en los ingresos del ciclo de vida

Cuando utilice eventos de compra para realizar un seguimiento de los datos de compra, debe realizar un seguimiento de los reembolsos registrando un evento de compra Braze con una propiedad `price` negativa. Este enfoque mantendrá un total exacto de los ingresos de por vida.

Sin embargo, tenga en cuenta que el reembolso contará como un evento de compra adicional. Veamos el siguiente ejemplo. Sam hace su primera compra por 12 $ pero devuelve parte de la compra para que le reembolsen 5 $. El perfil de Sam registraría:

- 1 compra con un precio de $12
- 1 compra con un precio de -$5
- Ingresos del ciclo de vida de $7

Aunque Sam tendría dos eventos de compra en su perfil, en realidad solo hizo una compra. Es importante tener esto en cuenta si tiene segmentos o casos de uso creados en torno al número de compras que ha realizado un usuario. Los reembolsos constantes inflarán el recuento de compras en el perfil del usuario.

## Adquirir propiedades para eventos {#purchase-properties}

Con las propiedades de eventos de compra, puede establecer propiedades en las compras que se pueden utilizar para calificar aún más las condiciones de activación, aumentar la personalización en la mensajería y generar análisis más sofisticados a través de la exportación de datos sin procesar. Los tipos de valores de las propiedades (cadena, numérico, booleano, fecha) varían según la plataforma y suelen asignarse como pares clave-valor.

Por ejemplo, si una aplicación de comercio electrónico quisiera enviar un mensaje a un usuario después de realizar una compra, podría mejorar adicionalmente su público objetivo y permitir una mayor personalización de la campaña añadiendo una propiedad de evento de compra de `brand_name`.

**Ejemplo de activación basada en las propiedades del evento de compra:**

![Ajustes de envío basados en acciones para enviar una campaña a los usuarios que compren auriculares con una marca igual a HeadphoneMart.][2]{: style="max-width:80%;margin-left:15px;"}

Consulte el [objeto de propiedades de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) para obtener más información.

### Segmentación de propiedades de eventos

La segmentación por propiedades de eventos le permite dirigirse a los usuarios basándose no sólo en los eventos personalizados realizados, sino también en las propiedades asociadas a dichos eventos. Esta función añade opciones de filtrado adicionales al segmentar los eventos de compra y personalizados.

![][6]{: style="max-width:80%;margin-left:15px;"}

Estos filtros de segmentación incluyen:
- Ha realizado el evento personalizado con la propiedad Y con valor V X veces en los últimos Y días.
- Ha realizado alguna compra con la propiedad Y con valor V X veces en los últimos Y días.
- Añade la posibilidad de segmentar en 1, 3, 7, 14, 21 y 30 días.

A diferencia de las [extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), los segmentos utilizados se actualizan en tiempo real, admiten una cantidad ilimitada de segmentos, ofrecen un historial retrospectivo de 30 días como máximo e incurren en puntos de datos. Debido al cargo adicional por punto de datos, debe ponerse en contacto con su gestor de éxito de clientes de Braze para activar las propiedades de eventos para sus eventos personalizados.

Una vez aprobadas, se pueden añadir propiedades adicionales en el panel de control, en **Configuración de datos** > **Eventos personalizados**, haciendo clic en **Gestionar propiedades**. A continuación, puede utilizar estas propiedades de evento en el paso de destino del constructor de campañas o Canvas.

### Propiedades de entrada en el lienzo y propiedades de eventos

{% alert important %}
A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible como referencia cuando se utiliza `canvas_entry_properties` y `event_properties` para el flujo de trabajo original de Canvas.
{% endalert %}

Puedes aprovechar `canvas_entry_properties` y `event_properties` en tus recorridos de usuario de Canvas. Consulta [las propiedades de entrada y las propiedades de evento de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) para obtener más información y ejemplos.

{% alert important %}
No puedes utilizar `event_properties` en el paso Mensaje principal. En su lugar, debe utilizar `canvas_entry_properties` o añadir un paso Rutas de acción con el evento correspondiente **antes** del paso Mensaje que incluye `event_properties`.
{% endalert %}

{% tabs local %}
{% tab Propiedades de entrada del lienzo %}

[Las propiedades de entrada del lienzo]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/) son las propiedades que se asignan a los lienzos basados en acciones o activados por la API. El objeto `canvas_entry_properties` tiene un límite de tamaño máximo de 50 KB.

{% alert important %}
En el caso concreto de los canales de mensajes integrados en la aplicación, sólo se puede hacer referencia a `canvas_entry_properties` en Canvas Flow y en el editor Canvas original si tienes activadas las propiedades de entrada persistente en el editor original como parte del acceso anticipado anterior.
{% endalert %}

Para la mensajería de Canvas Flow, `canvas_entry_properties` puede utilizarse en Liquid en cualquier paso Mensaje. Utilice este Líquido cuando haga referencia a estas propiedades: ``{% raw %} canvas_entry_properties${property_name} {% endraw %}``. Tenga en cuenta que los eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta manera. 

{% raw %}
Por ejemplo, considere la siguiente petición: `\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}`. Podrías añadir la palabra "zapatos" a un mensaje con el `{{canvas_entry_properties.${product_name}}}` de Liquid.
{% endraw %}

Para los lienzos construidos con el editor original, `canvas_entry_properties` sólo puede referenciarse en el primer paso completo de un lienzo.

{% endtab %}

{% tab Propiedades de los eventos %}
Las propiedades de eventos se refieren a las propiedades que usted establece para los eventos y compras personalizados. Estos `event_properties` se pueden utilizar en campañas con entrega basada en acciones y Lienzos.

En el Flujo del lienzo, las propiedades de eventos personalizados y eventos de compra se pueden utilizar en Liquid en cualquier paso de Mensaje que siga a un paso de Rutas de acción. Para Canvas Flow, asegúrate de utilizar {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} si haces referencia a estos `event_properties`. Estos eventos deben ser eventos personalizados o eventos de compra para ser utilizados de esta forma en el componente Mensaje.

En el editor Canvas original, `event_properties` no puede utilizarse en pasos completos programados. Sin embargo, puede utilizar `event_properties` en el primer paso completo de un Canvas basado en acciones, incluso si el paso completo está programado.

En el primer paso de Mensaje que sigue a una Ruta de Acción, puede utilizar `event_properties` relacionado con el evento al que se hace referencia en esa Ruta de Acción. Estos `event_properties` sólo se pueden utilizar si el usuario realmente realizó la acción (no fue al grupo Todos los demás). Puede tener otros pasos (que no sean otra Ruta de Acción o paso de Mensaje) entre esta Ruta de Acción y el paso de Mensaje.

{% endtab %}
{% endtabs %}

### Registrar las compras a nivel de pedido
Si desea registrar las compras a nivel de pedido en lugar de a nivel de producto, puede utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulte nuestra [especificación de objetos de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

## Bloquear eventos de compra

Es posible que en ocasiones identifique eventos de compra que consumen demasiados puntos de datos, que ya no son útiles para su estrategia de marketing o que se registraron por error. Para impedir que estos datos se envíen a Braze, puede bloquear el objeto de datos personalizados mientras su equipo de ingeniería trabaja para eliminarlo del backend de su aplicación o sitio web.

En el panel de control de Braze, puede gestionar las listas de bloqueo desde **Configuración de datos** > **Productos**. Consulte la sección [Gestión de datos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data/) para obtener más información.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), puede encontrar **Productos** en **Gestionar configuración**.
{% endalert %}

[1]: {% image_buster /assets/img/purchase_filter_example.gif %}
[2]: {% image_buster /assets/img/purchase2.png %}
[5]: {% image_buster /assets/img/purchase5.png %}
[6]: {% image_buster /assets/img/nested_object3.png %}
