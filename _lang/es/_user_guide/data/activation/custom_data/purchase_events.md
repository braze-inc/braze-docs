---
nav_title: Eventos de compra
article_title: Eventos de compra
page_order: 8
page_type: reference
description: "Este artículo de referencia describe los eventos y propiedades de la compra, su uso, segmentación, dónde ver los análisis relevantes y mucho más."
search_rank: 3
---

# Eventos de compra

> Esta página cubre los eventos y propiedades de la compra, su uso, segmentación, dónde ver los análisis relevantes y mucho más.

Los eventos de compra son acciones de compra realizadas por tus usuarios, y se utilizan para registrar las compras dentro de la aplicación y establecer el valor de duración (LTV) para cada perfil de usuario. Estos eventos deben ser configurados por tu equipo. El registro de eventos de compra te permite añadir propiedades como la cantidad y el tipo, lo que te ayuda a dirigirte aún más a tus usuarios en función de estas propiedades.

## Registro de eventos de compra

Puedes registrar las compras pasando un [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) a través del [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), o utilizando una de nuestras bibliotecas SDK que se enumeran a continuación.

A continuación se enumeran los métodos de varias plataformas que se utilizan para registrar las compras. En estas páginas también encontrarás documentación sobre cómo añadir propiedades y cantidades a tu evento de compra. Además, puedes dirigirte a tus usuarios en función de estas propiedades.

- [Android y FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=unity)
- [.NET MAUI]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=roku)

## Ver datos de compra

Una vez que hayas configurado y comenzado a registrar los eventos de compra, puedes ver estos datos de compra en el perfil de un usuario en la [pestaña Resumen]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab).

## Utilizar los datos de compra

Hay varias formas de utilizar los datos de compra en Braze:

- **[Segmentación](#purchase-event-segmentation):** Utiliza los datos de compra para crear segmentos de usuarios en función de su comportamiento de compra.
- **[Personalización](#personalization):** Utilizar los datos de compra para personalizar los mensajes a los usuarios.
- **[Desencadenar mensajes](#trigger-messages):** Configura los mensajes que se desencadenarán en función de los eventos de compra.
- **[Análisis](#analytics):** Analiza tus datos de compra para obtener información sobre el comportamiento de los usuarios y la eficacia de tus campañas de marketing.

### Segmentación {#purchase-event-segmentation}

Puedes desencadenar cualquier número o tipo de campañas de seguimiento basadas en los eventos de compra registrados. Por ejemplo, puedes crear un segmento de usuarios que hayan realizado una compra en los últimos 30 días, o un segmento de usuarios que hayan gastado más de una determinada cantidad.

Los siguientes filtros de segmentación están disponibles para segmentar a los usuarios:

- Primera compra realizada
- Primera compra para la aplicación
- Último producto comprado
- Dinero gastado
- Producto comprado
- Número total de compras
- X dinero gastado en Y días
- X producto comprado en Y días
- X Compra una propiedad en Y días
- X compras en los últimos Y días

Para más detalles sobre cada filtro, consulta el glosario de [filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) y filtra por "Comportamiento de compra".

\![Filtrar por usuarios que hayan realizado exactamente tres compras]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
Para segmentar en función del número de veces que se ha producido una compra concreta, registra esa compra individualmente como un [atributo personalizado incremental]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage).
{% endalert %}

### Personalización

Como cualquier otro tipo de datos que recopiles de tus usuarios, puedes utilizar los datos de compra para personalizar tu mensajería a través de Liquid. Por ejemplo, puedes enviar un correo electrónico personalizado a un usuario recomendándole productos similares a los que acaba de comprar.

Supongamos que tienes una propiedad de evento de compra llamada `last_purchased_product` que almacena el nombre del último producto que ha comprado un usuario. Podrías utilizar esta propiedad para personalizar un mensaje de correo electrónico como éste:

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

En este ejemplo, el mensaje se personaliza en función de la propiedad `last_purchased_product`. Si el último producto que compró el usuario fue "Zapatillas de correr", recibe un mensaje recomendándole pantalones cortos de correr y botellas de agua. Si el último producto era una "Esterilla de yoga", reciben un mensaje recomendando bloques y correas de yoga. Si el `last_purchased_product` es cualquier otra cosa, reciben un mensaje genérico de agradecimiento.

### Desencadenar mensajes

Un caso de uso común es enviar automáticamente un mensaje, como un correo electrónico, cuando un usuario realiza una compra. Por ejemplo, puedes enviar un mensaje de agradecimiento o un código de descuento para una futura compra.

Para ello, crea una campaña basada en una acción o Canvas y, a continuación, configura la acción desencadenante como **Realizar compra**. También puedes especificar condiciones adicionales para el desencadenante, como el producto adquirido o el importe de la compra.

También puedes personalizar tu mensaje desencadenado con Liquid. En el siguiente ejemplo, `${purchase_product_name}` es un atributo personalizado que sustituirías por el nombre real del atributo que almacena el nombre del producto adquirido en tu configuración de Braze.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### Análisis

Además del seguimiento de las métricas de compra para la segmentación, Braze también anota el número de compras de cada producto y los ingresos generados a lo largo del tiempo. Esto puede ser útil para identificar los productos más populares o medir el impacto de una campaña promocional en las ventas.

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
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">Ingresos de toda la vida</a></td>
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

#### Cálculo de ingresos vitalicios

Braze utiliza eventos de compra para calcular los ingresos de por vida (también llamados valor de por vida o LTV) de un usuario, que es una predicción de la ganancia neta atribuida a toda la relación futura con un cliente. Esto puede ayudarte a tomar decisiones informadas sobre las estrategias de captación y retención de clientes.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

Hay dos lugares principales en Braze que puedes consultar para conocer el LTV de tus usuarios:

- Para obtener métricas generales como los *ingresos de por vida* y el *valor de duración por usuario* de cada aplicación y sitio, consulta tu [Informe de ingresos]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
- Para conocer los ingresos de por vida de un usuario concreto, consulta su [perfil de usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab).

##### Impacto de las devoluciones en los ingresos de toda la vida

Cuando utilices eventos de compra para hacer un seguimiento de los datos de compra, debes hacer un seguimiento de los reembolsos registrando un evento de compra Braze con una propiedad negativa `price`. Este enfoque mantiene un total exacto de los ingresos de toda la vida.

Sin embargo, ten en cuenta que el reembolso contará como un evento de compra adicional. Consideremos el siguiente ejemplo. Sam hace su primera compra por 12 $, pero devuelve parte de la compra para que le reembolsen 5 $. El perfil de Sam se registraría:

- 1 compra con un precio de 12
- 1 compra con un precio de -$5
- Ingresos de por vida de 7 $.

Aunque Sam tendría dos eventos de compra en su perfil, en realidad sólo hizo una compra. Es importante tener esto en cuenta si tienes algún segmento o caso de uso construido en torno al número de compras que ha hecho un usuario. Los reembolsos constantes inflarán el recuento de compras en el perfil del usuario.

## Propiedades del evento de compra {#purchase-properties}

Con las propiedades del evento de compra, puedes establecer propiedades en las compras que pueden utilizarse para cualificar aún más las condiciones desencadenantes, aumentar la personalización en la mensajería y generar análisis más sofisticados mediante la exportación de datos sin procesar. Los tipos de valores de propiedad (cadena, numérico, booleano, fecha) varían según la plataforma y suelen asignarse como pares clave-valor.

Por ejemplo, si tienes una aplicación de comercio electrónico y quieres enviar un mensaje a un usuario tras realizar una compra, podrías mejorar adicionalmente tu audiencia objetivo y permitir una mayor personalización de la campaña añadiendo una propiedad de evento de compra de `brand_name`.

**Ejemplo de desencadenamiento basado en las propiedades del evento de compra:**

\![Configuración de entrega basada en acciones para enviar una campaña a los usuarios que compren auriculares con una marca igual a HeadphoneMart]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

Para más información, consulta el [objeto Propiedades de la compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object).

### Segmentación de propiedades del evento

La segmentación de las propiedades de los eventos te permite dirigirte a los usuarios basándote no sólo en los eventos personalizados realizados, sino también en las propiedades asociadas a esos eventos. Esta característica añade opciones de filtrado adicionales al segmentar los eventos de compra y personalizados.

\![]({% image_buster /assets/img/nested_object3.png %}){: style="max-width:80%;margin-left:15px;"}

Estos filtros de segmentación incluyen:
- Ha realizado el evento personalizado con la propiedad Y con valor V X veces en los últimos Y días
- Ha realizado alguna compra con la propiedad Y con valor V X veces en los últimos Y días
- Añade segmentación de 1 a 30 días en todas las compras, eventos y propiedades dentro de compras y eventos.

A diferencia de las [extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/), los segmentos utilizados se actualizan en tiempo real, admiten una cantidad ilimitada de segmentos, ofrecen un historial retrospectivo de 30 días como máximo e incurren en puntos de datos. Debido al cargo adicional por punto de datos, debes ponerte en contacto con tu administrador del éxito del cliente Braze para activar las propiedades del evento para tus eventos personalizados.

Una vez aprobadas, se pueden añadir propiedades adicionales en el panel, en **Configuración de datos** > **Eventos personalizados**, seleccionando **Administrar propiedades**. A continuación, puedes utilizar estas propiedades del evento en el paso de destino de la campaña o del constructor de Canvas.

### Propiedades de la entrada en Canvas y propiedades del evento

{% multi_lang_include canvas_entry_event_properties.md %}

### Registra las compras a nivel de pedido

Para registrar las compras a nivel de pedido en lugar de a nivel de producto, utiliza el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información. 

### Convenciones de denominación de ID de producto

En Braze, ofrecemos algunas convenciones generales de nomenclatura para el objeto de compra `product_id`. Al elegir `product_id`, Braze sugiere utilizar nombres simplistas como el nombre del producto o la categoría del producto (en lugar de SKU) con la intención de agrupar todos los artículos registrados por este `product_id`.

Esto ayuda a que los productos sean fáciles de identificar para su segmentación y desencadenamiento. 

## Bloquear eventos de compra

Ocasionalmente puedes identificar eventos de compra que registran demasiados puntos de datos, que ya no son útiles para tu estrategia de marketing o que se registraron por error. Para impedir que estos datos se envíen a Braze, puedes bloquear el objeto personalizado de datos mientras tu equipo de ingeniería trabaja para eliminarlo del backend de tu aplicación o sitio web.

En el panel de Braze, puedes administrar las listas de bloqueo desde **Configuración de datos** > Productos. Consulta [Gestionar datos de clientes]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) para obtener más información.

