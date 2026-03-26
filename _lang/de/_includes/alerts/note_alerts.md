{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
Frequency-Capping gilt nicht für Content-Cards.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
Ein Datums-String wie "12-1-2021" oder "12/1/2021" wird in ein Datetime-Objekt umgewandelt und als [Zeitattribut]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) behandelt.
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
Alle Nutzerprofildaten (angepasste Events, Angepasste Attribute, angepasste Daten) werden gespeichert, solange diese Profile aktiv sind.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze erstellt erst dann Profile für Nutzer:innen, wenn diese die App zum ersten Mal verwendet haben. Sie können also keine Nutzer:innen ansprechen, die Ihre App noch nicht geöffnet haben.
{% endalert %}

{% endif %}

{% if include.alert == 'Shopify attributes REST API' %}

{% alert note %}
Alle Attribute stammen aus der Braze REST API.
{% endalert %}

{% endif %}