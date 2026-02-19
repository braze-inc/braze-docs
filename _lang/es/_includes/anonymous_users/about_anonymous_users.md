Después de [integrar el SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/), los usuarios que inicien tu aplicación por primera vez se considerarán "anónimos" hasta que llames al método `changeUser` y les asignes un `external_id`. Una vez asignados, no puedes volver a hacerlos anónimos. Sin embargo, si desinstalan y vuelven a instalar tu aplicación, volverán a ser anónimos hasta que se llame a `changeUser`.

Si un usuario previamente identificado inicia una sesión en un nuevo dispositivo, toda su actividad anónima se sincronizará automáticamente con su perfil existente después de que llames a `changeUser` en ese dispositivo utilizando su `external_id`. Esto incluye cualquier atributo, evento o historial recopilado durante la sesión en el nuevo dispositivo.

{% if include.section == "user_guide" %}
{% alert tip %}
Para una guía completa, consulta [Configurar ID de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/).
{% endalert %}
{% endif %}