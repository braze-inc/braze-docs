---
nav_title: Optimizador de contenidos
article_title: Paso del agente Content Optimizer 
alias: "/content_optimizer_step/"
page_order: 5
description: "El paso del agente Content Optimizer te permite configurar y probar varias versiones de componentes de contenido en un solo paso. Te ayuda a experimentar con variaciones de contenido y se optimiza automáticamente hacia las combinaciones con mejor rendimiento a lo largo del tiempo."
page_type: reference

---

# Paso del agente Content Optimizer

> El paso del agente Content Optimizer te permite configurar y probar varias versiones de componentes de contenido en un solo paso. Te ayuda a experimentar con variaciones de contenido y se optimiza automáticamente hacia las combinaciones con mejor rendimiento a lo largo del tiempo. Para obtener una introducción, consulta [Optimizador de contenido]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
Content Optimizer se encuentra actualmente en fase beta. Para obtener ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Creación de un paso de optimizador de contenido

Para obtener los mejores resultados, utiliza el agente Content Optimizer en lienzos en los que los usuarios vayan entrando gradualmente a lo largo del tiempo. Si todos los usuarios entran en la etapa a la vez, el agente no tendrá tiempo para aprender de los primeros resultados. 

### Paso 1: Añadir un paso

Arrastre y suelte el componente **Optimizador de contenido** desde la barra lateral, o seleccione el botón<i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y seleccione **Optimizador de contenido**.

### Paso 2: Crea tu mensaje base

El mensaje base es el punto de partida para tu paso. Las variantes de cada componente de contenido se insertan dinámicamente en función de las combinaciones definidas en la pestaña **Configuración del optimizador de contenido**. 

{% alert note %}
Durante el periodo beta, el correo electrónico es el único canal compatible.
{% endalert %}

En la pestaña **Canales de mensajería**, selecciona **Correo electrónico** y crea tu mensaje de correo electrónico básico. Consulta nuestra sección dedicada [al correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email) para obtener ayuda. 

El agente Content Optimizer utiliza la configuración de envío (como el dominio de correo electrónico y la dirección para responder) especificada en esta variante para enviar todos los mensajes. Puedes empezar con un diseño nuevo o seleccionar una plantilla existente para este mensaje. En este paso, piensa qué componentes del mensaje quieres optimizar. Los definirás en [el paso 4](#step-4).

Los componentes compatibles para optimizar incluyen:

- Asunto
- Encabezado del cuerpo
- Contenido del cuerpo
- CTA primario

### Paso 3: Especificar la configuración de entrega

En la pestaña **Configuración de entrega**, puedes especificar si el paso debe utilizar Intelligent Timing o las validaciones de entrega. Para obtener más información, consulta [Editar la configuración de entrega]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) en el paso Mensaje.

### Paso 4: Añadir componentes y variantes de contenido {#step-4}

Los componentes del contenido son los elementos individuales del mensaje que deseas probar, como diferentes líneas del asunto, titulares, texto del cuerpo o llamadas a la acción principales. Estos componentes te permiten generar múltiples versiones de un mensaje y optimizarlas automáticamente en función del rendimiento a lo largo del tiempo.

Puedes añadir hasta tres componentes de contenido por paso y hasta cinco variantes por componente, lo que da un total de 125 combinaciones de contenido únicas.

![Opciones para añadir y configurar componentes de contenido en la interfaz de Content Optimizer. La interfaz muestra componentes seleccionables, como Asunto, Encabezado del cuerpo, Contenido del cuerpo y CTA principal, cada uno con campos para introducir diferentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Paso 4.1: Configurar componentes de contenido

Para configurar los componentes:

1. Ve a la pestaña **Configuración del optimizador de contenido**.
2. Elige los componentes que deseas optimizar. Opciones compatibles:
  - Asunto
  - Encabezado del cuerpo
  - Contenido del cuerpo
  - CTA primario
3. Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Utiliza variantes claras y distintas que difieran en tono, estructura o contenido. Esto ayuda a Content Optimizer a identificar el rendimiento de los mejores empleados de forma más eficaz. Puedes:
  - Escribe tus propias variantes manualmente.
  - Utiliza las sugerencias generadas por IA para explorar nuevas opciones rápidamente.

![Interfaz de configuración del optimizador de contenido que muestra opciones para añadir y configurar componentes de contenido para la optimización del correo electrónico. Cada componente tiene campos de entrada para introducir diferentes variantes. El texto visible incluye nombres de componentes y campos para introducir texto variante.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Paso 4.2: Añade líquido a tu mensaje

Después de definir al menos dos variantes para cada componente, copia la etiqueta de Liquid asociada a cada una y pégala en la ubicación correspondiente de tu mensaje base.

- Por ejemplo, si estás optimizando la línea del asunto, pega la{% raw %}`{% message_component "Subject" %}`{% endraw %}etiqueta  en el campo de asunto del editor de correo electrónico.
- También puedes incluir etiquetas de componentes dentro de textos más largos para probar solo una parte del componente. Por ejemplo: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Opciones para añadir y configurar componentes de contenido, como asunto, encabezado del cuerpo, contenido del cuerpo y CTA principal. Cada componente tiene campos para introducir diferentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si no añades una etiqueta de Liquid para un componente de contenido seleccionado, aparecerá una advertencia en la pestaña **Configuración del optimizador de contenido** y un error en la pestaña **Canales de mensajería**. El Canvas no se puede iniciar hasta que todos los componentes seleccionados se hayan añadido correctamente al mensaje base.

A medida que se ejecuta Canvas, el agente mezcla y combina variantes entre componentes para generar diferentes combinaciones de contenido. Con el tiempo, se da prioridad a las combinaciones de mayor rendimiento para su entrega, lo que te ayuda a mejorar el rendimiento sin intervención manual.

#### Referencia líquida

| Componente | Fragmento de código líquido |
| --- | --- | 
| Asunto | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Encabezado del cuerpo | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Contenido del cuerpo | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| CTA primario | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 5: Seleccionar evento de optimización

El evento de optimización determina cómo el agente Content Optimizer evalúa el rendimiento y asigna el tráfico a las combinaciones de contenido a lo largo del tiempo. 

En el caso del correo electrónico, puedes optimizarlo para uno de los siguientes eventos. El agente utiliza las aperturas y los clics registrados en los 7 días posteriores al envío de un mensaje para orientar la entrega hacia combinaciones de contenido con mejor rendimiento.

| Evento | Descripción | Ejemplos |
| --- | --- | --- |
| Aperturas | Optimiza las combinaciones que hacen que los destinatarios abran el correo electrónico. | Probar líneas del asunto o intentar aumentar la visibilidad |
| Clics | Optimiza las combinaciones que impulsan la interacción con los enlaces. No incluye los clics de bots ni los clics para cancelar la suscripción reconocidos por Braze. | Aumentar el tráfico, la interacción o la conversión a partir de enlaces. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

El evento de optimización seleccionado se aplica a todos los componentes de contenido de este paso. 

## Análisis

Para revisar el rendimiento, abre el panel de análisis por pasos para ver las métricas por variante de contenido y el rendimiento general de la combinación. El paso Optimizador de contenido utiliza los [mismos análisis que el paso Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics).

![Análisis de Content Optimizer para tres botones y el porcentaje de asignación de envíos, que tiende al alza.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

## Solución de problemas

| Problema | Descripción | Arregla |
| --- | --- | --- |
| Etiquetas de Liquid perdidas | Si añades un componente de contenido (como Asunto o CTA) pero no insertas la etiqueta de Liquid correspondiente en tu mensaje base, verás lo siguiente: <br>\- Una advertencia en la pestaña **Configuración del optimizador de contenido.** <br>\- Un error en la pestaña **Canales de mensajería.** | Copia el fragmento de código Liquid que aparece debajo de cada componente en la pestaña **Configuración del optimizador de contenido** y pégalo en la parte correspondiente de tu mensaje. |
| Etiquetas de Liquid huérfanas | Si eliminas un componente de contenido pero dejas su etiqueta de Liquid en el mensaje base, es posible que el mensaje no se muestre como esperabas al enviarlo. | Elimina cualquier etiqueta `message_component`no utilizada del mensaje base antes de lanzarlo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

