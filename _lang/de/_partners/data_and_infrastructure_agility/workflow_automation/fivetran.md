---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Fivetran, einem Tool zur Workflow-Automatisierung, das Sie bei der datengestützten Entscheidungsfindung unterstützen kann, indem es Ihnen abfragefertige Daten in Ihr Cloud-Warehouse liefert."
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/) ist eine weltweit anerkannte Marke, deren auf Analysten ausgerichtete Produkte und vollständig verwaltete Pipelines datengestützte Entscheidungen ermöglichen, indem sie abfragefertige Daten in Ihr Cloud Warehouse liefern.

Die Integration von Braze und Fivetran ermöglicht es Anwendern, eine wartungsfreie Pipeline zu erstellen, mit der Sie Braze-Daten sammeln und analysieren können, indem Sie alle Ihre Anwendungen und Datenbanken mit einem zentralen Warehouse verbinden. Nachdem die Daten im zentralen Warehouse gesammelt wurden, können Datenteams die Daten von Braze mit ihren bevorzugten Business Intelligence-Tools effektiv untersuchen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Fivetran-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Fivetran-Konto](https://fivetran.com/login?next=%2Fdashboard). |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen:<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][1] ab. |
| Lötende Ströme | [Braze Currents](https://www.braze.com/product/data-agility-management/currents/) sollte entweder mit Amazon S3 oder Google Cloud Storage verbunden sein. |
| Amazon S3 oder Google Cloud-Speicher | Diese Integration erfordert, dass Sie Zugang zu einem Amazon S3 oder Google Cloud Storage haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integration

Die folgende Currents-Integration wird sowohl für [Amazon S3](#setting-up-braze-currents-for-s3) als auch für [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage) unterstützt.

### Einrichten von Braze Currents für S3

#### Schritt 1: Suchen Sie Ihre externe ID {#step-one}

Klicken Sie im [Fivetran Dashboard](https://fivetran.com/dashboard) auf **\+ Connector** und wählen Sie den **Braze-Connector** aus, um das Einrichtungsformular zu starten. Wählen Sie als nächstes **Amazon S3**. Beachten Sie die hier angegebene externe ID; Sie benötigen sie, um Fivetran den Zugriff auf Ihren S3-Bucket zu ermöglichen. 

![Der Fivetran setzt die Form des Lötverbinders ein. Das für diesen Schritt benötigte externe ID-Feld befindet sich in der Mitte der Seite in einem hellgrauen Feld.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### Schritt 2: Geben Sie Fivetran Zugriff auf einen bestimmten S3-Bucket

##### Erstellen einer IAM-Richtlinie

Öffnen Sie die [Amazon IAM-Konsole](https://console.aws.amazon.com/iam/home#home) und navigieren Sie zu **Policies > Create Policy**.

![]({% image_buster /assets/img/fivetran_as3_iam.png %})

Klicken Sie anschließend auf die Registerkarte **JSON** und fügen Sie die folgende Richtlinie ein. Stellen Sie sicher, dass Sie `{your-bucket-name}` durch den Namen Ihres S3-Buckets ersetzen.

{% raw %}
```json
{
"Version": "2012-10-17",
"Statement": [
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}/*"
    },
    {
      "Effect": "Allow",
      "Action": [
"s3:Get*",
"s3:List*"
      ],
      "Resource": "arn:aws:s3:::{your-bucket-name}"
    }
  ]
}
```
{% endraw %}

Klicken Sie abschließend auf **Richtlinie überprüfen** und geben Sie der Richtlinie einen eindeutigen Namen und eine Beschreibung. Klicken Sie auf **Richtlinie erstellen**, um Ihre Richtlinie zu erstellen. 

![]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### Eine IAM-Rolle erstellen {#step-two}

Navigieren Sie in AWS zu **Rollen** und wählen Sie dann **Neue Rolle erstellen**.

![]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Wählen Sie **Anderes AWS-Konto** und geben Sie die Fivetran-Konto-ID `834469178297` an. Stellen Sie sicher, dass Sie das Kontrollkästchen **Externe ID erforderlich** aktivieren. Hier geben Sie die in Schritt 1 gefundene externe ID an.

![]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Klicken Sie dann auf **Weiter: Berechtigungen**, um die soeben erstellte Richtlinie auszuwählen.

![]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Klicken Sie auf **Weiter: Überprüfen Sie**, benennen Sie Ihre neue Rolle (z.B. Fivetran) und klicken Sie auf **Rolle erstellen**. Nachdem die Rolle erstellt wurde, klicken Sie darauf und notieren sich den angezeigten Rollen-ARN.

![Der in der Rolle aufgeführte Amazon S3 ARN.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Sie können Berechtigungen für die Rollen-ARN festlegen, die Sie für Fivetran bestimmen. Wenn Sie dieser Rolle selektive Rechte erteilen, kann Fivetran nur das synchronisieren, wozu es berechtigt ist.
{% endalert %}

#### Schritt 3: Vervollständigen Sie den Fivetran-Anschluss

Klicken Sie in Fivetran auf **\+ Connector** und wählen Sie den **Braze-Connector**, um das Einrichtungsformular zu starten. Füllen Sie in dem Formular die angegebenen Felder mit den entsprechenden Werten aus:
- `Destination schema`: Ein eindeutiger Schemaname.
- `API URL`: Ihr Braze REST API Endpunkt.
- `API Key`: Ihr Braze REST API-Schlüssel. 
- `External ID`: Die externe ID, die Sie in [Schritt 2](#step-two) der Currents-Einrichtungsanleitung festgelegt haben. Diese ID ist ein fester Wert.
- `Bucket`: Sie finden es in Ihrem Braze-Konto, indem Sie zu **Integration > Currents > [Ihr aktueller Name] > Bucket Name** navigieren.
- `Role ARN`: Die Rollen-ARN finden Sie in [Schritt 1](#step-one) der Anleitung zur aktuellen Einrichtung.

{% alert important %}
Stellen Sie sicher, dass **Amazon S3** als **Cloud-Speicher** ausgewählt ist.
{% endalert %}

Klicken Sie abschließend auf **Speichern & Testen** und Fivetran erledigt den Rest, indem es sich mit den Daten Ihres Braze-Kontos synchronisiert!

### Braze Currents für Google Cloud Storage einrichten

#### Schritt 1: Rufen Sie Ihre Fivetran-E-Mails aus Google Cloud Storage ab {#step-one2}

Klicken Sie im [Fivetran-Dashboard](https://fivetran.com/dashboard) auf **\+ Connector** und wählen Sie den **Braze-Connector** aus, um das Einrichtungsformular zu starten. Wählen Sie dann **Google Cloud-Speicher**. Notieren Sie sich die angezeigte E-Mail-Adresse.

![Der Fivetran setzt die Form des Lötverbinders ein. Das für diesen Schritt erforderliche E-Mail-Feld befindet sich in der Mitte der Seite in einem hellgrauen Feld.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### Schritt 2: Zugriff auf den Eimer gewähren

Navigieren Sie zu Ihrer [Google Storage Console](https://console.cloud.google.com/storage/browser) und wählen Sie den Bucket, mit dem Sie Braze Currents konfiguriert haben, und klicken Sie auf **Bucket-Berechtigungen bearbeiten**.

![Die in der Google Storage Console verfügbaren Buckets. Suchen Sie einen Eimer und klicken Sie auf das vertikale Drei-Punkte-Symbol, um das Dropdown-Menü zu öffnen, mit dem Sie die Eimerberechtigungen bearbeiten können.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

Als nächstes gewähren Sie `Storage Object Viewer` Zugriff auf die E-Mail aus [Schritt 1](#step-one2), indem Sie die E-Mail als Mitglied hinzufügen. Notieren Sie sich den Namen des Buckets; Sie benötigen ihn im nächsten Schritt zur Konfiguration von Fivetran.

![]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### Schritt 3: Vervollständigen Sie den Fivetran-Anschluss

Klicken Sie in Fivetran auf **\+ Connector** und wählen Sie den **Braze-Connector**, um das Einrichtungsformular zu starten. Füllen Sie in dem Formular die angegebenen Felder mit den entsprechenden Werten aus:
- `Destination schema`: Ein eindeutiger Schemaname.
- `API URL`: Ihr Braze REST API Endpunkt.
- `API Key`: Ihr Braze REST API-Schlüssel. 
- `Bucket Name`: Sie finden es in Ihrem Braze-Konto, indem Sie zu **Integration > Currents > [Ihr aktueller Name] > Bucket Name** navigieren.
- `Folder`: Sie finden es in Ihrem Braze-Konto, indem Sie zu **Integration > Currents > [Ihr aktueller Name] > Prefix** navigieren.

{% alert important %}
Stellen Sie sicher, dass **Google Cloud Storage** als **Cloud-Speicher** ausgewählt ist.
{% endalert %}

Klicken Sie abschließend auf **Speichern & Testen** und Fivetran erledigt den Rest, indem es sich mit den Daten Ihres Braze-Kontos synchronisiert!

[1]: {{site.baseurl}}/api/basics/#api-definitions