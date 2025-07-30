---
nav_title: Criterios de salida 
article_title: Criterios de salida 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Este artículo de referencia trata de los criterios de salida y de cómo los usuarios pueden salir de tu Canvas en función de los criterios seleccionados."
tool: Canvas
---

# Criterios de salida

> Al añadir eventos de excepción directamente a tus reglas de entrada de Canvas, tus usuarios pueden salir de tu Canvas en cuanto se produzca el evento al final del paso. Esto ayuda a conseguir un enfoque más específico de la mensajería de Canvas con tu audiencia.

## Configuración de los criterios de salida

En el paso **Público objetivo** del constructor de Canvas, puede establecer criterios de salida para identificar qué usuarios desea que salgan de su Canvas. 

Los criterios de salida incluyen un evento de excepción, que es la acción específica que puede provocar que los usuarios salgan del Canvas.

![Los criterios de salida configurados para reactivar la interacción de los usuarios que han navegado por los productos pero aún no los han añadido a su cesta o no han realizado un pedido.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Seleccionar eventos de excepción {#exception-events}

Cuando un usuario realice el evento de excepción, saldrá del Canvas. Ten en cuenta que los eventos de excepción sólo desencadenarán salidas cuando el usuario esté en el Canvas y avanzando por el recorrido del usuario.

Supongamos que tienes un Canvas configurado para promocionar un nuevo producto. En este caso, la compra del producto sería el evento de excepción. De este modo, después de que un usuario realice la compra, no recibirá más mensajes sobre un producto que ya compró. Los eventos de excepción mantienen tu mensajería relevante y personalizada.

Otros eventos de excepción son:

- Realizar una compra
- Iniciar una sesión
- Realizar un evento personalizado
- Realización de un evento de conversión
- Añadir una dirección de correo electrónico
- Modificar el valor de un atributo personalizado
- Actualizar el estado de una suscripción
- Actualización del estado de un grupo de suscripción
- Interactuar con una campaña
- Introducir una ubicación
- Desencadenar una geovalla
- Enviar un mensaje SMS entrante
- Enviar un mensaje entrante de WhatsApp
- Envío de un mensaje entrante LINE
- Realización de un evento de actualización del carrito
- Realización de un evento de pago completado
- Realización de un evento de salida iniciada

### Utilizar segmentos y filtros

También puedes añadir segmentos y filtros en los criterios de salida. Esto significa que los usuarios que coincidan con el segmento o el filtro saldrán del Canvas y no recibirán más mensajería. 

Por ejemplo, si el primer paso de un Canvas es un paso de Retraso con un retraso de cinco días, los criterios de salida se aplicarán al final de este paso. Así, si un usuario cumple los criterios de salida, saldrá al final de los cinco días.

{% alert note %}
Los atributos de matriz no se admiten actualmente como criterios de salida en eventos de excepción.
{% endalert %}

## Ejemplo

Supongamos que queremos dirigirnos a usuarios que aún no han realizado ninguna compra en nuestra empresa de suministro de mochilas. Para configurar los criterios de salida, lo haríamos:

1. Selecciona **Realizar Compra** como evento de excepción.
2. Selecciona **Añadir desencadenante**. 
3. En **Segmentos**, selecciona **Utilizado en el último día** para que, cuando se lance nuestro Canvas, la audiencia excluya a los usuarios que hayan realizado alguna compra.
4. Para **filtrar**, selecciona **Comportamiento de compra** > **Número de compras** > **Producto comprado**.
5. Configura el grupo de filtrado en `backpack-example exactly 1`. Esto significa que los usuarios que han comprado nuestro producto mochila saldrían del Canvas.

![Configuración de los Criterios de Salida con "Realiza Cualquier Compra" como evento de excepción, de forma que si un usuario realiza cualquier compra, entonces saldrá de este Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}


