---
nav_title: Exclusión voluntaria difusa
article_title: Exclusión aproximada
description: "Este artículo de referencia explica cómo configurar la exclusión difusa, una opción que intenta reconocer cuándo un mensaje entrante no coincide con una palabra clave de exclusión."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 1

---

# Exclusión voluntaria difusa

![Chat de mensajes iOS que muestra mensajes de exclusión salientes en respuesta a la exclusión difusa entrante "Please stopppp".]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Los usuarios que envíen SMS, MMS y RCS con Braze deben cumplir las leyes, reglamentos y normas industriales aplicables que se definan. En cuanto a la exclusión voluntaria, las leyes dictan que cuando un usuario envía un mensaje de texto con la palabra "STOP", todos los mensajes posteriores relacionados con ese programa de mensajería se detendrán. Braze procesa automáticamente estos mensajes y cancela la suscripción del usuario.<br><br>La exclusión difusa intenta reconocer cuándo un mensaje entrante no coincide con una [palabra clave de exclusión]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), pero indica una intención de exclusión. Si se habilita la exclusión voluntaria difusa y una respuesta de palabra clave entrante se considera "difusa", Braze responderá automáticamente con un mensaje de respuesta que indique a los usuarios que se excluyan.

Actualmente, sólo se admiten las palabras clave de exclusión creadas utilizando el inglés como [lengua local]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support).

## ¿Qué se considera aproximado?

Los criterios para que una respuesta entrante se considere "difusa" son los siguientes:
- Si al cambiar una letra con la letra uno a su izquierda o derecha en una palabra clave QWERTY se obtiene una palabra clave de exclusión coincidente.
- Una subcadena del mensaje coincide con una palabra clave de exclusión.

Por ejemplo, "Stpo" o "Please stopppp" se considerarán aproximados, y se enviará una respuesta de exclusión aproximada. Si el usuario responde con una palabra clave de adhesión voluntaria, se desencadenará un evento de cancelar suscripción.

## Configurar la exclusión difusa

Para configurar la exclusión difusa, vaya a la página de gestión de palabras clave del grupo de suscripción.

1. Ve a **Audiencia** > **Gestión de grupos de suscripción** y selecciona un grupo de suscripción **SMS/MMS/RCS**.
2. En **Palabras clave globales**, busca la categoría de **adhesión voluntaria** y selecciona el icono del lápiz.
3. Habilita **la exclusión voluntaria aproximada** alternándola.
4. Modifique la respuesta de exclusión difusa como desee. 

![Sección para editar las palabras clave de adhesión voluntaria.]({% image_buster /assets/img/sms/fuzzy2.png %})

## Buenas prácticas para mensajes difusos de exclusión voluntaria

Para garantizar una experiencia clara, conforme y positiva para tus suscriptores, es crucial configurar cuidadosamente tu mensaje de exclusión difusa. El objetivo principal del mensaje de exclusión difusa es **orientar a los usuarios que envían un mensaje similar, pero no exacto, a tu palabra clave de exclusión designada**. El mensaje indica a los usuarios cómo cancelar suscripción correctamente.

### Consideraciones críticas

{% alert warning %}
**NO** configures tu mensaje difuso de exclusión para confirmar una cancelación suscripción. Tu mensaje de baja difusa no debe contener lenguaje que implique que un usuario ya se ha dado de baja con éxito. Por ejemplo, **no** utilices "Se te ha dado de baja", "No recibirás más mensajes de este número" o "Ya te has dado de baja".
{% endalert %}

El mensaje de exclusión difusa se envía antes de que el usuario se haya dado de baja correctamente. Utilizar un lenguaje de confirmación engaña al suscriptor haciéndole creer que se ha dado de baja cuando en realidad no es así, lo que provoca la continuación de mensajes no deseados, la frustración del suscriptor e importantes riesgos de cumplimiento.

{% alert warning %}
**NO** configures tu mensaje de exclusión difusa para que sea idéntico o similar a tu palabra clave de exclusión exacta.
{% endalert %}

Si tu mensaje difuso es igual o demasiado parecido a tu palabra clave exacta de cancelación de suscripción (por ejemplo, si "STOP" es tu palabra clave exacta y tu mensaje difuso es "Envía STOP para cancelar suscripción"), puede crear confusión sobre si el mensaje inicial del usuario realmente dio lugar a una cancelación de suscripción o si necesita realizar otra acción. El mensaje difuso debe aclarar siempre qué acción debe realizar el usuario.

### Ejemplos de mensajes de exclusión difusa

Céntrate en guiar a los usuarios. Por ejemplo, si tu palabra clave de exclusión es "STOP", estos son ejemplos buenos y malos de mensajes de exclusión difusos que podrías crear:

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Buenos ejemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Malos ejemplos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Para cancelar suscripción a todos los mensajes, responde con la palabra BAJA".</td>
      <td>"Te has dado de baja correctamente. No recibirás más mensajes de este número. Responde START para volver a suscribirte" (Esto es una confirmación directa de cancelar suscripción, lo que es engañoso en un escenario de exclusión difusa).</td>
    </tr>
    <tr>
      <td>"Hemos recibido tu mensaje. Si quieres dejar de recibir mensajes de texto, envía el mensaje "STOP".</td>
      <td>"STOP" (Esto es sólo la palabra clave exacta en sí, que no guía al usuario).</td>
    </tr>
    <tr>
      <td>"¿Querías cancelar suscripción? Responde STOP para excluirte de todos los mensajes futuros".</td>
      <td>"Envía STOP para cancelar suscripción" (Si "STOP" es también tu palabra clave exacta, esto es redundante y no aclara la acción si el mensaje inicial era difuso).</td>
    </tr>
  </tbody>
</table>
