---
nav_title: Bewährte Praktiken
hidden: true
---

# Bewährte Praktiken für den Benutzerlebenszyklus und Identifikatoren

## Datenerfassung

Erfahren Sie mehr darüber, wie Braze Daten sammelt:
- [SDK Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)
- [Bewährte Methoden der Datenerfassung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/)
- [Lebenszyklus des Benutzerprofils]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)

## Braze-Identifikatoren

- `braze_id`: Eine von Braze zugewiesene Kennung, die unveränderlich ist und einem bestimmten Benutzer zugeordnet wird, wenn sie in unserer Datenbank erstellt wird.
- `external_id`: Ein vom Kunden zugewiesener Identifikator, in der Regel eine UUID. Wir empfehlen Kunden, die `external_id` zuzuweisen, wenn der Benutzer eindeutig identifiziert werden kann. Nachdem ein Benutzer identifiziert wurde, kann er nicht mehr in die Anonymität zurückversetzt werden.
- `user_alias`: Ein eindeutiger alternativer Identifikator, den der Kunde zuweisen kann, um den Benutzer über eine ID zu referenzieren, bevor eine `external_id` zugewiesen wird. Benutzer-Aliase können später mit anderen Aliasen oder einem `external_id` zusammengeführt werden, wenn einer über den Endpunkt [Benutzeridentifikation]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) von Braze verfügbar wird.
    - Innerhalb des Endpunkts [Benutzeridentifikation]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) kann das Feld `merge_behavior` verwendet werden, um anzugeben, welche Daten aus dem Benutzer-Alias-Profil im bekannten Benutzerprofil erhalten bleiben sollen.
    - Beachten Sie, dass der Benutzer-Alias nur dann ein sendefähiges Profil sein kann, wenn Sie E-Mail und/oder Telefon als Standardattribut in das Profil aufnehmen.
- `device_id`: Ein automatisch generierter, gerätespezifischer Identifikator. Einem Benutzerprofil kann eine Reihe von `device_ids` zugeordnet sein. Ein Benutzer, der sich beispielsweise auf seinem Arbeitscomputer, seinem Heimcomputer, seinem Tablet und seiner iOS-App bei seinem Konto angemeldet hat, hat 4 `device_ids` mit seinem Profil verknüpft.
- E-Mail Adresse & Telefonnummer:
    - Unterstützt als Bezeichner im Tracking-Endpunkt von Braze. 
    - Wenn Sie die E-Mail-Adresse oder Telefonnummern als Identifikator in einer Anfrage verwenden, gibt es drei mögliche Ergebnisse:
        1. Wenn ein Benutzer mit dieser E-Mail/Telefon-Nummer in Braze nicht existiert, wird ein Benutzerprofil erstellt, das nur E-Mail/Telefon enthält, und alle Daten in der Anfrage werden dem Profil hinzugefügt.
        2. Wenn ein Profil mit dieser E-Mail/Telefon-Nummer bereits in Braze existiert, wird es aktualisiert, um alle in der Anfrage gesendeten Daten aufzunehmen.
        3. In einem Anwendungsfall mit mehr als einem Profil mit dieser E-Mail/Telefon, wird das zuletzt aktualisierte Profil bevorzugt behandelt.
    - Beachten Sie, dass Braze ein zweites Profil erstellt, wenn ein Benutzerprofil existiert, das nur aus E-Mail und Telefon besteht, und dann ein identifiziertes Profil mit derselben E-Mail und demselben Telefon erstellt wird (z. B. ein weiteres Profil mit derselben E-Mail-Adresse UND einer externen ID). Spätere Aktualisierungen werden an das Profil mit der externen ID weitergeleitet.
        - Die beiden Profile können mit dem Endpunkt Braze [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) zusammengeführt werden

## Umgang mit anonymen Benutzern

Für einen Anwendungsfall, in dem Sie ein Benutzerprofil in Braze erstellen oder aktualisieren müssen, ohne Zugriff auf eine `external_id` zu haben, kann ein anderer Identifikator wie eine E-Mail-Adresse oder Telefonnummer an den Endpunkt Braze [Export user by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) übergeben werden, um festzustellen, ob ein Profil für den Benutzer in Braze existiert. 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Wenn ein Benutzer mit dieser E-Mail-Adresse oder Telefonnummer in Braze existiert, wird sein Profil angezeigt. Andernfalls wird ein leeres Array "Benutzer" zurückgegeben. Wenn Sie den Export-Endpunkt verwenden, um festzustellen, ob ein Benutzer mit dieser E-Mail-Adresse bereits existiert, haben Sie den Vorteil, dass Sie feststellen können, ob dem Benutzer anonyme Benutzerprofile zugeordnet sind. Zum Beispiel ein anonymes Profil, das über das SDK erstellt wurde (mit `braze_id`) oder ein zuvor erstelltes Benutzer-Alias-Profil. 

Wenn die Anfrage kein Benutzerprofil ergibt, können Sie entweder einen Benutzer-Alias oder einen reinen E-Mail-Benutzer erstellen:

### Benutzer-Alias

Verwenden Sie den Endpunkt Benutzerspur, um einen Benutzer-Alias zu erstellen, wobei Sie den von Ihnen gewählten Bezeichner als Alias-Namen verwenden. Wenn Sie `_update_existing_only` als `false` in das Attribut-, Ereignis- oder Kaufobjekt einbinden, in dem der neue Benutzer-Alias definiert ist, können Sie das Alias-Profil erstellen und gleichzeitig Attribute, Ereignisse und Käufe zu diesem Profil hinzufügen. 

Damit der Benutzer-Alias ein versendbares Profil ist, müssen Sie die E-Mail-Adresse in das Feld `email` einfügen, wie unten gezeigt.

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

Sie können diesen Benutzeralias später identifizieren und mit einem `external_id` zusammenführen, wenn einer über unseren Endpunkt [Benutzer identifizieren]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) verfügbar wird. 

### Einen reinen E-Mail-Benutzer erstellen

Verwenden Sie die E-Mail-Adresse als Identifikator für den Endpunkt der Benutzerspur. 

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

## Daten mit Benutzerprofilen synchronisieren

[Benutzer-Spur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- Hierbei handelt es sich um einen öffentlich zugänglichen Endpunkt, der Benutzer in Braze erstellen und aktualisieren kann, z. B. das Protokollieren von Attributen im Benutzerprofil. Dieser Endpunkt hat ein Ratenlimit von 50.000 Anfragen pro Minute, das auf der Ebene des Arbeitsbereichs gilt.
- Wenn Sie diesen Endpunkt verwenden, geben Sie den Schlüssel `partner` an, wie in unserer Partner-Dokumentation beschrieben.

[Cloud-Datenaufnahme]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- Ähnlich wie beim Endpunkt für die Benutzerspur können Daten über Cloud Data Ingestion mit Benutzerprofilen synchronisiert werden. Wenn Sie dieses Tool verwenden, werden Attribute, Ereignisse und Käufe in Profilen protokolliert, indem Sie die Data Warehouse-Tabelle oder die Ansicht, die Sie mit dem gewünschten Braze-Arbeitsbereich synchronisieren möchten, einrichten und verbinden.

[Datenpunkte]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)
- Braze hat ein Datenpunktverbrauchsmodell, bei dem Datenpunkte pro "Schreiben" in das Benutzerprofil anfallen, unabhängig davon, ob sich der Wert geändert hat. Aus diesem Grund empfehlen wir, dass nur die Attribute, die sich geändert haben, an Braze gesendet werden. 

## Senden von Benutzerzielgruppen an Braze

[Kohorten-Import-Synchronisationspartner-Dokumentation]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
- Benutzer-Audiences können mit Hilfe der Braze Cohort Import API Endpunkte als Kohorte mit Braze synchronisiert werden. Anstatt diese Zielgruppen im Benutzerprofil als Benutzerattribute zu speichern, können Kunden diese Kohorte mit Hilfe eines von Partnern entwickelten Filters in unserem Segmentierungstool aufbauen und ansprechen. Dies kann das Auffinden und die Ausrichtung auf ein bestimmtes Nutzersegment für die Kunden einfacher und bequemer machen.
- Die Endpunkte des Kohortenimports sind nicht öffentlich und für jeden Partner spezifisch. Aus diesem Grund werden Synchronisierungen mit den Kohorten-Endpunkten nicht auf die Ratenbeschränkungen für den Arbeitsbereich eines Kunden angerechnet. 

[Benutzer-Spur]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
- Dies ist ein öffentlich zugänglicher Endpunkt, der sofort verwendet werden kann, um Benutzer in Braze zu erstellen, indem ein Benutzer in einer bestimmten Zielgruppe durch ein Benutzerattribut bezeichnet wird. Der Hauptunterschied zwischen diesem Endpunkt und dem Kohortenimport-Endpunkt besteht darin, dass die über diesen Endpunkt gesendeten Zielgruppen im Benutzerprofil gespeichert werden, während der Kohortenimport-Endpunkt in unserem Segmentierungstool als Füllung angezeigt wird. Dieser Endpunkt hat ein Ratenlimit von 50.000 Anfragen pro Minute, das auf der Ebene des Arbeitsbereichs gilt.
- Wenn Sie diesen Endpunkt verwenden, vergewissern Sie sich, dass Sie den Schlüssel `partner` verwenden, wie in unserer [Partner-Dokumentation]({{site.baseurl}}/partners/isv_partners/api_partner) beschrieben.

[Datenpunkte]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)<br>
- Braze hat ein Datenpunktverbrauchsmodell, bei dem Datenpunkte pro "Schreiben" in das Benutzerprofil anfallen, unabhängig davon, ob sich der Wert geändert hat.
- Datenpunkte entstehen sowohl durch den Kohortenimport als auch durch die Endpunkte der Benutzerspur.

## Streaming von Engagement-Analysen an Partner

### Currents

Currents ist ein Streaming-Tool von Braze, mit dem sich das Nachrichteninteresse nahezu in Echtzeit analysieren lässt. Dies ermöglicht das Streaming von Daten auf Benutzerebene zu allen Sendungen, Zustellungen, Öffnungen, Klicks usw. für Kampagnen und Canvases, die vom Arbeitsbereich des Kunden aus gesendet wurden. Ein paar Dinge sind zu beachten: Currents werden pro Anschluss für den Kunden berechnet, daher müssen alle neuen Currents-Partner einen EA-Prozess durchlaufen. Wir verlangen von unseren Partnern, dass sie fünf Kunden als Teil des EA haben, bevor wir die benutzerdefinierte Benutzeroberfläche erstellen und den Connector öffentlich zugänglich machen. 
- [Partner-Dokumentation]({{site.baseurl}}/partners/isv_partners/currents_integration/)
- [Message Engagement Events]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) \- alle Kunden, die einen Currents Connector erwerben, haben Zugang zu diesen Events.
- [Benutzerverhaltensereignisse]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events) \- nicht alle Kunden, die einen Current-Connector kaufen, erwerben auch einen "All Events"-Connector, der diese Ereignisse enthält. 

### Snowflake Data Share

Kunden, die einen Snowflake Data Share-Connector erwerben, haben automatisch Zugang zu Ereignissen im Zusammenhang mit Nachrichten und Benutzerverhalten. Wenn Snowflake Data Share als Partnerintegration verwendet wird, stellt Braze eine Freigabe für die Snowflake-Instanz des Partners im Namen des Kunden bereit. Wir möchten darauf hinweisen, dass die gemeinsame Nutzung regionsübergreifender Daten für unsere Kunden einen höheren Preis hat. Daher bitten wir Partner, die eine Integration mit Snowflake wünschen, um den Hinweis, dass sie ein Konto auf `US-EAST-1` benötigen und/oder `EU-CENTRAL-1`
- [Partner-Dokumentation]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## Erstellen und Auslösen von Kampagnen und Canvases

### Erstellen von Assets in Braze
Braze bietet eine Reihe von Endpunkten, mit denen Kunden und Partner E-Mail-Vorlagen und Inhaltsblöcke innerhalb des Arbeitsbereichs eines Kunden erstellen/aktualisieren können. Diese Vorlagen und Inhaltsblöcke können wiederum in den Braze-Kampagnen und Canvases des Kunden verwendet werden.
- E-Mail-Vorlagen
    - [Vorlagenendpunkt erstellen]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    - [Endpunkt der Vorlage aktualisieren]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [Content-Blöcke]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) 
    - [Endpunkt Inhaltsblock erstellen]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [Endpunkt Inhaltsblock aktualisieren]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### API-ausgelöste Kampagnen und Canvases

Kunden können Kampagnen und Canvases so einrichten, dass sie über die API ausgelöst werden. Die API-Anfragen zum Auslösen dieser Kampagnen können verwendet werden, um die Kampagne weiter zu personalisieren und zu segmentieren, indem API-Auslösereigenschaften und Zielgruppen- oder Empfängerparameter übergeben werden. 
- [Auslösen von Kampagnen über API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - Kampagnen sind einzelne Nachrichten, wie z.B. einzelne E-Mails.
- [Auslösen von Leinwänden über API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - Canvas ist eine einheitliche Schnittstelle, auf der Marketer Kampagnen mit mehreren Botschaften und Schritten erstellen können, um eine zusammenhängende Reise zu gestalten. Wenn Sie ein Canvas auslösen, nehmen Sie einen Benutzer in den Canvas-Fluss auf, wo er so lange Nachrichten erhält, bis er die Canvas-Kriterien nicht mehr erfüllt. 
- [API-Trigger-Eigenschaften/Leinwand-Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 
    - Daten, die zum Zeitpunkt des Versands dynamisch in die Nachricht eingefügt werden können.

### API-Kampagnen
Bei der Erstellung von API-Kampagnen (anders als bei den oben erwähnten API-ausgelösten Kampagnen) wird das Braze-Dashboard nur zur Erstellung einer `campaign_id` verwendet. Die Nachricht der Kampagne selbst wird in der API-Anfrage definiert. 
- [API-Kampagne sofort senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [Planen Sie eine API-Kampagne]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### IDs senden
Verwenden Sie den Endpunkt von Braze, um eine Sende-ID zu generieren, die zur Aufschlüsselung der Kampagnenanalyse nach Sendungen verwendet werden kann. Wenn zum Beispiel eine `campaign_id` (API-Kampagne) pro Standort erstellt wird, könnte eine Sende-ID pro Sendung generiert werden, um zu verfolgen, wie gut verschiedene Nachrichten für einen bestimmten Standort funktionieren. 
- [IDs senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## Connected-Content

Connected Content kann innerhalb eines beliebigen Kanaltyps verwendet werden, um zum Zeitpunkt des Sendens eine API-Anfrage an den angegebenen Endpunkt zu stellen und das, was in der Antwort zurückgegeben wird, in die Nachricht einzufügen.

Dank der Vielseitigkeit von Connected Contents wird diese Funktion von vielen unserer Kunden genutzt, um Inhalte einzufügen, die nicht in Braze vorhanden sind oder sein können. Einige der häufigsten Anwendungsfälle, die wir sehen, sind:
- Vorlagen für Blog- oder Artikelinhalte in Nachrichten
- Empfehlungen zum Inhalt
- Produkt-Metadaten
- Lokalisierung und Übersetzung

Dinge, die Sie beachten sollten:
- Braze erhebt keine Gebühren für API-Aufrufe und wird nicht auf Ihr Datenpunktkontingent angerechnet.
- Es gibt ein Limit von 1 MB für Antworten auf Connected Content.
- Der Aufruf von Connected Content erfolgt, wenn die Nachricht gesendet wird, mit Ausnahme von In-App-Nachrichten, bei denen dieser Aufruf erfolgt, wenn die Nachricht angesehen wird.
- Aufrufe von Connected Content folgen nicht redirects.Braze verlangt aus Leistungsgründen, dass die Antwortzeit des Servers weniger als 2 Sekunden beträgt; wenn der Server länger als 2 Sekunden braucht, um zu antworten, wird der Inhalt nicht eingefügt.
- Die Systeme von Braze können denselben Aufruf der Connected Content API mehr als einmal pro Empfänger tätigen. Das liegt daran, dass Braze möglicherweise einen Aufruf der Connected Content API durchführen muss, um eine Nutzlast zu rendern, und dass Nutzlasten für die Validierung, Wiederholungslogik oder andere interne Zwecke mehrmals pro Empfänger gerendert werden können. 

Lesen Sie diese Artikel, um mehr über Connected Content zu erfahren:
- [Aufruf von Connected Content][1]
- [Abbrechen verbundener Inhalte][2]
- [Erneute Connected-Content-Versuche][3]

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries
