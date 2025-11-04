---
nav_title: Amazon S3
article_title: Amazon S3
alias: /partners/amazon_s3/
description: "Dieser referenzierende Artikel beschreibt die Partnerschaft zwischen Braze und Amazon S3, einem hoch skalierbaren Speichersystem, das von Amazon Serviceleistungen; Dienste angeboten wird."
page_type: partner
search_tag: Partner

---

# Amazon S3

> [Amazon S3](https://aws.amazon.com/s3/) ist ein hoch skalierbares Speichersystem, das von Amazon Serviceleistungen; Dienste angeboten wird.

{% alert important %}
Wenn Sie zwischen Cloud-Speicheranbietern wechseln, wenden Sie sich an Ihren Customer-Success-Manager von Braze, um weitere Unterstützung bei der Einrichtung und Validierung Ihrer neuen Integration zu erhalten.
{% endalert %}

Die Integration von Braze und Amazon S3 bietet zwei Strategien für die Integration:

- Nutzen Sie [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), um Ihre Daten dort zu speichern, bis Sie sie mit anderen Plattformen, Tools und Standorten verbinden möchten.
- Verwenden Sie Dashboard-Datenexporte (wie CSV-Exporte und Engagement-Berichte).

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Amazon S3-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Amazon S3-Konto. |
| Dediziertes S3-Bucket | Vor der Integration mit Amazon S3 müssen Sie ein S3-Bucket für Ihre App erstellen.<br><br>Wenn Sie bereits ein S3-Bucket haben, empfehlen wir Ihnen dennoch, ein neues Bucket speziell für Braze zu erstellen, damit Sie die Berechtigungen einschränken können. In der folgenden Anleitung erfahren Sie, wie Sie einen neuen Bucket erstellen. |
| Currents | Um Daten zurück in Amazon S3 exportieren zu können, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Erstellen eines neuen S3-Buckets

Um einen Bucket für Ihre App zu erstellen, gehen Sie wie folgt vor:

1. Öffnen Sie die [Amazon S3-Konsole](https://console.aws.amazon.com/s3/) und folgen Sie den Anweisungen, um **sich anzumelden** oder **ein Konto bei AWS zu erstellen**. 
2. Nachdem Sie sich angemeldet haben, wählen Sie **S3** aus der Kategorie **Speicherung & Zustellung von Inhalten**. 
3. Wählen Sie auf dem nächsten Bildschirm **Bucket erstellen** aus. 
4. Sie werden aufgefordert, Ihr Bucket zu erstellen und eine Region auszuwählen.

{% alert note %}
Currents unterstützt keine Buckets mit konfigurierter [Objektsperre](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html).
{% endalert %}

## Integration

Braze hat zwei verschiedene Strategien zur Integration mit Amazon S3 - eine für [Braze-Currents]({{site.baseurl}}/user_guide/data/braze_currents/) und eine für alle Dashboard-Datenexporte (wie CSV-Exporte oder Engagement-Berichte). Beide Integrationen unterstützen zwei verschiedene Authentifizierungs- oder Autorisierungsmethoden:

- [AWS geheime Zugriffsschlüsselmethode](#aws-secret-key-auth-method)
- [AWS Rolle ARN Methode](#aws-role-arn-auth-method)

## AWS Geheimschlüssel-Authentifizierungsmethode

Diese Authentifizierungsmethode generiert einen geheimen Schlüssel und eine Zugriffsschlüssel-ID, die es Braze ermöglicht, sich als Nutzer:in Ihrem AWS-Konto zu authentifizieren, um Daten in Ihren Bucket zu schreiben.

### Schritt 1: Nutzer:in erstellen {#secret-key-1}

Um Ihre ID und den geheimen Zugriffsschlüssel abzurufen, müssen Sie [in AWS eine IAM Nutzer:in und eine Administratorengruppe anlegen](https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html).

### Schritt 2: Zugangsdaten abrufen {#secret-key-2}

Nachdem Sie einen neuen Nutzer:innen angelegt haben, wählen Sie **Zugangsdaten anzeigen**, um Ihre ID und Ihren geheimen Zugangsschlüssel zu sehen. Notieren Sie diese Zugangsdaten irgendwo, oder wählen Sie den Button **Zugangsdaten herunterladen**, da Sie diese später in das Braze-Dashboard eingeben müssen.

![]({% image_buster /assets/img_archive/S3_Credentials.png %})

### Schritt 3: Richtlinie erstellen {#secret-key-3}

Navigieren Sie zu **Richtlinien** > **Erste Schritte** > **Richtlinie erstellen**, um Berechtigungen für Ihre Nutzer:innen hinzuzufügen. Wählen Sie anschließend **Eigene Richtlinie erstellen** aus. Dadurch erhalten Sie eingeschränkte Berechtigungen, so dass Braze nur auf die angegebenen Buckets zugreifen kann. 

![]({% image_buster /assets/img_archive/S3_CreatePolicy.png %})

{% alert note %}
Für den Export von Currents- und Dashboard-Daten sind unterschiedliche Richtlinien erforderlich. `s3:GetObject` ist erforderlich, damit das Backend von Braze eine Fehlerbehandlung durchführen kann.
{% endalert %}

Geben Sie den Namen einer Richtlinie Ihrer Wahl an und fügen Sie den folgenden Code-Snippet in den Abschnitt **Richtliniendokument** ein. Ersetzen Sie `INSERTBUCKETNAME` durch Ihren Bucket-Namen. Ohne diese Berechtigungen schlägt die Integration bei der Prüfung der Zugangsdaten fehl und kann nicht erstellt werden.

{% tabs %}
{% tab Braze-Currents %}
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

### Schritt 4: Richtlinie beifügen {#secret-key-4}

Nachdem Sie eine neue Richtlinie erstellt haben, gehen Sie zu **Nutzer:innen** und wählen Sie einen bestimmten Nutzer aus. Wählen Sie auf dem Tab **Berechtigungen** die Option **Richtlinie anhängen** und wählen Sie die neue Richtlinie aus, die Sie erstellt haben. Jetzt können Sie Ihre AWS-Zugangsdaten mit Ihrem Braze-Konto verknüpfen.

![]({% image_buster /assets/img_archive/S3_AttachPolicy.png %})

### Schritt 5: Verknüpfung von Braze mit AWS {#secret-key-5}

{% tabs %}
{% tab Braze-Currents %}

Gehen Sie in Braze zu **Partnerintegrationen** > **Datenexport**.

Wählen Sie dann **Create Current** und anschließend **Amazon S3 Data Export**.

Nennen Sie Ihren Current. Vergewissern Sie sich, dass im Abschnitt **Zugangsdaten** der **geheime AWS-Zugangsschlüssel** ausgewählt ist, und geben Sie dann Ihre S3-Zugangs-ID, den geheimen AWS-Zugangsschlüssel und den Namen Ihres AWS S3-Buckets in die entsprechenden Felder ein.

![]({{site.baseurl}}/assets/img/currents-s3-example.png)

{% alert warning %}
Halten Sie Ihre AWS Access Key ID und Ihren geheimen Zugangsschlüssel auf dem neuesten Stand. Wenn die Zugangsdaten Ihres Konnektors ablaufen, wird der Konnektor keine Ereignisse mehr senden. Wenn dieser Zustand länger als **48 Stunden** anhält, werden die Ereignisse des Konnektors gelöscht und die Daten gehen dauerhaft verloren.
{% endalert %}

Sie können auch die folgenden Anpassungen nach Ihren Bedürfnissen vornehmen:

- **Ordner Pfad:** Standardmäßig ist `currents` eingestellt. Wenn dieser Ordner nicht vorhanden ist, erstellt Braze ihn automatisch für Sie. 
- **Serverseitige AES-256-Verschlüsselung im Ruhezustand:** Standardmäßig ist diese Option ausgeschaltet und enthält die Kopfzeile `x-amz-server-side-encryption`.

Wählen Sie **Launch Current**, um fortzufahren.

Eine Benachrichtigung informiert Sie darüber, ob Ihre Zugangsdaten erfolgreich validiert wurden. AWS S3 sollte nun für Braze-Currents eingerichtet sein.

{% endtab %}
{% tab Dashboard Daten Export %}

Gehen Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Amazon S3**.

Vergewissern Sie sich auf der Seite **AWS-Zugangsdaten**, dass der **geheime AWS-Zugangsschlüssel** ausgewählt ist, und geben Sie dann Ihre AWS-Zugangs-ID, den geheimen AWS-Zugangsschlüssel und den Namen Ihres AWS S3-Buckets in die entsprechenden Felder ein. Wählen Sie bei der Eingabe Ihres geheimen Schlüssels zunächst **Zugangsdaten testen** aus, um sicherzustellen, dass Ihre Zugangsdaten funktionieren, und wählen Sie dann **Speichern**, wenn Sie erfolgreich waren.

![]({{site.baseurl}}/assets/img/s3_tech_partners.png)

{% alert tip %}
Sie können jederzeit neue Zugangsdaten abrufen, indem Sie zu Ihrem Nutzer:innen navigieren und in der AWS-Konsole auf dem Tab **Security Credentials** den Punkt **Create Access Key** auswählen.
{% endalert %}

Eine Benachrichtigung informiert Sie darüber, ob Ihre Zugangsdaten erfolgreich validiert wurden. AWS S3 sollte nun in Ihr Braze-Konto integriert sein.

{% endtab %}
{% endtabs %}

## AWS Rolle ARN Auth-Methode

Diese Authentifizierungsmethode generiert einen Rollen-Amazon-Ressourcennamen (ARN), der es dem Braze-Konto ermöglicht, sich als Mitglied der Rolle zu authentifizieren, die Sie zum Schreiben von Daten in Ihren Bucket erstellt haben.

### Schritt 1: Richtlinie erstellen {#role-arn-1}

Um loszulegen, melden Sie sich bei der AWS Verwaltungskonsole als Account Administrator an. Navigieren Sie zum IAM-Bereich der AWS Konsole, wählen Sie in der Navigationsleiste **Richtlinien aus** und wählen Sie **Richtlinie erstellen**.

![]({{site.baseurl}}/assets/img/create_policy_1_list.png)

{% alert note %}
Für den Export von Currents- und Dashboard-Daten sind unterschiedliche Richtlinien erforderlich. `s3:GetObject` ist erforderlich, damit das Backend von Braze eine Fehlerbehandlung durchführen kann.
{% endalert %}

Öffnen Sie den Tab **JSON** und geben Sie den folgenden Code-Snippet in den Abschnitt **Richtliniendokument** ein. Ersetzen Sie `INSERTBUCKETNAME` durch Ihren Bucket-Namen. Wählen Sie **Richtlinie überprüfen**, wenn Sie fertig sind.

{% tabs %}
{% tab Braze-Currents %}

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

Geben Sie dann der Richtlinie einen Namen und eine Beschreibung und wählen Sie **Richtlinie erstellen**.

![]({{site.baseurl}}/assets/img/create_policy_3_name.png)

![]({{site.baseurl}}/assets/img/create_policy_4_created.png)

### Schritt 2: Rolle erstellen {#role-arn-2}

Wählen Sie in demselben IAM-Bereich der Konsole **Rollen** > **Rolle erstellen**.

![]({{site.baseurl}}/assets/img/create_role_1_list.png)

Rufen Sie die ID Ihres Braze-Kontos und Ihre externe ID von Ihrem Braze-Konto ab:
- **Currents**: Gehen Sie in Braze zu **Partnerintegrationen** > **Datenexport**. Wählen Sie dann **Create Current** und anschließend **Amazon S3 Data Export**. Hier finden Sie die Bezeichner, die Sie zur Erstellung Ihrer Rolle benötigen.
- **Dashboard Daten exportieren**: Gehen Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Amazon S3**. Hier finden Sie die Bezeichner, die Sie zur Erstellung Ihrer Rolle benötigen.

Wählen Sie in der AWS-Konsole **ein anderes AWS-Konto** als SELEKTOR-Typ für die vertrauenswürdige Entität aus. Geben Sie Ihre Braze-Konto ID an, markieren Sie das Feld **Externe ID erforderlich** und geben Sie die externe ID von Braze ein. Wählen Sie nach Abschluss **Weiter** aus.

![Die S3-Seite "Rolle erstellen". Diese Seite enthält Felder für den Rollennamen, die Rollenbeschreibung, vertrauenswürdige Entitäten, Richtlinien und die Berechtigungsgrenze.]({{site.baseurl}}/assets/img/create_role_2_another.png)

### Schritt 3: Richtlinie beifügen {#role-arn-3}

Als nächstes fügen Sie der Rolle die Richtlinie hinzu, die Sie zuvor erstellt haben. Suchen Sie in der Suchleiste nach der Richtlinie, und setzen Sie ein Häkchen neben die Richtlinie, um sie anzuhängen. Wählen Sie nach Abschluss **Weiter** aus.

![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_3_attach.png)

Geben Sie der Rolle einen Namen und eine Beschreibung, und wählen Sie **Rolle erstellen**.

![Rollen-ARN]({{site.baseurl}}/assets/img/create_role_4_name.png)

Sie sollten nun Ihre neu erstellte Rolle in der Liste sehen.

### Schritt 4: Link zu Braze AWS {#role-arn-4}

In der AWS-Konsole finden Sie Ihre neu erstellte Rolle in der Liste. Wählen Sie den Namen aus, um die Details zu dieser Rolle zu öffnen.

![]({{site.baseurl}}/assets/img/create_role_5_created.png)

Achten Sie auf den **ARN der Rolle** oben auf der Seite mit der Rollenübersicht.

![]({{site.baseurl}}/assets/img/create_role_6_summary.png)

Kehren Sie zu Ihrem Braze-Konto zurück und kopieren Sie die Rollen-ARN in das dafür vorgesehene Feld.

{% tabs %}
{% tab Braze-Currents %}

Gehen Sie in Braze auf die Seite **Currents** unter **Integrationen**. Wählen Sie dann **Create Current** und wählen Sie **Amazon S3 Data Export**

![]({{site.baseurl}}/assets/img/currents-role-arn.png)

Geben Sie Ihrem Currents einen Namen. Vergewissern Sie sich dann im Abschnitt **Zugangsdaten**, dass **AWS Role ARN** ausgewählt ist, und geben Sie dann Ihre Rollen-ARN und den AWS S3 Bucket-Namen in die dafür vorgesehenen Felder ein.

Sie können auch die folgenden Anpassungen nach Ihren Bedürfnissen vornehmen:

- Ordnerpfad (Standard: `currents`)
- Serverseitige AES-256-Verschlüsselung im Ruhezustand (Standard: AUS) - Enthält den `x-amz-server-side-encryption` Header

Wählen Sie **Launch Current**, um fortzufahren. Sie erhalten eine Benachrichtigung, wenn Ihre Zugangsdaten erfolgreich validiert wurden. AWS S3 sollte nun für Braze-Currents eingerichtet sein.

{% alert important %}
Wenn Sie die Fehlermeldung "S3-Anmeldedaten sind ungültig" erhalten, kann dies daran liegen, dass Sie die Integration nach der Erstellung einer Rolle in AWS zu schnell durchgeführt haben. Warten Sie und versuchen Sie es erneut.
{% endalert %}

{% endtab %}
{% tab Dashboard Daten Export %}

Gehen Sie in Braze auf die **Technologie-Partnerseite** unter **Integrationen** und wählen Sie **Amazon S3**.

![]({{site.baseurl}}/assets/img/data-export-role-arn.png)

Vergewissern Sie sich auf der Seite **AWS-Zugangsdaten**, dass der Button **AWS Role ARN** ausgewählt ist, und geben Sie dann Ihren Rollen-ARN und den Namen Ihres AWS S3-Buckets in die entsprechenden Felder ein. Wählen Sie zunächst **Zugangsdaten testen**, um zu überprüfen, ob Ihre Zugangsdaten ordnungsgemäß funktionieren, und wählen Sie dann **Speichern**, wenn Sie erfolgreich waren.

{% alert tip %}
Sie können jederzeit neue Zugangsdaten abrufen, indem Sie zu Ihrem Nutzer:innen navigieren und auf dem Tab **Sicherheitszugangsdaten** in der AWS-Konsole **Zugriffsschlüssel erstellen** auswählen.
{% endalert %}

Eine Benachrichtigung informiert Sie darüber, ob Ihre Zugangsdaten erfolgreich validiert wurden. AWS S3 sollte nun in Ihr Braze-Konto integriert sein.

{% endtab %}
{% endtabs %}

## Verhalten beim Exportieren

Nutzer:innen, die eine Lösung zur Speicherung von Daten in der Cloud integriert haben und versuchen, APIs, Dashboard-Berichte oder CSV-Berichte zu exportieren, werden folgende Probleme haben:

- Alle API-Exporte geben keine Download-URL im Antwortkörper zurück und müssen über den Datenspeicher abgerufen werden.
- Alle Dashboard-Berichte und CSV-Berichte werden zum Download an die E-Mail des Nutzers:innen gesendet (keine Speicherberechtigung erforderlich) und auf dem Datenspeicher gesichert. 

## Mehrere Konnektoren

Wenn Sie mehr als einen Currents Konnektor erstellen möchten, um ihn an Ihr S3-Bucket zu senden, können Sie die gleichen Zugangsdaten verwenden, müssen aber für jeden einen anderen Ordnerpfad angeben. Diese können in demselben Workspace erstellt werden oder aufgeteilt und in mehreren Workspaces erstellt werden. Sie haben auch die Möglichkeit, für jede Integration eine eigene Richtlinie zu erstellen, oder eine Richtlinie zu erstellen, die beide Integrationen abdeckt. 

Wenn Sie dasselbe S3-Bucket sowohl für Currents als auch für Datenexporte verwenden möchten, müssen Sie zwei separate Richtlinien erstellen, da jede Integration unterschiedliche Berechtigungen erfordert.


