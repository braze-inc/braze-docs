{% if include.alert == 'User profile external_id' %}

{% alert warning %}
Weisen Sie Benutzerprofilen erst dann eine `external_id` zu, wenn Sie sie eindeutig identifizieren können. Wenn Sie einen Benutzer identifiziert haben, können Sie ihn nicht mehr in die Anonymität zurückversetzen.
<br><br>
Ein `external_id` kann über den [Endpunkt`/users/external_ids/rename` ]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) aktualisiert werden. Wenn Sie jedoch versuchen, während der Sitzung eines Nutzers:in ein anderes `external_id` einzustellen, wird ein neues Nutzerprofil erstellt, das mit dem neuen `external_id` verknüpft ist. Es werden keine Daten zwischen den beiden Profilen ausgetauscht.
{% endalert %}

{% endif %}

{% if include.alert == 'Segment Currents multiple connectors' %}

{% alert warning %}
Wenn Sie mehr als einen der gleichen Currents Konnektoren erstellen möchten (z.B. zwei Konnektoren für das Engagement von Nachrichten), müssen sich diese in verschiedenen Workspaces befinden. Da die Braze Segment Currents-Integration Ereignisse von verschiedenen Apps nicht in einem einzigen Workspace isolieren kann, führt dies zu unnötiger Daten-Deduplizierung und Datenverlust.
{% endalert %}

{% endif %}

{% if include.alert == 'Canvas race condition audience trigger' %}

{% alert warning %}
Vermeiden Sie es, eine aktionsbasierte Kampagne oder ein Canvas mit demselben Auslöser wie den Zielgruppenfilter zu konfigurieren (z. B. ein geändertes Attribut oder die Durchführung eines benutzerdefinierten Ereignisses). Es kann eine [Race-Condition]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions) auftreten, bei der der Nutzer:in zu dem Zeitpunkt, an dem er das Trigger-Ereignis ausführt, nicht in der Zielgruppe ist. Das bedeutet, dass er die Kampagne nicht erhält oder den Canvas nicht betreten kann.
{% endalert %}

{% endif %}
