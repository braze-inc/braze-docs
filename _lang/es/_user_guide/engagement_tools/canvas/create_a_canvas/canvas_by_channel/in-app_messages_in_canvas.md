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

 

## Añadir un mensaje dentro de la aplicación a tu viaje de usuario

Para añadir un mensaje dentro de la aplicación a tu Canvas, haz lo siguiente:

1. Añade un paso de [Mensajes]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) a tu recorrido de usuario.
2. Selecciona **Mensaje dentro de la aplicación** para tu **canal de mensajería**. 
3. Determina [cuándo caducará tu mensaje](#in-app-message-expiration) y qué [comportamiento de avance](#advancement-behavior-options) tendrá.

## 



  

En el caso de los pasos del lienzo con entrada activada por acción, los usuarios pueden entrar en el lienzo en mitad de la sesión. 

## Caducidad de los mensajes en la aplicación

  Después de enviar el mensaje dentro de la aplicación, puedes verlo una vez.



| Opción | Descripción | Ejemplo |
|---|---|---|
|  |  |  Entonces estaría disponible durante 2 días (48 horas) y, durante esos dos días, los usuarios podrían ver el mensaje in-app si abren la aplicación. |
|  |  |  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Ejemplos



{% tabs %}
  {% tab Promocional %}

Las promociones, los cupones y las rebajas suelen tener fechas de caducidad estrictas. El siguiente lienzo debería alertar a sus usuarios en los momentos más oportunos de que hay una promoción que pueden utilizar, y tal vez influir en una compra. 

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

 

  {% endtab %}
{% endtabs %}


## Priorizar los mensajes in-app

 Cuando esto ocurra, Braze seguirá el siguiente orden de prioridad para determinar qué mensaje in-app se muestra. 

 De manera predeterminada, los pasos anteriores en una variante en Canvas aparecerán antes que los pasos posteriores. 



### 

  

## 

  

 





Ya no puedes crear o duplicar Lienzos utilizando el editor original. Esta sección está disponible como referencia para entender cómo funciona el comportamiento de avance para los pasos con mensajes in-app.

Los lienzos creados en el editor original necesitan especificar un comportamiento de avance-el criterio para avanzar a través de su componente Lienzo.  Para los mensajes in-app en un flujo de trabajo de Canvas Flow, esta opción está configurada para que el público avance siempre inmediatamente.

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

## 



-  
-  
-  

   





- 
- 
- 
- 
- 

## Propiedades de eventos personalizados en un Canvas

 

## 



- 
- 
-  
