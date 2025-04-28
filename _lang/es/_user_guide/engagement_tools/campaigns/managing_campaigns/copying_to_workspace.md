---
nav_title: Copiar entre espacios de trabajo
article_title: Copiar entre espacios de trabajo
alias: "/copying_to_workspaces/"
page_order: 0.5
page_type: reference
description: "Este artículo ofrece una visión general de cómo copiar campañas en diferentes espacios de trabajo."
tool: Campaigns
---

# Copiar entre espacios de trabajo

> La copia de campañas entre espacios de trabajo le permite iniciar la composición de sus mensajes comenzando con una copia de una campaña en un espacio de trabajo diferente. Esta copia permanecerá como borrador hasta que la edite y la lance, lo que le ayudará a mantener y desarrollar sus exitosas estrategias de mensajería.<br><br>Esta página explica cómo copiar campañas a diferentes espacios de trabajo y enumera lo que se copia y lo que no.

{% alert important %}
En general, la copia de campañas entre espacios de trabajo está disponible para los siguientes canales compatibles: SMS, mensajes dentro de la aplicación, correo electrónico, plantillas de correo electrónico y bloques de contenido. Otros canales (como las tarjetas push y de contenido) aún no están disponibles.
{% endalert %}

## Cómo copiar una campaña en otro espacio de trabajo

![Menú con la opción "Copiar al espacio de trabajo".][1]{: style="float:right;max-width:25%;margin-left:15px;"}

Selecciona el icono de engranaje <i class="fas fa-cog"></i> situado junto a la campaña seleccionada, y selecciona **Copiar al espacio de trabajo**. Después de copiar, te recomendamos que revises y pruebes tu campaña para confirmar que todos los campos funcionan correctamente.

Al copiar una campaña entre espacios de trabajo, se copian campos como el nombre y la descripción de la campaña, las variantes, el tipo de programa de entrega y los comportamientos de conversión. En el caso de las campañas por correo electrónico, los campos como el cuerpo del mensaje, el asunto y el preencabezado también se copian en el espacio de trabajo de destino. 

Tenga en cuenta que las campañas multicanal con canales no compatibles no pueden copiarse a un espacio de trabajo diferente.

### Lo que se copia en los espacios de trabajo

Tenga en cuenta que la siguiente no es una lista exhaustiva de lo que se copia en los espacios de trabajo y lo que se omite. Como práctica recomendada, comprueba los detalles de la campaña y haz pruebas para confirmar que tu campaña funciona como se espera.

{% tabs %}
{% tab Campañas %}

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
{% tab Comportamientos de conversión %}

| Copiado | Omitido |
|---|---|
| Tipo de comportamiento | ID del espacio de trabajo |
| Interacción de la campaña |  ID de campaña | 
| Nombre del evento personalizado |  | 
| Nombre del producto |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Acciones %}

| Copiado | Omitido |
|---|---|
| Tipos de acción | Enviar recuento |
| Variaciones de los mensajes |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Variaciones del mensaje %}

| Copiado | Omitido |
|---|---|
| Enviar porcentaje | ID de API |
| Tipo |  Identificadores de grupos de semillas | 
|  |  Identificadores de plantillas de enlace | 
|  |  ID de grupos de usuarios internos | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Variación del mensaje de correo electrónico %}

| Copiado | Omitido |
|---|---|
| [Cuerpo del correo electrónico]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | Dirección De |
| Extras para mensajes |  Responder a | 
| Título |  CCO | 
| Asunto |  Plantilla de enlace | 
|  |  Alias de enlace |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Cuerpo del correo electrónico %}

| Copiado | Omitido |
|---|---|
| Texto sin formato | Alias de enlace |
| HTML y arrastrar y soltar contenido |  | 
| Preencabezado |  | 
| CSS en línea |  | 
| AMP HTML |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Plantillas de correo electrónico %}

| Copiado | Omitido |
|---|---|
| [Cuerpo del correo electrónico]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/?tab=email%20body) | ID de API |
| Descripción | ID de imagen | 
| Asunto | Territorios | 
| Cabeceras | Etiquetas | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Bloques de contenido %}

| Copiado | Omitido |
|---|---|
| Apellidos | Alias de enlace |
| Descripción | Claves de API | 
| Contenido | Territorios | 
| HTML y arrastrar y soltar contenido | Etiquetas | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Variación del mensaje SMS %}

| Copiado | Omitido |
|---|---|
| Cuerpo | Servicio de mensajería |
| Acortamiento de enlaces | Elementos multimedia VCF | 
| Seguimiento de clics |  | 
| Elementos multimedia |  | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Copia de campañas que contienen Liquid

En el caso de los cuerpos de mensaje que incluyen referencias Liquid, las referencias se copian en el área de trabajo de destino, pero es posible que no funcionen como se esperaba. Esto significa que si una campaña del espacio de trabajo A se copia en el espacio de trabajo B, el espacio de trabajo B no puede hacer referencia a los detalles del espacio de trabajo A, incluidas las referencias líquidas. Por ejemplo, los campos como las acciones desencadenantes y los filtros de audiencia no se copian.

Tenga en cuenta las siguientes referencias líquidas con dependencias al copiar campañas entre espacios de trabajo:

- Etiquetas de elementos del catálogo
- Etiquetas de contenido conectado
- Bloques de contenido
- Atributos personalizados
- Centros de preferencia
- Recomendaciones de productos
- Etiquetas de estado de suscripción
- Etiquetas de vales y promociones

Cuando se copia una campaña entre espacios de trabajo, los Bloques de contenido no se copian. Sin embargo, se puede hacer referencia a un Content Block en el área de trabajo de destino si existe un bloque con el mismo nombre. Como alternativa, puede crear el Bloque de contenido (o estas referencias líquidas) en el espacio de trabajo de destino para evitar errores al lanzar una campaña.

### Copiar campañas con banderas de características

Para copiar una campaña de bandera de características entre espacios de trabajo, asegúrate de que el espacio de trabajo de destino tiene un [experimento de bandera de características]({{site.baseurl}}/developer_guide/feature_flags/experiments) configurado con un ID que coincide con la bandera de características a la que se hace referencia en la campaña original. Si copias una campaña pero en el espacio de trabajo de destino no existe un ID de bandera de característica que coincida, la selección de bandera de característica en la campaña quedará en blanco al copiarla, y tendrás que seleccionar una diferente.

[1]: {% image_buster /assets/img_archive/clone_campaign.png %}

