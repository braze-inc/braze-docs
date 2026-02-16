---
nav_title: Calculadora de facturación
article_title: Calculadoras de facturación SMS y RCS
page_order: 5
description: "Este artículo de referencia trata sobre qué es un segmento de SMS, cómo se contabilizan para la facturación, así como las cosas que hay que tener en cuenta al crear mensajes SMS y RCS."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# Calculadoras de facturación SMS y RCS

> En Braze, los mensajes SMS se cobran por segmento del mensaje, mientras que los mensajes RCS se cobran por mensaje. Entender qué define un segmento SMS y los distintos tipos de facturación RCS te ayudará a comprender cómo se te facturará y a evitar excedentes accidentales.

## Calculadora de copias y segmentos de mensajes SMS

Los mensajes SMS se cobran por segmento del mensaje. Comprender cómo se dividen los mensajes SMS es clave para entender tu facturación.

### ¿Qué es un segmento SMS?

El Servicio de Mensajes Cortos (SMS) es un protocolo de comunicación estandarizado que permite a los dispositivos enviar y recibir mensajes de texto breves. Se diseñó para "encajar" entre otros protocolos de señalización, por eso la longitud de los mensajes SMS está limitada a 160 caracteres de 7 bits, como 1120 bits, o 140 bytes. Los segmentos de mensajes SMS son los lotes de caracteres que las compañías telefónicas utilizan para medir los mensajes de texto. Los mensajes se cobran por segmento de mensajes, por lo que los clientes que utilizan SMS se benefician enormemente de comprender los matices de cómo se dividirán los mensajes.

Cuando creas una campaña de SMS o Canvas con Braze, los mensajes que construyes en el compositor son representativos de lo que tus usuarios pueden ver cuando el mensaje llega a su teléfono, pero **no son indicativos de cómo se dividirá tu mensaje en segmentos y, en última instancia, de cómo se te cobrará**. Entender cuántos segmentos se enviarán y ser consciente de los posibles excesos que podrían producirse es su responsabilidad, pero le proporcionamos algunos recursos para facilitarle esta tarea. Consulta nuestra [calculadora interna de segmentos](#segment-calculator).

![]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Desglose por segmentos

El límite de caracteres para **un segmento SMS independiente** es de 160 caracteres[(codificación GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)) o 70 caracteres ([codificación UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)) según el tipo de codificación. Sin embargo, la mayoría de los teléfonos y redes admiten la concatenación, ofreciendo mensajes SMS más largos de hasta 1530 caracteres (GSM-7) o 670 caracteres (UCS-2). Así, aunque un mensaje puede incluir varios segmentos, si no supera estos límites de concatenación, se considerará un solo mensaje y se informará como tal.

Es importante tener en cuenta que **, a medida que se supera el límite de caracteres del primer segmento, los caracteres adicionales harán que todo el mensaje se divida y se segmente en función de los nuevos límites de caracteres**:
- **Codificación GSM-7**
    - Los mensajes que superen el límite de 160 caracteres ahora se segmentarán en segmentos de 153 caracteres y se enviarán individualmente, para luego ser reconstruidos por el dispositivo del destinatario. Por ejemplo, un mensaje de 161 caracteres se enviará como dos mensajes, uno con 153 caracteres y el segundo con 8 caracteres.
- **Codificación UCS-2**
    - Si incluyes caracteres no GSM, como Emojis, escritura china, coreana o japonesa, en los mensajes SMS, esos mensajes deben enviarse con codificación UCS-2. Los mensajes que superen el límite de segmento inicial de 70 caracteres harán que todo el mensaje se concatene en segmentos de mensaje de 67 caracteres. Por ejemplo, un mensaje de 71 caracteres se enviará como dos mensajes, uno con 67 caracteres y el segundo con 4 caracteres.

Independientemente del tipo de codificación, cada mensaje SMS enviado por Braze tiene un límite de hasta 10 segmentos y es compatible con [plantillas Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/), [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), emojis y enlaces.

{% tabs %}
{% tab GSM-7 encoding %}
| Número de caracteres | ¿Cuántos segmentos? |
| -------------------- | ----------------- |
| 0 - 160 caracteres 1 segmento
| 161 - 306 caracteres | 2 segmentos |
| 307 - 459 caracteres | 3 segmentos |
| 460 - 612 caracteres 4 segmentos
| 613 - 765 caracteres 5 segmentos
| 766 - 918 caracteres | 6 segmentos |
| 919 - 1071 caracteres | 7 segmentos |
| 1072 - 1224 caracteres | 8 segmentos |
| 1225 - 1377 caracteres | 9 segmentos |
| 1378 - 1530 caracteres | 10 segmentos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab UCS-2 encoding %}
| Número de caracteres | ¿Cuántos segmentos? |
| -------------------- | ----------------- |
| 0 - 70 caracteres | 1 segmento |
| 71 - 134 caracteres | 2 segmentos |
| 135 - 201 caracteres 3 segmentos
| 202 - 268 caracteres 4 segmentos
| 269 - 335 caracteres | 5 segmentos |
| 336 - 402 caracteres | 6 segmentos |
| 403 - 469 caracteres | 7 segmentos |
| 470 - 536 caracteres 8 segmentos
| 537 - 603 caracteres | 9 segmentos |
| 604 - 670 caracteres | 10 segmentos |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

### Cosas que debes tener en cuenta al crear tu copia

- **Límite de caracteres por segmento**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) tiene un límite de 160 caracteres para un solo segmento de SMS. Para los mensajes con más de 160 caracteres, todos los mensajes se segmentarán con un límite de 153 caracteres.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) tiene un límite de 70 caracteres por segmento del mensaje. Para los mensajes con más de 70 caracteres, todos los mensajes se segmentarán con un límite de 67 caracteres.<br><br>
- **Límite de segmentos por mensaje**
    - Hay una cantidad máxima de segmentos que puede enviar debido a las limitaciones del medio. No se pueden enviar más de **10 segmentos** de mensajes en un solo mensaje Braze SMS.
    - Esos 10 segmentos estarán limitados a 1530 caracteres (codificación GSM-7) o 670 caracteres (codificación UCS-2).<br><br>
- **Compatible con plantillas Liquid, contenido conectado, emojis y enlaces**
    - Liquid Templating y Connected Content pueden hacer que tu mensaje supere el límite de caracteres para tu tipo de codificación. Puedes utilizar el [filtro truncar palabras](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) para limitar el número de palabras que tu Liquid podría aportar al mensaje.
    - Los emojis no tienen un recuento de caracteres estándar para todos los emojis, así que asegúrate de comprobar que tus mensajes se segmentan y muestran correctamente.
    - Los enlaces pueden utilizar muchos caracteres, lo que da lugar a más segmentos de mensaje de los previstos. Aunque es posible utilizar acortadores de enlaces, lo mejor es utilizarlos con códigos cortos. Visite nuestras [preguntas frecuentes sobre SMS]({{site.baseurl}}/sms_faq/) para obtener más información.<br><br>
- **Pruebas**
    - Prueba siempre tus mensajes SMS antes de lanzarlos, especialmente cuando utilices Liquid y Contenido conectado, ya que superar los límites de mensajes o copias puede suponer cargos adicionales. Tenga en cuenta que los mensajes de prueba contarán para sus límites de mensajes.

### Calculadora de segmentos SMS {#segment-calculator}
---

{% include alerts/tip_alerts.md alert='SMS segment calculator' %}

## Facturación de mensajes RCS

Los mensajes RCS se facturan en función de su contenido y del país en el que se entrega el mensaje. Para calcular los costes con precisión, es esencial comprender los distintos tipos de mensajes y cómo se facturan.

### Tipos de facturación RCS

Nuestra plataforma admite dos modelos principales de facturación: un modelo global y un modelo para Estados Unidos.

#### Modelo global (mercados no estadounidenses)

Los mensajes se facturan por mensaje y se clasifican como Básicos o Únicos.

{% tabs local %}
{% tab Basic %}

Los mensajes RCS básicos son mensajes de sólo texto de hasta 160 caracteres y se facturan como un único mensaje.

{% alert note %}
Si añades botones o cualquier elemento enriquecido, el tipo de mensaje cambiará a Mensaje RCS único.
{% endalert %}

{% endtab %}
{% tab Single %}

Los mensajes RCS simples son mensajes que tienen más de 160 caracteres O incluyen elementos enriquecidos como botones o medios. Se facturan como un único mensaje, independientemente de la longitud del mensaje.

{% alert note %}
Enviar un mensaje de texto y un archivo multimedia por separado se sigue considerando como dos mensajes distintos.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Modelo de Estados Unidos

Los mensajes se clasifican en Rich o Rich Media.

{% tabs local %}
{% tab Rich messages %}

Los mensajes enriquecidos son mensajes de sólo texto con o sin botones. Se facturan por segmento, con cada segmento limitado a 160 bytes UTF-8, lo que significa que **el número de caracteres por segmento no es fijo**. Un mensaje con sólo 160 caracteres en inglés es un segmento, pero un mensaje con texto más largo y emojis podría ser varios segmentos.

{% endtab %}
{% tab Rich media messages %}

Los mensajes multimedia enriquecidos incluyen un archivo multimedia (imagen, video) o una tarjeta enriquecida y se facturan como un único mensaje.

{% endtab %}
{% endtabs %}

### Creador de mensajes y panel de uso de mensajes

Mientras creas tu mensaje, el creador de mensajes mostrará el tipo de facturación en tiempo real a través de una etiqueta (RCS Básico, RCS Único, Rich o Rich Media), ayudándote a hacer un seguimiento de los costes antes de enviarlo.

Tu [panel de uso de mensajes]({{site.baseurl}}/message_usage_dashboard/) reflejará estos tipos de facturación y proporcionará el número de segmentos utilizados para los mensajes de EE.UU., proporcionando una visión transparente de tu consumo de crédito de mensajes.
