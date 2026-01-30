---
nav_title: Panel de ingresos de comercio electrónico
article_title: Panel de ingresos de comercio electrónico
alias: "/ecommerce_revenue_dashboard/"
page_order: 6
description: "Este artículo ofrece un resumen del panel de atribución de ingresos de comercio electrónico - Último toque."
---

# Panel de ingresos de comercio electrónico

> El panel **Ingresos de comercio electrónico - Atribución** al último **contacto** hace un seguimiento de los ingresos atribuidos al último contacto para campañas y Lienzos utilizando [eventos recomendados de comercio electrónico]({{site.baseurl}}/ecommerce_events/). Utiliza este panel para saber qué mensajes generan ingresos y para controlar el rendimiento general del comercio electrónico a lo largo del tiempo.

{% alert note %}
Los eventos recomendados por eCommerce están actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente de Braze si estás interesado en participar en este acceso anticipado. <br><br>Si utilizas el nuevo [conector de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector), estos eventos recomendados estarán disponibles automáticamente a través de la integración. De lo contrario, estos eventos deben implementarse antes de que los datos aparezcan en este panel.
{% endalert %}

Para ver tu panel de ingresos de **comercio** electrónico, ve a **Análisis** > **Creador de paneles** y, a continuación, selecciona **Ingresos de comercio electrónico - Atribución del último contacto**. Este panel informa sobre los ingresos atribuidos a la última campaña o Canvas con el que interactuó un usuario antes de realizar un pedido, dentro de la ventana de conversión seleccionada.

## Métricas disponibles

| Métrica | Definición |
| --- | --- |
| Ingresos por comercio electrónico | Total de ingresos atribuidos al último contacto en función del intervalo de fechas y la ventana de conversión seleccionados. |
| Pedidos diarios realizados | El número medio de pedidos distintos realizados al día. |
| Ingresos medios diarios por comercio electrónico | Promedio de ingresos atribuidos por día para el periodo de tiempo seleccionado. |
| Ingresos por comercio electrónico a lo largo del tiempo | Una serie temporal de los ingresos atribuidos en el intervalo de fechas seleccionado. |
| Ingresos de comercio electrónico por campaña | Ingresos atribuidos desglosados por campaña. | 
| Ingresos de comercio electrónico por Canvas | Ingresos atribuidos desglosados por Canvas. |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Modelo de atribución

El panel **Ingresos de comercio electrónico - Atribución de** último toque utiliza la atribución de último toque. Esto significa que los ingresos se atribuyen a la campaña o Canvas de Braze más reciente con el que el usuario haya interactuado antes de realizar un pedido.

{% alert important %}
Las interacciones de mensajes deben haberse producido dentro de la ventana de conversión seleccionada. Los pedidos sin una interacción de mensaje elegible dentro de la ventana de conversión no se atribuyen.
{% endalert %}

## Datos incluidos

El panel de **atribución Ingresos de comercio electrónico - Último toque** extrae datos de los eventos recomendados de comercio electrónico:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

Los recuentos de ingresos y pedidos utilizan cálculos estandarizados de Braze.

| Métrica | Cálculo |
| --- | --- |
| Ingresos totales | Suma de los valores del pedido realizado - Suma de los valores reembolsados |
| Pedidos totales | Pedidos distintos realizados - Pedidos distintos anulados |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

### Datos excluidos

No se incluyen las compras registradas mediante el evento de compra heredado. Actualmente, el panel de **atribución de ingresos de comercio electrónico - Último toque** no admite características vinculadas a eventos de compra heredados, como los informes de LTV o ingresos dentro de campañas o Canvases. 


## Manejo de divisas

Todos los ingresos se muestran en USD. Las divisas distintas del USD se convierten a USD utilizando la tasa de cambio de la fecha en que se comunica el suceso. Para evitar la conversión, codifica la moneda en `USD` cuando envíes eventos.
