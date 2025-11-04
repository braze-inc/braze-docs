---
nav_title: Mensajes dentro de la aplicación
article_title: Mensajes dentro de la aplicación en Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Este artículo de referencia describe características y matices específicos de los mensajes dentro de la aplicación que puedes añadir a tu Canvas para mostrar mensajería enriquecida."
tool: Canvas
channel: in-app messages

---

# Mensajes dentro de la aplicación en Canvas

> Puedes añadir mensajes dentro de la aplicación como parte de tu recorrido en Canvas para mostrar mensajes enriquecidos cuando tu cliente interactúe con tu aplicación.

## Cómo funciona

Antes de poder utilizar mensajes dentro de la aplicación en tu Canvas, asegúrate de tener configurado un [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) con opciones de retraso y audiencia.

En el constructor Canvas, añade un paso en [Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) y selecciona **Mensaje dentro de la aplicación** como tu **canal de mensajería**. Puedes personalizar [cuándo caducará tu mensaje](#in-app-message-expiration) y qué [comportamiento de avance](#advancement-behavior) tendrá.

## Añadir un mensaje dentro de la aplicación a tu viaje de usuario

Para añadir un mensaje dentro de la aplicación a tu Canvas, haz lo siguiente:

1. Añade un paso de [Mensajes]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) a tu recorrido de usuario.
2. Selecciona **Mensaje dentro de la aplicación** para tu **canal de mensajería**. 
3. Determina [cuándo caducará tu mensaje](#in-app-message-expiration) y qué [comportamiento de avance](#advancement-behavior-options) tendrá.

## Mensajes desencadenados dentro de la aplicación

Puedes seleccionar un desencadenante para que tus mensajes dentro de la aplicación se desencadenen al iniciar la sesión, o por eventos personalizados y compras.

Una vez transcurridos los retrasos y comprobadas las opciones de audiencia, los mensajes dentro de la aplicación se activan en vivo cuando un usuario llega al paso Mensaje. Si un usuario inicia una sesión y realiza el evento desencadenante del mensaje dentro de la aplicación, el usuario verá el mensaje dentro de la aplicación. 

Para los pasos en Canvas que tienen entrada desencadenada por acción, los usuarios pueden entrar en el Canvas a mitad de sesión. Los mensajes dentro de la aplicación no están configurados para estar en vivo hasta que se inicia una sesión, por lo que si un usuario está en medio de una sesión cuando llega al paso Mensaje, no recibirá el mensaje dentro de la aplicación hasta que inicie otra sesión y realice el desencadenamiento correspondiente.

## Caducidad de los mensajes dentro de la aplicación

Puedes elegir cuándo caducará el mensaje dentro de la aplicación. Durante este tiempo, el mensaje dentro de la aplicación esperará a ser visto hasta que haya alcanzado la fecha de caducidad. Después de enviar el mensaje dentro de la aplicación, puedes verlo una vez.

\![La sección Controles de mensajes de un paso Mensaje para un mensaje dentro de la aplicación. El mensaje dentro de la aplicación caducará tres días después de que el paso esté disponible.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Opción | Descripción | Ejemplo |
|---|---|---|
| **Existe una duración tras el paso** | Establece que el mensaje dentro de la aplicación caduque en relación al momento en que el paso esté disponible para el usuario. | Un mensaje dentro de la aplicación con una caducidad de dos días estaría disponible cuando el usuario entrara en el paso Mensaje y se marcaran las opciones de audiencia. Cualquier retraso antes de llegar a este paso provendría de pasos de Retraso anteriores en tu Canvas. El mensaje dentro de la aplicación estaría entonces disponible durante 2 días (48 horas) desde que el usuario entra en el paso, y durante esos dos días, los usuarios pueden ver el mensaje dentro de la aplicación si la abren. |
| **En una fecha y hora concretas** | Selecciona una fecha y hora concretas en las que el mensaje dentro de la aplicación dejará de estar disponible. | Si tienes una venta que finaliza el 30 de noviembre de 2024, selecciona esta opción para que los usuarios ya no vean el mensaje dentro de la aplicación asociado cuando finalice la venta. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

Braze recomienda que consideres el uso de esta característica en tus Lienzos promocionales y de incorporación.

{% tabs %}
  {% tab Promotional %}

Las promociones, los cupones y las rebajas suelen tener fechas de caducidad difíciles. El siguiente Canvas debe alertar a tus usuarios en los momentos más oportunos de que hay una promoción que pueden utilizar, y quizás influir en una compra. Esta promoción caduca el 28 de febrero de 2019 a las 11:15 h en la zona horaria de tu empresa.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Paso en Canvas</th>
    <th>Retraso</th>
    <th>Audiencia</th>
    <th>Canal</th>
    <th>Caducidad</th>
    <th>Avance</th>
    <th>Detalles</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Día 1: 50% de descuento</td>
    <td>Ninguno</td>
    <td>Todo desde la entrada</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Avanzar audiencia tras retraso</td>
    <td>Push inicial que avisa a tus usuarios de la promoción. El objetivo es atraer a los usuarios a tu aplicación para que aprovechen la promoción.</td>
  </tr>
  <tr>
    <td>En la aplicación: 50% de descuento</td>
    <td>Ninguno</td>
    <td>Todo desde la entrada</td>
    <td>Mensaje dentro de la aplicación</td>
    <td><b>Expira por:</b> 28/2/2019 11:15 Hora de la empresa</td>
    <td>Mensaje dentro de la aplicación visto</td>
    <td>Ahora el usuario ha abierto la aplicación y recibirá este mensaje, independientemente de que antes lo haya hecho por el mensaje push.</td>
  </tr>
  <tr>
    <td>50% de descuento en recordatorio</td>
    <td>1 día después de que el usuario reciba el paso anterior</td>
    <td>Todo desde la entrada <br><br><b>Filtrar:</b> Última compra realizada hace más de una semana</td>
    <td>Mensaje dentro de la aplicación</td>
    <td><b>Expira por:</b> 28/2/2019 11:15 Hora de la empresa</td>
    <td>Ninguno (último mensaje en Canvas)</td>
    <td>El usuario ha recibido el mensaje dentro de la aplicación en el paso anterior, pero no ha realizado ninguna compra a pesar de estar en la aplicación. <br><br>Este mensaje pretende atraer aún más al usuario para que realice una compra utilizando la promoción.</td>
  </tr>
</tbody>
</table>

Los mensajes dentro de la aplicación caducan cuando expira la promoción para evitar cualquier discrepancia entre la mensajería y la experiencia del cliente.

  {% endtab %}
  {% tab User Onboarding %}

Tu primera impresión con un usuario es, quizás, la más crítica. Puede hacer o deshacer futuras visitas a tu aplicación. Tus comunicaciones iniciales con el usuario deben programarse con sensatez y fomentar las visitas frecuentes a tu aplicación para promover su uso.

<table class="tg">
<thead>
  <tr>
    <th>Paso en Canvas</th>
    <th>Retraso</th>
    <th>Audiencia</th>
    <th>Canal</th>
    <th>Caducidad</th>
    <th>Avance</th>
    <th>Detalles</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Correo electrónico de bienvenida</td>
    <td>Ninguno</td>
    <td>Todo desde la entrada</td>
    <td>Correo electrónico</td>
    <td>N/A</td>
    <td>Avanzar audiencia tras retraso</td>
    <td>Correo electrónico inicial que da la bienvenida a tus usuarios a un proyecto, afiliación u otro programa de incorporación. <br><br>El objetivo es conducir a los usuarios a tu aplicación para iniciar su incorporación.</td>
  </tr>
  <tr>
    <td>Día 3-6 mensaje dentro de la aplicación</td>
    <td>3 días después de que el usuario reciba el paso anterior</td>
    <td>Todo desde la entrada</td>
    <td>Mensaje dentro de la aplicación</td>
    <td><b>Caduca:</b> 3 días después de que el paso esté disponible</td>
    <td>Mensaje dentro de la aplicación en vivo</td>
    <td>Si el usuario ha seguido el correo electrónico y ha sido conducido a la aplicación, recibirá el mensaje dentro de la aplicación deseado para continuar o recordarle su incorporación y cualquier requisito asociado a ella.</td>
  </tr>
  <tr>
    <td>Día 5 push </td>
    <td>2 días después de que el usuario reciba el paso anterior</td>
    <td>Todo desde la entrada</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Mensaje enviado</td>
    <td>Después de que los usuarios hayan recibido su mensaje dentro de la aplicación, recibirán un push de seguimiento para continuar su incorporación.</td>
  </tr>
</tbody>
</table>

Estos mensajes push se espacian alrededor de un mensaje dentro de la aplicación para asegurarse de que el usuario ha visitado la aplicación y ha comenzado su incorporación. Esto ayuda a evitar cualquier correo no deseado o mensajes fuera de lugar que podrían disuadir a los usuarios de visitar tu aplicación, y en su lugar crear un orden fluido y sensato en sus experiencias iniciales con tu aplicación.

  {% endtab %}
{% endtabs %}


## Priorizar los mensajes dentro de la aplicación

Un usuario puede desencadenar dos mensajes dentro de la aplicación en tu Canvas al mismo tiempo. Cuando esto ocurra, Braze seguirá el siguiente orden de prioridad para determinar qué mensaje dentro de la aplicación se muestra. 

Selecciona **Establecer prioridad exacta** y arrastra los diferentes pasos en Canvas para reordenar su prioridad en el Canvas. Por predeterminado, los pasos anteriores de una variante en Canvas se mostrarán antes que los pasos posteriores. Una vez que tus pasos estén en el orden de prioridad que prefieras, selecciona **Aplicar clasificación**.

\![El clasificador de prioridades con dos pasos "Bienvenida IAM" y "Seguimiento IAM".]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Hacer cambios en borradores de Lienzos activos

Si realizas cambios en la prioridad de los mensajes dentro de la aplicación en **Configuración de envío** de un borrador de un Canvas activo, estos cambios se aplican directamente al Canvas activo cuando se cierra el clasificador de prioridades. Sin embargo, en un paso de Mensaje, el clasificador de prioridades se actualizará cuando se lance el borrador, ya que la configuración del paso en Canvas se aplica a nivel de paso. 

## Comportamiento de avance

Los pasos de mensajería hacen avanzar automáticamente a todos los usuarios que entran en el paso. Ten en cuenta que no espera a que el mensaje dentro de la aplicación se desencadene o se muestre. No es necesario especificar el comportamiento de avance de los mensajes, lo que simplifica la configuración del paso general.

Cuando un usuario entra en un paso de mensajes dentro de la aplicación, avanza fuera de él inmediatamente en lugar de ser retenido durante la ventana de caducidad. En este caso, tener un paso de Retraso en el recorrido del usuario puede ser útil.

Para utilizar la opción **Avanzar cuando se envíe el mensaje**, añade una [ruta de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) independiente para filtrar a los usuarios que no hayan recibido el paso anterior.

{% details Original Canvas editor %}

Ya no puedes crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible como referencia para entender cómo funciona el comportamiento de avance para los pasos con mensajes dentro de la aplicación.

Los lienzos creados en el editor original necesitan especificar un comportamiento de avance: los criterios para avanzar a través de su componente Canvas. [Los pasos con sólo mensajes dentro de la aplicación](#steps-iam-only) tienen diferentes opciones de avance que [los pasos con múltiples tipos de mensajes](#steps-multiple-channels) (como push o correo electrónico). Para los mensajes dentro de la aplicación en el flujo de trabajo actual de Canvas, esta opción está configurada para que la audiencia siempre avance inmediatamente.

La entrega basada en acciones no está disponible para los pasos en Canvas con mensajes dentro de la aplicación. Los pasos en Canvas con mensajes dentro de la aplicación deben programarse. En cambio, los mensajes dentro de la aplicación Canvas aparecerán la primera vez que tu usuario abra la aplicación (desencadenados por la sesión de inicio) después de que se le haya enviado el mensaje programado en el componente Canvas.

Si tienes varios mensajes dentro de la aplicación en un Canvas, un usuario debe iniciar varias sesiones para recibir cada uno de esos mensajes individuales.

{% alert important %}
Cuando se selecciona **Avanzar cuando el mensaje dentro de la aplicación está en vivo**, el mensaje dentro de la aplicación estará disponible hasta que caduque, aunque el usuario haya pasado a los pasos siguientes. Si no quieres que el mensaje dentro de la aplicación esté en vivo cuando se entreguen los siguientes pasos en Canvas, asegúrate de que la caducidad es más corta que el retraso en los pasos siguientes.
{% endalert %}

#### Pasos con varios canales {#steps-multiple-channels}

Los pasos con un mensaje dentro de la aplicación y otro canal tienen las siguientes opciones de avance:

| Opción | Descripción |
|---|---|---|
| Avanzar cuando se envía un mensaje | Los usuarios deben recibir un correo electrónico, un webhook o una notificación push, o ver el mensaje dentro de la aplicación para avanzar a los siguientes pasos en el Canvas.  <br> <br>  Si el mensaje dentro de la aplicación caduca y el usuario no ha recibido el correo electrónico, webhook o push, o no ha visto el mensaje dentro de la aplicación, saldrá del Canvas y no avanzará a los pasos siguientes. |
| Avanzar audiencia inmediatamente | Todas las personas de la audiencia del paso avanzan a los siguientes pasos una vez transcurrido el retraso, hayan visto o no el mensaje anotado. <br> <br> Los usuarios deben coincidir con el segmento y los criterios de filtrado del paso para avanzar a los siguientes pasos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Cuando se selecciona **Toda la audiencia**, el mensaje dentro de la aplicación estará disponible hasta que caduque, aunque el usuario haya pasado a pasos posteriores. Si no quieres que el mensaje dentro de la aplicación esté en vivo cuando se entreguen los siguientes pasos en Canvas, comprueba que la caducidad es más corta que el retraso en los pasos siguientes.
{% endalert %}

{% enddetails %}

## Acciones desencadenantes

Puedes elegir entre las siguientes acciones desencadenantes para dirigirte a tus usuarios:

- **Haz la compra:** Dirigirse a usuarios que realizan cualquier compra o una compra específica
- **Comienza la sesión:** Dirígete a usuarios que inician una sesión en cualquier aplicación o en una aplicación concreta
- **Realiza un evento personalizado:** Dirígete a los usuarios que realizan el evento personalizado seleccionado (el evento personalizado debe enviarse utilizando el SDK).

Un usuario tiene que entrar en el paso en Canvas, iniciar una sesión y, a continuación, realizar el desencadenamiento para recibir un mensaje dentro de la aplicación. Esto significa que no se admiten actualizaciones a mitad de sesión. Por ejemplo, si el desencadenante es iniciar una sesión, el usuario sólo tiene que entrar en el paso en Canvas e iniciar una sesión para recibir el mensaje dentro de la aplicación. Si el desencadenante no es iniciar una sesión, el usuario tiene que entrar en el paso en Canvas, iniciar una sesión y, a continuación, realizar el desencadenante para recibir el mensaje dentro de la aplicación.

\!["Hacer una compra específica" seleccionada como acción desencadenante.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Las siguientes características de Canvas no están disponibles con los mensajes dentro de la aplicación, por lo que no se aplicarán a tus mensajes dentro de la aplicación aunque estén activadas.

- Intelligent Timing
- Límite de velocidad
- Limitación de frecuencia
- Criterios de salida
- Horas tranquilas

## Propiedades del evento personalizadas en un Canvas

Se admiten propiedades del evento personalizadas en mensajes dentro de la aplicación para Canvas. Sin embargo, estas propiedades son del evento personalizado o de la compra que desencadena el mensaje dentro de la aplicación, que se encuentra en el paso Mensaje, no en la ruta de acción anterior.

## Consideraciones

He aquí algunas consideraciones a tener en cuenta al enviar mensajes dentro de la aplicación en un Canvas.

- Si el usuario nunca reinicia la aplicación o nunca inicia una sesión, la aplicación no podrá averiguar si el usuario es elegible para el mensaje dentro de la aplicación, lo que significa que no se enviará un mensaje dentro de la aplicación.
- Cuando se produce el primer clic y hay una variable de contexto Canvas (propiedades de la entrada Canvas), y un usuario vuelve a entrar en un Canvas cinco veces, Braze tomará la quinta entrada y utilizará esa variable de contexto en el mensaje dentro de la aplicación.
- Un usuario sólo puede ser elegible para 10 mensajes dentro de la aplicación a la vez. Por ejemplo, si un usuario pasa por diferentes pasos en Canvas para 10 mensajes dentro de la aplicación, sólo puedes tener hasta 10 de estos pasos.
