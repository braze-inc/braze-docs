{% if include.section == "UTM parameters" %}

Aunque el acortamiento de enlaces te permite hacer un seguimiento automático de tus URL, también puedes añadir parámetros UTM a tus URL para hacer un seguimiento del rendimiento de las campañas en herramientas de análisis de terceros, como Google Analytics.

Para añadir parámetros UTM a tu URL, haz lo siguiente:

1. Empieza con tu URL base. Esta es la URL de la página de la que quieres hacer un seguimiento (como `https://www.example.com`).
2. Añade un signo de interrogación (?) después de tu URL base.
3. Añade cada parámetro UTM separado por un ampersand (&).

Un ejemplo es `https://www.example.com?utm_source=newsletter&utm_medium=sms`.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Preguntas más frecuentes

### ¿Los enlaces que recibo al realizar el envío de prueba son URL reales?

Si la campaña se ha guardado como borrador antes del envío de prueba, sí. De lo contrario, se trata de un enlace de marcador de posición. Ten en cuenta que la URL exacta enviada en una campaña lanzada puede diferir de la enviada en un envío de prueba.

### ¿Puedo añadir parámetros UTM a una URL antes de acortarla?

Sí. Se pueden añadir parámetros estáticos y dinámicos. 

### ¿Durante cuánto tiempo son válidas las URL acortadas?

Las URL personalizadas son válidas durante dos meses desde el momento del registro de la URL.

### ¿Es necesario instalar el SDK de Braze para acortar enlaces?

No. El acortamiento de enlaces funciona sin ninguna integración SDK.

{% endif %}

{% if include.section == "Custom Domains" %}

## Dominios personalizados

El acortamiento de enlaces también le permite utilizar su propio dominio para personalizar el aspecto de sus URL acortadas, lo que contribuye a mostrar una imagen de marca coherente. Para más información, consulta [Dominios personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/).

{% endif %}