---
nav_title: Mensajería de usuarios
article_title: Mensajería de usuarios
description: "Este artículo de referencia explica cómo Braze gestionará los mensajes de los usuarios."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /user_guide/message_building_by_channel/whatsapp/quick_replies/

---

# Mensajes de los usuarios

> WhatsApp es un canal de comunicación bidireccional. Su marca no sólo puede enviar mensajes a los usuarios, sino que éstos pueden entablar conversaciones mediante campañas con plantillas y lienzos. Hay varias formas de hacerlo, como las respuestas rápidas de WhatsApp y las palabras desencadenantes. Las llamadas a la acción (CTA, por sus siglas en inglés) de respuesta rápida son una forma estupenda de fomentar la participación de los usuarios en tus mensajes de WhatsApp.

## Activadores basados en acciones 

Tanto las campañas como los lienzos pueden iniciarse, ramificarse y sufrir cambios a mitad de camino a partir de un mensaje entrante de WhatsApp (un usuario que envía un mensaje a tu WhatsApp), como una palabra desencadenante. 

Asegúrese de que su palabra desencadenante coincide con lo que espera de los usuarios.

**Lo que hay que saber:**
- Cada letra de su palabra desencadenante debe ir en mayúscula cuando esté configurada. Braze no exige que las palabras desencadenantes enviadas por los usuarios se escriban en mayúsculas. Por ejemplo, el mensaje "jOin2023" seguirá activando el Canvas o la campaña.
- Si no se especifica ninguna palabra desencadenante en el desencadenador basado en la acción del programa de entrada, la campaña o Canvas se ejecutará para TODOS los mensajes de WhatsApp entrantes. Esto incluye los mensajes que tengan frases coincidentes en campañas activas y Lienzos, en cuyo caso el usuario recibirá dos mensajes de WhatsApp.

{% tabs %}
{% tab Campaña %}

![]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp26.png %})

{% endtab %}
{% tab Canvas %}

![]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp24.png %})
{% endtab %}
{% endtabs %}

## Respuestas no reconocidas

Le recomendamos que incluya una opción para las respuestas no reconocidas en los lienzos interactivos. Esto guía a los usuarios para que entiendan cuáles son las indicaciones disponibles y establece las expectativas para el canal. La gestión de expectativas puede ser especialmente útil si dispone de canales de WhatsApp con chat con agentes en directo. 
- En el paso de acción, después de crear los grupos de acción para las frases de filtro personalizadas, añada un grupo de acción adicional para "Enviar mensaje de WhatsApp", pero **no marque Dónde está el cuerpo del mensaje**. Esto atrapará todas las respuestas de usuario no reconocidas, similar a una cláusula "else". 
- Recomendamos hacer un seguimiento con un mensaje de WhatsApp informando al usuario de que este canal no está atendido y guiándole a un canal de soporte si lo necesita. 

## Respuestas rápidas 

![La pantalla del teléfono que muestre un botón de llamada a la acción responderá al texto del botón pulsado.][11]{: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

Las respuestas rápidas aparecen como opciones de botón en las que se puede hacer clic dentro de la conversación, pero actúan como si el usuario respondiera con texto. A continuación, Braze los procesa como mensajes entrantes y puede enviar respuestas configuradas en función del botón en el que se haya hecho clic. Utilice el paso "Acción de mensaje entrante de WhatsApp" al crear y filtrar respuestas de sus usuarios.

![Un mensaje de WhatsApp con texto y tres botones de llamada a la acción.][13]{: style="max-width:50%;"}

### Configurar las experiencias de respuesta rápida en Canvas

#### Paso 1: Crea CTA

En primer lugar, crea tus CTA de respuesta rápida en el [Gestor de plantillas de mensajes de WhatsApp](https://business.facebook.com/wa/manage/message-templates/) dentro de una plantilla de mensaje. 

![La interfaz de usuario del gestor de plantillas de mensajes de WhatsApp muestra cómo crear un botón CTA, proporcionando el tipo de botón (personalizado) y el texto del botón.][12]{: style="max-width:80%;"}

Una vez que su plantilla haya sido enviada y aprobada por WhatsApp, podrá utilizarla para crear un Canvas dentro de Braze. 

{% alert tip %}
Puede crear el lienzo antes de recibir la aprobación de su plantilla de mensajes.
{% endalert %}

#### Paso 2: Construye tu Canvas

A continuación, construye un Canvas con un paso de mensaje que incluya tu plantilla creada. 

![][14]

Cree un paso de acción que siga al paso del mensaje. Cree un grupo por cada opción de respuesta rápida en este paso de acción.

![Un Canvas donde la acción de evaluación es "enviar un mensaje entrante de whatsapp".][15]

Para cada grupo de opciones de respuesta rápida, especifique el texto exacto del botón con el que está emparejando. Tenga en cuenta que las palabras clave deben estar en mayúsculas. 

![Un paso de Canvas en el que la acción "enviar un mensaje entrante de whatsapp" se configura para enviarse cuando se recibe un cuerpo de mensaje específico.][16]

Si desea una respuesta predeterminada para los usuarios que respondan al mensaje con texto en lugar de respuestas rápidas, cree un grupo adicional sin cuerpo de mensaje coincidente.

Continúa construyendo el Canvas como lo harías a partir de este momento.

### Respuestas

Lo más probable es que quiera un mensaje de respuesta para cada respuesta. Recomendamos disponer de una opción general para las respuestas fuera de los límites de las respuestas rápidas (por ejemplo, para los clientes que responden con un mensaje general en lugar de un aviso predeterminado). Por ejemplo: "Lo sentimos, no reconocimos su respuesta. Para cuestiones de asistencia, envíe un mensaje a <support channel>."

![Se ha creado un lienzo que muestra las respuestas de cada botón de llamada a la acción.][18]

Tenga en cuenta que puede utilizar cualquier acción posterior que ofrezca Braze Canvas, como mensajes en respuesta, actualizaciones de perfil de usuario o webhooks Braze-to-Braze. 

[1]: {% image_buster /assets/img/whatsapp/whatsapp24.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp25.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp26.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp27.png %} 

[11]: {% image_buster /assets/img/whatsapp/whatsapp11.png %}
[12]: {% image_buster /assets/img/whatsapp/whatsapp12.png %}
[13]: {% image_buster /assets/img/whatsapp/whatsapp13.png %}
[14]: {% image_buster /assets/img/whatsapp/whatsapp14.png %}
[15]: {% image_buster /assets/img/whatsapp/whatsapp15.png %}
[16]: {% image_buster /assets/img/whatsapp/whatsapp16.png %}
[17]: {% image_buster /assets/img/whatsapp/whatsapp17.png %}
[18]: {% image_buster /assets/img/whatsapp/whatsapp18.png %}
