---
nav_title: Nachrichten archivieren
article_title: Nachrichtenarchivierung
alias: "/message_archiving/"
page_order: 0
page_type: reference
description: "Dieser referenzierte Artikel behandelt die Nachrichtenarchivierung, ein Feature, mit dem Sie eine Kopie der an Nutzer:innen gesendeten Nachrichten speichern können."

---

# Nachrichten archivieren

> Mit der Nachrichtenarchivierung können Sie eine Kopie der an Nutzer:innen gesendeten Nachrichten zu Archivierungs- oder Compliance-Zwecken in Ihrem AWS S3-Bucket, Azure Blob Storage-Container oder Google Cloud Storage-Bucket speichern. <br><br> Dieser Artikel behandelt die Einrichtung der Archivierung für Nachrichten, JSON-Payload-Referenzen und häufig gestellte Fragen.

Die Archivierung von Nachrichten ist als zusätzliches Feature verfügbar. Um mit der Nachrichtenarchivierung zu beginnen, wenden Sie sich bitte an Ihren Braze-Customer-Success-Manager.

## Funktionsweise

Wenn dieses Feature eingeschaltet ist und Sie einen Cloud Storage Bucket mit Braze verbunden und als Standard Ziel für den Datenexport markiert haben, schreibt Braze für jede Nachricht, die über die von Ihnen ausgewählten Kanäle (E-Mail, SMS/MMS oder Push) an einen Nutzer:in gesendet wird, eine gzipped JSON-Datei in Ihren Cloud Storage Bucket. 

Diese Datei enthält die unter [Dateireferenzen](#file-references) definierten Felder und spiegelt die endgültigen Nachrichten wider, die als Template an die Nutzer:innen gesendet werden. Alle in Ihrer Kampagne definierten Template-Werte (z.B. {% raw %}`{{${first_name}}}`{% endraw %}) zeigen den endgültigen Wert an, den der Nutzer:in auf der Grundlage seiner Profilinformationen erhalten hat. Auf diese Weise können Sie eine Kopie der gesendeten Nachricht aufbewahren, um den Anforderungen der Compliance, der Rechnungsprüfung oder des Kundensupports gerecht zu werden.

Wenn Sie Zugangsdaten für mehrere Cloud-Speicheranbieter einrichten, exportiert die Nachrichtenarchivierung nur zu dem Anbieter, der explizit als Standardziel für den Datenexport markiert ist. Wenn kein expliziter Standard angegeben wird und ein AWS S3-Bucket verbunden ist, wird die Archivierung der Nachrichten in dieses Bucket hochgeladen.

{% alert important %}
Die Aktivierung dieses Features wirkt sich auf die Geschwindigkeit der Zustellung Ihrer Nachrichten aus, da der Datei-Upload unmittelbar vor dem Versand der Nachricht durchgeführt wird, um die Genauigkeit zu gewährleisten. Die Latenzzeit, die durch die Archivierung von Nachrichten entsteht, hängt vom Anbieter des Cloud-Speichers sowie vom Durchsatz und der Größe der gespeicherten Dokumente ab.
{% endalert %}

Das JSON wird in Ihrem Bucket mit der folgenden Schlüsselstruktur gespeichert:

`sent_messages/{channel, one of: email, push, sms}/{MD5 digest of downcased: email address, push token, or E.164 phone number}/{campaign or Canvas step API ID}/{dispatch ID}.json.gz`

Eine Beispieldatei könnte wie folgt aussehen:

`sent_messages/email/819baa08d8d7e77e19d4666f5fc6050b/ee965cb2-8934-4b0a-acf1-91c899c2f915/651fd10b282850b39e1169c13975234b.json.gz`

{% alert note %}
Der MD5-Digest kann nur mit einer bekannten, heruntergeladenen E-Mail Adresse, einem Push-Token oder einer E.164 Telefonnummer berechnet werden. Ein bekannter MD5-Digest kann nicht umgekehrt werden, um die heruntergeladene E-Mail Adresse, das Push-Token oder die E.164 Telefonnummer zu erhalten.
{% endalert %}

{% alert tip %}
**Haben Sie Probleme, Ihre Push-Token in Ihren Buckets zu finden?**<br>
Braze verkleinert Ihre Push-Token, bevor wir sie hashen. Dies führt dazu, dass der Push-Token `Test_Push_Token12345` im Schlüsselpfad mit dem Hashwert `32b802170652af2b5624b695f34de089` auf `test_push_token12345` herabgestuft wird.
{% endalert %}

## Einrichten der Archivierung von Nachrichten

Dieser Abschnitt führt Sie durch die Einrichtung der Archivierung von Nachrichten für Ihren Workspace. Bevor Sie fortfahren, vergewissern Sie sich, dass Ihr Unternehmen die Archivierung von Nachrichten erworben und aktiviert hat.

### Schritt 1: Cloud-Speicher-Bucket verbinden

Falls Sie dies noch nicht getan haben, verbinden Sie einen Cloud-Speicher-Bucket mit Braze. Weitere Schritte finden Sie in unserer Partner Dokumentation zu [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/), [Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/) oder [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

{% alert note %}
Sie müssen Currents nicht für die Archivierung von Nachrichten einrichten, daher können Sie diese Voraussetzung in der Dokumentation des Partners überspringen.
{% endalert %}

### Schritt 2: Kanäle für die Archivierung von Nachrichten auswählen

Auf der Seite mit den Einstellungen für **die Nachrichtenarchivierung** können Sie festlegen, welche Kanäle eine Kopie der gesendeten Nachrichten in Ihrem Cloud-Speicher Bucket speichern.

So wählen Sie Kanäle aus:

1. Gehen Sie zu **Einstellungen** > Nachrichtenarchivierung.
2. Wählen Sie Ihre Kanäle aus.
3. Wählen Sie **Änderungen speichern**.

![Auf der Seite Nachrichtenarchivierung können Sie drei Kanäle auswählen: E-Mail, Push und SMS.]({% image_buster /assets/img/message_archiving_settings.png %})

{% alert note %}
Wenn Sie die **Nachrichtenarchivierung** in den **Einstellungen** nicht sehen, vergewissern Sie sich, dass Ihr Unternehmen die Nachrichtenarchivierung erworben und aktiviert hat.
{% endalert %}

## Dateireferenzierungen

Im Folgenden finden Sie Verweise darauf, welche JSON-Nutzlast bei jeder zugestellten Nachricht an Ihren Cloud-Speicher-Bucket zugestellt wird. In unserem Code-Beispiel-Repository finden Sie [Beispieldateien für Nachrichtenarchive](https://github.com/braze-inc/braze-examples/tree/main/message-archiving).

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

Das`extras`Feld enthält die Schlüssel-Wert-Paare, die beim Verfassen einer E-Mail im HTML-Editor im Feld **„E-Mail-Extras“** konfiguriert wurden. E-Mail-Extras funktionieren mit allen E-Mail-Anbietern (einschließlich SendGrid und Sparkpost) und sind unabhängig vom verwendeten Anbieter in archivierten Nachrichten enthalten. Weitere Informationen zum Konfigurieren von E-Mail-Extras finden Sie unter [Erstellen einer E-Mail-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#adding-email-extras). Wie Sie Daten an Currents zurücksenden, erfahren Sie unter [Extras für Nachrichten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/).

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

### Variationen der Nutzlaststruktur

{% alert important %}
Das oberste`payload`Feld in Archiven für Push-Benachrichtigungen enthält die gesamte vom Anbieter an das Gerät gesendete Nutzlast. Innerhalb dieser JSON-Datei können Schlüssel wie`aps`(für APN) oder`notification`und`data`(für FCM) je nach Typ der Nachricht, Plattform und Konfiguration erheblich variieren.
{% endalert %}

Die Nachrichtenarchivierung erfasst die Nutzdaten der Nachricht selbst, jedoch nicht die Metadaten zur Zustellung, die an FCM oder APN gesendet werden. Die Metadaten der Zustellung umfassen:

- Gerätetoken
- Prioritätseinstellungen
- Zeit bis zum Ablauf (TTL)
- IDs ausblenden
- APN-Header
- Ablaufzeitstempel
- Weitere Felder zur Zustellung

Diese Felder dienen als Anweisungen für die Zustellung beim Push-Anbieter. Sie werden in der Regel nicht als Teil der Nachricht betrachtet.

Zum Beispiel:

- **iOS-Push-Benachrichtigungen** können unterschiedliche Strukturen für Rich-Benachrichtigungen (wobei ein Objekt`aps.alert` ist, das Felder wie`title`und enthält`body`) und einfache Benachrichtigungen (wobei eine `aps.alert`String-Zeichenfolge ist) aufweisen.
- **Android-Push-Benachrichtigungen** (z. B. FCM) verwenden Datennachrichten mit angepassten Schlüsseln. Die Nutzlaststruktur kann je nach Konfiguration der Nachrichten verschiedene optionale Felder enthalten, wie z. B. Buttons, Karussells oder zusätzliche Metadaten.

Darüber hinaus können Test-Sendungen über das Dashboard zu unterschiedlichen Nutzlaststrukturen als bei Produktionsnachrichten führen.

Das JSON-Payload-Format kann zwischen den Nachrichten variieren und sich im Laufe der Zeit ändern. Bei der Analyse archivierter Push-Nutzdaten sollten Sie nicht von einer festen Struktur ausgehen oder davon ausgehen, dass immer dieselben Felder vorhanden sind. Implementieren Sie eine flexible Parsing-Logik, die verschiedene Payload-Formate verarbeitet.

{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen

### Welche Templates sind nicht in der Nutzlast enthalten?

Änderungen, die vorgenommen werden, nachdem die Nachricht Braze verlassen hat, werden in der Datei, die in Ihrem Cloud-Speicher-Bucket gespeichert ist, nicht berücksichtigt. Dazu gehören auch Änderungen, die unsere Partner für die Zustellung vornehmen, wie z.B. das Einbinden von Links für das Tracking von Klicks und das Einfügen von Tracking-Pixeln.

### Was sind Nachrichten unter dem Wert "unassoziiert" im Pfad der Kampagne?

Wenn eine Nachricht außerhalb einer Kampagne oder eines Canvas versendet wird, wird die ID der Kampagne im Dateinamen als "unassoziiert" angezeigt. Dies geschieht, wenn Sie Testnachrichten über das Dashboard senden, wenn Braze automatische SMS/MMS-Antworten sendet oder wenn in den über die API gesendeten Nachrichten keine ID für die Kampagne angegeben ist.

### Wo finde ich weitere Informationen über diese Sendung?

Sie können entweder das Symbol`external_id`  oder`dispatch_id`  in Verbindung mit dem Symbol  verwenden, um die vorlagenbasierte`user_id` Nachricht mit unseren Currents-Daten zu referenzieren und weitere Informationen zu erhalten, wie beispielsweise den Zeitstempel der Zustellung, ob die Öffnung der Nachricht erfolgt ist oder ob Klicks auf die Nachricht erfolgt sind und vieles mehr.

### Wie werden Wiederholungsversuche behandelt?

Wenn Ihr Bucket im Cloud-Speicher nicht erreichbar ist, versucht Braze es bis zu dreimal mit einem [Backoff-Jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/#Jitter). AWS S3 Rate-Limits werden von Braze automatisch neu vergeben.

### Was passiert, wenn meine Zugangsdaten ungültig sind?

Wenn Ihre Zugangsdaten für den Cloud-Speicher zu irgendeinem Zeitpunkt ungültig werden, kann Braze keine Nachrichten in Ihrem Bucket für den Cloud-Speicher speichern und diese Nachrichten gehen verloren. Wir empfehlen Ihnen, Ihre [Benachrichtigungseinstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/notification_preferences/) für Amazon Web Services, Google Cloud Services oder Azure (Microsoft Azure) so zu konfigurieren, dass Sie bei Problemen mit Ihren Zugangsdaten eine Benachrichtigung erhalten.

### Warum weicht der Zeitstempel meiner Archivdatei `sent_at` leicht vom gesendeten Zeitstempel in Currents ab?

Die gerenderte Kopie wird unmittelbar vor dem Senden der Nachricht an die Nutzer:innen hochgeladen. Aufgrund der Uploadzeiten des Cloud-Speichers kann es zu einem Delay von einigen Sekunden zwischen dem Zeitstempel `sent_at` in der gerenderten Kopie und dem tatsächlichen Zeitpunkt des Versands kommen.

### Kann ich einen neuen Bucket speziell für die Archivierung von Nachrichten erstellen und gleichzeitig den aktuellen Bucket für Currents-Daten beibehalten?

Nein. Wenn Sie an der Erstellung dieser speziellen Buckets interessiert sind, senden Sie uns Ihr [Produkt-Feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### Werden archivierte Daten in einen speziellen Ordner in einem bestehenden Bucket geschrieben, ähnlich wie die Datenexporte von Currents strukturiert sind?

Die Daten werden in einen `sent_messages` Bereich des Buckets geschrieben. Weitere Einzelheiten finden Sie unter [Wie es funktioniert](#how-it-works).

### Ist es möglich, die Nachrichtenarchivierung zu verwenden, um Dateien in verschiedenen Workspaces zu gruppieren?

Nein. Die Archivierung von Nachrichten unterstützt keine Gruppierung von Dateien nach Workspaces. Stattdessen können Sie feststellen, zu welchem Workspace die Kampagne oder die Canvas-Schritt-API-ID gehört, und sie dann anhand dieser Informationen gruppieren.
