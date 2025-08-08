---
nav_title: Bewährte Praktiken
hidden: true
---

# Benutzer:in und Bezeichner - bewährte Verfahren

## Datenerfassung

Erfahren Sie mehr darüber, wie Braze Daten sammelt:
- [SDK Datenerfassung]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)
- [Bewährte Methoden der Datenerfassung]({{site.baseurl}}/user_guide/data/user_data_collection/best_practices/)
- [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/)

## Braze Bezeichner

- `braze_id`: Ein von Braze zugewiesener Bezeichner, der unveränderlich ist und mit einem bestimmten Nutzer:innen verbunden ist, wenn er in unserer Datenbank erstellt wird.
- `external_id`: Ein von Kund:in zugewiesener Bezeichner, normalerweise eine UUID. Wir empfehlen Kund:innen, den `external_id` zuzuweisen, wenn der Nutzer:in eindeutig identifiziert werden kann. Nachdem ein Nutzer:in identifiziert wurde, kann er nicht mehr in den anonymen Zustand zurückversetzt werden.
- `user_alias`: Ein eindeutiger alternativer Bezeichner, den der Kund:in zuweisen kann, um den Nutzer:in über eine ID zu referenzieren, bevor eine `external_id` zugewiesen wird. Nutzer:innen können später mit anderen Aliasen oder einer `external_id` zusammengeführt werden, wenn eine solche über den Endpunkt Braze [User identify]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) verfügbar wird.
    - Innerhalb des Endpunkts [Benutzeridentifikation]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) kann das Feld `merge_behavior` verwendet werden, um anzugeben, welche Daten aus dem Nutzer:in-Profil persistent sein sollen.
    - Beachten Sie, dass der Nutzer-Alias nur dann ein sendefähiges Profil ist, wenn Sie E-Mail und/oder Telefon als Standardattribut in das Profil aufnehmen.
- `device_id`: Ein automatisch generierter, gerätespezifischer Bezeichner. Einem Nutzerprofil kann eine Reihe von `device_ids` zugeordnet sein. Ein Nutzer:in, der sich auf seinem Computer am Arbeitsplatz, auf seinem Computer zu Hause, auf seinem Tablet und in der iOS App in sein Konto eingeloggt hat, hat beispielsweise 4 `device_ids`, die mit seinem Profil verbunden sind.
- E-Mail Adresse und Telefonnummer:
    - Wird als Bezeichner im Tracking-Endpunkt von Braze für Nutzer:innen unterstützt. 
    - Wenn Sie die E-Mail Adresse oder Telefonnummern als Bezeichner in einer Anfrage verwenden, gibt es drei mögliche Ergebnisse:
        1. Wenn ein Nutzer:innen mit dieser E-Mail/Telefon nicht in Braze existiert, wird ein Nutzerprofil erstellt, das nur aus E-Mail/Telefon besteht, und alle Daten in der Anfrage werden dem Profil hinzugefügt.
        2. Wenn ein Profil mit dieser E-Mail/Telefon bereits in Braze existiert, wird es aktualisiert, um die in der Anfrage gesendeten Daten aufzunehmen.
        3. In einem Anwendungsfall mit mehr als einem Profil mit dieser E-Mail/Telefon wird das zuletzt aktualisierte Profil vorrangig behandelt.
    - Beachten Sie, dass Braze ein zweites Profil erstellt, wenn ein Nutzerprofil mit nur E-Mail/Telefon existiert und dann ein identifiziertes Profil mit der gleichen E-Mail/Telefon erstellt wird (z.B. ein weiteres Profil mit der gleichen E-Mail Adresse UND einer externen ID). Spätere Updates werden an das Profil mit der externen ID weitergeleitet.
        - Die beiden Profile können mit dem Endpunkt Braze [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) zusammengeführt werden

## Umgang mit anonymen Nutzer:innen

Für einen Anwendungsfall, in dem Sie ein Nutzerprofil in Braze erstellen oder aktualisieren müssen, ohne Zugriff auf eine `external_id` zu haben, kann ein anderer Bezeichner wie eine E-Mail Adresse oder Telefonnummer an den Endpunkt Braze [Export user by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) übergeben werden, um festzustellen, ob ein Profil für den Nutzer:innen in Braze existiert. 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Wenn innerhalb von Braze ein Nutzer:in mit dieser E-Mail oder Telefonnummer existiert, wird sein Profil zurückgegeben. Andernfalls wird ein leeres Array "Nutzer:innen" zurückgegeben. Wenn Sie den Endpunkt für den Export verwenden, um festzustellen, ob ein Nutzer:in mit dieser E-Mail Adresse bereits existiert, haben Sie den Vorteil, dass Sie feststellen können, ob anonyme Nutzerprofile mit dem Nutzer verbunden sind. Zum Beispiel ein anonymes Profil, das über das SDK erstellt wurde (mit `braze_id`) oder ein zuvor erstelltes Nutzer:in-Profil. 

Wenn die Anfrage kein Nutzerprofil ergibt, können Sie entweder ein Nutzer-Alias oder einen reinen E-Mail-Benutzer anlegen:

### Nutzer:in alias

Verwenden Sie den Endpunkt des Nutzer:innen Tracking, um einen Nutzer-Alias zu erstellen, wobei Sie den von Ihnen gewählten Bezeichner als Alias-Namen verwenden. Indem Sie `_update_existing_only` als `false` in das Attribut, das Kauf-Event oder das Kauf-Objekt einbinden, in dem der neue Nutzer-Alias definiert ist, können Sie das Alias-Profil erstellen und diesem Profil gleichzeitig Attribute, Events und Käufe hinzufügen. 

Damit der Nutzer-Alias ein versendbares Profil ist, müssen Sie die E-Mail Adresse in das Feld `email` eingeben, wie unten gezeigt.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@braze.com",
       "alias_label" : "email"
     },
     "email": "test@braze.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

Sie können diesen Nutzer-Alias später über unseren Endpunkt [Nutzer:]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) innen identifizieren und mit einer `external_id` zusammenführen, wenn eine solche verfügbar ist. 

### Erstellen einer Nutzer:in, die nur per E-Mail erreichbar ist

Verwenden Sie die E-Mail Adresse als Bezeichner im Nutzer:innen Tracking Endpunkt. 

```json
{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
Diese Funktionalität befindet sich derzeit im Early Access.
{% endalert %}

## Synchronisierung von Daten mit Nutzer:innen-Profilen

[Nutzer:innen verfolgen]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- Dies ist ein öffentlich zugänglicher Endpunkt, mit dem Nutzer:innen in Braze erstellt und aktualisiert werden können, z.B. durch die Protokollierung von Attributen im Nutzerprofil. Für diesen Endpunkt gilt ein Rate-Limits von 50.000 Anfragen pro Minute auf der Ebene des Workspace.
- Wenn Sie diesen Endpunkt verwenden, geben Sie den Schlüssel `partner` an, wie in unserer Dokumentation für Partner beschrieben.

[Ingestion von Cloud-Daten]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- Ähnlich wie beim Endpunkt für das Tracking von Nutzern können Daten über Cloud Data Ingestion mit Nutzerprofilen synchronisiert werden. Wenn Sie dieses Tool verwenden, werden Attribute, Ereignisse und Käufe in Profilen protokolliert, indem Sie die Data Warehouse-Tabelle oder -Ansicht, die Sie mit dem gewünschten Braze Workspace synchronisieren möchten, einrichten und verbinden.

[Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/)
- Braze hat ein Datenpunkt-Verbrauchsmodell, bei dem Datenpunkte pro "Schreiben" in das Nutzerprofil anfallen, unabhängig davon, ob sich der Wert geändert hat. Aus diesem Grund empfehlen wir, dass nur die Attribute, die sich geändert haben, an Braze gesendet werden. 

## Zielgruppen von Nutzer:innen an Braze senden

[Kohortenimport Sync Partner Dokumentation]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
- Zielgruppen von Nutzern können über die Endpunkte der Braze Kohortenimport-API mit Braze als Kohorte synchronisiert werden. Anstatt diese Zielgruppen als Attribute im Benutzerprofil zu speichern, können Kunden diese Kohorte über einen von Partnern gebrandeten Filter in unserem Segmentierungs-Tool aufbauen und ansprechen. Dies kann das Auffinden und Targeting eines bestimmten Segments von Nutzer:innen für Kund:innen einfacher und leichter machen.
- Die Endpunkte für den Kohortenimport sind nicht öffentlich und werden von jedem Partner individuell festgelegt. Aus diesem Grund werden Synchronisierungen mit den Endpunkten der Kohorte nicht auf die Rate-Limits des Workspace eines Kunden angerechnet. 

[Nutzer:innen verfolgen]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
- Dies ist ein öffentlich zugänglicher Endpunkt, der sofort verwendet werden kann, um Nutzer:in in Braze zu erstellen, indem ein Nutzer:in einer bestimmten Zielgruppe durch ein Attribut bezeichnet wird. Der Hauptunterschied zwischen diesem Endpunkt und dem Endpunkt Kohortenimport besteht darin, dass Zielgruppen, die über diesen Endpunkt gesendet werden, im Nutzerprofil gespeichert werden, während der Endpunkt Kohortenimport in unserem Segmentierungs-Tool als Füllung angezeigt wird. Für diesen Endpunkt gilt ein Rate-Limits von 50.000 Anfragen pro Minute auf der Ebene des Workspace.
- Wenn Sie diesen Endpunkt verwenden, vergewissern Sie sich, dass Sie den Schlüssel `partner` verwenden, wie in unserer [Dokumentation für Partner]({{site.baseurl}}/partners/isv_partners/api_partner) beschrieben.

[Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/)<br>
- Braze hat ein Datenpunkt-Verbrauchsmodell, bei dem Datenpunkte pro "Schreiben" in das Nutzerprofil anfallen, unabhängig davon, ob sich der Wert geändert hat.
- Datenpunkte fallen sowohl beim Kohortenimport als auch beim Nutzer:in Tracking Endpunkten an.

## Streaming von Engagement Analytics zum Partner

### Currents

Currents ist ein nahezu in Realtime arbeitendes Analytics-Streaming-Tool für das Engagement von Nachrichten in Braze. Damit streamen Sie Daten auf Benutzerebene zu allen Sendungen, Zustellungen, Öffnungen, Klicks usw. für Kampagnen und Canvase, die aus dem Arbeitsbereich des Kunden gesendet wurden. Ein paar Dinge sind zu beachten: Currents wird pro Konnektor für die Kund:in berechnet, daher müssen alle neuen Currents Partner einen EA-Prozess durchlaufen. Wir verlangen von unseren Partnern, dass sie fünf Kund:innen in den EA aufnehmen, bevor wir die angepasste UI erstellen und den Konnektor öffentlich zur Verfügung stellen. 
- [Dokumentation für Partner]({{site.baseurl}}/partners/isv_partners/currents_integration/)
- [Messaging Engagement Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) \- alle Kund:in, die einen Currents Konnektor kaufen, haben Zugriff auf diese Events.
- [Nutzerverhalten-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) \- nicht alle Nutzer:innen, die einen Currents-Konnektor kaufen, erwerben auch einen "Alle Events"-Konnektor, der diese Events enthält. 

### Snowflake Daten teilen

Kunden, die einen Snowflake Data Share Konnektor erwerben, haben automatisch Zugriff auf Nachrichten-Engagement und Nutzerverhalten-Events. Wenn Snowflake Data Share als Partnerintegration verwendet wird, stellt Braze der Snowflake Instanz des Partners im Namen des Kunden eine Freigabe zur Verfügung. Da die gemeinsame Nutzung von Daten über Regionen hinweg für unsere Kunden mit höheren Kosten verbunden ist, bitten wir Partner, die eine Integration mit Snowflake vornehmen möchten, um die Anleitung, dass sie ein Konto auf `US-EAST-1` benötigen und/oder `EU-CENTRAL-1`
- [Dokumentation für Partner]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## Aufbau und Triggern von Kampagnen und Canvase

### Erstellen von Assets in Braze
Braze bietet eine Reihe von Endpunkten, die es Kunden und Partnern ermöglichen, E-Mail-Templates und Content-Blöcke innerhalb des Workspace eines Kunden zu erstellen/zu aktualisieren. Diese Templates und Content-Blöcke können wiederum in den Kampagnen und Canvase des Kund:in verwendet werden.
- E-Mail-Vorlagen
    - [Template-Endpunkt erstellen]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    - [Template Endpunkt aktualisieren]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [Content-Blöcke]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) 
    - [Content-Block-Endpunkt erstellen]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [Update Content-Block Endpunkt]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### API-getriggerte Kampagnen und Canvase

Kunden:in können Kampagnen und Canvase so einrichten, dass sie über APIs ausgelöst werden. Die API-Anfragen zum Triggern dieser Kampagnen können verwendet werden, um die Kampagne weiter zu personalisieren und zu segmentieren, indem die Eigenschaften des API-Triggers und die Parameter der Zielgruppe oder des Empfängers übergeben werden. 
- [Triggern von Kampagnen über API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - Kampagnen sind singuläre Nachrichten, wie z.B. einzelne E-Mails.
- [Canvase über API triggern]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - Canvas ist eine einheitliche Schnittstelle, auf der Marketer Kampagnen mit mehreren Nachrichten und Schritten erstellen können, um eine zusammenhängende Reise zu gestalten. Wenn Sie ein Canvas triggern, nehmen Sie einen Nutzer:innen in den Canvas-Fluss auf, wo er so lange Nachrichten erhält, bis er die Canvas-Kriterien nicht mehr erfüllt. 
- [API triggern Eigenschaften/Canvas Eingang Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 
    - Daten, die zum Zeitpunkt des Versands dynamisch in die Nachricht eingefügt werden können.

### API Kampagnen
Bei der Erstellung von API-Kampagnen (im Unterschied zu den oben referenzierten API-getriggerten Kampagnen) wird das Braze-Dashboard nur dazu verwendet, ein `campaign_id` zu generieren, mit dem der Kund:in Analytics für die Kampagnenberichterstattung verfolgen kann. Die Nachricht der Kampagne selbst wird in der API-Anfrage definiert. 
- [API-Kampagne sofort senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [Planen Sie eine API Kampagne]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### IDs senden
Verwenden Sie den Endpunkt von Braze, um eine Sende-ID zu generieren, mit der Sie die Analytics für Kampagnen nach Sendungen aufschlüsseln können. Wenn beispielsweise eine `campaign_id` (API-Kampagne) pro Standort erstellt wird, könnte eine Sende-ID pro Sendung generiert werden, um zu verfolgen, wie gut die verschiedenen Nachrichten für einen bestimmten Standort performen. 
- [IDs senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## Connected-Content

Connected-Content kann innerhalb eines beliebigen Kanals verwendet werden, um eine API-Anfrage an den angegebenen Endpunkt zum Zeitpunkt des Sendens zu stellen und das, was in der Antwort zurückgegeben wird, in die Nachricht einzufügen.

Die Vielseitigkeit von Connected-Content macht dies zu einem Feature, das von vielen unserer Kund:in genutzt wird, um Inhalte einzufügen, die nicht in Braze vorhanden sind oder sein können. Einige der häufigsten Anwendungsfälle, die wir sehen, sind:
- Templating von Blog- oder Artikelinhalten in Nachrichten
- Inhaltliche Empfehlungen
- Produkt-Metadaten
- Lokalisierung und Übersetzung

Dinge, die Sie beachten sollten:
- Braze erhebt keine Gebühren für API-Aufrufe und wird nicht auf Ihr Datenpunkt-Kontingent angerechnet.
- Es gibt ein Limit von 1 MB für Connected-Content-Antworten.
- Connected-Content-Aufrufe erfolgen, wenn die Nachricht gesendet wird, mit Ausnahme von In-App-Nachrichten, die diesen Aufruf tätigen, wenn die Nachricht angesehen wird.
- Connected-Content-Aufrufe folgen nicht redirects.Braze verlangt aus Performance-Gründen, dass die Antwortzeit des Servers weniger als 2 Sekunden beträgt; wenn der Server länger als 2 Sekunden braucht, um zu antworten, wird der Inhalt nicht eingefügt.
- Die Systeme von Braze können denselben Connected-Content-API-Aufruf mehr als einmal pro Empfänger:in tätigen. Das liegt daran, dass Braze möglicherweise einen Connected-Content-API-Aufruf tätigen muss, um eine Nachricht zu rendern, und dass Nachrichten für die Validierung, Wiederholungslogik oder andere interne Zwecke mehrmals pro Empfänger:in gerendert werden können. 

Lesen Sie diese Artikel, um mehr über Connected-Content zu erfahren:
- [Einen Connected-Content-Aufruf tätigen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)
- [Abbrechen von Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content)
- [Erneute Connected-Content-Versuche]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries)

