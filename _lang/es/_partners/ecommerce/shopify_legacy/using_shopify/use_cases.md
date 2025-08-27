---
nav_title: Ejemplos
article_title: "Casos de uso de Shopify en Braze"
description: "Este artículo de referencia describe casos de uso comunes para usuarios principiantes y avanzados en Shopify."
page_type: partner
search_tag: Partner
alias: "/shopify_use_cases_legacy/"
page_order: 2
---

# Casos prácticos

> ¿Te interesa ver cómo puedes aprovechar tu integración con Shopify para crear mensajes oportunos y eficaces para tus usuarios? Consulta las siguientes secciones sobre casos de uso comunes [para usuarios principiantes](#beginner) y [avanzados](#advanced) para obtener más información.

{% multi_lang_include alerts.md alert='Shopify obsoleto' %}

## Principiante

Estos son algunos casos de uso simples pero efectivos que puedes crear poco después de configurar Shopify. No se requiere ningún trabajo adicional. 

### Campañas

Estos casos de uso transaccionales te permiten alertar a tus usuarios cuando hay una actualización en su pedido de Shopify.

{% tabs local %}
{% tab Devolución %}
**Evento de reembolso de Shopify** - `shopify_created_refund`

Los usuarios recibieron un reembolso, parcial o completo. Esta campaña informa al usuario de que su pedido se ha reembolsado correctamente.

![Campaña basada en acciones que ingresa usuarios que realizan el evento personalizado "shopify_created_refund".]({% image_buster /assets/img/Shopify/refund.png %}){: style="max-width:45%;"}

**Ejemplo de mensajería**

![Envía un correo electrónico con el texto "Tu pedido ha sido reembolsado, sentimos que te hayas sentido decepcionado con tu pedido. Hemos enviado correctamente tu reembolso. Por favor, espera de 3 a 5 días laborables para que los fondos aparezcan en tu extracto" y un botón "Ver cuenta".]({% image_buster /assets/img/Shopify/refund2.png %}){: style="max-width:80%;border:0;"}
{% endtab %}
{% tab Anulación %}
**Evento de cancelación de Shopify** - `shopify_cancelled_order`

Los usuarios podían cancelar sus pedidos antes de que se procesen. Esta campaña informa al usuario de que su compra se ha cancelado correctamente. 

![Campaña basada en acciones que ingresa usuarios que realizan el evento personalizado "shopify_cancelled_order".]({% image_buster /assets/img/Shopify/cancellation.png %}){: style="max-width:45%;"}

**Ejemplo de mensajería**

![Correo electrónico con el texto "Tu pedido ha sido cancelado, ¡siento verte marchar! Hemos cancelado correctamente tu pedido. Por favor, espera de 3 a 5 días laborables para que los fondos aparezcan en tu extracto" y un botón "Ver cuenta".]({% image_buster /assets/img/Shopify/cancellation2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% tab Pedido procesado %}
**Shopify procesó el evento** - `shopify_fulfilled_order`

Todas las partidas del pedido de un usuario se han realizado correctamente. Esta campaña informa al usuario de que su pedido se ha procesado en su totalidad.

![Campaña basada en acciones que ingresa usuarios que realizan el evento personalizado "shopify_fulfilled_order".]({% image_buster /assets/img/Shopify/fulfilled.png %}){: style="max-width:45%;"}

**Ejemplo de mensajería**

![Mensaje de texto con el texto "¡Tu pedido se ha cumplido! ¡Se han entregado todos los artículos de tu cesta! Entra en tu cuenta y confirma la recepción. Puntos extra por dejar comentarios"]({% image_buster /assets/img/Shopify/fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Pedido parcialmente procesado %}
**Evento Shopify parcialmente procesado** - `shopify_partially_fulfilled_order`

Algunas partidas del pedido de un usuario se han procesado correctamente. Esta campaña permite a los usuarios saber que se ha cumplido una parte de su pedido.

![Campaña basada en acciones que ingresa usuarios que realizan el evento personalizado "shopify_partially_fulfilled_order".]({% image_buster /assets/img/Shopify/partially_fulfilled.png %}){: style="max-width:45%;"}

**Ejemplo de mensajería**

![Mensaje de texto con el texto "¡Tu pedido se ha procesado parcialmente! ¡Hemos entregado algunos de los artículos de tu pedido y el resto está en camino! Te enviaremos otra alerta cuando la entrega se haya completado por completo."]({% image_buster /assets/img/Shopify/partially_fulfilled2.png %}){: style="max-width:40%;border:0;"}

{% endtab %}
{% tab Pedido pagado %}
**Evento de pedido pagado de Shopify** - `shopify_paid_order`

El usuario paga su pedido y el estado del mismo cambia a pagado. Esta campaña permite al usuario saber que su pago con tarjeta de crédito fue capturado o que el pedido fue marcado como pagado si hubo un pago manual.

![Campaña basada en acciones que ingresa usuarios que realizan el evento personalizado "shopify_paid_order".]({% image_buster /assets/img/Shopify/paid.png %}){: style="max-width:45%;"}

**Ejemplo de mensajería**

![Correo electrónico con el texto "¡Hemos recibido tu Pago! Woohoo ¡tu pedido ha sido pagado! Por favor, espera 1-2 días laborables para que procesemos el pago y preparemos tus artículos. Entonces lo enviaremos" y un botón "Ver cuenta".]({% image_buster /assets/img/Shopify/paid2.png %}){: style="max-width:80%;border:0;"}

{% endtab %}
{% endtabs  %}
### Canvas

{% tabs local %}
{% tab Canvas de compra abandonada %}

**Canvas de compra abandonada**

Los usuarios abandonan el flujo de pago y no completan las transacciones antes de marcharse. Este Canvas te permite enviar recordatorios automatizados a los usuarios que no han finalizado sus transacciones para que vuelvan al flujo de pago.

Evento de entrada basado en la acción: `shopify_abandoned_checkout`<br>
Evento de excepción: `shopify_created_order` o Compra

![]({% image_buster /assets/img/Shopify/abandoned_checkout_canvas.gif %})

{% endtab %}
{% tab Canvas posterior a la compra %}

**Canvas posterior a la compra**

Los usuarios han realizado una compra con éxito, y ahora quieres saber qué les ha parecido su compra. Este Canvas te permite enviar mensajes de seguimiento a tu usuario para recoger sus opiniones. 

Evento de entrada basado en una acción: `shopify_created_order` o Compra

![]({% image_buster /assets/img/Shopify/post_purchase_canvas.gif %})

{% endtab %}
{% endtabs %}

## Avanzado

Una vez que te hayas familiarizado con la plataforma, podrás configurar casos de uso más complejos.

### Campañas

{% tabs local %}
{% tab Recomendaciones de los usuarios %}
**Recomendaciones de los usuarios**
![]({% image_buster /assets/img/Shopify/product_view.png %}){: style="max-width:30%;border:0;float:right;"}

El usuario hizo clic o vio un artículo pero no lo compró. Esta campaña envía un mensaje de seguimiento al usuario con artículos iguales o similares (recomendados por Connected Content) para incitarle a comprar uno de ellos.

Evento de entrada basado en la acción: `shopify_product_clicked` o `shopify_product_viewed`<br>
![]({% image_buster /assets/img/Shopify/product_view3.png %}){: style="max-width:45%;border:0;"}
<br><br>
Evento de excepción: `shopify_created_order` o Compra<br>
![]({% image_buster /assets/img/Shopify/product_view2.png %}){: style="max-width:50%;"}

{% endtab %}
{% endtabs %}

### Canvas

{% tabs local %}
{% tab Reembolso Winback Canvas %}

**Reembolso Winback Canvas**

Los usuarios recibieron un reembolso, parcial o completo. Este Canvas envía mensajes de seguimiento para conseguir que el usuario vuelva a realizar su compra.

Evento de entrada basado en la acción: `shopify_created_refund`<br>
Evento de excepción: `shopify_created_order` o Compra

![]({% image_buster /assets/img/Shopify/winback_canvas_refund.gif %})


{% endtab %}
{% tab Canvas de anulación Winback %}

**Canvas de anulación Winback**

Los usuarios podían cancelar sus pedidos antes de que se procesen. Este Canvas envía mensajes de seguimiento para conseguir que el usuario vuelva a realizar su compra.

Evento de entrada basado en la acción: `shopify_cancelled_order`<br>
Evento de excepción: `shopify_created_order` o Compra

![]({% image_buster /assets/img/Shopify/winback_canvas_cancel.gif %})


{% endtab %}
{% endtabs %}