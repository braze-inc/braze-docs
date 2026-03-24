---
nav_title: Integrationen in die Dateiablage
article_title: Integration von Dateispeichern
description: "Diese Seite behandelt die Braze Cloud-Datenaufnahme und wie Sie relevante Daten von S3 mit Braze synchronisieren."
page_order: 3
page_type: reference

---

# Integrationen in die Dateiablage

> Auf dieser Seite erfahren Sie, wie Sie die Unterstützung für die Cloud-Datenaufnahme einrichten und relevante Daten von S3 mit Braze synchronisieren.

Diese Seite zeigt die Synchronisierungs- und Quellschritte, die sich derzeit im Early Access (EA) befinden. Die Schritte für die allgemein verfügbare Version finden Sie unter [Allgemein verfügbare Version](#general-availability-experience).

## Funktionsweise

Sie können Cloud Data Ingestion (CDI) für S3 verwenden, um einen oder mehrere S3-Buckets in Ihrem AWS-Konto direkt in Braze zu integrieren. Wenn neue Dateien in S3 veröffentlicht werden, wird eine Nachricht an SQS gesendet, und Braze Cloud Data Ingestion nimmt diese neuen Dateien auf. 

Cloud Data Ingestion unterstützt Folgendes:

- JSON-Dateien
- CSV-Dateien
- Parquet-Dateien
- Attribute, angepasste Events, Kauf-Events, Nutzer:innen löschen und Katalogdaten

## Voraussetzungen

Für die Integration benötigen Sie die folgenden Ressourcen:

 - S3-Bucket für die Datenspeicherung 
 - SQS-Warteschlange für Benachrichtigungen über neue Dateien 
 - IAM-Rolle für den Braze-Zugriff  

### AWS-Definitionen

Zunächst eine Übersicht der Begriffe, die bei dieser Aufgabe verwendet werden.

| Begriff | Definition |
| --- | --- |
| Amazon Resource Name (ARN) | Der ARN ist ein eindeutiger Bezeichner für AWS-Ressourcen. |
| Identity and Access Management (IAM) | IAM ist ein Webdienst, mit dem Sie den Zugriff auf AWS-Ressourcen sicher kontrollieren können. In dieser Anleitung erstellen Sie eine IAM-Richtlinie und weisen sie einer IAM-Rolle zu, um Ihren S3-Bucket mit Braze Cloud Data Ingestion zu integrieren. |
| Amazon Simple Queue Service (SQS) | SQS ist eine gehostete Warteschlange, mit der Sie verteilte Softwaresysteme und Komponenten integrieren können. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cloud-Datenaufnahme in AWS einrichten

### 1. Schritt: Quell-Bucket erstellen

Erstellen Sie in Ihrem AWS-Konto einen S3-Bucket für allgemeine Zwecke mit Standardeinstellungen. S3-Buckets können über Synchronisierungen hinweg wiederverwendet werden, solange der Ordner eindeutig ist.

Die Standardeinstellungen sind:

- ACLs deaktiviert
- Gesamten öffentlichen Zugriff blockieren
- Bucket-Versionierung deaktivieren
- SSE-S3-Verschlüsselung
  - SSE-S3 ist der einzige unterstützte serverseitige Verschlüsselungstyp. Die Verschlüsselung mit Amazon KMS wird nicht unterstützt.

Notieren Sie sich die Region, in der Sie den Bucket erstellt haben, da Sie im nächsten Schritt eine SQS-Warteschlange in derselben Region erstellen werden.

### 2. Schritt: SQS-Warteschlange erstellen

Erstellen Sie eine SQS-Warteschlange, um zu verfolgen, wann Objekte zu dem von Ihnen erstellten Bucket hinzugefügt werden. Verwenden Sie vorerst die Standard-Konfigurationseinstellungen. 

Eine SQS-Warteschlange muss global eindeutig sein (z. B. kann nur eine für eine CDI-Synchronisierung verwendet werden und nicht in einem anderen Workspace wiederverwendet werden).

{% alert important %}
Stellen Sie sicher, dass Sie diese SQS in derselben Region anlegen, in der Sie auch den Bucket erstellt haben.
{% endalert %}

Notieren Sie sich unbedingt den ARN und die URL der SQS-Warteschlange, da Sie diese während der Konfiguration häufig benötigen werden.

![Auswählen von „Advanced" mit einem Beispiel-JSON-Objekt, um festzulegen, wer auf eine Warteschlange zugreifen darf.]({% image_buster /assets/img/cloud_ingestion/s3_ARN.png %})

### 3. Schritt: Zugriffsrichtlinie einrichten

Um die Zugriffsrichtlinie einzurichten, wählen Sie **Advanced options**. 

Fügen Sie die folgende Anweisung an die Zugriffsrichtlinie der Warteschlange an. Achten Sie darauf, `YOUR-BUCKET-NAME-HERE` durch Ihren Bucket-Namen, `YOUR-SQS-ARN` durch den ARN Ihrer SQS-Warteschlange und `YOUR-AWS-ACCOUNT-ID` durch Ihre AWS-Konto-ID zu ersetzen: 

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

### 4. Schritt: Ereignisbenachrichtigung zum S3-Bucket hinzufügen

1. Gehen Sie in dem in Schritt 1 erstellten Bucket zu **Properties** > **Event notifications**.
2. Geben Sie der Konfiguration einen Namen. Geben Sie optional ein Präfix oder Suffix an, wenn nur eine Teilmenge der Dateien von Braze aufgenommen werden soll.
3. Wählen Sie unter **Destination** die Option **SQS queue** aus und geben Sie den ARN der SQS an, die Sie in Schritt 2 erstellt haben.

{% alert note %}
Wenn Sie Ihre Dateien in den Stammordner eines S3-Buckets hochladen und dann einige der Dateien in einen bestimmten Ordner im Bucket verschieben, kann ein unerwarteter Fehler auftreten. Stattdessen können Sie die Ereignisbenachrichtigungen so ändern, dass sie nur für Dateien im Präfix gesendet werden, keine Dateien außerhalb dieses Präfixes in den S3-Bucket legen oder die Integration ohne Präfix aktualisieren, wodurch dann alle Dateien aufgenommen werden.
{% endalert %}

### 5. Schritt: IAM-Richtlinie erstellen

Erstellen Sie eine IAM-Richtlinie, um Braze die Interaktion mit Ihrem Quell-Bucket zu ermöglichen. Melden Sie sich zunächst bei der AWS-Verwaltungskonsole als Konto-Administrator an. 

1. Gehen Sie zum IAM-Bereich der AWS-Konsole, wählen Sie in der Navigationsleiste **Policies** und dann **Create Policy** aus.<br><br>![Der Button „Create Policy" in der AWS-Konsole.]({% image_buster /assets/img/create_policy_1_list.png %})<br><br>

2. Öffnen Sie den Tab **JSON** und geben Sie das folgende Code-Snippet in den Abschnitt **Policy Document** ein. Achten Sie darauf, `YOUR-BUCKET-NAME-HERE` durch Ihren Bucket-Namen und `YOUR-SQS-ARN-HERE` durch den ARN Ihrer SQS-Warteschlange zu ersetzen: 

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
3. Wählen Sie **Review Policy**, wenn Sie fertig sind.

4. Geben Sie der Richtlinie einen Namen und eine Beschreibung und wählen Sie dann **Create Policy**.  

![Eine Beispielrichtlinie mit dem Namen „new-policy-name".]({% image_buster /assets/img/create_policy_3_name.png %})

![Das Beschreibungsfeld für die Richtlinie.]({% image_buster /assets/img/create_policy_4_created.png %})

### 6. Schritt: IAM-Rolle erstellen

Um die Einrichtung in AWS abzuschließen, erstellen Sie eine IAM-Rolle und hängen die IAM-Richtlinie aus Schritt 5 an. 

1. Gehen Sie in demselben IAM-Bereich der Konsole, in dem Sie die IAM-Richtlinie erstellt haben, zu **Roles** > **Create Role**. 

![Der Button „Create Role".]({% image_buster /assets/img/create_role_1_list.png %})

{: start="2"}
2. Wählen Sie in AWS **Another AWS Account** als Typ für vertrauenswürdige Entitäten aus. Geben Sie Ihre Braze-Konto-ID an. Aktivieren Sie das Kontrollkästchen **Require external ID**.
3. Gehen Sie in Braze zu **Data Settings** > **Cloud Data Ingestion** > **Sources**, wählen Sie **Add data source** und dann **Amazon S3** im Abschnitt Dateiquellen.
4. Kopieren Sie die automatisch generierte **Braze Account ID**. 

![Die Seite „Add New Source" mit den Abschnitten „Source Name" und „S3 Connection Details".]({% image_buster /assets/img/braze_account_id.png %})

{: start="6"}
5. Fügen Sie in AWS die Konto-ID ein und wählen Sie anschließend **Next**.

![Die S3-Seite „Create Role". Diese Seite enthält Felder für den Rollennamen, die Rollenbeschreibung, vertrauenswürdige Entitäten, Richtlinien und die Berechtigungsgrenze.]({% image_buster /assets/img/create_role_2_another.png %})<br><br>

{: start="7"}
6. Hängen Sie die in Schritt 4 erstellte Richtlinie an die Rolle an. Suchen Sie die Richtlinie in der Suchleiste und setzen Sie ein Häkchen neben der Richtlinie, um sie anzuhängen. Wählen Sie anschließend **Next**.

![Rollen-ARN mit der ausgewählten Richtlinie „new-policy-name".]({% image_buster /assets/img/create_role_3_attach.png %})

Geben Sie der Rolle einen Namen und eine Beschreibung und wählen Sie **Create Role**.

![Eine Beispielrolle mit dem Namen „new-role-name".]({% image_buster /assets/img/create_role_4_name.png %})

{: start="8"}
7. Notieren Sie sich den ARN der erstellten Rolle und die generierte externe ID, da Sie diese für die Erstellung der Cloud-Datenaufnahme-Integration benötigen.

## Cloud-Datenaufnahme in Braze einrichten

1. Erstellen Sie zunächst eine neue Quelle im Braze-Dashboard. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Sources**, wählen Sie **Add data source** und dann **Amazon S3**.
2. Wählen Sie einen Namen für Ihre Quelle und geben Sie die Informationen aus dem AWS-Einrichtungsprozess ein, um eine neue Quelle zu erstellen. Geben Sie Folgendes an:

  - Rollen-ARN
  - Externe ID
  - Bucket-Name
  - Region

![Der Abschnitt „S3 Connection Details" mit den Feldern für Zugangsdaten (AWS-Einrichtung und Braze-Einrichtung) und Konfiguration.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_1.png %})

{: start="3"}
3. Wählen Sie **Test connection**, um zu bestätigen, dass Braze auf Ihren Bucket zugreifen kann. Nach einem erfolgreichen Test wählen Sie **Connect to Source**. Falls die Verbindung fehlschlägt, wird eine Fehlermeldung angezeigt, die bei der Fehlerbehebung hilft.

{: start="4"}
4. Erstellen Sie als Nächstes eine neue Synchronisierung. Gehen Sie zu **Data Settings** > **Cloud Data Ingestion** > **Syncs** und wählen Sie **Create data sync**.

![Die Seite „Create New Sync" mit der Konfiguration für Synchronisierungsname und Datenquelle.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_3.png %})

{: start="5"}
5. Wählen Sie einen Namen für Ihre Synchronisierung. Wählen Sie dann eine aktive S3-Quelle aus und geben Sie Ihre Quelltabelle für die Synchronisierung ein. Wählen Sie einen Datentyp und wählen Sie **Test Connection**.

![Eine Option zum Testen der Verbindung mit einer Datenvorschau.]({% image_buster /assets/img/cloud_ingestion/s3_ingestion_4.png %})

6. Geben Sie die restlichen Informationen aus dem AWS-Einrichtungsprozess ein. Geben Sie Folgendes an:
- SQS-URL (muss für jede neue Integration eindeutig sein)
- Ordnerpfad (optional, muss bei allen Synchronisierungen in einem Workspace eindeutig sein)

7. Wählen Sie einen Datentyp und wählen Sie **Test Connection**, um zu bestätigen, dass Braze die verfügbaren Dateien auflisten kann (nicht die Daten in diesen Dateien). Nach Erfolg wählen Sie **Next: Notifications**.
8. Fügen Sie Kontakt-E-Mail(s) für Benachrichtigungen hinzu, falls die Synchronisierung aufgrund von Zugriffs- oder Berechtigungsproblemen unterbrochen wird. Aktivieren Sie optional Benachrichtigungen für Fehler auf Nutzer:innen-Ebene und erfolgreiche Synchronisierungen.
9. Erstellen Sie die Synchronisierung.

{% details Allgemein verfügbare Version %}

1. Um eine neue Integration zu erstellen, gehen Sie zu **Data Settings** > **Cloud Data Ingestion**, wählen Sie **Create New Data Sync** und dann **S3 Import** im Abschnitt Dateiquellen. 
2. Geben Sie die Informationen aus dem AWS-Einrichtungsprozess ein, um eine neue Synchronisierung zu erstellen. Geben Sie Folgendes an:

  - Rollen-ARN
  - Externe ID
  - SQS-URL (muss für jede neue Integration eindeutig sein)
  - Bucket-Name
  - Ordnerpfad (optional, muss bei allen Synchronisierungen in einem Workspace eindeutig sein)
  - Region

{: start="3"}
3. Benennen Sie Ihre Integration und wählen Sie den Datentyp für diese Integration aus. 

{: start="4"}
4. Fügen Sie eine Kontakt-E-Mail für Benachrichtigungen hinzu, falls die Synchronisierung aufgrund von Zugriffs- oder Berechtigungsproblemen unterbrochen wird. Aktivieren Sie optional Benachrichtigungen für Fehler auf Nutzer:innen-Ebene und erfolgreiche Synchronisierungen. 

{: start="5"}
5. Wählen Sie abschließend **Test connection**, um zu bestätigen, dass Braze auf Ihren Bucket zugreifen und die verfügbaren Dateien auflisten kann (nicht die Daten in diesen Dateien). Speichern Sie anschließend die Synchronisierung. 

{% enddetails %}

## Erforderliche Dateiformate

Cloud Data Ingestion unterstützt JSON-, CSV- und Parquet-Dateien. Die erforderlichen Spalten hängen vom Datentyp ab: 

- Nutzerdaten (Attribute, angepasste Events, Kauf-Events) verwenden Nutzer:innen-Bezeichner und eine Nutzlast
- Katalogdaten verwenden Katalog-Bezeichner

Braze erzwingt keine zusätzlichen Anforderungen an Dateinamen über die von AWS vorgegebenen hinaus. Dateinamen sollten eindeutig sein. Wir empfehlen, zur Eindeutigkeit einen Zeitstempel anzuhängen.

Beispiele für alle unterstützten Dateitypen (Attribute, angepasste Events, Käufe, Kataloge und Nutzer:innen löschen) finden Sie in den Beispieldateien unter [braze-examples](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion/braze-examples/payloads/file_storage).

### Nutzer:innen-Bezeichner {#user-identifiers}

Für Nutzerdaten-Synchronisierungen (Attribute, angepasste Events, Kauf-Events) muss jede Zeile in Ihrer Quelldatei genau einen Nutzer:innen-Bezeichner und eine `PAYLOAD`-Spalte enthalten. Eine Quelldatei kann Zeilen mit verschiedenen Bezeichnertypen enthalten, aber jede einzelne Zeile sollte nur einen verwenden.

| Bezeichner | Beschreibung |
| --- | --- |
| `EXTERNAL_ID` | Identifiziert die Nutzer:in, die Sie aktualisieren möchten. Dieser Wert sollte dem in Braze verwendeten `external_id` entsprechen. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Diese beiden Spalten erstellen ein Nutzer-Alias-Objekt. `alias_name` sollte ein eindeutiger Bezeichner sein, und `alias_label` gibt den Typ des Alias an. Nutzer:innen können mehrere Aliase mit unterschiedlichen Labels haben, aber nur einen `alias_name` pro `alias_label`. |
| `BRAZE_ID` | Der Braze-Nutzer:innen-Bezeichner. Dieser wird vom Braze SDK generiert, und neue Nutzer:innen können nicht mit einer Braze-ID über Cloud Data Ingestion erstellt werden. Um neue Nutzer:innen anzulegen, geben Sie eine externe Nutzer-ID oder einen Nutzer-Alias an. |
| `EMAIL` | Die E-Mail-Adresse der Nutzer:in. Wenn mehrere Profile mit derselben E-Mail-Adresse vorhanden sind, wird das zuletzt aktualisierte Profil bei Updates bevorzugt. Wenn Sie sowohl E-Mail als auch Telefonnummer angeben, verwendet Braze die E-Mail als primären Bezeichner. |
| `PHONE` | Die Telefonnummer der Nutzer:in. Wenn mehrere Profile mit derselben Telefonnummer vorhanden sind, wird das zuletzt aktualisierte Profil bei Updates bevorzugt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Zusätzlich zu einem Bezeichner muss jede Zeile eine `PAYLOAD`-Spalte enthalten, die einen JSON-String mit den Feldern enthält, die Sie mit der Nutzer:in in Braze synchronisieren möchten.

{% alert note %}
Anders als bei Data-Warehouse-Quellen ist die Spalte `UPDATED_AT` für Dateispeicher-Synchronisierungen weder erforderlich noch unterstützt.
{% endalert %}

### Katalog-Bezeichner {#catalog-identifiers}

Für Katalog-Synchronisierungen muss Ihre Quelldatei die folgenden Spalten enthalten. Katalogdateien verwenden andere Bezeichner als Nutzerdaten-Dateien.

| Spalte | Erforderlich | Beschreibung |
| --- | --- | --- |
| `ID` | Ja | Der eindeutige Bezeichner für den Katalogartikel. Wird verwendet, um den Artikel in Braze zu erstellen, zu aktualisieren oder zu löschen. |
| `PAYLOAD` | Ja | Ein JSON-String mit den Katalogfeldern und -werten, die synchronisiert werden sollen. Muss dem Schema Ihres Katalogs in Braze entsprechen. |
| `DELETED` | Nein | Wenn `true`, wird der Katalogartikel mit der entsprechenden `ID` aus dem Katalog in Braze entfernt. Lassen Sie diese Spalte weg oder setzen Sie sie auf `false` für Erstell- oder Aktualisierungsvorgänge. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Beispiele

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
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
Fügen Sie eine optionale `DELETED`-Spalte hinzu. Wenn `DELETED` den Wert `true` hat, wird dieser Katalogartikel aus dem Katalog in Braze entfernt. Die vollständige Liste der erforderlichen Spalten finden Sie unter [Katalog-Bezeichner](#catalog-identifiers). Informationen zum Löschverhalten finden Sie unter [Katalogartikel löschen](#deleting-catalog-items).
{% endtab %}

{% endtabs %}  

## Daten löschen

Cloud Data Ingestion für S3 unterstützt das Löschen von Nutzer:innen und Katalogartikeln über Datei-Uploads. Verwenden Sie für jedes Szenario separate Synchronisierungen und Dateiformate.

- **[Nutzer:innen löschen](#deleting-users)** – Erstellen Sie eine Synchronisierung mit dem Datentyp **Delete Users** und laden Sie Dateien hoch, die ausschließlich Nutzer:innen-Bezeichner enthalten (keine Nutzlast).
- **[Katalogartikel löschen](#deleting-catalog-items)** – Nutzen Sie Ihre bestehende Katalogsynchronisierung und fügen Sie eine Spalte `deleted` (oder `DELETED`) hinzu, um Artikel zum Entfernen zu markieren.

### Nutzer:innen löschen

So löschen Sie Nutzerprofile in Braze mithilfe von Dateien in S3:

1. Erstellen Sie eine neue Cloud-Datenaufnahme-Synchronisierung (gleiche [AWS- und Braze-Einrichtung](#setting-up-cloud-data-ingestion-in-aws) wie für andere Synchronisierungen).
2. Stellen Sie bei der Konfiguration der Synchronisierung in Braze den **Datentyp** auf **Delete Users** ein.
3. Laden Sie Dateien in Ihren S3-Bucket hoch, die ausschließlich Spalten mit Nutzer:innen-Bezeichnern enthalten. Fügen Sie keine `PAYLOAD`-Spalte hinzu – die Synchronisierung schlägt fehl, wenn eine Nutzlast vorhanden ist, um versehentliche Löschungen zu vermeiden.

Jede Zeile in der Datei muss genau eine Nutzer:in identifizieren, und zwar mit einer der folgenden Angaben:

| Bezeichner | Beschreibung |
| --- | --- |
| `EXTERNAL_ID` | Entspricht dem in Braze verwendeten `external_id`. |
| `ALIAS_NAME` und `ALIAS_LABEL` | Beide Spalten zusammen identifizieren die Nutzer:in anhand des Nutzer-Alias. |
| `BRAZE_ID` | Von Braze generierte Nutzer-ID (nur für bestehende Nutzer:innen). |

{% alert important %}
Das Löschen von Nutzer:innen ist endgültig und kann nicht rückgängig gemacht werden. Schließen Sie nur Nutzer:innen ein, die Sie tatsächlich entfernen möchten. Weitere Informationen finden Sie unter [Nutzer:innen mit Cloud-Datenaufnahme löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/delete_users/).
{% endalert %}

**Beispiel – JSON (Nutzer:innen löschen):**
```jsonl
{"external_id":"user-to-delete-001"}
{"external_id":"user-to-delete-002"}
{"braze_id":"braze-id-from-profile"}
```

**Beispiel – CSV (Nutzer:innen löschen):**
```plaintext
external_id
user-to-delete-001
user-to-delete-002
```

Wenn die Synchronisierung ausgeführt wird, verarbeitet Braze neue Dateien im Bucket und löscht die entsprechenden Nutzerprofile.

### Katalogartikel löschen

So entfernen Sie Artikel aus einem Katalog mithilfe von Dateispeicher:

1. Verwenden Sie dieselbe S3-Synchronisierung, die Sie zur [Synchronisierung von Katalogdaten]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/) (Datentyp **Catalogs**) verwenden.
2. Fügen Sie in Ihren CSV- oder JSON-Dateien eine optionale Spalte **`deleted`** (oder **`DELETED`**) hinzu.
3. Setzen Sie `deleted` auf `true` für jeden Katalogartikel, den Sie aus dem Katalog in Braze entfernen möchten.

Jede Zeile benötigt weiterhin `ID` und `PAYLOAD`. Bei zum Löschen markierten Zeilen kann die Nutzlast minimal sein; Braze entfernt den Artikel anhand der `ID`.

**Beispiel – JSON (Katalogartikel löschen):**
```jsonl
{"id":"85","payload":"{\"product_name\": \"Product 85\", \"price\": 85.85}"}
{"id":"1","payload":"{\"product_name\": \"Product 1\", \"price\": 1.01}","deleted":true}
```

**Beispiel – CSV (Katalogartikel löschen):**
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```

Wenn die Synchronisierung ausgeführt wird, führen Zeilen mit `deleted: true` dazu, dass der entsprechende Katalogartikel in Braze gelöscht wird. Informationen zum vollständigen Synchronisierungs- und Löschverhalten von Katalogdaten finden Sie unter [Katalogdaten synchronisieren und löschen]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/).

## Wissenswertes

- Dateien, die dem S3-Quell-Bucket hinzugefügt werden, sollten 512&nbsp;MB nicht überschreiten. Dateien, die größer als 512&nbsp;MB sind, führen zu einem Fehler und werden nicht mit Braze synchronisiert.
- Es gibt zwar keine zusätzliche Begrenzung für die Anzahl der Zeilen pro Datei, aber wir empfehlen, kleinere Dateien zu verwenden, um die Geschwindigkeit Ihrer Synchronisierungen zu verbessern. Eine 500&nbsp;MB große Datei würde beispielsweise deutlich länger zur Aufnahme benötigen als fünf einzelne 100&nbsp;MB große Dateien.
- Es gibt kein zusätzliches Limit für die Anzahl der Dateien, die in einem bestimmten Zeitraum hochgeladen werden können.
- Die Reihenfolge innerhalb von oder zwischen Dateien wird nicht garantiert. Wir empfehlen, Updates in regelmäßigen Abständen zu bündeln, wenn Sie auf mögliche Race-Conditions achten.

## Fehlerbehebung

### Hochladen und Verarbeitung von Dateien

CDI verarbeitet nur Dateien, die nach der Erstellung der Synchronisierung hinzugefügt werden. Dabei sucht Braze nach neu hinzugefügten Dateien, was eine neue Nachricht an SQS triggert. Dadurch wird eine neue Synchronisierung gestartet, um die neue Datei zu verarbeiten.

Sie können vorhandene Dateien verwenden, um zu überprüfen, ob Braze auf Ihren Bucket zugreifen und aufzunehmende Dateien erkennen kann. Diese Dateien werden jedoch nicht mit Braze synchronisiert. Damit CDI sie verarbeiten kann, müssen Sie alle vorhandenen Dateien, die synchronisiert werden sollen, erneut auf S3 hochladen. 

### Umgang mit unerwarteten Dateifehlern

Wenn Sie eine hohe Anzahl von Fehlern oder fehlgeschlagenen Dateien beobachten, fügt möglicherweise ein anderer Prozess Dateien in einem anderen Ordner als dem CDI-Zielordner zum S3-Bucket hinzu.

Wenn Dateien in den Quell-Bucket, aber nicht in den Quellordner hochgeladen werden, verarbeitet CDI zwar die SQS-Benachrichtigung, führt aber keine Aktion mit der Datei durch – dies kann daher als Fehler erscheinen.