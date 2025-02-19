---
nav_title: "API-Übersicht"
article_title: API-Übersicht
page_order: 2.1
description: "Dieser Referenzartikel behandelt die API-Grundlagen, einschließlich dessen, was eine REST-API ist, die Terminologie und einen Überblick über API-Schlüssel."
page_type: reference
alias: /api/api_key/
---

# API-Übersicht

> Dieser Referenzartikel befasst sich mit den API-Grundlagen, einschließlich der allgemeinen Terminologie und einem Überblick über REST-API-Schlüssel, Berechtigungen und wie Sie diese sicher halten können.

## Braze REST API Sammlung

| Kollektion                                                                 | Zweck                                                                               |
|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [Kataloge]({{site.baseurl}}/api/endpoints/catalogs/)                       | Erstellen und verwalten Sie Kataloge und Katalogartikel, auf die Sie in Ihren Braze-Kampagnen verweisen können.    |
| [Ingestion von Cloud-Daten]({{site.baseurl}}/api/endpoints/cdi/)                | Verwalten Sie Ihre Data Warehouse-Integrationen und -Synchronisationen.                                    |
| [E-Mail-Listen und Adressen]({{site.baseurl}}/api/endpoints/email/)         | Richten Sie die bidirektionale Synchronisierung zwischen Braze und Ihren E-Mail-Systemen ein und verwalten Sie sie.           |
| [Exportieren]({{site.baseurl}}/api/endpoints/export/)                           | Greifen Sie auf verschiedene Details Ihrer Kampagnen, Canvases, KPIs und mehr zu und exportieren Sie sie.        |
| [Nachrichten]({{site.baseurl}}/api/endpoints/messaging/)                      | Planen, versenden und verwalten Sie Ihre Kampagnen und Canvases.                               |
| [Präferenz-Zentrum]({{site.baseurl}}/api/endpoints/preference_center/)     | Bauen Sie Ihr Einstellungscenter auf und aktualisieren Sie das Styling.                            |
| [SCIM]({{site.baseurl}}/api/endpoints/scim/)                               | Verwalten Sie Benutzeridentitäten in Cloud-basierten Anwendungen und Diensten.                      |
| [SMS]({{site.baseurl}}/api/endpoints/sms/)                                 | Verwalten Sie die Rufnummern Ihrer Benutzer in Ihren Abonnementgruppen.                         |
| [Abonnement-Gruppen]({{site.baseurl}}/api/endpoints/subscription_groups/) | Auflisten und Aktualisieren von SMS- und E-Mail-Abonnementgruppen, die im Braze Dashboard gespeichert sind. |
| [Vorlagen]({{site.baseurl}}/api/endpoints/templates/)                     | Erstellen und aktualisieren Sie Vorlagen für E-Mail-Nachrichten und Inhaltsblöcke.                   |
| [Benutzerdaten]({{site.baseurl}}/api/endpoints/user_data/)                     | Identifizieren, verfolgen und verwalten Sie Ihre Benutzer.                                               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## API-Definitionen

Im Folgenden finden Sie eine Übersicht der Begriffe, die Sie in der Braze REST API-Dokumentation finden können.

### Endpunkte

Braze verwaltet eine Reihe verschiedener Instanzen für unser Dashboard und unsere REST-Endpunkte. Wenn Ihr Konto eingerichtet ist, melden Sie sich unter einer der folgenden URLs an. Verwenden Sie den richtigen REST-Endpunkt, je nachdem, für welche Instanz Sie provisioniert sind. Wenn Sie sich nicht sicher sind, öffnen Sie ein [Support-Ticket][Support] oder verwenden Sie die folgende Tabelle, um die URL des von Ihnen verwendeten Dashboards mit dem richtigen REST-Endpunkt abzugleichen.

{% alert important %}
Wenn Sie Endpunkte für API-Aufrufe verwenden, benutzen Sie den REST-Endpunkt.

Für die SDK-Integration verwenden Sie den [SDK-Endpunkt]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/), nicht den REST-Endpunkt.
{% endalert %}

|Instanz|URL|REST Endpunkt|SDK Endpunkt|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### API-Grenzwerte

Für die meisten APIs hat Braze ein Standard-Ratenlimit von 250.000 Anfragen pro Stunde. Für bestimmte Anfragetypen gilt jedoch ein eigenes Tariflimit, um hohe Datenvolumina in unserem Kundenstamm besser bewältigen zu können. Einzelheiten finden Sie unter [API-Ratengrenzen]({{site.baseurl}}/api/api_limits/)

### Benutzer-IDs

- **Externe Benutzer-ID**: Die `external_id` dient als eindeutige Benutzerkennung, für die Sie Daten übermitteln. Diese Kennung sollte die gleiche sein wie die, die Sie im Braze SDK eingestellt haben, um zu vermeiden, dass mehrere Profile für denselben Benutzer erstellt werden.
- **Braze-Benutzer-ID**: `braze_id` dient als eindeutiger Benutzeridentifikator, der von Braze festgelegt wird. Diese Kennung kann zusätzlich zu external_ids zum Löschen von Benutzern über die REST-API verwendet werden.

Weitere Informationen finden Sie in den folgenden Artikeln zu Ihrer Plattform: [iOS][9], [Android][10] und [Web][13].

## Über REST-API-Schlüssel

Ein REST Application Programming Interface-Schlüssel (REST-API-Schlüssel) ist ein eindeutiger Code, der an eine API übergeben wird, um den API-Aufruf zu authentifizieren und die aufrufende Anwendung oder den Benutzer zu identifizieren. Der API-Zugriff erfolgt über HTTPS-Webanfragen an den REST-API-Endpunkt Ihres Unternehmens. Wir verwenden REST-API-Schlüssel bei Braze zusammen mit unseren App-Identifizierungsschlüsseln, um Daten zu verfolgen, darauf zuzugreifen, sie zu senden, zu exportieren und zu analysieren, um sicherzustellen, dass sowohl auf Ihrer als auch auf unserer Seite alles reibungslos läuft.

Workspaces und API-Schlüssel gehen bei Braze Hand in Hand. Arbeitsbereiche sind so konzipiert, dass sie Versionen derselben Anwendung für mehrere Plattformen enthalten. Viele Kunden nutzen Workspaces auch, um kostenlose und Premium-Versionen ihrer Anwendungen auf derselben Plattform unterzubringen. Wie Sie vielleicht bemerken, nutzen auch diese Arbeitsbereiche die REST-API und haben ihre eigenen REST-API-Schlüssel. Diese Schlüssel können individuell angepasst werden, um den Zugriff auf bestimmte Endpunkte der API zu ermöglichen. Jeder Aufruf der API muss einen Schlüssel enthalten, der Zugriff auf den getroffenen Endpunkt hat.

Wir bezeichnen sowohl den REST-API-Schlüssel als auch den Arbeitsbereich-API-Schlüssel als `api_key`. Die `api_key` ist in jeder Anfrage als Anfrage-Header enthalten und dient als Authentifizierungsschlüssel, mit dem Sie unsere REST-APIs nutzen können. Diese REST-APIs werden verwendet, um Benutzer zu verfolgen, Nachrichten zu versenden, Benutzerdaten zu exportieren und vieles mehr. Wenn Sie einen neuen REST-API-Schlüssel erstellen, müssen Sie ihm Zugriff auf bestimmte Endpunkte geben. Indem Sie einem API-Schlüssel bestimmte Berechtigungen zuweisen, können Sie genau festlegen, welche Anrufe ein API-Schlüssel authentifizieren kann.

![REST-API-Schlüssel auf der Registerkarte API-Schlüssel.][27]

{% alert tip %}
Zusätzlich zu den REST-API-Schlüsseln gibt es auch eine Art von Schlüsseln, die so genannten Identifier-Schlüssel, die verwendet werden können, um bestimmte Dinge wie Apps, Vorlagen, Canvases, Kampagnen, Content Cards und Segmente aus der API zu referenzieren. Weitere Informationen finden Sie unter [API-Kennungstypen]({{site.baseurl}}/api/identifier_types/).
{% endalert %}

### REST API-Schlüssel erstellen

So erstellen Sie einen neuen REST-API-Schlüssel:

1. Gehen Sie zu **Einstellungen** > **APIs und Identifikatoren**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie einen API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen** erstellen.
{% endalert %}

{:start="2"}
2\. Wählen Sie **API-Schlüssel erstellen**.
3\. Geben Sie Ihrem neuen Schlüssel einen Namen, um ihn auf einen Blick identifizieren zu können.
4\. Geben Sie [die zulässigen IP-Adressen](#api-ip-allowlisting) und Subnetze für den neuen Schlüssel an.
5\. Wählen Sie aus, welche [Berechtigungen](#rest-api-key-permissions) mit Ihrem neuen Schlüssel verknüpft werden sollen.

{% alert important %}
Beachten Sie, dass Sie nach der Erstellung eines neuen API-Schlüssels weder den Umfang der Berechtigungen noch die zugelassenen IPs bearbeiten können. Diese Einschränkung erfolgt aus Sicherheitsgründen. Wenn Sie den Geltungsbereich eines Schlüssels ändern müssen, erstellen Sie einen neuen Schlüssel mit den aktualisierten Berechtigungen und implementieren diesen Schlüssel anstelle des alten. Nachdem Sie Ihre Implementierung abgeschlossen haben, können Sie den alten Schlüssel löschen.
{% endalert %}

### Berechtigungen für REST-API-Schlüssel

API-Schlüsselberechtigungen sind Berechtigungen, die Sie einem Benutzer oder einer Gruppe zuweisen können, um deren Zugriff auf bestimmte API-Aufrufe zu beschränken. Um Ihre Liste der API-Schlüssel-Berechtigungen anzuzeigen, gehen Sie zu **Einstellungen** > **APIs und Identifikatoren** und wählen Sie Ihren API-Schlüssel aus.

{% tabs %}
{% tab Benutzerdaten %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `users.track` | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | Erfassen Sie Benutzerattribute, benutzerdefinierte Ereignisse und Käufe. |
| `users.delete` | [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | Löschen Sie einen beliebigen Benutzer. |
| `users.alias.new` | [`/users/alias/new`]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/) |Erstellen Sie einen neuen Alias für einen bestehenden Benutzer. |
| `users.identify` | [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) |Identifizieren Sie einen reinen Alias-Benutzer mit einer externen ID. |
| `users.export.ids` | [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) |Abfrage von Benutzerprofilinformationen nach Benutzer-ID. |
| `users.export.segment` | [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) |Abfrage von Benutzerprofilinformationen nach Segment. |
| `users.merge` | [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) | Verschmilzt zwei bestehende Benutzer miteinander. |
| `users.external_ids.rename` | [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/) | Ändern Sie die externe ID für einen bestehenden Benutzer. |
| `users.external_ids.remove` | [`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove/) | Entfernen Sie die externe ID für einen bestehenden Benutzer. |
| `users.alias.update` | [`/users/alias/update`]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) | Aktualisieren Sie einen Alias für einen bestehenden Benutzer. |
| `users.export.global_control_group` | [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) | Abfrage von Benutzerprofilinformationen in der Globalen Kontrollgruppe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

 {% endtab %}
 {% tab E-Mail %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `email.unsubscribe` | [`/email/unsubscribes`]({{site.baseurl}}/api/endpoints/email/get_query_unsubscribed_email_addresses/) | Abfrage nach abgemeldeten E-Mail-Adressen.  |
| `email.status` | [`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) | Status der E-Mail-Adresse ändern. |
| `email.hard_bounces` | [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) | Abfrage nach hartnäckig abgelehnten E-Mail-Adressen. |
| `email.bounce.remove` | [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces/) | Entfernen Sie E-Mail-Adressen aus Ihrer Hardbounce-Liste. |
| `email.spam.remove` | [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam/) | Entfernen Sie E-Mail-Adressen aus Ihrer Spam-Liste. |
| `email.blacklist` | [`/email/blacklist`]({{site.baseurl}}/api/endpoints/email/post_blacklist/) | Blockliste E-Mail-Adressen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Nachrichten %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `messages.send` | [`/messages/send `]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | Senden Sie eine Sofortnachricht an bestimmte Benutzer. |
| `messages.schedule.create` | [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) | Planen Sie das Versenden einer Nachricht zu einer bestimmten Zeit. |
| `messages.schedule.update` | [`/messages/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/) | Aktualisieren Sie eine geplante Nachricht. |
| `messages.schedule.delete` | [`/messages/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/) | Löschen Sie eine geplante Nachricht. |
| `messages.schedule_broadcasts` | [`/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/) | Abfrage aller geplanten Broadcast-Nachrichten. |
| `messages.live_activity.update` | [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update/) | Aktualisieren Sie eine iOS Live-Aktivität. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Kampagnen %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `campaigns.trigger.send` | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) | Lösen Sie den Versand einer bestehenden Kampagne aus. |
| `campaigns.trigger.schedule.create` | [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/) | Planen Sie einen zukünftigen Versand einer Kampagne mit API-gesteuerter Zustellung. |
| `campaigns.trigger.schedule.update` | [`/campaigns/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/) | Aktualisieren Sie eine geplante Kampagne mit API-gesteuerter Zustellung. |
| `campaigns.trigger.schedule.delete` | [`/campaigns/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/) |Löschen Sie eine Kampagne, die mit API-gesteuerter Zustellung geplant ist. |
| `campaigns.list` | [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) | Abfrage nach einer Liste von Kampagnen. |
| `campaigns.data_series` | [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | Abfrage von Kampagnenanalysen über einen bestimmten Zeitraum. |
| `campaigns.details` | [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | Abfrage von Details zu einer bestimmten Kampagne. |
| `sends.data_series` | [`/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) | Abfrage der Analyse des Nachrichtenversands über einen bestimmten Zeitraum. |
| `sends.id.create` | [`/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) | Erstellen Sie eine Sende-ID für die Nachverfolgung von Nachrichtenexplosionen. |
| `campaigns.url_info.details` | [`/campaigns/url_info/details`]({{site.baseurl}}) | Abfrage der URL-Details einer bestimmten Nachrichtenvariante innerhalb einer Kampagne. |
| `transactional.send` | [`/transactional/v1/campaigns/{campaign_id}/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) | Ermöglicht das Senden von Transaktionsnachrichten über den Endpunkt Transaktionsnachrichten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Segeltuch %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `canvas.trigger.send` | [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) | Lösen Sie das Senden einer bestehenden Leinwand aus. |
| `canvas.trigger.schedule.create` | [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/) | Planen Sie einen zukünftigen Versand eines Canvas mit API-gesteuerter Zustellung. |
| `canvas.trigger.schedule.update` | [`/canvas/trigger/schedule/update`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/) | Aktualisieren Sie ein Canvas, das mit API-gesteuerter Zustellung geplant ist. |
| `canvas.trigger.schedule.delete` | [`/canvas/trigger/schedule/delete`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/)| Löschen Sie ein Canvas, das mit einer API-gesteuerten Zustellung geplant ist. |
| `canvas.list` | [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) |  Abfrage nach einer Liste von Leinwänden. |
| `canvas.data_series` | [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | Abfrage nach Canvas-Analysen über einen bestimmten Zeitraum. |
| `canvas.details` | [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) | Abfrage von Details zu einem bestimmten Canvas. |
| `canvas.data_summary` | [`/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) | Abfrage nach Rollups von Canvas-Analysen über einen bestimmten Zeitraum. |
| `canvas.url_info.details` | [`/canvas/url_info/details`]({{site.baseurl}}/get_canvas_link_alias/) | Abfrage von URL-Details einer bestimmten Nachrichtenvariation innerhalb eines Canvas-Schrittes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Segmente %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `segments.list` | [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | Abfrage nach einer Liste von Segmenten. |
| `segments.data_series` | [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | Suchen Sie nach Segmentanalysen über einen bestimmten Zeitraum. |
| `segments.details` | [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/) | Abfrage von Details zu einem bestimmten Segment. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Käufe %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `purchases.product_list` | [`/purchases/product_list`]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) | Suchen Sie nach einer Liste der in Ihrer App gekauften Produkte. |
| `purchases.revenue_series` | [`/purchases/revenue_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_revenue_series/) | Abfrage der Gesamtausgaben pro Tag in Ihrer App über einen bestimmten Zeitraum. |
| `purchases.quantity_series` | [`/purchases/quantity_series`]({{site.baseurl}}/api/endpoints/export/purchases/get_number_of_purchases/) | Suchen Sie nach der Gesamtzahl der Käufe pro Tag in Ihrer App über einen bestimmten Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Ereignisse %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `events.list` | [`/events/list`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events/) | Abfrage nach einer Liste von benutzerdefinierten Ereignissen. |
| `events.data_series` | [`/events/data_series`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_analytics/) | Abfrage des Auftretens eines benutzerdefinierten Ereignisses über einen Zeitbereich. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab News Feed %}

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `feed.list` | [`/feed/list`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_cards/) | Abfrage nach einer Liste von News Feed-Karten. |
| `feed.data_series` | [`/feed/data_series`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_analytics/) | Abfrage von News Feed-Analysen über einen bestimmten Zeitraum. |
| `feed.details` | [`/feed/details`]({{site.baseurl}}/api/endpoints/export/news_feed/get_news_feed_card_details/) | Abfrage von Details zu einem bestimmten News Feed. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Sitzungen %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `sessions.data_series` | [`/sessions/data_series`]({{site.baseurl}}/api/endpoints/export/sessions/get_sessions_analytics/) | Abfrage nach Sitzungen pro Tag über einen bestimmten Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab KPIs %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `kpi.dau.data_series` | [`/kpi/dau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_dau_date/) |  Abfrage nach einmaligen aktiven Nutzern pro Tag über einen bestimmten Zeitraum. |
| `kpi.mau.data_series` | [`/kpi/mau/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_mau_30_days/) | Abfrage nach der Gesamtzahl der eindeutigen aktiven Benutzer über ein rollierendes 30-Tage-Fenster in einem bestimmten Zeitraum. |
| `kpi.new_users.data_series` | [`/kpi/new_users/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_daily_new_users_date/) | Abfrage nach neuen Benutzern pro Tag über einen bestimmten Zeitraum. |
| `kpi.uninstalls.data_series` | [`/kpi/uninstalls/data_series`]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/) | Abfrage nach App-Deinstallationen pro Tag über einen bestimmten Zeitraum. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Vorlagen %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `templates.email.create` | [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | Erstellen Sie eine neue E-Mail-Vorlage auf dem Dashboard. |
| `templates.email.info` | [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Abfrage von Informationen zu einer bestimmten Vorlage. |
| `templates.email.list` | [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | Abfrage nach einer Liste von E-Mail-Vorlagen. |
| `templates.email.update` | [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | Aktualisieren Sie eine auf dem Dashboard gespeicherte E-Mail-Vorlage. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SSO %}

| Erlaubnis | Beschreibung |
|---|---|---|
| `sso.saml.login` | Richten Sie die vom Identitätsanbieter veranlasste Anmeldung ein. Weitere Informationen finden Sie unter [Anmeldung durch den Service Provider (SP)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Inhalt Blöcke %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `content_blocks.info` | [`/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) | Abfrage von Informationen zu einer bestimmten Vorlage. |
| `content_blocks.list` | [`/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) | Abfrage nach einer Liste von Inhaltsblöcken. |
| `content_blocks.create` | [`/content_blocks/create`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/) | Erstellen Sie einen neuen Inhaltsblock auf dem Dashboard. |
| `content_blocks.update` | [`/content_blocks_update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) | Aktualisieren Sie einen bestehenden Inhaltsblock auf dem Dashboard. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Präferenz-Center %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `preference_center.get` | [`/preference_center/v1/{preferenceCenterExternalId}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center) | Besorgen Sie sich ein Präferenzzentrum. |
| `preference_center.list` | [`/preference_center/v1/list`]({{site.baseurl}}/api/endpoints/preference_center/get_list_preference_center/) | Liste der Präferenzzentren. |
| `preference_center.update` | [`/preference_center/v1`]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)<br><br>[`/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/) | Erstellen oder aktualisieren Sie ein Präferenzzentrum. |
| `preference_center.user.get` | [`/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center) | Holen Sie sich einen Link zum Einstellungscenter für einen Benutzer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Abonnement %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `subscription.status.set` | [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) | Setzen Sie den Status der Abonnementgruppe. |
| `subscription.status.get` | [`/subscription/status/get`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) | Status der Abonnementgruppe abrufen. |
| `subscription.groups.get` | [`/subscription/user/status`]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/) | Ermitteln Sie den Status von Abonnementgruppen, die bestimmte Benutzer explizit abonniert und abbestellt haben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab SMS %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `sms.invalid_phone_numbers` | [`/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) | Abfrage nach ungültigen Telefonnummern. |
| `sms.invalid_phone_numbers.remove` | [`/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) | Entfernen Sie das Kennzeichen für ungültige Telefonnummern von Benutzern. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Kataloge %}

| Erlaubnis | Endpunkt | Beschreibung |
|---|---|---|
| `catalogs.add_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/) | Mehrere Artikel zu einem bestehenden Katalog hinzufügen. |
| `catalogs.update_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/) | Aktualisieren Sie mehrere Artikel in einem bestehenden Katalog. |
| `catalogs.delete_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk) | Löschen Sie mehrere Artikel aus einem bestehenden Katalog. |
| `catalogs.get_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/) | Holen Sie einen einzelnen Artikel aus einem bestehenden Katalog. |
| `catalogs.update_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Aktualisieren Sie einen einzelnen Artikel in einem bestehenden Katalog. |
| `catalogs.create_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/) | Erstellen Sie einen einzelnen Artikel in einem bestehenden Katalog. |
| `catalogs.delete_item` | [`/catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/) | Löschen Sie einen einzelnen Artikel aus einem bestehenden Katalog. |
| `catalogs.replace_item` | [` /catalogs/{catalog_name}/items/{item_id}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) | Ersetzen Sie einen einzelnen Artikel aus einem bestehenden Katalog. |
| `catalogs.create` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/) | Erstellen Sie einen Katalog. |
| `catalogs.get` | [`/catalogs`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/) | Eine Liste von Katalogen erhalten |
| `catalogs.delete` | [`/catalogs/{catalog_name}`]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/) | Löschen Sie einen Katalog. |
| `catalogs.get_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/) | Holen Sie sich eine Artikelvorschau aus einem vorhandenen Katalog. |
| `catalogs.replace_items` | [`/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) | Ersetzen Sie Artikel in einem bestehenden Katalog. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% endtabs %}

### REST API-Schlüssel verwalten

Sie können Details zu vorhandenen REST-API-Schlüsseln unter **Einstellungen** > **APIs und Identifikatoren** > Registerkarte **API-Schlüssel** einsehen oder löschen. Beachten Sie, dass REST-API-Schlüssel nach ihrer Erstellung nicht mehr bearbeitet werden können.

Die Registerkarte **API-Schlüssel** enthält die folgenden Informationen für jeden Schlüssel:

| Feld        | Beschreibung                                                                                                         |
| ------------ | :------------------------------------------------------------------------------------------------------------------ |
| API-Schlüssel Name | Der Name, der dem Schlüssel bei der Erstellung gegeben wurde.                                                                            |
| Kennung   | Der API-Schlüssel.                                                                                                        |
| Erstellt von   | Die E-Mail-Adresse des Benutzers, der den Schlüssel erstellt hat. Dieses Feld wird für Schlüssel, die vor Juni 2023 erstellt wurden, als "N/A" angezeigt. |
| Datum erstellt | Das Datum, an dem dieser Schlüssel erstellt wurde.                                                                                      |
| Zuletzt gesehen    | Das Datum, an dem dieser Schlüssel zuletzt verwendet wurde. Dieses Feld wird als "N/A" für Schlüssel angezeigt, die noch nie verwendet wurden.                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Um die Details eines API-Schlüssels anzuzeigen, bewegen Sie den Mauszeiger über den Schlüssel und wählen Sie <i class="fa-solid fa-eye" alt="View"></i> **Ansicht**. Dazu gehören alle Berechtigungen, die dieser Schlüssel hat, IPs auf der Whitelist (falls vorhanden) und ob dieser Schlüssel für die IP-Whitelist von Braze ausgewählt wurde.

![Die Liste der API-Schlüssel-Berechtigungen im Braze Dashboard.][30]

Beachten Sie, dass beim [Löschen eines Benutzers]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/) die zugehörigen API-Schlüssel, die der Benutzer erstellt hat, nicht gelöscht werden. Um eine Taste zu löschen, bewegen Sie den Mauszeiger über die Taste und wählen Sie <i class="fa-solid fa-trash-can" alt="Delete"></i> **Löschen**.

![Ein API-Schlüssel mit dem Namen "Zuletzt gesehen", wobei das Papierkorbsymbol hervorgehoben ist und "Löschen" anzeigt.][29]{: style="max-width:30%;"}

### Sicherheit der REST-API-Schlüssel

API-Schlüssel werden zur Authentifizierung eines API-Aufrufs verwendet. Wenn Sie einen neuen REST-API-Schlüssel erstellen, müssen Sie ihm Zugriff auf bestimmte Endpunkte geben. Indem Sie einem API-Schlüssel bestimmte Berechtigungen zuweisen, können Sie genau festlegen, welche Anrufe ein API-Schlüssel authentifizieren kann.

Da REST-API-Schlüssel den Zugriff auf potenziell sensible REST-API-Endpunkte ermöglichen, sollten Sie diese Schlüssel sichern und nur mit vertrauenswürdigen Partnern teilen. Sie sollten niemals öffentlich bloßgestellt werden. Verwenden Sie diesen Schlüssel beispielsweise nicht, um AJAX-Aufrufe von Ihrer Website aus zu tätigen oder ihn auf eine andere Weise öffentlich zugänglich zu machen.

Eine gute Sicherheitspraxis ist es, einem Benutzer nur so viel Zugriff zu gewähren, wie er für seine Arbeit benötigt: Dieses Prinzip kann auch auf API-Schlüssel angewendet werden, indem jedem Schlüssel Berechtigungen zugewiesen werden. Diese Berechtigungen bieten Ihnen mehr Sicherheit und Kontrolle über die verschiedenen Bereiche Ihres Kontos.

{% alert warning %}
Da REST-API-Schlüssel den Zugriff auf potenziell sensible REST-API-Endpunkte ermöglichen, sollten Sie sicherstellen, dass sie sicher gespeichert und verwendet werden. Verwenden Sie diesen Schlüssel beispielsweise nicht, um AJAX-Aufrufe von Ihrer Website aus zu tätigen oder ihn auf eine andere Weise öffentlich zugänglich zu machen.
{% endalert %}

Wenn ein Schlüssel versehentlich freigelegt wird, kann er in der Entwicklerkonsole gelöscht werden. Wenn Sie Hilfe bei diesem Vorgang benötigen, öffnen Sie ein [support ticket][support].

### API IP-Zulassungsliste

Für zusätzliche Sicherheit können Sie eine Liste von IP-Adressen und Subnetzen angeben, die REST-API-Anfragen für einen bestimmten REST-API-Schlüssel stellen dürfen. Dies wird als "Zulassen" oder "Whitelisting" bezeichnet. Um bestimmte IP-Adressen oder Subnetze zuzulassen, fügen Sie diese bei der Erstellung eines neuen REST-API-Schlüssels zum Abschnitt **Whitelist IPs** hinzu:

![Option, um IPs bei der Erstellung eines API-Schlüssels aufzulisten.][26]

Wenn Sie nichts angeben, können die Anfragen von jeder IP-Adresse aus gesendet werden.

{% alert tip %}
Einen Braze-to-Braze Webhook erstellen und allowlisting verwenden? Sehen Sie sich unsere Liste der [IPs an, die Sie auf die Whitelist setzen können]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-whitelisting).
{% endalert %}

## Zusätzliche Ressourcen

### Ruby Client-Bibliothek

Wenn Sie Braze mit Ruby implementieren, können Sie unsere [Ruby-Client-Bibliothek](https://github.com/braze-inc/braze-api-client-ruby) verwenden, um die Zeit für den Datenimport zu verkürzen. Eine Client-Bibliothek ist eine Sammlung von Code für eine bestimmte Programmiersprache - in diesem Fall Ruby -, die die Verwendung einer API erleichtert.

Die Ruby-Client-Bibliothek unterstützt die [Benutzerendpunkte]({{site.baseurl}}/api/endpoints/user_data).

{% alert note %}
Diese Client-Bibliothek befindet sich derzeit in der Beta-Phase. Möchten Sie uns helfen, diese Bibliothek zu verbessern? Senden Sie uns Ihr Feedback an [smb-product@braze.com](mailto:smb-product@braze.com).
{% endalert %}

[1]: https://en.wikipedia.org/wiki/UTF-8
[7]: {{site.baseurl}}/api/objects_filters/connected_audience/
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[2]: {{site.baseurl}}/api/identifier_types/
[5]: {{site.baseurl}}/api/basics/
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro
[25]: {% image_buster /assets/img_archive/api-key-permissions.png %}
[26]: {% image_buster /assets/img_archive/api-key-ip-whitelisting.png %}
[Unterstützung]: {{site.baseurl}}/braze_support/
[28]: {% image_buster /assets/img_archive/create-new-key.png %}
[29]: {% image_buster /assets/img_archive/api-key-options.png %}
[27]: {% image_buster /assets/img_archive/rest-api-key.png %}
[30]: {% image_buster /assets/img_archive/view-api-key.png %}
