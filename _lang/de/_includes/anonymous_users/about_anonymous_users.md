Nachdem Sie [das Braze SDK integriert haben]({{site.baseurl}}/developer_guide/sdk_integration/), werden Nutzer:innen, die Ihre App zum ersten Mal starten, als "anonym" betrachtet, bis Sie die Methode `changeUser` aufrufen und ihnen eine `external_id` zuweisen. Einmal zugewiesen, können Sie sie nicht wieder anonymisieren. Wenn sie jedoch Ihre App deinstallieren und neu installieren, werden sie wieder anonym, bis `changeUser` aufgerufen wird.

Wenn ein zuvor identifizierter Nutzer eine Sitzung auf einem neuen Gerät beginnt, werden alle seine anonymen Aktivitäten automatisch mit seinem bestehenden Profil synchronisiert, nachdem Sie `changeUser` auf diesem Gerät über seinen `external_id` aufgerufen haben. Dazu gehören alle Attribute, Ereignisse oder Verläufe, die während der Sitzung auf dem neuen Gerät gesammelt wurden.

{% if include.section == "user_guide" %}
{% alert tip %}
Eine vollständige Anleitung finden Sie unter [Einrichten von Nutzer:innen IDs]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/).
{% endalert %}
{% endif %}