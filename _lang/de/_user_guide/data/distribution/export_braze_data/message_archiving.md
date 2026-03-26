---
nav_title: Nachrichten archivieren
article_title: Nachrichtenarchivierung
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "Dieser Referenzartikel behandelt die Nachrichtenarchivierung, ein Feature, mit dem Sie eine Kopie der an Nutzer:innen gesendeten Nachrichten speichern können."

---

# Nachrichtenarchivierung

> Mit der Nachrichtenarchivierung können Sie eine Kopie der an Nutzer:innen gesendeten Nachrichten zu Archivierungs- oder Compliance-Zwecken in Ihrem AWS S3-Bucket, Azure Blob Storage-Container oder Google Cloud Storage-Bucket speichern. <br><br> Dieser Artikel behandelt die Einrichtung der Nachrichtenarchivierung, JSON-Payload-Referenzen und häufig gestellte Fragen.

Die Nachrichtenarchivierung ist als zusätzliches Feature verfügbar. Um mit der Nachrichtenarchivierung zu beginnen, wenden Sie sich bitte an Ihren Braze-Customer-Success-Manager.

## Funktionsweise

Wenn dieses Feature eingeschaltet ist, schreibt Braze für jede Nachricht, die über die von Ihnen ausgewählten Kanäle (E-Mail, SMS/MMS oder Push) an eine:n Nutzer:in gesendet wird, eine gzipped JSON-Datei. Braze schreibt diese Dateien in Ihr Standard-Datenexportziel. Dazu gehören alle Kampagnentypen für jeden Kanal, wie z. B. Transaktions-E-Mail-Kampagnen, die über die [Transaktions-E-Mail-API]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign) gesendet werden.

Diese Datei enthält die unter [Dateireferenzen](#file-references) definierten Felder und spiegelt die endgültigen, als Template gerenderten Nachrichten wider, die an die Nutzer:innen gesendet wurden. Alle in Ihrer Kampagne definierten Template-Werte (z. B. {% raw %}`{{${first_name}}}`{% endraw %}) zeigen den endgültigen Wert an, den die Nutzer:innen auf der Grundlage ihrer Profilinformationen erhalten haben. Auf diese Weise können Sie eine Kopie der gesendeten Nachricht aufbewahren, um den Anforderungen der Compliance, der Rechnungsprüfung oder des Kundensupports gerecht zu werden.

Wenn Sie Zugangsdaten für mehrere Cloud-Speicheranbieter einrichten, exportiert die Nachrichtenarchivierung nur zu dem Anbieter, der als Standard-Datenexportziel markiert ist. Wenn kein expliziter Standard festgelegt ist und ein AWS S3-Bucket verbunden ist, lädt die Nachrichtenarchivierung in diesen Bucket hoch.

{% alert important %}
Die Aktivierung dieses Features wirkt sich auf die Zustellgeschwindigkeit Ihrer Nachrichten aus, da der Datei-Upload unmittelbar vor dem Versand der Nachricht durchgeführt wird, um die Genauigkeit zu gewährleisten. Die durch die Nachrichtenarchivierung verursachte Latenz hängt vom Cloud-Speicheranbieter sowie vom Durchsatz und der Größe der gespeicherten Dokumente ab.
{% endalert %}

Die JSON-Datei wird in Ihrem Speicher-Bucket mit der folgenden Schlüsselstruktur gespeichert:

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

Eine Beispieldatei könnte wie folgt aussehen:

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
Der MD5-Digest kann nur mit einer bekannten, kleingeschriebenen E-Mail-Adresse, einem Push-Token oder einer E.164-Telefonnummer berechnet werden. Ein bekannter MD5-Digest kann nicht umgekehrt werden, um die kleingeschriebene E-Mail-Adresse, das Push-Token oder die E.164-Telefonnummer zu erhalten.
{% endalert %}

{% alert tip %}
**Haben Sie Probleme, Ihre Push-Token in Ihren Buckets zu finden?**<br>
Braze wandelt Ihre Push-Token in Kleinbuchstaben um, bevor sie gehasht werden. Dies führt dazu, dass das Push-Token `Test_Push_Token12345` im Schlüsselpfad als `test_push_token12345` mit dem Hash `32b802170652af2b5624b695f34de089` erscheint.
{% endalert %}

## Einrichten der Nachrichtenarchivierung

Dieser Abschnitt führt Sie durch die Einrichtung der Nachrichtenarchivierung für Ihren Workspace. Bevor Sie fortfahren, vergewissern Sie sich, dass Ihr Unternehmen die Nachrichtenarchivierung erworben und aktiviert hat.

### 1. Schritt: Cloud-Speicher-Bucket verbinden

Falls Sie dies noch nicht getan haben, verbinden Sie einen Cloud-Speicher-Bucket mit Braze. Weitere Schritte finden Sie in unserer Partnerdokumentation zu [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), [Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) oder [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

{% alert note %}
Sie müssen Currents nicht für die Nachrichtenarchivierung einrichten, daher können Sie diese Voraussetzung in der Partnerdokumentation überspringen.
{% endalert %}

### 2. Schritt: Kanäle für die Nachrichtenarchivierung auswählen

Auf der Einstellungsseite **Nachrichtenarchivierung** können Sie festlegen, welche Kanäle eine Kopie der gesendeten Nachrichten in Ihrem Cloud-Speicher-Bucket speichern.

So wählen Sie Kanäle aus:

1. Gehen Sie zu **Einstellungen** > **Nachrichtenarchivierung**.
2. Wählen Sie Ihre Kanäle aus.
3. Wählen Sie **Änderungen speichern**.

![Auf der Seite Nachrichtenarchivierung können Sie drei Kanäle auswählen: E-Mail, Push und SMS.]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
Wenn Sie die **Nachrichtenarchivierung** in den **Einstellungen** nicht sehen, vergewissern Sie sich, dass Ihr Unternehmen die Nachrichtenarchivierung erworben und aktiviert hat.
{% endalert %}

## Dateireferenzen

Im Folgenden finden Sie Referenzen zur JSON-Payload, die bei jeder gesendeten Nachricht an Ihren Cloud-Speicher-Bucket übermittelt wird. In unserem Code-Beispiel-Repository finden Sie [Beispieldateien für Nachrichtenarchive](https://github.com/braze-inc/braze-examples/tree/main/message-archiving).

{% tabs %}
{% tab Email %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": ToAddress, ("customer@example.com")
  "subject": SubjectLine ("20% off coupon inside!"),
  "from_name": DisplayName ("Braze"),
  "from_address": FromAddress ("no-reply@braze.com"),
  "html_body": HtmlBody,
  "plaintext_body": PlainTextBody,
  "amp_body": AMPEmailBody,
  "extras": Hash of key-value pairs from Email Extras configured in the email editor,
  "headers": HashOfHeaders,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessageVariationApiId, // may not be available,
  "attachments": Array of JSON Objects containing 'bytes' and 'file_name', // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

Das Feld `extras` enthält die Schlüssel-Wert-Paare, die beim Verfassen einer E-Mail im HTML-Editor im Feld **E-Mail-Extras** konfiguriert wurden. E-Mail-Extras funktionieren mit allen E-Mail-Anbietern (einschließlich SendGrid und Sparkpost) und sind unabhängig vom verwendeten Anbieter in archivierten Nachrichten enthalten. Weitere Informationen zum Konfigurieren von E-Mail-Extras finden Sie unter [Erstellen einer E-Mail-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#adding-email-extras). Wie Sie Daten an Currents zurücksenden, erfahren Sie unter [Extras für Nachrichten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/).

![]({% image_buster /assets/img_archive/email_extras.png %}){: style="max-width:60%" }

{% endtab %}
{% tab SMS/MMS %}

```json
{
  "version": 1 //numerical version of the JSON structure
  "to": PhoneNumber, ("+15555555555"),
  "body": Body ("Hi there!"),
  "subscription_group": SubscriptionGroupExternalId,
  "provider": StringOfProviderName,
  "media_urls": ArrayOfString, // indicates a message is MMS
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

{% endtab %}
{% tab Push %}

```json
{
  "version": 1, //numerical version of the JSON structure
  "to": PushToken,
  "payload": JsonOfEntirePushPayload,
  "platform": one of "android_push" | "ios_push" | "kindle_push" | "web_push",
  "app_id": ApiKeyOfApp,
  "sent_at": UnixTimestamp,
  "dispatch_id": DispatchIdFromBraze,
  "campaign_id": CampaignApiId, // may not be available
  "canvas_id": CanvasApiApiId, // may not be available
  "canvas_step_id": CanvasStepApiId, // may not be available
  "canvas_variation_id" : CanvasVariationApiId, // may not be available
  "message_variation_id": MessagVariationApiId, // may not be available
  "user_id": String,
  "campaign_name": String, // will only be available if the message is from a campaign
  "canvas_name": String, // will only be available if the message is from a Canvas
  "canvas_step_name": String, // will only be available if the message is from a Canvas
  "external_id": String
}
```

### Variationen der Push-Payload-Struktur

{% alert important %}
Das oberste Feld `payload` in Push-Benachrichtigungsarchiven enthält die gesamte Anbieter-Payload, wie sie an das Gerät gesendet wurde. Innerhalb dieses JSON können Schlüssel wie `aps` (für APN) oder `notification` und `data` (für FCM) je nach Nachrichtentyp, Plattform und Konfiguration erheblich variieren.
{% endalert %}

Die Nachrichtenarchivierung erfasst die Nachrichten-Payload selbst, jedoch nicht die Zustellungs-Metadaten, die an FCM oder APN gesendet werden. Zustellungs-Metadaten umfassen:

- Geräte-Token
- Prioritätseinstellungen
- Time-to-Live (TTL)
- Collapse-IDs
- APN-Header
- Ablauf-Zeitstempel
- Weitere Felder zur Zustellungskonfiguration

Diese Felder dienen als Zustellungsanweisungen für den Push-Anbieter. Sie werden in der Regel nicht als Teil des Nachrichteninhalts betrachtet.

Zum Beispiel:

- **iOS-Push-Benachrichtigungen** können unterschiedliche Strukturen für Rich-Benachrichtigungen (wobei `aps.alert` ein Objekt ist, das Felder wie `title` und `body` enthält) und einfache Benachrichtigungen (wobei `aps.alert` ein String ist) aufweisen.
- **Android-Push-Benachrichtigungen** (z. B. FCM) verwenden Datennachrichten mit angepassten Schlüsseln. Die Payload-Struktur kann je nach Nachrichtenkonfiguration verschiedene optionale Felder enthalten, wie z. B. Push-Buttons, Karussells oder zusätzliche Metadaten.

Darüber hinaus können Testsendungen über das Dashboard andere Payload-Strukturen erzeugen als Produktionsnachrichten.

Das JSON-Payload-Format kann zwischen Nachrichten variieren und sich im Laufe der Zeit ändern. Gehen Sie beim Parsen archivierter Push-Payloads nicht von einer festen Struktur aus und erwarten Sie nicht, dass immer dieselben Felder vorhanden sind. Implementieren Sie eine flexible Parsing-Logik, die verschiedene Payload-Formate verarbeiten kann.

{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen

### Welches Templating ist nicht in der Payload enthalten?

Änderungen, die vorgenommen werden, nachdem die Nachricht Braze verlassen hat, werden in der Datei, die in Ihrem Cloud-Speicher-Bucket gespeichert ist, nicht berücksichtigt. Dazu gehören auch Änderungen, die unsere Partner für die E-Mail-Zustellung vornehmen, wie z. B. das Umschließen von Links für das Klick-Tracking und das Einfügen von Tracking-Pixeln.

### Was sind Nachrichten unter dem Wert „unassociated" im Kampagnenpfad?

Wenn eine Nachricht außerhalb einer Kampagne oder eines Canvas gesendet wird, lautet die Kampagnen-ID im Dateinamen „unassociated". Dies geschieht, wenn Sie Testnachrichten über das Dashboard senden, wenn Braze automatische SMS/MMS-Antworten sendet oder wenn über die API gesendete Nachrichten keine Kampagnen-ID enthalten.

### Wie finde ich weitere Informationen zu diesem Versand?

Sie können entweder die `external_id` oder die `dispatch_id` in Verbindung mit der `user_id` verwenden, um die gerenderte Nachricht mit unseren Currents-Daten abzugleichen und weitere Informationen zu erhalten, wie z. B. den Zeitstempel der Zustellung, ob die Nutzer:innen die Nachricht geöffnet oder angeklickt haben und vieles mehr.

### Wie werden Wiederholungsversuche behandelt?

Wenn Ihr Cloud-Speicher-Bucket nicht erreichbar ist, versucht Braze es bis zu dreimal mit einem [Backoff-Jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). AWS S3-Rate-Limit-Wiederholungen werden von Braze automatisch behandelt.

### Was passiert, wenn meine Zugangsdaten ungültig sind?

Wenn Ihre Cloud-Speicher-Zugangsdaten zu irgendeinem Zeitpunkt ungültig werden, kann Braze keine Nachrichten in Ihrem Cloud-Speicher-Bucket speichern, und diese Nachrichten gehen verloren. Wir empfehlen Ihnen, Ihre [Benachrichtigungseinstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) für Amazon Web Services, Google Cloud Services oder Azure (Microsoft Cloud Services) so zu konfigurieren, dass Sie bei Problemen mit Ihren Zugangsdaten benachrichtigt werden.

### Warum weicht der `sent_at`-Zeitstempel meiner Archivdatei leicht vom Sendezeitstempel in Currents ab?

Die gerenderte Kopie wird unmittelbar vor dem Senden der Nachricht an die Nutzer:innen hochgeladen. Aufgrund der Upload-Zeiten des Cloud-Speichers kann es zu einer Verzögerung von einigen Sekunden zwischen dem `sent_at`-Zeitstempel in der gerenderten Kopie und dem tatsächlichen Sendezeitpunkt kommen.

### Kann ich einen neuen Bucket speziell für die Nachrichtenarchivierung erstellen und gleichzeitig den aktuellen Bucket für Currents-Daten beibehalten?

Nein. Wenn Sie an der Erstellung dieser speziellen Buckets interessiert sind, senden Sie uns Ihr [Produkt-Feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### Werden archivierte Daten in einen speziellen Ordner in einem bestehenden Bucket geschrieben, ähnlich wie die Datenexporte von Currents strukturiert sind?

Die Daten werden in einen `sent_messages`-Bereich des Buckets geschrieben. Weitere Einzelheiten finden Sie unter [Funktionsweise](#how-it-works).

### Kann ich die Nachrichtenarchivierung verwenden, um Dateien in verschiedenen Workspaces zu gruppieren?

Nein. Die Nachrichtenarchivierung unterstützt keine Gruppierung von Dateien nach Workspaces. Stattdessen können Sie feststellen, zu welchem Workspace die Kampagnen- oder Canvas-Schritt-API-ID gehört, und die Dateien dann anhand dieser Information gruppieren.