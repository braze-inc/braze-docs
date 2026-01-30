Aunque los usuarios anónimos no tienen `external_ids`, puedes asignarles un [alias de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases). Debes asignar un alias de usuario cuando quieras añadir otros identificadores al usuario pero no sepas cuál es su `external_id` (por ejemplo, no ha iniciado sesión). Con los alias de usuario, también puedes:

- Utiliza la API Braze para registrar eventos y atributos asociados a usuarios anónimos
- Utiliza el filtro de segmentación [ID externo del usuario está en blanco]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#external-user-id) para dirigirte a usuarios anónimos en tu mensajería

{% if include.section == "user_guide" %}
{% alert tip %}
Para una guía completa, consulta [SDK de Braze: Configuración de un alias de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).
{% endalert %}
{% endif %}