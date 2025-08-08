Obwohl anonyme Nutzer:innen nicht über `external_ids` verfügen, können Sie ihnen stattdessen einen [Nutzer-Alias]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#user-aliases) zuweisen. Sie sollten einen Nutzer-Alias zuweisen, wenn Sie dem Nutzer:in andere Bezeichner hinzufügen möchten, aber nicht wissen, wie sein `external_id` lautet (z.B. weil er nicht angemeldet ist). Mit User-Aliasing können Sie auch Nutzer:in:

- Verwenden Sie die Braze API, um Ereignisse und Attribute zu protokollieren, die anonymen Nutzer:innen zugeordnet sind.
- Verwenden Sie den Segmentierungsfilter [Externe ID ist leer]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#external-user-id), um anonyme Nutzer:innen in Ihrem Messaging zu targetieren.

{% if include.section == "user_guide" %}
{% alert tip %}
Eine vollständige Anleitung finden Sie unter [Braze SDK: Einstellen eines Nutzer:in-Alias]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/#setting-a-user-id).
{% endalert %}
{% endif %}