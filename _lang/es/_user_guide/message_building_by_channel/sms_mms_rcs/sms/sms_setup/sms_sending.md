---
nav_title: "Envío de mensajes SMS"
article_title: Resumen del envío de mensajes SMS
page_order: 4
alias: /sms_message_sending/
description: "Este artículo de referencia cubre los aspectos básicos y las mejores prácticas del envío de SMS."
page_type: reference
channel:
  - SMS
  
---

# Envío de mensajes SMS

> La mensajería puede ser complicada, pero no tiene por qué serlo. En las siguientes secciones se enumeran los fundamentos del envío de mensajes SMS en Braze, incluida la importancia de los grupos de suscripción, los requisitos para los segmentos de SMS y los cuerpos de los mensajes, así como las opciones avanzadas de personalización disponibles.

## Conceptos básicos del envío de SMS

### Selecciona tu grupo de suscripción

Los mensajes SMS deben enviarse desde un [grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/). Un grupo de suscripción es un conjunto de números de teléfono remitentes (como códigos abreviados, códigos largos y/o ID alfanuméricos de remitente) que se utilizan para un tipo específico de mensajería. Debes designar un grupo de suscripción para asegurarte de que sólo se dirige a los usuarios suscritos. Algunos clientes pueden encontrarse con que tienen varios grupos de suscripción para diferentes casos de uso, como la mensajería SMS transaccional y la mensajería SMS promocional.<br><br>

### Cuerpo del mensaje de entrada

El cuerpo de un mensaje SMS acepta hasta 1.600 caracteres, incluidos emojis, Liquid y contenido conectado. El envío de una sola campaña puede dar lugar a muchos envíos de segmentos del mensaje. Los cuerpos de los mensajes SMS Braze pueden estar compuestos por las normas de codificación [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) o [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set). En caso de que se utilice un carácter UCS-2 (por ejemplo, un Emoji), el cuerpo del mensaje formateará automáticamente para ese estándar de codificación.<br><br> 

### Comprender los segmentos del mensaje y los límites de caracteres

Los segmentos del mensaje SMS son la forma en que la industria del SMS cuenta los mensajes. Un segmento del mensaje es una agrupación de hasta un número definido de caracteres (160 para la codificación GSM-7; 67 para la codificación UCS-2) que se enviarán en un único envío SMS. Si envías un SMS con 161 caracteres utilizando la codificación GSM-7, verás que se han enviado dos (2) segmentos del mensaje. El envío de varios segmentos del mensaje puede conllevar gastos adicionales.<br><br>

### Personalización de palabras clave (opcional)

La normativa exige que haya respuestas a todas las palabras clave de los SMS de adhesión voluntaria, exclusión voluntaria y ayuda/información. Con Braze, puedes definir tus propias palabras clave para desencadenar respuestas de adhesión voluntaria, exclusión voluntaria y ayuda, gestionar tus propias respuestas que se envían a los usuarios y definir conjuntos de palabras clave para distintos idiomas. Para más información, consulta nuestra colección sobre [Procesamiento de palabras clave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/).

{% alert tip %}
¿Quieres aprender a crear una campaña SMS? Consulta nuestra guía paso a paso para [Crear una campaña SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/).
{% endalert %}

## Mejores prácticas de envío {#sending-best-practices}

### Envío de SMS a varios países

Algunas marcas pueden querer enviar a un grupo de usuarios que tienen números de teléfono de distintos países. Para enviar un mensaje SMS a un número de teléfono de un país determinado, lo mejor es utilizar un código largo o un código abreviado del mismo país. De hecho, los códigos abreviados sólo pueden enviar SMS a números de teléfono del mismo país en el que se creó el código abreviado. 

Para superar esta limitación, durante [el proceso de configuración de]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) los grupos de suscripción, se pueden establecer grupos que contengan códigos largos y abreviados de varios países diferentes. Una vez completado, los números de teléfono de envío con el mismo código de país que el número de teléfono del usuario objetivo se utilizarán automáticamente al lanzar una campaña. No tendrás que crear campañas separadas para usuarios con números de teléfono con códigos de país diferentes, lo que te permitirá lanzar campañas o utilizar un componente de Canvas para dirigirte a usuarios relevantes.

\![Las cargas útiles del SMS se envían utilizando el mismo código de país que el número de teléfono del usuario de destino]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

#### Buenas prácticas

1. **Pide permiso**. Una de las reglas más importantes para utilizar los SMS como negocio es que primero debes obtener el permiso de los clientes para ponerte en contacto con ellos. No hacerlo puede dañar tu marca y acarrearte cuantiosos gastos legales.<br><br>
2. **Elige el número adecuado para tu caso de uso**. Hay tres tipos principales de números de teléfono que pueden enviar y recibir mensajes SMS: códigos largos, códigos abreviados e ID alfanuméricos de remitente, y sus capacidades y disponibilidad en las distintas regiones varían. Piensa de antemano si a tu empresa le conviene más un código de vanidad. <br><br>
3. **Presta atención a los tiempos**. Ten en cuenta que los clientes son más receptivos a los materiales dirigidos directamente a ellos. Un poco de personalización es muy útil, como utilizar el nombre de pila del destinatario o añadir un toque conversacional que refleje los intereses de tus clientes.<br><br>
4. Entabla **conversaciones bidireccionales**. El SMS es un canal tan eficaz para la interacción con los clientes que es importante anticipar -y gestionar eficazmente- las respuestas a tus mensajes. El 85% de los consumidores no sólo quiere poder recibir información, sino también responder a las empresas o entablar una conversación.<br><br>
5. **Mide lo que funciona**. ¿Llega a los clientes en el momento adecuado, con la mejor frecuencia y utilizando las llamadas a la acción más eficaces? Utilizar las herramientas de seguimiento adecuadas puede ofrecer métricas directas y cuantificables que demuestren su ROI. 

### Envío de gran volumen

¿Piensas hacer envíos de gran volumen? Tenemos algunas buenas prácticas para que te asegures de que funciona sin problemas.

- Ajusta la tasa límite de velocidad de entrega para tu campaña/lienzos según sea necesario, en función del tamaño de la audiencia objetivo. Esto garantizará que alcanzas el volumen de envío que necesitas y que Braze envía los mensajes a la tasa que Twilio espera y puede manejar.
- Asegúrate de respetar el límite de 160 caracteres, y ten en cuenta que los caracteres especiales cuentan dos veces (por ejemplo, las barras inclinadas `\`, las caretas `^` y las tildes `~`). 

