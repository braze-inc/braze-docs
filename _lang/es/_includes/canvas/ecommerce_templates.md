{% tabs %}
{% tab Abandoned browse %}

### Navegación abandonada

Utiliza la plantilla **de navegación abandonada** para promover la interacción con los usuarios que han navegado por los productos, pero no los han añadido a su carrito ni han realizado un pedido.

![Plantilla de Canvas «Navegación abandonada» aplicada con «Reglas de entrada» ampliadas.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Configuración

En la página Canvas, selecciona **Usar una plantilla de Canvas** > **Plantillas de Braze** y, a continuación, aplica la plantilla **Navegación abandonada**. 

##### Configuración predeterminada

La siguiente configuración está preconfigurada en tu Canvas:
- Conceptos básicos 
    - Nombre del Canvas: **Navegación abandonada**
    - Evento de conversión: `ecommerce.order placed`
        - Fecha límite para la conversión: 3 días 
- Cronograma de entrada 
    - Basada en la acción cuando un usuario realiza el`ecommerce.product_viewed`evento.
    - La hora de inicio es cuando creas la plantilla de Canvas.<br><br>![«Opciones basadas en acciones» para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br> 
- Audiencia objetivo 
    - Público de entrada 
        - El correo electrónico **no está en blanco.**
        - También puedes modificar los criterios de audiencia de entrada para satisfacer las necesidades de tu negocio.
    - Controles de entrada
        - Los usuarios son elegibles para volver a entrar en este Canvas una vez que haya finalizado su duración total.
    - Criterios de salida 
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started`, o `ecommerce.order_placed`<br><br>![Controles de entrada y criterios de salida para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br> 
- Enviar configuración 
    - Usuarios que están suscritos o que hicieron la adhesión voluntaria 
- Paso de retardo
    - 1 hora de retraso
- Paso de mensaje 
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla prediseñada. Si utilizas tu propia plantilla de correo electrónico, también puedes hacer referencia a [variables Liquid](#message-personalization), tal y como se muestra en la siguiente sección.

#### Personalización de productos abandonados para correos electrónicos 

A continuación, se muestra un ejemplo de cómo añadir un bloque de producto HTML a tu correo electrónico de navegación abandonada. 

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

##### URL del producto del producto

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

{% endtab %}
{% tab Abandoned cart %}

### Carrito abandonado

Utiliza la plantilla **«Carrito abandonado»** para cubrir las posibles pérdidas de ventas de los clientes que añadieron productos a su carrito pero no continuaron con el proceso de pago ni realizaron el pedido. 

![Plantilla Canvas «Carrito abandonado» aplicada con «Reglas de entrada» ampliadas.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Configuración

En la página Canvas, selecciona **Usar una plantilla de Canvas** > **Plantillas de Braze** y, a continuación, aplica la plantilla **del carrito abandonado**. 

##### Configuración predeterminada

La siguiente configuración está preconfigurada en tu Canvas:
- Conceptos básicos 
    - Nombre del Canvas: **Carrito abandonado**
    - Evento de conversión: `ecommerce.order_placed`
        - Fecha límite para la conversión: 3 días 
- Cronograma de entrada 
    - Desencadenador basado en acciones cuando un usuario desencadena el **evento «Realizar actualización del carrito**» (con ubicación en el menú desplegable).
    - La hora de inicio es cuando creas la plantilla de Canvas.<br><br>![«Opciones basadas en acciones» para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br> 
- Público objetivo 
    - Público de entrada 
        - Has utilizado estas aplicaciones **más de 0** veces. 
        - El correo electrónico **no está en blanco.**
    - Controles de entrada
        - Los usuarios vuelven a ser elegibles inmediatamente para realizar la entrada en Canvas.
    - Criterios de salida 
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started`, o `ecommerce.order_placed`<br><br>![Controles de entrada y criterios de salida para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br> 
- Enviar configuración 
    - Usuarios que están suscritos o que hicieron la adhesión voluntaria 
- Paso de retardo
     - 4 horas de retraso
- Paso de mensaje 
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla prediseñada. Si utilizas tu propia plantilla de correo electrónico, también puedes hacer referencia a [variables Liquid](#message-personalization), tal y como se muestra en la siguiente sección.

#### Cómo funciona la lógica de entrada de carritos abandonados

Cuando un usuario inicia el proceso de pago, tu carrito se marca como `checkout_started`. A partir de ese momento, cualquier actualización posterior del carrito con el mismo ID no dará derecho al usuario a volver a entrar en el proceso de compra abandonado.

1. Cuando un usuario añade un artículo a tu carrito, entra en Canvas.
2. Cada vez que añaden o actualizan artículos, vuelven a entrar en Canvas, lo que mantiene actualizados los datos de su carrito y la mensajería.
3. Cuando el usuario inicia el proceso de pago, tu carrito se etiqueta como `checkout_started`y sales del Canvas.
4. Las futuras actualizaciones del carrito que utilicen el mismo ID de carrito no desencadenarán una nueva entrada, ya que este carrito ya ha pasado a la fase de pago.

Cuando los usuarios pasan a la fase de pago, se les redirige al [Canvas](#abandoned-checkout) [de abandono del pago](#abandoned-checkout), diseñado para usuarios que se encuentran en una fase más avanzada del proceso de compra.

#### Personalización de productos abandonados en el carrito para correos electrónicos {#abandoned-cart-checkout}

Los recorridos de los usuarios que abandonan el carrito de compras requieren una etiqueta de Liquid`shopping_cart` especial para la personalización de los productos. 

A continuación, se muestra un ejemplo de cómo añadir un bloque HTML con tu etiqueta`shopping_cart` de Liquid para añadir productos a tu correo electrónico. 

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

##### URL del carrito HTML

Si deseas redirigir a los usuarios a su carrito, puedes añadir una propiedad de evento anidada bajo el objeto de metadatos, como por ejemplo:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Si utilizas Shopify, crea la URL de tu carrito utilizando esta plantilla Liquid:

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}} 
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### Compra abandonada

Utiliza la plantilla **«Compra abandonada»** para dirigirte a los clientes que iniciaron el proceso de compra pero lo abandonaron antes de realizar el pedido. 

![Plantilla Canvas «Abandoned Checkout» (Abandono del proceso de pago) aplicada con «Entry Rules» (Reglas de entrada) ampliadas.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Configuración

En la página Canvas, selecciona **Usar una plantilla de Canvas** > **Plantillas de Braze** y, a continuación, aplica la plantilla **Abandoned checkout** (Pago abandonado). 

##### Configuración predeterminada

La siguiente configuración está preconfigurada en tu Canvas:

- Conceptos básicos 
    - Nombre del Canvas: **Compra abandonada**
    - Evento de conversión: `ecommerce.order_placed`
        - Fecha límite para la conversión: 3 días 
- Cronograma de entrada 
    - Desencadenante basado en la acción cuando tú realizas el`ecommerce.checkout_started`evento.
    - La hora de inicio es cuando creas la plantilla de Canvas.<br><br>![«Opciones basadas en acciones» para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Audiencia objetivo 
    - Público de entrada 
        - Has utilizado estas aplicaciones **más de 0** veces. 
        - El correo electrónico **no está en blanco.**
    - Controles de entrada
        - Los usuarios vuelven a ser elegibles inmediatamente para realizar la entrada en Canvas.
        - Criterios de salida 
            - Realiza los`ecommerce.order_placed`eventos.<br><br>![Controles de entrada y criterios de salida para el Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Enviar configuración 
    - Usuarios que están suscritos o que hicieron la adhesión voluntaria 
- Paso de retardo
    - 4 horas de retraso
- Paso de mensaje 
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla prediseñada. Si utilizas tu propia plantilla de correo electrónico, también puedes hacer referencia a [variables Liquid](#message-personalization), tal y como se muestra en la siguiente sección.

#### Personalización de carritos abandonados para correos electrónicos

Los procesos de compra abandonados requieren una etiqueta de Liquid`shopping_cart` especial para la personalización de los productos. 

A continuación, se muestra un ejemplo de cómo añadir un bloque HTML con tu etiqueta`shopping_cart` de Liquid para añadir productos a tu correo electrónico. 

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

##### URL de pago

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Confirmación del pedido y cuestionario de satisfacción

Utiliza la plantilla **de cuestionario& sobre la confirmación del pedido** para confirmar los pedidos realizados con éxito y mejorar la satisfacción del cliente.

![Plantilla Canvas aplicada «Confirmación de pedido» con «Reglas de entrada» ampliadas.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Configuración

En la página Canvas, selecciona **Usar una plantilla de Canvas** > **Plantillas de Braze** y, a continuación, aplica la plantilla **de cuestionario& sobre la confirmación del pedido**. 

##### Configuración predeterminada

La siguiente configuración está preconfigurada en tu Canvas:

- Conceptos básicos 
    - Nombre del Canvas: **Confirmación del pedido con cuestionario de satisfacción**
    - Evento de conversión: `ecommerce.session_start`
        - Fecha límite para la conversión: 10 días 
- Cronograma de entrada 
    - Desencadenante basado en la acción cuando tú realizas el`ecommerce.cart_updated`evento.
    - La hora de inicio es cuando creas la plantilla de Canvas.<br><br>![«Opciones basadas en acciones» para el Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Audiencia objetivo 
    - Público de entrada 
        - Has utilizado estas aplicaciones **más de 0** veces. 
        - El correo electrónico **no está en blanco.**
    - Controles de entrada
        - Los usuarios vuelven a ser elegibles inmediatamente para realizar la entrada en Canvas.
    - Criterios de salida 
        - No aplicable<br><br>![Filtros adicionales y controles de entrada para el Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Enviar configuración 
    - Usuarios que están suscritos o que hicieron la adhesión voluntaria 
- Paso de mensaje 
    - Revisa la plantilla de correo electrónico y el bloque HTML con un ejemplo de plantilla Liquid para añadir productos a tu mensaje en la plantilla prediseñada. Si utilizas tu propia plantilla de correo electrónico, también puedes hacer referencia a [variables Liquid](#message-personalization), tal y como se muestra en la siguiente sección.

#### Personalización de la confirmación de pedidos para correos electrónicos

A continuación, se muestra un ejemplo de cómo añadir un bloque de producto HTML a la confirmación del pedido una vez que este se ha realizado.

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

##### URL del estado del pedido

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}