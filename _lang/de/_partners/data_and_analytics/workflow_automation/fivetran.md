---
nav_title: Fivetran
article_title: Fivetran
alias: /partners/fivetran/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Fivetran, einem Tool zur Automatisierung von Arbeitsabläufen, das Sie bei der datengestützten Entscheidungsfindung unterstützen kann, indem es Ihnen abfragefertige Daten in Ihrem Cloud Warehouse zustellt."
page_type: partner
search_tag: Partner
tool: Currents

---

# Fivetran

> [Fivetran](https://fivetran.com/) ist eine weltweit anerkannte Marke, deren auf Analysten ausgerichtete Produkte und vollständig verwaltete Pipelines datengestützte Entscheidungen ermöglichen, indem sie Ihnen abfragefertige Daten in Ihr Cloud Warehouse zustellen.

Die Integration von Braze und Fivetran erlaubt es Nutzern:innen, eine wartungsfreie Pipeline zu erstellen, die es Ihnen ermöglicht, Braze-Daten zu sammeln und zu analysieren, indem Sie alle Ihre Anwendungen und Datenbanken mit einem zentralen Warehouse verbinden. Nachdem die Daten im zentralen Data Warehouse gesammelt wurden, können die Teams die Daten von Braze mithilfe ihrer bevorzugten Business-Intelligence-Tools effektiv untersuchen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Fivetran Konto | Sie benötigen ein [Fivetran-Konto](https://fivetran.com/login?next=%2Fdashboard), um die Vorteile dieser Partnerschaft zu nutzen. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen:<br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#api-definitions) ab. |
| Braze-Currents | [Braze-Currents](https://www.braze.com/product/data-agility-management/currents/) sollte entweder mit Amazon S3 oder Google Cloud Storage verbunden sein. |
| Amazon S3 oder Google Cloud Storage | Diese Integration setzt voraus, dass Sie Zugang zu einem Amazon S3 oder Google Cloud Storage haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Integration

Die folgende Currents-Integration wird sowohl für [Amazon S3](#setting-up-braze-currents-for-s3) als auch für [Google Cloud Storage](#setting-up-braze-currents-for-google-cloud-storage) unterstützt.

### Einrichten von Braze-Currents für S3

#### Schritt 1: Suchen Sie Ihre externe ID {#step-one}

Wählen Sie im [Fivetran Dashboard](https://fivetran.com/dashboard) **\+ Konnektor** und dann den **Braze** Konnektor aus, um das Einrichtungsformular zu starten. Als nächstes wählen Sie **Amazon S3** aus. Beachten Sie die hier angegebene externe ID; Sie benötigen sie, um Fivetran den Zugriff auf Ihr S3-Bucket zu ermöglichen. 

![Der Fivetran richtet Braze Konnektoren ein. Das für diesen Schritt benötigte Feld für die externe ID befindet sich in der Mitte der Seite in einem hellgrauen Feld.]({% image_buster /assets/img/fivetran_braze_setupform_as3.png %})

#### Schritt 2: Geben Sie Fivetran Zugriff auf ein bestimmtes S3-Bucket

##### Erstellen einer IAM-Richtlinie

Öffnen Sie die [Amazon IAM-Konsole](https://console.aws.amazon.com/iam/home#home) und navigieren Sie zu **Policies > Create Policy**.

![Amazon IAM-Konsole mit einer Liste von Richtlinien.]({% image_buster /assets/img/fivetran_as3_iam.png %})

Als nächstes öffnen Sie den Tab **JSON** und fügen die folgende Richtlinie ein. Stellen Sie sicher, dass Sie `{your-bucket-name}` durch den Namen Ihres S3-Buckets ersetzen.

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

Wählen Sie abschließend **Richtlinie überprüfen** aus und geben Sie der Richtlinie einen eindeutigen Namen und eine Beschreibung. Wählen Sie **Richtlinie erstellen**, um Ihre Richtlinie zu erstellen. 

![Felder für den Namen der Richtlinie und eine Beschreibung.]({% image_buster /assets/img/fivetran_iam_policy_meta.png %})

##### Eine IAM-Rolle erstellen {#step-two}

Navigieren Sie in AWS zu **Rollen** und wählen Sie dann **Neue Rolle erstellen**.

![Die Seite "Rollen" mit dem Button zum Erstellen einer neuen Rolle.]({% image_buster /assets/img/fivetran_iam_new_role.png %})

Wählen Sie **Anderes AWS Konto** und geben Sie die ID des Fivetran Kontos `834469178297` an. Stellen Sie sicher, dass Sie das Kontrollkästchen **Externe ID erforderlich** aktivieren. Hier geben Sie die externe ID an, die Sie in Schritt 1 gefunden haben.

![Das Feld zur Eingabe Ihrer "Konto-ID", ein Kontrollkästchen, um die externe ID zu verlangen, und ein leeres Textfeld zur Eingabe Ihrer "externen ID".]({% image_buster /assets/img/fivetran_another_aws_account.png %})

Wählen Sie dann **aus: Berechtigungen** können Sie die soeben erstellte Richtlinie auswählen.

![Liste der Richtlinien.]({% image_buster /assets/img/fivetran_as3_select_policy.png %})

Wählen Sie **Weiter: Überprüfen Sie**, benennen Sie Ihre neue Rolle (z.B. Fivetran) und wählen Sie **Rolle erstellen**. Nachdem die Rolle erstellt wurde, wählen Sie sie aus und notieren Sie sich den angezeigten ARN der Rolle.

![Der in der Rolle aufgeführte Amazon S3 ARN.]({% image_buster /assets/img/fivetran_iam_role_arn.png %})

{% alert note %}
Sie können Berechtigungen für den Rollen-ARN festlegen, den Sie für Fivetran bestimmen. Wenn Sie dieser Rolle selektive Berechtigungen erteilen, kann Fivetran nur das synchronisieren, wozu er berechtigt ist.
{% endalert %}

#### Schritt 3: Vervollständigen Sie den Fivetran Konnektor

Wählen Sie in Fivetran **\+ Konnektor** und dann den Konnektor **Braze** aus, um das Einrichtungsformular zu starten. Füllen Sie in dem Formular die angegebenen Felder mit den entsprechenden Werten aus:
- `Destination schema`: Ein eindeutiger Schemaname.
- `API URL`: Ihr Braze REST API Endpunkt.
- `API Key`: Ihr Braze REST API-Schlüssel. 
- `External ID`: Die externe ID, die in [Schritt 2](#step-two) der Currents Einrichtungsanweisungen festgelegt wurde. Diese ID ist ein fester Wert.
- `Bucket`: Sie finden es in Ihrem Braze-Konto, indem Sie zu **Partnerintegrationen** > **Datenexport** > Ihr aktueller Name navigieren.
- `Role ARN`: Die Rollen-ARN finden Sie in [Schritt 1](#step-one) der Anleitung zur Einrichtung von Currents.

{% alert important %}
Stellen Sie sicher, dass **Amazon S3** als **Cloud-Speicher** ausgewählt ist.
{% endalert %}

Wählen Sie schließlich **Speichern & Testen** aus, und Fivetran erledigt den Rest, indem es die Daten aus Ihrem Braze-Konto synchronisiert!

### Einrichten von Braze-Currents für Google Cloud Storage

#### Schritt 1: Rufen Sie Ihre E-Mails von Fivetran über Google Cloud Storage ab {#step-one2}

Wählen Sie im [Fivetran-Dashboard](https://fivetran.com/dashboard) **\+ Konnektor** und dann den **Braze** Konnektor aus, um das Einrichtungsformular zu starten. Wählen Sie dann **Google Cloud Storage** aus. Notieren Sie sich die angezeigte E-Mail Adresse.

![Der Fivetran richtet Braze Konnektoren ein. Das für diesen Schritt erforderliche E-Mail-Feld befindet sich in der Mitte der Seite in einem hellgrauen Feld.]({% image_buster /assets/img/fivetran_braze_setupform_gcs.png %})

#### Schritt 2: Bucket-Zugriff gewähren

Navigieren Sie zu Ihrer [Google Storage Console](https://console.cloud.google.com/storage/browser), wählen Sie den Bucket aus, für den Sie Braze-Currents konfiguriert haben, und wählen Sie **Bucket-Berechtigungen bearbeiten**.

![Die in der Google Storage Console verfügbaren Buckets. Suchen Sie einen Bucket und wählen Sie das vertikale Symbol mit den drei Punkten aus, um die Dropdown-Öffnung zu öffnen, mit der Sie die Bucket-Berechtigungen bearbeiten können.]({% image_buster /assets/img/fivetran_edit_bucket_permissions_gcs.png %})

Als nächstes gewähren Sie `Storage Object Viewer` Zugriff auf die E-Mail aus [Schritt 1](#step-one2), indem Sie die E-Mail als Mitglied hinzufügen. Notieren Sie sich den Bucket-Namen; Sie benötigen ihn im nächsten Schritt, um Fivetran zu konfigurieren.

![Bucket mit Berechtigungen.]({% image_buster /assets/img/fivetran_add_members_gcs.png %})

#### Schritt 3: Vervollständigen Sie den Fivetran Konnektor

Wählen Sie in Fivetran **\+ Konnektor** und dann den Konnektor **Braze** aus, um das Einrichtungsformular zu starten. Füllen Sie in dem Formular die angegebenen Felder mit den entsprechenden Werten aus:
- `Destination schema`: Ein eindeutiger Schemaname.
- `API URL`: Ihr Braze REST API Endpunkt.
- `API Key`: Ihr Braze REST API-Schlüssel. 
- `Bucket Name`: Sie finden es in Ihrem Braze-Konto, indem Sie zu **Partnerintegrationen** > **Datenexport** > Ihr aktueller Name navigieren.
- `Folder`: Sie finden es in Ihrem Braze-Konto, indem Sie zu **Partnerintegrationen** > **Datenexport** > Ihr aktueller Name navigieren.

{% alert important %}
Stellen Sie sicher, dass **Google Cloud Storage** als **Cloud-Speicher** ausgewählt ist.
{% endalert %}

Wählen Sie schließlich **Speichern & Testen** aus, und Fivetran erledigt den Rest, indem es die Daten aus Ihrem Braze-Konto synchronisiert!

