# Dominios personalizados

> Esta página explica cómo utilizar dominios personalizados para mostrar una imagen de marca coherente. 

{% alert note %}
Póngase en contacto con su gestor de cuenta Braze si está interesado en empezar a utilizar dominios personalizados.
{% endalert %}

## Requisitos de dominio

- Los dominios deben ser adquiridos, poseídos y gestionados por usted.
- El dominio utilizado para esta función debe ser único (es decir, diferente del dominio de su sitio web), y el dominio no puede utilizarse para alojar ningún contenido web.
  - También puedes utilizar subdominios únicos, como `sms.braze.com` o `whatsapp.braze.com`.

### Delegación del dominio personalizado

Cuando delegas tu dominio en Braze, nos encargamos automáticamente de la renovación del certificado para evitar una interrupción del servicio. 

Para delegar tu dominio en Braze, haz lo siguiente: 

1. Presente a su gestor de éxito de clientes un dominio que cumpla los requisitos anteriores. A continuación, Braze comprobará la configuración DNS existente para el dominio y confirmará que:

- No existen registros de CAA O
- **Existen** registros de CAA, pero tienen un registro para {% raw %}`<any number> issue "letsencrypt.org"`{% endraw %} o {% raw %}`<anynumber> issuewild "letsencrypt.org"`{% endraw %}

{:start="2"}
2\. Cree cuatro nuevos registros A, uno para cada IP, y confirme que son los únicos registros A que existen para el host de enlace de dominio:
- `151.101.130.133`
- `151.101.194.133`
- `151.101.2.133`
- `151.101.66.133`

## Uso de dominios personalizados

Una vez configurados, los dominios personalizados pueden asignarse a uno o varios grupos de suscripción a WhatsApp y SMS. 

![La configuración de los grupos de suscripción permite seleccionar un dominio de acortamiento de enlaces.][7]

{% if include.channel == 'WhatsApp' %}
Las campañas enviadas con el seguimiento de clics activado o creadas dentro de las plantillas de mensajes de WhatsApp utilizarán el dominio asignado asociado a tus grupos de suscripción.

![Vista previa del creador de mensajes de WhatsApp con un dominio de enlace acortado que es diferente del dominio del cuadro "Mensaje".][6]
{% endif %}

{% if include.channel == 'SMS' %}
Las campañas enviadas con el acortamiento de enlaces activado utilizarán el dominio asignado asociado a tu grupo de suscripción SMS.

![Vista previa del creador de mensajes SMS con un dominio de enlace acortado que es diferente del dominio del cuadro "Mensaje".][8]
{% endif %}

## Preguntas más frecuentes

### ¿Pueden compartirse los dominios delegados entre varios grupos de suscripción?

Sí. Un único dominio puede utilizarse con varios grupos de suscripción. Para ello, seleccione el dominio de cada grupo de suscripción al que debe asociarse.

### ¿Pueden compartirse los dominios delegados en varios espacios de trabajo?

Sí. Los dominios pueden asociarse a grupos de suscripción en varios espacios de trabajo, suponiendo que los espacios de trabajo estén dentro de la misma empresa.

[6]: {% image_buster /assets/img/custom_domain_whatsapp_composer.png %}
[7]: {% image_buster /assets/img/custom_domain.png %}
[8]: {% image_buster /assets/img/custom_domain2.png %}