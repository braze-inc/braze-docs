---
nav_title: "API-Übersicht"
article_title: API-Übersicht
page_order: 2.1
description: "Dieser referenzierte Artikel behandelt die API-Grundlagen, einschließlich dessen, was eine REST API ist, die Terminologie und eine Übersicht über API-Schlüssel."
page_type: reference
alias: /api/api_key/
---

# API Übersicht

> Dieser referenzierte Artikel behandelt die API-Grundlagen, einschließlich gängiger Terminologie und einer Übersicht über REST API-Schlüssel, Berechtigungen und deren Sicherheit.

## Braze REST API Sammlung

| Kollektion                                                                 | Zweck                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Kataloge]({{site.baseurl}}/api/endpoints/catalogs/)                       | Erstellen und verwalten Sie Kataloge und Katalogartikel, die Sie in Ihren Kampagnen referenzieren können.    |
| [Cloud-Datenaufnahme]({{site.baseurl}}/api/endpoints/cdi/)                | Verwalten Sie Ihre Data Warehouse Integrationen und Synchronisationen.                                    |
| [E-Mail-Listen und Adressen]({{site.baseurl}}/api/endpoints/email/)         | Richten Sie die bidirektionale Synchronisierung zwischen Braze und Ihren E-Mail-Systemen ein und verwalten Sie sie.           |
| [Exportieren]({{site.baseurl}}/api/endpoints/export/)                           | Greifen Sie auf verschiedene Details Ihrer Kampagnen, Canvase, KPIs und mehr zu und exportieren Sie sie.        |
| [Nachrichten]({{site.baseurl}}/api/endpoints/messaging/)                      | Planen, versenden und verwalten Sie Ihre Kampagnen und Canvase.                               |
| [Präferenzzentrum]({{site.baseurl}}/api/endpoints/preference_center/)     | Bauen Sie Ihr Einstellungscenter auf und aktualisieren Sie das Styling.                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | Verwalten Sie Nutzer:innen in cloudbasierten Anwendungen und Diensten.                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | Verwalten Sie die Rufnummern Ihrer Nutzer:innen in Ihren Abo-Gruppen.                         |
| [Abo-Gruppen]({{site.baseurl}}/api/endpoints/subscription_groups/) | Auflistung und Update der im Braze-Dashboard gespeicherten Abo-Gruppen (SMS und E-Mail). |
| [Templates]({{site.baseurl}}/api/endpoints/templates/)                     | Erstellen und aktualisieren Sie Templates für E-Mail Messaging und Content-Blöcke.                   |
| [Nutzerdaten]({{site.baseurl}}/api/endpoints/user_data/)                     | Identifizieren, tracken und verwalten Sie Ihre Nutzer:innen.                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## API-Definitionen

Im Folgenden finden Sie eine Übersicht der Begriffe, die in der Dokumentation der Braze REST API vorkommen können.

### Endpunkte

Braze verwaltet eine Reihe von verschiedenen Instanzen für unser Dashboard und die REST-Endpunkte. Wenn Ihr Konto eingerichtet ist, melden Sie sich unter einer der folgenden URLs an. Verwenden Sie den richtigen REST-Endpunkt, je nachdem, für welche Instanz Sie bereitgestellt werden. Wenn Sie sich nicht sicher sind, öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/) oder verwenden Sie die folgende Tabelle, um die URL des Dashboards, das Sie verwenden, dem richtigen REST-Endpunkt zuzuordnen.

{% alert important %}
Wenn Sie Endpunkte für API-Aufrufe verwenden, benutzen Sie den REST Endpunkt.

Verwenden Sie für die SDK-Integration den [SDK-Endpunkt]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), nicht den REST-Endpunkt.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='instances' %}

### API-Grenzen

Für die meisten APIs hat Braze ein Standard Rate-Limit von 250.000 Anfragen pro Stunde. Für bestimmte Arten von Anfragen gelten jedoch eigene Rate-Limits, um große Datenmengen unserer Kund:innen besser verarbeiten zu können. Einzelheiten finden Sie unter [API Rate-Limits]({{site.baseurl}}/api/api_limits/)

### Benutzer-IDs

- **Externe Nutzer:innen ID**: Die `external_id` dient als eindeutiger Bezeichner des Nutzers:in, für den Sie Daten übermitteln. Dieser Bezeichner sollte mit dem übereinstimmen, den Sie im Braze SDK festgelegt haben, um zu vermeiden, dass mehrere Profile für denselben Nutzer:in erstellt werden.
- **Braze ID**: `braze_id` dient als eindeutiger Bezeichner für Nutzer:innen, der von Braze festgelegt wird. Dieser Bezeichner kann zusätzlich zu external_ids verwendet werden, um Nutzer:innen über die REST API zu löschen.

Weitere Informationen finden Sie in den folgenden Artikeln zu Ihrer Plattform: [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/), [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) und [Internet]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/).

## Über REST API-Schlüssel

Ein REST-API-Schlüssel (Application Programming Interface, API) ist ein eindeutiger Code, der an eine API übergeben wird, um den API-Aufruf zu authentifizieren und die aufrufende Anwendung oder den Nutzer zu identifizieren. Der API-Zugriff erfolgt über HTTPS-Webanfragen an den REST API Endpunkt Ihres Unternehmens. Wir verwenden bei Braze REST API-Schlüssel in Verbindung mit unseren App-Identifikator-Schlüsseln, um Daten zu verfolgen, abzurufen, zu senden, zu exportieren und zu analysieren, um sicherzustellen, dass sowohl auf Ihrer als auch auf unserer Seite alles reibungslos läuft.

Workspaces und API-Schlüssel gehen bei Braze Hand in Hand. Workspaces sind so konzipiert, dass sie Versionen derselben Anwendung für mehrere Plattformen enthalten. Viele Kund:innen nutzen Workspaces auch, um kostenlose und Premium-Versionen ihrer Anwendungen auf derselben Plattform unterzubringen. Wie Sie vielleicht bemerken, nutzen auch diese Workspaces die REST API und haben ihre eigenen REST-API-Schlüssel. Diese Schlüssel können individuell angepasst werden, um den Zugriff auf bestimmte Endpunkte der API zu ermöglichen. Jeder Aufruf der API muss einen Schlüssel mit Zugriff auf den Endpunkt enthalten.

Wir referenzieren sowohl den REST-API-Schlüssel als auch den Workspace-API-Schlüssel als `api_key`. Die `api_key` ist in jeder Anfrage als Anfrage-Header enthalten und dient als Authentifizierungsschlüssel, der Ihnen die Nutzung unserer REST APIs erlaubt. Diese REST APIs dienen dem Tracking von Nutzer:innen, dem Versand von Nachrichten, dem Export von Nutzerdaten und vielem mehr. Wenn Sie einen neuen REST API-Schlüssel erstellen, müssen Sie ihm Zugriff auf bestimmte Endpunkte geben. Indem Sie einem API-Schlüssel bestimmte Berechtigungen zuweisen, können Sie genau festlegen, welche Aufrufe ein API-Schlüssel authentifizieren kann.

![REST API-Schlüssel Panel auf dem Tab API-Schlüssel.]({% image_buster /assets/img_archive/rest-api-key.png %})

{% alert tip %}
Neben den REST-API-Schlüsseln gibt es auch eine Art von Bezeichner-Schlüsseln, die dazu dienen, bestimmte Dinge wie Apps, Templates, Canvase, Kampagnen, Content Cards und Segmente aus der API zu referenzieren. Weitere Informationen finden Sie unter [API-Kennungstypen]({{site.baseurl}}/api/identifier_types/).
{% endalert %}

### REST API-Schlüssel erstellen

So erstellen Sie einen neuen REST-API-Schlüssel:

1. Gehen Sie zu **Einstellungen** > **APIs und Bezeichner**.
2. Wählen Sie **API-Schlüssel erstellen**.
3. Geben Sie Ihrem neuen Schlüssel einen Namen, um ihn auf einen Blick identifizieren zu können.
4. Geben Sie [die zulässigen IP-Adressen](#api-ip-allowlisting) und Subnetze für den neuen Schlüssel an.
5. Wählen Sie aus, welche [Berechtigungen](#rest-api-key-permissions) mit Ihrem neuen Schlüssel verknüpft werden sollen.

{% alert important %}
Beachten Sie, dass Sie nach der Erstellung eines neuen API-Schlüssels den Umfang der Berechtigungen oder die zugelassenen IPs nicht mehr bearbeiten können. Diese Einschränkung erfolgt aus Sicherheitsgründen. Wenn Sie den Geltungsbereich eines Schlüssels ändern müssen, erstellen Sie einen neuen Schlüssel mit den aktualisierten Berechtigungen und implementieren diesen Schlüssel anstelle des alten. Nachdem Sie Ihre Implementierung abgeschlossen haben, können Sie den alten Schlüssel löschen.
{% endalert %}

### Berechtigungen für REST API-Schlüssel

API-Schlüssel-Berechtigungen sind Berechtigungen, die Sie einem Nutzer:innen oder einer Gruppe zuweisen können, um deren Zugriff auf bestimmte API-Aufrufe zu beschränken. Um Ihre Liste der API-Schlüssel-Berechtigungen anzuzeigen, gehen Sie zu **Einstellungen** > **APIs und Bezeichner** und wählen Sie Ihren API-Schlüssel aus.

{% tabs %}
{% tab Nutzer:innen-Daten %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | Aufzeichnen von Nutzerattributen, angepassten Events und Käufen. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | Löschen beliebiger Nutzer:innen. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |Erstellen eines neuen Alias für bestehende Nutzer:innen. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |Identifizieren Sie einen Nutzer:in mit einer externen ID, der nur einen Alias hat. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |Abfragen von Nutzerprofil-Informationen nach Nutzer-ID. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |Abfrage von Informationen zum Nutzerprofil nach Segmenten. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | Verschmilzt zwei bestehende Nutzer:innen miteinander. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | Ändern der externen ID von bestehenden Nutzer:innen. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | Entfernen der externen ID von bestehenden Nutzer:innen. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | Aktualisieren eines Alias für bestehende Nutzer:innen. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | Abrufen der Nutzerprofil-Informationen in der globalen Kontrollgruppe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

 {% endtab %}
 {% tab E-Mail %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | Abfragen von E-Mail-Adressen, für die kein Abo besteht.  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | Ändern des E-Mail-Adress-Status. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | Abfragen von E-Mail-Rückläufern (Hard Bounce). |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | Löschen von E-Mail-Adressen aus Ihrer Rückläuferliste (Hard Bounce). |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | Löschen von E-Mail-Adressen aus Ihrer Spam-Liste. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | Blockliste E-Mail-Adressen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Messaging %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | Senden Sie eine sofortige Nachricht an bestimmte Nutzer:innen. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | Planen einer Nachricht, die zu einem bestimmten Zeitpunkt gesendet werden soll. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | Aktualisieren einer geplanten Nachricht. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | Löschen einer geplanten Nachricht. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | Abfragen aller geplanten Broadcast-Nachrichten. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | Aktualisieren Sie eine iOS Live-Aktivität. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Kampagnen %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | Triggern Sie den Versand einer bestehenden Kampagne. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | Planen Sie einen zukünftigen Versand einer Kampagne mit API-getriggerter Zustellung. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | Aktualisieren Sie eine Kampagne, die mit einer API-getriggerten Zustellung geplant ist. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |Löschen Sie eine Kampagne, die mit einer API-getriggerten Zustellung geplant ist. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | Abfrage nach einer Liste von Kampagnen. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Abfrage von Analytics für Kampagnen über einen bestimmten Zeitraum. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | Abfrage von Details zu einer bestimmten Kampagne. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | Abfragen von Analytics zum Nachrichtenversand über einen bestimmten Zeitraum. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | Erstellen Sie eine Sende-ID für das Tracking von Nachrichten-Blasts. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | Abfragen der URL zu einer bestimmten Nachrichtenvariante in einer Kampagne. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | Erlaubt das Versenden von transaktionalen Nachrichten über den Endpunkt für transaktionale Nachrichten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Canvas %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | Trigger zum Senden eines vorhandenen Canvas. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | Planen des zukünftigen Versands eines Canvas mit API-getriggerter Zustellung. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | Aktualisieren eines Canvas, für das eine API-getriggerte Zustellung festgelegt wurde. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| Löschen eines Canvas, für das eine API-getriggerte Zustellung festgelegt wurde. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |  Abfragen einer Liste der Canvase. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Abfragen von Canvas-Analytics über einen bestimmten Zeitraum. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | Abfragen von Details zu einem bestimmten Canvas. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Abfragen von aggregierten Canvas-Analytics über einen bestimmten Zeitraum. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | Abfragen der URL zu einer bestimmten Nachrichtenvariante in einem Canvas-Schritt. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Segmente %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | Abfrage nach einer Liste von Segmenten. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Abfrage für Segment Analytics über einen Zeitbereich. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | Abfrage nach Details zu einem bestimmten Segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Käufe %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | Abfragen einer Liste von Produkten, die in Ihrer App gekauft wurden. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | Abfragen des Gesamtbetrags, der über einen bestimmten Zeitraum pro Tag in Ihrer App ausgegeben wurde. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | Suchen Sie nach der Gesamtzahl der Käufe pro Tag in Ihrer App über einen bestimmten Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Ereignisse %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | Abfrage nach einer Liste angepasster Events. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | Abfrage von Vorkommen eines angepassten Events über einen Zeitbereich. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Sitzungen %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | Abfragen der Sitzungen pro Tag über einen bestimmten Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab KPIs %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |  Abfragen von eindeutigen aktiven Nutzer:innen pro Tag über einen bestimmten Zeitraum. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Abfragen der Gesamtzahl eindeutiger aktiver Nutzer:innen über ein fortlaufendes Zeitfenster von 30 Tagen in einem bestimmten Zeitbereich. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | Abfragen von neuen Nutzer:innen pro Tag über einen bestimmten Zeitraum. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | Abfragen von App-Deinstallationen pro Tag über einen bestimmten Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Templates %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | Erstellen Sie auf dem Dashboard ein neues Template für E-Mails. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Abfragen von Informationen zu einem bestimmten Template. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Abfragen einer Liste der E-Mail-Templates. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | Aktualisieren Sie ein im Dashboard gespeichertes Template für E-Mails. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SSO %}

| Erlaubnis | Beschreibung |
|---|---|---|
| `sso.saml.login` | Richten Sie die vom Identitätsanbieter veranlasste Anmeldung ein. Weitere Informationen finden Sie unter [Anmeldung durch den Service Provider (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Content-Blöcke %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | Abfragen von Informationen zu einem bestimmten Template. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | Abfragen einer Liste der Content-Blöcke. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | Erstellen Sie einen neuen Content-Block auf dem Dashboard. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | Aktualisieren Sie einen bestehenden Content-Block auf dem Dashboard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Präferenz-Center %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Abrufen eines Präferenzzentrums. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | Auflisten von Präferenzzentren. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | Erstellen oder aktualisieren Sie ein Präferenzzentrum. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Abrufen eines Links zu einem Präferenzzentrum für eine:n Nutzer:in. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Abo %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | Abo-Gruppenstatus festlegen. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | Abrufen des Abo-Gruppenstatus. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | Abrufen des Status von Abo-Gruppen, die bestimmte Nutzer:in explizit abonniert und abgemeldet haben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SMS %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | Abfragen von ungültigen Telefonnummern. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | Entfernen der Kennzeichnung für ungültige Telefonnummern von Nutzer:innen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Kataloge %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | Hinzufügen mehrerer Artikel zu einem bestehenden Katalog. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | Aktualisieren mehrerer Artikel in einem bestehenden Katalog. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | Löschen mehrerer Artikel aus einem bestehenden Katalog. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | Abrufen eines einzelnen Artikels aus einem bestehenden Katalog. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Aktualisieren eines einzelnen Artikels in einem bestehenden Katalog. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | Erstellen eines einzelnen Artikels in einem bestehenden Katalog. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | Löschen eines einzelnen Artikels aus einem bestehenden Katalog. |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Ersetzen eines einzelnen Artikels in einem bestehenden Katalog. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | Erstellen Sie einen Katalog. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | Eine Liste der Kataloge erhalten |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | Löschen Sie einen Katalog. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | Abrufen von Artikelvorschauen aus einem bestehenden Katalog. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | Ersetzen Sie Artikel in einem bestehenden Katalog. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SDK-Authentifizierung %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `sdk_authentication.create` | [`/app_group/sdk_authentication/create`]({{site.baseurl}}/api/endpoints/sdk_authentication/post_create_sdk_authentication_key) | Erstellen Sie einen neuen SDK-Authentifizierungsschlüssel für Ihre App. |
| `sdk_authentication.primary` | [`/app_group/sdk_authentication/primary`]({{site.baseurl}}/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/) | Markieren Sie einen SDK-Authentifizierungsschlüssel als Primärschlüssel für Ihre App. |
| `sdk_authentication.delete` | [`/app_group/sdk_authentication/delete`]({{site.baseurl}}/api/endpoints/sdk_authentication/delete_sdk_authentication_key) | Löschen Sie einen SDK-Authentifizierungsschlüssel für Ihre App. |
| `sdk_authentication.keys` | [`/app_group/sdk_authentication/keys`]({{site.baseurl}}/api/endpoints/sdk_authentication/get_sdk_authentication_keys) | Erhalten Sie alle SDK Authentifizierungsschlüssel für Ihre App. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### REST API-Schlüssel verwalten

Unter **Einstellungen** > **APIs und Bezeichner** > **Tab API-Schlüssel** können Sie Details zu vorhandenen REST-API-Schlüsseln einsehen oder diese löschen. Beachten Sie, dass REST API-Schlüssel nach ihrer Erstellung nicht mehr bearbeitet werden können.

Der Tab **API-Schlüssel** enthält die folgenden Informationen für jeden Schlüssel:

| Feld        | Beschreibung                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| API-Schlüsselname | Der Name, der dem Schlüssel bei der Erstellung gegeben wurde.                                                                            |
| Bezeichner   | Der API-Schlüssel.                                                                                                        |
| Erstellt von   | Die E-Mail Adresse des Nutzers:in, der den Schlüssel erstellt hat. Dieses Feld wird für Schlüssel, die vor Juni 2023 erstellt wurden, als "N/A" angezeigt. |
| Datum der Erstellung | Das Datum, an dem dieser Schlüssel erstellt wurde.                                                                                      |
| Zuletzt angesehen    | Das Datum, an dem dieser Schlüssel zuletzt verwendet wurde. Dieses Feld wird als "N/A" für Schlüssel angezeigt, die noch nie verwendet wurden.                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Um die Details eines API-Schlüssels anzuzeigen, bewegen Sie den Mauszeiger über den Schlüssel und wählen Sie <i class="fa-solid fa-eye" alt="View"></i> **Ansicht**. Dazu gehören alle Berechtigungen, die dieser Schlüssel hat, IPs auf der Whitelist (falls vorhanden) und ob dieser Schlüssel in die IP-Whitelist von Braze aufgenommen wurde.

![Die Liste der API-Schlüssel-Berechtigungen im Braze-Dashboard.]({% image_buster /assets/img_archive/view-api-key.png %})

Beachten Sie, dass beim [Löschen von Nutzer:innen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) die zugehörigen API-Schlüssel, die von den Nutzer:innen erstellt wurden, nicht gelöscht werden. Um eine Taste zu löschen, bewegen Sie den Mauszeiger über die Taste und wählen Sie <i class="fa-solid fa-trash-can" alt="Delete"></i> **Löschen**.

![Ein API-Schlüssel mit dem Namen "Zuletzt gesehen", wobei das Papierkorbsymbol hervorgehoben ist und "Löschen" anzeigt.]({% image_buster /assets/img_archive/api-key-options.png %}){: style="max-width:30%;"}

### REST API-Schlüssel Sicherheit

API-Schlüssel werden zur Authentifizierung eines API-Aufrufs verwendet. Wenn Sie einen neuen REST API-Schlüssel erstellen, müssen Sie ihm Zugriff auf bestimmte Endpunkte geben. Indem Sie einem API-Schlüssel bestimmte Berechtigungen zuweisen, können Sie genau festlegen, welche Aufrufe ein API-Schlüssel authentifizieren kann.

Da REST API-Schlüssel den Zugang zu potenziell sensiblen REST API-Endpunkten erlauben, sollten Sie diese Schlüssel sichern und nur mit vertrauenswürdigen Partnern teilen. Sie sollten niemals öffentlich bloßgestellt werden. Verwenden Sie diesen Schlüssel beispielsweise nicht, um AJAX-Aufrufe von Ihrer Website aus zu tätigen oder ihn auf andere Weise öffentlich zugänglich zu machen.

Eine gute Sicherheitspraxis besteht darin, einem Nutzer:innen nur so viel Zugriff zu gewähren, wie er für die Erfüllung seiner Aufgabe benötigt. Dieses Prinzip kann auch auf API-Schlüssel angewendet werden, indem jedem Schlüssel Berechtigungen zugewiesen werden. Diese Berechtigungen bieten Ihnen mehr Sicherheit und Kontrolle über die verschiedenen Bereiche Ihres Kontos.

{% alert warning %}
Da REST API-Schlüssel den Zugang zu potenziell sensiblen REST API-Endpunkten erlauben, sollten Sie sicherstellen, dass sie sicher gespeichert und verwendet werden. Verwenden Sie diesen Schlüssel beispielsweise nicht, um AJAX-Aufrufe von Ihrer Website aus zu tätigen oder ihn auf andere Weise öffentlich zugänglich zu machen.
{% endalert %}

Wenn ein Schlüssel versehentlich freigelegt wurde, kann er aus der Entwickler:in gelöscht werden. Wenn Sie Hilfe bei diesem Vorgang benötigen, öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

### API IP allowlisting

Für zusätzliche Sicherheit können Sie eine Liste von IP-Adressen und Subnetzen angeben, die für einen bestimmten REST-API-Schlüssel Anfragen an die REST API zulassen. Dies wird als Allowlisting oder Whitelisting bezeichnet. Um bestimmte IP-Adressen oder Subnetze zuzulassen, fügen Sie sie bei der Erstellung eines neuen REST-API-Schlüssels dem Abschnitt **Whitelist IPs** hinzu:

![Option, um IPs bei der Erstellung eines API-Schlüssels aufzulisten.]({% image_buster /assets/img_archive/api-key-ip-whitelisting.png %})

Wenn Sie nichts angeben, können Anfragen von jeder IP-Adresse gesendet werden.

{% alert tip %}
Einen Braze-to-Braze Webhook erstellen und allowlisting verwenden? Sehen Sie sich unsere Liste der [IPs an, die Sie auf die Whitelist setzen können]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

## Zusätzliche Ressourcen

### Ruby Client Bibliothek

Wenn Sie Braze mit Ruby implementieren, können Sie unsere [Ruby Client Bibliothek](https://github.com/braze-inc/braze-api-client-ruby) verwenden, um die Zeit für den Datenimport zu reduzieren. Eine Client Bibliothek ist eine Sammlung von Code für eine bestimmte Programmiersprache - in diesem Fall Ruby -, die die Verwendung einer API erleichtert.

Die Ruby Client Bibliothek unterstützt die [Nutzer:innen Endpunkte]({{site.baseurl}}/api/endpoints/user_data).

{% alert important %}
Diese Client Bibliothek befindet sich derzeit in der Beta-Phase. Möchten Sie uns helfen, diese Bibliothek zu verbessern? Senden Sie uns Ihr Feedback an [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}

