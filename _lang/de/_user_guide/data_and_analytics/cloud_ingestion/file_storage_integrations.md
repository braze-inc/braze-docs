---
nav_title: Integration von Dateispeichern
article_title: Dateispeicher-Integrationen
description: "Dieser Referenzartikel behandelt die Datenaufnahme in der Braze Cloud und wie Sie relevante Daten von S3 mit Braze synchronisieren"
page_order: 3
page_type: reference

---

# Integrationen in die Dateiablage

> Dieser Artikel beschreibt, wie Sie die Unterstützung für die Datenaufnahme in der Cloud einrichten und relevante Daten von S3 mit Braze synchronisieren.

Sie können Cloud Data Ingestion (CDI) für S3 verwenden, um einen oder mehrere S3-Buckets in Ihrem AWS-Konto direkt in Braze zu integrieren. Wenn neue Dateien in S3 veröffentlicht werden, wird eine Nachricht an SQS gesendet, und Braze Cloud Data Ingestion nimmt diese neuen Dateien auf. 

Cloud Data Ingestion unterstützt JSON-, CSV- und Parquet-Dateien sowie Attribute, Event-, Kauf- und Nutzerdaten.

Für die Integration benötigen Sie die folgenden Ressourcen:
 - S3-Bucket für die Speicherung von Daten 
 - SQS-Warteschlange für Benachrichtigungen über neue Dateien 
 - IAM-Rolle für Braze-Zugriff  


## AWS-Definitionen

Lassen Sie uns zunächst einige der Begriffe definieren, die in dieser Aufgabe verwendet werden.

| Text | Definition |
| --- | --- |
| Amazon Ressourcen-Name (ARN) | Der ARN ist ein eindeutiger Bezeichner für AWS-Ressourcen. |
| Identitäts- und Zugriffsmanagement (IAM) | IAM ist ein Internet-Dienst, mit dem Sie den Zugriff auf AWS-Ressourcen sicher kontrollieren können. In dieser Anleitung erstellen Sie eine IAM-Richtlinie und weisen sie einer IAM-Rolle zu, um Ihr S3-Bucket mit Braze Cloud Data Ingestion zu integrieren. |
| Amazon Simple Queue Service (SQS) | SQS ist eine gehostete Warteschlange, mit der Sie verteilte Softwaresysteme und Komponenten integrieren können. |
{: .reset-td-br-1 .reset-td-br-2 }
 

## Einrichten der Datenaufnahme in der Cloud in AWS

### Schritt 1: Erstellen Sie einen Quell-Bucket

Erstellen Sie ein allgemeines S3-Bucket mit Standardeinstellungen in Ihrem AWS-Konto. 

Die Standardeinstellungen sind:
  - ACLs Deaktiviert
  - Sperren Sie den öffentlichen Zugang
  - Bucket Versionierung deaktivieren
  - SSE-S3 Verschlüsselung

Notieren Sie sich die Region, in der Sie den Bucket erstellt haben, da Sie im nächsten Schritt eine SQS-Warteschlange in derselben Region erstellen werden.

### Schritt 2: SQS-Warteschlange erstellen

Erstellen Sie eine SQS Warteschlange, um zu verfolgen, wann Objekte zu dem von Ihnen erstellten Bucket hinzugefügt werden. Verwenden Sie vorerst die Standard-Konfigurationseinstellungen.

{% alert important %}
Stellen Sie sicher, dass Sie diese SQS in derselben Region anlegen, in der Sie auch den Bucket angelegt haben.
{% endalert %}

Notieren Sie sich unbedingt den ARN und die URL der SQS, da Sie sie während dieser Konfiguration häufig verwenden werden.
<br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})
<br><br>

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

### Schritt 4: Hinzufügen einer Event-Benachrichtigung zum S3-Bucket

1. Gehen Sie in dem in Schritt 1 erstellten Bucket zu **Eigenschaften** > **Ereignisbenachrichtigungen**.

2. Geben Sie der Konfiguration einen Namen. Geben Sie optional ein Präfix oder Suffix für das Targeting an, wenn nur eine Teilmenge der Dateien von Braze aufgenommen werden soll.

3. Wählen Sie unter **Ziel** die **SQS Warteschlange** aus und geben Sie den ARN der SQS an, die Sie in Schritt 2 erstellt haben.

### Schritt 5: Erstellen Sie eine IAM-Richtlinie

Erstellen Sie eine IAM Richtlinie, um Braze die Interaktion mit Ihrem Source Bucket zu erlauben. Um loszulegen, melden Sie sich bei der AWS Verwaltungskonsole als Account Administrator an. 

1. Gehen Sie zum Abschnitt IAM der AWS Konsole, wählen Sie in der Navigationsleiste **Richtlinien** aus und wählen Sie dann **Richtlinie erstellen**.<br><br>![]({{site.baseurl}}/assets/img/create_policy_1_list.png)<br><br>

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

4. Geben Sie der Richtlinie einen Namen und eine Beschreibung und wählen Sie **Richtlinie erstellen**.  

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Schritt 6: Eine IAM-Rolle erstellen

Um die Einrichtung auf AWS abzuschließen, erstellen Sie eine IAM-Rolle und fügen ihr die IAM-Richtlinie aus Schritt 4 zu. 

1. Gehen Sie in demselben IAM-Bereich der Konsole, in dem Sie die IAM-Richtlinie erstellt haben, zu **Rollen** > **Rolle erstellen**. <br><br>![]({{site.baseurl}}/assets/img/create_role_1_list.png)<br><br>

2. Kopieren Sie die ID des Braze-Kontos für AWS von Ihrem Braze-Dashboard. Gehen Sie zu **Cloud Datenaufnahme**, klicken Sie auf **Neue Datensynchronisation erstellen** und wählen Sie **S3 Import**. <br><br>![]({{site.baseurl}}/assets/img/cloud_ingestion/s3_copy_braze_account_id.png)<br><br>

3. Wählen Sie in AWS **ein anderes AWS-Konto** als SELEKTOR-Typ für vertrauenswürdige Entitäten aus. Geben Sie die ID Ihres Braze-Kontos an, wählen Sie das Kontrollkästchen **Externe ID erforderlich** und geben Sie eine externe ID ein, die Braze verwenden soll. Wählen Sie nach Abschluss **Weiter** aus. <br><br> ![Die S3-Seite "Rolle erstellen". Diese Seite enthält Felder für den Rollennamen, die Rollenbeschreibung, vertrauenswürdige Entitäten, Richtlinien und die Berechtigungsgrenze.]({{site.baseurl}}/assets/img/create_role_2_another.png)

4. Hängen Sie die in Schritt 4 erstellte Richtlinie an die Rolle an. Suchen Sie die Richtlinie in der Suchleiste, und wählen Sie ein Häkchen neben der Richtlinie aus, um sie anzuhängen. Wählen Sie nach Abschluss **Weiter** aus.<br><br>![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)<br><br>Geben Sie der Rolle einen Namen und eine Beschreibung, und klicken Sie auf **Rolle erstellen**.<br><br>![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)<br><br>

{: start="5"}
5\. Notieren Sie sich den ARN der soeben erstellten Rolle und die externe ID, die Sie generiert haben, da Sie diese für die Integration der Datenaufnahme in der Cloud verwenden werden.  

## Einrichten der Datenaufnahme in der Cloud in Braze

1. Um eine neue Integration zu erstellen, gehen Sie zu **Dateneinstellungen** > **Datenaufnahme in der Cloud**, wählen Sie **Neue Datensynchronisation erstellen** und wählen Sie **S3-Import** aus dem Abschnitt Dateiquellen. 

2. Geben Sie die Informationen aus dem AWS-Einrichtungsprozess ein, um eine neue Synchronisierung zu erstellen. Geben Sie Folgendes an:
- Rollen-ARN
- Externe ID
- SQS URL (muss für jede neue Integration eindeutig sein)
- Bucket-Name
- Ordnerpfad (optional)
- Region  

![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3\. Geben Sie Ihrer Integration einen Namen, und wählen Sie den Datentyp für diese Integration aus. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_2.png %})<br><br>

4. Fügen Sie eine E-Mail für Benachrichtigungen hinzu, wenn die Synchronisierung aufgrund von Zugriffs- oder Berechtigungsproblemen unterbrochen wird. Schalten Sie optional Benachrichtigungen für Fehler auf Nutzer:innen-Ebene und erfolgreiche Synchronisierungen ein. <br><br> ![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})<br><br>

{: start="5"}
5\. Testen Sie schließlich die Verbindung und speichern Sie die Synchronisierung. <br><br>![]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})


## Erforderliche Dateiformate

Cloud Data Ingestion unterstützt JSON-, CSV- und Parquet-Dateien. Jede Datei muss eine oder mehrere der unterstützten Bezeichner-Spalten und eine Nutzdaten-Spalte als JSON String enthalten. 

- Nutzer:innen Bezeichner. Ihre Quelldatei kann eine oder mehrere Spalten oder Schlüssel mit Nutzer:innen enthalten. Jede Zeile sollte nur einen Bezeichner enthalten, aber eine Quelldatei kann mehrere Arten von Bezeichnern enthalten. 
    - `EXTERNAL_ID` - Dies ist der Bezeichner der Nutzerin oder des Nutzers, den oder die Sie aktualisieren möchten. Dies sollte dem in Braze verwendeten Wert `external_id` entsprechen. 
    - `ALIAS_NAME` und `ALIAS_LABEL` \- Diese beiden Spalten erstellen ein Benutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt die Art des Alias an. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`.
    - `BRAZE_ID` - Die Braze-Benutzerkennung. Diese wird vom Braze SDK generiert und neue Nutzer:innen können nicht mit einer Braze ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an.
    - `EMAIL` - Die E-Mail-Adresse des Benutzers. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. Wenn Sie sowohl E-Mail als auch Telefon angeben, verwenden wir die E-Mail als primäre Kennung.
    - `PHONE` - Die Telefonnummer der Nutzerin oder des Nutzers. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil bei der Aktualisierung bevorzugt. 
- `PAYLOAD` - Dies ist ein JSON String mit den Feldern, die Sie mit dem Nutzer:innen in Braze synchronisieren möchten.

{% alert note %}
Anders als bei Data Warehouse-Quellen ist die Spalte `UPDATED_AT` weder erforderlich noch wird sie unterstützt.
{% endalert %}

{% alert note %}
Die zum S3-Bucket hinzugefügten Dateien sollten 512 MB nicht überschreiten. Dateien, die größer als 512 MB sind, führen zu einer Fehlermeldung und werden nicht mit Braze synchronisiert.
{% endalert %}

{% tabs %}
{% tab JSON Attribute %}
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
{% tab JSON angepasste Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"name\": \"view-206\", \"time\": \"2024-04-02T14:34:08\", \"properties\": {\"bool_value\": false, \"preceding_event\": \"unsubscribe\", \"important_number\": 206}}"}
```  
{% alert important %}
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, sonst wird die Datei übersprungen.
{% endalert %}
{% endtab %}
{% tab JSON Kauf-Events %}
``` json  
{"external_id":"s3-qa-0","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
{"external_id":"s3-qa-1","payload":"{\"app_id\": \"YOUR_APP_ID\", \"product_id\": \"product-11\", \"currency\": \"BSD\", \"price\": 8.511527858335066, \"time\": \"2024-04-02T14:34:08\", \"quantity\": 19, \"properties\": {\"is_a_boolean\": true, \"important_number\": 40, \"preceding_event\": \"click\"}}"}
```  
{% alert important %}
Jede Zeile in Ihrer Quelldatei muss gültiges JSON enthalten, sonst wird die Datei übersprungen.
{% endalert %}

{% endtab %}
{% tab CSV-Attribute %}
``` csv  
external_id,payload
s3-qa-load-0-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""SNXIM"", ""age"": 54, ""subscriber"": true, ""retention"": {""previous_purchases"": 19, ""vip"": true}, ""last_visit"": ""2023-08-08T16:03:26.598806""}"
s3-qa-load-1-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""0J747"", ""age"": 73, ""subscriber"": false, ""retention"": {""previous_purchases"": 22, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598816""}"
s3-qa-load-2-d0daa196-cdf5-4a69-84ae-4797303aee75,"{""name"": ""EP1U0"", ""age"": 99, ""subscriber"": false, ""retention"": {""previous_purchases"": 23, ""vip"": false}, ""last_visit"": ""2023-08-08T16:03:26.598822""}"
```
{% endtab %}
{% endtabs %}  

Beispiele für alle unterstützten Dateitypen finden Sie in den Beispieldateien in [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).  
