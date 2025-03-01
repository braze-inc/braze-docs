---
nav_title: September
page_order: 5
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für September 2018."
---
# September 2018

## iOS 12 Benachrichtigungsgruppen: Zusätzliche Fähigkeiten

Sie können jetzt über Braze auf [die Funktionen der Apple Notification Group]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) zugreifen! Sie können Zusammenfassungsargumente und Gruppen hinzufügen, kritische Alarme verwenden, nach provisorisch authentifizierten Benutzern filtern und den Status "provisorisch authentifiziert" in Benutzerprofilen anzeigen.

## Stille Zeit

Kunden können jetzt für Canvas [stille Stunden]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) festlegen (die Zeit, in der Ihre Nachrichten nicht gesendet werden). Gehen Sie einfach zu Ihren **Canvas-Sendeeinstellungen** und aktivieren Sie "Stille Stunden aktivieren". Wählen Sie dann Ihre Ruhezeiten in der Ortszeit Ihres Benutzers und die Aktion, die folgen soll, wenn die Nachricht innerhalb dieser Ruhezeiten ausgelöst wird.

Kampagnen verwenden jetzt auch die Ruhezeit anstelle von "Senden Sie diese Nachricht während eines bestimmten Teils des Tages".

## Kunden anpassen

Braze-Kunden, die [Adjust]({{site.baseurl}}/partners/advertising_technologies/attribution/adjust/) verwenden, können jetzt ihren Braze-API-Schlüssel und ihre Braze-Instanz-URL sehen, die sie dann in der Adjust-Plattform zur Integration verwenden.

## Nicht im Segmentfilter

Kunden können jetzt ein Segment aus Benutzern erstellen, die [nicht in einem bestimmten Segment enthalten]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting) sind.

## Canvas-Empfänger CSV-Exporte

Kunden können jetzt [Daten]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_canvas_data/) über die Benutzer [exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_canvas_data/), die ein Canvas betreten haben. Die erzeugte CSV-Datei ähnelt der CSV-Datei der Kampagne.

## Vorläufig genehmigter iOS 12 Segmentfilter

Es wurde ein [Segmentfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) hinzugefügt, mit dem Sie Benutzer finden können, die unter iOS 12 für eine bestimmte App vorläufig autorisiert sind.

## Bild-Uploader für In-App-Nachrichten

Der Bild-Uploader für In-App-Nachrichten wurde vom Design-Panel in das Erstellungs-Panel verschoben.

## Nur-Lese-Zugriffsrechte auf der Seite Benutzerprofil

Vor dieser Version konnten Kunden den Abonnementstatus und die E-Mail-Adresse im Benutzerprofil mit [nur Leseberechtigung]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions) ändern. Wir haben die Berechtigung `import_user` in die Berechtigung `import_and_update_user` umbenannt und den Bearbeitungszugriff auf den Abonnementstatus und die E-Mail-Adresse eingeschränkt. Wenn ein Entwickler sich nur mit Leseberechtigung ausgibt oder nicht über diese Berechtigung verfügt, kann er den Abonnementstatus oder die E-Mail-Adresse nicht ändern.
