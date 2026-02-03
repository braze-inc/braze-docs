Bien que les utilisateurs anonymes n'aient pas de `external_ids`, vous pouvez leur attribuer un [alias d'utilisateur.]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases)  Vous devez attribuer un alias utilisateur lorsque vous souhaitez ajouter d'autres identifiants à l'utilisateur mais que vous ne connaissez pas son `external_id` (par exemple, il n'est pas connecté). Avec les aliasing de l'utilisateur, vous pouvez également :

- Utilisez l'API de Braze pour journaliser les événements et les attributs associés aux utilisateurs anonymes.
- Utilisez le filtre de segmentation [ID externe est vide]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#external-user-id) pour cibler les utilisateurs anonymes dans votre envoi de messages.

{% if include.section == "user_guide" %}
{% alert tip %}
Pour une présentation complète, consultez [Braze SDK : Définition d'un alias d'utilisateur]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).
{% endalert %}
{% endif %}