{% if include.alert == 'Content Cards frequency capping' %}

{% alert note %}
Die Frequenzbegrenzung gilt nicht für Inhaltskarten.
{% endalert %}

{% endif %}

{% if include.alert == 'Custom Attributes time attribute' %}

{% alert note %}
Ein Datums-String wie "12-1-2021" oder "12/1/2021" wird in ein Datetime-Objekt umgewandelt und als [Attribut für die Zeit]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) behandelt.
{% endalert %}

{% endif %}

{% if include.alert == 'Manage custom data storage' %}

{% alert note %}
Alle Nutzerprofildaten (angepasste Events, angepasste Attribute, angepasste Daten) werden gespeichert, solange diese Profile aktiv sind.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment profiles first app use' %}

{% alert note %}
Braze erstellt erst dann Profile für Benutzer, wenn diese die App zum ersten Mal verwendet haben. Sie können also keine Benutzer ansprechen, die Ihre App noch nicht geöffnet haben.
{% endalert %}

{% endif %}
