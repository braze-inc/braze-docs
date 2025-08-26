---
nav_title: Mensajería de usuarios
article_title: Mensajería de usuarios
description: "Este artículo de referencia explica cómo Braze gestionará los mensajes de los usuarios."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# Mensajes de los usuarios

> WhatsApp es un canal de comunicación bidireccional. Su marca no sólo puede enviar mensajes a los usuarios, sino que éstos pueden entablar conversaciones mediante campañas con plantillas y lienzos. Hay varias formas de hacerlo, como las respuestas rápidas de WhatsApp, los mensajes de lista y las palabras desencadenantes. Las llamadas a la acción (CTA) de respuesta rápida y de lista de mensajes son una forma estupenda de fomentar la interacción de los usuarios con tu mensajería de WhatsApp.

## Activadores basados en acciones 

Tanto las campañas como los Lienzos pueden iniciarse, ramificarse y tener cambios a mitad de camino a partir de un mensaje de WhatsApp entrante (un usuario que envía un mensaje a tu WhatsApp), como una palabra desencadenante. 

Asegúrese de que su palabra desencadenante coincide con lo que espera de los usuarios.

**Lo que hay que saber:**
- Cada letra de su palabra desencadenante debe ir en mayúscula cuando esté configurada. Braze no exige que las palabras desencadenantes enviadas por los usuarios se escriban en mayúsculas. Por ejemplo, el mensaje "jOin2023" seguirá activando el Canvas o la campaña.
- Si no se especifica ninguna palabra desencadenante en el desencadenador basado en la acción del programa de entrada, la campaña o Canvas se ejecutará para TODOS los mensajes de WhatsApp entrantes. Esto incluye los mensajes que tengan frases coincidentes en campañas activas y Lienzos, en cuyo caso el usuario recibirá dos mensajes de WhatsApp.

{% tabs %}
{% tab Campaña %}

![Opciones de programación de campañas basadas en acciones.]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

![Opciones de programación de Canvas basadas en acciones.]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## Respuestas no reconocidas

Le recomendamos que incluya una opción para las respuestas no reconocidas en los lienzos interactivos. Esto guía a los usuarios para que entiendan cuáles son las indicaciones disponibles y establece las expectativas para el canal. La gestión de expectativas puede ser especialmente útil si dispone de canales de WhatsApp con chat con agentes en directo. 
- En el paso de acción, después de crear los grupos de acción para las frases de filtro personalizadas, añada un grupo de acción adicional para "Enviar mensaje de WhatsApp", pero **no marque Dónde está el cuerpo del mensaje**. Esto atrapará todas las respuestas de usuario no reconocidas, similar a una cláusula "else". 
- Recomendamos hacer un seguimiento con un mensaje de WhatsApp informando al usuario de que este canal no está atendido y guiándole a un canal de soporte si lo necesita. 

## Respuestas rápidas 

![La pantalla del teléfono que muestra un botón de llamada a la acción responderá al texto del botón pulsado.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

Las respuestas rápidas aparecen como opciones de botón en las que se puede hacer clic dentro de la conversación, pero actúan como si el usuario respondiera con texto. A continuación, Braze los procesa como mensajes entrantes y puede enviar respuestas configuradas en función del botón en el que se haya hecho clic. Utilice el paso "Acción de mensaje entrante de WhatsApp" al crear y filtrar respuestas de sus usuarios.

![Un mensaje de WhatsApp con texto y tres botones de llamada a la acción.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Configura la experiencia de respuesta rápida en Canvas

#### Paso 1: Crea CTA

En primer lugar, crea tus CTA de respuesta rápida en el [Gestor de plantillas de mensajes de WhatsApp](https://business.facebook.com/wa/manage/message-templates/) dentro de una plantilla de mensaje. 

![La interfaz de usuario del administrador de plantillas de mensajes de WhatsApp muestra cómo crear un botón CTA, proporcionando el tipo de botón (personalizado) y el texto del botón.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

Una vez que su plantilla haya sido enviada y aprobada por WhatsApp, podrá utilizarla para crear un Canvas dentro de Braze. 

{% alert tip %}
Puede crear el lienzo antes de recibir la aprobación de su plantilla de mensajes.
{% endalert %}

#### Paso 2: Construye tu Canvas

A continuación, construye un Canvas con un paso de mensaje que incluya tu plantilla creada. 

![Creador de mensajes por pasos de WhatsApp con una plantilla de respuesta rápida rellenada.]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

Cree un paso de acción que siga al paso del mensaje. Cree un grupo por cada opción de respuesta rápida en este paso de acción.

![Un Canvas en el que la acción de evaluación es "enviar un mensaje entrante de whatsapp".]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

Para cada grupo de opciones de respuesta rápida, especifique el texto exacto del botón con el que está emparejando. Tenga en cuenta que las palabras clave deben estar en mayúsculas. 

![Un paso en Canvas en el que la acción "enviar un mensaje entrante de whatsapp" se configura para que se envíe cuando se reciba el cuerpo de un mensaje específico.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

Si desea una respuesta predeterminada para los usuarios que respondan al mensaje con texto en lugar de respuestas rápidas, cree un grupo adicional sin cuerpo de mensaje coincidente.

Continúa construyendo el Canvas como lo harías a partir de este momento.

### Respuestas

Lo más probable es que quiera un mensaje de respuesta para cada respuesta. Recomendamos disponer de una opción general para las respuestas fuera de los límites de las respuestas rápidas (por ejemplo, para los clientes que responden con un mensaje general en lugar de un aviso predeterminado). Por ejemplo: "Lo sentimos, no reconocimos su respuesta. Para cuestiones de asistencia, envíe un mensaje a <support channel>."

![Un Canvas construido mostrando las respuestas para cada botón de llamada a la acción.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

Tenga en cuenta que puede utilizar cualquier acción posterior que ofrezca Braze Canvas, como mensajes en respuesta, actualizaciones de perfil de usuario o webhooks Braze-to-Braze. 

## Listar mensajes

Los mensajes de lista aparecen como un cuerpo de mensaje con una lista de opciones en las que se puede hacer clic. Cada lista puede tener varias secciones, y cada lista puede tener hasta 10 filas.

![Ejemplo de mensaje de lista de WhatsApp con filas para diferentes estilos de moda.]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Configura la experiencia de mensajería de la lista en Canvas

#### Paso 1: Crear o editar un Lienzo basado en acciones existente

Sólo puedes añadir a los Lienzos mensajes de listas de WhatsApp que estén basados en acciones, ya que tienen que ser en respuesta a un mensaje de usuario.

#### Paso 2: Paso 1\. Crear un mensaje de WhatsApp

Añade un [paso de Mensaje de]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) WhatsApp y, a continuación, selecciona el diseño de mensaje de respuesta de **Lista de mensajes**.

![Una colección seleccionable de los distintos tipos de mensajes de respuesta de WhatsApp que puedes crear, incluido el "Mensaje de lista".]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

Añade un nombre de **botón de Lista** que los usuarios seleccionarán para mostrar tu lista. Después, utiliza los campos del **contenido de la Lista** para crear tu lista:

- **Sección:** Añade hasta 10 secciones para agrupar y organizar los elementos de tu lista. Por ejemplo, un comercio minorista de ropa podría utilizar secciones para organizarse por estilos estacionales (como primavera, verano, otoño e invierno) o artículos de ropa (como tops, pantalones y zapatos).
- **Fila:** Añade hasta 10 filas, o elementos de lista, en todas las secciones.
- **Descripción de la fila (opcional):** Añade una descripción opcional a todas las filas (elementos de la lista).

![La sección "Contenido de la lista" rellenada con dos secciones, y varias filas y descripciones de filas.]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

Cambia el orden de las secciones y filas seleccionando y arrastrando el icono situado junto a sus nombres.

![Arrastrar una sección de la lista a una nueva ubicación.]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

De nuevo en el compositor Canvas, añade una [ruta de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) después del paso en Mensaje que tenga un grupo para cada respuesta de lista. En cada grupo:

1. Añade un desencadenante para el **grupo de suscripción de WhatsApp entrante enviado** y selecciona el grupo de suscripción de WhatsApp correspondiente.
2. Marca la casilla **Donde está el cuerpo del mensaje**.
3. Especifica el contenido de una fila (o elemento de lista).

![Compositor para una ruta de acción con grupos para diferentes estilos de ropa.]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

Sigue construyendo tu Canvas.

### Crear rutas de acción para descripciones largas

Si tienes descripciones de filas, debes utilizar **Matches regex** para especificar una fila. Por ejemplo, si quieres especificar una fila con la descripción "Nuestro nuevo estilo que se adapta a tu par favorito de botines", podrías utilizar [regex]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) con "botines".

![Un desencadenador de WhatsApp que utiliza el filtro de "Matches regex" para capturar mensajes de respuesta con "botines".]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## Consideraciones sobre los mensajes de respuesta

Los mensajes de respuesta deben enviarse en las 24 horas siguientes a la recepción del mensaje de un usuario. Para ayudar a crear experiencias satisfactorias, Braze comprueba la lógica de mensajes para confirmar que hay un mensaje de usuario entrante que desbloquea el mensaje de respuesta. 

Los siguientes eventos desbloquean los mensajes de respuesta: 

- Mensaje de entrada 
  - [Ruta de acción]({{site.baseurl}}/action_paths/) o [entrada basada en la acción]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) con el desencadenante **Enviar un mensaje entrante de WhatsApp**.

![Un paso de entrada basado en una acción con el desencadenante "Enviar un mensaje entrante de WhatsApp".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [Entrada desencadenada por la API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)
- Mensaje de producto entrante 
  - [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated#types-of-ecommerce-recommended-events) evento

![Una ruta de acción con el desencadenante de un evento personalizado realizado `ecommerce.cart_updated`.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

