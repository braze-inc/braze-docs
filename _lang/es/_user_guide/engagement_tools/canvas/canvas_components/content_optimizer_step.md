---
nav_title: Optimizador de contenidos
article_title: Paso del agente Optimizador de Contenidos 
alias: "/content_optimizer_step/"
page_order: 5
description: "El paso de agente Optimizador de Contenidos te permite configurar y probar varias versiones de componentes de contenido en un solo paso. Te ayuda a experimentar con variaciones de contenido y optimiza automáticamente hacia las combinaciones de mejor rendimiento a lo largo del tiempo."
page_type: reference

---

# Paso del agente Optimizador de Contenidos

> El paso de agente Optimizador de Contenidos te permite configurar y probar varias versiones de componentes de contenido en un solo paso. Te ayuda a experimentar con variaciones de contenido y optimiza automáticamente hacia las combinaciones de mejor rendimiento a lo largo del tiempo. Para una introducción, consulta [Optimizador de Contenidos]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
El Optimizador de Contenidos está actualmente en fase beta. Si necesitas ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Crear un paso del Optimizador de Contenidos

Para obtener los mejores resultados, utiliza el agente Optimizador de Contenidos en Lienzos en los que los usuarios introduzcan el paso gradualmente a lo largo del tiempo. Si todos los usuarios entran en el paso a la vez, el agente no tendrá tiempo de aprender de los primeros resultados. 

### Paso 1: Añade un paso

Arrastra y suelta el componente **Optimizador de Contenidos** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **Optimizador de Contenidos**.

### Paso 2: Crea tu mensaje base

El mensaje base es el punto de partida de tu paso. Las variantes de cada componente de contenido se insertan dinámicamente en función de las combinaciones definidas en la pestaña **Configuración del optimizador de contenido**. 

{% alert note %}
Durante el periodo beta, el correo electrónico es el único canal admitido.
{% endalert %}

En la pestaña **Canales de mensajería**, selecciona **Correo electrónico** y crea tu mensaje de correo electrónico base. Consulta nuestra sección dedicada [al correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email) para obtener ayuda. 

El agente Optimizador de Contenidos utiliza la configuración de envío (como el dominio de correo electrónico y la dirección de responder a) especificada en esta variante para enviar todos los mensajes. Puedes empezar con un nuevo diseño o seleccionar una plantilla existente para este mensaje. En este paso, considera qué componentes del mensaje quieres optimizar. Los definirás en [el paso 4](#step-4).

Los componentes que se pueden optimizar son

- Asunto
- Encabezado del cuerpo
- Contenido del cuerpo
- CTA primario

### Paso 3: Especifica la configuración de entrega

En la pestaña **Configuración de entrega**, puedes especificar si el paso debe utilizar Intelligent Timing o validaciones de entrega. Para más detalles, consulta [Editar configuración de entrega]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) en el paso Mensaje.

### Paso 4: Añadir componentes de contenido y variantes {#step-4}

Los componentes del contenido son los elementos individuales de tu mensaje que quieres probar, como diferentes líneas del asunto, titulares, cuerpo del texto o llamadas a la acción principales. Estos componentes te permiten generar varias versiones de un mensaje y optimizarlas automáticamente en función del rendimiento a lo largo del tiempo.

Puedes añadir hasta tres componentes de contenido por paso y hasta cinco variantes por componente, para un total de 125 combinaciones de contenido únicas.

![Opciones para añadir y configurar componentes de contenido en la interfaz del Optimizador de Contenidos. La interfaz muestra componentes seleccionables como Asunto, Encabezado del cuerpo, Contenido del cuerpo y CTA principal, cada uno con campos para introducir distintas variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Paso 4.1: Configurar componentes de contenido

Para configurar los componentes:

1. Ve a la pestaña **Configuración del Optimizador de Contenidos**.
2. Elige qué componentes quieres optimizar. Opciones admitidas:
  - Asunto
  - Encabezado del cuerpo
  - Contenido del cuerpo
  - CTA primario
3. Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Utiliza variantes claras y distintas que difieran en el tono, la estructura o el contenido. Esto ayuda al Optimizador de Contenidos a identificar a los que más rinden con mayor eficacia. Puedes hacerlo:
  - Escribe manualmente tus propias variantes.
  - Utiliza las sugerencias generadas por la IA para explorar nuevas opciones rápidamente.

![Interfaz de configuración del optimizador de contenido que muestra opciones para añadir y configurar componentes de contenido para la optimización del correo electrónico. Cada componente tiene campos de entrada para introducir distintas variantes. El texto visible incluye los nombres de los componentes y los campos para introducir texto variante.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Paso 4.2: Añadir Liquid a tu mensaje

Tras definir al menos dos variantes para cada componente, copia la etiqueta de Liquid asociada a cada una y pégala en la ubicación correspondiente de tu mensaje base.

- Por ejemplo, si estás optimizando la línea del asunto, pega la etiqueta {% raw %}`{% message_component "Subject" %}`{% endraw %} en el campo del asunto del compositor del correo electrónico.
- También puedes incluir etiquetas de componentes dentro de un texto más largo para probar sólo una parte del componente. Por ejemplo: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Opciones para añadir y configurar componentes de contenido como Asunto, Encabezado del cuerpo, Contenido del cuerpo y CTA principal. Cada componente tiene campos para introducir distintas variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si no añades una etiqueta de Liquid para un componente de contenido seleccionado, verás una advertencia en la pestaña **Configuración del optimizador de contenido** y un error en la pestaña **Canales de mensajería**. El Canvas no puede lanzarse hasta que todos los componentes seleccionados se hayan añadido correctamente a tu mensaje base.

A medida que se ejecuta el Canvas, el agente mezcla y combina variantes entre los componentes para generar diferentes combinaciones de contenido. Con el tiempo, las combinaciones de mayor rendimiento se priorizan para su entrega, ayudándote a mejorar el rendimiento sin intervención manual.

#### Referencia líquida

| Componente | Fragmento de código Liquid |
| --- | --- | 
| Asunto | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Encabezado del cuerpo | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Contenido del cuerpo | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| CTA primario | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 5: Seleccionar evento de optimización

El evento de optimización determina cómo el agente Optimizador de Contenidos evalúa el rendimiento y asigna el tráfico a las combinaciones de contenidos a lo largo del tiempo. 

Para el correo electrónico, puedes optimizar uno de los siguientes eventos. El agente utiliza las aperturas y los clics que se registran en los 7 días siguientes al envío de un mensaje para desplazar la entrega hacia combinaciones de contenidos de mayor rendimiento.

| Evento | Descripción | Ejemplos |
| --- | --- | --- |
| Aperturas | Optimiza las combinaciones para que los destinatarios abran el correo electrónico. | Probar las líneas del asunto o intentar aumentar la visibilidad |
| Clics | Optimiza las combinaciones que impulsan la interacción con los enlaces. No incluye los clics de bot ni los clics de cancelar suscripción reconocidos por Braze. | Generar tráfico, interacción o conversión a partir de enlaces |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

El evento de optimización seleccionado se aplica a todos los componentes de contenido en este paso. 

## Análisis

Para revisar el rendimiento, abre el panel de análisis por pasos para ver las métricas por variante de contenido y el rendimiento general de la combinación. El paso Optimizador de contenidos utiliza los mismos análisis que el paso Mensajes. Para más detalles, consulta el paso [Análisis]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics) en mensajes.  

## Solución de problemas

| Problema | Descripción | Arregla |
| --- | --- | --- |
| Etiquetas de Liquid que faltan | Si añades un componente de contenido (como Asunto o CTA) pero no insertas la etiqueta de Liquid correspondiente en tu mensaje base, verás lo siguiente <br>\- Una advertencia en la pestaña **Configuración del Optimizador de Contenidos**  <br>\- Un error en la pestaña **Canales de mensajería**  | Copia el fragmento de código de Liquid que aparece debajo de cada componente en la pestaña **Configuración del optimizador de contenido** y pégalo en la parte adecuada de tu mensaje. |
| Etiquetas de Liquid huérfanas | Si eliminas un componente de contenido pero dejas su etiqueta de Liquid en el mensaje base, es posible que el mensaje no se muestre como se espera al enviarlo. | Elimina las etiquetas `message_component` no utilizadas de tu mensaje base antes de lanzarlo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

