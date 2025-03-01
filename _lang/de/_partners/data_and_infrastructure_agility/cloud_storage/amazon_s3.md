---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Amazon S3, einem hochskalierbaren Speichersystem, das von Amazon Web Services angeboten wird."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) ist ein hoch skalierbares Speichersystem, das von Amazon Web Services angeboten wird.

Die Integration von Braze und Amazon S3 nutzt [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), um Braze-Daten an Ihre S3-Instanz zu senden. So können Sie Daten dort speichern, bis Sie sie mit anderen Plattformen, Tools und Standorten verbinden möchten. Sie können die Integration auch über Dashboard-Datenexporte vornehmen. Folgen Sie den Anweisungen auf dieser Seite, um mit Ihrer AWS S3-Integration zu beginnen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Amazon S3-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Amazon S3-Konto. |
| Dedizierter S3 Bucket | Bevor Sie die Integration mit Amazon S3 vornehmen, müssen Sie einen S3-Bucket für Ihre App erstellen.<br><br>Wenn Sie bereits einen S3-Bucket haben, empfehlen wir Ihnen dennoch, einen neuen Bucket speziell für Braze zu erstellen, damit Sie die Berechtigungen einschränken können. Lesen Sie die folgende Anleitung, wie Sie einen neuen Eimer erstellen. |
| Currents | Um Daten zurück in Amazon S3 exportieren zu können, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Erstellen Sie einen neuen S3 Bucket

Um einen Bucket für Ihre App zu erstellen, öffnen Sie die [Amazon S3-Konsole](https://console.aws.amazon.com/s3/) und folgen Sie den Anweisungen zum **Anmelden** oder **Erstellen eines Kontos bei AWS**. Nachdem Sie sich angemeldet haben, wählen Sie **S3** aus der Kategorie **Storage & Content Delivery**. Wählen Sie auf dem nächsten Bildschirm **Bucket erstellen**. Sie werden aufgefordert, Ihren Bucket zu erstellen und eine Region auszuwählen.

## Integration

Braze hat zwei verschiedene Integrationsstrategien mit Amazon S3 - eine für [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/) und eine für alle Dashboard-Datenexporte (CSV-Exporte, Engagement-Berichte usw.). Beide Integrationen unterstützen zwei verschiedene Authentifizierungs-/Autorisierungsmethoden:

- [AWS-Methode für den geheimen Zugriffsschlüssel](#aws-secret-key-auth-method)
- [AWS-Rolle ARN-Methode](#aws-role-arn-auth-method)

## AWS Geheimschlüssel-Authentifizierungsmethode

Diese Authentifizierungsmethode generiert einen geheimen Schlüssel und eine Zugriffsschlüssel-ID, die es Braze ermöglicht, sich als Benutzer Ihres AWS-Kontos zu authentifizieren, um Daten in Ihren Bucket zu schreiben.

### Schritt 1: Benutzer erstellen {#secret-key-1}

Um Ihre Zugangsschlüssel-ID und Ihren geheimen Zugangsschlüssel abzurufen, müssen Sie [einen IAM-Benutzer und eine Administratorengruppe in AWS anlegen](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Schritt 2: Anmeldeinformationen erhalten {#secret-key-2}

Nachdem Sie einen neuen Benutzer erstellt haben, klicken Sie auf **Benutzersicherheitsnachweise anzeigen**, um Ihre Zugriffsschlüssel-ID und Ihren geheimen Zugriffsschlüssel zu sehen. Notieren Sie sich diese Anmeldedaten irgendwo, oder klicken Sie auf die Schaltfläche **Anmeldedaten herunterladen**, da Sie diese später in das Braze-Dashboard eingeben müssen.

![][11]

### Schritt 3: Richtlinie erstellen {#secret-key-3}

Navigieren Sie zu **Richtlinien > Erste Schritte > Richtlinie erstellen**, um Berechtigungen für Ihren Benutzer hinzuzufügen. Wählen Sie anschließend **Eigene Richtlinie erstellen**. Dadurch erhalten Sie eingeschränkte Berechtigungen, so dass Braze nur auf die angegebenen Buckets zugreifen kann. 

![][12]

{% alert note %}
Für "Currents" und "Dashboard-Datenexport" sind unterschiedliche Richtlinien erforderlich.
{% endalert %}

Geben Sie den Namen einer Richtlinie Ihrer Wahl an und fügen Sie den folgenden Codeschnipsel in den Abschnitt **Richtliniendokument** ein. Stellen Sie sicher, dass Sie `INSERTBUCKETNAME` durch den Namen Ihres Eimers ersetzen. Ohne diese Berechtigungen wird die Integration bei der Prüfung der Anmeldeinformationen scheitern und nicht erstellt werden.

{% tabs %}
{% tab Lötende Ströme %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```
{% endtab %}
{% tab Dashboard Daten Export %}
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME*", "arn:aws:s3:::INSERTBUCKETNAME/", "arn:aws:s3:::INSERTBUCKETNAME"]
        }
    ]
}
```
{% endtab %}
{% endtabs %}

### Schritt 4: Police beifügen {#secret-key-4}

Nachdem Sie eine neue Richtlinie erstellt haben, navigieren Sie zu **Benutzer** und klicken Sie auf Ihren spezifischen Benutzer. Klicken Sie auf der Registerkarte **Berechtigungen** auf **Richtlinie anhängen** und wählen Sie die neue Richtlinie, die Sie erstellt haben. Sie sind nun bereit, Ihre AWS-Anmeldedaten mit Ihrem Braze-Konto zu verknüpfen.

![][13]

### Schritt 5: Verknüpfung von Braze mit AWS {#secret-key-5}

{% tabs %}
{% tab Lötende Ströme %}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Datenexport**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Currents** unter **Integrationen**.
{% endalert %}

Klicken Sie anschließend auf **Aktuelle erstellen** und wählen Sie **Amazon S3 Datenexport**.

Benennen Sie Ihren Current und vergewissern Sie sich im Abschnitt **Credentials**, dass das Optionsfeld **AWS Secret Access Key** aktiviert ist. Geben Sie dann Ihre S3-Zugangs-ID, Ihren geheimen AWS-Zugangsschlüssel und den Namen Ihres AWS S3-Buckets in die entsprechenden Felder ein.

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Halten Sie Ihre AWS-Zugangsschlüssel-ID und Ihren geheimen Zugangsschlüssel auf dem neuesten Stand. Wenn die Anmeldeinformationen Ihres Connectors ablaufen, wird der Connector keine Ereignisse mehr senden. Wenn dies länger als **48 Stunden** andauert, werden die Ereignisse des Connectors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

Sie können auch die folgenden Anpassungen nach Ihren Wünschen vornehmen:

- **Ordner Pfad:** Die Standardeinstellung ist `currents`. Wenn dieser Ordner nicht existiert, wird Braze ihn automatisch für Sie erstellen. 
- **Server-seitige AES-256-Verschlüsselung im Ruhezustand:** Die Standardeinstellung ist AUS und enthält die Kopfzeile `x-amz-server-side-encryption`.

Klicken Sie auf **Aktuell starten**, um fortzufahren.

Eine Benachrichtigung informiert Sie darüber, ob Ihre Anmeldedaten erfolgreich validiert wurden. AWS S3 sollte nun für Braze Currents eingerichtet sein.

{% endtab %}
{% tab Dashboard Daten Export %}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und klicken Sie auf **Amazon S3**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Vergewissern Sie sich auf der Seite AWS Credentials, dass das Optionsfeld **AWS Secret Access Key** aktiviert ist, und geben Sie dann Ihre AWS-Zugangs-ID, Ihren geheimen AWS-Zugangsschlüssel und den Namen Ihres AWS S3-Buckets in die entsprechenden Felder ein. Klicken Sie bei der Eingabe Ihres geheimen Schlüssels zunächst auf **Anmeldeinformationen testen**, um sicherzustellen, dass Ihre Anmeldeinformationen funktionieren, und klicken Sie dann auf **Speichern**, wenn Sie erfolgreich waren.

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Sie können jederzeit neue Anmeldeinformationen abrufen, indem Sie zu Ihrem Benutzer navigieren und in der AWS-Konsole auf der Registerkarte **Sicherheitsanmeldeinformationen** auf **Zugangsschlüssel erstellen** klicken.
{% endalert %}

Eine Benachrichtigung informiert Sie darüber, ob Ihre Anmeldedaten erfolgreich validiert wurden. AWS S3 sollte nun in Ihr Braze-Konto integriert sein.

{% endtab %}
{% endtabs %}

## AWS-Rolle ARN Auth-Methode

Diese Authentifizierungsmethode erzeugt einen Rollen-Amazon-Ressourcennamen (ARN), der es dem Amazon-Konto von Braze ermöglicht, sich als Mitglied der Rolle zu authentifizieren, die Sie zum Schreiben von Daten in Ihren Bucket erstellt haben.

### Schritt 1: Richtlinie erstellen {#role-arn-1}

Um loszulegen, melden Sie sich bei der AWS-Verwaltungskonsole als Kontoverwalter an. Navigieren Sie zum Abschnitt IAM der AWS-Konsole, klicken Sie in der Navigationsleiste auf **Policies** und dann auf **Create Policy**.

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Für "Currents" und "Dashboard-Datenexport" sind unterschiedliche Richtlinien erforderlich.
{% endalert %}

Öffnen Sie die Registerkarte **JSON** und geben Sie den folgenden Codeschnipsel in den Abschnitt **Policy Document** ein. Stellen Sie sicher, dass Sie `INSERTBUCKETNAME` durch den Namen Ihres Eimers ersetzen. Klicken Sie auf **Richtlinie überprüfen**, wenn Sie fertig sind.

{% tabs %}
{% tab Lötende Ströme %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% tab Dashboard Daten Export %}

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": ["s3:ListBucket", "s3:GetBucketLocation"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME"]
        },
        {
            "Effect": "Allow",
            "Action": ["s3:PutObject", "s3:GetObject","s3:DeleteObject"],
            "Resource": ["arn:aws:s3:::INSERTBUCKETNAME/*"]
        }
    ]
}
```

{% endtab %}
{% endtabs %}

Geben Sie dann der Richtlinie einen Namen und eine Beschreibung und klicken Sie auf **Richtlinie erstellen**.

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Schritt 2: Rolle erstellen {#role-arn-2}

Klicken Sie im gleichen IAM-Bereich der Konsole auf **Rollen > Rolle erstellen**.

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Rufen Sie Ihre Braze-Konto-ID und Ihre externe ID von Ihrem Braze-Konto ab:
- **Ströme**: Navigieren Sie in Braze zu **Partnerintegrationen** > **Datenexport**. Klicken Sie anschließend auf **Aktuelle erstellen** und wählen Sie **Amazon S3 Datenexport**. Hier finden Sie die Identifikatoren, die Sie zur Erstellung Ihrer Rolle benötigen.
- **Export von Dashboard-Daten**: Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und klicken Sie auf **Amazon S3**. Hier finden Sie die Identifikatoren, die Sie zur Erstellung Ihrer Rolle benötigen.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, befinden sich diese Seiten an einer anderen Stelle:<br>- **Currents** finden Sie unter **Integrationen** > **Currents** <br>- **Technology Partners** befindet sich unter **Integrationen**
{% endalert %}

Zurück in der AWS-Konsole wählen Sie **Anderes AWS-Konto** als Auswahltyp für die vertrauenswürdige Entität. Geben Sie Ihre Braze-Konto-ID an, markieren Sie das Feld **Externe ID erforderlich** und geben Sie die externe Braze-ID ein. Klicken Sie auf **Weiter**, wenn Sie fertig sind.

![Die S3-Seite "Rolle erstellen". Diese Seite enthält Felder für den Rollennamen, die Rollenbeschreibung, vertrauenswürdige Entitäten, Richtlinien und die Berechtigungsgrenze.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Schritt 3: Police beifügen {#role-arn-3}

Als Nächstes verknüpfen Sie die zuvor erstellte Richtlinie mit der Rolle. Suchen Sie die Police in der Suchleiste und setzen Sie ein Häkchen neben die Police, um sie anzuhängen. Klicken Sie auf **Weiter**, wenn Sie fertig sind.

![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Geben Sie der Rolle einen Namen und eine Beschreibung, und klicken Sie auf **Rolle erstellen**.

![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

Sie sollten nun Ihre neu erstellte Rolle in der Liste sehen.

### Schritt 4: Link zu Braze AWS {#role-arn-4}

In der AWS-Konsole finden Sie Ihre neu erstellte Rolle in der Liste. Klicken Sie auf den Namen, um die Details zu dieser Rolle zu öffnen.

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

Achten Sie auf den **ARN der Rolle** oben auf der Seite mit der Rollenübersicht.

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Kehren Sie zu Ihrem Braze-Konto zurück und kopieren Sie die Rollen-ARN in das dafür vorgesehene Feld.

{% tabs %}
{% tab Lötende Ströme %}

Navigieren Sie in Braze zur Seite **Currents** unter **Integrationen**. Klicken Sie anschließend auf **Aktuelle erstellen** und wählen Sie **Amazon S3 Data Export**

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Geben Sie Ihrem Strom einen Namen. Vergewissern Sie sich dann im Abschnitt **Credentials**, dass das Optionsfeld **AWS Role ARN** ausgewählt ist, und geben Sie dann Ihren Rollen-ARN und den Namen Ihres AWS S3-Buckets in die entsprechenden Felder ein.

Sie können auch die folgenden Anpassungen nach Ihren Wünschen vornehmen:

- Ordnerpfad (Standardeinstellung: `currents`)
- Serverseitige AES-256-Verschlüsselung im Ruhezustand (Standardeinstellung: OFF) - Enthält den `x-amz-server-side-encryption` Header

Klicken Sie auf **Aktuell starten**, um fortzufahren.

Eine Benachrichtigung informiert Sie darüber, ob Ihre Anmeldedaten erfolgreich validiert wurden. AWS S3 sollte nun für Braze Currents eingerichtet sein.

{% alert important %}
Wenn Sie die Fehlermeldung "S3-Anmeldeinformationen sind ungültig" erhalten, kann dies daran liegen, dass Sie sich nach der Erstellung einer Rolle in AWS zu schnell integriert haben. Warten Sie und versuchen Sie es erneut.
{% endalert %}

{% endtab %}
{% tab Dashboard Daten Export %}

Navigieren Sie in Braze zur Seite **Technologiepartner** unter **Integrationen** und klicken Sie auf **Amazon S3**.

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Vergewissern Sie sich auf der Seite **AWS Credentials**, dass das Optionsfeld **AWS Role ARN** ausgewählt ist, und geben Sie dann Ihren Rollen-ARN und den Namen Ihres AWS S3-Buckets in die entsprechenden Felder ein. Klicken Sie zunächst auf **Anmeldedaten testen**, um sicherzustellen, dass Ihre Anmeldedaten richtig funktionieren, und klicken Sie dann auf **Speichern**, wenn Sie erfolgreich waren.

{% alert tip %}
Sie können jederzeit neue Anmeldeinformationen abrufen, indem Sie zu Ihrem Benutzer navigieren und auf der Registerkarte **Sicherheitsanmeldeinformationen** in der AWS-Konsole auf **Zugangsschlüssel erstellen** klicken.
{% endalert %}

Eine Benachrichtigung informiert Sie darüber, ob Ihre Anmeldedaten erfolgreich validiert wurden. AWS S3 sollte nun in Ihr Braze-Konto integriert sein.

{% endtab %}
{% endtabs %}

## Verhalten beim Exportieren

Benutzer, die eine Cloud-Datenspeicherlösung integriert haben und versuchen, APIs, Dashboard-Berichte oder CSV-Berichte zu exportieren, haben folgende Probleme:

- Alle API-Exporte geben keine Download-URL im Antwortkörper zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail des Benutzers gesendet (keine Speicherberechtigungen erforderlich) und auf dem Datenspeicher gesichert. 

## Mehrere Anschlüsse

Wenn Sie mehr als einen Currents-Connector erstellen möchten, um ihn an Ihren S3-Bucket zu senden, können Sie dieselben Anmeldedaten verwenden, müssen aber für jeden einen anderen Ordnerpfad angeben. Diese können in demselben Arbeitsbereich erstellt werden oder aufgeteilt und in mehreren Arbeitsbereichen erstellt werden. Sie haben auch die Möglichkeit, für jede Integration eine eigene Richtlinie zu erstellen, oder eine Richtlinie zu erstellen, die beide Integrationen abdeckt. 

Wenn Sie dasselbe S3-Bucket sowohl für Currents als auch für Datenexporte verwenden möchten, müssen Sie zwei separate Richtlinien erstellen, da jede Integration unterschiedliche Berechtigungen erfordert.


[11]: {% image_buster /assets/img_archive/S3_Credentials.png %}
[12]: {% image_buster /assets/img_archive/S3_CreatePolicy.png %}
[13]: {% image_buster /assets/img_archive/S3_AttachPolicy.png %}
