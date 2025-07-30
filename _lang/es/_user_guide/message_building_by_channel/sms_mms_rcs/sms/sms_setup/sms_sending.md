---
nav_title: "Envío de mensajes SMS"
article_title: Visión general del envío de mensajes SMS
page_order: 4
alias: /sms_message_sending/
description: "Este artículo de referencia cubre los aspectos básicos y las mejores prácticas del envío de SMS."
page_type: reference
channel:
  - SMS
  
---

# Envío de mensajes SMS

> La mensajería puede ser complicada, pero no tiene por qué serlo. En las siguientes secciones se enumeran los fundamentos del envío de mensajes SMS en Braze, incluida la importancia de los grupos de suscripción, los requisitos de los segmentos SMS y los cuerpos de los mensajes, así como las opciones avanzadas de personalización disponibles.

## Conceptos básicos del envío de SMS

### Seleccione su grupo de suscripción

Los mensajes SMS deben enviarse desde un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/). Un grupo de suscripción es una colección de números de teléfono de envío (como códigos cortos, códigos largos y/o ID alfanuméricos de remitente) que se utilizan para un tipo específico de mensajería. Debe designar un grupo de suscripción para asegurarse de que sólo los usuarios suscritos son los destinatarios. Algunos clientes pueden tener varios grupos de suscripción para diferentes casos de uso, como la mensajería SMS transaccional y la mensajería SMS promocional.<br><br>

### Cuerpo del mensaje de entrada

El cuerpo de un mensaje SMS acepta hasta 1.600 caracteres, incluidos emojis, Liquid y Connected Content. Un solo envío de campaña puede dar lugar a muchos envíos de segmentos de mensajes. Los cuerpos de los mensajes Braze SMS pueden estar compuestos por las normas de codificación [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) o [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set). En caso de que se utilice un carácter UCS-2 (por ejemplo, un Emoji), el cuerpo del mensaje formateará automáticamente para ese estándar de codificación.<br><br> 

### Comprender los segmentos de mensajes y los límites de caracteres

Los segmentos de mensajes SMS son la forma en que el sector de los SMS contabiliza los mensajes. Un segmento de mensaje es una agrupación de hasta un número definido de caracteres (160 para la codificación GSM-7; 67 para la codificación UCS-2) que se enviarán en un único envío SMS. Si envía un SMS con 161 caracteres utilizando la codificación GSM-7, verá que se han enviado dos (2) segmentos de mensaje. El envío de varios segmentos de mensajes puede dar lugar a cargos adicionales.<br><br>

### Personalización de palabras clave (opcional)

La normativa exige que haya respuestas a todas las palabras clave de los SMS de adhesión voluntaria, cancelación y ayuda/información. Con Braze, puede definir sus propias palabras clave para activar las respuestas Opt-In, Opt-Out y Ayuda, gestionar sus propias respuestas que se envían a los usuarios y definir conjuntos de palabras clave para diferentes idiomas. Para más información, consulta nuestra colección sobre [Procesamiento de palabras clave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/).

{% alert tip %}
¿Quieres saber cómo crear una campaña de SMS? Consulta nuestra guía paso a paso para [crear una campaña de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/).
{% endalert %}

## Buenas prácticas de envío {#sending-best-practices}

### Envío de SMS a varios países

Algunas marcas pueden desear enviar a un grupo de usuarios que tienen números de teléfono de diferentes países. Para enviar un SMS a un número de teléfono de un país determinado, lo mejor es utilizar un código largo o corto del mismo país. De hecho, los códigos cortos sólo pueden enviar SMS a números de teléfono del mismo país en el que se creó el código corto. 

Para superar esta limitación, durante [el proceso de configuración de]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) los grupos de suscripción, se pueden establecer grupos que contengan códigos largos y abreviados de varios países diferentes. Una vez completado, los números de teléfono de envío con el mismo código de país que el número de teléfono del usuario objetivo se utilizarán automáticamente al lanzar una campaña. No tendrá que crear campañas separadas para usuarios con números de teléfono con códigos de país diferentes, lo que le permitirá lanzar una sola campaña o utilizar un solo componente de Canvas para dirigirse a los usuarios pertinentes.

![Las cargas útiles del SMS se envían utilizando el mismo código de país que el número de teléfono del usuario de destino]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

#### Buenas prácticas

1. **Pide permiso**. Una de las reglas más importantes para utilizar los SMS en una empresa es que primero debe obtener el permiso de los clientes para ponerse en contacto con ellos. No hacerlo puede dañar su marca y acarrearle cuantiosos gastos legales.<br><br>
2. **Elija el número adecuado para su caso de uso**. Hay tres tipos principales de números de teléfono que pueden enviar y recibir mensajes SMS: códigos largos, códigos cortos e identificadores de remitente alfanuméricos, y sus capacidades y disponibilidad varían según las regiones. Piensa de antemano si a tu empresa le conviene más un código de vanidad. <br><br>
3. **Presta atención a los tiempos**. Ten en cuenta que los clientes son más receptivos a los materiales dirigidos directamente a ellos. Un poco de personalización es muy útil, como utilizar el nombre de pila del destinatario o añadir un toque de conversación que refleje los intereses de sus clientes.<br><br>
4. **Entable conversaciones bidireccionales**. Los SMS son un canal tan eficaz para relacionarse con los clientes que es importante anticiparse a las respuestas a los mensajes y gestionarlas con eficacia. El 85% de los consumidores no sólo quiere poder recibir información, sino también responder a las empresas o entablar una conversación.<br><br>
5. **Mida lo que funciona**. ¿Llega a los clientes en el momento adecuado, con la mejor frecuencia y utilizando las llamadas a la acción más eficaces? Utilizar las herramientas de seguimiento adecuadas puede ofrecer métricas directas y cuantificables que demuestren su ROI. 

### Envíos de gran volumen

¿Piensas hacer envíos de gran volumen? Tenemos algunas buenas prácticas para que te asegures de que funciona sin problemas.

- Ajusta la tasa límite de velocidad de entrega para tu campaña/Canvas según sea necesario, en función del tamaño de la audiencia objetivo. Esto garantizará que alcanzas el volumen de envío que necesitas y que Braze envía los mensajes a la tasa que Twilio espera y puede manejar.
- Asegúrese de respetar el límite de 160 caracteres y tenga en cuenta que los caracteres especiales se cuentan dos veces (por ejemplo, las barras inclinadas `\`, las comillas `^` y las tildes `~`). 

