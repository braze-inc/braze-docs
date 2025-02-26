---
nav_title: Criterios de salida 
article_title: Criterios de salida 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Este artículo de referencia cubre la función Criterios de salida para el Flujo de Canvas."
tool: Canvas
---

# Criterios de salida

> Al añadir [eventos de excepción]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events) directamente a tus reglas de entrada de Canvas, tus usuarios pueden salir de tu Canvas en cuanto se produzca el evento al final del paso. Esto ayuda a conseguir un enfoque más específico de la mensajería de Canvas con tu audiencia.

En el paso **Público objetivo** del constructor de Canvas, puede establecer criterios de salida para identificar qué usuarios desea que salgan de su Canvas. Añade tu evento de excepción y, a continuación, selecciona **Añadir desencadenante**. 

También puede incluir segmentos y filtros en los criterios de salida, lo que significa que los usuarios que coincidan con el segmento o el filtro saldrán del lienzo y no recibirán más mensajes. Si el primer paso de un Lienzo es un paso de Retraso con un retraso de cinco días, los criterios de salida se aplicarán al final de este paso. Así, si un usuario cumple los criterios de salida, saldrá al final de los cinco días.

{% alert note %}
Los atributos de matriz no se admiten actualmente como criterios de salida en eventos de excepción.
{% endalert %}

## Eventos de excepción

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

## Casos de uso

Supongamos que quieres dirigirte a usuarios que aún no han realizado ninguna compra en tu empresa. Primero, selecciona **Realizar Compra** como evento de excepción. A continuación, selecciona **Añadir desencadenante**. Cuando se lance tu Canvas, tu audiencia excluirá a los usuarios que hayan realizado alguna compra con la siguiente configuración **de Criterios de salida**. 

En el siguiente ejemplo, este criterio de salida también se aplica al segmento "Utilizado en el último día" para cualquier usuario que haya realizado exactamente una compra.

![Configuración de Criterios de Salida con "Hace Cualquier Compra" como el evento de excepción, así que si un usuario hace cualquier compra, entonces saldrá de este Canvas.][1]

[1]: {% image_buster /assets/img_archive/exit_criteria_example.png %} 
