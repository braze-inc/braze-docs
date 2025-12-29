---
nav_title: Condiciones de carrera
article_title: Condiciones de carrera
alias: /race_conditions/
page_order: 9
page_type: reference
description: "Este artículo trata de las mejores prácticas para evitar que las condiciones de carrera afecten a tus campañas de mensajería."
toc_headers: h2
---

# Condiciones de carrera

> Una condición de carrera se produce cuando un resultado depende de la secuencia o sincronización de varios acontecimientos. Por ejemplo, si la secuencia deseada de acontecimientos es "Acontecimiento A" y luego "Acontecimiento B", pero a veces el "Acontecimiento A" llega primero, y otras veces el "Acontecimiento B" llega primero, eso se conoce como condición de carrera. Esto puede provocar resultados inesperados o errores, porque estos eventos compiten por acceder a recursos o datos compartidos.

{% multi_lang_include video.html id="LyJaxDoMtMs" align="right" %}

En Braze, pueden darse condiciones de carrera cuando se desencadenan varias acciones al mismo tiempo basadas en datos de usuario o eventos. Por ejemplo, si un usuario desencadena varias campañas (como registrarse en un boletín o realizar una compra), puede que no reciba los mensajes en el orden correcto.

## Tipos de condiciones de carrera

Los tipos más comunes de condiciones de carrera pueden ocurrir cuando haces lo siguiente:

- Dirigirse a nuevos usuarios
- Utilizar varios puntos finales de la API
- Filtros de audiencia y desencadenantes basados en la acción. 

Considera los siguientes escenarios y aplica las mejores prácticas para evitar estas condiciones de carrera.

## Supuesto 1: Dirigirse a nuevos usuarios

En Braze, una de las condiciones de carrera más comunes se produce con los mensajes dirigidos a usuarios recién creados. El orden previsto de los acontecimientos es

1. Se crea un usuario;
2. El mismo usuario recibe inmediatamente un mensaje, realiza un evento personalizado o registra un atributo personalizado.

Sin embargo, en algunos casos, el segundo suceso se desencadenará primero. Esto significa que se está intentando enviar un mensaje a un usuario que todavía no existe. Como resultado, el usuario nunca lo recibe. Esto también se aplica a los eventos o atributos, cuando el evento o atributo intenta registrarse en un perfil de usuario que aún no se ha creado.

### Buenas prácticas

#### Introduce retrasos

Después de crear un nuevo usuario, puedes añadir una demora antes de enviar campañas dirigidas o Lienzos. Este retraso permite que se cree el perfil de usuario y que se actualice cualquier atributo relevante que pueda determinar su elegibilidad para recibir el mensaje.

Por ejemplo, después de que un usuario se registre en tu aplicación, puedes enviarle una oferta promocional al cabo de 24 horas. O, si estás creando un usuario o registrando un atributo personalizado, puedes añadir un retraso de un minuto antes de proceder en tu proceso para evitar esta condición de carrera.

También puedes añadir este retraso en el [SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration) para el evento personalizado específico que desencadena la entrada de un nuevo usuario en un Canvas. 

## Supuesto 2: Utilizar varios puntos finales de la API

{% alert important %}
Utilizamos el procesamiento asíncrono para maximizar la velocidad y la flexibilidad. Esto significa que cuando las llamadas a la API se nos envían por separado, no podemos garantizar que se procesen en el orden en que se enviaron.
{% endalert %}

Hay algunas situaciones en las que varios puntos finales de la API también pueden dar lugar a esta condición de carrera, como cuando:

- Utilizar puntos finales de API separados para crear usuarios y desencadenar Lienzos o campañas
- Hacer varias llamadas separadas al punto final `/users/track` para actualizar atributos personalizados, eventos o compras.

Cuando la información del usuario se envía a Braze utilizando el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track), ocasionalmente puede tardar unos segundos en procesarse. Esto significa que cuando se realizan solicitudes simultáneamente a los puntos finales `/users/track` y de mensajería como `/campaign/trigger/send`, no hay garantía de que la información del usuario se actualice antes de enviar un mensaje.

{% alert note %}
Si se envían atributos de usuario y eventos en la misma solicitud (ya sea desde `/users/track` o desde el SDK), entonces Braze procesará los atributos antes que los eventos o que intentar enviar cualquier mensaje.
{% endalert %}

### Buenas prácticas

#### Cuando utilices varios puntos finales, envía tus peticiones de una en una

Si utilizas varios puntos finales, puedes intentar escalonar las peticiones para que cada una se complete antes de que empiece la siguiente. Esto puede reducir la posibilidad de una condición de carrera. Por ejemplo, si necesitas actualizar atributos de usuario y enviar un mensaje, espera primero a que el perfil de usuario se actualice completamente antes de enviar un mensaje utilizando un punto final.

Si envías una solicitud de API de mensajes programados, estas solicitudes deben estar separadas, y debe crearse un usuario antes de enviar la solicitud de API programada.

#### Incluir datos clave con el desencadenante

En lugar de utilizar varios puntos finales, puedes incluir los [atributos de usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object#object-body) y [las propiedades desencadenantes]({{site.baseurl}}/api/objects_filters/trigger_properties_object) en una sola llamada a la API utilizando el [punto final`campaign/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns). 

Cuando estos objetos se incluyen con el desencadenante, los atributos se procesarán primero, antes de que se desencadene el mensaje, eliminando posibles condiciones de carrera. Ten en cuenta que las propiedades desencadenantes no actualizan el perfil de usuario, sino que sólo se utilizan en el contexto del mensaje.

#### Utiliza el POST: Punto final de seguimiento de usuarios (sincronización)

Utiliza el [punto final`/users/track/sync/` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track_synchronous) para registrar eventos personalizados y compras y actualizar los atributos del perfil de usuario de forma sincrónica. Utilizar este punto final para actualizar los perfiles de usuario al mismo tiempo y en una sola llamada puede ayudar a evitar posibles condiciones de carrera.

{% alert important %}
Este punto final está actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en la beta.
{% endalert %}

## Escenario 3: Emparejar desencadenantes basados en acciones y filtros de audiencia

Otra condición de carrera habitual puede darse si configuras una campaña basada en acciones o Canvas con el mismo desencadenante que el filtro de audiencia (como un atributo modificado o la realización de un evento personalizado). El usuario puede no estar en la audiencia en el momento de realizar el evento desencadenante, lo que significa que no recibirá la campaña ni entrará en el Canvas.

### Buenas prácticas

#### Comprueba tu audiencia tras un retraso

Para evitar utilizar filtros de audiencia que contengan los criterios desencadenantes, te recomendamos que compruebes tu audiencia antes de la entrega. Por ejemplo, puedes [utilizar las validaciones de entrega]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#edit-delivery-settings) en los pasos de mensajería de Canvas como comprobación adicional para confirmar que tu audiencia cumple los criterios de entrega en el envío del mensaje. También puedes aprovechar los criterios de salida de Canvas para dar de baja a cualquier usuario en cualquier punto del recorrido del usuario si cumple tus criterios.

En el caso de las campañas, puedes utilizar eventos de salida para permitir que las campañas con un evento desencadenado aborten los mensajes a los usuarios que realicen el evento de salida mientras están en el retardo.

#### Utiliza filtros únicos con el evento desencadenante

Cuando configures tus filtros, quizá quieras añadir un filtro redundante "por si acaso". Sin embargo, esta redundancia puede dar lugar a más problemas. En su lugar, evita utilizar cualquier filtro que contenga el desencadenante siempre que sea posible. Esta es la ruta más segura para evitar una condición de carrera.

Por ejemplo, si el desencadenante de tu campaña es "Ha realizado una compra" y tu filtro de audiencia es "Ha realizado cualquier compra", esta redundancia puede provocar una condición de carrera. 

#### Evita los filtros de audiencia que asumen que el evento desencadenante se ha actualizado

Esta buena práctica es similar a evitar filtros redundantes con el evento desencadenar. Normalmente, fallará un filtro que asuma que el evento desencadenante se actualiza en el perfil de usuario.

#### Utilizar Liquid aborta (sólo atributos)

En las campañas y los pasos en Canvas, utiliza Liquid aborts para evitar utilizar filtros de audiencia que contengan los atributos desencadenantes en el horario de entrada. Por ejemplo, supongamos que tienes un atributo de matriz "colores favoritos" y quieres dirigirte a cualquier usuario que actualice la matriz de atributos con cualquier valor, y que también tenga el color "azul" en la matriz después de que se haya completado la actualización. Si utilizas los filtros de audiencia de este ejemplo, te encontrarás con una condición de carrera y te perderás a los usuarios que añadan "azul" en la matriz por primera vez.

En este caso, puedes implementar un desencadenante de retraso en una campaña o utilizar un paso de Retraso en Canvas para permitir que el perfil de usuario se actualice durante un periodo de tiempo y, a continuación, utilizar la siguiente lógica de cancelación de Liquid:

{% raw %}
```liquid
{%assign colors={{custom_attribute.$(Favorite Color)|split:”,”}}%}
{%unless colors contains ‘Blue’%}
{%abort_message(Blue not present)%}
{%endunless%}
```
{% endraw %}

#### Confirma cómo se gestionan los datos de usuario

Si hay una condición de carrera durante la evaluación de la entrada en el Canvas, los usuarios pueden entrar en un Canvas en el que no debían entrar. Por ejemplo, el perfil de usuario podría configurarse para ser incluido en la audiencia y posteriormente actualizarse después de que el Canvas haya puesto en cola a los usuarios para que dejen de ser elegibles en la audiencia. 

Recomendamos confirmar cómo se gestionan y actualizan los datos de usuario, concretamente cuándo y cómo se actualizan atributos específicos, como por SDK, API, API por lotes y otros métodos. Esto puede ayudar a identificar y aclarar por qué un usuario ha entrado en una campaña o Canvas frente a cuándo se actualizó el perfil de un usuario.
