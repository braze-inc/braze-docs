---
nav_title: September
page_order: 5
noindex: true
page_type: update
description: "Dieser Artikel enthält die Versionshinweise für September 2018."
---
# September 2018

## iOS 12 Benachrichtigungsgruppen: Zusätzliche Fähigkeiten

Sie können jetzt über Braze auf [die Features der Benachrichtigungsgruppen von Apple]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) zugreifen! Sie können Zusammenfassungsargumente und Gruppen hinzufügen, kritische Warnungen verwenden, nach provisorisch authentifizierten Nutzer:innen filtern und den Status der provisorischen Authentifizierung in Nutzerprofilen anzeigen.

## Stille Zeit

Kunden:in können jetzt [Ruhezeiten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (die Zeit, in der Ihre Nachrichten nicht gesendet werden) für Canvas festlegen. Gehen Sie einfach zu Ihren **Canvas Sendeeinstellungen** und aktivieren Sie "Ruhezeiten aktivieren". Wählen Sie dann Ihre Ruhezeiten in der Ortszeit Ihres Benutzers und die Aktion, die folgen soll, wenn die Nachricht innerhalb dieser Ruhezeiten ausgelöst wird.

Kampagnen verwenden jetzt auch die Ruhezeit anstelle von "Senden Sie diese Nachricht während eines bestimmten Teils des Tages".

## Kunden:in anpassen

Kunden:in, die [Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/) verwenden, können jetzt ihren Braze API-Schlüssel und die URL der Braze-Instanz sehen, die sie dann in der Adjust-Plattform zur Integration verwenden.

## Nicht in Segmenten Filter

Kunden:in können nun ein Segment aus Nutzern:innen erstellen, die [nicht in einem bestimmten Segment enthalten]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting) sind.

## Canvas Empfänger:in CSV-Exporte

Kund:innen können jetzt über die Nutzer:innen eines Canvas [Daten exportieren]({{site.baseurl}}/user_guide/data/export_braze_data/export_canvas_data/). Die erzeugte CSV-Datei wird der CSV-Datei der Kampagne ähneln.

## Vorläufig genehmigter iOS 12 Segmente Filter

Es wurde ein [Filter für Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) hinzugefügt, mit dem Sie Nutzer:innen finden können, die unter iOS 12 für eine bestimmte App vorläufig zugelassen sind.

## In-App-Nachricht Bild-Uploader

Der Bild-Uploader für In-App-Nachrichten wurde aus dem Design Panel in das Compose Panel verschoben.

## Nur-Lese-Zugriff auf die Seite Nutzer:in

Vor dieser Version konnten Nutzer:innen den Abo-Status und die E-Mail Adresse im Nutzerprofil mit [Leseberechtigung]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions) ändern. Wir haben die Berechtigung `import_user` in die Berechtigung `import_and_update_user` umbenannt und den Bearbeitungszugriff auf den Abo-Status und die E-Mail Adresse eingeschränkt. Wenn sich ein Entwickler:in nur mit Leseberechtigung ausgibt oder ihm diese Berechtigung fehlt, kann er den Abo-Status oder die E-Mail Adresse nicht mehr ändern.
