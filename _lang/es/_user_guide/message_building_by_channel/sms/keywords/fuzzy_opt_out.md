---
nav_title: Exclusión aproximada
article_title: Exclusión aproximada
description: "Este artículo de referencia explica cómo configurar la exclusión difusa, una opción que intenta reconocer cuándo un mensaje entrante no coincide con una palabra clave de exclusión."
page_type: reference
channel:
  - SMS
page_order: 1

---

# Exclusión voluntaria difusa

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

> Los usuarios que envíen SMS con Braze deben cumplir las leyes, reglamentos y normas industriales aplicables que se definan. En cuanto a la exclusión voluntaria, las leyes dictan que cuando un usuario envía un mensaje de texto con la palabra "STOP", todos los mensajes posteriores relacionados con ese programa de mensajería se detendrán. Braze procesa automáticamente estos mensajes y cancela la suscripción del usuario.<br><br>La exclusión difusa intenta reconocer cuándo un mensaje entrante no coincide con una [palabra clave de exclusión]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/), pero indica una intención de exclusión. Si la exclusión difusa está activada y una respuesta de palabra clave entrante se considera "difusa", Braze responderá automáticamente pidiendo al usuario que confirme su intención. 

Actualmente, sólo se admiten las palabras clave de exclusión creadas utilizando el inglés como [lengua local]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support).

## ¿Qué se considera aproximado?

Los criterios para que una respuesta entrante se considere "difusa" son los siguientes:
- Si al cambiar una letra con la letra uno a su izquierda o derecha en una palabra clave QWERTY se obtiene una palabra clave de exclusión coincidente.
- Una subcadena del mensaje coincide con una palabra clave de exclusión.

Por ejemplo, "Stpo" o "Please stopppp" se considerarán aproximados, y se enviará una respuesta de exclusión aproximada.

## Configurar la exclusión difusa

Para configurar la exclusión difusa, vaya a la página de gestión de palabras clave del grupo de suscripción.

1. Vaya a **Audiencia** > **Suscripciones** y seleccione un grupo de suscripción SMS.

{:start="2"}
2\. En **Palabras clave globales de SMS**, busque la categoría de **exclusión** y seleccione el icono del lápiz.
3\. Habilita **la exclusión voluntaria aproximada** alternándola.
4\. Modifique la respuesta de exclusión difusa como desee. 

![][2]{: style="max-width:70%;"}

[1]: {% image_buster /assets/img/sms/fuzzy1.jpg %}
[2]: {% image_buster /assets/img/sms/fuzzy2.png %}

