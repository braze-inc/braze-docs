---
nav_title: Casos de uso del comercio electrónico
article_title: Casos de uso del comercio electrónico
alias: /ecommerce_use_cases/
page_order: 4
description: "Este artículo de referencia cubre varias plantillas Braze prediseñadas, adaptadas específicamente para especialistas en marketing de comercio electrónico, que facilitan la aplicación de estrategias esenciales."
toc_headers: h2
---

# Casos de uso del comercio electrónico

> Braze Canvas ofrece varias plantillas preconstruidas adaptadas específicamente para especialistas en marketing de comercio electrónico, lo que facilita la aplicación de estrategias esenciales. Esta página ofrece algunas plantillas clave que puedes utilizar para mejorar tus recorridos del cliente.

{% alert important %}
[Los eventos recomendados por eCommerce]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/) están actualmente en acceso anticipado. Ponte en contacto con tu administrador del éxito del cliente de Braze si estás interesado en participar en este acceso anticipado. <br><br>Si utilizas el nuevo conector de Shopify, los eventos recomendados de comercio electrónico estarán disponibles automáticamente a través de la integración.
{% endalert %}

## Utilizar una plantilla Canvas

Para utilizar una plantilla Canvas:
1. Ve a **Mensajería** > **Canvas**.
2. Selecciona **Crear lienzo** > **Utilizar una plantilla de lienzo**.
3. Busca en la pestaña **Plantillas Braze** la plantilla que quieras utilizar. Puedes obtener una vista previa de una plantilla seleccionando su nombre.
4. Selecciona **Aplicar plantilla** para la plantilla que quieras utilizar.<br><br>![La página "Plantillas Canvas" se abre en la pestaña "Plantillas Braze" y muestra una lista de las plantillas utilizadas recientemente y de las plantillas Braze seleccionables.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## plantillas eCommerce

- [Navegar abandonada](#abandoned-browse)
- [Carrito abandonado](#abandoned-cart)
- [Compra abandonada](#abandoned-checkout)
- [Confirmación del pedido y cuestionario de opinión](#order-confirmation--feedback-survey)

## Navegar abandonada

Utiliza la plantilla de **navegación abandonada** para interactuar con usuarios que han navegado por productos pero no los han añadido al carrito ni han realizado un pedido.

![Una plantilla Canvas "Exploración abandonada" aplicada con "Reglas de entrada" ampliadas.]({% image_buster /assets/img_archive/abandoned_browse.png %})

### Configurar

En la página Lienzo, selecciona **Utilizar una plantilla de lienzo** > **Plantillas de Braze** y, a continuación, aplica la plantilla de **exploración Abandonado**. 

#### Configuraciones predeterminadas

Las siguientes configuraciones están preconfiguradas en tu Canvas:
- Conceptos básicos 
    - Nombre del lienzo: **Navegar abandonada**
    - Evento de conversión: `ecommerce.order placed`
        - Plazo de conversión: 3 días 
- Cronograma de entrada 
    - Basado en la acción cuando un usuario realiza el evento `ecommerce.product_viewed` 
    - La hora de inicio es cuando creas la plantilla Canvas<br><br>!["Opciones basadas en acciones" para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- Audiencia objetivo 
    - Público de entrada 
        - El correo electrónico **no está en blanco**
        - También puedes modificar los criterios de audiencia de entrada para adaptarlos a las necesidades de tu empresa
    - Controles de entrada
        - Los usuarios son elegibles para volver a entrar en este Canvas una vez finalizada toda la duración del mismo.
    - Criterios de salida 
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started`, o `ecommerce.order_placed`<br><br>![Controles de entrada y criterios de salida del Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- Enviar configuración 
    - Usuarios que están suscritos o que hicieron la adhesión voluntaria 
- Paso de retardo
    - 1 hora de retraso
- Paso de mensaje 
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla preconstruida. Si utilizas tu propia plantilla de correo electrónico, también puedes hacer referencia a [variables Liquid](#message-personalization), como se demuestra en la sección siguiente.

### Personalización de productos de navegación abandonada para correos electrónicos 

Aquí tienes un ejemplo de cómo añadir un bloque HTML de producto para tu correo electrónico de navegación abandonada. 

{% raw %}
```java
<table style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

#### URL del producto

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

## Carrito abandonado

Utiliza la plantilla **Carrito abandonado** para cubrir las posibles ventas perdidas de clientes que añadieron productos a su carrito pero no continuaron con la compra o no hicieron un pedido. 

![Una plantilla Canvas "Carrito Abandonado" aplicada con "Reglas de Entrada" ampliadas.]({% image_buster /assets/img_archive/abandoned_cart.png %})

### Configurar

En la página Canvas, selecciona **Utilizar una plantilla Canvas** > **Plantillas Braze** y, a continuación, aplica la plantilla **Carrito abandonado**. 

#### Configuraciones predeterminadas

Las siguientes configuraciones están preconfiguradas en tu Canvas:
- Conceptos básicos 
    - Nombre del lienzo: **Carrito abandonado**
    - Evento de conversión: `ecommerce.order_placed`
        - Plazo de conversión: 3 días 
- Cronograma de entrada 
    - Desencadenante basado en la acción cuando un usuario desencadena el **Evento Actualizar Carro** (situado en el desplegable)
    - La hora de inicio es cuando creas la plantilla Canvas<br><br>!["Opciones basadas en acciones" para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- Público objetivo 
    - Público de entrada 
        - Ha utilizado estas aplicaciones **más de 0** veces 
        - El correo electrónico **no está en blanco**
    - Controles de entrada
        - Los usuarios son inmediatamente elegibles de nuevo para la entrada en Canvas
    - Criterios de salida 
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started`, o `ecommerce.order_placed`<br><br>![Controles de entrada y criterios de salida del Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- Enviar configuración 
    - Usuarios que están suscritos o que hicieron la adhesión voluntaria 
- Paso de retardo
     - 4 horas de retraso
- Paso de mensaje 
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla preconstruida. Si utilizas tu propia plantilla de correo electrónico, también puedes hacer referencia a [variables Liquid](#message-personalization), como se demuestra en la sección siguiente.

### Personalización del producto del carrito abandonado para correos electrónicos {#abandoned-cart-checkout}

Los viajes de usuarios con carritos abandonados requieren una etiqueta de Liquid `shopping_cart` especial para la personalización del producto. 

Aquí tienes un ejemplo de cómo añadir un bloque HTML con tu etiqueta de Liquid `shopping_cart` para añadir productos a tu correo electrónico. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Si utilizas Shopify, añade el nombre de tu catálogo para obtener la URL de la imagen variante.
{% endalert %}

#### URL HTML del carrito

Si quieres dirigir a los usuarios de vuelta a su carrito, puedes añadir una propiedad de eventos anidados bajo el objeto medata, como por ejemplo

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Si utilizas Shopify, crea la URL de tu carrito utilizando esta plantilla Liquid:

{% raw %}
```liquid
{{context.source}}/checkouts/cn/{{context.cart_id}}
```
{% endraw %}

## Compra abandonada

Utiliza la plantilla **Pago abandonado** para dirigirte a los clientes que iniciaron el proceso de pago pero lo abandonaron antes de realizar el pedido. 

![Una plantilla Canvas "Pago Abandonado" aplicada con "Reglas de Entrada" ampliadas.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

### Configurar

En la página Canvas, selecciona **Utilizar una plantilla Canvas** > **Plantillas Braze** y, a continuación, aplica la plantilla **Pago abandonado**. 

#### Configuraciones predeterminadas

Las siguientes configuraciones están preconfiguradas en tu Canvas:

- Conceptos básicos 
    - Nombre del lienzo: **Compra abandonada**
    - Evento de conversión: `ecommerce.order_placed`
        - Plazo de conversión: 3 días 
- Cronograma de entrada 
    - Acción desencadenante cuando un usuario realiza el evento `ecommerce.checkout_started` 
    - La hora de inicio es cuando creas la plantilla Canvas<br><br>!["Opciones basadas en acciones" para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Audiencia objetivo 
    - Público de entrada 
        - Ha utilizado estas aplicaciones **más de 0** veces 
        - El correo electrónico **no está en blanco**
    - Controles de entrada
        - Los usuarios son inmediatamente elegibles de nuevo para la entrada en Canvas
        - Criterios de salida 
            - Realiza los eventos `ecommerce.order_placed` <br><br>![Controles de entrada y criterios de salida del Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Enviar configuración 
    - Usuarios que están suscritos o que hicieron la adhesión voluntaria 
- Paso de retardo
    - 4 horas de retraso
- Paso de mensaje 
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla preconstruida. Si utilizas tu propia plantilla de correo electrónico, también puedes hacer referencia a [variables Liquid](#message-personalization), como se demuestra en la sección siguiente.

### Personalización del pago abandonado para correos electrónicos

Los recorridos de usuario de pago abandonado requieren una etiqueta de Liquid `shopping_cart` especial para la personalización del producto. 

Aquí tienes un ejemplo de cómo añadir un bloque HTML con tu etiqueta de Liquid `shopping_cart` para añadir productos a tu correo electrónico. 

{% raw %}
```java
<table style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

#### URL de pago

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

## Confirmación del pedido y cuestionario de opinión

Utiliza la plantilla de **cuestionario de confirmación de pedido y opinión** para confirmar los pedidos realizados con éxito y aumentar la satisfacción del cliente.

![Una plantilla Canvas de "Confirmación de pedido" aplicada con "Reglas de entrada" ampliadas.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

### Configurar

En la página Canvas, selecciona **Utilizar una plantilla Canvas** > **Plantillas Braze** y, a continuación, aplica la plantilla **Confirmación de pedido y cuestionario de opinión**. 

#### Configuraciones predeterminadas

Las siguientes configuraciones están preconfiguradas en tu Canvas:

- Conceptos básicos 
    - Nombre del lienzo: **Confirmación de pedido con cuestionario de opinión**
    - Evento de conversión: `ecommerce.session_start`
        - Plazo de conversión: 10 días 
- Cronograma de entrada 
    - Acción desencadenante cuando un usuario realiza el evento `ecommerce.cart_updated` 
    - La hora de inicio es cuando creas la plantilla Canvas<br><br>!["Opciones basadas en acciones" para el Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Audiencia objetivo 
    - Público de entrada 
        - Ha utilizado estas aplicaciones **más de 0** veces 
        - El correo electrónico **no está en blanco**
    - Controles de entrada
        - Los usuarios son inmediatamente elegibles de nuevo para la entrada en Canvas
    - Criterios de salida 
        - No aplicable<br><br>![Filtros adicionales y controles de entrada para el Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Enviar configuración 
    - Usuarios que están suscritos o que hicieron la adhesión voluntaria 
- Paso de mensaje 
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla preconstruida. Si utilizas tu propia plantilla de correo electrónico, también puedes hacer referencia a [variables Liquid](#message-personalization), como se demuestra en la sección siguiente.

### Personalización de la confirmación del pedido para los correos electrónicos

Aquí tienes un ejemplo de cómo añadir un bloque HTML de producto a tu confirmación de pedido después de realizar un pedido.

{% raw %}
```json
<table style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

#### URL del estado del pedido

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

## Personalización de mensajes

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) es un potente lenguaje de plantillas utilizado por Braze que te permite crear contenido dinámico y personalizado para tus clientes. Al utilizar las etiquetas de Liquid, puedes personalizar los mensajes en función de los datos de clientes, la información sobre productos y otras variables, mejorando la experiencia de compra e impulsando la interacción.

### Características principales de Liquid

- **Contenido dinámico:** Inserta en tus mensajes información específica del cliente, como nombres, detalles del pedido y preferencias.
- **Lógica condicional:** Utiliza sentencias if/else para mostrar contenidos diferentes en función de condiciones específicas (como la ubicación del cliente y su historial de compras).
- **Bucles:** Iterar sobre colecciones de productos o datos de clientes para mostrar listas o cuadrículas de elementos.

### Primeros pasos con Liquid

Para empezar a personalizar tus mensajes utilizando etiquetas de Liquid, puedes consultar los siguientes recursos:

- Referencia de [datos de Shopify]({{site.baseurl}}/shopify_features/#shopify-data) con etiquetas de Liquid predefinidas
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## Segmentación

Utiliza los segmentos Braze para crear segmentos de clientes específicos basados en atributos y comportamientos concretos, y entregar mensajes y campañas personalizados. Con esta potente característica, puedes interactuar eficazmente con tus clientes llegando a la audiencia adecuada con el mensaje correcto en el momento adecuado.

Para más información sobre cómo empezar con los segmentos, consulta [Acerca de los segmentos Braze]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments).

### Eventos recomendados

Los eventos de comercio electrónico se basan en [eventos recomendados]({{site.baseurl}}/recommended_events/).
Como los eventos recomendados son eventos personalizados más opinados, puedes buscar los nombres de eventos de comercio electrónico recomendados seleccionando cualquier [filtro de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters).

### Filtros de comercio electrónico

Segmenta a tus usuarios con filtros de comercio electrónico, como **Fuente de comercio electrónico** e **Ingresos totales**, yendo a la sección **Comercio electrónico** dentro del segmentador.

![Filtros de segmento desplegables con filtros "Ecommerce".]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:80%"}

{% alert important %}
Con el tiempo, el evento de compra quedará obsoleto y se sustituirá por [los eventos recomendados por eCommerce]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/). Cuando esto ocurra, los filtros de segmento dejarán de aparecer en el comportamiento de compra. Para ver una lista completa de eventos de compra, consulta [Registrar eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

## Propiedades de eventos anidados

Para segmentar por propiedades de eventos anidados, puedes aprovechar [las Extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions). Por ejemplo, puedes utilizar las extensiones de segmento para encontrar quién ha comprado el producto "SKU-123" en los últimos 90 días.

## Análisis

{% alert note %}
En este momento, la integración de Shopify no permite rellenar el [evento de compra]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events#purchase-events) Braze. Como resultado, los filtros de compra, las etiquetas de Liquid, los desencadenantes basados en acciones y los análisis deben utilizar el evento ecommerce.order_placed.
{% endalert %}

Para crear un [informe de Eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) basado en quién ha realizado un evento admitido a través de la integración, puedes especificar el [nombre]({{site.baseurl}}/shopify_data_features/) concreto del [evento]({{site.baseurl}}/shopify_data_features/).

Para obtener información sobre las tendencias relacionadas con los pedidos realizados desde tus Lienzos lanzados, tendrás que configurar un [Panel de Conversiones]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard) y especificar tus Lienzos.

Para casos de uso de informes más avanzados, puedes utilizar el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/) Braze para generar informes personalizados. 

