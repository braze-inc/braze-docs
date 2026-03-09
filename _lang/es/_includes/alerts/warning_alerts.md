{% if include.alert == 'User profile external_id' %}

{% alert warning %}
No asignes un `external_id` a un perfil de usuario antes de poder identificarlo de forma única. Después de identificar a un usuario, no puedes revertirlo a anónimo.
<br><br>
Se`external_id`puede actualizar utilizando el[`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)[punto final]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/). Sin embargo, cualquier intento de establecer un valor diferente`external_id`  durante la sesión de un usuario creará un nuevo perfil de usuario con el nuevo`external_id`  asociado a él. No se transmitirá ningún dato entre los dos perfiles.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
Si tiene intención de crear más de uno de los mismos conectores Currents (por ejemplo, dos conectores de eventos de compromiso de mensajes), deben estar en espacios de trabajo diferentes. Dado que la integración Braze Segment Currents no puede aislar los eventos de diferentes aplicaciones en un único espacio de trabajo, si no se hace esto, se producirá una desduplicación de datos innecesaria y se perderán datos.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
Evite configurar una campaña basada en acciones o Canvas con el mismo desencadenante que el filtro de audiencia (como un atributo modificado o la realización de un evento personalizado). Puede producirse una [condición de]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) [carrera]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) en la que el usuario no se encuentre en la audiencia en el momento en que realice el evento desencadenante, lo que significa que no recibirá la campaña ni entrará en Canvas.
{% endalert %}

{% endif %}
