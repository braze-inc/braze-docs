---
nav_title: Aliasing de enlaces
article_title: Aliasing de enlaces
alias: /link_aliasing/
page_order: 3
description: "Este artículo describe cómo funciona el aliasing de enlaces y proporciona ejemplos del aspecto que tendrán tus enlaces."
channel:
  - email

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"} aliasing de enlaces
 
> Utiliza el aliasing de enlaces para crear nombres reconocibles, generados por el usuario, para identificar los enlaces enviados en mensajes de correo electrónico de Braze. Estos enlaces están disponibles para reorientar la segmentación, desencadenar acciones y realizar análisis de enlaces.

## Acerca del aliasing de enlaces

Con el aliasing de enlaces, puedes crear nombres generados por el usuario para identificar y seguir los enlaces enviados en correos electrónicos. De este modo, puedes utilizar eficazmente estos aliasing de enlaces reconocibles en tus correos electrónicos para realizar un seguimiento de la interacción y analizar el rendimiento de la campaña, sin necesidad de hacer referencia al enlace completo.

Con el aliasing de enlaces, puedes:

- **Reorienta a los usuarios que hayan hecho clic en enlaces específicos:** Identificar y dirigirte a los usuarios que han hecho clic en un enlace.
- **Crea desencadenantes basados en acciones:** Envía un correo electrónico cuando un usuario haga clic en un enlace.
- **Analiza las métricas:** Compara cuántos usuarios han hecho clic en el Enlace A frente al Enlace B.

### Cómo funciona

Braze identifica de forma única los enlaces dentro de los correos electrónicos añadiendo un parámetro extra llamado `lid` (también conocido como identificador de enlace) a cada URL de enlace. Este valor de `lid` permite a Braze seguir, controlar y agregar las interacciones de los usuarios con el enlace aunque el resto de los parámetros de la URL puedan ser diferentes. Esto ayuda a obtener información sobre cómo interactúan los usuarios con el contenido de tus campañas de correo electrónico.

Los identificadores de enlace también se actualizarán si se duplica una campaña de correo electrónico, un Canvas con un mensaje de correo electrónico o un bloque de contenido.

## Crear un alias de enlace

Para crear un alias de enlace, sigue estos pasos: 

1. En tu campaña o componente Canvas, ve al cuerpo de tu correo electrónico.
2. Selecciona la pestaña **Gestión de enlaces**.
3. Braze genera automáticamente aliasing de enlaces predeterminados únicos para cada uno de tus enlaces.
4. Dale un nombre al alias. Los alias deben tener un nombre único por variante de campaña de correo electrónico o componente Canvas. 

También puedes establecer un alias que se utilizará para hacer referencia a un enlace específico cuando se trate de informes o segmentación. 

Página de gestión de enlaces con cuatro aliasing de enlaces.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
El aliasing de enlaces sólo se admite en los atributos `href` dentro de las etiquetas de anclaje HTML, donde es seguro añadir un parámetro de consulta. Es una buena práctica incluir un signo de interrogación (?) al final de tu enlace para que Braze pueda añadir fácilmente el valor `lid`. Sin añadir el valor `lid`, Braze no reconocerá la URL para aliasing de enlaces.
{% endalert %}

## Gestión de aliasing de enlaces

Para ver todos tus aliasing de enlaces rastreados, haz lo siguiente:

1. Ve a **Configuración** > **Preferencias de correo electrónico** en **Configuración del espacio de trabajo**.
2. Selecciona la pestaña **Configuración de aliasing de enlaces**.

{% alert important %}
Si utilizas la [navegación antigua]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), estas configuraciones se encuentran en **Administrar configuración**.
{% endalert %}

Aquí puedes ordenar, buscar y desactivar el seguimiento de aliasing de enlaces.

\![Página de aliasing de enlaces con seguimiento que muestra dos aliasing de enlaces llamados "TechPartners" y "Help" que están asociados a una campaña llamada "Email_Survey".]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Utiliza el [alias de enlace de lista para campaña]({{site.baseurl}}/get_campaign_link_alias/) y [el alias de enlace de lista para]({{site.baseurl}}/get_canvas_link_alias/) puntos finales de [Canvas]({{site.baseurl}}/get_canvas_link_alias/) para extraer el conjunto `alias` en cada variante de mensaje de una campaña o de un componente Canvas específico de correo electrónico.
{% endalert %}

Braze recomienda evaluar los enlaces dentro del correo electrónico, añadir plantillas de enlaces y proporcionar una convención de nomenclatura que funcione a efectos de segmentación y elaboración de informes. Esto te ayuda a hacer un seguimiento de todos los enlaces.

Cuando el aliasing de enlaces está activado, los mensajes, los bloques de contenido y las plantillas de enlaces no se modifican. Cualquier mensaje existente que utilice plantillas de enlaces o bloques de contenido será el mismo. Sin embargo, cuando actualices un mensaje, el marcado de alias de enlace se aplicará a todos los enlaces, por lo que tendrás que volver a aplicar las plantillas de enlace para que los enlaces sean visibles.

## Cómo se actualizan los enlaces con el aliasing de enlaces

Las tablas siguientes proporcionan ejemplos de enlaces en el cuerpo de un correo electrónico, resultados del aliasing de enlaces y explicaciones sobre cómo se actualiza el enlace original con el aliasing de enlaces.

### Permalink

**Lógica:** Braze inserta un signo de interrogación (?) y añade el primer parámetro de consulta en la URL.

| Enlace en el cuerpo del correo electrónico    | Enlace con Aliasing                     |
|-----------------------|----------------------------------------|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Enlace con más parámetros de consulta

**Lógica:** Braze detecta otros parámetros de consulta y añade `lid=` al final de la URL.

| Enlace en el cuerpo del correo electrónico                                            | Enlace con Aliasing                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Enlace HTML

**Lógica:** Braze reconoce que un enlace es una URL y ya tiene un signo de interrogación (?), por lo que el parámetro de consulta `lid` se añade después del signo de interrogación.

| Enlace en el cuerpo del correo electrónico                                                | Enlace con Aliasing                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Enlace con anclaje

**Lógica:** Braze espera que la URL utilice una estructura estándar en la que haya anclas (#) después de un signo de interrogación (?). Como Braze lee de izquierda a derecha, el signo de interrogación y el valor `lid` se añaden antes del ancla.

| Enlace en el cuerpo del correo electrónico                               | Enlace con Aliasing                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Enlace con ancla y etiqueta de captura

**Lógica:** Al utilizar el aliasing de enlaces con URL que contienen anclas (#), Braze espera que el ancla se coloque después de los parámetros de consulta. Esto significa que el valor `lid` debe añadirse antes del ancla para que el seguimiento sea correcto, y como Braze lee la URL de izquierda a derecha, el signo de interrogación (?) y `lid` deben ir antes del ancla.

| Enlace en el cuerpo del correo electrónico                                                                        | Enlace con Aliasing                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions#special-offer?lid={{link_alias}}">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Seguimiento de aliasing de enlaces

En la pestaña **Gestión de enlaces**, selecciona qué alias quieres que sean "seguidos" con fines de segmentación y que estén presentes en los filtros de segmentación. Ten en cuenta que los aliasing de enlaces rastreados sólo tienen fines de segmentación y no influirán en el rastreo de tu enlace a efectos de elaboración de informes.

{% alert tip %}
Para hacer un seguimiento de las métricas de interacción del enlace, asegúrate de que tu enlace precede con HTTP o HTTPS. Para desactivar el seguimiento de clics de enlaces específicos, consulta [Enlaces universales y Enlaces de aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

Braze te permite seleccionar un número ilimitado de enlaces de seguimiento, aunque sólo puedes reorientar a los usuarios a los enlaces más recientes que hayan abierto. Los perfiles de usuario incluyen los 100 enlaces en los que se ha clicado más recientemente. Por ejemplo, si haces un seguimiento de 500 enlaces y un usuario hace clic en los 500, puedes reorientar o crear segmentos basados en los 100 enlaces en los que se ha hecho clic más recientemente.

{% tabs local %}
{% tab Drag-And-Drop Editor %}

\![Pestaña de gestión de enlaces del editor de arrastrar y soltar correo electrónico.]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab HTML editor %}

\![Pestaña de gestión de enlaces del editor HTML de correo electrónico.]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Braze sólo realiza un seguimiento de hasta los últimos 100 aliasing de enlaces en los que se ha hecho clic a nivel de perfil.
{% endalert %}

### Filtros basados en acciones
 
Puedes crear mensajes basados en acciones dirigidos a cualquier enlace (con o sin seguimiento) o reorientar a los usuarios en función de si han hecho clic en un alias a través de cualquier campaña de correo electrónico o componente de Canvas.

\![Opciones basadas en acciones para dirigirse a usuarios que han hecho clic en un alias de un componente Canvas o han interactuado con una campaña.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### Filtros de segmentación

En Braze, si tienes un alias de enlace en tu correo electrónico y un usuario hace clic en él, el evento se registra en el perfil del usuario con el alias.

Si utilizas el filtro de segmentación "Alias de clic en cualquier campaña o paso en Canvas" y más tarde decides cambiar el nombre de este alias de enlace, los datos de clic anteriores del perfil de usuario **no** se actualizarán, lo que significa que seguirá mostrándose como el alias de enlace anterior. Por tanto, si te diriges a los usuarios basándote en el nuevo alias de enlace, no incluirá los datos del alias de enlace anterior.

Si utilizas el filtro de segmentación "Alias clicado en campaña" o "Alias clicado en Canvas", filtrarás a tus usuarios en función de si han hecho clic en un alias específico en una campaña o Canvas concretos. Si varios usuarios comparten la misma dirección de correo electrónico y se hace clic en el enlace alias, todos los demás usuarios que compartan la dirección de correo electrónico verán actualizados sus perfiles de usuario. 

Los siguientes filtros de segmentación se aplican a los eventos de clic que son objeto de seguimiento en el momento en que se procesa el evento. Esto significa que los enlaces sin seguimiento no eliminarán los datos existentes y que el seguimiento de un enlace no rellenará los datos. Para más detalles, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

#### Enlaces no rastreables

Al eliminar el seguimiento de un enlace no se reasignarán los segmentos existentes con el filtro al alias sin seguimiento. Los datos antiguos permanecerán en los perfiles de usuario hasta que sean sustituidos por datos más recientes. 

Los enlaces de los mensajes archivados se eliminan automáticamente. Sin embargo, si se desarchivan los mensajes archivados, habrá que volver a hacer el seguimiento de los enlaces. Cuando se hace un seguimiento de los alias de enlaces, los informes de enlaces se indexan por el alias en lugar de por los dominios de nivel superior o las URL completas.

\![Pestaña de análisis de campaña que muestra tres aliasing de enlaces y sus clics totales.]({% image_buster /assets/img/link_aliasing_click_table.png %})

### Evento de clics en el correo electrónico

Si exportas tus datos de interacción con Currents, un evento de clic de correo electrónico será ligeramente diferente si tienes habilitado el aliasing de enlaces. Tendrá dos campos adicionales para el [evento de clics de correo electrónico]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/) cuando el aliasing de enlaces esté activado: `link_id` y `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
El comportamiento de `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los Pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están "programados". Más información sobre [el comportamiento]({{site.baseurl}}/help/help_articles/data/dispatch_id/) de [`dispatch_id` en Canvas y las campañas.]({{site.baseurl}}/help/help_articles/data/dispatch_id/) 

_Actualización anotada en agosto de 2019._
{% endalert %}

## aliasing de enlaces en bloques de contenido

Los enlaces de los nuevos bloques de contenido se modificarán y Braze añadirá un `lid={{placeholder}}` a cada enlace cuando proceda. Este valor de marcador de posición se resuelve cuando se inserta en una variante de mensaje de correo electrónico.

Para modificar los enlaces dentro de los Bloques de contenido existentes que se crearon antes de que Braze habilitara el aliasing de enlaces, duplica los Bloques de contenido existentes y, a continuación, modifica los enlaces dentro de los Bloques de contenido duplicados.

Cuando se inserta un bloque de contenido sin valor `lid` en un mensaje nuevo, los enlaces de ese bloque de contenido no se siguen con un alias. Cuando se inserta un nuevo bloque de contenido en una variante de mensaje "antigua", los enlaces de esa variante de mensaje se reconocerán mediante el aliasing de enlaces. También se reconocen los enlaces del Bloque de contenido. Sin embargo, los Bloques de contenido "antiguos" no pueden anidar Bloques de contenido "nuevos".

{% alert tip %}
Para los bloques de contenido, Braze recomienda crear copias de los bloques de contenido existentes para utilizarlos en mensajes nuevos. Esto puede hacerse mediante duplicación masiva para evitar situaciones en las que podrías hacer referencia a un bloque de contenido que no ha sido habilitado para el aliasing de enlaces en un mensaje nuevo.
{% endalert %}

## aliasing de enlaces para URL generadas por Liquid

Para las URL generadas por Liquid, como las declaraciones `assign` en el HTML o desde un bloque de contenido, debes añadir un signo de interrogación (`?`) a la etiqueta de Liquid. Esto permite a Braze añadir parámetros de consulta (`lid = somevalue`) para que el aliasing de enlaces funcione correctamente. Sin identificar dónde añadir los parámetros de consulta, el aliasing de enlaces no reconocerá estas URL y no se aplicarán las plantillas de enlaces.

### Ejemplo

Consulta este ejemplo de aliasing de enlaces para ver el formato recomendado para el enlace:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

Si el enlace tiene parámetros que contienen un signo de interrogación (`?`), puedes sustituirlo en la etiqueta de anclaje por un ampersand (`&`), como en este ejemplo:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}


