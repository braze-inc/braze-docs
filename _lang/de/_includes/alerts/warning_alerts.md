{% if include.alert == 'User profile external_id' %}

{% alert warning %}
Weisen Sie Benutzerprofilen erst dann eine `external_id` zu, wenn Sie sie eindeutig identifizieren können. Wenn Sie einen Benutzer identifiziert haben, können Sie ihn nicht mehr in die Anonymität zurückversetzen.
<br><br>
Ein Update für`external_id`  kann über den[`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)[Endpunkt]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) durchgeführt werden. Jeder Versuch, während einer Sitzung eines`external_id` Nutzers einen anderen Wert festzulegen, führt jedoch zur Erstellung eines neuen Nutzerprofils mit dem neuen`external_id`zugehörigen Wert. Es werden keine Daten zwischen den beiden Profilen ausgetauscht.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
Wenn Sie mehr als einen der gleichen Currents Konnektoren erstellen möchten (z.B. zwei Konnektoren für das Engagement von Nachrichten), müssen sich diese in verschiedenen Workspaces befinden. Da die Braze Segment Currents-Integration Ereignisse von verschiedenen Apps nicht in einem einzigen Workspace isolieren kann, führt dies zu unnötiger Daten-Deduplizierung und Datenverlust.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
Vermeiden Sie es, eine aktionsbasierte Kampagne oder ein Canvas mit demselben Auslöser wie den Zielgruppenfilter zu konfigurieren (z. B. ein geändertes Attribut oder die Durchführung eines benutzerdefinierten Ereignisses). Es kann zu einer[ Race-Condition]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) kommen, bei der der Nutzer:in zum Zeitpunkt der Auslösung des Trigger-Ereignisses nicht zur Zielgruppe gehört, was bedeutet, dass er die Kampagne nicht erhält oder nicht in den Canvas gelangt.
{% endalert %}

{% endif %}
