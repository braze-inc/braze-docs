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

Después de que pasen los retrasos y se comprueben las opciones de audiencia, el mensaje dentro de la aplicación se establecerá en vivo, y los usuarios lo verán si abren la aplicación. Los mensajes dentro de la aplicación en Canvas sólo pueden ser desencadenados por el evento desencadenado `start session`; no pueden ser desencadenados por eventos personalizados en un componente Canvas.

En el caso de los pasos del lienzo con entrada activada por acción, los usuarios pueden entrar en el lienzo en mitad de la sesión. Sin embargo, como se ha indicado anteriormente, los mensajes in-app no se activarán hasta que comience la siguiente sesión, por lo que estos usuarios se perderían el mensaje in-app inicial, ya que no podían entrar en el Canvas antes de que comenzara la sesión.

## Añadir un mensaje dentro de la aplicación a tu viaje de usuario

Para añadir un mensaje dentro de la aplicación a tu Canvas, haz lo siguiente:

1. Añade un paso de [Mensajes]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) a tu recorrido de usuario.
2. Selecciona **Mensaje dentro de la aplicación** para tu **canal de mensajería**. 
3. Determina [cuándo caducará tu mensaje](#in-app-message-expiration) y qué [comportamiento de avance](#advancement-behavior-options) tendrá.

### Caducidad de los mensajes en la aplicación

En el editor de mensajes dentro de la aplicación, puedes elegir cuándo caducará el mensaje dentro de la aplicación. Durante este tiempo, el mensaje dentro de la aplicación se "sentará" y esperará a ser visto hasta que haya alcanzado la fecha de caducidad. Después de enviar el mensaje dentro de la aplicación, puedes verlo una vez.

![][1]

| Opción | Descripción | Ejemplo |
|---|---|---|
| El mensaje expira después del periodo especificado | La primera opción le permite caducar el mensaje in-app en relación con el momento en que el paso esté disponible para el usuario. | Por ejemplo, un mensaje in-app con una caducidad de dos días estaría disponible después de que transcurra el retraso del paso y se comprueben las opciones de audiencia. Entonces estaría disponible durante 2 días (48 horas) y, durante esos dos días, los usuarios podrían ver el mensaje in-app si abren la aplicación. |
| El mensaje caduca en la fecha especificada | La segunda opción te permite elegir una fecha y hora concretas en las que el mensaje in-app dejará de estar disponible. | Por ejemplo, si tiene una oferta que finalizó en una fecha y hora específicas, puede seleccionar esta opción para que los usuarios ya no vean el mensaje asociado en la aplicación cuando finalice la oferta. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Ejemplos

Puedes utilizar mensajes dentro de la aplicación en tus Lienzos promocionales y de incorporación.

{% tabs %}
  {% tab Promocional %}

Las promociones, los cupones y las rebajas suelen tener fechas de caducidad estrictas. El siguiente lienzo debería alertar a sus usuarios en los momentos más oportunos de que hay una promoción que pueden utilizar, y tal vez influir en una compra. Esta promoción caduca el 28 de febrero de 2019 a las 11:15 h en la zona horaria de la empresa.

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

Como puede ver, los mensajes in-app caducan cuando expira la promoción para evitar cualquier discrepancia entre la mensajería y la experiencia del cliente.

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

Como puede ver, los mensajes push se espacian alrededor de un mensaje in-app para asegurarse de que el usuario ha visitado la aplicación y ha comenzado su onboarding. Esto evitará el molesto spam o los mensajes fuera de orden que podrían disuadir a los usuarios de visitar tu aplicación, y en su lugar creará un orden fluido y sensato en sus experiencias iniciales con tu aplicación.

  {% endtab %}
{% endtabs %}

### Opciones de comportamiento de avance

En Canvas, los pasos en Mensajería hacen avanzar automáticamente a todos los usuarios que entran en el paso. Para utilizar la opción **Avanzar cuando se envíe el mensaje**, añade una [Ruta de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) independiente para filtrar a los usuarios que no hayan recibido el paso anterior.

{% details Comportamiento original del editor de Canvas %}

{% alert important %}
Ya no puedes crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible como referencia para entender cómo funciona el comportamiento de avance para los pasos con mensajes in-app.
{% endalert %}

Los lienzos creados en el editor original necesitan especificar un comportamiento de avance-el criterio para avanzar a través de su componente Lienzo. [Los pasos con sólo mensajes dentro de aplicación](#steps-iam-only) tienen diferentes opciones de avance que [los pasos con múltiples tipos de mensajes](#steps-multiple-channels) (push, email, etc.). Para los mensajes in-app en un flujo de trabajo de Canvas Flow, esta opción está configurada para que el público avance siempre inmediatamente.

La entrega basada en acciones no está disponible para los pasos de Canvas con mensajes in-app. Los pasos del lienzo con mensajes in-app deben programarse. En su lugar, los mensajes Canvas in-app aparecerán la primera vez que el usuario abra la aplicación (activados por la sesión de inicio) después de que se le haya enviado el mensaje programado en el componente Canvas.

Si tienes varios mensajes in-app dentro de un Canvas, un usuario debe iniciar varias sesiones para recibir cada uno de esos mensajes individuales.

{% alert important %}
Los mensajes dentro de la aplicación no pueden ser activados por eventos en Canvas.
{% endalert %}

![][2]

{% alert important %}
Si se selecciona **Avanzar cuando el mensaje dentro de la aplicación está activo**, el mensaje dentro de la aplicación estará disponible hasta que caduque, aunque el usuario haya pasado a los pasos siguientes. Si no desea que el mensaje in-app esté activo cuando se entreguen los siguientes pasos del Canvas, asegúrese de que la caducidad es más corta que el retraso en los pasos posteriores.
{% endalert %}

#### Pasos con varios canales {#steps-multiple-channels}

Los pasos con un mensaje in-app y otro canal tienen las siguientes opciones de avance:

| Opción | Descripción |
|---|---|---|
| Avanzar cuando el mensaje se haya enviado | Los usuarios deben recibir un correo electrónico, un webhook o una notificación push, o ver el mensaje en la aplicación para avanzar a los pasos siguientes en Canvas.  <br> <br>  Si el mensaje in-app caduca y el usuario no ha recibido el correo electrónico, webhook o push, o no ha visto el mensaje in-app, saldrá del Canvas y no avanzará a los pasos siguientes. |
| Avanzar audiencia inmediatamente | Todos los destinatarios del paso avanzan a los pasos siguientes una vez transcurrido el retardo, hayan visto o no el mensaje señalado.  <br> <br> Los usuarios deben cumplir los criterios de segmento y filtro del paso para avanzar a los siguientes pasos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]

{% alert important %}
Cuando se selecciona **Todo el público**, el mensaje in-app estará disponible hasta que caduque, aunque el usuario haya pasado a los pasos siguientes. Si no quieres que el mensaje in-app esté activo cuando se entreguen los siguientes pasos del Canvas, comprueba que la caducidad es más corta que el retraso en los pasos posteriores.
{% endalert %}

{% enddetails %}

## Priorizar los mensajes in-app

Un cliente puede activar dos mensajes in-app dentro de tu Canvas al mismo tiempo. Cuando esto ocurra, Braze seguirá el siguiente orden de prioridad para determinar qué mensaje in-app se muestra. Arrastre diferentes pasos del lienzo para reordenar su prioridad. De manera predeterminada, los pasos anteriores en una variante en Canvas aparecerán antes que los pasos posteriores.

![]({% image_buster /assets/img_archive/step_priority.png %}){: style="max-width:80%"}

Ve a la **Configuración de envío** de la sección Canvas para priorizar los mensajes dentro de la aplicación de un Canvas frente a los mensajes dentro de la aplicación de otros Canvas y campañas.

![]({% image_buster /assets/img_archive/canvas_send_settings.png %})

Por defecto, la prioridad de los componentes del lienzo es media, y los pasos creados más recientemente tienen la prioridad relativa más alta. Las prioridades a nivel de lienzo y campaña también son medias por defecto, con la prioridad relativa más alta por defecto para los elementos creados más recientemente.

![]({% image_buster /assets/img_archive/canvas_priority.png %}){: style="max-width:85%"}

### Borradores de un lienzo activo

Al editar un borrador de un Lienzo activo, los cambios en la prioridad de los mensajes dentro de la aplicación en la **Configuración de envío** no se guardan con el borrador. Estos cambios se aplican directamente al Canvas activo cuando se cierra el modal del clasificador de prioridades. Sin embargo, en un paso de Mensaje, el clasificador de prioridades se actualizará cuando un usuario lance el borrador, ya que la configuración de pasos se aplica a nivel de paso.

## Propiedades de eventos personalizados en un Canvas

La entrega basada en acciones no está disponible para los pasos en Canvas con mensajes dentro de la aplicación. Esto significa que tampoco puedes utilizar propiedades del evento personalizadas para estos pasos. 

Para crear plantillas de propiedades del evento en Canvas, te recomendamos almacenar las propiedades del evento como atributos personalizados en tu primer paso en Canvas y personalizar tu mensaje dentro de la aplicación con los atributos personalizados en el segundo paso.


[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live"
[2]: {% image_buster /assets/img/iam-advancement-behavior.png %} "IAM Live"
[3]: {% image_buster /assets/img/push-advancement-behavior.png %} "IAM Live"
