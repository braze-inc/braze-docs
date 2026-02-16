---
nav_title: "SQL-Tabellenreferenz"
article_title: SQL-Tabellen-Referenz
page_order: 3
page_type: reference
toc_headers: h2
description: "Dieser Artikel enthält Tabellen und Spalten, die im Abfrage-Builder oder bei der Erstellung von SQL-Segmenterweiterungen abgefragt werden können."
tool: Segments
---

<style>
table td {
   word-break: keep-all;
}
</style>

# SQL-Tabellenreferenz

Diese Seite ist eine Referenz der Tabellen und Spalten, die im [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) oder bei der Erstellung von [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) abgefragt werden können. 

## Inhaltsverzeichnis

Tabelle | Beschreibung
------|------------
[CATALOGS_ITEMS_SHARED](#CATALOGS_ITEMS_SHARED) | Nicht gelöschte Artikel im Katalog
[CHANGELOGS_GLOBALCONTROLGROUP_SHARED](#CHANGELOGS_GLOBALCONTROLGROUP_SHARED) | Wenn die globale Kontrollgruppe geändert wird
[USERS_BEHAVIORS_CUSTOMEVENT_SHARED](#USERS_BEHAVIORS_CUSTOMEVENT_SHARED) | Wenn ein Benutzer ein benutzerdefiniertes Ereignis ausführt
[USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED](#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED) | Wenn ein Benutzer eine App installiert und wir sie einem Partner zuordnen
[USERS_BEHAVIORS_LOCATION_SHARED](#USERS_BEHAVIORS_LOCATION_SHARED) | Wenn ein:e Nutzer:in einen Standort aufzeichnet
[USERS_BEHAVIORS_PURCHASE_SHARED](#USERS_BEHAVIORS_PURCHASE_SHARED) | Wenn ein Benutzer einen Kauf tätigt
[USERS_BEHAVIORS_UNINSTALL_SHARED](#USERS_BEHAVIORS_UNINSTALL_SHARED) | Wenn ein Benutzer eine App deinstalliert
[USERS_BEHAVIORS_UPGRADEDAPP_SHARED](#USERS_BEHAVIORS_UPGRADEDAPP_SHARED) | Wenn ein:e Nutzer:in die App aktualisiert
[USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED](#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED) | Wenn ein:e Nutzer:in seine oder ihre erste Sitzung hat
[USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED](#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED) | Wenn ein Nutzer den News Feed anschaut
[USERS_BEHAVIORS_APP_SESSIONEND_SHARED](#USERS_BEHAVIORS_APP_SESSIONEND_SHARED) | Wenn ein Benutzer eine Sitzung in einer App beendet
[USERS_BEHAVIORS_APP_SESSIONSTART_SHARED](#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED) | Wenn ein Benutzer eine Sitzung in einer App beginnt
[USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED) | Wenn ein:e Nutzer:in einen Geofence-Bereich auslöst (z. B. wenn er oder sie einen Geofence aufruft oder verlässt). Dieses Event wurde mit anderen Events zusammengefasst und über den Endpunkt für Standard-Events empfangen. Daher kann es sein, dass der Endpunkt es nicht in Echtzeit empfangen hat.
[USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED](#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED) | Wenn ein:e Nutzer:in einen Geofence-Bereich auslöst (z. B. wenn er oder sie einen Geofence aufruft oder verlässt). Dieses Event wurde über den speziellen Geofence-Endpunkt empfangen und wird daher in Echtzeit empfangen, sobald das Gerät eines Nutzers oder einerr Nutzerin feststellt, dass es einen Geofence getriggert hat. <br><br>Außerdem ist es möglich, dass einige Geofence-Events aufgrund der Rate-Limiting am Geofence-Endpunkt nicht als RecordEvent angezeigt werden. Alle Geofence-Events werden jedoch durch DataEvent dargestellt (allerdings möglicherweise mit einer gewissen Verzögerung aufgrund der Stapelverarbeitung).
[USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED) | Wenn sich ein Push-to-Start-Token für eine Live-Aktivität ändert
[USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED](#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED) | Wenn sich ein Update Token für eine Live-Aktivität ändert
[USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED](#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED) | Wenn sich der Status eines Push-Benachrichtigungstokens ändert
[USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED) | Wenn ein:e Nutzer:in einen Kanal wie z. B. eine E-Mail abonniert oder abbestellt
[USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED](#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED) | Wenn ein:e Nutzer:in sich bei einer Abonnementgruppe anmeldet oder von ihr abmeldet
[USERS_CAMPAIGNS_CONVERSION_SHARED](#USERS_CAMPAIGNS_CONVERSION_SHARED) | Wenn ein:e Nutzer:in für eine Kampagne konvertiert
[USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED](#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED) | Wenn ein Benutzer in die Kontrollgruppe für eine Kampagne aufgenommen wird
[USERS_CAMPAIGNS_FREQUENCYCAP_SHARED](#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED) | Wenn die Frequenz eines Benutzers für eine Kampagne begrenzt wird
[USERS_CAMPAIGNS_REVENUE_SHARED](#USERS_CAMPAIGNS_REVENUE_SHARED) | Wenn ein Benutzer innerhalb des primären Umrechnungszeitraums Umsatz generiert
[USERS_CANVASSTEP_PROGRESSION_SHARED](#USERS_CANVASSTEP_PROGRESSION_SHARED) | Wenn ein Nutzer:innen zu einem Canvas-Schritt übergeht
[USERS_CANVAS_CONVERSION_SHARED](#USERS_CANVAS_CONVERSION_SHARED) | Wenn ein:e Nutzer:in für ein Canvas-Konversions-Event konvertiert
[USERS_CANVAS_ENTRY_SHARED](#USERS_CANVAS_ENTRY_SHARED) | Wenn ein Benutzer einen Canvas betritt
[USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED](#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED) | Wenn ein:e Nutzer:in ein Canvas verlässt, weil er oder sie die Kriterien für das Verlassen der Zielgruppe erfüllt
[USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED](#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED) | Wenn ein:e Nutzer:in ein Canvas verlässt, weil er oder sie ein Ausnahme-Event ausgeführt hat
[USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED) | Wenn ein Benutzer für einen Schritt des Canvas-Experiments konvertiert
[USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED](#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED) | Wenn ein:e Nutzer:in einen Pfad für einen Experimentierschritt eingibt
[USERS_CANVAS_FREQUENCYCAP_SHARED](#USERS_CANVAS_FREQUENCYCAP_SHARED) | Wenn die Frequenz eines Benutzers für einen Canvas-Schritt begrenzt wird
[USERS_CANVAS_REVENUE_SHARED](#USERS_CANVAS_REVENUE_SHARED) | Wenn ein:e Nutzer:in innerhalb des primären Konversions-Event-Zeitraums Umsatz generiert
[USERS_MESSAGES_BANNER_ABORT_SHARED](#USERS_MESSAGES_BANNER_ABORT_SHARED) | Eine ursprünglich geplante Bannernachricht wurde aus irgendeinem Grund abgebrochen
[USERS_MESSAGES_BANNER_CLICK_SHARED](#USERS_MESSAGES_BANNER_CLICK_SHARED) | Wenn ein Nutzer:innen auf ein Banner klickt
[USERS_MESSAGES_BANNER_IMPRESSION_SHARED](#USERS_MESSAGES_BANNER_IMPRESSION_SHARED) | Wenn ein Nutzer:innen ein Banner sieht
[USERS_MESSAGES_CONTENTCARD_ABORT_SHARED](#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED) | Eine ursprünglich geplante Inhaltskartennachricht wurde aus irgendeinem Grund abgebrochen.
[USERS_MESSAGES_CONTENTCARD_CLICK_SHARED](#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED) | Wenn ein Benutzer auf eine Inhaltskarte klickt
[USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED](#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED) | Wenn ein Benutzer eine Inhaltskarte ablehnt
[USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED](#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED) | Wenn ein Benutzer eine Inhaltskarte ansieht
[USERS_MESSAGES_CONTENTCARD_SEND_SHARED](#USERS_MESSAGES_CONTENTCARD_SEND_SHARED) | Wenn wir eine Inhaltskarte an einen Benutzer senden
[USERS_MESSAGES_EMAIL_ABORT_SHARED](#USERS_MESSAGES_EMAIL_ABORT_SHARED) | Eine ursprünglich geplante E-Mail-Nachricht wurde aus irgendeinem Grund abgebrochen.
[USERS_MESSAGES_EMAIL_BOUNCE_SHARED](#USERS_MESSAGES_EMAIL_BOUNCE_SHARED) | Ein E-Mail-Anbieter hat einen Hard Bounce zurückgegeben. Ein Hard Bounce bedeutet einen dauerhaften Zustellbarkeitsfehler.
[USERS_MESSAGES_EMAIL_CLICK_SHARED](#USERS_MESSAGES_EMAIL_CLICK_SHARED) | Wenn ein Benutzer auf einen Link in einer E-Mail klickt
[USERS_MESSAGES_EMAIL_DEFERRAL_SHARED](#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED) | Wenn eine E-Mail aufgeschoben wird
[USERS_MESSAGES_EMAIL_DELIVERY_SHARED](#USERS_MESSAGES_EMAIL_DELIVERY_SHARED) | Wenn eine E-Mail zugestellt wird
[USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED](#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED) | Wenn eine E-Mail als Spam markiert wird
[USERS_MESSAGES_EMAIL_OPEN_SHARED](#USERS_MESSAGES_EMAIL_OPEN_SHARED) | Wenn ein Benutzer eine E-Mail öffnet
[USERS_MESSAGES_EMAIL_SEND_SHARED](#USERS_MESSAGES_EMAIL_SEND_SHARED) | Wenn wir eine E-Mail an einen Benutzer senden
[USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED](#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED) | Wenn eine E-Mail als Soft-Bounce eingeht
[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED](#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED) | Wenn sich ein:e Nutzer:in von einer E-Mail abmeldet
[USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED](#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED) | Wenn ein Nutzer:innen ein Feature-Flag sieht
[USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED](#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED) | Eine ursprünglich geplante In-App-Nachricht wurde aus irgendeinem Grund abgebrochen.
[USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED](#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED) | Wenn ein Benutzer auf eine In-App-Nachricht klickt
[USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED](#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED) | Wenn ein Nutzer eine In-App-Nachricht anschaut
[USERS_MESSAGES_LINE_ABORT_SHARED](#USERS_MESSAGES_LINE_ABORT_SHARED) | Wenn eine geplante LINE Nachricht nicht zugestellt werden kann, bevor sie an LINE gesendet wird
[USERS_MESSAGES_LINE_CLICK_SHARED](#USERS_MESSAGES_LINE_CLICK_SHARED) | Wenn ein Nutzer:innen auf einen Link in einer LINE Nachricht klickt
[USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED) | Wenn eine LINE Nachricht von einem Nutzer:innen empfangen wird
[USERS_MESSAGES_LINE_SEND_SHARED](#USERS_MESSAGES_LINE_SEND_SHARED) | Wenn eine LINE Nachricht an LINE gesendet wird
[USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED](#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED) | Wenn eine Live-Aktivität ein Ergebnisereignis hat
[USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED](#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED) | Wenn eine Live Activity Nachricht gesendet wird
[USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED) | Eine ursprünglich geplante Nachricht der Newsfeed-Karte wurde aus irgendeinem Grund abgebrochen
[USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED) | Wenn ein Benutzer auf eine News-Feed-Karte klickt
[USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED](#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED) | Wenn ein Benutzer eine News-Feed-Karte ansieht
[USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED) | Eine ursprünglich geplante Push-Benachrichtigung wurde aus irgendeinem Grund abgebrochen.
[USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED) | Wenn eine Push-Benachrichtigung abprallt
[USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED) | Wenn ein Benutzer die App nach Erhalt einer Benachrichtigung öffnet, ohne auf die Benachrichtigung zu klicken
[USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED) | Wenn ein Nutzer:innen eine Push-Benachrichtigung erhält, während die App geöffnet ist. <br><br>Dieses Ereignis wird vom [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) nicht unterstützt und ist im [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) veraltet.
[USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED) | Wenn ein Benutzer eine Push-Benachrichtigung öffnet oder auf eine Push-Benachrichtigungsschaltfläche klickt (einschließlich einer SCHLIESSEN-Schaltfläche, die die App NICHT öffnet). <br><br> Aktionen auf Knopfdruck haben mehrere Auswirkungen. Aktionen wie „Nein“, „Ablehnen“ und „Abbrechen“ werden durch Klicken ausgeführt, während Aktionen wie „Akzeptieren“ durch Öffnen ausgeführt werden. Beide sind in dieser Tabelle vertreten, aber sie lassen sich in der **BUTTON_ACTION_TYPE** Spalte. Beispielsweise kann eine Abfrage verwendet werden, um nach einem `BUTTON_ACTION_TYPE` zu gruppieren, bei dem es sich nicht um „Nein“, „Ablehnen“ und „Abbrechen“ handelt.
[USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED](#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED) | Wenn wir eine Push-Benachrichtigung an einen Benutzer senden
[USERS_MESSAGES_RCS_ABORT_SHARED](#USERS_MESSAGES_RCS_ABORT_SHARED) | Wenn ein RCS-Sendevorgang aufgrund eines Fehlers in Braze unterbrochen wird und die Nachricht verworfen wird
[USERS_MESSAGES_RCS_CLICK_SHARED](#USERS_MESSAGES_RCS_CLICK_SHARED) | Wenn der Endnutzer mit einer RCS Nachricht interagiert, indem er auf ein UI-Element tippt oder klickt
[USERS_MESSAGES_RCS_DELIVERY_SHARED](#USERS_MESSAGES_RCS_DELIVERY_SHARED) | Wenn eine RCS Nachricht erfolgreich an das mobile Gerät eines Endnutzers:in zugestellt wurde
[USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED) | Wenn Braze eine RCS Nachricht empfängt, die von einem Endnutzer:in stammt
[USERS_MESSAGES_RCS_READ_SHARED](#USERS_MESSAGES_RCS_READ_SHARED) | Wenn der Endnutzer:in eine RCS Nachricht auf seinem Gerät öffnet
[USERS_MESSAGES_RCS_REJECTION_SHARED](#USERS_MESSAGES_RCS_REJECTION_SHARED) | Wenn eine RCS-Nachricht aufgrund eines Eingriffs des Netzbetreibers nicht zugestellt werden kann
[USERS_MESSAGES_RCS_SEND_SHARED](#USERS_MESSAGES_RCS_SEND_SHARED) | Wenn eine RCS-Nachricht aus den Systemen von Braze an Partner für die Zustellung auf der letzten Meile gesendet wird
[USERS_MESSAGES_SMS_ABORT_SHARED](#USERS_MESSAGES_SMS_ABORT_SHARED) | Eine ursprünglich geplante SMS-Nachricht wurde aus irgendeinem Grund abgebrochen.
[USERS_MESSAGES_SMS_CARRIERSEND_SHARED](#USERS_MESSAGES_SMS_CARRIERSEND_SHARED) | Wenn eine SMS-Nachricht an den Netzbetreiber gesendet wird
[USERS_MESSAGES_SMS_DELIVERY_SHARED](#USERS_MESSAGES_SMS_DELIVERY_SHARED) | Wenn eine SMS-Nachricht zugestellt wird
[USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED](#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED) | Wenn Braze nicht in der Lage ist, die SMS-Nachricht an den SMS-Dienstanbieter zu übermitteln
[USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED) | Wenn eine SMS-Nachricht von einem Benutzer empfangen wird
[USERS_MESSAGES_SMS_REJECTION_SHARED](#USERS_MESSAGES_SMS_REJECTION_SHARED) | Wenn eine SMS-Nachricht einem Benutzer nicht zugestellt wird
[USERS_MESSAGES_SMS_SEND_SHARED](#USERS_MESSAGES_SMS_SEND_SHARED) | Wenn eine SMS-Nachricht gesendet wird
[USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED](#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED) | Wenn ein Benutzer auf eine verkürzte URL von Braze in einer SMS-Nachricht klickt
[USERS_MESSAGES_WEBHOOK_ABORT_SHARED](#USERS_MESSAGES_WEBHOOK_ABORT_SHARED) | Eine ursprünglich geplante Webhook-Nachricht wurde aus irgendeinem Grund abgebrochen
[USERS_MESSAGES_WEBHOOK_FAILURE_SHARED](#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED) | Wenn eine Webhook Nachricht zugestellt wird, aber mit einer Fehlerantwort des Endpunkts fehlschlägt
[USERS_MESSAGES_WEBHOOK_SEND_SHARED](#USERS_MESSAGES_WEBHOOK_SEND_SHARED) | Wenn wir einen Webhook für einen Benutzer senden
[USERS_MESSAGES_WHATSAPP_ABORT_SHARED](#USERS_MESSAGES_WHATSAPP_ABORT_SHARED) | Eine ursprünglich geplante WhatsApp-Nachricht wurde aus irgendeinem Grund abgebrochen
[USERS_MESSAGES_WHATSAPP_CLICK_SHARED](#USERS_MESSAGES_WHATSAPP_CLICK_SHARED) | Wenn ein Nutzer:innen auf einen Link oder Button in einer WhatsApp Nachricht klickt
[USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED](#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED) |Wenn eine WhatsApp-Nachricht zugestellt wird
[USERS_MESSAGES_WHATSAPP_FAILURE_SHARED](#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED) | Wenn eine WhatsApp-Nachricht einem Benutzer nicht zugestellt wird
[USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED](#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED) | Wenn eine WhatsApp-Nachricht von einem Benutzer empfangen wird
[USERS_MESSAGES_WHATSAPP_READ_SHARED](#USERS_MESSAGES_WHATSAPP_READ_SHARED) | Wenn ein Benutzer eine WhatsApp-Nachricht öffnet
[USERS_MESSAGES_WHATSAPP_SEND_SHARED](#USERS_MESSAGES_WHATSAPP_SEND_SHARED) | Wenn wir eine WhatsApp-Nachricht für einen Benutzer senden
[USERS_RANDOMBUCKETNUMBERUPDATE_SHARED](#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED) | Wenn die zufällige Bucket-Nummer eines Benutzers geändert wird
[USERS_USERDELETEREQUEST_SHARED](#USERS_USERDELETEREQUEST_SHARED) | Wenn ein Benutzer durch eine Kundenanfrage gelöscht wird
[USERS_USERORPHAN_SHARED](#USERS_USERORPHAN_SHARED) | Wenn ein Benutzer mit dem Profil eines anderen Benutzers zusammengeführt wird und das ursprüngliche Profil verwaist ist


## Kataloge

### CATALOGS_ITEMS_SHARED {#CATALOGS_ITEMS_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`catalog_id` | `string` | BSON ID des Katalogs
`item_id` | `string` | BSON ID des Katalogartikels
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe
`field_name` | `null,` `string` | Name des Feldes
`field_value` | `null,` `string` | Wert des Feldes
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Changelogs

### CHANGELOGS_GLOBALCONTROLGROUP_SHARED {#CHANGELOGS_GLOBALCONTROLGROUP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`random_bucket_number` | `null, int` | Neue zufällige Bucket-Nummer
`global_control_group` | `null, boolean` | Mit dieser Änderung wird die Bucket-Nummer in die globale Kontrollgruppe aufgenommen.
`previous_global_control_group` | `null, boolean` | Vor dieser Änderung war die Bucket-Nummer in der globalen Kontrollgruppe enthalten, jetzt ist sie es nicht mehr.
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Verhaltensweisen

### USERS_BEHAVIORS_CUSTOMEVENT_SHARED {#USERS_BEHAVIORS_CUSTOMEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die das Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_api_id` | `null,` `string` | API-ID der App, in der diese Aktion stattgefunden hat
`time` | `int` | Unix-Zeitstempel, zu dem der oder die Nutzer:in das Event durchgeführt hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das benutzerdefinierte Ereignis aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`name` | `string` | Name des angepasstes Events
`properties` | `string` | Benutzerdefinierte Eigenschaften des Ereignisses, gespeichert als JSON-kodierte Zeichenkette
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Eine von `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED {#USERS_BEHAVIORS_INSTALLATTRIBUTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die die Installation vorgenommen hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem der Benutzer installiert hat
`source` | `string` | die Quelle der Attribution
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_LOCATION_SHARED {#USERS_BEHAVIORS_LOCATION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die den Standort aufzeichnet
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_api_id` | `null,` `string` | API-ID der App, mit der dieser Standort aufgenommen wurde
`time` | `int` | Unix-Zeitstempel, zu dem der Ort aufgezeichnet wurde
`latitude` | `float` | [PII] Breitengrad des aufgezeichneten Standorts
`longitude` | `float` | [PII] Längengrad des aufgezeichneten Standorts
`altitude` | `null, float` | [PII] Höhe des aufgezeichneten Standorts
`ll_accuracy` | `null, float` | Längen- und Breitengradgenauigkeit des aufgezeichneten Standorts
`alt_accuracy` | `null, float` | Höhengenauigkeit des aufgezeichneten Standorts
`device_id` | `null,` `string` | ID des Geräts, auf dem der Standort aufgezeichnet wurde
`sdk_version` | `null,` `string` | Version des Braze-SDK, die verwendet wurde, als der Standort aufgenommen wurde
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Eine von `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_PURCHASE_SHARED {#USERS_BEHAVIORS_PURCHASE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Benutzers, der einen Kauf getätigt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_api_id` | `null,` `string` | API-ID der App, in der der Kauf getätigt wurde
`time` | `int` | Unix-Zeitstempel, zu dem der Benutzer den Kauf getätigt hat
`device_id` | `null,` `string` | ID des Geräts, auf dem der Kauf getätigt wurde
`sdk_version` | `null,` `string` | Version des Braze SDK, die während des Kaufs verwendet wurde
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`product_id` | `string` | ID des gekauften Produkts
`price` | `float` | Kaufpreis
`currency` | `string` | Kaufwährung
`properties` | `string` | Benutzerdefinierte Eigenschaften des Kaufs, gespeichert als JSON-kodierte Zeichenkette
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Eine von `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UNINSTALL_SHARED {#USERS_BEHAVIORS_UNINSTALL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die die Deinstallation durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_api_id` | `null,` `string` | API ID der App, die deinstalliert wurde
`time` | `int` | Unix-Zeitstempel, zu dem der Benutzer deinstalliert hat
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_UPGRADEDAPP_SHARED {#USERS_BEHAVIORS_UPGRADEDAPP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die die App aktualisiert hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_api_id` | `null,` `string` | API-ID der App, die der oder die Nutzer:in aktualisiert hat
`time` | `int` | Unix-Zeitstempel, zu dem der oder die Nutzer:in die App aktualisiert hat
`device_id` | `null,` `string` | ID des Geräts, auf dem der oder die Nuzter:in die App aktualisiert hat
`sdk_version` | `null,` `string` | Verwendete Version des Braze SDK
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`old_app_version` | `null,` `string` | Alte Version der App
`new_app_version` | `null,` `string` | Neue Version der App
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED {#USERS_BEHAVIORS_APP_FIRSTSESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Benutzers, der diese Aktion durchführt
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_api_id` | `null,` `string` | API-ID der App, in der diese Sitzung stattgefunden hat
`time` | `int` | Unix-Zeitstempel des Sitzungsbeginns
`session_id` | `string` | UUID der Sitzung
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem die Sitzung stattgefunden hat
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während der Sitzung verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED {#USERS_BEHAVIORS_APP_NEWSFEEDIMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONEND_SHARED {#USERS_BEHAVIORS_APP_SESSIONEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Benutzers, der diese Aktion durchführt
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_api_id` | `null,` `string` | API-ID der App, in der diese Sitzung stattgefunden hat
`time` | `int` | Unix-Zeitstempel des Sitzungsendes
`duration` | `null, float` | Dauer der Sitzung in Sekunden
`session_id` | `string` | UUID der Sitzung
`device_id` | `null,` `string` | ID des Geräts, auf dem die Sitzung stattgefunden hat
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während der Sitzung verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_APP_SESSIONSTART_SHARED {#USERS_BEHAVIORS_APP_SESSIONSTART_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Benutzers, der diese Aktion durchführt
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_api_id` | `null,` `string` | API-ID der App, in der diese Sitzung stattgefunden hat
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel des Sitzungsbeginns
`session_id` | `string` | UUID der Sitzung
`device_id` | `null,` `string` | ID des Geräts, auf dem die Sitzung stattgefunden hat
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während der Sitzung verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_DATAEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die das Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_api_id` | `null,` `string` | API-ID der App, in der diese Aktion stattgefunden hat
`time` | `int` | Unix-Zeitstempel, zu dem der oder die Nutzer:in das Event durchgeführt hat
`device_id` | `null,` `string` | ID des Geräts, auf dem das benutzerdefinierte Ereignis aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`event_type` | `string` | Welche Art von Geofencing-Event wurde getriggert (z. B. „Aufrufen“ oder „Verlassen“)
`location_set_id` | `string` | Die ID des Ortssatzes des Geofence, der ausgelöst wurde
`geofence_id` | `string` | Die ID des Geofence, der ausgelöst wurde
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED {#USERS_BEHAVIORS_GEOFENCE_RECORDEVENT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die das Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_api_id` | `null,` `string` | API-ID der App, in der diese Aktion stattgefunden hat
`time` | `int` | Unix-Zeitstempel, zu dem der oder die Nutzer:in das Event durchgeführt hat
`device_id` | `null,` `string` | ID des Geräts, auf dem das benutzerdefinierte Ereignis aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`event_type` | `string` | Welche Art von Geofencing-Event wurde getriggert (z. B. „Aufrufen“ oder „Verlassen“)
`location_set_id` | `string` | Die ID des Ortssatzes des Geofence, der ausgelöst wurde
`geofence_id` | `string` | Die ID des Geofence, der ausgelöst wurde
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_PUSHTOSTARTTOKENCHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`activity_attributes_type` | `null,` `string` | Live Aktivität Attribut Typ
`push_to_start_token` | `null,` `string` | Live Activity Push zum Starten des Tokens
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS Push-Token, 1 für die Entwicklung, 2 für die Produktion
`push_token_state_change_type` | `null,` `string` | Eine Beschreibung des Push-Token-Statusänderungstyps
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED {#USERS_BEHAVIORS_LIVEACTIVITY_UPDATETOKENCHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`activity_id` | `null,` `string` | Live Bezeichner der Aktivität
`update_token` | `null,` `string` | Update-Token für Live-Aktivitäten
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS Push-Token, 1 für die Entwicklung, 2 für die Produktion
`push_token_state_change_type` | `null,` `string` | Eine Beschreibung des Push-Token-Statusänderungstyps
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED {#USERS_BEHAVIORS_PUSHNOTIFICATION_TOKENSTATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`push_token` | `null,` `string` | Push-Token des Ereignisses
`push_token_created_at` | `null, int` | UNIX-Zeitstempel, zu dem das Push-Token erstellt wurde
`push_token_updated_at` | `null, int` | UNIX-Zeitstempel, zu dem das Push-Token zuletzt aktualisiert wurde
`push_token_foreground_push_disabled` | `null, boolean` | Foreground push disabled Flag des Push-Tokens
`push_token_device_id` | `null,` `string` | Geräte-ID des Push-Tokens
`push_token_provisionally_opted_in` | `null, boolean` | Vorläufiges Opt-in-Flag des Push-Tokens
`ios_push_token_apns_gateway` | `null, int` | APNS-Gateway des Push-Tokens, gilt nur für iOS Push-Token, 1 für die Entwicklung, 2 für die Produktion
`web_push_token_public_key` | `null,` `string` | Public Key des Push-Tokens, gilt nur für Web-Push-Tokens
`web_push_token_user_auth` | `null,` `string` | Benutzer:in des Push-Tokens, gilt nur für Web-Push-Token
`web_push_token_vapid_public_key` | `null,` `string` | VAPID Public Key des Push-Tokens, gilt nur für Web-Push-Tokens
`push_token_state_change_type` | `null,` `string` | Eine Beschreibung des Push-Token-Statusänderungstyps
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTION_GLOBALSTATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des betroffenen Benutzers
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`email_address` | `null,` `string` | [PII] E-Mail Adresse des Nutzers:innen
`state_change_source` | `null,` `string` | Quelle der Zustandsänderung (REST, SDK, Dashboard, etc.)
`subscription_status` | `string` | Abo-Status: Abonnent:in", "Abgemeldet" oder "Opt-in
`channel` | `null,` `string` | Kanal des globalen Abonnementstatus wie z.B. E-Mail
`time` | `int` | Unix-Zeitstempel, an dem sich der Status des Abonnements geändert hat
`timezone` | `null,` `string` | Zeitzone des Benutzers
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_api_id` | `null,` `string` | API-ID der App, zu der das Event gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariante, zu der dieses Ereignis gehört
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`send_id` | `null,` `string` | ID der Nachricht, von der diese Aktion zur Änderung des Abo-Status stammt
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`channel_identifier` | `null,` `string` | [PII] Der Bezeichner des Nutzers:innen auf dem Kanal, für den das Ereignis gilt.
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED {#USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des betroffenen Benutzers
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`email_address` | `null,` `string` | [PII] E-Mail Adresse des Nutzers:innen
`phone_number` | `null,` `string` | [PII] Telefonnummer des Nutzers:innen im Format e164
`app_api_id` | `null,` `string` | API-ID der App, zu der das Event gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariante, zu der dieses Ereignis gehört
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`channel` | `null,` `string` | Kanal: 'E-Mail' oder 'SMS', je nach Kanaltyp der Abonnementgruppe
`subscription_status` | `string` | Abo-Status: Abonnent:in", "Abgemeldet" oder "Opt-in
`time` | `int` | Unix-Zeitstempel, an dem sich der Status des Abonnements geändert hat
`timezone` | `null,` `string` | Zeitzone des Benutzers
`send_id` | `null,` `string` | ID der Nachricht, von der diese Aktion zur Änderung des Abo-Status stammt
`state_change_source` | `null,` `string` | Quelle der Statusänderung (REST, SDK, Dashboard, etc.)
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`channel_identifier` | `null,` `string` | [PII] Der Bezeichner des Nutzers:innen auf dem Kanal, für den das Ereignis gilt.
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Kampagnen

### USERS_CAMPAIGNS_CONVERSION_SHARED {#USERS_CAMPAIGNS_CONVERSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`conversion_behavior_index` | `null, int` | Index des Konvertierungsverhaltens
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED {#USERS_CAMPAIGNS_ENROLLINCONTROL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_FREQUENCYCAP_SHARED {#USERS_CAMPAIGNS_FREQUENCYCAP_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`channel` | `null,` `string` | Kanal, zu dem dieses Event gehört
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CAMPAIGNS_REVENUE_SHARED {#USERS_CAMPAIGNS_REVENUE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`revenue` | `long` | Der Betrag der generierten USD-Einnahmen in Cent
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Canvas

### USERS_CANVASSTEP_PROGRESSION_SHARED {#USERS_CANVASSTEP_PROGRESSION_SHARED}

| Feld                                  | Typ                     | Beschreibung                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | Globale eindeutige ID für dieses Event                                                                               |
| `user_id`                              | `string`, `null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] Externe ID des Nutzers:innen                                                                              |
| `device_id`                            | `string`, `null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist                                            |
| `app_group_id`                         | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                                                   |
| `app_group_api_id`                     | `string`, `null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                                                    |
| `time`                                 | `int`, `null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                                                                      |
| `canvas_id`                            | `string`, `null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört                                                     |
| `canvas_api_id`                        | `string`, `null`    | API-ID des Canvas, zu dem dieses Event gehört        |         
| `canvas_variation_api_id`              | `string`, `null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                                                                 |
| `progression_type`                     | `string`, `null`    | Art des Schrittfolgeereignisses |
| `is_canvas_entry`                      | `boolean`, `null`   | Ob dies der Eingang zu einem ersten Canvas-Schritt ist        |
| `exit_reason`                          | `string`, `null`    | Wenn es sich um einen Exit handelt, der Grund, warum ein Nutzer:in während des Schritts den Canvas verlassen hat                  |
| `canvas_entry_id`                      | `string`, `null`    | Eindeutiger Bezeichner für diese Instanz eines Nutzers:innen in einem Canvas  |
| `next_step_id`                         | `string`, `null`    | BSON ID des nächsten Schritts im Canvas |
| `next_step_api_id`                     | `string`, `null`    | API ID des nächsten Schritts im Canvas |
| `sf_created_at`                        | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_CONVERSION_SHARED {#USERS_CANVAS_CONVERSION_SHARED}

| Feld                                  | Typ                     | Beschreibung                                                                                                     |
| -------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | Globale eindeutige ID für dieses Event                                                                               |
| `user_id`                              | `string`, `null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                                                                   |
| `external_user_id`                     | `string`, `null`    | [PII] Externe ID des Nutzers:innen                                                                              |
| `device_id`                            | `string`, `null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist                                            |
| `app_group_id`                         | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                                                   |
| `app_group_api_id`                     | `string`, `null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                                                    |
| `time`                                 | `int`, `null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                                                                      |
| `app_api_id`                           | `string`, `null`    | API-ID der App, in der dieses Ereignis aufgetreten ist                                                                  |
| `canvas_id`                            | `string`, `null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört                                                     |
| `canvas_api_id`                        | `string`, `null`    | API-ID des Canvas, zu dem dieses Event gehört                                                                      |
| `canvas_variation_api_id`              | `string`, `null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                                                            |
| `canvas_step_api_id`                   | `string`, `null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                                                                 |
| `canvas_step_message_variation_api_id` | `string`, `null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat                                                  |
| `conversion_behavior_index`            | `int`, `null`       | Art des Konversions-Events, das der oder die Nutzer:in durchgeführt hat, wobei „0“ für eine primäre Konversion und „1“ für eine sekundäre Konversion steht |
| `gender`                               | `string`, `null`    | [PII] Geschlecht der Nutzer:innen                                                                                        |
| `country`                              | `string`, `null`    | [PII] Land des Nutzers:innen                                                                                       |
| `timezone`                             | `string`, `null`    | Zeitzone des Benutzers                                                                                            |
| `language`                             | `string`, `null`    | [PII] Sprache des Nutzers:innen                                                                                      |
| `sf_created_at`                        | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_ENTRY_SHARED {#USERS_CANVAS_ENTRY_SHARED}

| Feld                     | Typ                     | Beschreibung                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                 | `string`, `null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`        | `string`, `null`    | [PII] Externe ID des Nutzers:innen                                   |
| `device_id`               | `string`, `null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist |
| `app_group_id`            | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `app_group_api_id`        | `string`, `null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                         |
| `time`                    | `int`, `null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`               | `string`, `null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`           | `string`, `null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id` | `string`, `null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`      | `string`, `null`    | [Veraltet] API ID des Canvas-Schrittes, zu dem dieses Ereignis gehört         |
| `gender`                  | `string`, `null`    | [PII] Geschlecht der Nutzer:innen                                             |
| `country`                 | `string`, `null`    | [PII] Land des Nutzers:innen                                            |
| `timezone`                | `string`, `null`    | Zeitzone des Benutzers                                                 |
| `language`                | `string`, `null`    | [PII] Sprache des Nutzers:innen                                           |
| `in_control_group`        | `boolean`, `null`   | Wahr, wenn der Benutzer in der Kontrollgruppe eingeschrieben war                   |
| `sf_created_at`           | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED {#USERS_CANVAS_EXIT_MATCHEDAUDIENCE_SHARED}

| Feld                     | Typ                     | Beschreibung                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                 | `string`, `null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`        | `string`, `null`    | [PII] Externe ID des Nutzers:innen                                   |
| `app_group_id`            | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `app_group_api_id`        | `string`, `null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                         |
| `time`                    | `int`, `null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`               | `string`, `null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`           | `string`, `null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id` | `string`, `null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`      | `string`, `null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                      |
| `sf_created_at`           | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED {#USERS_CANVAS_EXIT_PERFORMEDEVENT_SHARED}

| Feld                     | Typ                     | Beschreibung                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                 | `string`, `null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`        | `string`, `null`    | [PII] Externe ID des Nutzers:innen                                   |
| `app_group_id`            | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `app_group_api_id`        | `string`, `null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                         |
| `time`                    | `int`, `null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`               | `string`, `null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`           | `string`, `null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id` | `string`, `null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`      | `string`, `null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                      |
| `sf_created_at`           | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_CONVERSION_SHARED}

| Feld                       | Typ                     | Beschreibung                                                                                                     |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------- |
| `id`                        | `string`, `null`    | Globale eindeutige ID für dieses Event                                                                               |
| `user_id`                   | `string`, `null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                                                                   |
| `external_user_id`          | `string`, `null`    | [PII] Externe ID des Nutzers:innen                                                                              |
| `app_group_id`              | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                                                   |
| `time`                      | `int`, `null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                                                                      |
| `app_api_id`                | `string`, `null`    | API-ID der App, in der dieses Ereignis aufgetreten ist                                                                  |
| `canvas_id`                 | `string`, `null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört                                                     |
| `canvas_api_id`             | `string`, `null`    | API-ID des Canvas, zu dem dieses Event gehört                                                                      |
| `canvas_variation_api_id`   | `string`, `null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                                                            |
| `canvas_step_api_id`        | `string`, `null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                                                                 |
| `experiment_step_api_id`    | `string`, `null`    | API-ID des Experiment-Schrittes, zu dem dieses Ereignis gehört                                                             |
| `conversion_behavior_index` | `int`, `null`       | Art des Konversions-Events, das der oder die Nutzer:in durchgeführt hat, wobei „0“ für eine primäre Konversion und „1“ für eine sekundäre Konversion steht |
| `sf_created_at`             | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                                                                   |
| `experiment_split_api_id` | `string`, `null` | API ID des Experiment-Splits, für den sich der Nutzer:in angemeldet hat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED {#USERS_CANVAS_EXPERIMENTSTEP_SPLITENTRY_SHARED}

| Feld                     | Typ                     | Beschreibung                                                          |
| ------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                      | `string`, `null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                 | `string`, `null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`        | `string`, `null`    | [PII] Externe ID des Nutzers:innen                                   |
| `app_group_id`            | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `time`                    | `int`, `null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`               | `string`, `null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`           | `string`, `null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id` | `string`, `null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`      | `string`, `null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                      |
| `experiment_step_api_id`  | `string`, `null`    | API-ID des Experiment-Schrittes, zu dem dieses Ereignis gehört                  |
| `in_control_group`        | `boolean`, `null`   | Wahr, wenn der Benutzer in der Kontrollgruppe eingeschrieben war                   |
| `sf_created_at`           | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |

| `experiment_split_api_id` | `string`, `null` | API ID des Experiments, an dem der Nutzer:innen teilgenommen hat |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_FREQUENCYCAP_SHARED {#USERS_CANVAS_FREQUENCYCAP_SHARED}

| Feld                                  | Typ                     | Beschreibung                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                              | `string`, `null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`                     | `string`, `null`    | [PII] Externe ID des Nutzers:innen                                   |
| `device_id`                            | `string`, `null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist |
| `app_group_id`                         | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `app_group_api_id`                     | `string`, `null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                         |
| `time`                                 | `int`, `null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`                            | `string`, `null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`                        | `string`, `null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id`              | `string`, `null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`                   | `string`, `null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat       |
| `channel`                              | `string`, `null`    | Messaging-Kanal, zu dem dieses Event gehört (E-Mail, Push, etc.)          |
| `gender`                               | `string`, `null`    | [PII] Geschlecht der Nutzer:innen                                             |
| `country`                              | `string`, `null`    | [PII] Land des Nutzers:innen                                            |
| `timezone`                             | `string`, `null`    | Zeitzone des Benutzers                                                 |
| `language`                             | `string`, `null`    | [PII] Sprache des Nutzers:innen                                           |
| `sf_created_at`                        | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_CANVAS_REVENUE_SHARED {#USERS_CANVAS_REVENUE_SHARED}

| Feld                                  | Typ                     | Beschreibung                                                          |
| -------------------------------------- | ------------------------ | -------------------------------------------------------------------- |
| `id`                                   | `string`, `null`    | Globale eindeutige ID für dieses Event                                    |
| `user_id`                              | `string`, `null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat                        |
| `external_user_id`                     | `string`, `null`    | [PII] Externe ID des Nutzers:innen                                   |
| `device_id`                            | `string`, `null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist |
| `app_group_id`                         | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                        |
| `app_group_api_id`                     | `string`, `null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                         |
| `time`                                 | `int`, `null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist                           |
| `canvas_id`                            | `string`, `null`    | (Nur für Braze) ID des Canvas, zu dem dieses Event gehört          |
| `canvas_api_id`                        | `string`, `null`    | API-ID des Canvas, zu dem dieses Event gehört                           |
| `canvas_variation_api_id`              | `string`, `null`    | API-ID der Canvas-Variation, zu der dieses Ereignis gehört                 |
| `canvas_step_api_id`                   | `string`, `null`    | API-ID des Canvas-Schritts, zu dem dieses Event gehört                      |
| `canvas_step_message_variation_api_id` | `string`, `null`    | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat       |
| `gender`                               | `string`, `null`    | [PII] Geschlecht der Nutzer:innen                                             |
| `country`                              | `string`, `null`    | [PII] Land des Nutzers:innen                                            |
| `timezone`                             | `string`, `null`    | Zeitzone des Benutzers                                                 |
| `language`                             | `string`, `null`    | [PII] Sprache des Nutzers:innen                                           |
| `revenue`                              | `int`, `null`       | Betrag der generierten Einnahmen in USD, angezeigt in Cents               |
| `sf_created_at`                        | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                        |
| `app_api_id` | `string`, `null` | API-ID der App, in der dieses Ereignis aufgetreten ist |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Nachrichten


### USERS_MESSAGES_BANNER_ABORT_SHARED {#USERS_MESSAGES_BANNER_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`campaign_id` | `null,` `string` | BSON ID der Kampagne, zu der dieses Ereignis gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Gerätebrowser - extrahiert aus user_agent \- auf dem die Öffnung erfolgte
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Einer der ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (bis zu 128 Zeichen)
`banner_placement_id` | `null,` `string` | Von Kund:in angegebene ID für die Platzierung von Bannern
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_CLICK_SHARED {#USERS_MESSAGES_BANNER_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`campaign_id` | `null,` `string` | BSON ID der Kampagne, zu der dieses Ereignis gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Gerätebrowser - extrahiert aus user_agent \- auf dem die Öffnung erfolgte
`button_id` | `null,` `string` | ID des angeklickten Buttons, wenn dieser Klick einen Klick auf einen Button darstellt
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Einer der ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`banner_placement_id` | `null,` `string` | Von Kund:in angegebene ID für die Platzierung von Bannern
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_BANNER_IMPRESSION_SHARED {#USERS_MESSAGES_BANNER_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`campaign_id` | `null,` `string` | BSON ID der Kampagne, zu der dieses Ereignis gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Gerätebrowser - extrahiert aus user_agent \- auf dem die Öffnung erfolgte
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Einer der ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`banner_placement_id` | `null,` `string` | Von Kund:in angegebene ID für die Platzierung von Bannern
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_ABORT_SHARED {#USERS_MESSAGES_CONTENTCARD_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (maximal 2.000 Zeichen)
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_CLICK_SHARED {#USERS_MESSAGES_CONTENTCARD_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`content_card_id` | `string` | ID der Karte, die dieses Event ausgelöst hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Browser des Geräts
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Eine von `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED {#USERS_MESSAGES_CONTENTCARD_DISMISS_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`content_card_id` | `string` | ID der Karte, die dieses Event ausgelöst hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Browser des Geräts
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Eine von `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED {#USERS_MESSAGES_CONTENTCARD_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`content_card_id` | `string` | ID der Karte, die dieses Event ausgelöst hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Browser des Geräts
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Eine von `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_CONTENTCARD_SEND_SHARED {#USERS_MESSAGES_CONTENTCARD_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`content_card_id` | `string` | ID der Karte, die dieses Event ausgelöst hat
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`message_extras` | `null,` `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare beim Liquid-Rendering
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_ABORT_SHARED {#USERS_MESSAGES_EMAIL_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`email_address` | `string` | [PII] E-Mail Adresse des Nutzers:innen
`ip_pool` | `null,` `string` | IP-Pool, von dem aus die E-Mail gesendet wurde
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (maximal 2.000 Zeichen)
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_BOUNCE_SHARED {#USERS_MESSAGES_EMAIL_BOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`email_address` | `string` | [PII] E-Mail Adresse des Nutzers:innen
`sending_ip` | `null,` `string` | IP-Adresse, von der aus die E-Mail gesendet wurde
`ip_pool` | `null,` `string` | IP-Pool, von dem aus die E-Mail gesendet wurde
`bounce_reason` | `null,` `string` | [PII] Der SMTP Grund Code und die Nutzer:in Nachricht, die für dieses Bounce-Ereignis empfangen wurde
`esp` | `null,` `string` | ESP für das Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,` `string` | Absenderdomain für die E-Mail
`is_drop` | `null, boolean` | Zeigt an, dass dieses Event als Löschen-Event zählt
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_CLICK_SHARED {#USERS_MESSAGES_EMAIL_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`email_address` | `string` | [PII] E-Mail Adresse des Nutzers:innen
`url` | `null,` `string` | URL, auf die der Benutzer geklickt hat
`user_agent` | `null,` `string` | Nutzeragent, auf dem der Klick erfolgte
`ip_pool` | `null,` `string` | IP-Pool, von dem aus die E-Mail gesendet wurde
`link_id` | `null,` `string` | Eindeutige ID für den angeklickten Link, wie von Braze erstellt
`link_alias` | `null,` `string` | Alias, der mit dieser Link-ID verknüpft ist
`esp` | `null,` `string` | ESP für das Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,` `string` | Absenderdomain für die E-Mail
`is_amp` | `null, boolean` | Zeigt an, dass es sich um ein AMP-Event handelt
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`suspected_bot_click_reason` | `null, object` | Warum dieses Ereignis als Bot eingestuft wurde
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_EMAIL_DEFERRAL_SHARED {#USERS_MESSAGES_EMAIL_DEFERRAL_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | BSON ID der Kampagne, zu der dieses Ereignis gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`email_address` | `null,` `string` | [PII] E-Mail Adresse des Nutzers:innen
`recipient_domain` | `null,` `string` | E-Mail Domain des Empfängers
`esp` | `null,` `string` | ESP für das Ereignis (Sparkpost oder SendGrid oder Amazon SES)
`from_domain` | `null,` `string` | Absenderdomain für die E-Mail
`ip_pool` | `null,` `string` | IP-Pool, von dem aus die E-Mail versendet wurde
`sending_ip` | `null,` `string` | IP-Adresse, von der aus die E-Mail gesendet wurde
`timezone` | `null,` `string` | Zeitzone des Benutzers
`deferral_reason` | `null,` `string` | [PII] Der SMTP Grund Code und die Nutzer:in Nachricht, die für dieses Aufschiebungsereignis empfangen wurde
`attempt_count` | `null, int` | Anzahl der Versuche, die Nachricht zu versenden
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_DELIVERY_SHARED {#USERS_MESSAGES_EMAIL_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`email_address` | `string` | [PII] E-Mail Adresse des Nutzers:innen
`sending_ip` | `null,` `string` | IP-Adresse, von der die E-Mail gesendet wurde
`ip_pool` | `null,` `string` | IP-Pool, von dem aus die E-Mail gesendet wurde
`esp` | `null,` `string` | ESP für das Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,` `string` | Absenderdomain für die E-Mail
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED {#USERS_MESSAGES_EMAIL_MARKASSPAM_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`email_address` | `string` | [PII] E-Mail Adresse des Nutzers:innen
`user_agent` | `null,` `string` | Benutzer-Agent, auf dem die Spam-Meldung erfolgte
`ip_pool` | `null,` `string` | IP-Pool, von dem aus die E-Mail gesendet wurde
`esp` | `null,` `string` | ESP für das Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,` `string` | Absenderdomain für die E-Mail
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_OPEN_SHARED {#USERS_MESSAGES_EMAIL_OPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`email_address` | `string` | [PII] E-Mail Adresse des Nutzers:innen
`user_agent` | `null,` `string` | Benutzer-Agent, auf dem das Öffnen erfolgte
`ip_pool` | `null,` `string` | IP-Pool, von dem aus die E-Mail gesendet wurde
`machine_open` | `null,` `string` | Wird auf „wahr“ gesetzt, wenn das offene Event ohne Nutzereingriff getriggert wird, z. B. durch ein Apple-Gerät mit aktiviertem E-Mail-Datenschutz. Der Wert kann sich im Laufe der Zeit ändern, um mehr Granularität zu bieten.
`esp` | `null,` `string` | ESP für das Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,` `string` | Absenderdomain für die E-Mail
`is_amp` | `null, boolean` | Zeigt an, dass es sich um ein AMP-Event handelt
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SEND_SHARED {#USERS_MESSAGES_EMAIL_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`email_address` | `string` | [PII] E-Mail Adresse des Nutzers:innen
`ip_pool` | `null,` `string` | IP-Pool, von dem aus die E-Mail gesendet wurde
`message_extras` | `null,` `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während der Liquid-Darstellung
`esp` | `null,` `string` | ESP für das Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,` `string` | Absenderdomain für die E-Mail
`sf_created_at` | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED {#USERS_MESSAGES_EMAIL_SOFTBOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`email_address` | `string` | [PII] E-Mail Adresse des Nutzers:innen
`sending_ip` | `null,` `string` | IP-Adresse, von der aus die E-Mail gesendet wurde
`ip_pool` | `null,` `string` | IP-Pool, von dem aus die E-Mail gesendet wurde
`bounce_reason` | `null,` `string` | [PII] Der SMTP Grund Code und die Nutzer:in Nachricht, die für dieses Bounce-Ereignis empfangen wurde
`esp` | `null,` `string` | ESP für das Ereignis (SparkPost, SendGrid oder Amazon SES)
`from_domain` | `null,` `string` | Absenderdomain für die E-Mail
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED {#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`email_address` | `string` | [PII] E-Mail Adresse des Nutzers:innen
`ip_pool` | `null,` `string` | IP-Pool, von dem aus die E-Mail gesendet wurde
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED {#USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_id` | `null,` `string` | BSON ID der Kampagne, zu der dieses Ereignis gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`feature_flag_id_name` | `null,` `string` | Der Feature-Flag Rollout Bezeichner
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`browser` | `null,` `string` | Gerätebrowser - extrahiert aus user_agent \- auf dem die Öffnung erfolgte
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`device_model` | `null,` `string` | Modell des Geräts
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`platform` | `null,` `string` | Plattform des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`timezone` | `null,` `string` | Zeitzone des Benutzers
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED {#USERS_MESSAGES_INAPPMESSAGE_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`card_api_id` | `null,` `string` | API-ID der Karte
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Browser des Geräts
`version` | `string` | Welche Version der In-App-Nachricht, Legacy oder Triggered
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Eine von `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (maximal 2.000 Zeichen)
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED {#USERS_MESSAGES_INAPPMESSAGE_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`card_api_id` | `null,` `string` | API-ID der Karte
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Browser des Geräts
`version` | `string` | welche Version der In-App-Nachricht, Legacy oder ausgelöst
`button_id` | `null,` `string` | ID des angeklickten Buttons, wenn dieser Klick einen Klick auf einen Button darstellt
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Eine von `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED {#USERS_MESSAGES_INAPPMESSAGE_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`card_api_id` | `null,` `string` | API-ID der Karte
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Browser des Geräts
`version` | `string` | welche Version der In-App-Nachricht, Legacy oder ausgelöst
`ad_id` | `null,` `string` | [PII] Bezeichner der Werbung
`ad_id_type` | `null,` `string` | Eine von `ios_idfa`, `google_ad_id`, `windows_ad_id`, OR `roku_ad_id`
`ad_tracking_enabled` | `null, boolean` | Ob die Werbeverfolgung für das Gerät aktiviert ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`message_extras` | `null,` `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare beim Liquid-Rendering
`locale_key` | `null,` `string` | [PII] Der Schlüssel, der den Übersetzungen (z.B. 'en-us') entspricht, die zum Verfassen dieser Nachricht verwendet wurden (Standard: null).
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_ABORT_SHARED {#USERS_MESSAGES_LINE_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (bis zu 128 Zeichen)
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`line_channel_id` | `null,` `string` | Die ID des LINE-Kanals, an den die Nachricht gesendet oder von dem sie empfangen wurde
`line_channel_name` | `null,` `string` | Der Name des LINE-Kanals, an den die Nachricht gesendet oder von dem sie empfangen wurde
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`native_line_id` | `null,` `string` | [PII] Die Line ID des Nutzers:innen, an den die Nachricht gesendet oder von dem sie empfangen wurde
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`timezone` | `null,` `string` | Zeitzone des Benutzers
`campaign_name` | `null,` `string` | Name der Kampagne
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_CLICK_SHARED {#USERS_MESSAGES_LINE_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`timezone` | `null,` `string` | Zeitzone des Benutzers
`native_line_id` | `null,` `string` | [PII] Die Line ID des Nutzers:innen, an den die Nachricht gesendet oder von dem sie empfangen wurde
`line_channel_id` | `null,` `string` | Die ID des LINE-Kanals, an den die Nachricht gesendet oder von dem sie empfangen wurde
`line_channel_name` | `null,` `string` | Der Name des LINE-Kanals, an den die Nachricht gesendet oder von dem sie empfangen wurde
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_name` | `null,` `string` | Name der Kampagne
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`short_url` | `null,` `string` | Verkürzte Url, die angeklickt wurde
`url` | `null,` `string` | URL, auf die der Benutzer geklickt hat
`user_agent` | `null,` `string` | Benutzer-Agent, auf dem die Spam-Meldung erfolgte
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_LINE_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_name` | `null,` `string` | Name der Kampagne
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`line_channel_id` | `null,` `string` | Die ID des LINE-Kanals, an den die Nachricht gesendet oder von dem sie empfangen wurde
`line_channel_name` | `null,` `string` | Der Name des LINE-Kanals, an den die Nachricht gesendet oder von dem sie empfangen wurde
`media_id` | `null,` `string` | Die von LINE generierte ID, die zum Abrufen eingehender Medien von LINE verwendet werden kann
`message_body` | `null,` `string` | Getippte Antwort des Nutzers:in
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`native_line_id` | `null,` `string` | [PII] Die Line ID des Nutzers:innen, an den die Nachricht gesendet oder von dem sie empfangen wurde
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`timezone` | `null,` `string` | Zeitzone des Benutzers
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LINE_SEND_SHARED {#USERS_MESSAGES_LINE_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_name` | `null,` `string` | Name der Kampagne
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`line_channel_id` | `null,` `string` | Die ID des LINE-Kanals, an den die Nachricht gesendet oder von dem sie empfangen wurde
`line_channel_name` | `null,` `string` | Der Name des LINE-Kanals, an den die Nachricht gesendet oder von dem sie empfangen wurde
`message_extras` | `null,` `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare beim Liquid-Rendering
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`native_line_id` | `null,` `string` | [PII] Die Line ID des Nutzers:innen, an den die Nachricht gesendet oder von dem sie empfangen wurde
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`timezone` | `null,` `string` | Zeitzone des Benutzers
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED {#USERS_MESSAGES_LIVEACTIVITY_OUTCOME_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`activity_id` | `null,` `string` | Live Bezeichner der Aktivität
`activity_attributes_type` | `null,` `string` | Live Aktivität Attribut Typ
`push_to_start_token` | `null,` `string` | Live Activity Push zum Starten des Tokens
`update_token` | `null,` `string` | Update-Token für Live-Aktivitäten
`live_activity_event_type` | `null,` `string` | Veranstaltungstyp der Live-Aktivität. Eine von ['start', 'update', 'end']
`live_activity_event_outcome` | `null,` `string` | Ergebnis der Veranstaltung Live Activity
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED {#USERS_MESSAGES_LIVEACTIVITY_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`activity_id` | `null,` `string` | Live Bezeichner der Aktivität
`activity_attributes_type` | `null,` `string` | Live Aktivität Attribut Typ
`push_to_start_token` | `null,` `string` | Live Activity Push zum Starten des Tokens
`update_token` | `null,` `string` | Update-Token für Live-Aktivitäten
`live_activity_event_type` | `null,` `string` | Veranstaltungstyp der Live-Aktivität. Eine von ['start', 'update', 'end']
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`card_api_id` | `null,` `string` | API-ID der Karte
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Gerätebrowser - extrahiert aus user_agent \- auf dem die Öffnung erfolgte
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (bis zu 128 Zeichen)
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`card_api_id` | `null,` `string` | API-ID der Karte
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Gerätebrowser - extrahiert aus user_agent \- auf dem die Öffnung erfolgte
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED {#USERS_MESSAGES_NEWSFEEDCARD_IMPRESSION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`card_api_id` | `null,` `string` | API-ID der Karte
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Gerätebrowser - extrahiert aus user_agent \- auf dem die Öffnung erfolgte
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` dass wir einen Lieferversuch unternommen haben, um
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`platform` | `string` | Plattform des Geräts
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (maximal 2.000 Zeichen)
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_BOUNCE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`push_token` | `null,` `string` | Push-Token, der nicht funktioniert
`device_id` | `null,` `string` | `device_id` an die wir einen Zustellungsversuch unternommen haben, der geplatzt ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`platform` | `null,` `string` | Plattform des Geräts
`ad_id` | `null,` `string` | [PII] Werbe-ID des Geräts, an das wir eine Zustellung versucht haben
`ad_id_type` | `null,` `string` | Typ der Ad-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_INFLUENCEDOPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Browser des Geräts
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_IOSFOREGROUND_SHARED}

{% alert important %}
Dieses Ereignis wird vom [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) nicht unterstützt und ist im [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) veraltet.
{% endalert %}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Browser des Geräts
`ad_id` | `null,` `string` | [PII] Werbe-ID des Geräts, an das wir eine Zustellung versucht haben
`ad_id_type` | `null,` `string` | Typ der Ad-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_OPEN_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`sdk_version` | `null,` `string` | Version des Braze-SDK, die während des Events verwendet wird
`platform` | `null,` `string` | Plattform des Geräts
`os_version` | `null,` `string` | Version des Betriebssystems des Geräts
`device_model` | `null,` `string` | Modell des Geräts
`resolution` | `null,` `string` | Auflösung des Geräts
`carrier` | `null,` `string` | Netzbetreiber des Geräts
`browser` | `null,` `string` | Browser des Geräts
`button_string` | `null,` `string` | Bezeichner (button_string) des angeklickten Buttons der Push-Benachrichtigung. null, wenn nicht von einem Klick auf den Button
`button_action_type` | `null,` `string` | Aktiontyp des Buttons „Push-Benachrichtigung“. Eine der Optionen [URI, DEEP_LINK, NONE, CLOSE]. null, wenn nicht durch einen Klick auf einen Button
`slide_id` | `null,` `string` | Bezeichner der Folie des Push-Karussells, auf die der oder die Nutzer:in klickt
`slide_action_type` | `null,` `string` | Aktionstyp der Folie „Push-Karussell“
`ad_id` | `null,` `string` | [PII] Werbe-ID des Geräts, an das wir eine Zustellung versucht haben
`ad_id_type` | `null,` `string` | Typ der Ad-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED {#USERS_MESSAGES_PUSHNOTIFICATION_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`push_token` | `null,` `string` | Push-Token für einen Zustellversuch
`device_id` | `null,` `string` | `device_id` dass wir einen Lieferversuch unternommen haben, um
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`app_api_id` | `null,` `string` | API-ID der App, in der dieses Ereignis aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`platform` | `string` | Plattform des Geräts
`ad_id` | `null,` `string` | [PII] Werbe-ID des Geräts, an das wir eine Zustellung versucht haben
`ad_id_type` | `null,` `string` | Typ der Ad-ID
`ad_tracking_enabled` | `null, boolean` | Ob Tracking für Werbung aktiviert ist oder nicht
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`message_extras` | `null,` `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare beim Liquid-Rendering
`is_sampled` | `null,` `string` | Zeigt an, ob der Push-Versand abgetastet wurde und ein Zustellungsereignis erwartet wird
`locale_key` | `null,` `string` | [PII] Der Schlüssel, der den Übersetzungen (z.B. 'en-us') entspricht, die zum Verfassen dieser Nachricht verwendet wurden (Standard: null).
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_ABORT_SHARED {#USERS_MESSAGES_RCS_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (bis zu 128 Zeichen)
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`campaign_name` | `null,` `string` | Name der Kampagne
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,` `string` | Name des Canvas
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`canvas_variation_name` | `null,` `string` | Name der Canvas-Variante, die dieser Nutzer:in erhalten hat
`message_variation_name` | `null,` `string` | Name der Variation der Nachricht
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_CLICK_SHARED {#USERS_MESSAGES_RCS_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`campaign_name` | `null,` `string` | Name der Kampagne
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,` `string` | Name des Canvas
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`message_variation_name` | `null,` `string` | Name der Variation der Nachricht
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`short_url` | `null,` `string` | Verkürzte Url, die angeklickt wurde
`suspected_bot_click_reason` | `null,` `string` | Warum dieses Ereignis als Bot eingestuft wurde
`user_agent` | `null,` `string` | Benutzer-Agent, auf dem die Spam-Meldung erfolgte
`user_phone_number` | `null,` `string` | [PII] Die Telefonnummer des Nutzers:innen, von dem die Nachricht empfangen wurde
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`interaction_type` | `null,` `string` | Die Art der Interaktion, die den Klick ausgelöst hat. Beispiel String-Werte: Text-URL, Antwort, OpenURL
`element_label` | `null,` `string` | Optionale Details zum angeklickten Element, z. B. der Text eines Antwortvorschlags oder eines Buttons
`element_type` | `null,` `string` | Gibt an, ob eine interaction_type, die für alle Vorschläge und Buttons gleich ist, von einem Vorschlag oder Button stammt. Beispiele: Anregung, Button
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`url` | `null,` `string` | URL, auf die der Benutzer geklickt hat
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`canvas_variation_name` | `null,` `string` | Name der Canvas-Variante, die dieser Nutzer:in erhalten hat
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_DELIVERY_SHARED {#USERS_MESSAGES_RCS_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`campaign_name` | `null,` `string` | Name der Kampagne
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,` `string` | Name des Canvas
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`canvas_variation_name` | `null,` `string` | Name der Canvas-Variante, die dieser Nutzer:in erhalten hat
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`message_variation_name` | `null,` `string` | Name der Variation der Nachricht
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Nutzers:innen, der die Nachricht erhält, im Format e.164 (zum Beispiel +14155552671)
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`from_rcs_sender` | `null,` `string` | Die RCS-Sender ID oder der Name des Agenten, der die Nachricht versendet hat
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_RCS_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`action` | `null,` `string` | Aktion, die als Antwort auf diese Nachricht durchgeführt wurde. (zum Beispiel Abonnent:in, Abgemeldet oder Keine).
`campaign_name` | `null,` `string` | Name der Kampagne
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,` `string` | Name des Canvas
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`media_urls` | `null,` `string` | Medien-URLs von dem oder der Nutzer:in
`message_variation_name` | `null,` `string` | Name der Variation der Nachricht
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`user_phone_number` | `null,` `string` | [PII] Die Telefonnummer des Nutzers:innen, von dem die Nachricht empfangen wurde
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`message_body` | `null,` `string` | Getippte Antwort des Nutzers:in
`to_rcs_sender` | `null,` `string` | Der eingehende RCS-Sender, an den die Nachricht gesendet wurde
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_id` | `null,` `string` | BSON ID der Kampagne, zu der dieses Ereignis gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_READ_SHARED {#USERS_MESSAGES_RCS_READ_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`campaign_name` | `null,` `string` | Name der Kampagne
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,` `string` | Name des Canvas
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`canvas_variation_name` | `null,` `string` | Name der Canvas-Variante, die dieser Nutzer:in erhalten hat
`message_variation_name` | `null,` `string` | Name der Variation der Nachricht
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Nutzers:innen, der die Nachricht erhält, im Format e.164 (zum Beispiel +14155552671)
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_REJECTION_SHARED {#USERS_MESSAGES_RCS_REJECTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`campaign_name` | `null,` `string` | Name der Kampagne
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,` `string` | Name des Canvas
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`canvas_variation_name` | `null,` `string` | Name der Canvas-Variante, die dieser Nutzer:in erhalten hat
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`error` | `null,` `string` | Fehler-Name
`from_rcs_sender` | `null,` `string` | Die RCS-Sender ID oder der Name des Agenten, der die Nachricht versendet hat
`is_sms_fallback` | `null, boolean` | Zeigt an, ob ein SMS Fallback für diese abgelehnte RCS Nachricht versucht wurde. Es ist mit dem Ereignis SMS-Zustellung verknüpft/gepaart
`message_variation_name` | `null,` `string` | Name der Variation der Nachricht
`provider_error_code` | `null,` `string` | Fehlercode des Anbieters
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Nutzers:innen, der die Nachricht erhält, im Format e.164 (zum Beispiel +14155552671)
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_RCS_SEND_SHARED {#USERS_MESSAGES_RCS_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`campaign_name` | `null,` `string` | Name der Kampagne
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_name` | `null,` `string` | Name des Canvas
`canvas_step_name` | `null,` `string` | Name des Canvas-Schrittes
`canvas_variation_name` | `null,` `string` | Name der Canvas-Variante, die dieser Nutzer:in erhalten hat
`category` | `null,` `string` | Name der Schlüsselwortkategorie, wird nur für automatische Nachrichten ausgefüllt: 'Opt-in', 'Opt-out', 'Hilfe' oder angepasster Wert
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`from_rcs_sender` | `null,` `string` | Die RCS-Sender ID oder der Name des Agenten, der die Nachricht versendet hat
`message_extras` | `null,` `string` | Ein JSON-String der getaggten Schlüssel-Wert-Paare beim Liquid-Rendering
`message_variation_name` | `null,` `string` | Name der Variation der Nachricht
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Nutzers:innen, der die Nachricht erhält, im Format e.164 (zum Beispiel +14155552671)
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_ABORT_SHARED {#USERS_MESSAGES_SMS_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`subscription_group_api_id` | `null,` `string` | Externe ID der Abonnementgruppe
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (maximal 2.000 Zeichen)
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_CARRIERSEND_SHARED {#USERS_MESSAGES_SMS_CARRIERSEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Empfängers:in
`from_phone_number` | `null,` `string` | Rufnummer, von der aus die SMS-Nachricht gesendet wurde
`subscription_group_api_id` | `null,` `string` | externe ID der Abonnementgruppe
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERY_SHARED {#USERS_MESSAGES_SMS_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Empfängers:in
`from_phone_number` | `null,` `string` | Rufnummer, von der aus die SMS-Nachricht gesendet wurde
`subscription_group_api_id` | `null,` `string` | Externe ID der Abonnementgruppe
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`is_sms_fallback` | `null, boolean` | Zeigt an, ob ein SMS Fallback für diese abgelehnte RCS Nachricht versucht wurde. Es ist mit dem Ereignis SMS-Zustellung verknüpft/gepaart
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED {#USERS_MESSAGES_SMS_DELIVERYFAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Empfängers:in
`subscription_group_api_id` | `null,` `string` | externe ID der Abonnementgruppe
`error` | `null,` `string` | Fehlername
`provider_error_code` | `null,` `string` | Fehlercode vom SMS-Dienstanbieter
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`is_sms_fallback` | `null, boolean` | Zeigt an, ob ein SMS Fallback für diese abgelehnte RCS Nachricht versucht wurde. Es ist mit dem Ereignis SMS-Zustellung verknüpft/gepaart
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_SMS_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `null,` `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, der mit der eingehenden Rufnummer verbunden ist
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_phone_number` | `string` | [PII] die Telefonnummer des Nutzers:innen, von dem die Nachricht empfangen wurde
`subscription_group_id` | `null,` `string` | ID der Abonnentengruppe, an die sich diese SMS-Nachricht richtet
`subscription_group_api_id` | `null,` `string` | API-ID der Abonnentengruppe, auf die diese SMS-Nachricht abzielt
`inbound_phone_number` | `string` | Die eingehende Nummer, an die die Nachricht gesendet wurde
`action` | `string` | Als Antwort auf diese Nachricht durchgeführte Aktion. Zum Beispiel `Subscribed`, `Unsubscribed`, oder `None`.
`message_body` | `string` | Antwort von dem oder der Nutzer:in
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | Medien-URLs von dem oder der Nutzer:in
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariante, zu der dieses Ereignis gehört
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation für den Canvas-Schritt, zu der dieses Event gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_REJECTION_SHARED {#USERS_MESSAGES_SMS_REJECTION_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Empfängers:in
`from_phone_number` | `null,` `string` | Rufnummer, von der aus die SMS-Nachricht gesendet wurde
`subscription_group_api_id` | `null,` `string` | externe ID der Abonnementgruppe
`error` | `null,` `string` | Fehlername
`provider_error_code` | `null,` `string` | Fehlercode vom SMS-Dienstanbieter
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`is_sms_fallback` | `null, boolean` | Zeigt an, ob ein SMS Fallback für diese abgelehnte RCS Nachricht versucht wurde. Es ist mit dem Ereignis SMS-Zustellung verknüpft/gepaart
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SEND_SHARED {#USERS_MESSAGES_SMS_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Empfängers:in
`subscription_group_api_id` | `null,` `string` | externe ID der Abonnementgruppe
`category` | `null,` `string` | Stichwort Kategorie-Name, wird nur für automatische Antwortnachrichten ausgefüllt: „Opt-in“, „Opt-out“, „Hilfe“ oder angepasster Wert
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`message_extras` | `null,` `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare beim Liquid-Rendering
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED {#USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `null,` `string` | Braze ID des Nutzers, auf den short_url, abzielt null, wenn short_url kein Tracking von Nutzer:innen-Klicks verwendet hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers, auf den short_url Targeting betreibt, falls vorhanden, null, wenn short_url kein Tracking von Nutzer:innen verwendet hat
`app_group_api_id` | `null,` `string` | API ID des Workspace, der zur Generierung verwendet wird short_url
`time` | `int` | Unix-Zeitstempel, zu dem short_url angeklickt wurde
`timezone` | `null,` `string` | Zeitzone des Benutzers
`campaign_id` | `null,` `string` | Braze ID der Kampagne, für die short_url generiert wurde, null, wenn nicht aus einer Kampagne
`campaign_api_id` | `null,` `string` | API ID der Kampagne, für die short_url generiert wurde, null, wenn nicht aus einer Kampagne
`message_variation_api_id` | `null,` `string` | API ID der Nachrichtenvariation, für die short_url generiert wurde, null, wenn nicht aus einer Kampagne
`canvas_id` | `null,` `string` | Braze ID des Canvas, für den short_url generiert wurde, null, wenn nicht von einem Canvas
`canvas_api_id` | `null,` `string` | API ID des Canvas, für den short_url generiert wurde, null, wenn nicht von einem Canvas
`canvas_variation_api_id` | `null,` `string` | API ID der Canvas-Variante, für die short_url generiert wurde, null, wenn nicht von einem Canvas
`canvas_step_api_id` | `null,` `string` | API ID des Canvas-Schrittes, für den short_url generiert wurde, null, wenn nicht von einem Canvas
`canvas_step_message_variation_api_id` | `null,` `string` | API ID des Canvas-Schrittes, für den die Nachrichtenvariation short_url generiert wurde, null, wenn nicht von einem Canvas
`url` | `string` | Original-URL in der Nachricht, auf die die Weiterleitung durch short_url
`short_url` | `string` | verkürzte URL, die angeklickt wurde
`user_agent` | `null,` `string` | Nutzer:in, die eine Anfrage stellen short_url
`user_phone_number` | `string` | [PII] die Telefonnummer der Nutzer:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`is_suspected_bot_click` | `null, boolean` | Ob dieses Ereignis als Bot-Ereignis verarbeitet wurde
`suspected_bot_click_reason` | `null, object` | Warum dieses Ereignis als Bot eingestuft wurde
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_ABORT_SHARED {#USERS_MESSAGES_WEBHOOK_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (maximal 2.000 Zeichen)
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WEBHOOK_FAILURE_SHARED {#USERS_MESSAGES_WEBHOOK_FAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`http_status_code` | `null, int` | HTTP Status Code der Antwort
`endpoint_url` | `null,` `string` | Die angefragte Url des Endpunkts
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`campaign_id` | `null,` `string` | BSON ID der Kampagne, zu der dieses Ereignis gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`content_length` | `null, int` | Inhaltliche Länge der Antwort
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`host` | `null,` `string` | Der Host für die Anfrage
`id` | `string` | Globale eindeutige ID für dieses Event
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`raw_response` | `null,` `string` | Abgeschnittene Rohantwort vom Endpunkt
`retry_count` | `null, int` | Die Anzahl der versuchten Wiederholungsversuche
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`url_path` | `null,` `string` | Der Pfad der angefragten Url
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`webhook_duration` | `null, int` | Gesamtdauer dieser Anfrage in Millisekunden
`webhook_failure_source` | `null,` `string` | Um festzustellen, ob ein Fehler von Braze oder vom Endpunkt selbst verursacht wurde. Das Quellfeld könnte Externer Endpunkt sein, Treat no status code to host unreachable
`is_terminal` | `null, boolean` | Ob dieses Ereignis der letzte Versuch eines Sendevorgangs war
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WEBHOOK_SEND_SHARED {#USERS_MESSAGES_WEBHOOK_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`gender` | `null,` `string` | [PII] Geschlecht der Nutzer:innen
`country` | `null,` `string` | [PII] Land des Nutzers:innen
`timezone` | `null,` `string` | Zeitzone des Benutzers
`language` | `null,` `string` | [PII] Sprache des Nutzers:innen
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`message_extras` | `null,` `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare beim Liquid-Rendering
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_ABORT_SHARED {#USERS_MESSAGES_WHATSAPP_ABORT_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`to_phone_number` | 	`null,` `string` | [PII] Telefonnummer des Empfängers:in
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`timezone` | `null,` `string` | Zeitzone des Benutzers
`app_group_id` | `null,` `string` | ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`abort_type` | `null,` `string` | Art des Abbruchs, eine von ['liquid_abort_message', 'quiet_hours', 'rate_limit']
`abort_log` | `null,` `string` | [PII] Protokollnachricht, die Details zum Abbruch beschreibt (maximal 2.000 Zeichen)
`sf_created_at` | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde      
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


### USERS_MESSAGES_WHATSAPP_CLICK_SHARED {#USERS_MESSAGES_WHATSAPP_CLICK_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`user_id` | `string` | Braze ID des Nutzers:innen, der dieses Ereignis durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzer:innen
`device_id` | `null,` `string` | ID des Geräts, auf dem das Event aufgetreten ist
`app_group_id` | `null,` `string` | BSON ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`app_group_api_id` | `null,` `string` | API ID der App-Gruppe, zu der dieser Nutzer:innen gehört
`time` | `int` | UNIX-Zeitstempel, zu dem das Ereignis eingetreten ist
`timezone` | `null,` `string` | Zeitzone des Benutzers
`campaign_id` | `null,` `string` | BSON ID der Kampagne, zu der dieses Ereignis gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | BSON ID des Canvas, zu dem dieses Ereignis gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`url` | `null,` `string` | URL, auf die der Benutzer geklickt hat
`short_url` | `null,` `string` | Verkürzte Url, die angeklickt wurde
`user_agent` | `null,` `string` | Benutzer-Agent, auf dem die Spam-Meldung erfolgte
`user_phone_number` | `null,` `string` | [PII] Die Telefonnummer des Nutzers:innen, von dem die Nachricht empfangen wurde
`sf_created_at` | `timestamp`, `null` | als dieses Ereignis von der Snowpipe aufgegriffen wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED {#USERS_MESSAGES_WHATSAPP_DELIVERY_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Empfängers:in
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`timezone` | `null,` `string` | Zeitzone des Benutzers
`from_phone_number` | `null,` `string` | Rufnummer, von der aus die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,` `string` | ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`sf_created_at` | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde      
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`flow_id` | `null,` `string` | Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn der Nutzer:in auf einen WhatsApp Flow antwortet.
`template_name` | `null,` `string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn Sie eine Template Nachricht senden
`message_id` | `null,` `string` | Die eindeutige ID, die von Meta für diese Nachricht generiert wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_FAILURE_SHARED {#USERS_MESSAGES_WHATSAPP_FAILURE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Empfängers:in
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`timezone` | `null,` `string` | Zeitzone des Benutzers
`from_phone_number` | `null,` `string` | Rufnummer, von der aus die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,` `string` | ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`provider_error_code` | `null,` `string` | Fehlercode von WhatsApp
`provider_error_title` | `null, ` `string` | Fehlertitel von WhatsApp
`sf_created_at` | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde      
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`message_id` | `null,` `string` | Die eindeutige ID, die von Meta für diese Nachricht generiert wurde
`template_name` | `null,` `string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn Sie eine Template Nachricht senden
`flow_id` | `null,` `string` | Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn der Nutzer:in auf einen WhatsApp Flow antwortet.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED {#USERS_MESSAGES_WHATSAPP_INBOUNDRECEIVE_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`user_phone_number` | `string` | [PII] die Telefonnummer des Nutzers:innen, von dem die Nachricht empfangen wurde
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`inbound_phone_number` | `string` | Die eingehende Nummer, an die die Nachricht gesendet wurde
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`timezone` | `null,` `string` | Zeitzone des Benutzers
`app_group_id` | `null,` `string` | ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`message_body` | `string` | Antwort von dem oder der Nutzer:in
`quick_reply_text` | `string` | Text der vom Benutzer gedrückten Taste
`media_urls` | `null, {"type"=>"array", "items"=>["null", "string"]}` | Medien-URLs von dem oder der Nutzer:in
`action` | `string` | Als Antwort auf diese Nachricht durchgeführte Aktion. Zum Beispiel `Subscribed`, `Unsubscribed`, oder `None`.
`sf_created_at` | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde      
`catalog_id` | `null,` `string` | Katalog ID eines Produkts, wenn ein Produkt in der eingehenden Nachricht referenziert wird. Andernfalls ist sie leer.
`product_id` | `null,` `string` | ID des gekauften Produkts
`flow_id` | `null,` `string` | Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn der Nutzer:in auf einen WhatsApp Flow antwortet.
`flow_response_json` | `null,` `string` | [PII] Die Formularwerte, die der Nutzer:innen eingegeben hat. Vorhanden, wenn der Nutzer:in auf einen WhatsApp Flow antwortet.
`message_id` | `null,` `string` | Die eindeutige ID, die von Meta für diese Nachricht generiert wurde
`in_reply_to` | `null,` `string` | Die message_id der Nachricht, auf die diese Nachricht geantwortet hat
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_READ_SHARED {#USERS_MESSAGES_WHATSAPP_READ_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`to_phone_number` | `null,` `string` | [PII] Telefonnummer des Empfängers:in
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`timezone` | `null,` `string` | Zeitzone des Benutzers
`from_phone_number` | `null,` `string` | Rufnummer, von der aus die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,` `string` | ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`sf_created_at` | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde      
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`template_name` | `null,` `string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn Sie eine Template Nachricht senden
`message_id` | `null,` `string` | Die eindeutige ID, die von Meta für diese Nachricht generiert wurde
`flow_id` | `null,` `string` | Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn der Nutzer:in auf einen WhatsApp Flow antwortet.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_MESSAGES_WHATSAPP_SEND_SHARED {#USERS_MESSAGES_WHATSAPP_SEND_SHARED}

Feld | Typ | Beschreibung
------|------|------------
`id` | `string` | Globale eindeutige ID für dieses Event
`time` | `int` | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist
`to_phone_number` | `null,` `string`	| [PII] Telefonnummer des Empfängers:in
`user_id` | `string` | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat
`external_user_id` | `null,` `string` | [PII] Externe ID des Nutzers:innen
`device_id` | `null,` `string` | `device_id` die an diesen Benutzer gebunden ist, wenn der Benutzer anonym ist
`timezone` | `null,` `string` | Zeitzone des Benutzers
`from_phone_number` | `null,` `string` | Telefonnummer, von der die WhatsApp-Nachricht gesendet wurde
`app_group_id` | `null,` `string` | ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`app_group_api_id` | `null,` `string` | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört
`subscription_group_api_id` | `string` | API-ID der Abonnementgruppe
`campaign_id` | `null,` `string` | Intern verwendete Braze-ID der Kampagne, zu der dieses Event gehört
`campaign_api_id` | `null,` `string` | API-ID der Kampagne, zu der dieses Event gehört
`message_variation_api_id` | `null,` `string` | API-ID der Nachrichtenvariation, die dieser Benutzer erhalten hat
`canvas_id` | `null,` `string` | Interne Braze-ID des Canvas, zu dem dieses Event gehört
`canvas_api_id` | `null,` `string` | API-ID des Canvas, zu dem dieses Event gehört
`canvas_variation_api_id` | `null,` `string` | API-ID der Canvas-Variation, zu der dieses Ereignis gehört
`canvas_step_api_id` | `null,` `string` | API-ID des Canvas-Schritts, zu dem dieses Event gehört
`canvas_step_message_variation_api_id` | `null,` `string` | API-ID der Canvas-Schritt-Nachrichtenvariante, die dieser Benutzer erhalten hat
`dispatch_id` | `null,` `string` | ID der Sendung, zu der diese Nachricht gehört
`message_extras` | `null,` `string` | [PII] Ein JSON-String der getaggten Schlüssel-Wert-Paare während der Liquid-Darstellung
`sf_created_at` | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde      
`send_id` | `null,` `string` | ID zum Senden von Nachrichten, zu denen diese Nachricht gehört
`flow_id` | `null,` `string` | Die eindeutige ID des Flows im WhatsApp Manager:in. Vorhanden, wenn der Nutzer:in auf einen WhatsApp Flow antwortet.
`template_name` | `null,` `string` | [PII] Name des Templates im WhatsApp Manager. Vorhanden, wenn Sie eine Template Nachricht senden
`message_id` | `null,` `string` | Die eindeutige ID, die von Meta für diese Nachricht generiert wurde
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Nutzer:innen

### USERS_RANDOMBUCKETNUMBERUPDATE_SHARED {#USERS_RANDOMBUCKETNUMBERUPDATE_SHARED}

| Feld                       | Typ                     | Beschreibung                                        |
| --------------------------- | ------------------------ | -------------------------------------------------- |
| `id`                        | `string`, `null`    | Globale eindeutige ID für dieses Event                  |
| `app_group_id`              | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört      |
| `app_group_api_id`          | `string`, `null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört       |
| `user_id`                   | `string`, `null`    | Braze-ID des Nutzers oder der Nutzerin, der oder die dieses Event durchgeführt hat      |
| `external_user_id`          | `string`, `null`    | [PII] Externe ID des Nutzers:innen                 |
| `time`                      | `int`, `null`       | Unix-Zeitstempel, zu dem das Ereignis eingetreten ist         |
| `random_bucket_number`      | `int`, `null`       | Aktuelle zufällige Bucket-Nummer, die dem oder der Nutzer:in zugewiesen wurde  |
| `prev_random_bucket_number` | `int`, `null`       | Vorherige zufällige Bucket-Nummer, die dem oder der Nutzer:in zugewiesen wurde |
| `sf_created_at`             | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERDELETEREQUEST_SHARED {#USERS_USERDELETEREQUEST_SHARED}

| Feld              | Typ                     | Beschreibung                                                   |
| ------------------ | ------------------------ | ------------------------------------------------------------- |
| `id`               | `string`, `null`    | Globale eindeutige ID für dieses Event                             |
| `user_id`          | `string`, `null`    | Braze ID des Benutzers, der gelöscht wurde                          |
| `app_group_id`     | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                 |
| `app_group_api_id` | `string`, `null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                  |
| `time`             | `int`, `null`       | Unix-Zeitstempel, zu dem die Löschanfrage des Benutzers bearbeitet wurde |
| `sf_created_at`    | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### USERS_USERORPHAN_SHARED {#USERS_USERORPHAN_SHARED}

| Feld              | Typ                     | Beschreibung                                                                   |
| ------------------ | ------------------------ | ----------------------------------------------------------------------------- |
| `id`               | `string`, `null`    | Globale eindeutige ID für dieses Event                                             |
| `user_id`          | `string`, `null`    | Braze ID des Benutzers, der verwaist wurde                                         |
| `external_user_id` | `string`, `null`    | [PII] Externe ID des Nutzers:innen                                            |
| `device_id`        | `string`, `null`    | ID des Geräts, das mit diesem Benutzer verbunden ist, wenn der Benutzer anonym ist          |
| `app_group_id`     | `string`, `null`    | Braze ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                 |
| `app_group_api_id` | `string`, `null`    | API-ID des Arbeitsbereichs, zu dem dieser Benutzer gehört                                  |
| `app_api_id`       | `string`, `null`    | API ID der App, zu der der verwaiste Benutzer gehörte                               |
| `time`             | `int`, `null`       | Unix-Zeitstempel, zu dem der Benutzer verwaist wurde                                 |
| `orphaned_by_id`   | `string`, `null`    | Braze ID des Benutzers, dessen Profil mit dem Profil des verwaisten Benutzers zusammengeführt wurde |
| `sf_created_at`    | `timestamp`, `null` | Zeitpunkt, zu dem dieses Event von der Snowpipe aufgegriffen wurde                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
