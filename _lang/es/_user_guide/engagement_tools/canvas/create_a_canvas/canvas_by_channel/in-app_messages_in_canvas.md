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

# Mensajes in-app en Canvas

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

En el caso de los pasos del lienzo con entrada activada por acción, los usuarios pueden entrar en el lienzo en mitad de la sesión. Los mensajes dentro de la aplicación no están configurados para estar en vivo hasta que se inicia una sesión, por lo que si un usuario está en mitad de la sesión cuando llega al paso Mensaje, no recibirá el mensaje dentro de la aplicación hasta que inicie otra sesión y realice el desencadenamiento correspondiente.

## Caducidad de los mensajes en la aplicación

Puedes elegir cuándo caducará el mensaje dentro de la aplicación. Durante este tiempo, el mensaje dentro de la aplicación esperará a ser visto hasta que haya alcanzado la fecha de caducidad. Después de enviar el mensaje dentro de la aplicación, puedes verlo una vez.

![La sección Controles de mensaje de un paso Mensaje para un mensaje dentro de la aplicación. El mensaje dentro de la aplicación caducará tres días después de que el paso esté disponible.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Opción | Descripción | Ejemplo |
|---|---|---|
| **Existe una duración tras el paso** | Establece que el mensaje dentro de la aplicación caduque en relación al momento en que el paso esté disponible para el usuario. | Un mensaje dentro de la aplicación con una caducidad de dos días estaría disponible después de que transcurriera el retraso del paso y se comprobaran las opciones de audiencia. Entonces estaría disponible durante 2 días (48 horas) y, durante esos dos días, los usuarios podrían ver el mensaje in-app si abren la aplicación. |
| **En una fecha y hora concretas** | Selecciona una fecha y hora concretas en las que el mensaje dentro de la aplicación dejará de estar disponible. | Si tienes una venta que finaliza el 30 de noviembre de 2024, selecciona esta opción para que los usuarios ya no vean el mensaje dentro de la aplicación asociado cuando finalice la venta. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Ejemplos

Braze recomienda que consideres el uso de esta característica en tus Lienzos promocionales y de incorporación.

{% tabs %}
  {% tab Promocional %}

Las promociones, los cupones y las rebajas suelen tener fechas de caducidad estrictas. El siguiente lienzo debería alertar a sus usuarios en los momentos más oportunos de que hay una promoción que pueden utilizar, y tal vez influir en una compra. Esta promoción caduca el 28 de febrero de 2019 a las 11:15 h en la zona horaria de tu empresa.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Paso en Canvas</th>
    <th>Demora</th>
    <th>Audiencia</th>
    <th>Canal</th>
    <th>Caducidad</th>
    <th>Avance</th>
    <th>Detalles</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Primer día: 50 % de descuento</td>
    <td>Ninguno</td>
    <td>Todos de entrada</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Avanzar audiencia después de la demora</td>
    <td>Push inicial que avisa a tus usuarios de la promoción. El objetivo es atraer a los usuarios a su aplicación para que aprovechen la promoción.</td>
  </tr>
  <tr>
    <td>In-app: 50 % de descuento</td>
    <td>Ninguno</td>
    <td>Todos de entrada</td>
    <td>Mensaje dentro de la aplicación</td>
    <td><b>Caduca el:</b> 28/2/2019, 11:15 h, horario de la empresa</td>
    <td>Mensajes In-App vistos</td>
    <td>El usuario ya ha abierto la aplicación y recibirá este mensaje, independientemente de que lo haya hecho antes por el mensaje push.</td>
  </tr>
  <tr>
    <td>recordatorio del 50 % de descuento</td>
    <td>1 día después de que el usuario reciba el paso anterior</td>
    <td>Todos de entrada <br><br><b>Filtro:</b> Última compra realizada hace más de una semana</td>
    <td>Mensaje dentro de la aplicación</td>
    <td><b>Caduca el:</b> 28/2/2019, 11:15 h, horario de la empresa</td>
    <td>Ninguno (último mensaje en Canvas)</td>
    <td>El usuario ha recibido el mensaje in-app en el paso anterior pero no ha realizado ninguna compra a pesar de estar en la app. <br><br>Este mensaje pretende atraer aún más al usuario para que realice una compra utilizando la promoción.</td>
  </tr>
</tbody>
</table>

Los mensajes dentro de la aplicación caducan cuando expira la promoción para evitar cualquier discrepancia entre la mensajería y la experiencia del cliente.

  {% endtab %}
  {% tab Incorporación de usuarios %}

Su primera impresión con un usuario es, quizás, la más crítica. Puede hacer o deshacer futuras visitas a su aplicación. Las comunicaciones iniciales con el usuario deben tener una duración razonable y fomentar las visitas frecuentes a la aplicación para promover su uso.

<table class="tg">
<thead>
  <tr>
    <th>Paso en Canvas</th>
    <th>Demora</th>
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
    <td>Todos de entrada</td>
    <td>Correo electrónico</td>
    <td>N/A</td>
    <td>Audiencia anticipada tras el retraso</td>
    <td>Correo electrónico inicial que da la bienvenida a sus usuarios a un proyecto, afiliación u otro programa de incorporación. <br><br>El objetivo es dirigir a los usuarios a su aplicación para que comiencen su integración.</td>
  </tr>
  <tr>
    <td>Mensaje dentro de la aplicación día 3-6</td>
    <td>3 días después de que el usuario reciba el paso anterior</td>
    <td>Todos de entrada</td>
    <td>Mensaje dentro de la aplicación</td>
    <td><b>Caduca:</b> 3 días después de que el paso esté disponible</td>
    <td>Mensaje In-App Live</td>
    <td>Si el usuario ha seguido el mensaje de correo electrónico y ha accedido a la aplicación, recibirá el mensaje dentro de la aplicación que desee para continuar o recordarle su incorporación y los requisitos asociados a ella.</td>
  </tr>
  <tr>
    <td>Push día 5 </td>
    <td>2 días después de que el usuario reciba el paso anterior</td>
    <td>Todos de entrada</td>
    <td>Push</td>
    <td>N/A</td>
    <td>Mensaje enviado</td>
    <td>Una vez que los usuarios hayan recibido su mensaje en la aplicación, recibirán un push de seguimiento para continuar con su incorporación.</td>
  </tr>
</tbody>
</table>

Estos mensajes push se espacian alrededor de un mensaje dentro de la aplicación para asegurarse de que el usuario ha visitado la aplicación y ha comenzado su incorporación. Esto ayuda a evitar cualquier correo no deseado o mensajes fuera de lugar que podrían disuadir a los usuarios de visitar tu aplicación, y en su lugar crear un orden fluido y sensato en sus experiencias iniciales con tu aplicación.

  {% endtab %}
{% endtabs %}


## Priorizar los mensajes in-app

Un usuario puede desencadenar dos mensajes dentro de la aplicación en tu Canvas al mismo tiempo. Cuando esto ocurra, Braze seguirá el siguiente orden de prioridad para determinar qué mensaje in-app se muestra. 

Selecciona **Establecer prioridad exacta** y arrastra los diferentes pasos en Canvas para reordenar su prioridad en el Canvas. De manera predeterminada, los pasos anteriores en una variante en Canvas aparecerán antes que los pasos posteriores. Una vez que tus pasos estén en el orden de prioridad que prefieras, selecciona **Aplicar clasificación**.

![El clasificador de prioridades con dos pasos "Bienvenida IAM" y "Seguimiento IAM".]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Hacer cambios en borradores de Lienzos activos

Si realizas cambios en la prioridad de los mensajes dentro de la aplicación en **Configuración de envío** de un borrador de un Canvas activo, estos cambios se aplican directamente al Canvas activo cuando se cierra el clasificador de prioridades. Sin embargo, en un paso de Mensaje, el clasificador de prioridades se actualizará cuando se lance el borrador, ya que la configuración del paso en Canvas se aplica a nivel de paso. 

## Comportamiento de avance

Los pasos de mensajería hacen avanzar automáticamente a todos los usuarios que entran en el paso. Ten en cuenta que no espera a que el mensaje dentro de la aplicación se desencadene o se muestre. No es necesario especificar el comportamiento de avance de los mensajes, lo que simplifica la configuración del paso general.

Cuando un usuario entra en un paso de mensajes dentro de la aplicación, avanza fuera de él inmediatamente en lugar de ser retenido durante la ventana de caducidad. En este caso, tener un paso de Retraso en el recorrido del usuario puede ser útil.

Para utilizar la opción **Avanzar cuando se envíe el mensaje**, añade una [ruta de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) independiente para filtrar a los usuarios que no hayan recibido el paso anterior.

{% details Editor de lienzos original %}

Ya no puedes crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible como referencia para entender cómo funciona el comportamiento de avance para los pasos con mensajes in-app.

Los lienzos creados en el editor original necesitan especificar un comportamiento de avance-el criterio para avanzar a través de su componente Lienzo. [Los pasos con sólo mensajes dentro de la aplicación](#steps-iam-only) tienen diferentes opciones de avance que [los pasos con múltiples tipos de mensajes](#steps-multiple-channels) (como push o correo electrónico). Para los mensajes in-app en un flujo de trabajo de Canvas Flow, esta opción está configurada para que el público avance siempre inmediatamente.

La entrega basada en acciones no está disponible para los pasos de Canvas con mensajes in-app. Los pasos del lienzo con mensajes in-app deben programarse. En su lugar, los mensajes Canvas in-app aparecerán la primera vez que el usuario abra la aplicación (activados por la sesión de inicio) después de que se le haya enviado el mensaje programado en el componente Canvas.

Si tienes varios mensajes in-app dentro de un Canvas, un usuario debe iniciar varias sesiones para recibir cada uno de esos mensajes individuales.

{% alert important %}
Si se selecciona **Avanzar cuando el mensaje dentro de la aplicación está activo**, el mensaje dentro de la aplicación estará disponible hasta que caduque, aunque el usuario haya pasado a los pasos siguientes. Si no desea que el mensaje in-app esté activo cuando se entreguen los siguientes pasos del Canvas, asegúrese de que la caducidad es más corta que el retraso en los pasos posteriores.
{% endalert %}

#### Pasos con varios canales {#steps-multiple-channels}

Los pasos con un mensaje in-app y otro canal tienen las siguientes opciones de avance:

| Opción | Descripción |
|---|---|---|
| Avanzar cuando el mensaje se haya enviado | Los usuarios deben recibir un correo electrónico, un webhook o una notificación push, o ver el mensaje en la aplicación para avanzar a los pasos siguientes en Canvas.  <br> <br>  Si el mensaje in-app caduca y el usuario no ha recibido el correo electrónico, webhook o push, o no ha visto el mensaje in-app, saldrá del Canvas y no avanzará a los pasos siguientes. |
| Avanzar audiencia inmediatamente | Todos los destinatarios del paso avanzan a los pasos siguientes una vez transcurrido el retardo, hayan visto o no el mensaje señalado. <br> <br> Los usuarios deben cumplir los criterios de segmento y filtro del paso para avanzar a los siguientes pasos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Cuando se selecciona **Todo el público**, el mensaje in-app estará disponible hasta que caduque, aunque el usuario haya pasado a los pasos siguientes. Si no quieres que el mensaje in-app esté activo cuando se entreguen los siguientes pasos del Canvas, comprueba que la caducidad es más corta que el retraso en los pasos posteriores.
{% endalert %}

{% enddetails %}

## Acciones desencadenantes

Puedes elegir entre las siguientes acciones desencadenantes para dirigirte a tus usuarios:

- **Haz la compra:** Dirigirse a usuarios que realizan cualquier compra o una compra específica
- **Comienza la sesión:** Dirígete a usuarios que inician una sesión en cualquier aplicación o en una aplicación concreta
- **Realizar un evento personalizado:** Usuarios objetivo que realizan el evento personalizado seleccionado

Un usuario tiene que entrar en el paso en Canvas, iniciar una sesión y, a continuación, realizar el desencadenamiento para recibir un mensaje dentro de la aplicación. Esto significa que no se admiten actualizaciones a mitad de sesión. Por ejemplo, si el desencadenante es iniciar una sesión, el usuario sólo tiene que entrar en el paso en Canvas e iniciar una sesión para recibir el mensaje dentro de la aplicación. Si el desencadenante no es iniciar una sesión, el usuario tiene que entrar en el paso en Canvas, iniciar una sesión y, a continuación, realizar el desencadenante para recibir el mensaje dentro de la aplicación.

!["Hacer una compra específica" seleccionada como acción desencadenante.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Las siguientes características de Canvas no están disponibles con los mensajes dentro de la aplicación, por lo que no se aplicarán a tus mensajes dentro de la aplicación aunque estén activadas.

- Intelligent Timing
- Limitación de velocidad
- Limitación de frecuencia
- Criterios de salida
- Horas tranquilas

## Propiedades de eventos personalizados en un Canvas

Se admiten propiedades del evento personalizadas en mensajes dentro de la aplicación para Canvas. Sin embargo, estas propiedades son del evento personalizado o de la compra que desencadena el mensaje dentro de la aplicación, que se encuentra en el paso Mensaje, no en la ruta de acción anterior.

## Consideraciones

He aquí algunas consideraciones a tener en cuenta al enviar mensajes dentro de la aplicación en un Canvas.

- Si el usuario nunca reinicia la aplicación o nunca inicia una sesión, la aplicación no podrá averiguar si el usuario es elegible para el mensaje dentro de la aplicación, lo que significa que no se enviará un mensaje dentro de la aplicación.
- Cuando se produce el primer clic y hay una variable de contexto Canvas (propiedades de la entrada Canvas), y un usuario vuelve a entrar en un Canvas cinco veces, Braze tomará la quinta entrada y utilizará esa variable de contexto en el mensaje dentro de la aplicación.
- Un usuario sólo puede ser elegible para 10 mensajes dentro de la aplicación a la vez. Por ejemplo, si un usuario pasa por diferentes pasos en Canvas para 10 mensajes dentro de la aplicación, sólo puedes tener hasta 10 de estos pasos.
