{% tabs %}
{% tab Abandoned browse %}

### Navegar abandonada

Utiliza la plantilla de **navegación abandonada** para interactuar con usuarios que han navegado por productos pero no los han añadido al carrito ni han realizado un pedido.

![Una plantilla Canvas "Exploración abandonada" aplicada con "Reglas de entrada" ampliadas.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Configurar

En la página Lienzo, selecciona **Utilizar una plantilla de lienzo** > **Plantillas de Braze** y, a continuación, aplica la plantilla de **exploración Abandonado**. 

##### Configuraciones predeterminadas

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

#### Personalización de productos de navegación abandonada para correos electrónicos 

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

##### URL del producto

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}    

{% endtab %}
{% tab Abandoned cart %}

### Carrito abandonado

Utiliza la plantilla **Carrito abandonado** para cubrir las posibles ventas perdidas de clientes que añadieron productos a su carrito pero no continuaron con la compra o no hicieron un pedido. 

![Una plantilla Canvas "Carrito abandonado" aplicada con "Reglas de entrada" ampliadas.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Configurar

En la página Canvas, selecciona **Utilizar una plantilla Canvas** > **Plantillas Braze** y, a continuación, aplica la plantilla **Carrito abandonado**. 

##### Configuraciones predeterminadas

Las siguientes configuraciones están preconfiguradas en tu Canvas:
- Conceptos básicos 
    - Nombre del lienzo: **Carrito abandonado**
    - Evento de conversión: `ecommerce.order_placed`
        - Plazo de conversión: 3 días 
- Cronograma de entrada 
    - Desencadenante basado en la acción cuando un usuario desencadena el **Evento Actualizar carro** (situado en el desplegable)
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

#### Cómo funciona la lógica de reentrada de un carrito abandonado

Cuando un usuario inicia el proceso de pago, su cesta se marca como `checkout_started`. A partir de ese momento, cualquier otra actualización del carrito con el mismo ID de carrito no permitirá al usuario volver a entrar en el recorrido de usuario del carrito abandonado.

1. Cuando un usuario añade un artículo a su cesta, entra en el Canvas.
2. Cada vez que añaden o actualizan artículos, vuelven a entrar en el Canvas, lo que mantiene actualizados los datos de su carrito y su mensajería.
3. Cuando el usuario inicia el proceso de pago, su cesta se etiqueta como `checkout_started`, y sale del Canvas.
4. Cualquier actualización futura del carrito que utilice el mismo ID no desencadenará una nueva entrada porque este carrito ya ha pasado a la fase de pago.

Cuando los usuarios pasan al proceso de compra, se dirigen al [Canvas de compra abandonada](#abandoned-checkout), que está diseñado para los usuarios que están más avanzados en el proceso de compra.

#### Personalización del producto del carrito abandonado para correos electrónicos {#abandoned-cart-checkout}

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

##### URL HTML del carrito

Si quieres dirigir a los usuarios de vuelta a su carrito, puedes añadir una propiedad de eventos anidada bajo el objeto de metadatos, como por ejemplo

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

Utiliza la plantilla **Pago abandonado** para dirigirte a los clientes que iniciaron el proceso de pago pero lo abandonaron antes de realizar el pedido. 

![Una plantilla Canvas "Pago Abandonado" aplicada con "Reglas de entrada" ampliadas.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Configurar

En la página Canvas, selecciona **Utilizar una plantilla Canvas** > **Plantillas Braze** y, a continuación, aplica la plantilla **Pago abandonado**. 

##### Configuraciones predeterminadas

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

#### Personalización del pago abandonado para correos electrónicos

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

##### URL de pago

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Confirmación del pedido y cuestionario de opinión

Utiliza la plantilla de **cuestionario de opinión de confirmación de pedido & ** para confirmar el éxito de los pedidos y mejorar la satisfacción del cliente.

![Una plantilla Canvas de "Confirmación de pedido" aplicada con "Reglas de entrada" ampliadas.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Configurar

En la página Canvas, selecciona **Utilizar una plantilla Canvas** > **Plantillas Braze** y, a continuación, aplica la plantilla de **encuesta de opinión de Confirmación de pedido & **. 

##### Configuraciones predeterminadas

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

#### Personalización de la confirmación del pedido para los correos electrónicos

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

##### URL del estado del pedido

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}