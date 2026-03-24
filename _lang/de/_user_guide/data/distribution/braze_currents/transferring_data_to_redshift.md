---
nav_title: Daten an Redshift übertragen
article_title: Datenübertragung an Redshift
page_order: 8
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie Daten von Amazon S3 über einen Extract, Transform, Load (ETL)-Prozess nach Redshift übertragen."
tool: Currents

---

# Daten an Redshift übertragen

> [Amazon Redshift](https://aws.amazon.com/redshift/) ist ein beliebtes Data Warehouse, das auf Amazon Serviceleistungen; Dienste neben Amazon S3 läuft. Die Daten aus Currents sind so strukturiert, dass sie direkt in Redshift übertragen werden können.

Im Folgenden wird beschrieben, wie Daten von Amazon S3 über einen ETL-Prozess (Extract, Transform, Load) zu Redshift übertragen werden können. Den vollständigen Code finden Sie im [GitHub-Repository](https://github.com/Appboy/currents-examples) „Currents examples“.

{% alert important %}
Dies ist nur eine von vielen Optionen, die Sie wählen können, wenn es darum geht, Ihre Daten an Orte zu übertragen, die für Sie am vorteilhaftesten sind.
{% endalert %}

## Übersicht über den S3-zu-Redshift-Loader

Das[`s3loader.py`](https://github.com/Appboy/currents-examples/tree/master/redshift-s3-loader)Skript verwendet eine separate Manifesttabelle in derselben Redshift-Datenbank, um die bereits kopierten Dateien zu verfolgen. Die allgemeine Struktur ist wie folgt:

1. Listen Sie alle Dateien in S3 auf und identifizieren Sie anschließend die neuen Dateien seit der letzten Ausführung,`s3loader.py`indem Sie die Liste mit dem Bezeichner der Manifesttabelle vergleichen.
2. Erstellen Sie eine Manifestdatei, die die neuen Dateien enthält.
3. Führen Sie eine`COPY`Abfrage aus, um die neuen Dateien mithilfe der Manifestdatei von S3 nach Redshift zu kopieren.
4. Bitte fügen Sie die Namen der Dateien ein, die in die separate Manifesttabelle in Redshift kopiert werden.
5. Verpflichten Sie sich.

## Abhängigkeiten

Bitte installieren Sie das AWS Python SDK und Psycopg, um den Loader ausführen zu können:

```bash
pip install boto3
pip install psycopg2
```

## Berechtigungen

### Redshift-Rolle mit Lesezugriff auf S3

Falls Sie dies noch nicht getan haben, erstellen Sie gemäß der [AWS-Dokumentation](http://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-create-an-iam-role.html) eine Rolle, die Befehle für Ihre Dateien`COPY` in S3 ausführen kann.

### Redshift VPC-eingehende Regeln

Wenn sich Ihr Redshift-Cluster in einer VPC befindet, müssen Sie die VPC so konfigurieren, dass Verbindungen von dem Server zulässig sind, auf dem Sie den S3 Loader ausführen. Bitte gehen Sie in Ihren Redshift-Cluster und wählen Sie den Eintrag „VPC Security Groups“ aus, mit dem sich der Loader verbinden soll. Fügen Sie anschließend eine neue eingehende Regel hinzu: **Typ** = Redshift, **Protokoll** = TCP, **Port** = der Port für Ihren Cluster, **Quelle** = die IP-Adresse des Servers, auf dem der Loader ausgeführt wird (oder „Anywhere“ für Testzwecke).

### Identitäts- und Zugriffsmanagement (IAM)-Nutzer:in mit Vollzugriff auf S3

Der S3-Loader benötigt Lesezugriff auf die Dateien, die Ihre Currents-Daten enthalten, sowie Vollzugriff auf den Standort der Manifestdateien, die er für die `COPY`Redshift-Befehle generiert. Erstellen Sie einen neuen Nutzer für die Identitäts- und Zugriffsverwaltung (IAM) mit der entsprechenden`AmazonS3FullAccess` Berechtigung über die [IAM-Konsole](https://console.aws.amazon.com/iam/home#/users). Bitte speichern Sie die Zugangsdaten, da Sie diese an den Loader übermitteln müssen.

Sie können die Zugangsdaten über Umgebungsvariablen, die gemeinsam genutzte Anmeldedatei (`~/.aws/credentials`) oder die [AWS-Konfigurationsdatei](http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials) an den Loader übergeben. Alternativ können Sie diese direkt in den Loader einfügen, indem Sie sie den`aws_secret_access_key``aws_access_key_id`Feldern und innerhalb eines`S3LoadJob`Objekts zuweisen. Wir empfehlen jedoch nicht, Zugangsdaten fest in Ihrem Code zu codieren.

## Nutzung

### Beispiel für die Verwendung

Das folgende Beispielprogramm lädt Daten für das`users.messages.contentcard.Impression`Ereignis aus S3 in die`content_card_impression`Tabelle in Redshift.

```
if __name__ == '__main__':
    host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
    port = 5439
    database = '{YOUR_DATABASE}'
    user = '{YOUR_USER}'
    password = '{YOUR_PASSWORD}'
    role = '{YOUR_REDSHIFT_ROLE_ARN}'

    # Do not hard code these credentials.
    aws_access_key_id = None
    aws_secret_access_key = None

    # Content Card Impression Avro fields:
    #   id            - string
    #   user_id       - string
    #   external_user_id - string (nullable)
    #   app_id        - string
    #   content_card_id  - string
    #   campaign_id   - string (nullable)
    #   send_id       - string (nullable)
    #   time          - int
    #   platform      - string (nullable)
    #   device_model  - string (nullable)

    print('Loading Content Card Impression...')
    cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
    cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
    cc_impression_redshift_table = 'content_card_impression'
    cc_impression_redshift_column_def = [
        ('id', 'text'),
        ('user_id', 'text'),
        ('external_user_id', 'text'),
        ('app_id', 'text'),
        ('content_card_id', 'text'),
        ('campaign_id', 'text'),
        ('send_id', 'text'),
        ('time', 'integer'),
        ('platform', 'text'),
        ('device_model', 'text')
    ]

    cc_impression_redshift = RedshiftEndpoint(host, port, database, user, password,
        cc_impression_redshift_table, cc_impression_redshift_column_def)
    cc_impression_s3 = S3Endpoint(cc_impression_s3_bucket, cc_impression_s3_prefix)

    cc_impression_job = S3LoadJob(cc_impression_redshift, cc_impression_s3, role,
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    cc_impression_job.perform()
```

### Zugangsdaten

Um den Loader auszuführen, müssen Sie zunächst die `host`, `port`, und`database`  Ihres Redshift-Clusters sowie die`user`  und`password`  eines Redshift-Nutzers angeben, der  Abfragen`COPY` ausführen kann. Darüber hinaus müssen Sie die ARN der Redshift-Rolle mit S3-Lesezugriff angeben, die Sie in einem vorherigen Abschnitt erstellt haben.

```
host = '{YOUR_CLUSTER}.redshift.amazonaws.com'
port = 5439
database = '{YOUR_DATABASE}'
user = '{YOUR_USER}'
password = '{YOUR_PASSWORD}'
role = '{YOUR_REDSHIFT_ROLE_ARN}'
```

### Jobkonfiguration

Bitte geben Sie den S3-Bucket und das Präfix Ihrer Ereignisdateien sowie den Namen der Redshift-Tabelle an, in die Sie die Daten`COPY`importieren möchten.

Zusätzlich zu`COPY`den Avro-Dateien mit der Option „auto“, wie vom Loader gefordert, muss die Spaltendefinition in Ihrer Redshift-Tabelle mit den Feldnamen im Avro-Schema übereinstimmen, wie im Beispielprogramm gezeigt, mit der entsprechenden Typ-Abbildung (z. B.`string`zu `text`,`int`zu `integer`).

Sie können dem Loader auch eine`batch_size`Option übergeben, wenn Sie feststellen, dass das Kopieren aller Dateien auf einmal zu lange dauert. Die Übergabe eines Parameters`batch_size`erlaubt es dem Loader, schrittweise jeweils einen Batch zu kopieren und zu übertragen, ohne alles gleichzeitig kopieren zu müssen. Die Dauer des Ladens eines Batches hängt sowohl von der Größe Ihrer `batch_size`Dateien als auch von der Größe Ihres Redshift-Clusters ab.

```
# Content Card Impression Avro fields:
#   id            - string
#   user_id       - string
#   external_user_id - string (nullable)
#   app_id        - string
#   content_card_id  - string
#   campaign_id   - string (nullable)
#   send_id       - string (nullable)
#   time          - int
#   platform      - string (nullable)
#   device_model  - string (nullable)
cc_impression_s3_bucket = '{YOUR_CURRENTS_BUCKET}'
cc_impression_s3_prefix = '{YOUR_CURRENTS_PREFIX}'
cc_impression_redshift_table = 'content_card_impression'
cc_impression_redshift_column_def = [
    ('id', 'text'),
    ('user_id', 'text'),
    ('external_user_id', 'text'),
    ('app_id', 'text'),
    ('content_card_id', 'text'),
    ('campaign_id', 'text'),
    ('send_id', 'text'),
    ('time', 'integer'),
    ('platform', 'text'),
    ('device_model', 'text')
]
cc_impression_batch_size = 1000
```