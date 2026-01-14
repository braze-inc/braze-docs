---
nav_title: Integrationen in die Dateiablage
article_title: Integration von Dateispeichern
description: "Diese Seite behandelt die Datenaufnahme in der Braze Cloud und wie Sie relevante Daten von S3 mit Braze synchronisieren."
page_order: 3
page_type: reference

---

# Integrationen in die Dateiablage

> Auf dieser Seite erfahren Sie, wie Sie die Unterstützung für die Datenaufnahme in der Cloud einrichten und die relevanten Daten von S3 mit Braze synchronisieren.

## Funktionsweise

Sie können Cloud Data Ingestion (CDI) für S3 verwenden, um einen oder mehrere S3-Buckets in Ihrem AWS-Konto direkt in Braze zu integrieren. Wenn neue Dateien in S3 veröffentlicht werden, wird eine Nachricht an SQS gesendet, und Braze Cloud Data Ingestion nimmt diese neuen Dateien auf. 

Die Datenaufnahme in der Cloud unterstützt Folgendes:

- JSON-Dateien
- CSV-Dateien
- Parkett Dateien
- Attribute, angepasste Events, Kauf-Events, Nutzer:innen löschen und Katalogdaten

## Voraussetzungen

Für die Integration benötigen Sie die folgenden Ressourcen:

 - S3-Bucket für die Speicherung von Daten 
 - SQS-Warteschlange für Benachrichtigungen über neue Dateien 
 - IAM-Rolle für Braze-Zugriff  

### AWS-Definitionen

Lassen Sie uns zunächst einige der in dieser Aufgabe verwendeten Begriffe definieren.

| Begriff | Definition |
| --- | --- |
| Amazon Ressourcen-Name (ARN) | Der ARN ist ein eindeutiger Bezeichner für AWS-Ressourcen. |
| Identitäts- und Zugriffsmanagement (IAM) | IAM ist ein Internet-Dienst, mit dem Sie den Zugriff auf AWS-Ressourcen sicher kontrollieren können. In dieser Anleitung erstellen Sie eine IAM-Richtlinie und weisen sie einer IAM-Rolle zu, um Ihr S3-Bucket mit Braze Cloud Data Ingestion zu integrieren. |
| Amazon Simple Queue Service (SQS) | SQS ist eine gehostete Warteschlange, mit der Sie verteilte Softwaresysteme und Komponenten integrieren können. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Einrichten der Datenaufnahme in der Cloud in AWS

### Schritt 1: Erstellen Sie einen Quell-Bucket

Erstellen Sie in Ihrem AWS-Konto ein S3-Bucket für allgemeine Zwecke mit Standardeinstellungen. S3-Buckets können über Synchronisierungen hinweg wiederverwendet werden, solange der Ordner eindeutig ist.

Die Standardeinstellungen sind:

- ACLs Deaktiviert
- Sperren Sie den öffentlichen Zugang
- Bucket Versionierung deaktivieren
- SSE-S3 Verschlüsselung

Notieren Sie sich die Region, in der Sie den Bucket erstellt haben, da Sie im nächsten Schritt eine SQS-Warteschlange in derselben Region erstellen werden.

### Schritt 2: SQS-Warteschlange erstellen

Erstellen Sie eine SQS Warteschlange, um zu verfolgen, wann Objekte zu dem von Ihnen erstellten Bucket hinzugefügt werden. Verwenden Sie vorerst die Standard-Konfigurationseinstellungen. 

Eine SQS-Warteschlange muss global eindeutig sein (z.B. kann nur eine für eine CDI-Synchronisierung verwendet werden und kann nicht in einem anderen Workspace wiederverwendet werden).

{% alert important %}
Stellen Sie sicher, dass Sie diese SQS in der gleichen Region anlegen, in der Sie auch den Bucket erstellt haben.
{% endalert %}

Notieren Sie sich unbedingt den ARN und die URL der SQS, da Sie sie während dieser Konfiguration häufig verwenden werden.

![Auswählen von "Erweitert" mit einem JSON-Beispielobjekt, um festzulegen, wer auf eine Warteschlange zugreifen darf.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### Schritt 3: Zugriffsrichtlinie einrichten

Um die Richtlinie für den Zugriff einzurichten, wählen Sie **Erweiterte Optionen**. 

Fügen Sie die folgende Anweisung an die Richtlinie für den Zugriff auf die Warteschlange an. Achten Sie darauf, `YOUR-BUCKET-NAME-HERE` durch den Bucket-Namen, `YOUR-SQS-ARN` durch den ARN Ihrer SQS-Warteschlange und `YOUR-AWS-ACCOUNT-ID` durch Ihre AWS-Konto-ID zu ersetzen: 

``` json 
{
  "Sid": "braze-cdi-s3-sqs-publish",
  "Effect": "Allow",
  "Principal": {
    "Service": "s3.amazonaws.com"
  },
  "Action": "SQS:SendMessage",
  "Resource": "YOUR-SQS-ARN",
  "Condition": {
    "StringEquals": {
      "aws:SourceAccount": "YOUR-AWS-ACCOUNT-ID"
    },
    "ArnLike": {
      "aws:SourceArn": "arn:aws:s3:::YOUR-BUCKET-NAME-HERE"
    }
  }
} 
```

### Schritt 4: Hinzufügen einer Ereignisbenachrichtigung zum S3-Bucket

1. Gehen Sie in dem in Schritt 1 erstellten Bucket zu **Eigenschaften** > **Ereignisbenachrichtigungen**.
2. Geben Sie der Konfiguration einen Namen. Geben Sie optional ein Präfix oder Suffix für das Targeting an, wenn nur eine Teilmenge der Dateien von Braze aufgenommen werden soll.
3. Wählen Sie unter **Ziel** die **SQS Warteschlange** aus und geben Sie den ARN der SQS an, die Sie in Schritt 2 erstellt haben.

{% alert note %}
Wenn Sie Ihre Dateien in den Stammordner eines S3-Buckets hochladen und dann einige der Dateien in einen bestimmten Ordner im Bucket verschieben, kann ein unerwarteter Fehler auftreten. Stattdessen können Sie die Ereignisbenachrichtigungen so ändern, dass sie nur für die Dateien im Präfix gesendet werden, vermeiden, dass Dateien außerhalb dieses Präfixes in den S3-Bucket gelegt werden, oder die Integration ohne Präfix aktualisieren, die dann alle Dateien einliest.
{% endalert %}

### Schritt 5: Erstellen Sie eine IAM-Richtlinie

Erstellen Sie eine IAM Richtlinie, um Braze die Interaktion mit Ihrem Source Bucket zu erlauben. Um loszulegen, melden Sie sich bei der AWS Verwaltungskonsole als Account Administrator an. 

1. Gehen Sie zum Abschnitt IAM der AWS Konsole, wählen Sie in der Navigationsleiste **Richtlinien** aus und wählen Sie dann **Richtlinie erstellen**.<br><br>![Der Button "Richtlinie erstellen" in der AWS-Konsole.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Öffnen Sie den Tab **JSON** und geben Sie den folgenden Code-Snippet in den Abschnitt **Policy Document** ein. Achten Sie darauf, `YOUR-BUCKET-NAME-HERE` durch Ihren Bucket-Namen und `YOUR-SQS-ARN-HERE` durch den Namen Ihrer SQS Warteschlange zu ersetzen: 

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetObjectAttributes", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::YOUR-BUCKET-NAME-HERE/*"]
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:GetQueueUrl",
                "sqs:ReceiveMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "YOUR-SQS-ARN-HERE"
        }
    ]
}

```  

{: start="3"}
3\. Wählen Sie **Richtlinie überprüfen**, wenn Sie fertig sind.

4. Geben Sie der Richtlinie einen Namen und eine Beschreibung und wählen Sie dann **Richtlinie erstellen**.  

![Eine Beispielrichtlinie mit dem Namen "new-policy-name".]({% image_buster /assets/img/create_policy_3_name.png %})

![Das Beschreibungsfeld für die Richtlinie.]({% image_buster /assets/img/create_policy_4_created.png %})

### Schritt 6: Eine IAM-Rolle erstellen

Um die Einrichtung auf AWS abzuschließen, erstellen Sie eine IAM-Rolle und fügen ihr die IAM-Richtlinie aus Schritt 4 zu. 

1. Gehen Sie in demselben IAM-Bereich der Konsole, in dem Sie die IAM-Richtlinie erstellt haben, zu **Rollen** > **Rolle erstellen**. 

<br><br>![Der Button "Rolle erstellen".]({% image_buster /assets/img/create_role_1_list.png %})<br><br>

{: start="2"}
2\. Kopieren Sie die ID des Braze-Kontos für AWS von Ihrem Braze-Dashboard. Gehen Sie zu **Cloud Datenaufnahme**, wählen Sie **Neue Datensynchronisation erstellen** und wählen Sie **S3 Import**.

3. Wählen Sie in AWS **ein anderes AWS-Konto** als SELEKTOR-Typ für vertrauenswürdige Entitäten aus. Geben Sie Ihre Braze-Konto ID an. Wählen Sie das Kontrollkästchen **Externe ID erforderlich** aus, und geben Sie eine externe ID ein, die Braze verwenden soll. Dies ist die externe ID, die beim Erstellen einer S3-Currents-Verbindung im Abschnitt **Zugangsdaten** Ihrer Currents-Verbindung im Braze-Dashboard generiert wurde. Wählen Sie nach Abschluss **Weiter** aus. 

<br><br> ![Die S3-Seite "Rolle erstellen". Diese Seite enthält Felder für den Rollennamen, die Rollenbeschreibung, vertrauenswürdige Entitäten, Richtlinien und die Berechtigungsgrenze.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="4"}
4\. Hängen Sie die in Schritt 4 erstellte Richtlinie an die Rolle an. Suchen Sie die Richtlinie in der Suchleiste, und wählen Sie ein Häkchen neben der Richtlinie aus, um sie anzuhängen. Wählen Sie nach Abschluss **Weiter** aus.

<br><br>![Rollen-ARN mit dem ausgewählten new-policy-name.]({% image_buster /assets/img/create_role_3_attach.png %})<br><br>

Geben Sie der Rolle einen Namen und eine Beschreibung, und wählen Sie **Rolle erstellen**.

<br><br>![Eine Beispielrolle mit dem Namen "new-role-name".]({% image_buster /assets/img/create_role_4_name.png %})<br><br>

{: start="5"}
5\. Notieren Sie sich den ARN der soeben erstellten Rolle und die externe ID, die Sie generiert haben, da Sie diese zum Erstellen der Integration für die Datenaufnahme in der Cloud verwenden werden.

## Einrichten der Datenaufnahme in der Cloud in Braze

1. Um eine neue Integration zu erstellen, gehen Sie zu **Dateneinstellungen** > **Datenaufnahme in der Cloud**, wählen Sie **Neue Datensynchronisation erstellen** und wählen Sie **S3-Import** aus dem Abschnitt Dateiquellen. 
2. Geben Sie die Informationen aus dem AWS-Einrichtungsprozess ein, um eine neue Synchronisierung zu erstellen. Geben Sie Folgendes an:

  - Rollen-ARN
  - Externe ID
  - SQS URL (muss für jede neue Integration eindeutig sein)
  - Bucket-Name
  - Ordnerpfad (optional, muss bei allen Synchronisierungen in einem Workspace eindeutig sein)
  - Region

![Beispiel für die Zugangsdaten, wie sie in S3 angezeigt werden, um eine neue Importsynchronisation zu erstellen.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. Benennen Sie Ihre Integration und wählen Sie den Datentyp für diese Integration aus. 

<br><br>![Einrichten der Synchronisationsdetails für "cdi-s3-als-Quelle-Integration" mit Nutzer:in-Attributen als Datentyp.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

{: start="4"}
4\. Fügen Sie eine E-Mail für Benachrichtigungen hinzu, wenn die Synchronisierung aufgrund von Zugriffs- oder Berechtigungsproblemen unterbrochen wird. Schalten Sie optional Benachrichtigungen für Fehler auf Nutzer:innen-Ebene und erfolgreiche Synchronisierungen ein. 

<br><br> ![Einrichten von Benachrichtigungseinstellungen für Synchronisationsfehler-Benachrichtigungen.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\. Testen Sie schließlich die Verbindung und speichern Sie die Synchronisierung. 

<br><br>![Eine Option zum Testen der Verbindung mit einer Vorschau der Daten.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

## Erforderliche Dateiformate

Cloud Data Ingestion unterstützt JSON-, CSV- und Parquet-Dateien. Jede Datei muss eine oder mehrere der unterstützten Bezeichner-Spalten und eine Nutzdaten-Spalte als JSON String enthalten.

Braze erzwingt keine zusätzlichen Anforderungen an Dateinamen, die über die von AWS erzwungenen hinausgehen. Dateinamen sollten eindeutig sein. Wir empfehlen, zur Eindeutigkeit einen Zeitstempel hinzuzufügen.

### Nutzer:innen Bezeichner

Ihre Quelldatei kann eine oder mehrere Spalten oder Schlüssel mit Nutzer:innen enthalten. Jede Zeile sollte nur einen Bezeichner enthalten, aber eine Quelldatei kann mehrere Arten von Bezeichnern enthalten.

| Bezeichner | Beschreibung |
| --- | --- |
| `EXTERNAL_ID` | Dies ist der Bezeichner des Nutzers:innen, den Sie aktualisieren möchten. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`. |
| `BRAZE_ID` | Der Braze Nutzer:innen Bezeichner. Diese wird vom Braze SDK generiert und neue Nutzer:innen können nicht mit einer Braze ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an. |
| `EMAIL` | Die E-Mail Adresse des Nutzers:innen. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. Wenn Sie sowohl E-Mail als auch Telefon angeben, verwenden wir die E-Mail als primäre Kennung. |
| `PHONE` | Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. |
|`PAYLOAD` | Dies ist ein JSON String mit den Feldern, die Sie mit dem Nutzer:innen in Braze synchronisieren möchten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Anders als bei Data Warehouse-Quellen ist die Spalte `UPDATED_AT` weder erforderlich noch wird sie unterstützt.
{% endalert %}

{% tabs %}
{% tab JSON Attributes %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"name\": \"GT896\", \"age\": 74, \"subscriber\": true, \"retention\": {\"previous_purchases\": 21, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600803\"}"}
{"external_id":"s3-qa-1","payload":"{\"name\": \"HSCJC\", \"age\": 86, \"subscriber\": false, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600824\"}"}
{"external_id":"s3-qa-2","payload":"{\"name\": \"YTMQZ\", \"age\": 43, \"subscriber\": false, \"retention\": {\"previous_purchases\": 23, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600831\"}"}
{"external_id":"s3-qa-3","payload":"{\"name\": \"5P44M\", \"age\": 15, \"subscriber\": true, \"retention\": {\"previous_purchases\": 7, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600838\"}"}
{"external_id":"s3-qa-4","payload":"{\"name\": \"WMYS7\", \"age\": 11, \"subscriber\": true, \"retention\": {\"previous_purchases\": 0, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600844\"}"}
{"external_id":"s3-qa-5","payload":"{\"name\": \"KCBLK\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 11, \"vip\": true}, \"last_visit\": \"2023-08-08T16:03:26.600850\"}"}
{"external_id":"s3-qa-6","payload":"{\"name\": \"T93MJ\", \"age\": 47, \"subscriber\": true, \"retention\": {\"previous_purchases\": 10, \"vip\": false}, \"last_visit\": \"2023-08-08T16:03:26.600856\"}"}
```  
{% alert important %}
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, sonst wird die Datei übersprungen.
{% endalert %}
{% endtab %}
{% tab JSON Custom Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, sonst wird die Datei übersprungen.
{% endalert %}
{% endtab %}
{% tab JSON Purchase Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, sonst wird die Datei übersprungen.
{% endalert %}

{% endtab %}
{% tab CSV Attributes %}
```plaintext  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% tab CSV Catalogs  %}
```plaintext  
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}" 
1,"{""product_name"": ""Product 1"", ""price"": 1.01}" 
```
{% endtab %}

{% endtabs %}  

Beispiele für alle unterstützten Dateitypen finden Sie in den Beispieldateien in [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).  

## Was Sie wissen sollten

- Dateien, die dem S3-Bucket hinzugefügt werden, sollten 512 MB nicht überschreiten. Dateien, die größer als 512 MB sind, führen zu einer Fehlermeldung und werden nicht mit Braze synchronisiert.
- Es gibt zwar keine zusätzliche Begrenzung für die Anzahl der Zeilen pro Datei, aber wir empfehlen, kleinere Dateien zu verwenden, um die Geschwindigkeit Ihrer Synchronisierungen zu erhöhen. Eine 500 MB große Datei würde zum Beispiel wesentlich länger brauchen als fünf einzelne 100 MB große Dateien.
- Es gibt kein zusätzliches Limit für die Anzahl der Dateien, die in einer bestimmten Zeit hochgeladen werden können.
- Das Ordnen in oder zwischen Dateien wird nicht unterstützt. Wir empfehlen, Updates in regelmäßigen Abständen durchzuführen, wenn Sie auf zu erwartende Race-Conditions achten.

## Fehlersuche

### Hochladen von Dateien und Verarbeitung

CDI verarbeitet nur Dateien, die nach der Erstellung der Synchronisierung hinzugefügt werden. Bei diesem Prozess sucht Braze nach neuen Dateien, die hinzugefügt werden sollen, was eine neue Nachricht an SQS triggert. Dadurch wird eine neue Synchronisierung gestartet, um die neue Datei zu verarbeiten.

Vorhandene Dateien können verwendet werden, um die Datenstruktur in der Testverbindung zu validieren, sie werden jedoch nicht mit Braze synchronisiert. Bestehende Dateien, die synchronisiert werden sollen, müssen erneut in S3 hochgeladen werden, um von CDI verarbeitet zu werden.

### Umgang mit unerwarteten Dateifehlern

Wenn Sie eine hohe Anzahl von Fehlern oder fehlgeschlagenen Dateien beobachten, haben Sie möglicherweise einen anderen Prozess, der dem S3-Bucket Dateien in einem anderen Ordner als dem Zielordner für CDI hinzufügt.

Wenn Dateien in den Quell-Bucket hochgeladen werden, sich aber nicht im Quellordner befinden, verarbeitet CDI zwar die SQS-Benachrichtigung, führt aber keine Aktion mit der Datei durch, so dass dies als Fehler erscheinen kann.
