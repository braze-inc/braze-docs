---
nav_title: "SQL-Tabellenreferenz"
article_title: SQL-Tabellen-Referenz
page_order: 3
page_type: reference
toc_headers: h2
description: "Diese Seite ist eine Referenz der Snowflake-SQL-Tabellen und -Spalten, die im Query Builder, in SQL-Segmenterweiterungen und im Snowflake Data Sharing verwendet werden."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQL-Tabellenreferenz

Diese Seite ist eine Referenz der Snowflake-SQL-Tabellen und -Spalten, die in den folgenden Braze-Tools verfügbar sind:

- [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/)
- [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)
- [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)

Die meisten Tabellen sind in allen drei Tools verfügbar. Tabellen, die mit **Nur Snowflake Data Sharing** gekennzeichnet sind, stehen ausschließlich im Snowflake Data Sharing zur Verfügung und sind im Query Builder oder in SQL-Segmenterweiterungen nicht zugänglich.

{% alert tip %}
Diese SQL-Tabellen entsprechen den Events, die im [Currents-Event-Glossar]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) dokumentiert sind. Beispielsweise entspricht die SQL-Tabelle `USERS_MESSAGES_EMAIL_SEND_SHARED` dem Currents-Event `users.messages.email.Send`. Wenn Sie JSON-Event-Schemas oder partnerspezifische Formate (Amplitude, Mixpanel, Segment) benötigen, lesen Sie im Currents-Glossar nach.
{% endalert %}

## Inhaltsverzeichnis

Tabelle | Beschreibung
------|------------
[AGENTCONSOLE_AGENTEXECUTED_SHARED](#AGENTCONSOLE_AGENTEXECUTED_SHARED) | Wenn ein Agent Console-Agent ausgeführt wird (**nur Snowflake Data Sharing**)
[AGENTCONSOLE_TOOLINVOCATION_SHARED](#AGENTCONSOLE_TOOLINVOCATION_SHARED) | Wenn ein Tool ausgeführt wird (**nur Snowflake Data Sharing**)
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | Nicht gelöschte Katalog-Artikel
[CHANGELOGS_CAMPAIGN_SHARED](#CHANGELOGS_CAMPAIGN_SHARED) | Wenn eine Kampagne geändert wird (**nur Snowflake Data Sharing**)
[CHANGELOGS_CANVAS_SHARED](#CHANGELOGS_CANVAS_SHARED) | Wenn ein Canvas geändert wird (**nur Snowflake Data Sharing**)
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | Wenn die globale Kontrollgruppe geändert wird
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Wenn eine Nutzer:in ein angepasstes Event ausführt
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Wenn eine Nutzer:in eine App installiert und wir dies einem Partner zuordnen
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Wenn eine Nutzer:in einen Standort aufzeichnet
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Wenn eine Nutzer:in einen Kauf tätigt
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Wenn eine Nutzer:in eine App deinstalliert
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Wenn eine Nutzer:in die App upgradet
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Wenn eine Nutzer:in ihre erste Sitzung hat
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Wenn eine Nutzer:in den News Feed ansieht
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Wenn eine Nutzer:in eine Sitzung in einer App beendet
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Wenn eine Nutzer:in eine Sitzung in einer App beginnt
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Wenn eine Nutzer:in einen Geofence-Bereich auslöst (z. B. beim Betreten oder Verlassen eines Geofence). Dieses Event wurde zusammen mit anderen Events gebündelt und über den Standard-Events-Endpunkt empfangen und wurde daher möglicherweise nicht in Realtime vom Endpunkt empfangen.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Wenn eine Nutzer:in einen Geofence-Bereich auslöst (z. B. beim Betreten oder Verlassen eines Geofence). Dieses Event wurde über den dedizierten Geofence-Endpunkt empfangen und wird daher in Realtime empfangen, sobald das Gerät der Nutzer:in erkennt, dass ein Geofence ausgelöst wurde. <br><br>Aufgrund von Rate-Limiting am Geofence-Endpunkt ist es außerdem möglich, dass einige Geofence-Events nicht als RecordEvent abgebildet werden. Alle Geofence-Events werden jedoch durch DataEvent repräsentiert (allerdings möglicherweise mit einer gewissen Verzögerung durch die Bündelung).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Wenn sich ein Live Activity Push-to-Start-Token ändert
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Wenn sich ein Live Activity Update-Token ändert
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | Wenn sich der Status eines Push-Benachrichtigungs-Tokens ändert
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Wenn eine Nutzer:in global für einen Kanal wie E-Mail abonniert oder abgemeldet wird
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Wenn eine Nutzer:in eine Abo-Gruppe abonniert oder sich davon abmeldet
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Wenn eine Nutzer:in für eine Kampagne konvertiert
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Wenn eine Nutzer:in in die Kontrollgruppe einer Kampagne aufgenommen wird
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Wenn eine Nutzer:in für eine Kampagne ein Frequency Cap erreicht
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Wenn eine Nutzer:in innerhalb des primären Konversionszeitraums Umsatz generiert
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Wenn eine Nutzer:in zu einem Canvas-Schritt fortschreitet
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Wenn eine Nutzer:in für ein Canvas-Konversions-Event konvertiert
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Wenn eine Nutzer:in ein Canvas betritt
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Wenn eine Nutzer:in ein Canvas verlässt, weil sie die Zielgruppen-Ausstiegskriterien erfüllt
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Wenn eine Nutzer:in ein Canvas verlässt, weil sie ein Ausnahme-Event ausgeführt hat
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Wenn eine Nutzer:in für einen Canvas-Experiment-Schritt konvertiert
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Wenn eine Nutzer:in einen Experiment-Schritt-Pfad betritt
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Wenn eine Nutzer:in für einen Canvas-Schritt ein Frequency Cap erreicht
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Wenn eine Nutzer:in innerhalb des primären Konversions-Event-Zeitraums Umsatz generiert
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | Eine ursprünglich geplante Banner-Nachricht wurde aus einem bestimmten Grund abgebrochen
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | Wenn eine Nutzer:in auf ein Banner klickt
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | Wenn eine Nutzer:in ein Banner ansieht
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Eine ursprünglich geplante Content-Card-Nachricht wurde aus einem bestimmten Grund abgebrochen.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Wenn eine Nutzer:in auf eine Content Card klickt
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Wenn eine Nutzer:in eine Content Card schließt
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Wenn eine Nutzer:in eine Content Card ansieht
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Wenn wir einer Nutzer:in eine Content Card senden
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Eine ursprünglich geplante E-Mail-Nachricht wurde aus einem bestimmten Grund abgebrochen.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Ein E-Mail-Anbieter hat einen Hard Bounce zurückgegeben. Ein Hard Bounce weist auf einen dauerhaften Zustellbarkeitsfehler hin.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Wenn eine Nutzer:in auf einen Link in einer E-Mail klickt
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | Wenn eine E-Mail zurückgestellt wird
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Wenn eine E-Mail zugestellt wird
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Wenn eine E-Mail als Spam markiert wird
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Wenn eine Nutzer:in eine E-Mail öffnet
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Wenn wir einer Nutzer:in eine E-Mail senden
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Wenn eine E-Mail einen Soft Bounce verursacht
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Wenn sich eine Nutzer:in von E-Mails abmeldet
[USERS_MESSAGES_EMAIL_RETRY_SHARED](#USERS_MESSAGES_EMAIL_RETRY_SHARED) | Wenn eine E-Mail-Nachricht nach Depriorisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | Wenn eine Nutzer:in ein Feature-Flag ansieht
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Eine ursprünglich geplante In-App-Nachricht wurde aus einem bestimmten Grund abgebrochen.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Wenn eine Nutzer:in auf eine In-App-Nachricht klickt
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Wenn eine Nutzer:in eine In-App-Nachricht ansieht
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | Wenn eine geplante LINE-Nachricht vor dem Senden an LINE nicht zugestellt werden kann
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | Wenn eine Nutzer:in auf einen Link in einer LINE-Nachricht klickt
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | Wenn eine LINE-Nachricht von einer Nutzer:in empfangen wird
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | Wenn eine LINE-Nachricht an LINE gesendet wird
[USERS_MESSAGES_LINE_RETRY_SHARED](#USERS_MESSAGES_LINE_RETRY_SHARED) | Wenn eine LINE-Nachricht nach Depriorisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Wenn eine Live Activity ein Ergebnis-Event hat
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Wenn eine Live Activity-Nachricht gesendet wird
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Eine ursprünglich geplante Newsfeed-Karten-Nachricht wurde aus einem bestimmten Grund abgebrochen
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Wenn eine Nutzer:in auf eine Newsfeed-Karte klickt
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Wenn eine Nutzer:in eine Newsfeed-Karte ansieht
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Eine ursprünglich geplante Push-Benachrichtigung wurde aus einem bestimmten Grund abgebrochen.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Wenn eine Push-Benachrichtigung einen Absprung verursacht
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Wenn eine Nutzer:in die App öffnet, nachdem sie eine Benachrichtigung erhalten hat, ohne auf die Benachrichtigung zu klicken
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Wenn eine Nutzer:in eine Push-Benachrichtigung erhält, während die App geöffnet ist. <br><br>Dieses Event wird vom [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) nicht unterstützt und ist im [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) veraltet.
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Wenn eine Nutzer:in eine Push-Benachrichtigung öffnet oder auf einen Push-Benachrichtigungs-Button klickt (einschließlich eines SCHLIESSEN-Buttons, der die App NICHT öffnet). <br><br> Push-Button-Aktionen haben mehrere Ergebnisse. Nein-, Ablehnen- und Abbrechen-Aktionen sind „Klicks", und Akzeptieren-Aktionen sind „Öffnungen". Beide werden in dieser Tabelle dargestellt, können aber in der Spalte **BUTTON_ACTION_TYPE** unterschieden werden. Beispielsweise kann eine Abfrage verwendet werden, um nach einem `BUTTON_ACTION_TYPE` zu gruppieren, der nicht Nein, Ablehnen oder Abbrechen ist.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Wenn wir einer Nutzer:in eine Push-Benachrichtigung senden
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Wenn ein RCS-Versand aufgrund eines innerhalb von Braze erkannten Fehlers unterbrochen wird und die Nachricht verworfen wird
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | Wenn die Endnutzer:in mit einer RCS-Nachricht interagiert, indem sie auf ein UI-Element tippt oder klickt
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | Wenn eine RCS-Nachricht erfolgreich an das Mobilgerät einer Endnutzer:in zugestellt wird
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Wenn Braze eine RCS-Nachricht empfängt, die von der Endnutzer:in stammt
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | Wenn die Endnutzer:in eine RCS-Nachricht auf ihrem Gerät öffnet
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | Wenn eine RCS-Nachricht aufgrund eines Eingriffs des Mobilfunkanbieters nicht zugestellt werden kann
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Wenn eine RCS-Nachricht aus den Braze-Systemen an Last-Mile-Zustellpartner gesendet wird
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Eine ursprünglich geplante SMS-Nachricht wurde aus einem bestimmten Grund abgebrochen.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Wenn eine SMS-Nachricht an den Mobilfunkanbieter gesendet wird
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Wenn eine SMS-Nachricht zugestellt wird
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Wenn Braze die SMS-Nachricht nicht an den SMS-Dienstanbieter zustellen kann
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Wenn eine SMS-Nachricht von einer Nutzer:in empfangen wird
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Wenn eine SMS-Nachricht nicht an eine Nutzer:in zugestellt wird
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Wenn eine SMS-Nachricht gesendet wird
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Wenn eine Nutzer:in auf eine von Braze gekürzte URL in einer SMS-Nachricht klickt
[USERS_MESSAGES_SMS_RETRY_SHARED](#USERS_MESSAGES_SMS_RETRY_SHARED) | Wenn eine SMS-Nachricht nach Depriorisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Eine ursprünglich geplante Webhook-Nachricht wurde aus einem bestimmten Grund abgebrochen
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Wenn eine Webhook-Nachricht zugestellt wird, aber mit einer Fehlerantwort vom Endpunkt fehlschlägt
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Wenn wir einen Webhook für eine Nutzer:in senden
[USERS_MESSAGES_WEBHOOK_RETRY_SHARED](#USERS_MESSAGES_WEBHOOK_RETRY_SHARED) | Wenn eine Webhook-Nachricht nach Depriorisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Eine ursprünglich geplante WhatsApp-Nachricht wurde aus einem bestimmten Grund abgebrochen
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | Wenn eine Nutzer:in auf einen Link oder Button in einer WhatsApp-Nachricht klickt
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) | Wenn eine WhatsApp-Nachricht zugestellt wird
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Wenn eine WhatsApp-Nachricht nicht an eine Nutzer:in zugestellt wird
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Wenn eine WhatsApp-Nachricht von einer Nutzer:in empfangen wird
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Wenn eine Nutzer:in eine WhatsApp-Nachricht öffnet
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Wenn wir eine WhatsApp-Nachricht für eine Nutzer:in senden
[USERS_MESSAGES_WHATSAPP_RETRY_SHARED](#USERS_MESSAGES_WHATSAPP_RETRY_SHARED) | Wenn eine WhatsApp-Nachricht nach Depriorisierung oder Frequency Capping erneut versucht wird (**nur Snowflake Data Sharing**)
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Wenn die zufällige Bucket-Nummer einer Nutzer:in geändert wird
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Wenn eine Nutzer:in auf Anfrage einer Kund:in gelöscht wird
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Wenn eine Nutzer:in mit dem Profil einer anderen Nutzer:in zusammengeführt wird und das ursprüngliche Profil verwaist
[SNAPSHOTS_APP_SHARED](#SNAPSHOTS_APP_SHARED) | App-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED](#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED) | Kampagnen-Nachrichtenvarianten-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_FLOW_STEP_SHARED](#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED) | Canvas-Flow-Schritt-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_STEP_SHARED](#SNAPSHOTS_CANVAS_STEP_SHARED) | Canvas-Schritt-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_CANVAS_VARIATION_SHARED](#SNAPSHOTS_CANVAS_VARIATION_SHARED) | Canvas-Varianten-Snapshots (**nur Snowflake Data Sharing**)
[SNAPSHOTS_EXPERIMENT_STEP_SHARED](#SNAPSHOTS_EXPERIMENT_STEP_SHARED) | Experiment-Schritt-Snapshots (**nur Snowflake Data Sharing**)


## Agent Console {#agent-console}

{% alert note %}
Agent Console-Tabellen sind nur in Snowflake Data Sharing verfügbar.
{% endalert %}

### AGENTCONSOLE_AGENTEXECUTED_SHARED {#AGENTCONSOLE_AGENTEXECUTED_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`invocation_id` | `string` | Globale eindeutige ID für diese Nachricht
`request_id` | `string` | Eindeutige ID für diese gesamte LLM-Anfrage und vollständige Ausführung
`duration` | `int` | Dauer der Sitzung in Sekunden
`prompt_tokens` | `int` | Wie viele Prompt-Token diese Anfrage verbraucht hat
`completion_tokens` | `int` | Wie viele Completion-Token diese Anfrage verbraucht hat
`total_tokens` | `int` | Wie viele Token diese Anfrage insgesamt verbraucht hat
`cache_tokens` | `int` | Wie viele gecachte Token diese Anfrage verbraucht hat
`reasoning_tokens` | `int` | Wie viele Reasoning-Token diese Anfrage verbraucht hat
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`agent_id` | `string` | BSON-ID des CustomerDefinedAgent
`agent_name` | `string` | Name des CustomerDefinedAgent
`model_provider` | `string` | Name des LLM-Modellanbieters
`model_name` | `string` | Name des in dieser Anfrage verwendeten LLM-Modells
`provider_request_id` | `string` | Vom Modellanbieter für den API-Aufruf vergebene Anfrage-ID
`cache_hit` | `boolean` | Ob diese Anfrage den Cache genutzt hat, um die Antwort zurückzugeben
`llm_owned_by_customer` | `boolean` | Wenn true, wurde der API-Schlüssel der Kund:in verwendet; wenn false, wurde der Braze-Schlüssel verwendet
`is_error` | `boolean` | Ob diese Anfrage einen Fehler verursacht hat
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`user_id` | `string` | [PII] Braze-Nutzer-ID der Nutzer:in, die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`input` | `null,`&nbsp;`string` | [PII] Eingabe an das LLM
`output` | `null,`&nbsp;`string` | [PII] Antwort vom LLM
`invocation_source` | `null,`&nbsp;`string` | Welches Ruby-Objekt die LLM-Anfrage ausgelöst hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### AGENTCONSOLE_TOOLINVOCATION_SHARED {#AGENTCONSOLE_TOOLINVOCATION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`tool_call_id` | `string` | Globale eindeutige ID für diesen Tool-Aufruf
`duration` | `int` | Dauer der Sitzung in Sekunden
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`agent_id` | `string` | BSON-ID des CustomerDefinedAgent
`agent_name` | `string` | Name des CustomerDefinedAgent
`is_error` | `boolean` | Ob diese Anfrage einen Fehler verursacht hat
`tool_name` | `string` | Name des Tools
`tool_arguments` | `null,`&nbsp;`string` | [PII] JSON der Tool-Argumente
`invocation_source` | `null,`&nbsp;`string` | Welches Ruby-Objekt die LLM-Anfrage ausgelöst hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Kataloge

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`catalog_id` | `string` | BSON-ID des Katalogs
`item_id` | `string` | BSON-ID des Katalog-Artikels
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe
`field_name` | `null,`&nbsp;`string` | Name des Feldes
`field_value` | `null,`&nbsp;`string` | Wert des Feldes
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Changelogs

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis stattfand
`random_bucket_number` | `null, int` | Neue zufällige Bucket-Nummer
`global_control_group` | `null, boolean` | Mit dieser Änderung wird die Bucket-Nummer als globale Kontrollgruppe einbezogen
`previous_global_control_group` | `null, boolean` | Vor dieser Änderung wurde die Bucket-Nummer als globale Kontrollgruppe einbezogen, was nun nicht mehr der Fall ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### CHANGELOGS_CAMPAIGN_SHARED {#CHANGELOGS_CAMPAIGN_SHARED}

{% alert note %}
Diese Tabelle ist nur in Snowflake Data Sharing verfügbar.
{% endalert %}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`api_id` | `string` | API-ID der Kampagne
`name` | `null,`&nbsp;`string` | Name der Kampagne
`conversion_behaviors` | `null,`&nbsp;`string` | Konversionsverhalten für die Kampagne
`actions` | `null,`&nbsp;`string` | Aktionen für die Kampagne
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### CHANGELOGS_CANVAS_SHARED {#CHANGELOGS_CANVAS_SHARED}

{% alert note %}
Diese Tabelle ist nur in Snowflake Data Sharing verfügbar.
{% endalert %}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`api_id` | `string` | API-ID des Canvas
`name` | `null,`&nbsp;`string` | Name des Canvas
`conversion_behaviors` | `null,`&nbsp;`string` | Konversionsverhalten für das Canvas
`variations` | `null,`&nbsp;`string` | Varianten für das Canvas
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Verhalten

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die das Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Aktion stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in das Event ausgeführt hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das angepasste Event stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`name` | `string` | Name des angepassten Events
`properties` | `string` | Angepasste Eigenschaften des Events, gespeichert als JSON-codierter String
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die die Installation durchgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in die Installation durchgeführt hat
`source` | `string` | Die Quelle der Attribution
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die den Standort aufzeichnet
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieser Standort aufgezeichnet wurde
`time` | `int` | Unix-Zeitstempel, zu dem der Standort aufgezeichnet wurde
`latitude` | `float` | [PII] Breitengrad des aufgezeichneten Standorts
`longitude` | `float` | [PII] Längengrad des aufgezeichneten Standorts
`altitude` | `null, float` | [PII] Höhe des aufgezeichneten Standorts
`ll_accuracy` | `null, float` | Genauigkeit von Breiten- und Längengrad des aufgezeichneten Standorts
`alt_accuracy` | `null, float` | Höhengenauigkeit des aufgezeichneten Standorts
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem der Standort aufgezeichnet wurde
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die bei der Standortaufzeichnung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die einen Kauf getätigt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der der Kauf stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in den Kauf getätigt hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem der Kauf stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Kaufs verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`product_id` | `string` | ID des gekauften Produkts
`price` | `float` | Preis des Kaufs
`currency` | `string` | Währung des Kaufs
`properties` | `string` | Angepasste Eigenschaften des Kaufs, gespeichert als JSON-codierter String
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die die Deinstallation durchgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, die deinstalliert wurde
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in die Deinstallation durchgeführt hat
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die die App upgradet hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, die die Nutzer:in upgradet hat
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in die App upgradet hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Nutzer:in die App upgradet hat
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`old_app_version` | `null,`&nbsp;`string` | Alte Version der App
`new_app_version` | `null,`&nbsp;`string` | Neue Version der App
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die diese Aktion ausführt
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Sitzung stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Sitzung begann
`session_id` | `string` | UUID der Sitzung
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:in
`country` | `null,`&nbsp;`string` | [PII] Land der Nutzer:in
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`language` | `null,`&nbsp;`string` | [PII] Sprache der Nutzer:in
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Sitzung stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während der Sitzung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event stattfand
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die diese Aktion ausführt
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Sitzung stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Sitzung endete
`duration` | `null, float` | Dauer der Sitzung in Sekunden
`session_id` | `string` | UUID der Sitzung
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Sitzung stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während der Sitzung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die diese Aktion ausführt
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Sitzung stattfand
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem die Sitzung begann
`session_id` | `string` | UUID der Sitzung
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem die Sitzung stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während der Sitzung verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die das Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Aktion stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in das Event ausgeführt hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das angepasste Event stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`event_type` | `string` | Welche Art von Geofence-Event ausgelöst wurde (z. B. „enter" oder „exit")
`location_set_id` | `string` | Die ID des Standort-Sets des ausgelösten Geofence
`geofence_id` | `string` | Die ID des ausgelösten Geofence
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der Nutzer:in, die das Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der diese Aktion stattfand
`time` | `int` | Unix-Zeitstempel, zu dem die Nutzer:in das Event ausgeführt hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das angepasste Event stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`event_type` | `string` | Welche Art von Geofence-Event ausgelöst wurde (z. B. „enter" oder „exit")
`location_set_id` | `string` | Die ID des Standort-Sets des ausgelösten Geofence
`geofence_id` | `string` | Die ID des ausgelösten Geofence
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`activity_attributes_type` | `null,`&nbsp;`string` | Live Activity-Attributtyp
`push_to_start_token` | `null,`&nbsp;`string` | Live Activity Push-to-Start-Token
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS-Push-Token, 1 für Entwicklung, 2 für Produktion
`push_token_state_change_type` | `null,`&nbsp;`string` | Eine Beschreibung des Push-Token-Statusänderungstyps
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`activity_id` | `null,`&nbsp;`string` | Live Activity-Bezeichner
`update_token` | `null,`&nbsp;`string` | Live Activity Update-Token
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event stattfand
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS-Push-Token, 1 für Entwicklung, 2 für Produktion
`push_token_state_change_type` | `null,`&nbsp;`string` | Eine Beschreibung des Push-Token-Statusänderungstyps
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`time_ms` | `int` | Zeitpunkt in Millisekunden, zu dem das Event stattfand
`user_id` | `string` | Braze-Nutzer-ID der Nutzer:in, die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID der Nutzer:in
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`push_token` | `null,`&nbsp;`string` | Push-Token des Events
`push_token_created_at` | `null, int` | Unix-Zeitstempel, zu dem das Push-Token erstellt wurde
`push_token_updated_at` | `null, int` | Unix-Zeitstempel, zu dem das Push-Token zuletzt aktualisiert wurde
`push_token_foreground_push_disabled` | `null, boolean` | Flag für deaktivierte Vordergrund-Push-Benachrichtigungen des Push-Tokens
`push_token_device_id` | `null,`&nbsp;`string` | Geräte-ID des Push-Tokens
`push_token_provisionally_opted_in` | `null, boolean` | Flag für vorläufiges Opt-in des Push-Tokens
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS-Push-Token, 1 für Entwicklung, 2 für Produktion
`web_push_token_public_key` | `null,`&nbsp;`string` | Public Key des Push-Tokens, gilt nur für Web-Push-Token
`web_push_token_user_auth` | `null,`&nbsp;`string` | Nutzer-Authentifizierung des Push-Tokens, gilt nur für Web-Push-Token
`web_push_token_vapid_public_key` | `null,`&nbsp;`string` | VAPID Public Key des Push-Tokens, gilt nur für Web-Push-Token
`push_token_state_change_type` | `null,`&nbsp;`string` | Eine Beschreibung des Push-Token-Statusänderungstyps
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der betroffenen Nutzer:in
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse der Nutzer:in
`state_change_source` | `null,`&nbsp;`string` | Quelle der Statusänderung (REST, SDK, Dashboard usw.)
`subscription_status` | `string` | Abo-Status: „Subscribed", „Unsubscribed" oder „Opted In"
`channel` | `null,`&nbsp;`string` | Kanal des globalen Abo-Status, z. B. E-Mail
`time` | `int` | Unix-Zeitstempel, zu dem sich der Abo-Status geändert hat
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, zu der das Event gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, zu der dieses Event gehört
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, von der diese Abo-Statusänderung ausging
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`channel_identifier` | `null,`&nbsp;`string` | [PII] Der Bezeichner der Nutzer:in auf dem Kanal, für den das Event gilt.
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID der betroffenen Nutzer:in
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID der Nutzer:in
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit dieser Nutzer:in verknüpft ist, wenn die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese Nutzer:in gehört
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse der Nutzer:in
`phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer der Nutzer:in im E.164-Format
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, zu der das Event gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, zu der dieses Event gehört
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`channel` | `null,`&nbsp;`string` | Kanal: „email" oder „sms", je nach Kanaltyp der Abo-Gruppe
`subscription_status` | `string` | Abo-Status: „Subscribed", „Unsubscribed" oder „Opted In"
`time` | `int` | Unix-Zeitstempel, zu dem sich der Abo-Status geändert hat
`timezone` | `null,`&nbsp;`string` | Zeitzone der Nutzer:in
`send_id` | `null,`&nbsp;`string` | Nachrichten-Sende-ID, von der diese Abo-Statusänderung ausging
`state_change_source` | `null,`&nbsp;`string` | Quelle der Statusänderung (REST, SDK, Dashboard usw.)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese Nutzer:in gehört
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`channel_identifier` | `null,`&nbsp;`string` | [PII] Der Bezeichner der Nutzer:in auf dem Kanal, für den das Event gilt.
`sf_created_at` | `timestamp`,&nbsp;`null` | Wann dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Kampagnen

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die dieser Benutzer erhalten hat
`conversion_behavior_index` | `null, int` | Index des Konversionsverhaltens
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone des Benutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der dieser Benutzer gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone des Benutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der dieser Benutzer gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die dieser Benutzer erhalten hat
`channel` | `null,`&nbsp;`string` | Kanal, zu dem dieses Event gehört
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone des Benutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der dieser Benutzer gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers
`timezone` | `null,`&nbsp;`string` | Zeitzone des Benutzers
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers
`revenue` | `long` | Betrag des generierten Umsatzes in USD in Cents
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der dieser Benutzer gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Feld                                  | Typ                     | Beschreibung                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Globale eindeutige ID für dieses Event                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID des Nutzers                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                                                                      |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Event gehört        |         
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                                                                 |
| `progression_type`                     | `string`,&nbsp;`null`    | Art des Schrittfolgeereignisses |
| `is_canvas_entry`                      | `boolean`,&nbsp;`null`   | Ob dies der Eingang zu einem ersten Canvas-Schritt ist        |
| `exit_reason`                          | `string`,&nbsp;`null`    | Wenn es sich um einen Exit handelt, der Grund, warum ein:e Nutzer:in während des Schritts den Canvas verlassen hat                  |
| `canvas_entry_id`                      | `string`,&nbsp;`null`    | Eindeutiger Bezeichner für diese Instanz eines Nutzers oder einer Nutzerin in einem Canvas  |
| `next_step_id`                         | `string`,&nbsp;`null`    | BSON ID des nächsten Schritts im Canvas |
| `next_step_api_id`                     | `string`,&nbsp;`null`    | API ID des nächsten Schritts im Canvas |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Feld                                  | Typ                     | Beschreibung                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Globale eindeutige ID für dieses Event                                                                               |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                                                                   |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID des Nutzers                                                                              |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist                                            |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                                                   |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                                                    |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                                                                      |
| `app_api_id`                           | `string`,&nbsp;`null`    | API-ID der App, in der dieses Ereignis aufgetreten ist                                                                  |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört                                                     |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Event gehört                                                                      |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                                                            |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                                                                 |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat                                                  |
| `conversion_behavior_index`            | `int`,&nbsp;`null`       | Art des Konversions-Events, das der oder die Nutzer:in durchgeführt hat, wobei „0" für eine primäre Konversion und „1" für eine sekundäre Konversion steht |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Geschlecht der Nutzer:innen                                                                                        |
| `country`                              | `string`,&nbsp;`null`    | [PII] Land des Nutzers                                                                                       |
| `timezone`                             | `string`,&nbsp;`null`    | Zeitzone des Benutzers                                                                                            |
| `language`                             | `string`,&nbsp;`null`    | [PII] Sprache des Nutzers                                                                                      |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Feld                     | Typ                     | Beschreibung                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID des Nutzers                                   |
| `device_id`               | `string`,&nbsp;`null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                         |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | [Veraltet] API-ID des Canvas-Schritts, zu dem dieses Ereignis gehört         |
| `gender`                  | `string`,&nbsp;`null`    | [PII] Geschlecht der Nutzer:innen                                             |
| `country`                 | `string`,&nbsp;`null`    | [PII] Land des Nutzers                                            |
| `timezone`                | `string`,&nbsp;`null`    | Zeitzone des Benutzers                                                 |
| `language`                | `string`,&nbsp;`null`    | [PII] Sprache des Nutzers                                           |
| `in_control_group`        | `boolean`,&nbsp;`null`   | Wahr, wenn der Benutzer in der Kontrollgruppe eingeschrieben war                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Feld                     | Typ                     | Beschreibung                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID des Nutzers                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                         |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Feld                     | Typ                     | Beschreibung                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID des Nutzers                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `app_group_api_id`        | `string`,&nbsp;`null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                         |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                      |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Feld                       | Typ                     | Beschreibung                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | Globale eindeutige ID für dieses Event                                                                               |
| `user_id`                   | `string`,&nbsp;`null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                                                                   |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] Externe ID des Nutzers                                                                              |
| `app_group_id`              | `string`,&nbsp;`null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                                                   |
| `time`                      | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                                                                      |
| `app_api_id`                | `string`,&nbsp;`null`    | API-ID der App, in der dieses Ereignis aufgetreten ist                                                                  |
| `canvas_id`                 | `string`,&nbsp;`null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört                                                     |
| `canvas_api_id`             | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Event gehört                                                                      |
| `canvas_variation_api_id`   | `string`,&nbsp;`null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                                                            |
| `canvas_step_api_id`        | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                                                                 |
| `experiment_step_api_id`    | `string`,&nbsp;`null`    | API-ID des Experiment-Schrittes, zu dem dieses Ereignis gehört                                                             |
| `conversion_behavior_index` | `int`,&nbsp;`null`       | Art des Konversions-Events, das der oder die Nutzer:in durchgeführt hat, wobei „0" für eine primäre Konversion und „1" für eine sekundäre Konversion steht |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                                                                   |
| `experiment_split_api_id` | `string`,&nbsp;`null` | API-ID des Experiment-Splits, in den der oder die Nutzer:in eingeschrieben wurde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Feld                     | Typ                     | Beschreibung                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`,&nbsp;`null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                 | `string`,&nbsp;`null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`        | `string`,&nbsp;`null`    | [PII] Externe ID des Nutzers                                   |
| `app_group_id`            | `string`,&nbsp;`null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `time`                    | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`               | `string`,&nbsp;`null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`           | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`      | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                      |
| `experiment_step_api_id`  | `string`,&nbsp;`null`    | API-ID des Experiment-Schrittes, zu dem dieses Ereignis gehört                  |
| `in_control_group`        | `boolean`,&nbsp;`null`   | Wahr, wenn der Benutzer in der Kontrollgruppe eingeschrieben war                   |
| `sf_created_at`           | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |

| `experiment_split_api_id` | `string`,&nbsp;`null` | API-ID des Experiment-Splits, in den der oder die Nutzer:in eingeschrieben wurde |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Feld                                  | Typ                     | Beschreibung                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID des Nutzers                                   |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                         |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat       |
| `channel`                              | `string`,&nbsp;`null`    | Messaging-Kanal, zu dem dieses Event gehört (E-Mail, Push, etc.)          |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Geschlecht der Nutzer:innen                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] Land des Nutzers                                            |
| `timezone`                             | `string`,&nbsp;`null`    | Zeitzone des Benutzers                                                 |
| `language`                             | `string`,&nbsp;`null`    | [PII] Sprache des Nutzers                                           |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Feld                                  | Typ                     | Beschreibung                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`,&nbsp;`null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                              | `string`,&nbsp;`null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`                     | `string`,&nbsp;`null`    | [PII] Externe ID des Nutzers                                   |
| `device_id`                            | `string`,&nbsp;`null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist |
| `app_group_id`                         | `string`,&nbsp;`null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `app_group_api_id`                     | `string`,&nbsp;`null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                         |
| `time`                                 | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`                            | `string`,&nbsp;`null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`                        | `string`,&nbsp;`null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id`              | `string`,&nbsp;`null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`                   | `string`,&nbsp;`null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                      |
| `canvas_step_message_variation_api_id` | `string`,&nbsp;`null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat       |
| `gender`                               | `string`,&nbsp;`null`    | [PII] Geschlecht der Nutzer:innen                                             |
| `country`                              | `string`,&nbsp;`null`    | [PII] Land des Nutzers                                            |
| `timezone`                             | `string`,&nbsp;`null`    | Zeitzone des Benutzers                                                 |
| `language`                             | `string`,&nbsp;`null`    | [PII] Sprache des Nutzers                                           |
| `revenue`                              | `int`,&nbsp;`null`       | Betrag des generierten Umsatzes in USD, angezeigt in Cents               |
| `sf_created_at`                        | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |
| `app_api_id` | `string`,&nbsp;`null` | API-ID der App, in der dieses Ereignis aufgetreten ist |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Nachrichten


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Geräte-Browser – aus dem User-Agent extrahiert – in dem die Öffnung stattfand
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (bis zu 128 Zeichen)
`banner_placement_id` | `null,`&nbsp;`string` | Vom Kunden festgelegte Banner-Platzierungs-ID
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Geräte-Browser – aus dem User-Agent extrahiert – in dem die Öffnung stattfand
`button_id` | `null,`&nbsp;`string` | ID des angeklickten Buttons, falls dieser Klick einen Button-Klick darstellt
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`banner_placement_id` | `null,`&nbsp;`string` | Vom Kunden festgelegte Banner-Platzierungs-ID
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Geräte-Browser – aus dem User-Agent extrahiert – in dem die Öffnung stattfand
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`banner_placement_id` | `null,`&nbsp;`string` | Vom Kunden festgelegte Banner-Platzierungs-ID
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`content_card_id` | `string` | ID der Karte, die dieses Event erzeugt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`content_card_id` | `string` | ID der Karte, die dieses Event erzeugt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`content_card_id` | `string` | ID der Karte, die dieses Event erzeugt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`content_card_id` | `string` | ID der Karte, die dieses Event erzeugt hat
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`email_address` | `string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`email_address` | `string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der der E-Mail-Versand erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`bounce_reason` | `null,`&nbsp;`string` | [PII] Der SMTP-Antwortcode und die benutzerfreundliche Nachricht für dieses Absprung-Event
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Event (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`is_drop` | `null, boolean` | Gibt an, dass dieses Event als Drop-Event zählt
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`email_address` | `string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`url` | `null,`&nbsp;`string` | URL, auf die der/die Nutzer:in geklickt hat
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem der Klick stattfand
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`link_id` | `null,`&nbsp;`string` | Eindeutige ID für den angeklickten Link, erstellt von Braze
`link_alias` | `null,`&nbsp;`string` | Alias, der mit dieser Link-ID verknüpft ist
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Event (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`is_amp` | `null, boolean` | Gibt an, dass es sich um ein AMP-Event handelt
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Event als Bot-Event verarbeitet wurde
`suspected_bot_click_reason` | `null, object` | Warum dieses Event als Bot klassifiziert wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`recipient_domain` | `null,`&nbsp;`string` | E-Mail-Domain des Empfängers bzw. der Empfängerin
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Event (Sparkpost, Sendgrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der der E-Mail-Versand erfolgte
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`deferral_reason` | `null,`&nbsp;`string` | [PII] Der SMTP-Antwortcode und die benutzerfreundliche Nachricht für dieses Verzögerungs-Event
`attempt_count` | `null, int` | Anzahl der Zustellversuche für die Nachricht
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`email_address` | `string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der die E-Mail gesendet wurde
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Event (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`email_address` | `string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem der Spam-Bericht erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Event (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`email_address` | `string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem die Öffnung stattfand
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`machine_open` | `null,`&nbsp;`string` | Wird auf 'true' gesetzt, wenn das Öffnungs-Event ohne Nutzerinteraktion ausgelöst wird, z. B. durch ein Apple-Gerät mit aktiviertem E-Mail-Datenschutz. Der Wert kann sich im Laufe der Zeit ändern, um mehr Granularität zu bieten.
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Event (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`is_amp` | `null, boolean` | Gibt an, dass es sich um ein AMP-Event handelt
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`email_address` | `string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Event (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`email_address` | `string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`sending_ip` | `null,`&nbsp;`string` | IP-Adresse, von der der E-Mail-Versand erfolgte
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`bounce_reason` | `null,`&nbsp;`string` | [PII] Der SMTP-Antwortcode und die benutzerfreundliche Nachricht für dieses Absprung-Event
`esp` | `null,`&nbsp;`string` | ESP im Zusammenhang mit dem Event (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,`&nbsp;`string` | Absender-Domain für die E-Mail
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`email_address` | `string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_RETRY_SHARED {#USERS_MESSAGES_EMAIL_RETRY_SHARED}

{% alert note %}
Diese Tabelle ist nur im Snowflake Data Sharing verfügbar.
{% endalert %}

Dieses Event tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und später innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | [PII] Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`retry_type` | `null,`&nbsp;`string` | Art der Wiederholung
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zur Wiederholung
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`email_address` | `null,`&nbsp;`string` | [PII] E-Mail-Adresse des Nutzers bzw. der Nutzerin
`ip_pool` | `null,`&nbsp;`string` | IP-Pool, über den der E-Mail-Versand erfolgte
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`feature_flag_id_name` | `null,`&nbsp;`string` | Der Feature-Flag-Rollout-Bezeichner
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`browser` | `null,`&nbsp;`string` | Geräte-Browser – aus dem User-Agent extrahiert – in dem die Öffnung stattfand
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Karte
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`version` | `string` | Version der In-App-Nachricht, Legacy oder getriggert
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Karte
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`version` | `string` | Version der In-App-Nachricht, Legacy oder getriggert
`button_id` | `null,`&nbsp;`string` | ID des angeklickten Buttons, falls dieser Klick einen Button-Klick darstellt
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Karte
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`version` | `string` | Version der In-App-Nachricht, Legacy oder getriggert
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-Bezeichner
`ad_id_type` | `null,`&nbsp;`string` | Einer von `ios_idfa`, `google_ad_id`, `windows_ad_id` ODER `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob Werbe-Tracking für das Gerät aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`locale_key` | `null,`&nbsp;`string` | [PII] Der Schlüssel, der den Übersetzungen entspricht (z. B. 'en-us'), die zum Erstellen dieser Nachricht verwendet wurden (null für Standard).
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (bis zu 128 Zeichen)
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID des Nutzers bzw. der Nutzerin, von der die Nachricht gesendet oder empfangen wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID des Nutzers bzw. der Nutzerin, von der die Nachricht gesendet oder empfangen wurde
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Event als Bot-Event verarbeitet wurde
`short_url` | `null,`&nbsp;`string` | Gekürzte URL, die angeklickt wurde
`url` | `null,`&nbsp;`string` | URL, auf die der/die Nutzer:in geklickt hat
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem der Spam-Bericht erfolgte
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`media_id` | `null,`&nbsp;`string` | Die von LINE generierte ID, die zum Abrufen eingehender Medien von LINE verwendet werden kann
`message_body` | `null,`&nbsp;`string` | Getippte Antwort des Nutzers bzw. der Nutzerin
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID des Nutzers bzw. der Nutzerin, von der die Nachricht gesendet oder empfangen wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID des Nutzers bzw. der Nutzerin, von der die Nachricht gesendet oder empfangen wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_LINE_RETRY_SHARED {#USERS_MESSAGES_LINE_RETRY_SHARED}

{% alert note %}
Diese Tabelle ist nur im Snowflake Data Sharing verfügbar.
{% endalert %}

Dieses Event tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und später innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | [PII] Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`retry_type` | `null,`&nbsp;`string` | Art der Wiederholung
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zur Wiederholung
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`line_channel_id` | `null,`&nbsp;`string` | Die LINE-Kanal-ID, an die die Nachricht gesendet oder von der sie empfangen wurde
`line_channel_name` | `null,`&nbsp;`string` | Der LINE-Kanalname, an den die Nachricht gesendet oder von dem sie empfangen wurde
`native_line_id` | `null,`&nbsp;`string` | [PII] Die LINE-ID des Nutzers bzw. der Nutzerin, von der die Nachricht gesendet oder empfangen wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`activity_id` | `null,`&nbsp;`string` | Live-Activity-Bezeichner
`activity_attributes_type` | `null,`&nbsp;`string` | Live-Activity-Attributtyp
`push_to_start_token` | `null,`&nbsp;`string` | Live-Activity-Push-to-Start-Token
`update_token` | `null,`&nbsp;`string` | Live-Activity-Update-Token
`live_activity_event_type` | `null,`&nbsp;`string` | Event-Typ der Live Activity. Einer von ['start', 'update', 'end']
`live_activity_event_outcome` | `null,`&nbsp;`string` | Ergebnis des Live-Activity-Events
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`activity_id` | `null,`&nbsp;`string` | Live-Activity-Bezeichner
`activity_attributes_type` | `null,`&nbsp;`string` | Live-Activity-Attributtyp
`push_to_start_token` | `null,`&nbsp;`string` | Live-Activity-Push-to-Start-Token
`update_token` | `null,`&nbsp;`string` | Live-Activity-Update-Token
`live_activity_event_type` | `null,`&nbsp;`string` | Event-Typ der Live Activity. Einer von ['start', 'update', 'end']
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Karte
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Geräte-Browser – aus dem User-Agent extrahiert – in dem die Öffnung stattfand
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (bis zu 128 Zeichen)
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Karte
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Geräte-Browser – aus dem User-Agent extrahiert – in dem die Öffnung stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`card_api_id` | `null,`&nbsp;`string` | API-ID der Karte
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Geräte-Browser – aus dem User-Agent extrahiert – in dem die Öffnung stattfand
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, an die ein Zustellversuch unternommen wurde
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`platform` | `string` | Plattform des Geräts
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`push_token` | `null,`&nbsp;`string` | Push-Token, das abgesprungen ist
`device_id` | `null,`&nbsp;`string` | `device_id`, an die ein Zustellversuch unternommen wurde, der abgesprungen ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
Dieses Event wird vom [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) nicht unterstützt und ist im [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) veraltet.
{% endalert %}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,`&nbsp;`string` | Version des Braze SDK, die während des Events verwendet wurde
`platform` | `null,`&nbsp;`string` | Plattform des Geräts
`os_version` | `null,`&nbsp;`string` | Version des Betriebssystems des Geräts
`device_model` | `null,`&nbsp;`string` | Modell des Geräts
`resolution` | `null,`&nbsp;`string` | Auflösung des Geräts
`carrier` | `null,`&nbsp;`string` | Mobilfunkanbieter des Geräts
`browser` | `null,`&nbsp;`string` | Browser des Geräts
`button_string` | `null,`&nbsp;`string` | Bezeichner (button_string) des angeklickten Push-Benachrichtigungs-Buttons. null, wenn nicht von einem Button-Klick
`button_action_type` | `null,`&nbsp;`string` | Aktionstyp des Push-Benachrichtigungs-Buttons. Einer von [URI, DEEP_LINK, NONE, CLOSE]. null, wenn nicht von einem Button-Klick
`slide_id` | `null,`&nbsp;`string` | Slide-Bezeichner des Push-Karussell-Slides, auf den der/die Nutzer:in geklickt hat
`slide_action_type` | `null,`&nbsp;`string` | Aktionstyp des Push-Karussell-Slides
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`push_token` | `null,`&nbsp;`string` | Push-Token, an das ein Zustellversuch unternommen wurde
`device_id` | `null,`&nbsp;`string` | `device_id`, an die ein Zustellversuch unternommen wurde
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`app_api_id` | `null,`&nbsp;`string` | API-ID der App, in der dieses Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`platform` | `string` | Plattform des Geräts
`ad_id` | `null,`&nbsp;`string` | [PII] Werbe-ID des Geräts, an das ein Zustellversuch unternommen wurde
`ad_id_type` | `null,`&nbsp;`string` | Typ der Werbe-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`is_sampled` | `null,`&nbsp;`string` | Gibt an, ob der Push-Versand gesampelt wurde und ein Zustellungs-Event erwartet wurde
`locale_key` | `null,`&nbsp;`string` | [PII] Der Schlüssel, der den Übersetzungen entspricht (z. B. 'en-us'), die zum Erstellen dieser Nachricht verwendet wurden (null für Standard).
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (bis zu 128 Zeichen)
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`is_suspected_bot_click` | `null, boolean` | Ob dieses Event als Bot-Event verarbeitet wurde
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`short_url` | `null,`&nbsp;`string` | Gekürzte URL, die angeklickt wurde
`suspected_bot_click_reason` | `null,`&nbsp;`string` | Warum dieses Event als Bot klassifiziert wurde
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem der Spam-Bericht erfolgte
`user_phone_number` | `null,`&nbsp;`string` | [PII] Die Telefonnummer des Nutzers bzw. der Nutzerin, von der die Nachricht empfangen wurde
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`interaction_type` | `null,`&nbsp;`string` | Der Interaktionstyp, der den Klick ausgelöst hat. Beispiel-String-Werte: Text URL, Reply, OpenURL
`element_label` | `null,`&nbsp;`string` | Optionale Details zum angeklickten Element, z. B. der Text einer vorgeschlagenen Antwort oder eines Buttons
`element_type` | `null,`&nbsp;`string` | Gibt an, ob ein interaction_type, der bei Vorschlägen und Buttons gleich ist, von einem Vorschlag oder Button stammt. Beispiele: Suggestion, Button
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`url` | `null,`&nbsp;`string` | URL, auf die der/die Nutzer:in geklickt hat
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin im E.164-Format (z. B. +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`from_rcs_sender` | `null,`&nbsp;`string` | Die RCS-Sender-ID oder der Agentenname, der zum Senden der Nachricht verwendet wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`action` | `null,`&nbsp;`string` | Aktion, die als Reaktion auf diese Nachricht ausgeführt wurde. (z. B. Subscribed, Unsubscribed oder None).
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`media_urls` | `null,`&nbsp;`string` | Medien-URLs des Nutzers bzw. der Nutzerin
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`user_phone_number` | `null,`&nbsp;`string` | [PII] Die Telefonnummer des Nutzers bzw. der Nutzerin, von der die Nachricht empfangen wurde
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`message_body` | `null,`&nbsp;`string` | Getippte Antwort des Nutzers bzw. der Nutzerin
`to_rcs_sender` | `null,`&nbsp;`string` | Der eingehende RCS-Sender, an den die Nachricht gesendet wurde
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin im E.164-Format (z. B. +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`error` | `null,`&nbsp;`string` | Fehlername
`from_rcs_sender` | `null,`&nbsp;`string` | Die RCS-Sender-ID oder der Agentenname, der zum Senden der Nachricht verwendet wurde
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Verknüpft mit dem SMS-Zustellungs-Event
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode des Anbieters
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin im E.164-Format (z. B. +14155552671)
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`category` | `null,`&nbsp;`string` | Name der Keyword-Kategorie, nur für automatische Antwortnachrichten befüllt: 'opt-in', 'opt-out', 'help' oder benutzerdefinierter Wert
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`from_rcs_sender` | `null,`&nbsp;`string` | Die RCS-Sender-ID oder der Agentenname, der zum Senden der Nachricht verwendet wurde
`message_extras` | `null,`&nbsp;`string` | Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin im E.164-Format (z. B. +14155552671)
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die SMS gesendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die SMS gesendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Verknüpft mit dem SMS-Zustellungs-Event
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`error` | `null,`&nbsp;`string` | Fehlername
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode des SMS-Dienstanbieters
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Verknüpft mit dem SMS-Zustellungs-Event
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `null,`&nbsp;`string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, der mit der eingehenden Telefonnummer verknüpft ist
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`user_phone_number` | `string` | [PII] Die Telefonnummer des Nutzers bzw. der Nutzerin, von der die Nachricht empfangen wurde
`subscription_group_id` | `null,`&nbsp;`string` | ID der Abo-Gruppe, die für diese SMS-Nachricht angesprochen wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe, die für diese SMS-Nachricht angesprochen wurde
`inbound_phone_number` | `string` | Die eingehende Nummer, an die die Nachricht gesendet wurde
`action` | `string` | Aktion, die als Reaktion auf diese Nachricht ausgeführt wurde. Zum Beispiel `Subscribed`, `Unsubscribed` oder `None`.
`message_body` | `string` | Antwort des Nutzers bzw. der Nutzerin
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | Medien-URLs des Nutzers bzw. der Nutzerin
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, zu der dieses Event gehört
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, zu der dieses Event gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die SMS gesendet wurde
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`error` | `null,`&nbsp;`string` | Fehlername
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode des SMS-Dienstanbieters
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_sms_fallback` | `null, boolean` | Gibt an, ob ein SMS-Fallback für diese abgelehnte RCS-Nachricht versucht wurde. Verknüpft mit dem SMS-Zustellungs-Event
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin
`subscription_group_api_id` | `null,`&nbsp;`string` | Externe ID der Abo-Gruppe
`category` | `null,`&nbsp;`string` | Name der Keyword-Kategorie, nur für automatische Antwortnachrichten befüllt: 'Opt-in', 'Opt-out', 'Help' oder benutzerdefinierter Wert
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `null,`&nbsp;`string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die von short_url angesprochen wurde, null wenn short_url kein Nutzer-Klick-Tracking verwendet hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin, der/die von short_url angesprochen wurde, falls vorhanden, null wenn short_url kein Nutzer-Klick-Tracking verwendet hat
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, der zur Generierung von short_url verwendet wurde
`time` | `int` | Unix-Zeitstempel, zu dem short_url angeklickt wurde
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`campaign_id` | `null,`&nbsp;`string` | Braze-ID der Kampagne, für die short_url generiert wurde, null wenn nicht aus einer Kampagne
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, für die short_url generiert wurde, null wenn nicht aus einer Kampagne
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, für die short_url generiert wurde, null wenn nicht aus einer Kampagne
`canvas_id` | `null,`&nbsp;`string` | Braze-ID des Canvas, für den short_url generiert wurde, null wenn nicht aus einem Canvas
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, für den short_url generiert wurde, null wenn nicht aus einem Canvas
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, für die short_url generiert wurde, null wenn nicht aus einem Canvas
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, für den short_url generiert wurde, null wenn nicht aus einem Canvas
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, für die short_url generiert wurde, null wenn nicht aus einem Canvas
`url` | `string` | Ursprüngliche URL in der Nachricht, auf die short_url weiterleitet
`short_url` | `string` | Gekürzte URL, die angeklickt wurde
`user_agent` | `null,`&nbsp;`string` | User-Agent, der short_url angefordert hat
`user_phone_number` | `string` | [PII] Die Telefonnummer des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Event als Bot-Event verarbeitet wurde
`suspected_bot_click_reason` | `null, object` | Warum dieses Event als Bot klassifiziert wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_RETRY_SHARED {#USERS_MESSAGES_SMS_RETRY_SHARED}

{% alert note %}
Diese Tabelle ist nur im Snowflake Data Sharing verfügbar.
{% endalert %}

Dieses Event tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und später innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | [PII] Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe
`retry_type` | `null,`&nbsp;`string` | Art der Wiederholung
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zur Wiederholung
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`http_status_code` | `null, int` | HTTP-Statuscode der Antwort
`endpoint_url` | `null,`&nbsp;`string` | Die angeforderte Endpunkt-URL
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`content_length` | `null, int` | Inhaltslänge der Antwort
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`host` | `null,`&nbsp;`string` | Der Host für die Anfrage
`id` | `string` | Global eindeutige ID für dieses Event
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`raw_response` | `null,`&nbsp;`string` | Gekürzte Rohantwort vom Endpunkt
`retry_count` | `null, int` | Anzahl der durchgeführten Wiederholungsversuche
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`url_path` | `null,`&nbsp;`string` | Der Pfad der angeforderten URL
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`webhook_duration` | `null, int` | Gesamtdauer dieser Anfrage in Millisekunden
`webhook_failure_source` | `null,`&nbsp;`string` | Gibt an, ob ein Fehler von Braze oder vom Endpunkt selbst verursacht wurde. Das Quellfeld kann „External Endpoint", „Treat no status code to host unreachable" sein
`is_terminal` | `null, boolean` | Ob dieses Event der letzte Versuch bei einem Versand war
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`campaign_name` | `null,`&nbsp;`string` | Name der Kampagne
`message_variation_name` | `null,`&nbsp;`string` | Name der Nachrichtenvariante
`canvas_name` | `null,`&nbsp;`string` | Name des Canvas
`canvas_variation_name` | `null,`&nbsp;`string` | Name der Canvas-Variante, die diese:r Nutzer:in erhalten hat
`canvas_step_name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_RETRY_SHARED {#USERS_MESSAGES_WEBHOOK_RETRY_SHARED}

{% alert note %}
Diese Tabelle ist nur im Snowflake Data Sharing verfügbar.
{% endalert %}

Dieses Event tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und später innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | [PII] Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`gender` | `null,`&nbsp;`string` | [PII] Geschlecht des Nutzers bzw. der Nutzerin
`country` | `null,`&nbsp;`string` | [PII] Land des Nutzers bzw. der Nutzerin
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`language` | `null,`&nbsp;`string` | [PII] Sprache des Nutzers bzw. der Nutzerin
`retry_type` | `null,`&nbsp;`string` | Art der Wiederholung
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zur Wiederholung
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`to_phone_number` | 	`null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`abort_type` | `null,`&nbsp;`string` | Art des Abbruchs, einer von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,`&nbsp;`string` | [PII] Protokollnachricht mit Abbruchdetails (maximal 2.000 Zeichen)
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`url` | `null,`&nbsp;`string` | URL, auf die der/die Nutzer:in geklickt hat
`short_url` | `null,`&nbsp;`string` | Gekürzte URL, die angeklickt wurde
`user_agent` | `null,`&nbsp;`string` | User-Agent, auf dem der Spam-Bericht erfolgte
`user_phone_number` | `null,`&nbsp;`string` | [PII] Die Telefonnummer des Nutzers bzw. der Nutzerin, von der die Nachricht empfangen wurde
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn der/die Nutzer:in auf einen WhatsApp Flow antwortet.
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`message_id` | `null,`&nbsp;`string` | Die von Meta generierte eindeutige ID für diese Nachricht
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`provider_error_code` | `null,`&nbsp;`string` | Fehlercode von WhatsApp
`provider_error_title` | `null, `&nbsp;`string` | Fehlertitel von WhatsApp
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`message_id` | `null,`&nbsp;`string` | Die von Meta generierte eindeutige ID für diese Nachricht
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn der/die Nutzer:in auf einen WhatsApp Flow antwortet.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`user_phone_number` | `string` | [PII] Die Telefonnummer des Nutzers bzw. der Nutzerin, von der die Nachricht empfangen wurde
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`inbound_phone_number` | `string` | Die eingehende Nummer, an die die Nachricht gesendet wurde
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`message_body` | `string` | Antwort des Nutzers bzw. der Nutzerin
`quick_reply_text` | `string` | Text des Buttons, den der/die Nutzer:in gedrückt hat
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | Medien-URLs des Nutzers bzw. der Nutzerin
`action` | `string` | Aktion, die als Reaktion auf diese Nachricht ausgeführt wurde. Zum Beispiel `Subscribed`, `Unsubscribed` oder `None`.
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`catalog_id` | `null,`&nbsp;`string` | Katalog-ID eines Produkts, wenn ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls leer.
`product_id` | `null,`&nbsp;`string` | ID des gekauften Produkts
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn der/die Nutzer:in auf einen WhatsApp Flow antwortet.
`flow_response_json` | `null,`&nbsp;`string` | [PII] Die Formularwerte, mit denen der/die Nutzer:in geantwortet hat. Vorhanden, wenn der/die Nutzer:in auf einen WhatsApp Flow antwortet.
`message_id` | `null,`&nbsp;`string` | Die von Meta generierte eindeutige ID für diese Nachricht
`in_reply_to` | `null,`&nbsp;`string` | Die message_id der Nachricht, auf die diese Nachricht geantwortet hat
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`message_id` | `null,`&nbsp;`string` | Die von Meta generierte eindeutige ID für diese Nachricht
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn der/die Nutzer:in auf einen WhatsApp Flow antwortet.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Event stattfand
`to_phone_number` | `null,`&nbsp;`string`	| [PII] Telefonnummer des Empfängers bzw. der Empfängerin
`user_id` | `string` | Braze-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe Nutzer-ID des Nutzers bzw. der Nutzerin
`device_id` | `null,`&nbsp;`string` | `device_id`, die mit diesem/dieser Nutzer:in verknüpft ist, wenn der/die Nutzer:in anonym ist
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`from_phone_number` | `null,`&nbsp;`string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,`&nbsp;`string` | ID des Workspace, zu dem diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID des Workspace, zu dem diese:r Nutzer:in gehört
`subscription_group_api_id` | `string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | Interne Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`message_extras` | `null,`&nbsp;`string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während des Liquid-Renderings
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
`send_id` | `null,`&nbsp;`string` | Nachrichtenversand-ID, zu der diese Nachricht gehört
`flow_id` | `null,`&nbsp;`string` | Die eindeutige ID des Flows im WhatsApp Manager. Vorhanden, wenn der/die Nutzer:in auf einen WhatsApp Flow antwortet.
`template_name` | `null,`&nbsp;`string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn eine Template-Nachricht gesendet wird
`message_id` | `null,`&nbsp;`string` | Die von Meta generierte eindeutige ID für diese Nachricht
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_RETRY_SHARED {#USERS_MESSAGES_WHATSAPP_RETRY_SHARED}

{% alert note %}
Diese Tabelle ist nur im Snowflake Data Sharing verfügbar.
{% endalert %}

Dieses Event tritt auf, wenn eine Nachricht herabgestuft oder durch Frequency Capping begrenzt wird und später innerhalb des konfigurierten Wiederholungsfensters erneut versucht wird.

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`user_id` | `string` | [PII] Braze Nutzer-ID des Nutzers bzw. der Nutzerin, der/die dieses Event ausgeführt hat
`external_user_id` | `null,`&nbsp;`string` | [PII] Externe ID des Nutzers bzw. der Nutzerin
`app_group_id` | `null,`&nbsp;`string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`app_group_api_id` | `null,`&nbsp;`string` | API-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattfand
`to_phone_number` | `null,`&nbsp;`string` | [PII] Telefonnummer des Empfängers bzw. der Empfängerin im E.164-Format
`device_id` | `null,`&nbsp;`string` | ID des Geräts, auf dem das Event aufgetreten ist
`timezone` | `null,`&nbsp;`string` | Zeitzone des Nutzers bzw. der Nutzerin
`subscription_group_api_id` | `null,`&nbsp;`string` | API-ID der Abo-Gruppe
`campaign_id` | `null,`&nbsp;`string` | BSON-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,`&nbsp;`string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`canvas_id` | `null,`&nbsp;`string` | BSON-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,`&nbsp;`string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Variante, zu der dieses Event gehört
`canvas_step_api_id` | `null,`&nbsp;`string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,`&nbsp;`string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die diese:r Nutzer:in erhalten hat
`dispatch_id` | `null,`&nbsp;`string` | ID des Versands, zu dem diese Nachricht gehört
`retry_type` | `null,`&nbsp;`string` | Art der Wiederholung
`retry_log` | `null,`&nbsp;`string` | Protokollnachricht mit Details zur Wiederholung
`sf_created_at` | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Nutzer:innen

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Feld                        | Typ                      | Beschreibung                                                          |
| --------------------------- | ------------------------ | --------------------------------------------------------------------- |
| `id`                        | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Event                                 |
| `app_group_id`              | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört               |
| `app_group_api_id`          | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                 |
| `user_id`                   | `string`,&nbsp;`null`    | Braze-ID der/des Nutzer:in, die/der dieses Event ausgeführt hat       |
| `external_user_id`          | `string`,&nbsp;`null`    | [PII] Externe Nutzer-ID der/des Nutzer:in                             |
| `time`                      | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem das Event stattgefunden hat                  |
| `random_bucket_number`      | `int`,&nbsp;`null`       | Aktuelle zufällige Bucket-Nummer, die der/dem Nutzer:in zugewiesen ist |
| `prev_random_bucket_number` | `int`,&nbsp;`null`       | Vorherige zufällige Bucket-Nummer, die der/dem Nutzer:in zugewiesen war |
| `sf_created_at`             | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Feld               | Typ                      | Beschreibung                                                                    |
| ------------------ | ------------------------ | ------------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Event                                           |
| `user_id`          | `string`,&nbsp;`null`    | Braze-ID der/des Nutzer:in, die/der gelöscht wurde                              |
| `app_group_id`     | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                         |
| `app_group_api_id` | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                           |
| `time`             | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem die Löschanfrage für die/den Nutzer:in verarbeitet wurde |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Feld               | Typ                      | Beschreibung                                                                                          |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------------------------------- |
| `id`               | `string`,&nbsp;`null`    | Global eindeutige ID für dieses Event                                                                 |
| `user_id`          | `string`,&nbsp;`null`    | Braze-ID der/des verwaisten Nutzer:in                                                                 |
| `external_user_id` | `string`,&nbsp;`null`    | [PII] Externe Nutzer-ID der/des Nutzer:in                                                             |
| `device_id`        | `string`,&nbsp;`null`    | ID des Geräts, das mit dieser/diesem Nutzer:in verknüpft ist, falls die/der Nutzer:in anonym ist      |
| `app_group_id`     | `string`,&nbsp;`null`    | Braze-ID des Workspace, zu dem diese:r Nutzer:in gehört                                               |
| `app_group_api_id` | `string`,&nbsp;`null`    | API-ID des Workspace, zu dem diese:r Nutzer:in gehört                                                 |
| `app_api_id`       | `string`,&nbsp;`null`    | API-ID der App, zu der die/der verwaiste Nutzer:in gehörte                                            |
| `time`             | `int`,&nbsp;`null`       | Unix-Zeitstempel, zu dem die/der Nutzer:in verwaist wurde                                             |
| `orphaned_by_id`   | `string`,&nbsp;`null`    | Braze-ID der/des Nutzer:in, deren/dessen Profil mit dem Profil der/des verwaisten Nutzer:in zusammengeführt wurde |
| `sf_created_at`    | `timestamp`,&nbsp;`null` | Zeitpunkt, zu dem dieses Event von der Snowpipe erfasst wurde                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Snapshots {#snapshots}

{% alert note %}
Snapshot-Tabellen sind nur in Snowflake Data Sharing verfügbar.
{% endalert %}

### SNAPSHOTS_APP_SHARED {#SNAPSHOTS_APP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID der App
`name` | `null,`&nbsp;`string` | Name der App
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED {#SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID der Kampagnen-Nachrichtenvariante
`name` | `null,`&nbsp;`string` | Name der Kampagnen-Nachrichtenvariante
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED {#SNAPSHOTS_CANVAS_FLOW_STEP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`type` | `null,`&nbsp;`string` | Typ des Canvas-Flow-Schritts
`api_step_id` | `string` | API-ID des Canvas-Schritts
`experiment_splits` | `null,`&nbsp;`string` | Experiment-Aufteilungen für den Schritt
`conversion_behaviors` | `null,`&nbsp;`string` | Konversionsverhalten für den Schritt
`name` | `null,`&nbsp;`string` | Name des Canvas-Flow-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_STEP_SHARED {#SNAPSHOTS_CANVAS_STEP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID des Canvas-Schritts
`name` | `null,`&nbsp;`string` | Name des Canvas-Schritts
`actions` | `null,`&nbsp;`string` | Aktionen für den Canvas-Schritt
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_CANVAS_VARIATION_SHARED {#SNAPSHOTS_CANVAS_VARIATION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`api_id` | `string` | API-ID der Canvas-Variante
`name` | `null,`&nbsp;`string` | Name der Canvas-Variante
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### SNAPSHOTS_EXPERIMENT_STEP_SHARED {#SNAPSHOTS_EXPERIMENT_STEP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Global eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Event stattgefunden hat
`app_group_id` | `string` | BSON-ID der App-Gruppe, zu der diese:r Nutzer:in gehört
`type` | `null,`&nbsp;`string` | Typ des Experiment-Schritts
`api_step_id` | `string` | API-ID des Experiment-Schritts
`experiment_splits` | `null,`&nbsp;`string` | Experiment-Aufteilungen für den Schritt
`conversion_behaviors` | `null,`&nbsp;`string` | Konversionsverhalten für den Schritt
`name` | `null,`&nbsp;`string` | Name des Experiment-Schritts
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }