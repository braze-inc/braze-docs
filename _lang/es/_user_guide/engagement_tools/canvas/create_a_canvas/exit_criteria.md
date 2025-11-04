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

### Cómo salen los usuarios

Tras realizar el evento de salida, los usuarios salen del Canvas en cuanto se sale del paso en el que se encuentran. Por ejemplo, si un usuario está en un paso de Retraso durante 30 días y realiza el evento de salida el primer día del paso de Retraso, el usuario no saldrá del Canvas hasta dentro de 29 días.

Consideremos otro ejemplo cuando se utilizan criterios de salida basados en el tiempo. Un usuario introduce un paso de Retraso fijado en 24 horas el 1 de julio a las 12 de la mañana. En este periodo de retraso, realizan el evento de salida "Última compra realizada hace menos de 1 hora" a las 3 de la madrugada. Este usuario será evaluado según los criterios de salida el 2 de julio a las 12 de la mañana, que es cuando finaliza la duración del paso de Retraso. Como han pasado 21 horas desde su compra el 1 de julio a las 3 de la madrugada, no saldrán del Canvas porque no hicieron una compra en la hora siguiente a salir del paso en Retraso el 2 de julio. Esto afecta al "Total de salidas por criterios de salida" en tus análisis del Canvas, que sólo se actualizan después de que un usuario haya salido completamente del Canvas.

## Configuración de los criterios de salida

En el paso **Audiencia objetivo** del creador de Canvas, puedes configurar los criterios de salida para identificar qué usuarios quieres que salgan de tu Canvas. 

Los criterios de salida incluyen un evento de excepción, que es la acción específica que puede provocar que los usuarios salgan del Canvas.

\![Los criterios de salida configurados para reactivar la interacción de los usuarios que han navegado por productos pero aún no los han añadido a su cesta ni han realizado un pedido.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Seleccionar eventos de excepción {#exception-events}

Cuando un usuario realice el evento de excepción, saldrá del Canvas. Ten en cuenta que los eventos de excepción sólo desencadenarán salidas cuando el usuario esté en el Canvas y avanzando por el recorrido del usuario.

Supongamos que tienes un Canvas configurado para promocionar un nuevo producto. En este caso, la compra del producto sería el evento de excepción. De este modo, después de que un usuario realice la compra, no recibirá más mensajes sobre un producto que ya compró. Los eventos de excepción mantienen tu mensajería relevante y personalizada.

Otros eventos de excepción son:

- Hacer una compra
- Iniciar una sesión
- Realización de un evento personalizado
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
- Realización de un evento de inicio de pago

#### Pasos programados

Si se programa un paso en Canvas, el usuario abandonará inmediatamente el Canvas después de que se produzca el evento de excepción. Supongamos que un usuario entra en un Canvas en el que el primer paso tiene un retraso de una semana y un evento de excepción. Si el usuario realiza el evento de excepción el día 5, saldría inmediatamente después de realizar el evento de excepción (el día 5). 
 
#### Pasos desencadenados

Si un paso en Canvas es desencadenado por un evento, se cancelará el último envío programado en cola desde ese desencadenante, pero el usuario permanecerá dentro del Canvas mientras dure la ventana. Eso significa que el usuario puede seguir recibiendo el paso si vuelve a realizar el evento desencadenante dentro de la ventana. Cuando pase la ventana, el usuario saldrá del Canvas.

### Utilizar segmentos y filtros

También puedes añadir segmentos y filtros en los criterios de salida. Esto significa que los usuarios que coincidan con el segmento y el filtro saldrán del Canvas y no recibirán más mensajería. 

Por ejemplo, si el primer paso de un Canvas es un paso de Retraso con un retraso de cinco días, los criterios de salida se aplicarán al final de este paso. Así, si un usuario cumple los criterios de salida, saldrá al final de los cinco días.

{% alert note %}
Los atributos de matriz no se admiten actualmente como criterios de salida en eventos de excepción.
{% endalert %}

### Tener el mismo evento de salida y de conversión

Cuando el evento de salida y el evento de conversión sean el mismo, se contabilizarán tanto el evento de conversión como el de salida. Por ejemplo, si un Canvas tiene un paso de Retraso y un usuario realiza los criterios de salida mientras está en ese paso de Retraso, el evento de salida se incrementará en cuanto el usuario salga del paso de Retraso. La conversión también se incrementará en cuanto el evento se registre en el perfil de usuario.

Las conversiones se siguen incluso después de que finalice el Canvas, pero las salidas no se siguen una vez que el usuario sale del Canvas. La ventana de conversión se extiende hasta tres días más allá de la duración máxima del Canvas. Esto significa que las conversiones seguirán siendo objeto de seguimiento después de que las salidas dejen de serlo. 

El tiempo mínimo para una ventana de conversión es de cinco minutos. Ajusta las ventanas de conversión a cinco minutos para que tus eventos de conversión se aproximen lo más posible a la paridad con los eventos de salida. También recomendamos configurar la ventana de conversión para que al menos coincida con la ruta más larga del Canvas.

Considera el siguiente ejemplo sobre cómo se calculan los análisis:

1. Diez usuarios pasan por el Canvas.
2. Tres usuarios realizan el evento de conversión en cinco minutos (el número de eventos de salida es tres, y el número de eventos de conversión es tres).
3. Otros cinco usuarios salen del Canvas al cabo de cinco minutos, pero realizan el evento de conversión al cabo de dos días (el número de eventos de salida sigue siendo el mismo, pero el evento de conversión aumenta a ocho).
4. Los dos últimos usuarios salen del Canvas al cabo de cinco minutos, pero no realizan el evento de conversión, o lo realizan al cabo de tres días y cinco minutos (no se contabilizan ni en los eventos de salida ni en las métricas de eventos de conversión).

## Ejemplo

Supongamos que queremos dirigirnos a usuarios que aún no han realizado ninguna compra en nuestra empresa de suministro de mochilas. Para configurar los criterios de salida, lo haríamos:

1. Selecciona **Realizar Compra** como evento de excepción.
2. Selecciona **Añadir desencadenante**. 
3. En **Segmentos**, selecciona **Utilizado en el último día** para que, cuando se lance nuestro Canvas, la audiencia excluya a los usuarios que hayan realizado alguna compra.
4. Para **filtrar**, selecciona **Comportamiento de compra** > **Número de compras** > **Producto comprado**.
5. Configura el grupo de filtrado en `backpack-example exactly 1`. Esto significa que los usuarios que han comprado nuestro producto mochila saldrían del Canvas.

\![Configuración de los Criterios de Salida con "Realiza cualquier compra" como evento de excepción, de modo que si un usuario realiza cualquier compra, entonces saldrá de este Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}


