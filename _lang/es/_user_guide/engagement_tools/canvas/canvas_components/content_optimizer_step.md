---
nav_title: Optimizador de contenidos
article_title: Paso del agente Content Optimizer 
alias: "/content_optimizer_step/"
page_order: 5
description: "El paso del agente Content Optimizer te permite configurar y probar varias versiones de componentes de contenido en un solo paso. Te ayuda a experimentar con variaciones de contenido y se optimiza automáticamente hacia las combinaciones con mejor rendimiento a lo largo del tiempo."
page_type: reference

---

# Paso del agente Content Optimizer

> El paso del agente Content Optimizer te permite configurar y probar varias versiones de componentes de contenido en un solo paso. Te ayuda a experimentar con variaciones de contenido y se optimiza automáticamente hacia las combinaciones con mejor rendimiento a lo largo del tiempo. Para una introducción, consulta [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
Content Optimizer se encuentra actualmente en fase beta. Para obtener ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

## Creación de un paso de Content Optimizer

Para obtener los mejores resultados, utiliza el agente Content Optimizer en Canvas donde los usuarios vayan entrando gradualmente a lo largo del tiempo. Si todos los usuarios entran en el paso a la vez, el agente no tendrá tiempo para aprender de los primeros resultados. 

### Paso 1: Añadir un paso

Arrastra y suelta el componente **Content Optimizer** desde la barra lateral, o selecciona el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y selecciona **Content Optimizer**.

### Paso 2: Crea tu mensaje base

El mensaje base es el punto de partida para tu paso. Las variantes de cada componente de contenido se insertan dinámicamente en función de las combinaciones definidas en la pestaña **Content Optimizer Settings**. 

{% alert note %}
Durante el periodo beta, el correo electrónico es el único canal compatible. 
{% endalert %}

En la pestaña **Messaging Channels**, selecciona **Email** y crea tu mensaje de correo electrónico base. Consulta nuestra sección dedicada al [correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email) para obtener ayuda. 

El agente Content Optimizer utiliza la configuración de envío (como el dominio de correo electrónico y la dirección de responder a) especificada en esta variante para enviar todos los mensajes. Puedes empezar con un diseño nuevo o seleccionar una plantilla existente para este mensaje. En este paso, piensa qué componentes del mensaje quieres optimizar. Los definirás en [el paso 4](#step-4).

Los componentes compatibles para optimizar incluyen:

- Subject
- Body Header
- Body Content
- Primary CTA

### Paso 3: Especificar la configuración de entrega

En la pestaña **Delivery Settings**, puedes especificar si el paso debe utilizar Intelligent Timing o las validaciones de entrega. Para obtener más información, consulta [Editar la configuración de entrega]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) en el paso Mensaje.

### Paso 4: Añadir componentes y variantes de contenido {#step-4}

Los componentes de contenido son los elementos individuales del mensaje que deseas probar, como diferentes líneas del asunto, titulares, texto del cuerpo o llamadas a la acción principales. Estos componentes te permiten generar múltiples versiones de un mensaje y optimizarlas automáticamente en función del rendimiento a lo largo del tiempo.

Puedes añadir hasta tres componentes de contenido por paso y hasta cinco variantes por componente, lo que da un total de 125 combinaciones de contenido únicas.

![Opciones para añadir y configurar componentes de contenido en la interfaz de Content Optimizer. La interfaz muestra componentes seleccionables, como Subject, Body Header, Body Content y Primary CTA, cada uno con campos para introducir diferentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Paso 4.1: Configurar componentes de contenido

Para configurar los componentes:

1. Ve a la pestaña **Content Optimizer Settings**.
2. Elige los componentes que deseas optimizar. Opciones compatibles:
  - Subject
  - Body Header
  - Body Content
  - Primary CTA
3. Para cada componente seleccionado, define un conjunto de versiones alternativas de ese contenido (variantes). Utiliza variantes claras y distintas que difieran en tono, estructura o contenido. Esto ayuda a Content Optimizer a identificar las combinaciones con mejor rendimiento de forma más eficaz. Puedes:
  - Escribir tus propias variantes manualmente.
  - Utilizar las sugerencias generadas por IA para explorar nuevas opciones rápidamente.

![Interfaz de Content Optimizer Settings que muestra opciones para añadir y configurar componentes de contenido para la optimización del correo electrónico. Cada componente tiene campos de entrada para introducir diferentes variantes. El texto visible incluye nombres de componentes y campos para introducir texto de variantes.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Paso 4.2: Añade Liquid a tu mensaje

Después de definir al menos dos variantes para cada componente, copia la etiqueta de Liquid asociada a cada una y pégala en la ubicación correspondiente de tu mensaje base.

- Por ejemplo, si estás optimizando la línea del asunto, pega la etiqueta {% raw %}`{% message_component "Subject" %}`{% endraw %} en el campo de asunto del editor de correo electrónico.
- También puedes incluir etiquetas de componentes dentro de textos más largos para probar solo una parte del componente. Por ejemplo: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Opciones para añadir y configurar componentes de contenido, como Subject, Body Header, Body Content y Primary CTA. Cada componente tiene campos para introducir diferentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si no añades una etiqueta de Liquid para un componente de contenido seleccionado, aparecerá una advertencia en la pestaña **Content Optimizer Settings** y un error en la pestaña **Messaging Channels**. El Canvas no se puede lanzar hasta que todos los componentes seleccionados se hayan añadido correctamente al mensaje base.

A medida que se ejecuta el Canvas, el agente mezcla y combina variantes entre componentes para generar diferentes combinaciones de contenido. Con el tiempo, se da prioridad a las combinaciones de mayor rendimiento para su entrega, lo que te ayuda a mejorar el rendimiento sin intervención manual.

#### Referencia de Liquid

| Componente | Fragmento de código Liquid |
| --- | --- | 
| Subject | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Body Header | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Body Content | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| Primary CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 5: Seleccionar evento de optimización

El evento de optimización determina cómo el agente Content Optimizer evalúa el rendimiento y asigna el tráfico a las combinaciones de contenido a lo largo del tiempo. 

En el caso del correo electrónico, puedes optimizar para uno de los siguientes eventos. El agente utiliza las aperturas y los clics registrados en los 7 días posteriores al envío de un mensaje para orientar la entrega hacia combinaciones de contenido con mejor rendimiento.

| Evento | Descripción | Casos de uso |
| --- | --- | --- |
| Aperturas | Optimiza las combinaciones que hacen que los destinatarios abran el correo electrónico. | Probar líneas del asunto o intentar aumentar la visibilidad |
| Clics | Optimiza las combinaciones que impulsan la interacción con los enlaces. No incluye los clics de bots ni los clics para cancelar suscripción reconocidos por Braze. | Aumentar el tráfico, la interacción o la conversión a partir de enlaces |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

El evento de optimización seleccionado se aplica a todos los componentes de contenido de este paso. 

## Buenas prácticas

- En general, recomendamos probar más de un componente en el paso de Content Optimizer.
- Si estás optimizando para clics, incluye líneas del asunto en tus pruebas, ya que unas líneas del asunto más potentes pueden contribuir a aumentar las aperturas y crear más oportunidades de clics.
- Si estás optimizando para aperturas, centra tus pruebas en la línea del asunto.

## Análisis

Para revisar el rendimiento, abre el panel de análisis a nivel de paso para ver las métricas por variante de contenido y el rendimiento general de la combinación. El paso Content Optimizer utiliza los [mismos análisis que el paso Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics).

![Análisis de Content Optimizer para tres botones y el porcentaje de asignación de envíos, que tiende al alza.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

## Solución de problemas

| Problema | Descripción | Solución |
| --- | --- | --- |
| Etiquetas de Liquid faltantes | Si añades un componente de contenido (como Subject o CTA) pero no insertas la etiqueta de Liquid correspondiente en tu mensaje base, verás lo siguiente: <br>- Una advertencia en la pestaña **Content Optimizer Settings** <br>- Un error en la pestaña **Messaging Channels** | Copia el fragmento de código Liquid que aparece debajo de cada componente en la pestaña **Content Optimizer Settings** y pégalo en la parte correspondiente de tu mensaje. |
| Etiquetas de Liquid huérfanas | Si eliminas un componente de contenido pero dejas su etiqueta de Liquid en el mensaje base, es posible que el mensaje no se muestre como esperabas al enviarlo. | Elimina cualquier etiqueta `message_component` no utilizada del mensaje base antes de lanzarlo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }