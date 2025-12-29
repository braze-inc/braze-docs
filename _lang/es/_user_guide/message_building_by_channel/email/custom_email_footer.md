---
nav_title: Pie de página de correo electrónico personalizado
article_title: Pie de página de correo electrónico personalizado
page_order: 6.5
description: "Este artículo describe cómo configurar un pie de página de correo electrónico personalizado para todo el espacio de trabajo."
channel:
  - email

---

# Pie de página de correo electrónico personalizado

> Puedes establecer un pie de página de correo electrónico personalizado para todo el espacio de trabajo, que puedes plantillas en cada correo electrónico utilizando el atributo {% raw %}`{{${email_footer}}}`{% endraw %} Liquid.

Al utilizar pies de página de correo electrónico personalizados, ya no tendrás que crear un pie de página nuevo para cada plantilla o campaña de correo electrónico que utilices. Los cambios que hagas en tu pie de página personalizado se reflejarán en todas las campañas de correo electrónico nuevas y existentes. Recuerda que el cumplimiento de la [Ley CAN-SPAM de 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) exige que incluyas una dirección física de tu empresa y un enlace para cancelar suscripción en tus correos electrónicos.

{% alert warning %}
Es tu responsabilidad asegurarte de que tu pie de página personalizado cumple los requisitos mencionados.
{% endalert %}

## Crear tu pie de página personalizado

Para crear o editar tu pie de página personalizado, haz lo siguiente:

1. Ve a **Configuración** > **Preferencias de correo electrónico**.
2. Ve a la sección **Pie de página personalizado** y activa los pies de página personalizados.
3. Edita tu pie de página en la sección **Redactar**.
4. Envía un mensaje de prueba. 

Un ejemplo de pie de página personalizado.]({% image_buster /assets/img_archive/custom_footer.png %})

El pie de página predeterminado utiliza el atributo {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} y nuestra dirección postal física. Si utilizas este predeterminado, asegúrate de seleccionar **<other>** para el **Protocolo**.

{% alert important %}
Para cumplir la normativa CAN-SPAM, tu pie de página personalizado debe incluir {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}. No podrás guardar un pie de página personalizado sin este atributo.
{% endalert %}

\![Valores de protocolo y URL necesarios para el pie de página personalizado.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Pies de página sin enlaces para cancelar suscripción

Ten mucho cuidado cuando utilices una plantilla con el pie de página personalizado {% raw %}`{{${email_footer}}}` pero sin la etiqueta de enlace de cancelar suscripción `{{${set_user_to_unsubscribed_url}}}`{% endraw %}. Aparecerá una advertencia, pero será tu decisión enviar un correo electrónico con o sin enlace para cancelar suscripción.

Aquí tienes una advertencia en el compositor de correo electrónico:

\![Ejemplo de correo electrónico redactado sin pie de página.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

Aquí tienes una advertencia en el compositor de la campaña:

Composición de la campaña sin pies.]({% image_buster /assets/img_archive/no_footer_test.png %})

### Añadir un enlace personalizado para cancelar suscripción

Para añadir un enlace de cancelar suscripción personalizado, puedes cambiar el enlace de cancelar suscripción del pie de página personalizado de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} a un enlace a tu propio sitio web con un parámetro de consulta que incluya el ID de usuario. Un ejemplo es:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

A continuación, llama al [punto final`/email/status` ]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) para actualizar el estado de suscripción del usuario. Para más detalles, consulta nuestra documentación sobre cómo [cambiar el estado de la suscripción por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

A continuación, guarda este nuevo enlace. La etiqueta predeterminada de Braze para cancelar suscripción {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} debe estar en el pie de página. Esto significa que tienes que incluir el enlace predeterminado "ocultándolo" colocando la etiqueta en un comentario o en una etiqueta oculta de `<div>`.

## Buenas prácticas

Sugerimos las siguientes prácticas recomendadas al crear y utilizar pies de página personalizados.

### Personalización con atributos

Al crear un pie de página personalizado, Braze sugiere utilizar [atributos para la personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). Tienes a tu disposición el conjunto completo de atributos predeterminados y personalizados, pero aquí tienes algunos que pueden resultarte útiles:

| Atributo | Etiqueta |
| --------- | --- |
| Dirección de correo electrónico del usuario | {% raw %}`{{${email_address}}}`{% endraw %} |
| URL personalizada del usuario para cancelar suscripción | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>Esta etiqueta sustituye a la anterior {% raw %}`{{${unsubscribe_url}}}`{% endraw %}. Te recomendamos que utilices en su lugar la nueva etiqueta {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}. |
| URL de adhesión voluntaria personalizada del usuario | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| URL personalizada de suscriptor del usuario | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| URL personalizada del usuario del Centro de Preferencias de Braze | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Incluyendo un enlace para cancelar suscripción y un enlace de adhesión voluntaria

{% raw  %}
Como práctica recomendada, Braze recomienda incluir tanto un enlace para cancelar suscripción (como ``{{${set_user_to_unsubscribed_url}}}``) como un enlace de adhesión voluntaria (como ``{{${set_user_to_opted_in_url}}}``) en tu pie de página personalizado. De este modo, los usuarios podrán tanto cancelar suscripción como adhesión voluntaria, y podrás recopilar pasivamente los datos de adhesión de una parte de tus usuarios.
{% endraw %}

### Configuración de pies de página personalizados para correos electrónicos en texto plano

También puedes elegir establecer un pie de página personalizado para los correos electrónicos de texto sin formato en la pestaña **Páginas de suscripción y pies de página** de la página **Preferencias de correo electrónico**, que sigue las mismas reglas que el pie de página personalizado para los correos electrónicos HTML. 

Si no incluyes un pie de página en texto plano, Braze creará uno automáticamente a partir del pie de página HTML. Cuando tus pies de página personalizados estén a tu gusto, selecciona **Guardar**.

\![Correo electrónico con la opción Establecer pie de página de texto sin formato personalizado seleccionada.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

