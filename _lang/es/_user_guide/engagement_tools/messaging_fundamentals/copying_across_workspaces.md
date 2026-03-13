---
nav_title: Copiar entre espacios de trabajo
article_title: Copiar entre espacios de trabajo
page_order: 4
alias: "/copying_to_workspaces/"
page_type: reference
description: "Este artículo de referencia ofrece un resumen sobre cómo copiar campañas y lienzos a diferentes espacios de trabajo."
tool:
    - Campaigns
    - Canvas
---

# Copiar campañas y lienzos entre espacios de trabajo

> La copia de campañas entre espacios de trabajo le permite iniciar la composición de sus mensajes comenzando con una copia de una campaña en un espacio de trabajo diferente. Esta página explica cómo copiar campañas a diferentes espacios de trabajo y enumera lo que se copia y lo que no.

Cuando copias una campaña o un Canvas a un espacio de trabajo diferente, la copia permanecerá como borrador hasta que la edites y la lances, lo que te ayudará a conservar y desarrollar tus estrategias de mensajería exitosas.

{% tabs local %}
{% tab campaigns %}

{% alert important %}
La copia de campañas entre espacios de trabajo ya está disponible de forma generalizada. Actualmente, no está disponible la compatibilidad con tarjetas de contenido en los canales.
{% endalert %}

Puedes copiar campañas entre espacios de trabajo para estos canales compatibles: SMS, mensajes dentro de la aplicación, notificaciones push, correo electrónico y webhooks. También puedes copiar plantillas de correo electrónico, características y bloques de contenido. Tenga en cuenta que las campañas multicanal con canales no compatibles no pueden copiarse a un espacio de trabajo diferente.

Para copiar una campaña a un espacio de trabajo diferente:

1. Selecciona el ícono<i class="fas fa-cog"></i> de engranaje situado junto a la campaña seleccionada.
2. Selecciona **Copiar al espacio de trabajo**. 
3. Después de copiar, revisa y prueba tu campaña para confirmar que todos los campos funcionan correctamente.

{% endtab %}
{% tab canvas %}

{% alert important %}
La función de copiar lienzos entre espacios de trabajo ya está disponible de forma generalizada. Los siguientes canales no son compatibles actualmente: LINE, tarjetas de contenido y WhatsApp.
{% endalert %}

Puedes copiar lienzos entre espacios de trabajo para estos canales compatibles: correo electrónico, mensajes dentro de la aplicación, push, webhooks y SMS.

Para copiar un Canvas a un espacio de trabajo diferente:

1. Selecciona el<i class="fa-solid fa-ellipsis-vertical"></i> menú situado junto al Canvas seleccionado.
2. Selecciona **Copiar al espacio de trabajo**. 
3. Después de copiar, revisa y prueba tu Canvas para confirmar que todos los campos funcionan correctamente.

Al copiar un Canvas con pasos de Audience Sync, la configuración no se copiará en el espacio de trabajo de destino, pero sí se copiarán los pasos del recorrido.

{% endtab %}
{% endtabs %}

## Lo que se copia en los espacios de trabajo

Nota: la siguiente no es una lista exhaustiva de lo que se copia entre espacios de trabajo y lo que se omite. Como práctica recomendada, revisa los detalles de la campaña y de Canvas y realiza pruebas para confirmar que tu mensaje funciona según lo esperado.

### Detalles

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Descripción | Territorios | 
| Tipo | Etiquetas | 
| Acciones (anidadas) | Segmentos | 
| Comportamientos de conversión (anidados) | Aprobaciones | 
| Configuraciones del tiempo de silencio | Planificación por desencadenante | 
| Configuraciones de limitación de frecuencia | Resúmenes de campaña | 
| Estado de suscripción del destinatario | Filtros | 
| Planificación recurrente |  | 
| Es transaccional |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Descripción | Territorios | 
| Tipo | Etiquetas | 
| Acciones (anidadas) | Segmentos | 
| Comportamientos de conversión (anidados) | Aprobaciones | 
| Configuraciones del tiempo de silencio | Planificación por desencadenante | 
| Configuraciones de limitación de frecuencia | Resúmenes en Canvas | 
| Estado de suscripción del destinatario | Filtros | 
| Planificación recurrente |  | 
| Es transaccional |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Comportamientos de conversión

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID del espacio de trabajo |
| Interacción de la campaña |  ID de campaña | 
| Nombre del evento personalizado |  | 
| Nombre del producto |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID del espacio de trabajo |
| Interacción con el Canvas |  ID de Canvas | 
| Nombre del evento personalizado |  | 
| Nombre del producto |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Acciones

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID del espacio de trabajo |
| Interacción de la campaña |  ID de campaña | 
| Nombre del evento personalizado |  | 
| Nombre del producto |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID del espacio de trabajo |
| Interacción con el Canvas |  ID de Canvas | 
| Nombre del evento personalizado |  | 
| Nombre del producto |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Variaciones de los mensajes

{% tabs local %}
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Enviar porcentaje | ID de API |
| Tipo |  Identificadores de grupos de semillas | 
|  |  Identificadores de plantillas de enlace | 
|  |  ID de grupos de usuarios internos | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

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
{% tab campaigns %}

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
{% tab canvas %}

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
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Texto sin formato | Alias de enlace |
| HTML y arrastrar y soltar contenido | Traducciones | 
| Preencabezado |  | 
| CSS en línea |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

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
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Cuerpo del correo electrónico | ID de API |
| Descripción | ID de imagen | 
| Asunto | Territorios | 
| Cabeceras | Etiquetas | 
| | Traducciones |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

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
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Apellidos | Alias de enlace |
| Descripción | Claves de API | 
| Contenido | Territorios | 
| HTML y arrastrar y soltar contenido | Etiquetas | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

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
{% tab campaigns %}

| Copiado | Omitido |
|---|---|
| Cuerpo | Servicio de mensajería |
| Acortamiento de enlaces | Elementos multimedia VCF | 
| Seguimiento de clics |  | 
| Elementos multimedia |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab canvas %}

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

Las referencias líquidas dentro del cuerpo de los mensajes se copian en el espacio de trabajo de destino, pero es posible que no funcionen como se espera. Esto significa que si se copia un Canvas del espacio de trabajo A al espacio de trabajo B, este último no podrá hacer referencia a los detalles del espacio de trabajo A, incluidas las referencias Liquid. Por ejemplo, los campos como las acciones desencadenantes y los filtros de audiencia no se copian.

Realiza el seguimiento de las siguientes referencias de Liquid con dependencias al copiar campañas y lienzos entre espacios de trabajo:

- Etiquetas de elementos del catálogo
- Etiquetas de contenido conectado
- Bloques de contenido
- Atributos personalizados
- Centros de preferencia
- Recomendaciones de productos
- Etiquetas de estado de suscripción
- Etiquetas de vales y promociones

## Copiar mensajes con indicadores de característica

Para copiar una campaña de indicadores de funciones y un lienzo con un paso de indicador de funciones entre espacios de trabajo, asegúrate de que el espacio de trabajo de destino tenga configurado un [experimento de indicador de funciones]({{site.baseurl}}/developer_guide/feature_flags/experiments) con un ID que coincida con el indicador de funciones al que se hace referencia en la campaña original o con el paso de indicador de funciones al que se hace referencia en el lienzo original.

Si copias una campaña o un Canvas que tiene un paso de indicador de función con un ID de indicador de función que no existe en el espacio de trabajo de destino, se copiará el paso de indicador de función, pero no su contenido.

## Copiar mensajes con bloques de contenido

Cuando se copia una campaña entre espacios de trabajo, los Bloques de contenido no se copian. Sin embargo, se puede hacer referencia a un Content Block en el área de trabajo de destino si existe un bloque con el mismo nombre. Como alternativa, puede crear el Bloque de contenido (o estas referencias líquidas) en el espacio de trabajo de destino para evitar errores al lanzar una campaña.

En el caso de los lienzos que hacen referencia a un bloque de contenido, primero hay que copiar el bloque de contenido al espacio de trabajo de destino.
