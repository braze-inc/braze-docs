{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
La limitación de frecuencia no se aplica a las tarjetas de contenido.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
Una cadena de fecha como "12-1-2021" o "12/1/2021" se convertirá en un objeto datetime y se tratará como un [atributo de hora]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
Todos los datos de los perfiles de usuario (eventos personalizados, atributos personalizados, datos personalizados) se almacenan mientras esos perfiles estén activos.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze no genera perfiles para los usuarios hasta que han utilizado la aplicación por primera vez, por lo que no puedes dirigirte a usuarios que aún no han abierto tu aplicación.
{% endalert %}

{% endif %}
