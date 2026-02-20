{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
La limite de fréquence ne s'applique pas aux cartes de contenu.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
Une chaîne de caractères de date telle que "12-1-2021" ou "12/1/2021" sera convertie en objet datetime et traitée comme un [attribut time]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time).
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
Toutes les données des profils utilisateurs (événements personnalisés, attributs personnalisés, données personnalisées) sont stockées tant que ces profils sont actifs.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze ne crée pas de profils pour les utilisateurs tant qu’ils n’ont pas utilisé l’application une première fois, ce qui signifie que vous ne pouvez pas cibler des utilisateurs qui n’ont pas encore ouvert votre application.
{% endalert %}

{% endif %}
