---
nav_title: Copiar entre espacios de trabajo
article_title: Copiar entre espacios de trabajo
page_order: 4.5
alias: "/copying_to_workspaces/"
page_type: reference
description: "Este artículo de referencia ofrece un resumen de cómo copiar campañas y Lienzos en diferentes espacios de trabajo."
tool:
    - Campaigns
    - Canvas
---

# Copiar campañas y lienzos en distintos espacios de trabajo

> La copia de campañas entre espacios de trabajo le permite iniciar la composición de sus mensajes comenzando con una copia de una campaña en un espacio de trabajo diferente. Esta página explica cómo copiar campañas a diferentes espacios de trabajo y enumera lo que se copia y lo que no.

Cuando copies una campaña o Canvas en un espacio de trabajo diferente, la copia permanecerá como borrador hasta que la edites y la lances, lo que te ayudará a mantener y desarrollar tus estrategias de mensajería de éxito.

{% tabs local %}
{% tab campañas %}

{% alert important %}
La copia de campañas entre espacios de trabajo está disponible en general. El soporte de canal para las tarjetas de contenido no está disponible actualmente.
{% endalert %}

Puedes copiar campañas entre espacios de trabajo para estos canales compatibles: SMS, mensajes dentro de la aplicación, notificaciones push, correo electrónico y webhooks. También puedes copiar entre plantillas de correo electrónico, banderas de características y bloques de contenido. Tenga en cuenta que las campañas multicanal con canales no compatibles no pueden copiarse a un espacio de trabajo diferente.

Para copiar una campaña a otro espacio de trabajo:

1. Selecciona el ícono de engranaje <i class="fas fa-cog"></i> situado junto a la campaña seleccionada.
2. Selecciona **Copiar al espacio de trabajo**. 
3. Después de copiar, revisa y prueba tu campaña para confirmar que todos los campos funcionan correctamente.

{% endtab %}
{% tab Canvas %}

{% alert important %}
La copia de lienzos entre espacios de trabajo está disponible en general. Los siguientes canales no son compatibles actualmente: LINE, Tarjetas de contenido y WhatsApp.
{% endalert %}

Puedes copiar Canvases entre espacios de trabajo para estos canales compatibles: correo electrónico, mensajes dentro de la aplicación, push, webhooks y SMS.

Para copiar un Canvas a otro espacio de trabajo:

1. Selecciona el menú <i class="fa-solid fa-ellipsis-vertical"></i> situado junto al Canvas seleccionado.
2. Selecciona **Copiar al espacio de trabajo**. 
3. Después de copiar, revisa y prueba tu Canvas para confirmar que todos los campos funcionan correctamente.

Al copiar un Canvas con pasos de Sincronización de Audiencia, la configuración no se copiará en el espacio de trabajo de destino, pero sí los pasos del trayecto.

{% endtab %}
{% endtabs %}

## Lo que se copia en los espacios de trabajo

Ten en cuenta que la siguiente no es una lista exhaustiva de lo que se copia entre espacios de trabajo y lo que se omite. Como práctica recomendada, comprueba los detalles de la campaña y de Canvas y haz una prueba para confirmar que tu mensaje funciona como esperabas.

### Detalles

{% tabs local %}
{% tab campañas %}

| Copiado | Omitido |
|---|---|
| Descripción | Territorios | 
| Tipo | Etiquetas | 
| Acciones (anidadas) | Segmentos | 
| Comportamientos de conversión (anidados) | Aprobaciones | 
| Configuraciones del tiempo de silencio | Planificación por desencadenante | 
| Configuraciones de limitación de frecuencia | Resúmenes de campaña | 
| Estado de suscripción del destinatario |  | 
| Planificación recurrente |  | 
| Es transaccional |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Copiado | Omitido |
|---|---|
| Descripción | Territorios | 
| Tipo | Etiquetas | 
| Acciones (anidadas) | Segmentos | 
| Comportamientos de conversión (anidados) | Aprobaciones | 
| Configuraciones del tiempo de silencio | Planificación por desencadenante | 
| Configuraciones de limitación de frecuencia | Resúmenes en Canvas | 
| Estado de suscripción del destinatario |  | 
| Planificación recurrente |  | 
| Es transaccional |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Comportamientos de conversión

{% tabs local %}
{% tab campañas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID del espacio de trabajo |
| Interacción de la campaña |  ID de campaña | 
| Nombre del evento personalizado |  | 
| Nombre del producto |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID del espacio de trabajo |
| Interacción en Canvas |  ID de Canvas | 
| Nombre del evento personalizado |  | 
| Nombre del producto |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Acciones

{% tabs local %}
{% tab campañas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID del espacio de trabajo |
| Interacción de la campaña |  ID de campaña | 
| Nombre del evento personalizado |  | 
| Nombre del producto |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID del espacio de trabajo |
| Interacción en Canvas |  ID de Canvas | 
| Nombre del evento personalizado |  | 
| Nombre del producto |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variaciones de los mensajes

{% tabs local %}
{% tab campañas %}

| Copiado | Omitido |
|---|---|
| Enviar porcentaje | ID de API |
| Tipo |  Identificadores de grupos de semillas | 
|  |  Identificadores de plantillas de enlace | 
|  |  ID de grupos de usuarios internos | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Copiado | Omitido |
|---|---|
| Enviar porcentaje | ID de API |
| Tipo |  Identificadores de grupos de semillas | 
|  |  Identificadores de plantillas de enlace | 
|  |  ID de grupos de usuarios internos | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}


### Variación del mensaje de correo electrónico

{% tabs local %}
{% tab campañas %}

| Copiado | Omitido |
|---|---|
| Cuerpo del correo electrónico | Dirección De |
| Extras para mensajes |  Responder a | 
| Título |  CCO | 
| Asunto |  Plantilla de enlace | 
|  |  Alias de enlace |
|  | Traducciones |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Copiado | Omitido |
|---|---|
| Cuerpo del correo electrónico | Dirección De |
| Extras para mensajes |  Responder a | 
| Título |  CCO | 
| Asunto |  Plantilla de enlace | 
|  |  Alias de enlace |
|  | Traducciones |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Cuerpo del correo electrónico

{% tabs local %}
{% tab campañas %}

| Copiado | Omitido |
|---|---|
| Texto sin formato | Alias de enlace |
| HTML y arrastrar y soltar contenido | Traducciones | 
| Preencabezado |  | 
| CSS en línea |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Copiado | Omitido |
|---|---|
| Texto sin formato | Alias de enlace |
| HTML y arrastrar y soltar contenido | Traducciones | 
| Preencabezado |  | 
| CSS en línea |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Plantillas de correo electrónico

{% tabs local %}
{% tab campañas %}

| Copiado | Omitido |
|---|---|
| Cuerpo del correo electrónico | ID de API |
| Descripción | ID de imagen | 
| Asunto | Territorios | 
| Cabeceras | Etiquetas | 
| | Traducciones |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Copiado | Omitido |
|---|---|
| Cuerpo del correo electrónico | ID de API |
| Descripción | ID de imagen | 
| Asunto | Territorios | 
| Cabeceras | Etiquetas | 
| | Traducciones |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Bloques de contenido

{% tabs local %}
{% tab campañas %}

| Copiado | Omitido |
|---|---|
| Apellidos | Alias de enlace |
| Descripción | Claves de API | 
| Contenido | Territorios | 
| HTML y arrastrar y soltar contenido | Etiquetas | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Copiado | Omitido |
|---|---|
| Apellidos | Alias de enlace |
| Descripción | Claves de API | 
| Contenido | Territorios | 
| HTML y arrastrar y soltar contenido | Etiquetas | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variación del mensaje SMS

{% tabs local %}
{% tab campañas %}

| Copiado | Omitido |
|---|---|
| Cuerpo | Servicio de mensajería |
| Acortamiento de enlaces | Elementos multimedia VCF | 
| Seguimiento de clics |  | 
| Elementos multimedia |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Copiado | Omitido |
|---|---|
| Cuerpo | Servicio de mensajería |
| Acortamiento de enlaces | Elementos multimedia VCF | 
| Seguimiento de clics |  | 
| Elementos multimedia |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Copiar mensajes que contienen Liquid

Las referencias Liquid dentro de los cuerpos de los mensajes se copian en el espacio de trabajo de destino, pero puede que las referencias no funcionen como se espera. Esto significa que si un Canvas del espacio de trabajo A se copia en el espacio de trabajo B, éste no podrá hacer referencia a los detalles del espacio de trabajo A, incluidas las referencias Liquid. Por ejemplo, los campos como las acciones desencadenantes y los filtros de audiencia no se copian.

Realiza un seguimiento de las siguientes referencias Liquid con dependencias al copiar campañas y Lienzos entre espacios de trabajo:

- Etiquetas de elementos del catálogo
- Etiquetas de contenido conectado
- Bloques de contenido
- Atributos personalizados
- Centros de preferencia
- Recomendaciones de productos
- Etiquetas de estado de suscripción
- Etiquetas de vales y promociones

## Copiar mensajes con banderas de características

Para copiar una campaña de bandera de características y un Canvas con un paso de Bandera de Características entre espacios de trabajo, asegúrate de que el espacio de trabajo de destino tiene un [experimento de bandera de características]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurado con un ID que coincide con la bandera de características a la que se hace referencia en la campaña original o con el paso de Bandera de Características al que se hace referencia en el Canvas original.

Si copias una campaña o Canvas que tiene un paso de Bandera de Características con un ID de Bandera de Características que no existe en el espacio de trabajo de destino, el paso de Bandera de Características se copiará pero no su contenido.

## Copiar mensajes con bloques de contenido

Cuando se copia una campaña entre espacios de trabajo, los Bloques de contenido no se copian. Sin embargo, se puede hacer referencia a un Content Block en el área de trabajo de destino si existe un bloque con el mismo nombre. Como alternativa, puede crear el Bloque de contenido (o estas referencias líquidas) en el espacio de trabajo de destino para evitar errores al lanzar una campaña.

Para los Lienzos que hacen referencia a un Bloque de contenido, el Bloque de contenido debe copiarse primero en el espacio de trabajo de destino.
