Embora usuários anônimos não tenham `external_ids`, você pode atribuir a eles um [alias de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases) em vez disso. Você deve atribuir um alias de usuário quando quiser adicionar outros identificadores ao usuário, mas não souber qual é o `external_id` deles (por exemplo, eles não estão logados). Com aliases de usuário, você também pode:

- Usar a API Braze para registrar eventos e atributos associados a usuários anônimos
- Usar o filtro de segmentação [ID de Usuário Externo está em branco]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#external-user-id) para direcionar usuários anônimos em seu envio de mensagens

{% if include.section == "user_guide" %}
{% alert tip %}
Para um guia completo, veja [SDK Braze: Definindo um alias de usuário]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).
{% endalert %}
{% endif %}